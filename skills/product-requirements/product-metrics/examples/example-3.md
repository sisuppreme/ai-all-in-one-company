# Example 3 — The definition that changed quietly

## Before

In March, an analyst edits the dictionary entry for "active account" from *any activity in the last 28 days* to *any activity in the last 7 days*, to match a new dashboard vendor's default. No note is made. April's review shows active accounts "down 31%," the team spends two weeks hunting a churn problem that does not exist, and the about page (still citing the 28-day figure) now contradicts the dashboard.

## After

The same change, made as a versioned definition change:

```markdown
## Metric dictionary — entry AC-02 "active account"

- Definition (v3, from 2026-03-01): account with ≥1 meaningful activity
  event in the last 7 days.
- Owner: Product analytics
- Source: warehouse table analytics.account_activity

### Changelog
- v3 — 2026-03-01: window changed 28 days → 7 days to align with the
  weekly reporting cadence. Figures before 2026-03-01 are not comparable;
  dashboards show a break marker at 2026-03-01. (Requested by: analytics
  lead; approved by: product lead.)
- v2 — 2025-11-15: bot traffic excluded.
```

April's review reads the trend within v3 only, the break is visible on every chart, and the about page is updated in the same change.

## Note

Corrected under PR-185: definition changes are versioned changelog entries with date, old and new definition, and reason — silent redefinition is how dashboards start lying.
