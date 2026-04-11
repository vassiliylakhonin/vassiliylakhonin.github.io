# vassiliylakhonin.github.io

<p align="left">
  <a href="https://github.com/vassiliylakhonin/vassiliylakhonin.github.io/stargazers"><img src="https://img.shields.io/github/stars/vassiliylakhonin/vassiliylakhonin.github.io?style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/vassiliylakhonin/vassiliylakhonin.github.io/network/members"><img src="https://img.shields.io/github/forks/vassiliylakhonin/vassiliylakhonin.github.io?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/vassiliylakhonin/vassiliylakhonin.github.io/issues"><img src="https://img.shields.io/github/issues/vassiliylakhonin/vassiliylakhonin.github.io?style=for-the-badge" alt="Issues"></a>
  <a href="https://github.com/vassiliylakhonin/vassiliylakhonin.github.io/actions"><img src="https://img.shields.io/github/actions/workflow/status/vassiliylakhonin/vassiliylakhonin.github.io/link-check.yml?branch=main&style=for-the-badge" alt="Link Check"></a>
  <a href="https://vassiliylakhonin.github.io/"><img src="https://img.shields.io/badge/live-site-blue?style=for-the-badge" alt="Live Site"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License"></a>
</p>

Personal portfolio and CV site for **Vassiliy Lakhonin**, built for both humans and agents:
- recruiter-friendly profile + case studies,
- machine-readable metadata (`resume.json`, `capabilities.json`, `evidence.json`),
- AI indexing support (`llms.txt`, JSON-LD, `sitemap.xml`),
- live MCP endpoint for programmatic profile access,
- authority/entity signal layer (`authority.json`) for AI retrieval clarity.

---

## Live endpoints

- Site: <https://vassiliylakhonin.github.io/>
- CV PDF: <https://vassiliylakhonin.github.io/Vassiliy-Lakhonin_CV.pdf>
- Services: <https://vassiliylakhonin.github.io/services.html>
- Agent profile: <https://vassiliylakhonin.github.io/profile.md>
- MCP (SSE): <https://vassiliy-lakhonin-mcp-production.up.railway.app/sse>
- MCP health: <https://vassiliy-lakhonin-mcp-production.up.railway.app/health>

Machine-readable:
- Agent discovery entrypoint: <https://vassiliylakhonin.github.io/agent-discovery.md>
- Agent readiness score: <https://vassiliylakhonin.github.io/readiness.json>
- Agent card: <https://vassiliylakhonin.github.io/agent-card.json>
- Resume JSON: <https://vassiliylakhonin.github.io/resume.json>
- Capabilities: <https://vassiliylakhonin.github.io/capabilities.json>
- Evidence: <https://vassiliylakhonin.github.io/evidence.json>
- Availability: <https://vassiliylakhonin.github.io/availability.json>
- Engagement intake: <https://vassiliylakhonin.github.io/engage.json>
- Engagement intake v2: <https://vassiliylakhonin.github.io/engage.v2.json>
- Interview story bank: <https://vassiliylakhonin.github.io/stories.json>
- Skills: <https://vassiliylakhonin.github.io/skills.json>
- Verification: <https://vassiliylakhonin.github.io/verification.json>
- Authority signals: <https://vassiliylakhonin.github.io/authority.json>
- Freshness snapshot: <https://vassiliylakhonin.github.io/freshness.json>
- Evals snapshot: <https://vassiliylakhonin.github.io/evals.json>
- Provenance snapshot: <https://vassiliylakhonin.github.io/provenance.json>

## Featured case studies

- [Nonprofit Impact Orchestra](https://vassiliylakhonin.github.io/case-study-openclaw-rbm-skill.html): Agent-assisted nonprofit grant orchestration with human checkpoints.
- [Global Think Tank Analyst](https://vassiliylakhonin.github.io/case-study-global-think-tank-analyst.html): Structured geopolitical and policy analysis in think-tank style.
- [Donor reporting quality and delivery reliability](https://vassiliylakhonin.github.io/case-study-donor-reporting.html): Problem-action-result proof with measurable outcomes.

## Career Ops package (for higher response quality)

- Fit scoring template: <https://vassiliylakhonin.github.io/fit-score-template.md>
- Tracker schema: <https://vassiliylakhonin.github.io/tracker-schema.md>
- Story bank (Markdown): <https://vassiliylakhonin.github.io/stories.md>
- Story bank (JSON): <https://vassiliylakhonin.github.io/stories.json>
- Engagement intake v2: <https://vassiliylakhonin.github.io/engage.v2.json>

---

## What makes this repo different

- **Dual-surface design**: content optimized for both human readers and AI agents.
- **Citability-first case studies**: each markdown case includes TL;DR, Evidence, Metrics, Context/Constraint blocks.
- **Structured trust layer**: verification + evidence + authority mapping files.
- **Indexing-ready by default**: `robots.txt`, `sitemap.xml`, `llms.txt`, JSON-LD.
- **MCP integration**: profile data available via local and hosted server.

---

## Repository structure

```text
.
├── index.md
├── profile.md
├── services.html
├── case-study-*.html / case-study-*.md
├── article-*.html
├── Vassiliy-Lakhonin_CV.pdf
├── agent-card.json
├── resume.json
├── capabilities.json
├── evidence.json
├── availability.json
├── engage.json
├── skills.json
├── verification.json
├── authority.json
├── llms.txt
├── humans.txt
├── robots.txt
├── sitemap.xml
├── schema/templates/*.json
├── scripts/geo_quick_audit.py
├── scripts/schema_audit.py
├── scripts/build_readiness_report.py
└── mcp/
    ├── server.py
    ├── requirements.txt
    └── railway.toml
```

---

## Local development

```bash
git clone https://github.com/vassiliylakhonin/vassiliylakhonin.github.io.git
cd vassiliylakhonin.github.io
bundle exec jekyll serve
```

If Ruby/Jekyll is not set up, edit markdown/html/json directly and push to `main`.

---

## MCP server (local)

```bash
python3.13 -m pip install -r mcp/requirements.txt
python3.13 mcp/server.py
```

Host allowlist for SSE/HTTP transport security:

```bash
export MCP_ALLOWED_HOSTS='vassiliy-lakhonin-mcp-production.up.railway.app,127.0.0.1:*,localhost:*'
```

If `MCP_ALLOWED_HOSTS` is not set, the server uses the same safe defaults above. This prevents `Invalid Host header` errors behind Railway while keeping DNS rebinding protection enabled.

Expected tools include: `get_profile`, `get_resume`, `get_availability`, `get_capabilities`, `get_evidence`, `get_engage`, `get_agent_card`, `get_verification`, `get_skills`, `get_case_study`, `list_resources`, `search_profile`.

---

## CI / indexing automation

- Internal link checks run on push/PR: `.github/workflows/link-check.yml`
- IndexNow submission on push: `.github/workflows/indexing-push.yml`
- GEO baseline audit (weekly + key-file changes): `.github/workflows/geo-audit.yml`
- Schema coverage audit (weekly + content changes): `.github/workflows/schema-audit.yml`
- Agent observability snapshot (weekly + key changes): `.github/workflows/agent-observability.yml`
- Optional Google Search Console submission via repository secrets

Quick checks locally:

```bash
python3 scripts/geo_quick_audit.py
python3 scripts/schema_audit.py
python3 scripts/build_readiness_report.py
python3 scripts/build_freshness_report.py
python3 scripts/build_evals_report.py
python3 scripts/build_provenance_report.py
```

See scoring rubric: `docs/GEO_BASELINE.md`

---

## License

MIT
