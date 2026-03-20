# GEO Baseline (for this repo)

Scoring rubric (0-100):
- JSON artifacts completeness: 40
- robots.txt AI crawler policy coverage: 20
- llms.txt MCP/agent-link integrity: 15
- MCP remote availability (`/sse`, `/health`): 25

Pass criteria:
- No critical failures
- Score >= 80

Critical failures (CI red):
- Missing required machine-readable files
- Unreachable remote MCP endpoints

Warnings (CI green, improvement needed):
- Missing explicit AI crawler section in `robots.txt`
- Missing key links in `llms.txt`

Run locally:

```bash
python3 scripts/geo_quick_audit.py
```

Artifacts:
- `geo-report.md`
- `geo-report.json`
