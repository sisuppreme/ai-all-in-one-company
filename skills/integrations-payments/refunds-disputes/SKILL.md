# refunds-disputes

## Metadata

- **Owner department:** D11 Integrations & Payments (IN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Stripe, "Idempotent requests" — https://docs.stripe.com/api/idempotent_requests ; Stripe, "Receive Stripe events in your webhook endpoint" — https://docs.stripe.com/webhooks ; Stripe dispute documentation (response window, one-shot evidence submission; checked 2026-11-21, per docs/internal/research/D11.md)
- **Depends on:** payments, webhooks
- **Feeds into:** subscriptions, invoicing-tax

## When to use / Do NOT use

- **Use when:** a customer gets money back (admin or self-serve refund, full or partial) or a cardholder dispute/chargeback arrives and needs an evidence response before its deadline.
- **Do NOT use when:** the charge itself is being created (payments), a renewal failed and recovery is still running (dunning), or the correction is to an issued invoice document rather than the payment (invoicing-tax owns credit notes).

## Rules

1. **IN-041 — Refunds execute at the provider against the original payment.** A refund names the original provider payment ID and is created through the provider's refund API. A local status change, a support macro, or a new outbound payment is not a refund.
2. **IN-042 — Idempotency key on every refund call.** The key derives from the refund request (order ID + refund sequence), so a retried request, a double-click, or a timed-out admin action returns the original refund instead of issuing a second one.
3. **IN-043 — A refund is done only when the provider confirms it.** Local payment row, entitlement, and customer notification update from provider state — the refund webhook or a server-side API re-read — never from the admin button click. Pending and failed refunds display as pending and failed.
4. **IN-044 — Reason and amount are recorded on every refund.** The refund row stores the provider refund ID, amount, currency, reason, and who initiated it. A refund with no reason is un-auditable and does not ship.
5. **IN-045 — Partial refunds state their effect before execution.** Before a partial refund runs, the flow states what happens to access and to the remaining balance, and the customer-facing copy matches it. The effect is never decided after a complaint.
6. **IN-046 — Entitlement reversal follows one written rule.** Per product, refunds reverse access immediately or at the end of the paid period — one rule, applied identically by every entitlement check, stated in the refund UI before confirmation.
7. **IN-047 — Refunds return to the original payment method only.** The payments flow never refunds to a different card, account, or wallet. Any exception is a manual, logged, out-of-band decision outside this flow.
8. **IN-048 — A dispute alerts a named owner the same day.** The dispute-created webhook creates a case assigned to a named owner, records the provider's response deadline, amount, and reason on the case, and alerts the owner queue the day the dispute opens — not at the next dashboard visit.
9. **IN-049 — Internal deadline beats the provider deadline.** Evidence assembly targets days before the provider's response window closes (Stripe documents typically 7–21 days, checked 2026-11-21). The provider deadline is the hard outer limit, never the working date.
10. **IN-050 — Evidence is matched to the dispute reason.** The pack is assembled per reason code: receipt and charge record, delivery or access logs, terms acceptance, and the customer communication record. Irrelevant bulk is omitted; the issuer gets the documents that answer the stated reason.
11. **IN-051 — Evidence submission is one-shot and final.** Submission cannot be edited or supplemented afterward, so the pack passes a completeness review against the reason checklist before anyone submits. A draft saved in the dashboard is not a submission.
12. **IN-052 — Dispute state mirrors the provider to closure.** Local dispute status changes only from provider events or API re-reads — opened, evidence submitted, won, lost, closed. Refund and dispute rates are reported metrics with alert thresholds, reviewed on a cadence, not discovered in the dashboard.

## BAN list

- **BAN-IN-021 — Label-only refund.** Banned: marking an order "refunded" in the UI or database without creating a refund object at the provider. Defeats: DET-FAKE-006. Bad: the admin clicks Refund, the order shows "Refunded," the customer waits — no provider call was ever made and no money moves. Instead: create the refund through the provider against the original payment ID (IN-041) and let provider state drive the label (IN-043). Severity: BLOCK.
- **BAN-IN-022 — "Evidence submitted" that was never submitted.** Banned: showing a dispute as answered because a draft or evidence file exists locally, while nothing was transmitted to the provider before the deadline. Defeats: DET-FAKE-022. Bad: the case reads "Evidence submitted" from an uploaded PDF; the response window closes and the dispute is lost by default. Instead: record submission only from the provider's confirmation, and work to the internal early deadline (IN-049, IN-051). Severity: BLOCK.
- **BAN-IN-023 — Refund confirmation sent before the provider confirms.** Banned: emailing "Your refund is complete" on button click, before the provider has accepted and confirmed the refund. Defeats: DET-FAKE-013. Bad: the customer is told the money is back; the provider then fails the refund and support learns about it from a chargeback. Instead: notify from the provider-confirmed state change, with the provider's expected-arrival wording (IN-043). Severity: BLOCK.
- **BAN-IN-024 — Hand-edited dispute outcome.** Banned: closing a dispute locally as won, lost, or resolved by editing the row, without a provider outcome event. Defeats: DET-FAKE-010. Bad: an admin marks a dispute "Won" to clear the queue; accounting and access decisions are made against a result the issuer never returned. Instead: dispute status converges from provider events and re-reads only, tracked to real closure (IN-052). Severity: BLOCK.
- **BAN-IN-025 — Refund authorization enforced only in the UI.** Banned: hiding the refund button from non-admin roles while the refund endpoint accepts the call from any authenticated session. Defeats: DET-FAKE-021. Bad: a support agent's session replays the refund request directly against the API and it executes. Instead: authorize the refund action server-side per request, independent of what the UI renders. Severity: BLOCK.

## Gates

- **G-IN-021 — Refund agreement test.** Verifies: IN-041, IN-042, IN-043, IN-044. Check: automated — in provider test mode, issue a full refund and a partial refund; assert a provider refund object exists for each, the local mirror matches amount and status, entitlement follows the written rule, and the notification was sent only after provider confirmation; replay one refund request with the same idempotency key and assert exactly one refund exists. Pass: all assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-IN-022 — Dispute drill.** Verifies: IN-048, IN-049. Check: automated — fire a test dispute-created event and assert the alert reaches the named owner queue the same day and a case is created with the provider deadline, reason, and an evidence checklist attached. Pass: alert and case both exist with the deadline recorded. Fail: block shipment. Recorded in: progress.md.
- **G-IN-023 — Refund/dispute reconciliation diff.** Verifies: IN-043, IN-052. Check: automated — the scheduled reconciliation compares local refund and dispute rows against the provider's lists and exits non-zero on any unmatched, mis-stated, or hand-edited row. Pass: zero drift. Fail: alert the owner and repair from provider state before the next release. Recorded in: progress.md.
- **G-IN-024 — Open-dispute deadline audit.** Verifies: IN-049, IN-050, IN-052. Check: manual — sample every open dispute: each has a named owner, the provider deadline, an internal deadline days earlier, and an evidence-pack status; none is past its internal deadline unsubmitted. Pass: every open case is inside its internal deadline with a pack in progress or submitted. Fail: escalate to the owner the same day. Recorded in: progress.md.

## Anti-patterns

- **Refund as a ticket-closer.** Issuing refunds to make support conversations end, with the reason field left generic ("goodwill") on every one. Catch it: sample refund reasons monthly; a single repeated reason across unlike cases means the record is decoration, not data (IN-044).
- **The evidence dump.** Submitting every document the company has — contracts, screenshots, unrelated logs — instead of the few that answer the dispute's reason code. Catch it: the pack index names which reason element each document answers; a document answering nothing is removed (IN-050).
- **Deadline kept in someone's head.** The response window lives in an owner's memory or a chat message instead of on the case. Catch it: any dispute without a deadline field on its record is treated as already late (IN-048).
- **Win-rate vanity.** Reporting disputes won as the headline while the dispute *rate* climbs — networks count disputes received, not disputes won, and rate thresholds are what endanger the account. Catch it: the metrics review leads with rate and refund rate, outcomes second (IN-052).

## Examples

- [Example 1 — The refund that was only a label](examples/example-1.md) — corrects IN-041 / IN-043.
- [Example 2 — The double refund on retry](examples/example-2.md) — corrects IN-042.
- [Example 3 — The dispute answered on deadline day](examples/example-3.md) — corrects IN-048 / IN-049 / IN-051.

## Recall anchors

- No provider refund object, no refund — a label is not money back.
- One key per refund request; a retry returns the original.
- The provider's deadline is the outer limit; work days earlier.
- Evidence submits once — review the pack before, not after.
- Dispute and refund state mirror the provider, never the dashboard editor.

## Checklist

- [ ] Every refund creates a provider refund against the original payment ID, with an idempotency key (IN-041, IN-042).
- [ ] Local row, entitlement, and customer notification all update from provider-confirmed state (IN-043).
- [ ] Reason, amount, and initiator recorded on every refund; partial-refund effects stated before execution (IN-044, IN-045).
- [ ] No refund path pays a destination other than the original payment method (IN-047).
- [ ] Dispute webhook alerts a named owner the same day, with deadline and reason on the case (IN-048).
- [ ] Evidence pack is reason-matched, reviewed complete, and submitted before the internal deadline (IN-049, IN-050, IN-051).
- [ ] Refund agreement test and dispute drill pass in test mode (G-IN-021, G-IN-022).
- [ ] Refund/dispute rates are reported with alert thresholds, and the last reconciliation diff was clean (IN-052, G-IN-023).
