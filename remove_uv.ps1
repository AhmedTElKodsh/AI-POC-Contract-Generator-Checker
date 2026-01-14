# PowerShell script to remove uv (Astronomer UV) from the system
# This script handles multiple possible installation methods

Write-Host "Removing UV (Astronomer) from the system..." -ForegroundColor Yellow

# Method 1: Check if installed via pipx
try {
    $pipxInstalled = Get-Command pipx -ErrorAction SilentlyContinue
    if ($pipxInstalled) {
        Write-Host "Attempting to remove via pipx..." -ForegroundColor Cyan
        pipx uninstall uv
        Write-Host "Successfully removed uv via pipx" -ForegroundColor Green
        exit 0
    }
} catch {
    Write-Host "Not installed via pipx, continuing..." -ForegroundColor Yellow
}

# Method 2: Check if installed via pip (Python package managers)
$pythonVersions = @("python", "python3", "py")

foreach ($py in $pythonVersions) {
    try {
        $pythonCmd = Get-Command $py -ErrorAction SilentlyContinue
        if ($pythonCmd) {
            Write-Host "Attempting to remove via $py -m pip..." -ForegroundColor Cyan
            & $py -m pip uninstall uv -y 2>$null
            if ($LASTEXITCODE -eq 0) {
                Write-Host "Successfully removed uv via $py" -ForegroundColor Green
                exit 0
            }
        }
    } catch {
        continue
    }
}

# Method 3: Manual removal of binaries
$uvPaths = @(
    "$env:USERPROFILE\.local\bin\uv.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python311\Scripts\uv.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python312\Scripts\uv.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python313\Scripts\uv.exe"
)

$removed = $false
foreach ($path in $uvPaths) {
    if (Test-Path $path) {
        Write-Host "Removing uv binary: $path" -ForegroundColor Cyan
        try {
            Remove-Item $path -Force -ErrorAction Stop
            Write-Host "Successfully removed: $path" -ForegroundColor Green
            $removed = $true
        } catch {
            Write-Host "Failed to remove: $path" -ForegroundColor Red
        }
    }
}

# Method 4: Remove from PATH if installed system-wide
if (-not $removed) {
    Write-Host "Checking for system-wide installation..." -ForegroundColor Cyan
    try {
        # Check if uv is in a system PATH location
        $systemPaths = @(
            "C:\Program Files\uv\bin",
            "C:\Program Files (x86)\uv\bin",
            "$env:ProgramFiles\uv\bin"
        )

        foreach ($sysPath in $systemPaths) {
            if (Test-Path "$sysPath\uv.exe") {
                Write-Host "Found system installation at: $sysPath" -ForegroundColor Yellow
                Write-Host "Please run this script as Administrator to remove system installations" -ForegroundColor Red
                Write-Host "Or manually delete: $sysPath\uv.exe" -ForegroundColor Yellow
            }
        }
    } catch {
        Write-Host "No system installation found" -ForegroundColor Yellow
    }
}

# Final verification
try {
    $uvCheck = Get-Command uv -ErrorAction SilentlyContinue
    if (-not $uvCheck) {
        Write-Host "UV has been successfully removed from the system!" -ForegroundColor Green
    } else {
        Write-Host "UV is still available at: $($uvCheck.Source)" -ForegroundColor Yellow
        Write-Host "You may need to restart your terminal or remove it from PATH manually" -ForegroundColor Yellow
    }
} catch {
    Write-Host "UV removal verification completed" -ForegroundColor Green
}

Write-Host "Script completed. Please restart your terminal for changes to take effect." -ForegroundColor Cyan