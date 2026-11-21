# Example 3 — The chat-request feature

## Before

A stakeholder messages the team channel: "Enterprise prospect needs data residency in the EU — can we add region pinning this sprint?" An engineer builds it over four days. The scope document is never updated, no item is displaced, and the sprint's planned audit-log work quietly slips. Two weeks later the pricing page (updated by marketing from the chat thread) lists "EU data residency" while the help center still says all data is hosted in one region — the site contradicts itself.

## After

The request is handled as a scope change before any build starts:

```markdown
## Scope change log — Release 2.0

| Date | Change | Decider | Displaced |
|---|---|---|---|
| 2026-11-19 | Region pinning (EU) added as Must — required by signed prospect contract #114 | Product lead | Audit log demoted Must → Should; push notifications (Could) dropped from this release |
```

The scope document's classes are updated in the same edit, and the pricing page and help center are both written from the updated document, so the two surfaces agree.

## Note

Corrected under PR-148: every scope change is logged with decider, date, and what it displaced; an unlogged change is treated as never approved (see also PR-147).
