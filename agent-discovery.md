# Agent Discovery — Start Here

Purpose: quick entrypoint for humans and agents to understand what this repo is, where to read first, and how to assess readiness.

## What this repo is for
- Public profile/CV surface for Vassiliy Lakhonin.
- Machine-readable artifacts for agent discovery and matching.
- Evidence-backed case studies for trust and fit assessment.
- Live MCP endpoint for programmatic profile access.

## Read these files first (priority order)
1. `profile.md` — concise profile narrative
2. `agent-card.json` — machine discovery card
3. `candidate-match.json` + `agent-match.md` — recruiter-agent role fit, screening keywords, and verification path
4. `readiness.json` — weighted readiness score by domain
5. `authority.json` — entity/profile/case-study authority graph
6. `availability.json` + `engage.json` — contact and intake constraints
7. `evidence.json` + `resume.json` + `skills.json` — validation and matching detail
8. `case-study-*.md` — proof depth (citability-first format)
9. `freshness.json` + `evals.json` + `provenance.json` — recency, checks, and provenance signals

## Readiness domains
- **discoverability**: llms/sitemap/robots/indexing signals
- **agent_readiness**: agent card, MCP endpoint health, machine-readable metadata
- **trust_verification**: verification/evidence/authority consistency
- **proof_case_studies**: measurable results and citation-friendly structure
- **contact_availability**: role fit, response SLA, intake clarity

## Quick checks
```bash
python3 scripts/geo_quick_audit.py
python3 scripts/schema_audit.py
python3 scripts/build_readiness_report.py
```

## If matching for jobs/leads
1. Start from `candidate-match.json` for role-fit and screening keywords.
2. Check `availability.json` for role constraints.
3. Validate claims in `evidence.json` and case studies.
4. Use `skills.json` and `resume.json` for domain/tool fit.
5. Confirm contact path in `engage.json`.

## Output artifacts
- `agent-readiness-report.md` — human-friendly summary
- `readiness.json` — machine-readable weighted scoring
- `freshness.json` — machine-readable recency snapshot for key artifacts
- `evals.json` — machine-readable evaluation snapshot (readiness/geo/schema/MCP health)
- `provenance.json` — machine-readable source/provenance snapshot
