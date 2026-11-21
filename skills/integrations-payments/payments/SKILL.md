# payments

## Metadata

- **Owner department:** D11 Integrations & Payments (IN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Stripe, "Idempotent requests" — https://docs.stripe.com/api/idempotent_requests ; Stripe, "Receive Stripe events in your webhook endpoint" — https://docs.stripe.com/webhooks
- **Depends on:** webhooks
- **Feeds into:** subscriptions, refunds-disputes, invoicing-tax

## When to use / Do NOT use

- **Use when:** a project takes a one-off payment: checkout creation, charge confirmation, order state, refunds recorded against a payment, or payment reconciliation. The provider moves the money; this skill mirrors the state.
- **Do NOT use when:** the charge recurs on a schedule (subscriptions owns the lifecycle), the money state arrives by webhook mechanics (webhooks owns receiving; this skill owns what the event means for the order), or the question is dispute evidence (refunds-disputes).

## Rules

1. **IN-001 — Server-computed amounts.** Amount, currency, and line items are computed server-side from the catalog, keyed by the plan or product ID the client names. A client-supplied amount is a defect, not a convenience.
2. **IN-002 — Idempotency key on every money call.** Every checkout creation, charge, and refund carries an idempotency key derived from the business operation (the order ID). A retry with the same key returns the original result and creates no second charge.
3. **IN-003 — Pending order first.** The order row is created in `pending` state before the provider session or PaymentIntent exists, and the provider object is created against that order. No provider charge exists without a local order to reconcile against.
4. **IN-004 — Card data never touches your servers.** Card entry is the provider's hosted checkout page or the provider's JS elements, so card data flows browser → provider directly (SAQ A posture). No PAN in requests to your endpoints, logs, metadata, or error reports.
5. **IN-005 — Entitlement comes from the webhook, never the redirect.** Access is granted only inside the verified webhook handler or a server-side API re-read of the payment object. The success page is a display state ("payment processing") and grants nothing, so a customer who closes the tab still receives what they paid for.
6. **IN-006 — The order records the provider's payment ID.** Every paid order stores the provider payment/intent ID and the provider-reported amount and currency. A local row marked paid with no provider ID is not a payment; it is a claim.
7. **IN-007 — Declines surface as failures.** A provider decline leaves the order unpaid, shows the customer an error with a retry path, and records the decline. A decline never renders as a confirmation, a "thank you" page, or a silent success.
8. **IN-008 — Reconcile the event before fulfilling.** Before an order is fulfilled, the webhook event is checked against the expected order: account, amount, currency, and state must all match. A signed event that names the wrong amount fulfills nothing.
9. **IN-009 — Refunds are recorded against the original payment.** A refund names the original provider payment ID, carries its own idempotency key, and updates the order row and entitlement in the same flow. Dashboard-only refunds with no local record are drift the reconciliation gate will flag.
10. **IN-010 — Scheduled reconciliation diff.** A scheduled job diffs local payment rows against the provider's payment list and repairs or alerts on every mismatch. The local table is a mirror; the provider is the source of truth for money state.
11. **IN-011 — Test mode end-to-end before live.** In provider test mode: a test-card purchase grants access, a double-submit produces one charge, a webhook replay produces one grant, and a decline card declines. Test keys and test-mode labeling never appear in production configuration.
12. **IN-012 — Integer minor units.** Amounts are stored and sent as integers in the provider's minor units (cents, not dollars) with the currency stated on every record. Floating-point money math is a defect.

## BAN list

- **BAN-IN-001 — The success-page grant.** Banned: granting access because the browser landed on the checkout success URL. Defeats: DET-FAKE-006. Bad: `/checkout/success` sets `plan = pro` on visit, so anyone who guesses the URL gets Pro free and no charge exists. Instead: the success page displays a processing state; entitlement flips only in the verified webhook handler (IN-005). Severity: BLOCK.
- **BAN-IN-002 — Client-priced checkout.** Banned: reading the charge amount or currency from the client request body. Defeats: DET-FAKE-006. Bad: `POST /checkout { "amount": 100 }` buys the $49 plan for $1.00 because the server trusts the posted figure. Instead: the client names the plan ID; the server computes amount and currency from the catalog (IN-001). Severity: BLOCK.
- **BAN-IN-003 — The homegrown card form.** Banned: collecting raw card number, expiry, or CVC in your own form fields — including "validating" them yourself and marking the order paid on submit. Defeats: DET-FAKE-007. Bad: custom inputs pass a Luhn check, the order is marked paid, and no provider is ever contacted; an expired card "pays" too. Instead: provider hosted checkout or provider JS elements carry the card data (IN-004), and the provider's response decides approval. Severity: BLOCK.
- **BAN-IN-004 — The keyless charge.** Banned: creating a checkout session, charge, or refund without an idempotency key. Defeats: DET-FAKE-006. Bad: a double-click on Pay creates two PaymentIntents and the customer is charged twice for one order. Instead: every money-moving call carries a key derived from the order ID (IN-002). Severity: BLOCK.
- **BAN-IN-005 — The silent decline.** Banned: rendering a declined or failed payment as a success or confirmation state. Defeats: DET-FAKE-007. Bad: the issuer declines the card and the UI shows "Payment successful — check your email for your receipt"; no charge and no receipt exist. Instead: the order stays unpaid, the decline is surfaced as an error with a retry path, and the decline is recorded (IN-007). Severity: BLOCK.

## Gates

- **G-IN-001 — Double-submit test.** Verifies: IN-002. Check: automated — in provider test mode, fire the checkout creation twice with the same idempotency key, then query the provider for charges against the order. Pass: exactly one charge exists. Fail: block shipment. Recorded in: progress.md. Simulated-provider provision (pre-provisioning): where no provider account or test-mode keys exist yet, a local simulated provider — a provider double that keeps its own charge records behind the same query surface — stands in for the provider and this check runs against it unchanged; the result is recorded as simulated in progress.md and in the product's own documentation, the run against the real provider's test mode remains required before public launch, and simulated results must never be presented as real in any user-facing surface (Real Content Rule).
- **G-IN-002 — Test-mode purchase and decline walk.** Verifies: IN-005, IN-007, IN-011. Check: automated — complete a purchase with the provider's documented success test card and assert entitlement flips only after the webhook is processed, not at the redirect; then pay with the provider's documented decline test card and assert the order stays unpaid and an error state is shown. Pass: both assertions hold. Fail: block shipment. Recorded in: progress.md. Simulated-provider provision (pre-provisioning): where no provider account or test-mode keys exist yet, a local simulated provider — a provider double issuing its own documented success and decline test instruments and delivering the entitlement webhook — stands in for the provider and this check runs against it unchanged; the result is recorded as simulated in progress.md and in the product's own documentation, the run against the real provider's test mode remains required before public launch, and simulated results must never be presented as real in any user-facing surface (Real Content Rule).
- **G-IN-003 — Reconciliation diff.** Verifies: IN-006, IN-010. Check: automated — script compares the local payments table against the provider API list for the period and exits non-zero on any row unmatched on provider payment ID, amount, or currency. Pass: zero unmatched rows. Fail: block the release and alert. Recorded in: progress.md.
- **G-IN-004 — Card-data absence scan.** Verifies: IN-004. Check: automated — grep the codebase and a sample of server request logs for PAN-shaped digit sequences and for card field names posted to the project's own endpoints; assert the checkout page loads the provider's hosted page or elements. Pass: zero hits and provider capture confirmed. Fail: block shipment. Recorded in: progress.md.
- **G-IN-005 — Webhook replay test.** Verifies: IN-005, IN-008. Check: automated — deliver the same payment-succeeded event twice through provider tooling and assert exactly one entitlement grant and one order state transition. Pass: a single effect from duplicate delivery. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The dashboard screenshot as proof.** "It shows in the provider dashboard" offered as verification of a payment flow. Catch it: ask for the reconciliation diff output (G-IN-003) and the local row's provider payment ID (IN-006); a screenshot reconciles nothing.
- **Client-side confirmation in a trench coat.** The success page "just re-checks" by calling the provider from the browser and granting access on the answer. Catch it: search for entitlement writes outside the webhook handler and the server-side re-read path; any other writer is this pattern (IN-005).
- **Display-price drift.** The page shows $49, the catalog says $49, and the charge lands at 4899 or 4901 minor units after a float conversion. Catch it: in the test purchase, compare displayed price, catalog price, and charged minor units as integers (IN-012).
- **Refund amnesia.** A refund is issued by hand in the provider dashboard; the local row still says paid and the customer keeps access. Catch it: the reconciliation diff flags provider refunds with no matching local record (IN-009, IN-010).

## Examples

- [Example 1 — Replacing the success-page grant with a webhook grant](examples/example-1.md) — corrects IN-005.
- [Example 2 — Replacing a client-priced checkout with a server-computed, idempotent one](examples/example-2.md) — corrects IN-001.
- [Example 3 — Replacing a homegrown card form with provider elements](examples/example-3.md) — corrects IN-004.

## Recall anchors

- The provider moves the money; your database only mirrors it.
- The success page grants nothing — the webhook grants.
- Server computes the amount; the client only names the plan.
- Every money call carries an idempotency key from the order ID.
- A decline is an error the customer sees, never a quiet success.

## Checklist

- [ ] Amounts, currency, and line items are computed server-side from the catalog (IN-001).
- [ ] Checkout, charge, and refund calls all carry order-derived idempotency keys (IN-002, G-IN-001).
- [ ] Card data reaches only the provider — hosted page or elements; absence scan clean (IN-004, G-IN-004).
- [ ] Entitlement flips only in the webhook handler or server-side re-read (IN-005, G-IN-002).
- [ ] Every paid order stores the provider payment ID, amount, and currency (IN-006).
- [ ] Decline test card declines visibly and leaves the order unpaid (IN-007, G-IN-002).
- [ ] Reconciliation diff runs on schedule and exits zero (IN-010, G-IN-003).
- [ ] Duplicate webhook delivery produces exactly one grant (G-IN-005).
