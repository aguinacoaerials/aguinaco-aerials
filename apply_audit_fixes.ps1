$base = Split-Path -Parent $MyInvocation.MyCommand.Path

$headRoot = @"
  <link rel="icon" href="assets/images/Logo.png" type="image/png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800;900&display=swap" />
"@

$headServices = @"
  <link rel="icon" href="../assets/images/Logo.png" type="image/png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800;900&display=swap" />
"@

$skipLink = '  <a href="#main-content" class="skip-link">Saltar al contenido principal</a>'

$cookieRoot = @'
  <div id="cookieBanner" role="dialog" aria-label="Aviso de cookies" aria-modal="true" aria-live="polite">
    <p>
      Utilizamos cookies propias y de terceros para mejorar la experiencia de navegación.
      <a href="cookies.html">Más información</a>
    </p>
    <div class="cookie-actions">
      <button id="cookieAccept" class="btn btn-primary btn-sm">Aceptar</button>
      <button id="cookieReject" class="btn btn-outline btn-sm">Rechazar</button>
    </div>
  </div>
'@

$cookieServices = @'
  <div id="cookieBanner" role="dialog" aria-label="Aviso de cookies" aria-modal="true" aria-live="polite">
    <p>
      Utilizamos cookies propias y de terceros para mejorar la experiencia de navegación.
      <a href="../cookies.html">Más información</a>
    </p>
    <div class="cookie-actions">
      <button id="cookieAccept" class="btn btn-primary btn-sm">Aceptar</button>
      <button id="cookieReject" class="btn btn-outline btn-sm">Rechazar</button>
    </div>
  </div>
'@

$mobileRoot = @'
  <div class="mobile-cta-bar" aria-label="Acciones rápidas">
    <a href="tel:+34685097504" class="btn btn-outline btn-sm">Llamar</a>
    <a href="contact.html" class="btn btn-primary btn-sm">Presupuesto</a>
  </div>
'@

$mobileServices = @'
  <div class="mobile-cta-bar" aria-label="Acciones rápidas">
    <a href="tel:+34685097504" class="btn btn-outline btn-sm">Llamar</a>
    <a href="../contact.html" class="btn btn-primary btn-sm">Presupuesto</a>
  </div>
'@

function Update-HtmlFile {
    param([string]$Path, [bool]$IsService = $false)

    if ($Path -like '*index.html') { return }

    $content = Get-Content $Path -Raw -Encoding UTF8
    if ($content -match 'skip-link') { Write-Host "Skip: $Path (already patched)"; return }

    $head = if ($IsService) { $headServices } else { $headRoot }
    $cookie = if ($IsService) { $cookieServices } else { $cookieRoot }
    $mobile = if ($IsService) { $mobileServices } else { $mobileRoot }

    if ($content -notmatch 'rel="icon"') {
        $content = $content -replace '(<meta name="viewport"[^>]+>\s*)', "`$1`n$head`n"
    }

    $content = $content -replace '(<body>\s*)', "`$1`n$skipLink`n"

    $content = $content -replace '(</div>\s*\r?\n\s*<!-- PAGE HERO -->)', "</div>`n`n  <main id=`"main-content`">`n`n  <!-- PAGE HERO -->"
    $content = $content -replace '(</div>\s*\r?\n\s*<section class="page-hero")', "</div>`n`n  <main id=`"main-content`">`n`n  <section class=`"page-hero`""
    $content = $content -replace '(</div>\s*\r?\n\s*<section class="section")', "</div>`n`n  <main id=`"main-content`">`n`n  <section class=`"section`""

    if ($content -notmatch '<main id="main-content">') {
        $content = $content -replace '(</div>\s*\r?\n\s*<!--)', "</div>`n`n  <main id=`"main-content`">`n`n  <!--"
    }

    $content = $content -replace '(<!-- FOOTER -->|<!-- ══════════ FOOTER|<footer role="contentinfo">|<footer>)', "  </main>`n`n  $mobile`n`n  `$1"

    if ($content -notmatch 'id="cookieBanner"') {
        $content = $content -replace '(<script src="[^"]*main\.js"></script>)', "$cookie`n`n  `$1"
    }

    if ($content -match 'id="hamburger"[^>]*aria-label="Abrir menú"[^>]*>' -and $content -notmatch 'aria-expanded') {
        $content = $content -replace '(<button class="hamburger" id="hamburger" aria-label="Abrir menú")', '$1 aria-expanded="false"'
    }

    $content = $content -replace ' de demostración', ''
    $content = $content -replace 'demostración ', ''

    Set-Content $Path $content -Encoding UTF8 -NoNewline
    Write-Host "Updated: $Path"
}

Get-ChildItem $base -Filter '*.html' | ForEach-Object { Update-HtmlFile $_.FullName $false }
Get-ChildItem (Join-Path $base 'services') -Filter '*.html' | ForEach-Object { Update-HtmlFile $_.FullName $true }

Write-Host 'Done.'
