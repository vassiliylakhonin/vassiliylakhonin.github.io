# Contributing

Thanks for improving this project.

## Scope

High-leverage contributions:
- Onboarding and docs clarity
- JSON schema and data quality checks
- MCP server reliability and safety
- CI stability and observability
- UX clarity for recruiter and agent flows

## Quick setup

```bash
git clone https://github.com/vassiliylakhonin/vassiliylakhonin.github.io.git
cd vassiliylakhonin.github.io
```

Optional local checks:

```bash
python3 scripts/geo_quick_audit.py
python3 scripts/schema_audit.py
python3 scripts/build_readiness_report.py
```

## Branch and PR flow

1. Create a branch: `feat/<short-name>` or `fix/<short-name>`
2. Keep PRs focused and small.
3. Add clear before/after notes in the PR.
4. Link related issue when available.
5. Ensure workflows pass.

## Commit style

Use concise conventional-style subjects when possible:
- `feat: ...`
- `fix: ...`
- `docs: ...`
- `chore: ...`

## Content and data rules

- Keep claims evidence-backed.
- Do not add fake social proof or inflated metrics.
- Preserve compatibility for published JSON endpoints when possible.
- If a schema contract changes, document it in `CHANGELOG.md`.

## Security

Do not open public issues for sensitive vulnerabilities. Use `SECURITY.md`.
