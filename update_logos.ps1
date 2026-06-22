Get-ChildItem -Path . -Filter *.html -Recurse | ForEach-Object {
    $content = [System.IO.File]::ReadAllText($_.FullName)
    $modified = $false
    
    if ($content -match 'LOGOLETRASPNG\.png') {
        $content = $content -replace 'LOGOLETRASPNG\.png', 'NEWLOGOLETRASPNG.png'
        $modified = $true
    }
    if ($content -match 'height:\s*36px') {
        $content = $content -replace 'height:\s*36px', 'height: 48px'
        $modified = $true
    }
    if ($content -match 'height:\s*22px') {
        $content = $content -replace 'height:\s*22px', 'height: 48px'
        $modified = $true
    }
    if ($content -match 'height:\s*40px') {
        $content = $content -replace 'height:\s*40px', 'height: 48px'
        $modified = $true
    }
    
    if ($modified) {
        [System.IO.File]::WriteAllText($_.FullName, $content, (New-Object System.Text.UTF8Encoding $False))
        Write-Output "Updated $($_.FullName)"
    }
}
