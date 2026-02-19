# Vassiliy Lakhonin - CV Site (GitHub Pages)

This repository contains the source files for my GitHub Pages profile site (CV, case studies, article briefs, and supporting links).

## Live site
- Main profile: https://vassiliylakhonin.github.io/
- Agent profile (Markdown): https://vassiliylakhonin.github.io/profile.md
- CV PDF: https://vassiliylakhonin.github.io/Vassiliy-Lakhonin_CV.pdf
- Agent card: https://vassiliylakhonin.github.io/agent-card.json
- Resume JSON: https://vassiliylakhonin.github.io/resume.json
- Evidence JSON: https://vassiliylakhonin.github.io/evidence.json
- Availability JSON: https://vassiliylakhonin.github.io/availability.json
- Engagement intake JSON: https://vassiliylakhonin.github.io/engage.json
- Verification JSON: https://vassiliylakhonin.github.io/verification.json
- Services: https://vassiliylakhonin.github.io/services.html
- Pet project (OpenClaw RBM logic model skill, Git repo): https://lnkd.in/d4dbTz6p
- Pet project listing (ClawHub): https://lnkd.in/dYuhhN8r
- Donor reporting case study: https://vassiliylakhonin.github.io/case-study-donor-reporting.html
- Donor reporting case study (Markdown): https://vassiliylakhonin.github.io/case-study-donor-reporting.md
- Portfolio audit-readiness case study: https://vassiliylakhonin.github.io/case-study-portfolio-audit-readiness.html
- Portfolio audit-readiness case study (Markdown): https://vassiliylakhonin.github.io/case-study-portfolio-audit-readiness.md
- SaaS / E-commerce launch case study: https://vassiliylakhonin.github.io/case-study-saas-ecommerce-launch.html
- SaaS / E-commerce launch case study (Markdown): https://vassiliylakhonin.github.io/case-study-saas-ecommerce-launch.md
- Article brief (state scholarships): https://vassiliylakhonin.github.io/article-state-scholarships-digital-transformation.html
- Article brief (fitness data overload): https://vassiliylakhonin.github.io/article-data-overload-fitness-tracking.html
- Article brief (regional policy analysis): https://vassiliylakhonin.github.io/article-regional-development-policy-analysis.html

## What’s included
- One-page CV with quantified outcomes and role variants (development + private-sector PMO/compliance).
- Proof pages in problem-action-result format (case studies).
- Markdown-first profile and case-study copies for agent/crawler parsing.
- AI-friendly article brief pages with plain-language summaries and source links.
- Work samples (reporting/KPI tracker links).
- Direct contact path (email + LinkedIn).

## Indexing notes
- `sitemap.xml` and `robots.txt` support crawler indexing.
- `llms.txt` provides a curated list of key pages for agents.
- `humans.txt` provides a concise human-readable site summary.
- `capabilities.json` provides machine-readable service and engagement metadata.
- `agent-card.json` provides A2A-style capability discovery metadata for agent workflows.
- `resume.json`, `evidence.json`, `availability.json`, `engage.json`, and `verification.json` provide machine-readable hiring, verification, and intake data for AI/retrieval systems.
- The homepage includes `schema.org` JSON-LD (`ProfilePage` / `Person`).
- Article brief pages include `ScholarlyArticle` JSON-LD.
- GitHub Actions internal link checks run on push/pull request (`.github/workflows/link-check.yml`) to validate sitemap-to-file integrity and block deprecated sample URLs.
- GitHub Actions indexing push (`.github/workflows/indexing-push.yml`) submits site URLs to IndexNow on each push.
- Optional Google Search Console sitemap submission runs when `GSC_SERVICE_ACCOUNT_JSON` and `GSC_SITE_URL` secrets are configured.

## Crawler policy
- `robots.txt` explicitly allows `OAI-SearchBot`, `GPTBot`, and standard crawlers for discovery.
- If policy changes later (for example, blocking model-training crawlers), update `robots.txt` and redeploy.

## Key files
- `index.md` - Homepage content
- `profile.md` - Short machine-friendly candidate profile
- `llms.txt` - AI-agent oriented key pages
- `humans.txt` - Human-readable site metadata
- `agent-card.json` - Agent discovery card (A2A-style fields)
- `capabilities.json` - Machine-readable capability profile
- `resume.json` - JSON Resume profile
- `evidence.json` - Claim and metric evidence map
- `availability.json` - Role/availability metadata
- `engage.json` - Structured outreach intake schema
- `verification.json` - Identity and cross-source proof mapping
- `robots.txt` - Crawl policy
- `sitemap.xml` - Indexable URL list
- `b8f4e0b43e38ee17c13c3a4b6cf8ea21.txt` - IndexNow key file
- `og-image.svg` - Social preview card used by Open Graph/Twitter tags
- `services.html` - Services and deliverables page
- `case-study-*.md` - Agent-friendly markdown versions of case studies
- `article-*.html` - AI-friendly article summaries with source links
- `mcp/server.py` - Local read-only MCP server for profile resources
- `Vassiliy-Lakhonin_CV.pdf` - Downloadable CV

## MCP server (local)
```bash
git clone https://github.com/vassiliylakhonin/vassiliylakhonin.github.io.git
cd vassiliylakhonin.github.io
python3 mcp/server.py
```

## Update workflow
```bash
git clone https://github.com/vassiliylakhonin/vassiliylakhonin.github.io.git
cd vassiliylakhonin.github.io
git add .
git commit -m "Update site content"
git push
```
