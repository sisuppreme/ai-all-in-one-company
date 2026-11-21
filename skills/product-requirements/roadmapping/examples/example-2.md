# Example 2 — Promised before it was validated

## Before

A sales call needs a differentiator, so the public roadmap gains an entry the same afternoon:

> Public roadmap: "Coming soon — Slack integration: post board updates to any channel."

Internally, the integration is an unshaped Later bet: no opportunity has been selected, no assumption test has run, and engineering has never scoped Slack's API. Three months later a customer churns citing the missing integration they were promised.

## After

The internal roadmap keeps the item where the evidence puts it:

```markdown
### Later
- Meet teams inside their existing chat tools (Objective: activation in
  team accounts). Candidate solutions include a Slack integration —
  unvalidated: no assumption tests run. Review by: 2027-01-15.
```

The public roadmap carries only the outcome, framed as exploration:

> "Exploring: bringing FlowBoard updates into the tools your team already chats in."

No capability is named, no timing implied, and nothing a customer can hold the company to has been asserted. If discovery validates the Slack solution, the public entry is upgraded through the two-view consistency check (G-PR-124) at the same time as the internal one.

## Note

Corrected under PR-247: the external roadmap is deliberately less specific than the internal one and never promises a capability the internal roadmap has not validated (see also PR-250, two views, one truth).
