$file = "C:\Users\Ahmed\Documents\PowerShell\OpenSpecCompletion.ps1"
$lines = Get-Content $file
$output = @()

for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]
    # If line ends with a comma and next line starts with closing parenthesis
    if ($line.Trim().EndsWith(',') -and ($i + 1 -lt $lines.Count) -and ($lines[$i + 1].Trim().StartsWith(')'))) {
        $line = $line.TrimEnd(',')
    }
    $output += $line
}

$output | Out-File -FilePath $file -Encoding UTF8 -NoNewline
Write-Host "Fixed trailing commas before closing parentheses"