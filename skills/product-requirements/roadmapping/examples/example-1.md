# Example 1 — The feature-date timeline

## Before

```markdown
## Product roadmap 2026

| Feature | Ship date |
|---|---|
| Reporting module v2 | March 14 |
| AI insights | June 2 |
| Mobile app | September 19 |
| Marketplace integrations | November 30 |
```

Four feature names, four dates, no objectives, no discovery status. By June the dates have slipped twice, the document is quietly edited each time, and sales has already quoted "June 2" to two prospects.

## After

```markdown
## Roadmap — internal

### Now (in build, validated)
- Cut time-to-first-report for new accounts (Objective: activation).
  Discovery: opportunity tree OT-3; assumption tests AT-7, AT-9 passed.
  Acceptance criteria attached. MoSCoW: Must.

### Next (in discovery)
- Explain *why* a metric moved, in-product (Objective: weekly retention).
  Assumption tests in progress; no date.

### Later (strategic bets, not yet shaped)
- Serve field teams without reliable connectivity (Objective: new segment).
- Become the system of record for multi-entity finance teams.
  Review by: 2027-01-15. No dates.
```

The public roadmap shows the same three outcome lines with horizons only — no dates, no feature names that imply commitments.

## Note

Corrected under PR-242 and PR-243: items are outcomes linked to objectives, and Next/Later items carry no dates — a date on an unvalidated item is a promise the team has not earned.
