# third-party-apis

## Metadata

- **Owner department:** D11 Integrations & Payments (IN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Microsoft Learn, Azure Architecture Center, "Circuit Breaker Pattern" — https://learn.microsoft.com/en-gb/azure/architecture/patterns/circuit-breaker ; Stripe, "Idempotent requests" — https://docs.stripe.com/api/idempotent_requests
- **Depends on:** api-keys-management
- **Feeds into:** payments, subscriptions, webhooks, transactional-email, sms, oauth-sso

## When to use / Do NOT use

- **Use when:** the product calls any external provider API — payments, email, SMS, maps, search, AI models, data feeds — whether adding a new integration or changing an existing one. This skill owns the wrapper every outbound call passes through.
- **Do NOT use when:** the call is to the project's own backend (api-building, D4), or the work is the provider-specific money/message semantics of a single flow (payments, webhooks, sms own those; this skill owns the shared calling discipline underneath them). Provider-specific facts live in the integration's dated annex, never in this skill.

## Rules

1. **IN-181 — One adapter per provider.** Each provider sits behind a single internal adapter module that speaks the provider's API and exposes the project's own domain interface. No provider SDK type, response object, or error shape appears outside the adapter; replacing the provider is a one-module change.
2. **IN-182 — Every call carries a timeout.** Every outbound call sets an explicit connect timeout and read timeout, sized to the caller's latency budget and recorded in the adapter's configuration. A call with no timeout is a defect, even if it has never hung yet.
3. **IN-183 — Retries are bounded and safe.** Transient failures (timeouts, 5xx, connection resets) are retried with exponential backoff and jitter, up to a configured maximum. A non-idempotent operation is retried only when it carries an idempotency key derived from the business operation; without a key it is attempted once.
4. **IN-184 — Circuit breaker per provider.** Repeated provider failures trip a circuit breaker for that provider; while open, calls fail fast into the degradation path instead of queueing behind a dead dependency. The breaker half-opens on a timer to probe recovery.
5. **IN-185 — Responses are validated before use.** Every provider response is checked against the adapter's expected schema (required fields, types, value ranges) before any field reaches domain code. A response that fails validation is an integration error, never data.
6. **IN-186 — Outage is a visible state, never empty data.** When a provider is down or a call fails after retries, the product shows its designed degradation: an explicit unavailable/stale state naming the affected feature. A provider failure is never rendered as an empty list, zero count, or "no results" — the user's data did not disappear.
7. **IN-187 — Rate limits are respected by design.** The adapter tracks the provider's documented limits (token bucket or queue where volume warrants) and treats a 429 as a backoff signal, honoring Retry-After when present. Client code never retries a 429 immediately.
8. **IN-188 — Credentials stay server-side.** Provider secret keys live in secret storage, are scoped per environment, and are used only by server-side code. The browser receives only keys the provider designed to be public, or short-lived scoped tokens the server mints. No secret appears in the client bundle, the repo, or logs.
9. **IN-189 — Contract drift alerts.** Schema-validation failures (IN-185) are logged and alerted as integration incidents, because providers change response shapes without changing version numbers. A rising validation-failure rate is treated as provider drift until proven otherwise.
10. **IN-190 — The degradation statement ships with the integration.** Every integration has a written statement, kept with its annex: what the product does when this provider is slow, down, or returning errors — which features degrade, what the user sees, and what is queued for later. No statement, no launch.
11. **IN-191 — Raw traffic is logged, secrets redacted.** Requests and responses are logged at the adapter (method, endpoint, status, latency, provider request ID) with credentials and personal data redacted, so a dispute or incident can be reconstructed from logs alone.
12. **IN-192 — Done means tested against failure.** An integration is complete only after it passes the sandbox contract suite and the failure drills (G-IN-091–G-IN-094) in staging. "It worked once in development" is not a completion state.

## BAN list

- **BAN-IN-091 — Fixture fallback sold as live.** Banned: shipping a code path that returns canned, hardcoded, or sample data when the provider call fails, times out, or was never wired up — presented to the user as the provider's real response. Defeats: DET-FAKE-009. Bad: the "AI summarizer" catches provider errors and returns one of three rotating template paragraphs; users cannot tell the model was never reached. Instead: call the provider through the adapter and surface failure per IN-186; a fallback is allowed only when it is labeled as a fallback in the UI. Severity: BLOCK.
- **BAN-IN-092 — Outage rendered as empty.** Banned: mapping a provider timeout, 5xx, or open circuit breaker to an empty list, zero count, or "nothing here yet" state. Defeats: DET-FAKE-022. Bad: the provider's outage makes the orders page show "You have no orders" for every customer for an hour. Instead: render the degradation state from the integration's statement (IN-190) — feature unavailable, data intact, retry offered. Severity: BLOCK.
- **BAN-IN-093 — Swallowed errors serving stale as current.** Banned: catching provider errors and silently returning cached or default data with no staleness marker, so figures freeze while the UI claims they are live. Defeats: DET-FAKE-004. Bad: the exchange-rate widget has shown the same rate for three days because every failed fetch falls back to the first cached value. Instead: serve cached data only with a visible "as of <time>" label, or fail into the degradation state. Severity: BLOCK.
- **BAN-IN-094 — Success claimed before provider confirmation.** Banned: telling the user an external action succeeded (ticket created, message sent, record synced) when the request was merely dispatched, or after it failed. Defeats: DET-FAKE-010. Bad: the UI toasts "Support ticket created" on submit; the helpdesk provider rejected the call, and no ticket exists. Instead: confirm from the provider's response (or its later status callback) before claiming the effect; a pending state is shown as pending. Severity: BLOCK.
- **BAN-IN-095 — First page presented as the whole dataset.** Banned: fetching one page of a provider's paginated results and rendering it as the complete list, with counts, filters, or totals computed from that page alone. Defeats: DET-FAKE-017. Bad: the catalog imports the provider's first 100 items and reports "100 products" while the provider holds 4,000. Instead: paginate to completion or query server-side, and derive every count from the same full query as the results. Severity: BLOCK.

## Gates

- **G-IN-091 — Sandbox contract suite.** Verifies: IN-181, IN-185. Check: automated — run the adapter's contract tests against the provider's sandbox/test environment (or replayed recorded fixtures where no sandbox exists), asserting request shape, auth, pagination, and response parsing for every operation the product uses. Pass: every contract test green. Fail: block the integration change. Recorded in: progress.md.
- **G-IN-092 — Dead-endpoint and latency drill.** Verifies: IN-182, IN-184, IN-186. Check: automated — in staging, point the adapter at a dead URL (e.g. `http://127.0.0.1:9`) and at a fault-injection endpoint that sleeps past the read timeout; assert each affected feature answers within its latency budget with the degradation state from its statement, and that no screen renders an empty/zero state for existing data. Pass: all assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-IN-093 — Failure-injection retry audit.** Verifies: IN-183, IN-187. Check: automated — route the adapter through a fault proxy returning, in sequence, 500, 429 with Retry-After, and a dropped connection; assert retry count never exceeds the configured maximum, backoff intervals grow, the 429 waits at least the Retry-After interval, and a non-idempotent operation without an idempotency key is attempted exactly once. Pass: all assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-IN-094 — Malformed-response fixture suite.** Verifies: IN-185, IN-189. Check: automated — replay recorded provider fixtures mutated to be malformed (missing fields, wrong types, truncated body, error payload with HTTP 200) through the adapter; assert every one is rejected by schema validation, none reaches domain code, and a drift alert is emitted per case. Pass: all fixtures rejected and alerted. Fail: block shipment. Recorded in: progress.md.
- **G-IN-095 — Secret scan.** Verifies: IN-188. Check: automated — scan the repository and the built frontend bundle for provider key patterns (e.g. `grep -rE "(sk_live|sk_test|AKIA|ghp_)[A-Za-z0-9_]+" build/ src/` plus the project's secret-scanner in CI). Pass: zero findings. Fail: block shipment and rotate any key found. Recorded in: progress.md.

## Anti-patterns

- **SDK confetti.** Provider SDK calls sprinkled through pages, handlers, and components, each with its own error handling. Catch it: grep the codebase for the provider's SDK import — every hit outside the adapter module is a violation of IN-181 waiting to hurt.
- **The infinite spinner.** A loading state with no timeout behind it, so a hung provider call becomes a permanently spinning page. Catch it: any loading UI whose underlying call lacks a configured read timeout (IN-182).
- **Copy-paste integration.** A second provider integrated by cloning the first provider's calls into feature code instead of writing its adapter. Catch it: two providers' base URLs or auth headers appearing in the same feature file.
- **Happy-path annex.** An integration annex that documents requests and success responses but no error shapes, limits, or outage behavior. Catch it: an annex with no error table and no degradation statement fails IN-190 on sight.

## Examples

- [Example 1 — An outage shown as "no orders" corrected to a degradation state](examples/example-1.md) — corrects IN-186.
- [Example 2 — Scattered provider calls consolidated behind an adapter](examples/example-2.md) — corrects IN-181.
- [Example 3 — An unbounded, retry-everything call given timeouts and safe retries](examples/example-3.md) — corrects IN-182, IN-183.

## Recall anchors

- One provider, one adapter — SDK types never escape it.
- No timeout, no call.
- Retry only what is idempotent or keyed, with backoff and a cap.
- An outage is a visible state — never empty data.
- Validate the response before a single field is used.

## Checklist

- [ ] Every provider call passes through its adapter; no SDK types leak into domain code (IN-181).
- [ ] Connect and read timeouts are configured for every outbound call (IN-182).
- [ ] Retries are bounded with backoff and jitter; non-idempotent retries carry idempotency keys (IN-183).
- [ ] Circuit breaker and degradation statement exist for this provider (IN-184, IN-190).
- [ ] Responses are schema-validated before use, and validation failures alert (IN-185, IN-189).
- [ ] Failure states render as unavailable/stale — never as empty lists or zero counts (IN-186).
- [ ] No provider secret appears in the repo, the client bundle, or logs (G-IN-095).
- [ ] Sandbox contract suite and failure drills pass in staging (G-IN-091–G-IN-094).

