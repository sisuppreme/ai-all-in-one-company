# Example 2 — Ninety percent Must

## Before

```markdown
## Scope — Release 2.0 (capacity ≈ 30 dev-days)

All items are Must have — the stakeholders agreed everything is critical.

| Item | Effort (days) |
|---|---|
| Onboarding flow | 6 |
| Billing redesign | 5 |
| CSV export | 3 |
| SSO login | 6 |
| Push notifications | 4 |
| Audit log | 3 |
| **Total Must** | **27 of 30 days (90%)** |
```

With 90% of capacity classed Must, a single three-day overrun consumes the entire contingency and forces either a slipped date or silent quality cuts.

## After

Re-triage recorded in the scope document (decider: product lead, date: 2026-11-18):

| Item | Class | Effort (days) | Objective link |
|---|---|---|---|
| Onboarding flow | Must | 6 | Activation objective |
| Billing redesign | Must | 5 | Checkout drop-off objective |
| CSV export | Must | 3 | Retention objective (top support request) |
| SSO login | Should | 6 | — |
| Audit log | Should | 3 | — |
| Push notifications | Could | 4 | — |
| Legacy importer | Won't have (this time) | — | No current objective |

Must total: 14 of 30 days ≈ 47% of capacity. Contingency: Should (9 days) and Could (4 days), cut in that order under the agreed de-scope rule.

## Note

Corrected under PR-144 and PR-145: Must effort exceeded ~60% of capacity, so re-triage was mandatory before build started; the After brings Musts to ≈47% and restores real contingency.
