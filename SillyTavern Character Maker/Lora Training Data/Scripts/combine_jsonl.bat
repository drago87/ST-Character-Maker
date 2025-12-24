@echo off
REM --------------------------------------------------------
REM Drag & drop multiple JSONL files and/or folders onto
REM this script to combine them into "CMC Lora Training Data.jsonl"
REM in the 'Dataset' folder
REM --------------------------------------------------------

SETLOCAL

REM Check Python
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python not found in PATH.
    pause
    EXIT /B
)

IF "%~1"=="" (
    echo Drop JSONL files or folders onto this script.
    pause
    EXIT /B
)

SET "SCRIPT_DIR=%~dp0"

REM Collect all arguments
SET "ARGS="
:loop
IF "%~1"=="" GOTO done_args
SET "ARGS=%ARGS% "%~1""
SHIFT
GOTO loop
:done_args

echo Combining files/folders: %ARGS%
python "%SCRIPT_DIR%combine_jsonl.py" %ARGS%

echo.
echo Done. Combined file is in "%SCRIPT_DIR%Dataset"
pause