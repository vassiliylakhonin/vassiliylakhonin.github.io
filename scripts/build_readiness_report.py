#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path('.')

def main() -> int:
    p = ROOT / 'readiness.json'
    if not p.exists():
        raise SystemExit('readiness.json not found')

    data = json.loads(p.read_text(encoding='utf-8'))
    weights = data.get('weights', {})
    scores = data.get('scores', {})
    overall = data.get('overall_score')
    gaps = data.get('top_gaps', [])

    lines = [
        '# Agent Readiness Report',
        '',
        f"- Overall score: **{overall}/100**",
        f"- Version: `{data.get('version', 'n/a')}`",
        f"- Updated at: `{data.get('updated_at', 'n/a')}`",
        '',
        '## Domain scores',
        '',
        '| Domain | Weight | Score | Weighted |',
        '|---|---:|---:|---:|',
    ]

    for k in ['discoverability', 'agent_readiness', 'trust_verification', 'proof_case_studies', 'contact_availability']:
        w = float(weights.get(k, 0))
        s = float(scores.get(k, 0))
        lines.append(f'| `{k}` | {w:.2f} | {s:.1f} | {w*s:.2f} |')

    lines += ['', '## Top gaps', *[f'- {g}' for g in gaps]]
    lines += [
        '',
        '## Start here for agents',
        '- `agent-discovery.md`',
        '- `agent-card.json`',
        '- `authority.json`',
        '- `availability.json` + `engage.json`',
    ]

    out = ROOT / 'agent-readiness-report.md'
    out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'Wrote {out}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
