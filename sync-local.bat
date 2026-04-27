@echo off
setlocal
set REPO=C:\Users\ChrisKameir\Claude\Vault\Kameir.com\Kameir.com\site

echo === Removing stale lock files ===
if exist "%REPO%\.git\HEAD.lock" del "%REPO%\.git\HEAD.lock"
if exist "%REPO%\.git\index.lock" del "%REPO%\.git\index.lock"

echo === Pulling latest from GitHub ===
git -C "%REPO%" fetch origin
git -C "%REPO%" reset --hard origin/main

echo.
echo === Done — local copy is now synced with GitHub ===
git -C "%REPO%" log --oneline -3
pause
