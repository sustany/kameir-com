@echo off
setlocal
set REPO=C:\Users\ChrisKameir\Claude\Vault\Kameir.com\Kameir.com\site

echo === [1/4] Clearing stale lock files ===
if exist "%REPO%\.git\HEAD.lock"        del /f /q "%REPO%\.git\HEAD.lock"
if exist "%REPO%\.git\index.lock"       del /f /q "%REPO%\.git\index.lock"
if exist "%REPO%\.git\MERGE_HEAD"       del /f /q "%REPO%\.git\MERGE_HEAD"
if exist "%REPO%\.git\MERGE_MSG"        del /f /q "%REPO%\.git\MERGE_MSG"
if exist "%REPO%\.git\MERGE_MODE"   