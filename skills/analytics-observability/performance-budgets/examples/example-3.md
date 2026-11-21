# Example 3 — Quiet same-PR raise to waiver and recorded decision

## Before

One commit inside a feature pull request:

```diff
-      "javascript_kb": 300,
+      "javascript_kb": 500,
```

The feature added 180 KB of JavaScript, the gate failed, and the limit was raised in the same change so the build went green. No reason is recorded anywhere; the budget now ratifies whatever shipped.

## After

The feature PR keeps the 300 KB limit and takes a waiver, recorded in `performance-waivers.md` next to the budget file:

> **Waiver — checkout JavaScript budget.** Limit: 300 KB; observed: 480 KB. Owner: frontend lead. Reason: the payment provider's hosted-fields SDK ships as one bundle and cannot be split this release; the provider's smaller build is scheduled for evaluation next release. Expiry: 2026-12-31. On expiry the gate fails again unless the breach is fixed or this waiver is renewed as a budget decision.

If the team later decides 500 KB is genuinely acceptable, that raise lands as its own change with the reason entered in DECISIONS.md — never bundled into the change that breached the limit.

Note: corrects AN-209 and AN-210 — waivers carry an owner, a reason, and an expiry, and a raise is a recorded decision, not a quiet edit.
