$file = "C:\Users\Ahmed\Documents\PowerShell\OpenSpecCompletion.ps1"
$content = Get-Content $file -Raw

# Fix trailing commas before closing parentheses in array definitions
# This regex matches: comma, optional whitespace, closing parenthesis, closing parenthesis
# But only when it's at the end of a line (before closing array parenthesis)
$pattern = '(?m)(,+)(\s*\),?\s*\))'
$replacement = '$2'

$content = $content -replace $pattern, $replacement

Set-Content $file -Value $content -NoNewline
Write-Host "Fixed trailing commas in file"