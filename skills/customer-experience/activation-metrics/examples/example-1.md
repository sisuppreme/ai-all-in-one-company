# Example 1 — Replacing "signed up" with a validated activation event

## Before

```text
Metrics definition (wiki page, "Growth" section)
  Activation = account created.
  Activation rate (March): 100% of signups.
  Onboarding goal: "increase activation" — current plan: shorten the
  signup form from five fields to three.

Cohort check nobody ran:
  Users whose first week included creating and sharing a report
  retained at day 30 at roughly double the rate of users who only
  created an account — on this product's own event data.
```

Every signup counts as activated, so the metric cannot move and onboarding is aimed at form fields instead of first value.

## After

```text
Metrics definition (dated 2026-11-21, version 2)
  Activation event: report_shared (tracking-plan name, verified firing
  in a test session, G-CX-042).
  Window: within 7 days of signup.
  Denominator: the signup cohort of the period (CX-090).
  Validation: cohort analysis on this product's data — users firing
  report_shared within 7 days retained at day 30 measurably better
  than users who did not (G-CX-043, run recorded with the definition).
  Activation rate (March, restated): 31% of signups.
  Onboarding goal: get a new user to create and share a first report
  in the first session; the signup form is out of scope.
```

## Note

Corrects CX-082 and CX-083: activation is one instrumented core-value event with a window, validated against retention on the product's own data — never the signup itself.
