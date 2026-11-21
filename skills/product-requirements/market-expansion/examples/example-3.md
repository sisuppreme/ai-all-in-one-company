# Example 3 — Pilot with thresholds vs. pilot that could not die

_All product, people, dates, and figures in this example are hypothetical
and illustrative. They are a worked example of the record format, not
real-world market facts._

Scenario: LedgerLane (the hypothetical invoicing SaaS from Examples 1
and 2) has a signed CONDITIONAL GO for Germany, its conditions have
closed, and the decider has recorded a GO. Under **PR-274**, that GO
launches a pilot first — not the full market.

## Before

The pilot plan in the first draft of the readiness record reads:

> "Pilot: open sign-ups in Germany from 1 June. We'll watch activation
> and support load and expand when it feels ready. Success looks like
> strong growth."

There is no cohort limit, no end date, no success threshold, and no
kill threshold. Nothing in the plan can ever declare the pilot a
failure, and nothing schedules the decision that ends it. As **PR-274**
puts it, a pilot with no kill threshold is a launch with extra steps.
Left alone, this pilot drifts into being the full launch by inertia —
nobody ever decides to expand, and nobody can decide to stop.

## After

The pilot section is rewritten and signed before the pilot starts.
The thresholds below are written into the record on 2026-05-22, ten
days before the first pilot user is admitted — pre-registered, per
**PR-274**, not fitted to results afterwards (**PR-263**):

**Pilot definition (PR-274)**

- Cohort: first 300 German sign-ups, or 8 weeks from 2026-06-01,
  whichever comes first.
- Scope: pilot availability only — public copy says "pilot in
  Germany," checked against the record under **PR-280**; it does not
  say "now live in Germany."
- Metrics drawn from product-metrics, as PR-274 requires the project's
  own metrics to be named in advance:

| Metric (8-week pilot) | Success threshold | Kill threshold |
|---|---|---|
| Activation (account set up + first invoice sent within 7 days) | ≥ 35% of cohort | < 20% of cohort |
| First-transaction completion | ≥ 80% of attempted first payments | < 60% |
| Refund rate | ≤ 2% of transactions | > 5% |
| Support contacts per active user | ≤ 0.5 | > 1.2 |

The record also carries the exit plan the kill thresholds would
trigger (**PR-277**): how pilot users are told, in German; refunds of
prepaid amounts within 30 days of an exit decision; which data
obligations survive exit, copied from the privacy-laws register; and
the VP Product as named exit-decision owner.

**Post-pilot review (PR-278)**

The review date, 2026-07-27, is in the record from the start. The
hypothetical pilot results recorded at that review:

| Metric | Actual | Against threshold |
|---|---|---|
| Activation | 27% | Below success (35%), above kill (20%) |
| First-transaction completion | 84% | Meets success |
| Refund rate | 1.4% | Meets success |
| Support contacts per active user | 0.9 | Above success (0.5), below kill (1.2) |

No kill threshold was crossed, so EXIT is not triggered; no full
success either, so EXPAND is not earned. The decider records the
second decision **PR-278** requires, dated and signed 2026-07-27:

> **HOLD.** Pilot extended 6 weeks to 2026-09-07 with new dated
> thresholds: activation ≥ 32% and support contacts per active user
> ≤ 0.7 for the extension cohort, after the two onboarding fixes
> recorded in this review ship. Kill thresholds unchanged. Next
> review: 2026-09-07. Full launch remains unapproved; if this review
> had not been recorded, the pilot would have been HOLD by default —
> silence is never an automatic expand (PR-278).

The record's review/expiry date is updated to 2026-12-31 (**PR-279**):
after that date these verdicts are stale and cannot support a full
launch claim until the affected dimensions are re-evidenced.

## Note

Corrected under PR-274 and PR-278, with PR-277 and PR-279: a GO is a
pilot first, with success and kill thresholds pre-registered before
the pilot starts, and the pilot ends in a second written decision —
EXPAND, HOLD, or EXIT — citing actual values against those thresholds.
