#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path('.')


def extract_types(path: Path) -> set[str]:
    text = path.read_text(encoding='utf-8', errors='ignore')
    blocks = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', text, flags=re.I | re.S)
    types: set[str] = set()
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        try:
            data = json.loads(b)
        except Exception:
            continue

        def walk(obj):
            if isinstance(obj, dict):
                t = obj.get('@type')
                if isinstance(t, str):
                    types.add(t)
                elif isinstance(t, list):
                    for x in t:
                        if isinstance(x, str):
                            types.add(x)
                for v in obj.values():
                    walk(v)
            elif isinstance(obj, list):
                for i in obj:
                    walk(i)

        walk(data)
    return types


def main() -> int:
    critical = []
    warnings = []
    checks = []

    html_files = [p for p in ROOT.glob('*.html') if not p.name.startswith('google')]
    source_files = html_files + ([Path('index.md')] if Path('index.md').exists() else [])
    if not source_files:
        critical.append('No content files found for schema audit')

    all_types: set[str] = set()
    per_file: dict[str, set[str]] = {}
    for f in source_files:
        t = extract_types(f)
        per_file[f.name] = t
        all_types |= t
        checks.append((f'{f.name}:jsonld_present', bool(t)))

    # Global expectations
    checks.append(('global:Person', 'Person' in all_types))
    if 'Person' not in all_types:
        critical.append('Missing Person schema across site')

    checks.append(('global:WebSite', 'WebSite' in all_types))
    if 'WebSite' not in all_types:
        warnings.append('WebSite schema not found (recommended for homepage discoverability)')

    # Page-type expectations
    for f, t in per_file.items():
        if f.startswith('case-study-'):
            ok = 'Article' in t and 'Person' in t
            checks.append((f'{f}:case_schema', ok))
            if not ok:
                critical.append(f'{f} should include Article + Person schema')
        elif f.startswith('article-'):
            ok = (('Article' in t) or ('ScholarlyArticle' in t)) and ('Person' in t)
            checks.append((f'{f}:article_schema', ok))
            if not ok:
                critical.append(f'{f} should include ScholarlyArticle/Article + Person schema')
        elif f == 'services.html':
            ok = (('Service' in t) or ('ProfessionalService' in t)) and ('Person' in t)
            checks.append((f'{f}:service_schema', ok))
            if not ok:
                critical.append('services.html should include Service/ProfessionalService + Person schema')

    report = [
        '# Schema Coverage Report',
        '',
        f'- Critical issues: **{len(critical)}**',
        f'- Warnings: **{len(warnings)}**',
        '',
        '## Checks'
    ]
    for name, ok in checks:
        report.append(f"- {'✅' if ok else '❌'} {name}")

    if critical:
        report += ['', '## Critical', *[f'- {x}' for x in critical]]
    if warnings:
        report += ['', '## Warnings', *[f'- {x}' for x in warnings]]

    Path('schema-report.md').write_text('\n'.join(report), encoding='utf-8')
    Path('schema-report.json').write_text(json.dumps({
        'critical': critical,
        'warnings': warnings,
        'all_types': sorted(all_types)
    }, ensure_ascii=False, indent=2), encoding='utf-8')

    print('\n'.join(report))
    return 1 if critical else 0


if __name__ == '__main__':
    sys.exit(main())
