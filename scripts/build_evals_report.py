#!/usr/bin/env python3
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Tuple


def load_json(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except Exception:
        return {}


def mcp_health(url: str) -> Tuple[str, Optional[int]]:
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            return ('pass' if 200 <= r.status < 300 else 'warn', int(r.status))
    except Exception:
        return ('warn', None)


def main() -> int:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')

    readiness = load_json('readiness.json')
    overall = readiness.get('overall_score')

    geo = load_json('geo-report.json')
    schema = load_json('schema-report.json')

    schema_critical = len(schema.get('critical', []))
    schema_status = 'pass' if schema_critical == 0 else 'fail'

    geo_score = geo.get('score')
    if isinstance(geo_score, (int, float)):
        geo_status = 'pass' if geo_score >= 85 else 'warn'
    else:
        geo_status = 'warn'

    mcp_status, mcp_http = mcp_health('https://vassiliy-lakhonin-mcp-production.up.railway.app/health')

    checks = [
        {
            'name': 'readiness_overall',
            'status': 'pass' if isinstance(overall, (int, float)) and overall >= 90 else 'warn',
            'value': overall,
            'target': '>= 90',
        },
        {
            'name': 'geo_baseline_score',
            'status': geo_status,
            'value': geo_score,
            'target': '>= 85',
        },
        {
            'name': 'schema_critical_issues',
            'status': schema_status,
            'value': schema_critical,
            'target': '== 0',
        },
        {
            'name': 'mcp_health_http',
            'status': mcp_status,
            'value': mcp_http,
            'target': '2xx',
        },
    ]

    pass_count = sum(1 for c in checks if c['status'] == 'pass')
    warn_count = sum(1 for c in checks if c['status'] == 'warn')
    fail_count = sum(1 for c in checks if c['status'] == 'fail')

    out = {
        'schema_version': '1.0',
        'generated_at': now,
        'summary': {
            'pass': pass_count,
            'warn': warn_count,
            'fail': fail_count,
        },
        'checks': checks,
    }

    Path('evals.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Wrote evals.json')
    return 1 if fail_count else 0


if __name__ == '__main__':
    raise SystemExit(main())
