#!/usr/bin/env python3
"""
parallel_upload.py — One worker in a matrix. Takes its slice of missing.json,
downloads from source, uploads to ChemiCloud via cPanel API. Server is the
source of truth — no progress.json needed.

Env:
  SHARD_INDEX, SHARD_TOTAL  — which slice of missing.json this runner handles
  CPANEL_HOST, CPANEL_USER, CPANEL_TOKEN, DEPLOY_DIR  — upload target
"""
import os, re, json, time, ssl, uuid, random, zipfile
import urllib.request, urllib.parse, urllib.error
from pathlib import Path

SHARD_INDEX  = int(os.environ.get("SHARD_INDEX", "0"))
SHARD_TOTAL  = int(os.environ.get("SHARD_TOTAL", "1"))
CPANEL_HOST  = os.environ["CPANEL_HOST"]
CPANEL_USER  = os.environ["CPANEL_USER"]
CPANEL_TOKEN = os.environ["CPANEL_TOKEN"]
DEPLOY_DIR   = os.environ["DEPLOY_DIR"]
ORDERS_PATH  = f"{DEPLOY_DIR}/AI-legal-research/orders"

REPO_ROOT  = Path(__file__).parent.parent
MISSING_FILE = REPO_ROOT / "missing.json"

_HOST_DELAY = {"www.damiencharlotin.com": 3.0}
DEFAULT_DELAY = 1.5
UPLOAD_DELAY  = 0.4

_ssl_ctx = ssl.create_default_context()
_ssl_ctx.check_hostname = False
_ssl_ctx.verify_mode    = ssl.CERT_NONE

_BASE = f"https://{CPANEL_HOST}:2083/execute"
_AUTH = {"Authorization": f"cpanel {CPANEL_USER}:{CPANEL_TOKEN}",
         "Content-Type":  "application/x-www-form-urlencoded"}

_DOWNLOAD_HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"),
    "Accept":          "application/pdf,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection":      "keep-alive",
    "Referer":         "https://www.damiencharlotin.com/hallucinations/",
}

_last_req = {}
_blocked_hosts = set()

def _uapi(ep, params, timeout=60):
    data = urllib.parse.urlencode(params).encode()
    req  = urllib.request.Request(f"{_BASE}/{ep}", data=data, headers=_AUTH)
    with urllib.request.urlopen(req, context=_ssl_ctx, timeout=timeout) as r:
        return json.load(r)

def _save_text(filename, content, remote_dir):
    res = _uapi("Fileman/save_file_content", {
        "dir": remote_dir, "file": filename, "content": content,
        "from_charset": "UTF-8", "to_charset": "UTF-8",
    })
    return res.get("status") == 1

def _mkdir(remote_dir):
    try: _uapi("Fileman/mkdir", {"path": remote_dir})
    except Exception: pass

def _upload_zip(zip_path, remote_dir, retries=3):
    for attempt in range(1, retries+1):
        boundary = uuid.uuid4().hex.encode()
        raw = zip_path.read_bytes()
        body = (
            b"--" + boundary + b"\r\n"
            b'Content-Disposition: form-data; name="dir"\r\n\r\n' + remote_dir.encode() +
            b"\r\n--" + boundary + b"\r\n"
            b'Content-Disposition: form-data; name="overwrite"\r\n\r\n1\r\n'
            b"--" + boundary + b"\r\n"
            b'Content-Disposition: form-data; name="file-1"; filename="deploy.zip"\r\n'
            b"Content-Type: application/zip\r\n\r\n" + raw +
            b"\r\n--" + boundary + b"--\r\n"
        )
        req = urllib.request.Request(
            f"https://{CPANEL_HOST}:2083/execute/Fileman/upload_files",
            data=body,
            headers={**_AUTH, "Content-Type": f"multipart/form-data; boundary={boundary.decode()}"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, context=_ssl_ctx, timeout=300) as r:
                res = json.load(r)
            if res.get("status") == 1: return True
            print(f"    ZIP attempt {attempt} failed: {res.get('errors', res)}", flush=True)
        except Exception as e:
            print(f"    ZIP attempt {attempt} error: {e}", flush=True)
        if attempt < retries: time.sleep(5*attempt)
    return False

def upload_pdf(pdf_bytes, filename, remote_dir, web_sub):
    tmp_pdf = Path(f"/tmp/{uuid.uuid4().hex}_{filename}")
    tmp_pdf.write_bytes(pdf_bytes)
    tmp_zip = Path(f"/tmp/{uuid.uuid4().hex}.zip")
    with zipfile.ZipFile(tmp_zip, "w", zipfile.ZIP_STORED) as zf:
        zf.write(tmp_pdf, filename)
    tmp_pdf.unlink()
    if not _upload_zip(tmp_zip, remote_dir):
        tmp_zip.unlink(missing_ok=True); return False
    tmp_zip.unlink(missing_ok=True)
    time.sleep(UPLOAD_DELAY)

    tok = "".join(random.choices("abcdef0123456789", k=12))
    ext = f"_x_{tok}.php"
    php = (
        "<?php $d=__DIR__;$z=new ZipArchive;"
        "$r=$z->open($d.'/deploy.zip');"
        "if($r===true){$z->extractTo($d);$z->close();"
        "unlink($d.'/deploy.zip');unlink(__FILE__);echo 'OK';}"
        "else{http_response_code(500);echo 'FAIL:'.$r;} ?>"
    )
    if not _save_text(ext, php, remote_dir): return False

    php_url = f"https://kameir.com/{web_sub}/{ext}"
    for att in range(1, 4):
        try:
            with urllib.request.urlopen(php_url, context=_ssl_ctx, timeout=120) as r:
                body = r.read().decode().strip()
            if body == "OK": return True
            print(f"    PHP attempt {att}: {body[:100]}", flush=True)
        except Exception as e:
            print(f"    PHP attempt {att} error: {e}", flush=True)
        time.sleep(3)
    _uapi("Fileman/trash", {"path": f"/{remote_dir}/{ext}"})
    _uapi("Fileman/trash", {"path": f"/{remote_dir}/deploy.zip"})
    return False

def download_pdf(url):
    host_m = re.match(r"https?://([^/]+)", url)
    key = host_m.group(1) if host_m else url
    if key in _blocked_hosts:
        print("    Skipping (host blocked this session)", flush=True)
        return None
    delay = _HOST_DELAY.get(key, DEFAULT_DELAY)
    since = time.time() - _last_req.get(key, 0)
    if since < delay: time.sleep(delay - since)

    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(url, headers=_DOWNLOAD_HEADERS)
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            _last_req[key] = time.time()
            if len(data) < 500:
                print(f"    Too small ({len(data)}B) on attempt {attempt}", flush=True)
                time.sleep(5); continue
            return data
        except urllib.error.HTTPError as e:
            _last_req[key] = time.time()
            if e.code in (403, 429):
                print(f"    HTTP {e.code} — marking {key} blocked for this session", flush=True)
                _blocked_hosts.add(key); return None
            print(f"    Download attempt {attempt}: HTTP {e.code}", flush=True)
            time.sleep(7*attempt)
        except Exception as e:
            print(f"    Download attempt {attempt}: {e}", flush=True)
            time.sleep(7*attempt)
    _last_req[key] = time.time()
    return None

def main():
    missing = json.loads(MISSING_FILE.read_text())
    # Stable shard: deterministic by index modulo total
    my_slice = [m for i, m in enumerate(missing) if i % SHARD_TOTAL == SHARD_INDEX]
    print(f"Shard {SHARD_INDEX}/{SHARD_TOTAL}: handling {len(my_slice)} of {len(missing)} missing", flush=True)

    uploaded = failed = skipped = 0
    for i, item in enumerate(my_slice, 1):
        slug    = item["slug"]
        url     = item["source_url"]
        folder  = item["folder"]
        fname   = item["fname"]
        web_sub = f"AI-legal-research/orders/{folder}"
        rem_dir = f"{ORDERS_PATH}/{folder}"

        print(f"\n[{i}/{len(my_slice)}] {folder}/{fname[:60]}", flush=True)

        host_m = re.match(r"https?://([^/]+)", url)
        host = host_m.group(1) if host_m else ""
        if host in _blocked_hosts:
            print("  ⊘ host blocked — skipping rest", flush=True)
            skipped += 1
            continue

        pdf = download_pdf(url)
        if pdf is None:
            failed += 1; continue
        print(f"  ↓ {len(pdf):,} bytes", flush=True)

        _mkdir(rem_dir); time.sleep(UPLOAD_DELAY)
        if upload_pdf(pdf, fname, rem_dir, web_sub):
            print("  ✓ uploaded", flush=True); uploaded += 1
        else:
            print("  ✗ upload failed", flush=True); failed += 1

    print(f"\n{'='*40}")
    print(f"Shard {SHARD_INDEX} done: {uploaded} uploaded, {failed} failed, {skipped} skipped")
    print(f"Blocked hosts: {_blocked_hosts}")

if __name__ == "__main__":
    main()
