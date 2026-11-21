# Example 2 — Reconciling a dashboard rate against raw events

## Before

```text
Monthly growth review (October)
  Dashboard activation rate: 38% (window not stated).
  By-channel breakdown: 1,240 activated users across channels.
  Headline signup figure used in the same deck: 1,180 signups.

  Nobody can explain why the segments sum to more users than
  signed up, or which window the 38% uses. The 38% is quoted to
  leadership anyway.
```

The dashboard and its own breakdown disagree, and the rate carries no window — three different numbers are circulating as "activation."

## After

```text
G-CX-041 reconciliation run (October cohort, raw events):
  Signups (cohort):            1,180
  Fired report_shared ≤ 7 days:   402  → 34.1%
  Dashboard figure:               38%  → MISMATCH, reporting blocked.

Root causes found:
  1. The dashboard query used a 30-day window; the definition says 7.
  2. The by-channel summary included 60 seed/staff accounts excluded
     from the headline cohort (BAN-CX-043, BAN-CX-045).

Fixes applied at the source:
  - Dashboard query set to the defined 7-day window.
  - Non-customer accounts excluded in every activation query.
  - Re-run: dashboard 34.1%, segments sum to 402. Reconciled.
  - The rate is now published as "34.1% within 7 days of signup."
```

## Note

Corrects CX-092: when the dashboard and an independent raw-event computation disagree, reporting blocks until the discrepancy is explained and fixed at the source — the dashboard is never quoted anyway.
