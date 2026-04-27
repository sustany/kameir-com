@echo off
setlocal
set REPO=C:\Users\ChrisKameir\Claude\Vault\Kameir.com\Kameir.com\site

echo === Step 1: Remove stale lock files ===
if exist "%REPO%\.git\HEAD.lock" del "%REPO%\.git\HEAD.lock" && echo Deleted HEAD.lock
if exist "%REPO%\.git\index.lock" del "%REPO%\.git\index.lock" && echo Deleted index.lock

echo.
echo === Step 2: Stash ALL changes including untracked files ===
git -C "%REPO%" stash push --include-untracked -m "pre-deploy stash"
if %ERRORLEVEL% NEQ 0 (
    echo STASH FAILED.
    pause
    exit /b 1
)

echo.
echo === Step 3: Pull and rebase our ai-ethics commit on top of remote ===
git -C "%REPO%" pull --rebase origin main
if %ERRORLEVEL% NEQ 0 (
    echo PULL FAILED. Restoring stash...
    git -C "%REPO%" rebase --abort
    git -C "%REPO%" stash pop
    pause
    exit /b 1
)

echo.
echo === Step 4: Push to GitHub ===
git -C "%REPO%" push origin main
if %ERRORLEVEL% NEQ 0 (
    echo PUSH FAILED. See error above.
    pause
    exit /b 1
)

echo.
echo === Step 5: Restore stashed changes ===
git -C "%REPO%" stash pop
if %ERRORLEVEL% NEQ 0 (
    echo Note: stash pop had conflicts or nothing to restore - check git status manually.
)

echo.
echo === DONE — GitHub Actions will now build and deploy kameir.com ===
echo The three new pages are live at:
echo   kameir.com/ai-ethics
echo   kameir.com/ai-ethics/lead-magnet
echo   kameir.com/ai-ethics/book-a-call
pause
