# churn-prevention

## Metadata

- **Owner department:** D18 Customer Experience (CX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://docs.recurly.com/recurly-engage/docs/cancel-save ; https://docs.stripe.com/billing/revenue-recovery/smart-retries ; https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf
- **Depends on:** subscriptions, dunning
- **Feeds into:** feedback-loops, trial-conversion

## When to use / Do NOT use

- **Use when:** building or auditing a cancellation flow, exit survey, or save offer; configuring dunning, payment retries, or card updates; reviewing churn reasons and save outcomes; writing any copy on the cancel or win-back path.
- **Do NOT use when:** the work is trial terms and trial-end behavior (use trial-conversion — its cancellation step follows this skill's rules), subscription plan mechanics (use D11 subscriptions), or general feedback collection outside the exit moment (use feedback-loops).

## Rules

1. **CX-141 — Two churn kinds, two logs.** Voluntary churn (user cancels) and involuntary churn (payment failure) are tracked separately; every event records its kind, the stated reason or failure cause, any offer shown, and the outcome. A single blended churn number is not a reviewable record.
2. **CX-142 — Cancel in-product, in the same medium.** Cancellation is completable inside the product, in the same medium as signup, in no more steps than signup took. No path may require emailing support, calling, or waiting for a human to process the request (ROSCA's simple-cancellation duty; the FTC dark-patterns report names obstruction an enforcement target).
3. **CX-143 — One question, one offer, one confirmation.** The cancel flow contains at most: one optional exit-reason question, at most one save offer matched to that reason, and one final confirmation. No second save screen appears after the offer is declined.
4. **CX-144 — Offers matched to the stated reason.** The offer follows the reason: pause for low usage, downgrade or discount for price, support escalation for a defect or unmet need. An accepted offer is applied in the billing system in the same session, and the confirmation shows the new state.
5. **CX-145 — Decline is plain and one step.** The decline control is labeled in plain words ("Cancel my subscription"), styled no less visibly than the accept control, and never carries confirmshaming copy ("No, I don't want to save money"). One decline action completes the flow.
6. **CX-146 — Declining completes the cancellation.** When the offer is declined, cancellation takes effect immediately: the confirmation states the access end date and any final charge, and no charge is taken after that date. A cancellation that needs a later manual step is not complete.
7. **CX-147 — Exit feedback is product feedback.** Stated reasons are reviewed on a fixed cadence by a named owner, recurring reasons route to the product backlog or support with the originating records linked, and fixes are announced back to affected users where a channel exists. Reasons nobody reads are not collected.
8. **CX-148 — At-risk signals trigger help, not pressure.** Usage-drop or failed-payment signals trigger an offer of assistance — a check-in, a help article, a support path — never scare copy, fake deadlines, or loss-framed warnings the product cannot substantiate.
9. **CX-149 — Dunning runs before any non-payment cancellation.** Failed payments trigger, in the billing platform: smart retries, automatic card-account updates where the network offers them, and dunning emails containing a working payment-update link. All three run before an account is cancelled for non-payment.
10. **CX-150 — Non-payment cancellation is announced in advance.** An account is cancelled for non-payment only after the dunning sequence (CX-149) completes, and the user is told the exact end date before it arrives. No account ends silently mid-cycle.
11. **CX-151 — Save rate never justifies friction.** The save rate is reported alongside cancellation-completion rate and post-cancel complaints. Adding any step, screen, or delay to the cancel flow is forbidden unless the friction audit (G-CX-072) still passes and the reason is recorded; a step added to lift the save rate is removed.
12. **CX-152 — The billing state is the truth.** After confirmation, the billing system shows the subscription cancelled (or paused/downgraded, if an offer was accepted) with exactly the end date the confirmation stated. Any disagreement between the UI state and the billing state is a defect, found by G-CX-073, not by a charged user.

## BAN list

- **BAN-CX-071 — Phantom cancellation.** Banned: a cancel flow that displays "Your subscription is cancelled" while the subscription stays active in billing and the next charge is taken. Defeats: DET-FAKE-011. Bad: the user cancels, sees a confirmation screen, and is charged again on the renewal date because the cancel handler only hid the plan banner. Instead: complete the cancellation in the billing system in the same session and state the real end date (CX-146, CX-152). Severity: BLOCK.
- **BAN-CX-072 — Cancel path that submits nowhere.** Banned: the only cancellation route is a "request cancellation" form or email link whose submission creates no billing change and no tracked task. Defeats: DET-FAKE-015. Bad: Settings links to a form reading "Tell us why you're leaving and we'll process your cancellation"; submissions land in an unmonitored inbox and renewals continue. Instead: cancel self-serve in-product (CX-142); the reason question is optional and inside that flow (CX-143). Severity: BLOCK.
- **BAN-CX-073 — Confirmation state that lies.** Banned: a confirmation screen or email stating an access end date or "no further charges" that the billing system does not honor. Defeats: DET-FAKE-022. Bad: the confirmation says "Access until March 31 — this was your final charge," but the subscription record still shows auto-renew on and an invoice is generated April 1. Instead: generate the confirmation from the billing record after the state change lands, and verify the two agree (CX-152, G-CX-073). Severity: BLOCK.
- **BAN-CX-074 — Save offer that doesn't stick.** Banned: an accepted pause or downgrade that displays as applied but silently reverts, so the next cycle bills the original plan at the original price. Defeats: DET-FAKE-016. Bad: the user accepts a two-month pause, sees "Paused until June," and is charged in May because the pause was stored only in UI state. Instead: apply the offer as a billing-system state change and show the resulting plan, price, and resume date from that record (CX-144). Severity: BLOCK.
- **BAN-CX-075 — Fake urgency on the save offer.** Banned: a countdown timer, expiring-offer clock, or "only today" deadline on a save offer that resets, restarts, or is not enforced by any real expiry. Defeats: DET-FAKE-018. Bad: the save screen shows "This 30% offer expires in 09:59" on every visit, indefinitely. Instead: show the offer's real terms with no timer, or a deadline the billing system actually enforces (CX-144, CX-148). Severity: BLOCK.

## Gates

- **G-CX-071 — Cancel-flow walkthrough per reason.** Verifies: CX-143, CX-144, CX-146. Check (automated): as a test subscriber, run the cancel flow once per exit reason and assert: exactly one reason question and at most one offer appear; the offer matches the stated reason; accepting it changes the billing record to the offered state in the same session; declining completes the cancellation immediately; the reason, offer, and outcome are written to the churn log. Pass: every assertion true for every reason. Fail: block shipment. Recorded in: progress.md.
- **G-CX-072 — Friction audit.** Verifies: CX-142, CX-151. Check (automated): scripted click-count of signup vs. cancellation from the same starting surface, plus a check that the cancel path never leaves the product or requires a message to support. Pass: cancel steps ≤ signup steps, completed entirely in-product. Fail: block shipment until steps are removed. Recorded in: progress.md.
- **G-CX-073 — Post-cancel billing state test.** Verifies: CX-146, CX-152. Check (automated): cancel a test subscription, then query the billing system and assert: status is cancelled, the end date equals the date on the confirmation, and with a test clock advanced past that date, no further invoice is generated. Pass: all three assertions true. Fail: block shipment. Recorded in: progress.md.
- **G-CX-074 — Dunning sequence test.** Verifies: CX-149, CX-150. Check (automated): in billing test mode, fail a test payment and assert: retries are attempted, a card-update attempt or request fires, dunning emails send with a payment-update link that resolves, the account stays active through the sequence, and cancellation — with advance notice naming the end date — happens only after the sequence completes. Pass: every stage fires in order. Fail: block shipment. Recorded in: progress.md.
- **G-CX-075 — Churn-log review audit.** Verifies: CX-141, CX-147, CX-151. Check: sample the last 30 days of churn events and assert each records kind (voluntary/involuntary), reason or failure cause, offer shown, and outcome; confirm a review record exists for the period naming the owner and any reason routed to the backlog. Pass: complete records and a current review. Fail: warn; two consecutive failures block the next release. Recorded in: progress.md.

## Anti-patterns

- **Save-rate worship.** The team celebrates a rising save rate while post-cancel complaints and chargebacks climb — retention by exhaustion. Catch it by reading the save rate only next to the completion rate and complaint count (CX-151); if they move in opposite directions, the flow got worse, not better.
- **Reason-blind roadmap.** Exit reasons are collected faithfully and never opened, so the top fixable reason ships in no release. Catch it at the review cadence: if no reason has been routed anywhere in a full cycle, the survey is decoration and the review (CX-147) is not happening.
- **Win-back barrage.** A cancelled user gets a sequence of escalating win-back emails after choosing to leave. Catch it by capping post-cancel contact at one message and checking the suppression list actually excludes completed cancellations.
- **Pause preselected.** The save screen pre-checks "Pause instead" so a user who clicks through quickly pauses rather than cancels, then is charged at resume. Catch it by requiring the user's explicit selection — no option on the cancel path starts pre-chosen.

## Examples

- [Example 1 — The cancel button that went nowhere](examples/example-1.md) — violates/corrects CX-142, CX-143 (BAN-CX-072).
- [Example 2 — One discount popup for every reason](examples/example-2.md) — violates/corrects CX-144, CX-145 (BAN-CX-075).
- [Example 3 — The failed card that silently ended the account](examples/example-3.md) — violates/corrects CX-149, CX-150.

## Recall anchors

- Cancel takes no more steps than signup — ever.
- One question, one matched offer, one confirmation.
- Declining the offer is the cancellation completing, not a detour.
- A trapped customer is a liability, not a save.
- Failed payment is a billing problem to fix before it is a churn event.

## Checklist

- [ ] Cancellation completes in-product, in the same medium, in ≤ signup steps (CX-142, G-CX-072).
- [ ] Flow is one optional reason question, at most one matched offer, one confirmation (CX-143, G-CX-071).
- [ ] Every offer matches its stated reason and applies in billing when accepted (CX-144, G-CX-071).
- [ ] Decline is plain, one step, free of confirmshaming, and completes the cancellation (CX-145, CX-146).
- [ ] Confirmation end date and final charge match the billing record exactly (CX-152, G-CX-073).
- [ ] Dunning — retries, card updates, linked emails — runs before any non-payment cancellation, with advance notice (CX-149, CX-150, G-CX-074).
- [ ] Voluntary and involuntary churn logged separately with reason, offer, and outcome (CX-141, G-CX-075).
- [ ] Exit reasons reviewed on cadence and routed to the backlog by a named owner (CX-147, G-CX-075).
