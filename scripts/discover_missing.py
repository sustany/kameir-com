#!/usr/bin/env python3
"""
discover_missing.py — Builds the list of PDFs that need to be uploaded.

Truth source: HEAD-probe https://kameir.com/AI-legal-research/orders/<folder>/<file>
for every PDF in hallucinations.json. Anything not returning 200 goes into missing.json.

Output: missing.json (list of {slug, url, folder, fname, source_url})
"""
import json, re, ssl, urllib.request, urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

REPO_ROOT = Path(__file__).parent.parent
DATA_FILE = REPO_ROOT / "src" / "data" / "hallucinations.json"
OUT_FILE  = REPO_ROOT / "missing.json"

_STATE_WORDS = {"Alabama":"AL","Alaska":"AK","Arizona":"AZ","Arkansas":"AR","California":"CA","Colorado":"CO","Connecticut":"CT","Delaware":"DE","Florida":"FL","Georgia":"GA","Hawaii":"HI","Idaho":"ID","Illinois":"IL","Indiana":"IN","Iowa":"IA","Kansas":"KS","Kentucky":"KY","Louisiana":"LA","Maine":"ME","Maryland":"MD","Massachusetts":"MA","Michigan":"MI","Minnesota":"MN","Mississippi":"MS","Missouri":"MO","Montana":"MT","Nebraska":"NE","Nevada":"NV","Hampshire":"NH","Jersey":"NJ","New Mexico":"NM","York":"NY","North Carolina":"NC","North Dakota":"ND","Ohio":"OH","Oklahoma":"OK","Oregon":"OR","Pennsylvania":"PA","Rhode Island":"RI","South Carolina":"SC","South Dakota":"SD","Tennessee":"TN","Texas":"TX","Utah":"UT","Vermont":"VT","Virginia":"VA","Washington":"WA","West Virginia":"WV","Wisconsin":"WI","Wyoming":"WY","Columbia":"DC"}
_FEDERAL = {"GAO","ASBCA","CBCA","COFC","PTAB","TTAB","BIA","EEOC","NLRB","USPTO","Federal Circuit","CAFC","Fed. Cir."}
_COUNTRY = {"Canada":"CA-INTL","Australia":"AU","Israel":"IL","UK":"UK","France":"FR","Brazil":"BR","Argentina":"AR-INTL","Ireland":"IE","India":"IN-INTL","Italy":"IT","New Zealand":"NZ","Spain":"ES","Netherlands":"NL","South Africa":"ZA","Germany":"DE","Japan":"JP","Singapore":"SG","UAE":"AE","Portugal":"PT","Mexico":"MX-INTL"}

def court_to_folder(court, state):
    if state == "USA":
        if not court: return "DC"
        for body in _FEDERAL:
            if body.lower() in court.lower(): return "DC"
        for word, code in _STATE_WORDS.items():
            if word.lower() in court.lower(): return code
        m = re.match(r"^([A-Z]{2})\s", court)
        if m and m.group(1) in _STATE_WORDS.values(): return m.group(1)
        return "DC"
    return _COUNTRY.get(state, re.sub(r"[^A-Z0-9-]","",state.upper())[:10] or "INTL")

def safe_filename(url):
    name = url.rstrip("/").split("/")[-1].split("?")[0]
    name = re.sub(r"[^\w.\-]","_",name)
    if not name.lower().endswith(".pdf"): name += ".pdf"
    return name or "order.pdf"

def main():
    data = json.loads(DATA_FILE.read_text())
    cases = [c for c in data if c.get("sourceUrl","").lower().endswith(".pdf")]

    expected = []
    for c in cases:
        folder = court_to_folder(c.get("court",""), c.get("state",""))
        fname  = safe_filename(c["sourceUrl"])
        expected.append({
            "slug":       c.get("slug",""),
            "folder":     folder,
            "fname":      fname,
            "source_url": c["sourceUrl"],
            "live_url":   f"https://kameir.com/AI-legal-research/orders/{folder}/{fname}",
        })

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    def head(item):
        try:
            req = urllib.request.Request(item["live_url"], method="HEAD")
            req.add_header("User-Agent","Mozilla/5.0")
            with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
                return item, r.status
        except urllib.error.HTTPError as e:
            return item, e.code
        except Exception:
            return item, 0

    live_n = 0
    missing = []
    with ThreadPoolExecutor(max_workers=40) as ex:
        for item, status in (f.result() for f in as_completed(ex.submit(head,i) for i in expected)):
            if status == 200:
                live_n += 1
            else:
                missing.append(item)

    OUT_FILE.write_text(json.dumps(missing, indent=2))
    print(f"Total expected:  {len(expected)}")
    print(f"Live on server:  {live_n}")
    print(f"Missing (output): {len(missing)}")
    print(f"Wrote {OUT_FILE}")

if __name__ == "__main__":
    main()
