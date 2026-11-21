# subscriptions

## Metadata

- **Owner department:** D11 Integrations & Payments (IN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Stripe, "Subscription invoices" — https://docs.stripe.com/billing/invoices/subscription ; Stripe, "Use free trial periods on subscriptions" — https://docs.stripe.com/billing/subscriptions/trials/free-trials ; Stripe, "Receive Stripe events in your webhook endpoint" — https://docs.stripe.com/webhooks
- **Depends on:** payments, webhooks
- **Feeds into:** dunning, refunds-disputes, invoicing-tax

## When to use / Do NOT use

- **Use when:** a product sells recurring access — trials, renewals, plan changes, pauses, cancellation — and the entitlement a user sees must match what the payment provider will actually charge. This skill owns the subscription lifecycle as mirrored from the provider.
- **Do NOT use when:** the charge is one-off (payments), the work is recovering a failed renewal (dunning), or money is moving back to the customer (refunds-disputes). Do not use it to design pricing; prices come from the catalog the billing configuration mirrors.

## Rules

1. **IN-021 — The provider state machine is the model.** Local subscription status mirrors the provider lifecycle (trialing, active, past_due, canceled/unpaid). Every local transition is driven by an invoice or subscription webhook event or a verified server-side API read — nothing else moves state.
2. **IN-022 — No local timers.** No local clock, cron job, client flag, or stored date ever grants, extends, or revokes access. A date field is display data; the provider event is the transition.
3. **IN-023 — Every row carries the provider truth.** Each subscription row stores the provider subscription ID, provider customer ID, current status, and current period end. Entitlement logic never infers state from payment history, signup date, or plan name.
4. **IN-024 — Trial terms are shown before signup.** Trial length, whether a payment method is required upfront, the price at conversion, and the conversion date appear on the signup surface. A trial converts only on those terms; terms that differ at charge time from terms shown at signup are a defect.
5. **IN-025 — Trial-end behavior is configured, never inherited.** For each plan, the missing-payment-method outcome at trial end (invoice, pause, or cancel) and the with-card outcome are set explicitly in the provider configuration. Provider defaults left in place are a finding.
6. **IN-026 — No surprise conversion.** A trial-will-end warning reaches the customer before conversion (driven by the provider's trial-will-end event where offered), naming the amount and the date. A first charge the customer could not see coming is a defect, not a conversion.
7. **IN-027 — Cancellation is a provider state change.** Cancel writes to the provider, the local mirror converges to the returned state, and the customer receives a confirmation stating what access remains and until when. Whether cancellation takes effect at period end or immediately is a per-plan configured choice, stated before the customer confirms.
8. **IN-028 — Cancellation is as easy as signup.** The cancel path lives in the same channel as signup, takes no more steps than signup, and requires no call, chat, or retention gauntlet. This is the ROSCA / FTC Act Section 5 line: a negative-option offer whose cancellation is materially harder than its enrollment is an unfair-practice risk, independent of any single rule.
9. **IN-029 — Plan changes declare their arithmetic first.** Before the customer confirms an upgrade, downgrade, or interval switch, the UI states the proration behavior and the effective date. The change is executed at the provider and mirrored; it is never simulated locally and "synced later."
10. **IN-030 — One entitlement rule, read from the mirror.** Every surface — web, API, email, export — decides access by reading the same mirrored subscription state, including the one written past_due access rule handed to dunning. No page improvises its own access check.
11. **IN-031 — Reconciliation repairs missed events.** A periodic sync re-reads live subscriptions from the provider and repairs any local row whose status or period end has drifted. Webhooks are assumed losable; drift found by a customer is a defect in this sync, not bad luck.
12. **IN-032 — Mutations are idempotent and server-side.** Create, plan change, pause, resume, and cancel are executed server-side with an idempotency key derived from the business operation, so a double-click, retry, or replayed request produces exactly one effect.

## BAN list

- **BAN-IN-011 — The UI-only cancel.** Banned: a cancel button that hides the subscription in the UI while the provider keeps billing, or that revokes access the provider still shows as paid. Defeats: DET-FAKE-011. Bad: "Cancel" sets `hidden=true` on the local row; the customer is charged again at renewal and the support inbox finds out first. Instead: cancel at the provider, converge the mirror to the returned state, and confirm to the customer what remains and until when (IN-027). Severity: BLOCK.
- **BAN-IN-012 — The timer entitlement.** Banned: granting, extending, or revoking access from a local clock, a `trialEndsAt` comparison, or a client-side plan flag. Defeats: DET-FAKE-021. Bad: middleware reads `localStorage.plan === "pro"` and a `setTimeout` ends trials in the browser; editing storage grants Pro, and paying customers lose access when the tab's clock is wrong. Instead: entitlements read the mirrored provider state only (IN-022, IN-030). Severity: BLOCK.
- **BAN-IN-013 — Status ahead of the provider.** Banned: any surface displaying a subscription state the provider has not reached — "Pro active" rendered on signup success, "canceled" shown before the provider confirms. Defeats: DET-FAKE-022. Bad: the success page announces "Your Pro plan is active" while the subscription object was never created because the webhook failed; the dashboard and the invoice disagree for a week. Instead: render state from the mirror, which moves only on provider events or verified reads (IN-021). Severity: BLOCK.
- **BAN-IN-014 — The phantom plan change.** Banned: applying an upgrade or downgrade in local state only, so it shows in the app but never reaches the provider and reverts or double-charges at renewal. Defeats: DET-FAKE-016. Bad: the settings page switches the user to the annual plan locally; at renewal the provider charges the old monthly price and the "change" silently disappears. Instead: execute the change at the provider with proration stated up front, then mirror the result (IN-029). Severity: BLOCK.
- **BAN-IN-015 — The subscription that exists only in your database.** Banned: marking a customer subscribed — plan, welcome email, unlocked features — without a subscription object existing at the provider. Defeats: DET-FAKE-006. Bad: trial signup inserts a local row with status `trialing` and unlocks Pro; no provider subscription was created, so nothing ever converts, renews, or can be canceled. Instead: create the subscription at the provider first; the local row is its mirror and carries its ID (IN-023). Severity: BLOCK.

## Gates

- **G-IN-011 — Test-clock lifecycle walk.** Verifies: IN-021, IN-025, IN-026. Check: automated — in test mode with a provider test clock, create a trialing subscription, advance the clock, and assert in order: the trial-will-end warning is sent, the conversion charge matches the terms shown at signup, a decline card moves the mirror to past_due, and a card update returns it to active. Pass: every transition lands in the configured local state. Fail: block shipment. Recorded in: progress.md.
- **G-IN-012 — Missed-webhook drill.** Verifies: IN-031. Check: automated — disable the webhook endpoint for one renewal cycle in test mode, let the renewal happen, re-enable the endpoint, and run the reconciliation sync. Pass: the sync repairs the mirror to the provider's state with no manual edit. Fail: block shipment; the sync is part of the feature, not an enhancement. Recorded in: progress.md.
- **G-IN-013 — Cancel-path verification.** Verifies: IN-027, IN-028. Check: automated plus timed walkthrough — script a cancellation in test mode and assert the provider state, the local mirror, the confirmation message, and the entitlement at period end all agree; then walk signup and cancel side by side and count steps. Pass: all four records agree and cancel takes no more steps than signup. Fail: block shipment. Recorded in: progress.md.
- **G-IN-014 — Trial-terms surface diff.** Verifies: IN-024, IN-025. Check: automated — extract the trial length, card requirement, conversion price, and trial-end behavior from the signup surface and diff them against the provider product/price and subscription configuration. Pass: zero differences, and both card and no-card trial-end outcomes are explicitly configured. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The second state machine.** A local status enum grows values the provider never emits ("grace," "pending-cancel," "vip") until nobody can say which system is right. Catch it: list local statuses next to provider statuses; any local value with no provider counterpart is deleted or demoted to a display label.
- **Webhook-only faith.** The mirror is trusted because "webhooks are reliable," and no reconciliation job exists in the repo. Catch it: search the codebase for the periodic provider re-read; if the only writer of subscription state is the webhook handler, drift is a matter of time (IN-031).
- **Retention-maze creep.** The cancel flow gains one small step per quarter — a survey, an offer modal, a "talk to us" screen — each harmless alone. Catch it: re-run the G-IN-013 step count after any cancel-flow change; growth in steps is a finding even when cancel still works.
- **Proration surprise.** Plan changes ship with the provider's default proration because nobody chose one, and the first upgraded customer is charged an amount no screen ever showed. Catch it: if the confirm screen cannot state the amount and effective date, the proration behavior was never configured (IN-029).

## Examples

- [Example 1 — The cancel button that only hid the row](examples/example-1.md) — corrects IN-027.
- [Example 2 — A browser timer replaced by the provider lifecycle](examples/example-2.md) — corrects IN-022.
- [Example 3 — The missed webhook the reconciliation sync repaired](examples/example-3.md) — corrects IN-031.

## Recall anchors

- The provider's state machine is the only state machine.
- No local timer ever grants, extends, or revokes access.
- Trials convert only on the terms shown at signup.
- Cancel at the provider, confirm to the customer, same steps as signup.
- Webhooks get missed; the reconciliation sync is not optional.

## Checklist

- [ ] Every subscription row carries provider subscription ID, status, and period end (IN-023).
- [ ] Trial-end behavior is explicitly configured for card and no-card cases (G-IN-014).
- [ ] Signup surface trial terms diff clean against the provider configuration (G-IN-014).
- [ ] Test-clock lifecycle walk passes end to end (G-IN-011).
- [ ] Missed-webhook drill: the sync repairs the mirror unaided (G-IN-012).
- [ ] Cancel verified at provider, mirror, confirmation, and entitlement — in no more steps than signup (G-IN-013).
- [ ] Plan-change screens state proration and effective date before confirmation (IN-029).
- [ ] All entitlement checks read the one mirrored state (IN-030).
