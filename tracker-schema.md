# Application Tracker Schema

Canonical statuses:
- Evaluated
- Applied
- Responded
- Interview
- Offer
- Rejected
- Discarded
- SKIP

## TSV columns (recommended order)
1. id
2. date
3. company
4. role
5. status
6. fit_score (X.X/5)
7. cv_version
8. source_url
9. report_link
10. notes

## Operating rules
- One row per unique role posting.
- Update status, do not duplicate rows.
- Keep fit_score immutable after first evaluation (add note if revised).
- Weekly review: move stale items to Discarded/SKIP.
