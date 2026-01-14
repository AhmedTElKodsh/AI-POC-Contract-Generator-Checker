@echo off
REM Add Tesseract and Poppler to PATH for current session
set PATH=%PATH%;C:\Program Files\Tesseract-OCR
set PATH=%PATH%;%~dp0poppler-24.08.0\Library\bin

echo PATH updated for current session
echo Tesseract: C:\Program Files\Tesseract-OCR
echo Poppler: %~dp0poppler-24.08.0\Library\bin
echo.
echo Run this script before using the application in a new terminal
