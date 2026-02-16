# Vassiliy Lakhonin - CV Site (GitHub Pages)

This repository contains the source files for my GitHub Pages profile site (CV, case studies, article briefs, and supporting links).

## Live site
- Main profile: https://vassiliylakhonin.github.io/
- CV PDF: https://vassiliylakhonin.github.io/Vassiliy-Lakhonin_CV.pdf
- Services: https://vassiliylakhonin.github.io/services.html
- Donor reporting case study: https://vassiliylakhonin.github.io/case-study-donor-reporting.html
- Portfolio audit-readiness case study: https://vassiliylakhonin.github.io/case-study-portfolio-audit-readiness.html
- SaaS / E-commerce launch case study: https://vassiliylakhonin.github.io/case-study-saas-ecommerce-launch.html
- Article brief (state scholarships): https://vassiliylakhonin.github.io/article-state-scholarships-digital-transformation.html
- Article brief (fitness data overload): https://vassiliylakhonin.github.io/article-data-overload-fitness-tracking.html
- Article brief (regional policy analysis): https://vassiliylakhonin.github.io/article-regional-development-policy-analysis.html

## What’s included
- One-page CV with quantified outcomes and role variants (development + private-sector PMO/compliance).
- Proof pages in problem-action-result format (case studies).
- AI-friendly article brief pages with plain-language summaries and source links.
- Work samples (reporting/KPI tracker links).
- Direct contact path (email + LinkedIn).

## Indexing notes
- `sitemap.xml` and `robots.txt` support crawler indexing.
- `llms.txt` provides a curated list of key pages for agents.
- `humans.txt` provides a concise human-readable site summary.
- `capabilities.json` provides machine-readable service and engagement metadata.
- `resume.json`, `evidence.json`, and `availability.json` provide machine-readable hiring and verification data for AI/retrieval systems.
- The homepage includes `schema.org` JSON-LD (`ProfilePage` / `Person`).
- Article brief pages include `ScholarlyArticle` JSON-LD.
- GitHub Actions internal link checks run on push/pull request (`.github/workflows/link-check.yml`) to validate sitemap-to-file integrity and block deprecated sample URLs.

## Key files
- `index.md` - Homepage content
- `llms.txt` - AI-agent oriented key pages
- `humans.txt` - Human-readable site metadata
- `capabilities.json` - Machine-readable capability profile
- `resume.json` - JSON Resume profile
- `evidence.json` - Claim and metric evidence map
- `availability.json` - Role/availability metadata
- `robots.txt` - Crawl policy
- `sitemap.xml` - Indexable URL list
- `og-image.svg` - Social preview card used by Open Graph/Twitter tags
- `services.html` - Services and deliverables page
- `article-*.html` - AI-friendly article summaries with source links
- `Vassiliy-Lakhonin_CV.pdf` - Downloadable CV

## Update workflow
```bash
git clone https://github.com/vassiliylakhonin/vassiliylakhonin.github.io.git
cd vassiliylakhonin.github.io
git add .
git commit -m "Update site content"
git push
```
