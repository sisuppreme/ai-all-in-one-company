# api-building

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OpenAPI Specification v3.1.0 — https://spec.openapis.org/oas/v3.1.0 ; Stripe, "Idempotent requests" — https://docs.stripe.com/api/idempotent_requests ; PROJECT_ANATOMY.md, "API implementation"
- **Depends on:** api-architecture, validation, error-handling
- **Feeds into:** sdk-design, admin-tools, payments

## When to use / Do NOT use

- **Use when:** implementing or reviewing any HTTP endpoint that reads or writes server state — the handler pipeline, idempotency, transactions, and response shaping for a route all live here.
- **Do NOT use when:** the question is what the API should look like (rest-conventions owns shape and naming), how a specific payload is validated (validation), or how errors are formatted in depth (error-handling). This skill assumes those decisions exist and builds handlers that honor them.

## Rules

1. **BE-001 — One handler pipeline.** Every handler runs in this order: authenticate → authorize (object-level) → validate against the schema → run the domain operation → serialize through the response mapper. No step is skipped or reordered.
2. **BE-002 — Persistence is the definition of done.** A write endpoint is done only when its effect survives a reload and is visible from a second session or client. A 200/201 response is not evidence of an effect.
3. **BE-003 — The server recomputes trusted values.** Amounts, prices, roles, and owner IDs are never taken from the request; they are looked up or recomputed server-side from the authenticated identity and stored data.
4. **BE-004 — The database arbitrates races.** Check-then-act sequences (stock, uniqueness, balance) run inside a transaction or behind a unique constraint. Application-level "check then write" without one is a defect.
5. **BE-005 — Idempotency keys on non-replayable writes.** POSTs that create orders, take payments, or send messages accept an `Idempotency-Key`: the server stores the key with a hash of the request and the first response, replays the stored response on retry, and rejects reuse of the key with a different body.
6. **BE-006 — Two exits only.** Every handler ends in the success serializer or the problem-details error path. There is no third response shape — no ad-hoc JSON, no plain-text errors, no 200-with-error.
7. **BE-007 — Long work returns 202.** Work that depends on a slow or third-party operation returns `202` with a status resource and continues as a background job (queues-jobs). The request never blocks on a provider.
8. **BE-008 — Serializers whitelist contract fields.** Responses are built by a mapper that exposes only the fields in the OpenAPI contract. Raw database rows or ORM entities are never serialized directly.
9. **BE-009 — The contract is the source of truth.** The OpenAPI description is written or updated with the endpoint, and contract tests run against the running service in CI. Implementation and contract may not drift silently.
10. **BE-010 — Multi-record writes are atomic.** A handler that changes more than one record commits all of them or none of them in a single transaction. A partial write left behind by an error is a defect.

## BAN list

- **BAN-BE-001 — Stub handler shipped as an endpoint.** Banned: a route whose body returns a constant, a fixture, or a generated ID without performing the operation, while callers treat it as done. Defeats: DET-CODE-003. Bad: `POST /orders` returns `201 { id: "ord_123" }` from a counter and writes nothing to the database. Instead: implement the real write path through the pipeline (BE-001), or keep the route unregistered until it is real. Severity: BLOCK.
- **BAN-BE-002 — Success response with no persisted effect.** Banned: a handler that reports success while discarding the submission — no record created, nothing retrievable afterward. Defeats: DET-FAKE-015. Bad: the contact-form endpoint logs the payload and returns `{ ok: true }`; no one can ever read the messages. Instead: persist the submission in the same request and make it retrievable by its owner. Severity: BLOCK.
- **BAN-BE-003 — Client-supplied role or owner trusted.** Banned: authorizing or scoping a write using a role, owner ID, or tenant ID taken from the request body, query, or headers. Defeats: DET-FAKE-021. Bad: `POST /invoices` accepts `ownerId` from the body, so any caller files invoices under another user. Instead: derive ownership from the authenticated session server-side (BE-003) and authorize the object on every request. Severity: BLOCK.
- **BAN-BE-004 — Check-then-act without a constraint.** Banned: reading a value (stock, balance, existence) and then writing based on it, with no transaction, lock, unique constraint, or atomic update between the read and the write. Defeats: DET-CODE-030. Bad: two concurrent checkouts both read `stock = 1`, both decrement, and the item is oversold. Instead: decrement atomically (`UPDATE … WHERE stock > 0` and check affected rows) or transact with a uniqueness constraint (BE-004). Severity: BLOCK.

## Gates

- **G-BE-001 — Contract test suite.** Verifies: BE-001, BE-009. Check: automated — run the contract test suite against the running service in CI; every endpoint in the OpenAPI document is exercised for shape, status codes, and error format. Pass: 100% of contract tests green. Fail: block merge. Recorded in: progress.md.
- **G-BE-002 — Persistence test per write endpoint.** Verifies: BE-002. Check: automated — for each write endpoint, perform the write, reload, and re-read the resource from a second session; assert the effect is present and identical. Pass: every write endpoint's effect survives and is visible cross-session. Fail: block shipment. Recorded in: progress.md.
- **G-BE-003 — Duplicate-submit test.** Verifies: BE-004, BE-005. Check: automated — submit the same create request twice concurrently with one idempotency key, and twice with no key where the schema forbids duplicates; assert exactly one record and one effect. Pass: single effect in both runs. Fail: block shipment. Recorded in: progress.md.
- **G-BE-004 — Trusted-value audit.** Verifies: BE-003. Check: automated grep plus review — search handlers for request-derived fields named `amount`, `price`, `total`, `role`, `ownerId`, or `tenantId` reaching a write without a server-side lookup; hand-check every hit. Pass: zero unexamined hits. Fail: warn, and fix before the endpoint ships. Recorded in: progress.md.

## Anti-patterns

- **The optimistic 200.** The handler returns success first and "handles persistence later" — or never. Catch it: for every success response, name the exact record that now exists; if you cannot, the endpoint is a stub wearing a status code.
- **The fixture fallback.** The real query is wrapped in a try/catch that silently serves sample data when the database fails. Catch it: kill the database in staging and watch whether any screen still shows plausible data.
- **Serializer by entity.** The handler returns the ORM object and trusts the framework to render it, leaking password hashes, internal flags, and other tenants' fields. Catch it: diff one raw response against the contract's field list.
- **The synchronous provider call.** The request thread waits on an email, payment, or AI provider, so provider latency becomes your latency and provider outages become yours. Catch it: any handler whose p95 is bounded by a third party's p95 belongs behind BE-007.

## Examples

- [Example 1 — Idempotency key on order creation](examples/example-1.md) — corrects BE-005, BE-003.
- [Example 2 — Stub endpoint replaced by a real write path](examples/example-2.md) — corrects BE-002.
- [Example 3 — Check-then-act race made atomic](examples/example-3.md) — corrects BE-004.

## Recall anchors

- Authenticate, authorize, validate, transact, serialize — in that order.
- A response is not an effect; persistence is the definition of done.
- The client proposes; the server recomputes.
- Retries must be safe: idempotency keys on every non-replayable write.
- Two exits only: the serializer or problem details.

## Checklist

- [ ] Every handler follows the BE-001 pipeline with no skipped step.
- [ ] Every write endpoint passes its persistence test (G-BE-002).
- [ ] No trusted value (amount, price, role, owner) is taken from the request (G-BE-004).
- [ ] Non-replayable POSTs accept and honor `Idempotency-Key` (G-BE-003).
- [ ] Check-then-act paths run in a transaction or behind a constraint (BE-004).
- [ ] Responses serialize only contract fields (BE-008).
- [ ] Contract tests are green against the running service (G-BE-001).
