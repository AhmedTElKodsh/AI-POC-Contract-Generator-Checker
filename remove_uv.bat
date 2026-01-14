@echo off
REM Batch script to remove uv (Astronomer UV) from the system
echo Removing UV (Astronomer) from the system...

REM Method 1: Check if installed via pipx
pipx uninstall uv 2>nul
if %errorlevel% equ 0 (
    echo Successfully removed uv via pipx
    goto :verify
)

REM Method 2: Check if installed via pip
python -m pip uninstall uv -y 2>nul
if %errorlevel% equ 0 (
    echo Successfully removed uv via python
    goto :verify
)

python3 -m pip uninstall uv -y 2>nul
if %errorlevel% equ 0 (
    echo Successfully removed uv via python3
    goto :verify
)

py -m pip uninstall uv -y 2>nul
if %errorlevel% equ 0 (
    echo Successfully removed uv via py
    goto :verify
)

REM Method 3: Manual removal of known binary locations
set "UV_PATHS[0]=%USERPROFILE%\.local\bin\uv.exe"
set "UV_PATHS[1]=%LOCALAPPDATA%\Programs\Python\Python311\Scripts\uv.exe"
set "UV_PATHS[2]=%LOCALAPPDATA%\Programs\Python\Python312\Scripts\uv.exe"
set "UV_PATHS[3]=%LOCALAPPDATA%\Programs\Python\Python313\Scripts\uv.exe"

set "removed=false"

for /L %%i in (0,1,3) do (
    call set "current_path=%%UV_PATHS[%%i]%%"
    if exist "!current_path!" (
        echo Removing uv binary: !current_path!
        del /F /Q "!current_path!" 2>nul
        if !errorlevel! equ 0 (
            echo Successfully removed: !current_path!
            set "removed=true"
        ) else (
            echo Failed to remove: !current_path!
        )
    )
)

REM Method 4: Check for system-wide installation
if "%removed%"=="false" (
    echo Checking for system-wide installation...
    if exist "C:\Program Files\uv\bin\uv.exe" (
        echo Found system installation at: C:\Program Files\uv\bin
        echo Please run this script as Administrator to remove system installations
        echo Or manually delete: C:\Program Files\uv\bin\uv.exe
    )
)

:verify
REM Final verification
uv --version >nul 2>&1
if %errorlevel% neq 0 (
    echo UV has been successfully removed from the system!
) else (
    echo UV is still available in PATH
    echo You may need to restart your command prompt or remove it from PATH manually
)

echo Script completed. Please restart your command prompt for changes to take effect.
pause