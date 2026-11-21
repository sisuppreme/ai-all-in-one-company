# Example 1 — The boundary that excluded nothing

## Before

```markdown
## Scope — Release 2.0 (6 weeks)

### In scope
- New onboarding flow
- Billing page redesign
- CSV export
- SSO login
- Mobile push notifications
- Admin audit log

### Out of scope
- (to be decided)
```

Every candidate is "in," nothing is excluded, and there are no MoSCoW classes or effort estimates — so the first overrun has nothing agreed to cut.

## After

```markdown
## Scope — Release 2.0 (6 weeks, capacity ≈ 30 dev-days)

### Must have (16 days — 53% of capacity)
- New onboarding flow (Objective: raise activation from trial to first project)
- Billing page redesign (Objective: stop checkout drop-off on expired cards)

### Should have (8 days)
- CSV export
- Admin audit log

### Could have (6 days)
- Mobile push notifications

### Won't have (this time)
- SSO login — deferred: enterprise deals are not in this quarter's objective;
  revisit when two or more signed prospects require it.
```

De-scope order if the Musts overrun: Could first (push notifications), then Should (audit log).

## Note

Corrected under PR-142: a scope document with an empty Won't-have list is invalid; the After also satisfies PR-141 (four classes) and PR-144 (Must effort ≈ 53% of capacity).
