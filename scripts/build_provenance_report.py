#!/usr/bin/env python3
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def cmd(args: list[str]) -> str:
    try:
        return subprocess.check_output(args, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return ''


def main() -> int:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')

    head_sha = cmd(['git', 'rev-parse', 'HEAD'])
    branch = cmd(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    latest_commit_at = cmd(['git', 'log', '-1', '--format=%cI'])
    latest_signed_flag = cmd(['git', 'log', '-1', '--format=%G?'])

    signature_map = {
        'G': 'verified',
        'U': 'good_untrusted',
        'Y': 'good_expired_key',
        'R': 'good_revoked_key',
        'E': 'missing_key',
        'B': 'bad_signature',
        'N': 'unsigned',
    }

    out = {
        'schema_version': '1.0',
        'generated_at': now,
        'source_repository': 'https://github.com/vassiliylakhonin/vassiliylakhonin.github.io',
        'default_branch': branch or 'main',
        'head': {
            'sha': head_sha,
            'committed_at': latest_commit_at,
            'signature_status': signature_map.get(latest_signed_flag, 'unknown'),
            'signature_flag': latest_signed_flag or 'unknown',
        },
        'recommendation': 'Enable signed commits/tags for stronger provenance signals in agent trust pipelines.'
    }

    Path('provenance.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Wrote provenance.json')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
