# AI-Ready Portfolio Starter

<p align="left">
  <a href="https://github.com/vassiliylakhonin/vassiliylakhonin.github.io/stargazers"><img src="https://img.shields.io/github/stars/vassiliylakhonin/vassiliylakhonin.github.io?style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/vassiliylakhonin/vassiliylakhonin.github.io/network/members"><img src="https://img.shields.io/github/forks/vassiliylakhonin/vassiliylakhonin.github.io?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/vassiliylakhonin/vassiliylakhonin.github.io/actions/workflows/link-check.yml"><img src="https://img.shields.io/github/actions/workflow/status/vassiliylakhonin/vassiliylakhonin.github.io/link-check.yml?branch=main&style=for-the-badge" alt="CI"></a>
  <a href="https://vassiliylakhonin.github.io/"><img src="https://img.shields.io/badge/live-demo-blue?style=for-the-badge" alt="Live Demo"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License"></a>
</p>

Build an AI-ready professional profile in about 30 minutes: human-readable website + machine-readable profile data + MCP endpoint.

## Why this exists

Most portfolio sites are readable but not machine-usable. Most structured CVs are parseable but weak for humans. This project combines both in one repo, with validation and trust signals.

## 5-minute quick start

1. **Fork this repo**.
2. Edit these 3 files first:
   - `index.md` (human profile page)
   - `resume.json` (machine-readable profile)
   - `availability.json` (status and role targeting)
3. Enable GitHub Pages (Settings -> Pages -> Deploy from branch `main`).
4. Open your live URL and verify these endpoints:
   - `/`
   - `/resume.json`
   - `/agent-card.json`
5. Optional: run MCP locally.

```bash
git clone https://github.com/<you>/<your-repo>.git
cd <your-repo>
python3 -m pip install -r mcp/requirements.txt
python3 mcp/server.py --http
```

Then test:
- `http://localhost:8000/health`
- `http://localhost:8000/sse`

## Demo snapshots

### 1) Quick start flow

![Quick start flow](./docs/assets/demo-quickstart.svg)

### 2) Machine-readable profile layer

![Machine-readable endpoints](./docs/assets/demo-machine-readable.svg)

### 3) MCP integration flow

![MCP integration flow](./docs/assets/demo-mcp-flow.svg)

## What you get

- Human-friendly profile site (GitHub Pages + Jekyll)
- Structured profile endpoints (`resume.json`, `skills.json`, `evidence.json`, `verification.json`)
- Agent discovery entrypoints (`agent-card.json`, `agent-discovery.md`, `llms.txt`)
- MCP server for recruiter/agent queries (`mcp/server.py`)
- CI checks for links, schema coverage, GEO baseline, and observability snapshots

## Live reference implementation

- Site: <https://vassiliylakhonin.github.io/>
- Recruiter page: <https://vassiliylakhonin.github.io/for-recruiters.html>
- CV PDF: <https://vassiliylakhonin.github.io/Vassiliy-Lakhonin_CV.pdf>
- ATS resume (plain): <https://vassiliylakhonin.github.io/Vassiliy-Lakhonin_ATS-Resume.html>
- Agent card: <https://vassiliylakhonin.github.io/agent-card.json>
- Resume JSON: <https://vassiliylakhonin.github.io/resume.json>
- MCP SSE: <https://vassiliy-lakhonin-mcp-production.up.railway.app/sse>
- MCP health: <https://vassiliy-lakhonin-mcp-production.up.railway.app/health>

## Repository map

```text
.
├── index.md
├── for-recruiters.md
├── profile.md
├── resume.json
├── capabilities.json
├── evidence.json
├── availability.json
├── skills.json
├── verification.json
├── agent-card.json
├── agent-discovery.md
├── llms.txt
├── mcp/
│   ├── server.py
│   ├── README.md
│   └── requirements.txt
├── scripts/
└── .github/workflows/
```

## Architecture (high level)

```mermaid
flowchart LR
  A[Markdown and JSON profile source] --> B[GitHub Pages site]
  A --> C[Machine-readable endpoints]
  C --> D[AI search and retrieval]
  C --> E[MCP Server]
  E --> F[Recruiter and agent clients]
  A --> G[CI audits and observability]
```

## Developer workflow

### Local content checks

```bash
python3 scripts/geo_quick_audit.py
python3 scripts/schema_audit.py
python3 scripts/build_readiness_report.py
python3 scripts/build_freshness_report.py
python3 scripts/build_evals_report.py
python3 scripts/build_provenance_report.py
```

### Serve site locally

```bash
bundle exec jekyll serve
```

## Trust and governance

- Contributing guide: [CONTRIBUTING.md](./CONTRIBUTING.md)
- Code of conduct: [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
- Security policy: [SECURITY.md](./SECURITY.md)
- Changelog: [CHANGELOG.md](./CHANGELOG.md)

## Roadmap (short)

- Starter profile preset with one-command setup
- Better docs for role-specific profile variants
- More MCP tools for matching, outreach, and profile QA
- Community showcase of profiles built from this repo

## Contributing

Small improvements are welcome: docs clarity, schema hardening, checks, and MCP reliability improvements. Start with issues labeled `good first issue`.

## License

MIT
