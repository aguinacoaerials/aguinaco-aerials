#!/usr/bin/env python3
"""Apply shared audit fixes to all HTML pages."""
from pathlib import Path
import re

BASE = Path(__file__).parent

HEAD_ROOT = """
  <link rel="icon" href="assets/images/Logo.png" type="image/png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800;900&display=swap" />"""

HEAD_SVC = """
  <link rel="icon" href="../assets/images/Logo.png" type="image/png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800;900&display=swap" />"""

SKIP = '  <a href="#main-content" class="skip-link">Saltar al contenido principal</a>\n'

COOKIE_ROOT = """
  <div id="cookieBanner" role="dialog" aria-label="Aviso de cookies" aria-modal="true" aria-live="polite">
    <p>
      Utilizamos cookies propias y de terceros para mejorar la experiencia de navegación.
      <a href="cookies.html">Más información</a>
    </p>
    <div class="cookie-actions">
      <button id="cookieAccept" class="btn btn-primary btn-sm">Aceptar</button>
      <button id="cookieReject" class="btn btn-outline btn-sm">Rechazar</button>
    </div>
  </div>"""

COOKIE_SVC = COOKIE_ROOT.replace('cookies.html', '../cookies.html')

MOBILE_ROOT = """
  <div class="mobile-cta-bar" aria-label="Acciones rápidas">
    <a href="tel:+34685097504" class="btn btn-outline btn-sm">Llamar</a>
    <a href="contact.html" class="btn btn-primary btn-sm">Presupuesto</a>
  </div>"""

MOBILE_SVC = MOBILE_ROOT.replace('contact.html', '../contact.html')


def patch(content: str, is_service: bool) -> str:
    if 'skip-link' in content:
        return content

    head = HEAD_SVC if is_service else HEAD_ROOT
    cookie = COOKIE_SVC if is_service else COOKIE_ROOT
    mobile = MOBILE_SVC if is_service else MOBILE_ROOT

    if 'rel="icon"' not in content:
        content = re.sub(
            r'(<meta name="viewport"[^>]+>\s*)',
            r'\1' + head + '\n',
            content,
            count=1,
        )

    content = re.sub(r'(<body>\s*)', r'\1\n' + SKIP, content, count=1)

    # Insert <main> after mobile menu closes
    content = re.sub(
        r'(</div>\s*\n\s*(?:<!-- PAGE HERO -->|<section class="page-hero"|<section class="section"))',
        r'</div>\n\n  <main id="main-content">\n\n  \2',
        content,
        count=1,
    )

    # Close main + mobile CTA before footer
    content = re.sub(
        r'\n(\s*(?:<!-- FOOTER -->|<!-- ══════════ FOOTER|<footer))',
        r'\n\n  </main>\n\n' + mobile + r'\n\1',
        content,
        count=1,
    )

    if 'id="cookieBanner"' not in content:
        content = re.sub(
            r'(\s*<script src="[^"]*main\.js"></script>)',
            cookie + r'\1',
            content,
            count=1,
        )

    if 'aria-expanded' not in content:
        content = content.replace(
            'aria-label="Abrir menú">',
            'aria-label="Abrir menú" aria-expanded="false">',
        )

    content = content.replace(' de demostración', '')
    content = content.replace('demostración ', '')

    return content


def main():
    for path in sorted(BASE.glob('*.html')):
        if path.name == 'index.html':
            continue
        text = path.read_text(encoding='utf-8')
        path.write_text(patch(text, False), encoding='utf-8')
        print(f'Updated {path.name}')

    svc_dir = BASE / 'services'
    if svc_dir.exists():
        for path in sorted(svc_dir.glob('*.html')):
            text = path.read_text(encoding='utf-8')
            path.write_text(patch(text, True), encoding='utf-8')
            print(f'Updated services/{path.name}')


if __name__ == '__main__':
    main()
