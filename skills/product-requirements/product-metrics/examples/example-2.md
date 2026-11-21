# Example 2 — The 40% faster claim

## Before

Homepage draft, hero subheading:

> "Teams ship 40% faster with FlowBoard."

Asked where the number comes from, the team cannot answer: no event measures "shipping," no window or segment was ever defined, and no dataset exists. The figure was written because the hero needed a number.

## After

The claim is pulled until it can be computed. The metric is defined first:

```markdown
## Metric dictionary — entry IN-07 "time to first completed board"

- Event: board_completed (first occurrence per account)
- Window: rolling 28 days
- Segment: trial accounts created in the window
- Exclusions: internal test accounts; accounts with no board created
- Owner: Onboarding team
- Source: product analytics, query Q-114 (saved report)
```

Measured result for the current window: median time-to-first-board is 2.1 days for accounts using the template gallery vs. 3.4 days without — a 38% reduction, computed from query Q-114. The hero is rewritten to state exactly that, with the comparison named:

> "New teams finish their first board in a median 2.1 days with templates — 38% faster than starting blank (28-day rolling, trial accounts)."

## Note

Corrected under PR-186: no number is published unless it resolves to a dictionary definition and a queryable source; the definition (PR-183) was written before the claim, not after.
