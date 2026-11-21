# Example 1 — Scan-only report vs. four-pass audit

## Before

> **Accessibility audit — summary**
> Ran axe-core against the home page, pricing page, and checkout. Result: 0 critical violations.
> Conclusion: the site is WCAG 2.2 AA compliant and accessible.

No other pass was run. The checkout's card form is built from clickable `<div>`s that keyboard focus never reaches, and a sticky cookie banner fully covers the focused "Pay now" button — both invisible to the scanner's rule set, both blocking real users.

## After

> **Accessibility audit — summary (2026-11-21, build 4f2c1a)**
> Scope: home, pricing, and the complete checkout process (cart → details → payment → confirmation), target WCAG 2.2 AA.
> Method: (1) axe-core scan over all in-scope URLs, report archived; (2) keyboard-only walk of checkout; (3) NVDA + Chrome smoke test of checkout; (4) visual checks at 200%/400% zoom with contrast measurement.
> Result: 31 of 55 in-scope criteria support, 6 partially support, 3 do not support, 15 not applicable. Critical findings: checkout payment controls are non-keyboard-operable `<div>`s (2.1.1, 4.1.2); focused "Pay now" button fully obscured by the sticky cookie banner (2.4.11). Full per-criterion table and findings register attached.

*Demonstrates AC-002 — automated tools are one pass, never the audit.*
