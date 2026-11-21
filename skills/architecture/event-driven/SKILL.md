# event-driven

## Metadata

- **Owner department:** D2 Architecture & System Design (AR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Fowler, "What do you mean by 'Event-Driven'?" — https://www.martinfowler.com/articles/201701-event-driven.html ; AsyncAPI Specification 3.1.0 — https://www.asyncapi.com/docs/reference/specification/v3.1.0 ; CloudEvents (CNCF envelope attributes) — http://cloudevents.io/ ; Zalando event guidelines (events as interface, compatibility, no sensitive personal data) — https://opensource.zalando.com/restful-api-guidelines/
- **Depends on:** architecture-patterns, api-architecture, adr-writing
- **Feeds into:** queues-jobs, notifications, realtime

## When to use / Do NOT use

- **Use when:** components communicate through events or messages: introducing a broker or stream, defining an event type, making consumers reliable, or auditing an existing event flow for coupling and correctness.
- **Do NOT use when:** a synchronous call is the honest shape of the interaction (the caller needs the answer to proceed) — use api-architecture and make the call. Do not use this skill to justify a broker for a system with no independent consumers; that is the decorative-infrastructure failure in architecture-patterns.

## Rules

1. **AR-201 — Name the pattern first.** Choose and record which pattern applies — event notification, event-carried state transfer, event sourcing, or CQRS — before building; the four have different consistency and coupling consequences and are not interchangeable.
2. **AR-202 — Events are facts.** Events are named in the past tense (`OrderPlaced`, `PaymentFailed`) and state something that already happened; an event is never a command a producer secretly depends on one specific consumer executing.
3. **AR-203 — Every event is a contract.** Each event type has an entry in the AsyncAPI document, a versioned payload schema, a named owner, and a list of known consumers.
4. **AR-204 — CloudEvents envelope.** Every event carries the standard envelope attributes — `specversion`, `id`, `source`, `type` — so events stay routable and deduplicatable across brokers and vendors.
5. **AR-205 — Publication is atomic.** Events are published atomically with the business write (transactional outbox or an event store). Writing to the database and then publishing as a separate step is a defect.
6. **AR-206 — Consumers are idempotent.** A consumer deduplicates on event `id` and `source` and produces the same effect whether an event arrives once or five times.
7. **AR-207 — Ordering scope is stated.** Each stream declares its ordering scope (per aggregate or per key, via partitioning), and consumers tolerate out-of-order delivery within that scope.
8. **AR-208 — Poison messages go to a dead-letter queue.** After bounded retries, a failing message lands in a DLQ with an alert. Infinite retry and silent dropping are both forbidden.
9. **AR-209 — Minimum payload.** Payloads carry only the data the chosen pattern requires. Full entity snapshots under event-carried state transfer require an explicit ADR, and events never carry sensitive personal data beyond need.
10. **AR-210 — A replay procedure exists.** Every stream documents how a consumer rebuilds state or reprocesses from a chosen point, and the procedure is exercised before it is needed in an incident.
11. **AR-211 — Schema evolution is compatibility-checked.** New payload schema versions are checked against the previous version under the compatibility rules (additive changes safe; removals and retypes breaking) before deployment.
12. **AR-212 — Consumers fail independently.** A producer keeps working while any consumer is down, and when the consumer returns, the backlog drains with no duplicate effects applied.

## BAN list

- **BAN-AR-101 — A command in event's clothing.** Banned: naming or using an event as an imperative command that one named consumer is expected to execute. Defeats: DET-CODE-008. Bad: the checkout service publishes `SendWelcomeEmail` and its success metric assumes the email service "event consumer" ran — the producer is coupled to a specific consumer's behavior while pretending to be decoupled. Instead: publish the fact (`UserRegistered`) and let the email service decide, as a known consumer, to send the email. Severity: BLOCK.
- **BAN-AR-102 — Dual-write publication.** Banned: writing to the database and publishing the event as two uncoordinated steps. Defeats: DET-CODE-030. Bad: the handler commits the order, then calls the broker; the process crashes between the two and the order exists with no event — downstream systems never learn of it, and nothing detects the gap. Instead: write the event to an outbox table in the same transaction as the order, and let a relay publish from the outbox. Severity: BLOCK.
- **BAN-AR-103 — Swallowed poison messages.** Banned: a consumer catching all exceptions, acknowledging the message, and moving on with no record. Defeats: DET-CODE-005. Bad: a malformed event fails parsing, the catch block logs nothing, the message is acked, and 4,000 orders silently never reach fulfillment. Instead: bounded retries, then the dead-letter queue with an alert and the payload preserved for inspection. Severity: BLOCK.
- **BAN-AR-104 — Unversioned payload changed in place.** Banned: changing a published event's payload shape without a new schema version and compatibility check. Defeats: DET-CODE-032. Bad: `amount` is renamed to `amount_minor` in the producer on Friday; every consumer built against the old shape fails or, worse, reads a missing field as zero. Instead: add the new field, keep the old one through the deprecation window, and bump the schema version with a compatibility check in CI. Severity: BLOCK.

## Gates

- **G-AR-101 — Contract and compatibility check.** Verifies: AR-203, AR-211. Check: automated — the AsyncAPI document validates in CI, and each new payload schema is compatibility-checked against its previous version. Pass: validation exits 0 and no unapproved breaking schema change. Fail: block merge. Recorded in: progress.md.
- **G-AR-102 — Replay and duplicate-delivery test.** Verifies: AR-206, AR-210. Check: automated — recorded events are replayed against consumers in CI, with each event delivered twice. Pass: final state equals the single-delivery state; no duplicate effects. Fail: block release. Recorded in: progress.md.
- **G-AR-103 — Consumer-outage test.** Verifies: AR-212. Check: mechanized manual — in staging, disable one consumer, run normal producer traffic, then restore the consumer. Pass: producers are unaffected while it is down, and the backlog drains afterward with no duplicates applied. Fail: block release until the consumer is decoupled. Recorded in: progress.md.
- **G-AR-104 — Outbox path check.** Verifies: AR-205. Check: automated — search the codebase for direct broker-publish calls outside the outbox relay module. Pass: none found; all publication flows through the outbox. Fail: block merge. Recorded in: progress.md.

## Anti-patterns

- **Event spaghetti.** Events trigger events trigger events, and no inventory exists, so nobody can say what happens when an order is placed. Catch it: pick one business action and trace its full event chain from the AsyncAPI document alone; if the trace needs the code, the inventory failed.
- **Request/reply in disguise.** A producer publishes an "event" and blocks waiting for a response event, rebuilding synchronous coupling with worse tooling. Catch it: any producer that cannot finish its transaction without a consumer's answer is a call, not an event.
- **The snapshot firehose.** Full entity snapshots published on every field change "just in case," coupling every consumer to the producer's entire schema and leaking personal data into the stream. Catch it: compare payload contents against the minimum-payload rule; fields no consumer reads are removed.
- **Retry as error handling.** Failures are met with longer retry loops instead of a DLQ and an alert, so poison messages surface only when users complain. Catch it: find the DLQ and its alert; if either is missing, retries are the error handling.

## Examples

- [Example 1 — `SendWelcomeEmail` becomes `UserRegistered`](examples/example-1.md) — corrects AR-202.
- [Example 2 — Dual write becomes a transactional outbox](examples/example-2.md) — corrects AR-205.
- [Example 3 — The poison message gets a DLQ, not a loop](examples/example-3.md) — corrects AR-208, AR-206.

## Recall anchors

- Name the pattern before building anything.
- Events are facts in the past tense, never commands.
- Publish atomically: outbox or event store, never dual write.
- Consumers deduplicate, tolerate disorder, and dead-letter poison.
- A consumer down must never take the producer with it.

## Checklist

- [ ] The pattern (notification, state transfer, event sourcing, CQRS) is named and recorded (AR-201).
- [ ] Every event type has an AsyncAPI entry, a versioned schema, an owner, and known consumers (AR-203).
- [ ] Every event carries the CloudEvents envelope attributes (AR-204).
- [ ] Outbox path check passes: no direct broker publishes outside the relay (G-AR-104).
- [ ] Replay test passes with duplicate delivery producing no duplicate effects (G-AR-102).
- [ ] Consumer-outage test passed in staging within the current release cycle (G-AR-103).
- [ ] Every stream has a DLQ with an alert and a documented replay procedure (AR-208, AR-210).
