# trial-conversion

## Metadata

- **Owner department:** D18 Customer Experience (CX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Stripe, "Use free trial periods on subscriptions" — https://docs.stripe.com/billing/subscriptions/trials/free-trials ; Gibson Dunn, "FTC Restarts Negative Option Rulemaking After Eighth Circuit Vacatur" — https://www.gibsondunn.com/ftc-restarts-negative-option-rulemaking-after-eighth-circuit-vacatur-enforcement-under-rosca-continues/ ; FTC, "Bringing Dark Patterns to Light" (staff report, September 2022) — https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf
- **Depends on:** subscriptions, user-onboarding, activation-metrics
- **Feeds into:** churn-prevention, dunning, lifecycle-email

## When to use / Do NOT use

- **Use when:** designing, building, or changing any free-trial offer — signup flow, trial terms copy, reminder emails, trial-to-paid transition, or trial cancellation path.
- **Do NOT use when:** the offer is a money-back guarantee on a paid plan (no trial state exists; that is refunds-disputes), or for post-conversion retention offers (that is churn-prevention).

## Rules

1. **CX-101 — Terms before signup.** Before the user commits, one screen states in plain language: trial length in days, the exact calendar date of the first charge, the amount and billing interval after the trial, and whether a payment method is required now. No term appears only in linked fine print.
2. **CX-102 — Config matches copy.** The marketed trial length, price, and end behavior are configured in the billing platform exactly as written. Any mismatch between copy and configuration is a release blocker, not a copy fix.
3. **CX-103 — Real trial state.** Signup creates an actual trial subscription with an explicit trial end in the billing platform. A banner, a flag in the app's own database, or full access with a note is not a trial.
4. **CX-104 — Card decision is stated.** Card-upfront vs. no-card is a deliberate, recorded decision with its trade-off. The signup screen says which one applies before the user starts.
5. **CX-105 — Reminder before first charge.** Every trial user receives a reminder before the first charge — driven by the billing platform's trial-will-end event, which fires several days before expiry, plus an in-app notice — naming the charge date and amount. No first charge is ever the first notice.
6. **CX-106 — Express informed consent.** Conversion to paid rests on the consent captured at signup under the terms shown then (ROSCA: clear disclosure, express informed consent, simple cancellation). If terms change mid-trial, the user is told and re-consents, or the original terms apply.
7. **CX-107 — Deliberate no-card outcome.** What happens when a no-card trial expires — invoice, pause, or cancel — is chosen and documented. A card added later for an unrelated purchase is never silently charged for the trial.
8. **CX-108 — Cancel symmetry.** Cancelling during a trial takes no more steps than starting it, completes in-product in the same medium, and takes effect immediately for billing (access runs to the stated trial end). No retention maze, no "email support to cancel."
9. **CX-109 — Earn the conversion.** In-trial prompts point the user at the activation event and unfinished value ("your report is ready to export"), never at scarcity or guilt. Prompts stop after conversion or cancellation.
10. **CX-110 — Honest urgency only.** Any countdown or deadline shown is computed from the user's real trial end and stops at zero. Deadlines that reset, extend silently, or differ per user without a stated reason are prohibited.
11. **CX-111 — Trial integrity.** Trial access expires at the configured end — never earlier, never silently extended — and no charge occurs before the stated date. An intentional extension is granted explicitly and the user is told the new end date.
12. **CX-112 — Measured honestly.** Trial start, activation, reminder delivery, conversion, and trial cancellation are instrumented. Conversion is reported with its denominator (all trial starts), and trial cancellations are reported as their own figure, not folded into churn.

## BAN list

- **BAN-CX-051 — Fake trial.** Banned: marketing a trial that has no trial state behind it — a banner over ordinary full access, or a "trial" that is a paid subscription from day one. Defeats: DET-FAKE-003. Bad: the pricing page says "14 days free"; signup creates a normal subscription and a cron job is promised to "sort out billing later." Instead: create the subscription in the billing platform with an explicit trial end matching the copy, and block release until a test-clock run proves it. Severity: BLOCK.
- **BAN-CX-052 — Silent first charge.** Banned: converting a trial to paid with no prior reminder naming the date and amount — including relying on the signup screen alone weeks later. Defeats: DET-CON-028. Bad: the user enters a card on day 1, hears nothing, and is charged on day 15 with no email or in-app notice. Instead: wire the trial-will-end event to a reminder email and an in-app notice, and test that both fire before any charge. Severity: BLOCK.
- **BAN-CX-053 — Fake countdown.** Banned: a trial or offer countdown that resets on reload, restarts per session, or shows a deadline other than the user's real trial end. Defeats: DET-FAKE-018. Bad: "Your trial offer expires in 04:59" ticks down on the upgrade modal and resets to 5:00 on every visit. Instead: display the actual days remaining from the subscription's trial end, or show no countdown at all. Severity: BLOCK.
- **BAN-CX-054 — Cancellation maze.** Banned: making trial cancellation harder than signup — extra save screens in sequence, a cancel button that errors or hides, or cancellation only via support contact. Defeats: DET-CON-015. Bad: signup is one click; cancelling requires a settings page, two retention modals, and a chat with support during business hours. Instead: one in-product cancel action with at most one optional reason question and one confirmation, effective immediately for billing. Severity: BLOCK.
- **BAN-CX-055 — Price or term switch.** Banned: charging a different amount, interval, or start date than the terms shown at signup, or quietly shortening the trial after signup. Defeats: DET-CON-016. Bad: signup promises "$12/month after your trial"; the first invoice is $15 because pricing changed during the trial and nobody was told. Instead: honor the terms shown at signup for the first charge, and present any new terms for explicit acceptance before they apply. Severity: BLOCK.

## Gates

- **G-CX-051 — Test-clock trial run (automated).** Verifies: CX-102, CX-103, CX-105, CX-111. Check: in the billing platform's test mode (Stripe test clocks or equivalent), run a shortened trial for both the card and no-card cases; assert the trial-will-end event fires, the reminder email is sent, and at expiry the subscription transitions exactly as configured. Pass: both cases transition as configured with the reminder sent before any charge. Fail: block release. Recorded in: progress.md.
- **G-CX-052 — Copy-vs-config diff.** Verifies: CX-101, CX-102, CX-104. Check: extract trial length, first-charge date logic, post-trial amount, interval, and card requirement from the signup and pricing copy; diff each against the billing configuration. Pass: zero differences. Fail: block release until copy or config changes. Recorded in: progress.md.
- **G-CX-053 — Cancel symmetry test (automated).** Verifies: CX-108. Check: scripted end-to-end run — count the steps to start a trial and the steps to cancel it in-product; assert cancel steps ≤ signup steps, cancellation completes without contacting support, and the billing state shows no charge scheduled. Pass: all assertions hold. Fail: block release. Recorded in: progress.md.
- **G-CX-054 — Consent and terms record.** Verifies: CX-106, CX-107. Check: for a test signup, retrieve the stored consent record; it must capture the exact terms version shown, the timestamp, and the documented no-card expiry behavior. Pass: record complete and terms version matches the live signup screen. Fail: block release. Recorded in: progress.md.
- **G-CX-055 — Countdown truth check.** Verifies: CX-110. Check: load the upgrade prompt twice in separate sessions and once after a reload; the deadline shown must equal the subscription's real trial end in every load and never reset. Pass: identical, correct deadline everywhere. Fail: remove the countdown and block release. Recorded in: progress.md.

## Anti-patterns

- **Value-free nagging.** In-trial upgrade prompts that appear on every screen from day one, before the user has reached any value. Catch it: prompts should be tied to activation progress; if a prompt would make sense for a user who has done nothing, it is nagging, not conversion work.
- **Reminder in the junk drawer.** The trial-ending notice exists but is sent once, to a channel the user never sees, at a time calculated to be missed. Catch it: check reminder delivery and open evidence in the trial metrics, not just that a send was logged.
- **Downgrade-by-default framing.** The post-trial plan selector pre-selects the most expensive tier with the cheaper tiers visually muted. Catch it: compare the selector against the plan the trial terms named; the stated plan is the default.
- **Win-back before goodbye.** A user who cancels mid-trial immediately receives discount pressure instead of the promised clean exit and end-of-access date. Catch it: read the first message a cancelled trial user receives; it confirms the cancellation, nothing else.

## Examples

- [Example 1 — Terms and reminder](examples/example-1.md) — violates/corrects CX-101, CX-105.
- [Example 2 — Cancellation maze](examples/example-2.md) — violates/corrects CX-108.
- [Example 3 — Fake countdown](examples/example-3.md) — violates/corrects CX-110.

## Recall anchors

- Terms on one screen, before signup: length, first-charge date, amount, card or no card.
- The trial lives in the billing platform, never in marketing copy.
- No first charge without a reminder naming the date and amount.
- Cancelling takes no more steps than joining — and always completes.
- Every deadline shown is the user's real trial end.

## Checklist

- [ ] Signup screen states trial length, first-charge date, post-trial amount and interval, and card requirement (CX-101, CX-104).
- [ ] Billing configuration diffed against the copy with zero differences (CX-102, G-CX-052).
- [ ] Test-clock run passed for both card and no-card trials, reminder fired (CX-105, CX-111, G-CX-051).
- [ ] No-card expiry behavior is chosen, documented, and configured (CX-107).
- [ ] Cancel path tested end-to-end: steps ≤ signup, in-product, effective immediately (CX-108, G-CX-053).
- [ ] Consent record stored with the exact terms version shown (CX-106, G-CX-054).
- [ ] Any countdown verified against the real trial end across sessions (CX-110, G-CX-055).
- [ ] Trial funnel events instrumented, conversion reported with its denominator (CX-112).
