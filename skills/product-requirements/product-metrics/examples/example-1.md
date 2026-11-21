# Example 1 — Signups as the North Star

## Before

```markdown
## Success metrics — Q1

North Star: total account signups.
Current: 10,240 accounts. Target: 15,000 by end of Q1.
```

Signups rise whenever ads run, including when activation is flat — most new accounts never create a project, so the "North Star" grows while customer value does not.

## After

```markdown
## Metric framework — Q1

North Star: weekly accounts that complete their first board and invite a
teammate ("activated teams"). It rises only when a customer reaches the
product's core value, and it leads revenue by one billing cycle.

Input metrics:
- Breadth: new trial starts per week (owner: Growth)
- Depth: % of trials creating a first board within 24h (owner: Onboarding)
- Frequency: weekly active teams per activated account (owner: Product)
- Efficiency: trial-to-paid conversion % (owner: Growth)

Guardrails: support tickets per activated account; monthly churn.
Definitions: see metric dictionary entries NS-01, IN-01…IN-04.
```

## Note

Corrected under PR-181 and PR-188: the North Star captures value customers get and leads revenue; vanity counts like total signups are context, never the success measure.
