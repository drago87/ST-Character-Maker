@echo off
REM --------------------------------------------------------
REM Drag & drop a .md file onto this script to convert it
REM into JSONL files in the 'jsonl' folder
REM --------------------------------------------------------

SETLOCAL

REM Check Python
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python not found in PATH.
    pause
    EXIT /B
)

SET "INPUT=%~1"
IF "%INPUT%"=="" (
    echo Drop a .md file onto this script.
    pause
    EXIT /B
)

SET "SCRIPT_DIR=%~dp0"

echo Processing: "%INPUT%"
python "%SCRIPT_DIR%md_to_jsonl.py" "%INPUT%"

echo.
echo Done. JSONL files are in "%SCRIPT_DIR%jsonl"
pause