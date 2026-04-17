# Changelog

All notable changes to this project are documented in this file.

## [0.2.5] - 2026-04-17

### Changed
- Hardened `agent-card.json` for better Claude Code, Codex, OpenClaw, and generic agent discovery
- Expanded agent card resources to include recruiter, ATS, profile markdown, case-study, and MCP endpoints
- Added `agent-runtime-discovery` skill block with explicit discovery examples and output resources
- Refreshed agent card version metadata

## [0.2.4] - 2026-04-17

### Changed
- Rewrote `case-study-global-think-tank-analyst.md` and `case-study-global-think-tank-analyst.html`
- Aligned case study with the live ClawHub skill framing (policy-risk memo architecture)
- Updated narrative toward decision-quality outputs, evidence discipline, and bounded confidence

## [0.2.3] - 2026-04-17

### Changed
- Rewrote `case-study-openclaw-rbm-skill.md` and `case-study-openclaw-rbm-skill.html`
- Repositioned the case study around the live ClawHub skill "Nonprofit Proposal Decision Engine"
- Updated narrative from generic orchestration story to decision-quality model (Go / Conditional Go / No-Go, donor-fit matrix, evidence discipline)

## [0.2.2] - 2026-04-17

### Added
- New ATS-friendly resume page: `Vassiliy-Lakhonin_ATS-Resume.md` (published as `/Vassiliy-Lakhonin_ATS-Resume.html`)

### Changed
- Recruiter page now includes explicit work authorization and relocation note
- Recruiter fast links now include ATS resume link
- Sitemap updated with ATS resume URL

## [0.2.1] - 2026-04-17

### Changed
- Upgraded site-wide visual system in `_layouts/default.html` (hero, KPI cards, chips, cleaner navigation)
- Added reusable top navigation include in `_includes/header.html`
- Improved homepage first screen in `index.md` with stronger value framing and action CTA
- Improved recruiter page first screen in `for-recruiters.md` with KPI-driven summary and direct contact CTA
- Refreshed `services.html` with modern visual hierarchy and clearer service framing
- Added high-conversion CTA panel on homepage with direct intro-call flow
- Added artifact-backed social proof cards on homepage

## [0.2.0] - 2026-04-17

### Added
- `CONTRIBUTING.md` with contribution workflow and quality rules
- `CODE_OF_CONDUCT.md`
- `SECURITY.md` with private disclosure process
- GitHub issue templates (bug report and feature request)
- Pull request template
- Community health config for issue forms
- Demo snapshot assets in `docs/assets/` for quick-start, machine-readable endpoints, and MCP flow

### Changed
- Repositioned `README.md` to template-first onboarding
- Added 5-minute quick start flow and high-level architecture section
- Clarified trust/governance entrypoints in README

## [0.1.0] - 2026-02-09

### Added
- Initial public version of AI-indexed portfolio/CV site
- Machine-readable profile endpoints
- MCP server and baseline workflows
