# Example 2 — Vague finding vs. criterion-cited finding

## Before

> **Finding 7 — Sign-up form**
> Accessibility problems on the sign-up form. Labels are unclear and the errors are hard to see. Severity: high. Fix ASAP.

No developer can act on this: no criterion, no field named, no reproduction steps, no measured values, and "high" is asserted with no impact reasoning.

## After

> **Finding 7 — Sign-up form, email field — fails WCAG 1.4.3 Contrast (Minimum), severity: major**
> The email field's only label is placeholder text rendered #9e9e9e on #ffffff (2.7:1, below the 4.5:1 floor); the label also disappears once the field is filled, so the field's purpose is unverifiable after entry (see also 3.3.2). Reproduce: load /signup, inspect the email field before and after typing. Affected users: low-vision users cannot read the label; all users lose the label after entry. Evidence: screenshot signup-email-label.png; contrast measured on rendered colors in Chrome DevTools.

*Demonstrates AC-005 — every finding cites a success criterion, with reproduction steps and evidence.*
