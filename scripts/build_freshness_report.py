#!/usr/bin/env python3
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

ROOT = Path('.')

TRACKED = [
    'index.md',
    'profile.md',
    'agent-discovery.md',
    'agent-card.json',
    'readiness.json',
    'authority.json',
    'verification.json',
    'capabilities.json',
    'availability.json',
    'engage.json',
    'skills.json',
    'evidence.json',
    'llms.txt',
]


def git_last_commit_iso(path: str) -> Optional[str]:
    try:
        out = subprocess.check_output(
            ['git', 'log', '-1', '--format=%cI', '--', path],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        return out or None
    except Exception:
        return None


def main() -> int:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    artifacts = []
    missing = []

    for rel in TRACKED:
        p = ROOT / rel
        if not p.exists():
            missing.append(rel)
            continue
        artifacts.append(
            {
                'path': rel,
                'last_commit_at': git_last_commit_iso(rel),
                'size_bytes': p.stat().st_size,
            }
        )

    repo_last_commit = git_last_commit_iso('.')

    out = {
        'schema_version': '1.0',
        'generated_at': now,
        'repository_last_commit_at': repo_last_commit,
        'tracked_artifacts_count': len(artifacts),
        'missing_artifacts': missing,
        'artifacts': artifacts,
    }

    Path('freshness.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Wrote freshness.json')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
