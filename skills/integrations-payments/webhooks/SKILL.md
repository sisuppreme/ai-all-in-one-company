# webhooks

## Metadata

- **Owner department:** D11 Integrations & Payments (IN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Stripe, "Receive Stripe events in your webhook endpoint" — https://docs.stripe.com/webhooks ; PROJECT_ANATOMY.md, "Webhooks"
- **Depends on:** payments, api-keys-management
- **Feeds into:** subscriptions, refunds-disputes, dunning, transactional-email

## When to use / Do NOT use

- **Use when:** a project receives provider events (payments, subscriptions, disputes, delivery status) or sends events to customers: endpoint design, signature verification, deduplication, processing, replay, and delivery logging.
- **Do NOT use when:** the question is what an event means for money state (payments and subscriptions own the semantics; this skill owns receiving and processing mechanics), or the transport is a general job queue with no provider signature or delivery contract (D4 queues-jobs owns transport mechanics).

## Rules

1. **IN-101 — Verify the signature over the raw body, before parsing.** The endpoint reads the exact bytes received and verifies the provider signature with the provider's library before any JSON parsing or body-parsing middleware touches the route. A parsed-and-reserialized body fails verification and is the most common self-inflicted outage.
2. **IN-102 — Reject and log every failed verification.** A request with a missing, invalid, or stale signature (outside the provider's timestamp tolerance — Stripe's libraries default to five minutes, the replay defense) is rejected with an error status, logged with its source, and changes no state. The endpoint is public by design; the signature is the only authentication.
3. **IN-103 — Persist before you acknowledge.** On successful verification, insert the event into an events table and only then return 2xx. The 2xx is a promise that the event is durably stored, never a claim that it has been processed.
4. **IN-104 — Deduplication is a database constraint, not a check.** The events table carries a unique constraint on the provider event ID; a duplicate delivery collides on insert and is acknowledged as already-received. An application-level "look up, then insert" is a race (DET-CODE-030), not deduplication.
5. **IN-105 — Process asynchronously, never in the request.** The request handler verifies, stores, and returns; a worker processes from the queue. No provider call, email send, or multi-table write happens inside the webhook request — slow handlers time out, and timeouts are what trigger duplicate retries.
6. **IN-106 — Handlers converge state; they never increment it.** A handler sets the mirror to the event's state ("set subscription status to `past_due`"), so a duplicate, a retry, or a replay of the same event is a no-op. A handler that adds, counts, or appends per delivery double-applies on the provider's normal at-least-once delivery.
7. **IN-107 — Assume unordered delivery.** Events arrive out of order; a handler never trusts arrival order or an older event over newer state. Where the event's object state matters, re-read the current object from the provider API and converge the mirror to that, so a late `created` event cannot resurrect a canceled subscription.
8. **IN-108 — Reconcile before fulfilling.** A signed event is necessary but not sufficient: before any fulfillment or entitlement change, the event is checked against the expected local record — account, amount, currency, and state must all match. A verified event naming the wrong amount fulfills nothing and is logged for review.
9. **IN-109 — Recover missed events with a periodic provider-state sync.** A scheduled job re-reads the provider state for active objects (subscriptions, open invoices, recent payments) and repairs the mirror where it has drifted. Webhooks get missed — endpoints go down, deliveries exhaust retries — and the sync is what makes the mirror converge anyway.
10. **IN-110 — Every delivery and outcome is logged, and failures are replayable.** Each event row records receipt time, verification result, processing outcome, and attempt count; a failed processing keeps the event and retries or dead-letters it for manual replay, never drops it. Events that arrived while the endpoint or worker was down are recovered by provider resend or event re-fetch, and the replay path is tested, not assumed.
11. **IN-111 — The signing secret is a credential.** Each endpoint has its own signing secret, held in the project's secret store (never in source, config files committed to the repo, or logs), and rotatable without a code change. D7 secrets-management owns compromise response; this skill owns the per-endpoint register entry.
12. **IN-112 — Outbound webhooks follow the same discipline.** Events sent to customers are signed with a per-endpoint secret the customer can rotate, retried with backoff over days (not minutes), logged per attempt with the response received, and exposed in a delivery-status view with a customer-triggered replay. An outbound event with no delivery record is a claim, not a notification.

## BAN list

- **BAN-IN-051 — The trusted POST.** Banned: a webhook endpoint that acts on any POST claiming an event ("payment succeeded") without signature verification. Defeats: DET-FAKE-006. Bad: `POST /webhooks/stripe` with a hand-written JSON body marks an order paid and grants access — no charge exists anywhere, and anyone who finds the URL can mint paid orders. Instead: verify the signature over the raw body first (IN-101) and reject failures (IN-102). Severity: BLOCK.
- **BAN-IN-052 — Check-then-insert deduplication.** Banned: deduplicating by reading for an existing event row and inserting if absent. Defeats: DET-CODE-030. Bad: two concurrent duplicate deliveries both read "not found," both insert, and the customer is granted twice and emailed twice. Instead: a unique constraint on the provider event ID makes the duplicate collide safely (IN-104). Severity: BLOCK.
- **BAN-IN-053 — The incrementing handler.** Banned: handlers that advance state per delivery — incrementing a counter, appending a credit, counting retries as renewals. Defeats: DET-FAKE-022. Bad: the provider retries a `payment_succeeded` event once and the customer's balance is credited twice; the dashboard now reports money that never moved. Instead: handlers set the mirror to the event's state, so redelivery is a no-op (IN-106). Severity: BLOCK.
- **BAN-IN-054 — The swallowed processing failure.** Banned: catching a handler exception, returning 2xx anyway, and discarding the event. Defeats: DET-CODE-005. Bad: the fulfillment write throws, the catch block logs "ok," the provider sees success and never retries, and the paid customer silently gets nothing. Instead: the stored event keeps a failed outcome, retries or dead-letters, and is replayable (IN-110); the failure is visible, not absorbed. Severity: BLOCK.
- **BAN-IN-055 — The committed signing secret.** Banned: a webhook signing secret hardcoded in source or committed in a config file. Defeats: DET-CODE-018. Bad: `WEBHOOK_SECRET = "whsec_..."` sits in the repo, so anyone with read access can forge perfectly signed events and defeat IN-101 entirely. Instead: the secret lives in the secret store, one per endpoint, rotatable without a deploy (IN-111). Severity: BLOCK.

## Gates

- **G-IN-051 — Forgery test.** Verifies: IN-101, IN-102. Check: automated — POST a correctly shaped payment event to the endpoint with an invalid signature (and a second with a valid signature over a tampered body), then query the affected order. Pass: both requests are rejected with an error status and the order state is unchanged. Fail: block shipment. Recorded in: progress.md. Simulated-provider provision (pre-provisioning): where no provider account exists yet, the endpoint is configured with a local simulated provider's signing secret and both forgery cases are exercised against it unchanged; the result is recorded as simulated in progress.md and in the product's own documentation, the run with a real provider-issued signing secret remains required before public launch, and simulated results must never be presented as real in any user-facing surface (Real Content Rule).
- **G-IN-052 — Duplicate-delivery test.** Verifies: IN-104, IN-106. Check: automated — deliver the same real event twice through provider tooling (resend from the provider dashboard or CLI) and assert one event row, one state transition, and one side effect (one grant, one email). Pass: exactly one effect from two deliveries, including under concurrent delivery. Fail: block shipment. Recorded in: progress.md. Simulated-provider provision (pre-provisioning): where no provider account or provider tooling exists yet, a local simulated provider — a provider double that delivers validly signed events and resends the same event on demand — stands in for the provider and this check runs against it unchanged; the result is recorded as simulated in progress.md and in the product's own documentation, the run through the real provider's tooling remains required before public launch, and simulated results must never be presented as real in any user-facing surface (Real Content Rule).
- **G-IN-053 — Backlog replay test.** Verifies: IN-105, IN-109, IN-110. Check: automated — stop the worker, deliver a sequence of events (including an out-of-order pair), restart the worker, then run the provider-state sync. Pass: the mirror converges to the provider's current state, every event has a recorded outcome, and no effect is doubled. Fail: block shipment. Recorded in: progress.md.
- **G-IN-054 — Reconciliation-before-fulfillment test.** Verifies: IN-108. Check: automated — in test mode, deliver a validly signed event whose amount does not match the expected order, and assert nothing is fulfilled and the mismatch is logged. Pass: zero fulfillment, one logged mismatch. Fail: block shipment. Recorded in: progress.md.
- **G-IN-055 — Signing-secret scan.** Verifies: IN-111. Check: automated — grep the repository and committed config for signing-secret literals and provider secret prefixes (e.g. `whsec_`) and assert the endpoint reads its secret from the secret store at runtime. Pass: zero literals in the repo. Fail: block shipment and rotate the exposed secret. Recorded in: progress.md.

## Anti-patterns

- **The success redirect as a webhook substitute.** "We don't need webhooks; the success page tells us it worked." Catch it: search for entitlement or order-state writes triggered by a browser return URL — that path trusts the client completely (payments IN-005); webhooks verified under IN-101 are the only event source.
- **Verify-after-parse.** The signature check runs, but on the framework's parsed-then-reserialized JSON, so it fails intermittently and someone proposes "just skipping verification when it fails." Catch it: any code path where a verification failure can fall through to processing — the raw-body route must bypass body-parsing middleware entirely (IN-101).
- **The 200-always endpoint.** The handler returns 2xx before storing anything "to keep the provider happy," so a crash after the response loses the event permanently. Catch it: kill the process between response and insert in a drill — if the event is gone, the ack lied (IN-103).
- **Retry-blind outbound sending.** Customer webhooks are fired once, synchronously, inside the customer's triggering request, with no attempt log. Catch it: ask for the delivery record of one specific event; if none exists, delivery status is being asserted, not tracked (IN-112).

## Examples

- [Example 1 — Replacing a trusted POST with signature verification over the raw body](examples/example-1.md) — corrects IN-101.
- [Example 2 — Replacing check-then-insert with a unique constraint and a converging handler](examples/example-2.md) — corrects IN-104.
- [Example 3 — Replacing in-request processing with persist, acknowledge, and queue](examples/example-3.md) — corrects IN-105.

## Recall anchors

- Verify the signature over the raw bytes — before parsing, every time.
- Store first, acknowledge second, process third — never in the request.
- Duplicates and disorder are normal delivery, not errors; converge, don't count.
- A signed event still has to match the order before it fulfills anything.
- Missed events are certain; the periodic sync is what makes the mirror true.

## Checklist

- [ ] Signature verified over the raw body before any parsing middleware (IN-101, G-IN-051).
- [ ] Failed verifications are rejected and logged with no state change (IN-102).
- [ ] The event is durably stored before the 2xx is returned (IN-103).
- [ ] A unique constraint on the provider event ID enforces deduplication (IN-104, G-IN-052).
- [ ] Handlers set state, never increment it, and tolerate out-of-order arrival (IN-106, IN-107).
- [ ] Fulfillment reconciles account, amount, currency, and state first (IN-108, G-IN-054).
- [ ] The periodic provider-state sync runs and the replay path is tested (IN-109, IN-110, G-IN-053).
- [ ] Signing secrets are per-endpoint, in the secret store, and absent from the repo (IN-111, G-IN-055).
