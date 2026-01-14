$file = "C:\Users\Ahmed\Documents\PowerShell\OpenSpecCompletion.ps1"
$content = Get-Content $file -Raw

# Pattern to match: comma at end of line that's followed by closing parentheses
# Matches: ",\n)" where the previous line ends with a hashtable
$content = $content -replace ',\s*\n\s*\)', ')'
$content = $content -replace ',\s*\)', ')'

Set-Content $file -Value $content -NoNewline
Write-Host "Fixed all trailing commas"