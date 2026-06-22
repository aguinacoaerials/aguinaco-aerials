# Script to replace all gold-color references with blue equivalents in styles.css
import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Targeted replacements (order matters)
replacements = [
    # Navbar logo accent
    ('.nav-logo span { color: var(--gold); }',
     '.nav-logo span { color: var(--blue); }'),

    # Nav link underline
    ('width: 0; height: 2px; background: var(--gold);',
     'width: 0; height: 2px; background: var(--blue);'),

    # Mobile menu hover
    ('.mobile-menu a:hover { color: var(--gold); }',
     '.mobile-menu a:hover { color: var(--blue); }'),

    # Mobile close hover
    ('.mobile-close:hover { color: var(--gold); transform: rotate(90deg); }',
     '.mobile-close:hover { color: var(--blue); transform: rotate(90deg); }'),

    # Hero badge
    ('background: rgba(212,168,67,0.12); border: 1px solid rgba(212,168,67,0.3);\n  color: var(--gold);',
     'background: rgba(74,159,255,0.10); border: 1px solid rgba(74,159,255,0.25);\n  color: var(--blue);'),

    # Hero badge dot
    ('width: 7px; height: 7px; background: var(--gold);',
     'width: 7px; height: 7px; background: var(--blue);'),

    # Hero title line-gold → line-blue
    ('.hero-title .line-gold { color: var(--gold); }',
     '.hero-title .line-gold { color: var(--blue); }'),

    # Hero stats border
    ('border: 1px solid rgba(212,168,67,0.15);',
     'border: 1px solid rgba(74,159,255,0.15);'),

    # Hero stat number
    ('color: var(--gold); line-height: 1;\n}',
     'color: var(--blue); line-height: 1;\n}'),

    # svc-card gold overlay gradient
    ('background: linear-gradient(135deg, rgba(212,168,67,0.06), transparent 60%);',
     'background: linear-gradient(135deg, rgba(74,159,255,0.07), transparent 60%);'),

    # svc-card hover border gold
    ('border-color: rgba(212,168,67,0.35);',
     'border-color: rgba(74,159,255,0.35);'),

    # svc-card-num color
    ('color: rgba(212,168,67,0.08); line-height: 1; pointer-events: none;',
     'color: rgba(74,159,255,0.08); line-height: 1; pointer-events: none;'),

    # svc-card-num hover
    ('.svc-card:hover .svc-card-num { color: rgba(212,168,67,0.15); }',
     '.svc-card:hover .svc-card-num { color: rgba(74,159,255,0.15); }'),

    # svc-card-icon background
    ('background: rgba(212,168,67,0.1); border-radius: 16px;',
     'background: rgba(74,159,255,0.1); border-radius: 16px;'),

    # svc-card-icon border
    ('border: 1px solid rgba(212,168,67,0.2);\n  transition: var(--transition);\n}',
     'border: 1px solid rgba(74,159,255,0.2);\n  transition: var(--transition);\n}'),

    # svc-card hover icon
    ('background: rgba(212,168,67,0.2);\n  border-color: rgba(212,168,67,0.4);',
     'background: rgba(74,159,255,0.18);\n  border-color: rgba(74,159,255,0.4);'),

    # svc-card-icon svg stroke
    ('.svc-card-icon svg { width: 28px; height: 28px; stroke: var(--gold); }',
     '.svc-card-icon svg { width: 28px; height: 28px; stroke: var(--blue); }'),

    # svc-card-tag
    ('text-transform: uppercase; color: var(--gold);\n  background: rgba(212,168,67,0.1); border: 1px solid rgba(212,168,67,0.25);',
     'text-transform: uppercase; color: var(--blue);\n  background: rgba(74,159,255,0.1); border: 1px solid rgba(74,159,255,0.22);'),

    # svc-check
    ('background: rgba(212,168,67,0.15); color: var(--gold);',
     'background: rgba(74,159,255,0.15); color: var(--blue);'),

    # svc-card-link
    ('color: var(--gold); font-size: 0.87rem; font-weight: 600;',
     'color: var(--blue); font-size: 0.87rem; font-weight: 600;'),

    # About badge border
    ('border: 1px solid rgba(212,168,67,0.2); border-radius: 12px;',
     'border: 1px solid rgba(74,159,255,0.2); border-radius: 12px;'),

    # About badge num
    ('font-family: var(--font-main); font-size: 2rem; font-weight: 800; color: var(--gold);',
     'font-family: var(--font-main); font-size: 2rem; font-weight: 800; color: var(--blue);'),

    # About feature hover
    ('.about-feature:hover { border-color: rgba(212,168,67,0.25); }',
     '.about-feature:hover { border-color: rgba(74,159,255,0.25); }'),

    # About feature icon background
    ('width: 36px; height: 36px; background: rgba(212,168,67,0.1);',
     'width: 36px; height: 36px; background: rgba(74,159,255,0.1);'),

    # Portfolio tabs active
    ('background: var(--gold); color: var(--dark); border-color: var(--gold);',
     'background: var(--blue); color: var(--white); border-color: var(--blue);'),

    # Portfolio tag
    ('text-transform: uppercase; color: var(--gold); margin-bottom: 6px;',
     'text-transform: uppercase; color: var(--blue); margin-bottom: 6px;'),

    # Real estate feature checkmark
    ('.realestate-feature span { color: var(--gold); }',
     '.realestate-feature span { color: var(--blue); }'),

    # Testimonial card hover
    ('.testimonial-card:hover { border-color: rgba(212,168,67,0.25); transform: translateY(-4px); }',
     '.testimonial-card:hover { border-color: rgba(74,159,255,0.25); transform: translateY(-4px); }'),

    # Testimonial stars
    ('.testimonial-stars { display: flex; gap: 4px; color: var(--gold);',
     '.testimonial-stars { display: flex; gap: 4px; color: var(--blue);'),

    # Testimonial avatar gradient
    ('background: linear-gradient(135deg, var(--gold), var(--gold-dark));',
     'background: linear-gradient(135deg, var(--blue), var(--blue-deep));'),

    # Contact icon
    ('width: 48px; height: 48px; background: rgba(212,168,67,0.1);',
     'width: 48px; height: 48px; background: rgba(74,159,255,0.1);'),

    # Form focus
    ('border-color: var(--gold); box-shadow: 0 0 0 3px rgba(212,168,67,0.12);',
     'border-color: var(--blue); box-shadow: 0 0 0 3px rgba(74,159,255,0.12);'),

    # Footer social hover
    ('.footer-social:hover { background: var(--gold); border-color: var(--gold); }',
     '.footer-social:hover { background: var(--blue); border-color: var(--blue); }'),

    # Footer links hover
    ('.footer-links a:hover { color: var(--gold); padding-left: 4px; }',
     '.footer-links a:hover { color: var(--blue); padding-left: 4px; }'),

    # Footer bottom link
    ('.footer-bottom a { color: var(--gold); }',
     '.footer-bottom a { color: var(--blue); }'),
]

for old, new in replacements:
    if old in css:
        css = css.replace(old, new, 1)
        print(f'OK: {old[:60].strip()!r}')
    else:
        print(f'MISS: {old[:60].strip()!r}')

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('\nDone.')
