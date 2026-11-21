# Example 1 — The cap that only sent an email

## Before

```text
Admin panel → AI writing assistant → Budget
  Monthly budget: [set]   Status: PROTECTED ✓
  On limit: email alerts to ops@…

Wrapper code (paraphrased): on each call, if month-to-date spend > budget,
send the alert email (once per day), then make the provider call anyway.
Result: the budget was passed on the 9th; the alert went to an unmonitored
inbox; calls ran unbounded for three more weeks until the invoice arrived.
```

The control existed, the UI claimed protection, and nothing ever stopped a call. The first real signal of overspend was the bill.

## After

```text
Config (per feature): budget_period = month, budget_owner = <named owner>,
on_limit = degrade.

Wrapper behavior: before every provider call, the wrapper reads the
server-side metered spend for the feature. At the budget limit it makes
no provider call: the feature degrades to the non-AI template path and
shows "AI drafting is paused until the next budget period," the trace
records the enforcement, and the alert fires as a notification on top of
enforcement — not instead of it.

Staging proof (G-AI-091): test budget set low, scripted traffic driven
past it; provider-call count past the cap: 0.
```

## Note

Violates AI-183 (BAN-AI-091): an alert-only cap presented as enforcement. Corrected by enforcing the budget in the wrapper before the call, degrading honestly at the limit, and proving it with the budget-guard test.
