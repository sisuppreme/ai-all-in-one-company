# transactions-concurrency

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** PROJECT_ANATOMY.md Part 3, *Databases and migrations* (transactional DDL) and *Payments and billing* (idempotency); Ruby on Rails Guides, "Active Record Migrations" — https://guides.rubyonrails.org/v7.1.3/active_record_migrations.html
- **Depends on:** schema-design, data-access
- **Feeds into:** api-building, payments, webhooks

## When to use / Do NOT use

- **Use when:** an operation writes more than one row or table, moves money or inventory, transitions a state machine, or can be retried or run concurrently by two callers.
- **Do NOT use when:** the operation is a single atomic write the engine already guarantees, or a pure read (use sql-fundamentals). Do not wrap whole request handlers in transactions "just in case" — scope is decided per operation, below.

## Rules

1. **DB-081 — One operation, one transaction.** Every multi-write operation that must succeed or fail together runs inside a single transaction. If a failure between the writes would leave state nobody can explain, the writes belong in one transaction.
2. **DB-082 — Contended records get a lock or a version.** Money movement, inventory decrement, and state-machine transitions always run in a transaction that takes a row lock (`SELECT ... FOR UPDATE`) or checks a version column (optimistic locking). A bare read-modify-write on a contended record is a defect.
3. **DB-083 — Isolation is chosen, not inherited.** The default is read-committed plus explicit locks or version checks where contention lives. Serializable is used only where an invariant demands it — and then DB-085 applies. The choice and its reason are stated in the code or the design doc.
4. **DB-084 — Retries are idempotent.** Any operation that can be retried — by the client, a queue, or the database layer — carries an idempotency key or a natural-key upsert, so a retry never double-applies its effect.
5. **DB-085 — Serialization failures are retried, not surfaced or swallowed.** Deadlock and serialization failures are caught, logged with the operation name, and retried with backoff up to a stated cap. They are never returned as a raw 500 by default, and never caught-and-forgotten while reporting success.
6. **DB-086 — Transactions stay short and local.** No transaction is held open across an external HTTP call, a queue publish to an outside system, or user think-time. External calls happen before the transaction opens or after it commits.
7. **DB-087 — One lock order.** Code paths that lock the same tables acquire locks in a consistent, documented order (e.g. always by ascending account ID for transfers). A new path that locks in the opposite order is a defect even if it works today.
8. **DB-088 — Reports do not pin the primary.** Long-running reports and exports read from a snapshot or a replica, never from a long open transaction on the primary.
9. **DB-089 — No fire-and-forget inside a transaction.** Work spawned from inside a transaction is awaited inside it, or recorded in a transactional outbox and published after commit. An unawaited write that escapes the transaction boundary is a defect.
10. **DB-090 — Boundaries are explicit.** Transaction boundaries are visible in the service layer (an explicit transaction call per operation). Relying on per-statement autocommit across a multi-write service method is a defect, however the ORM defaults are set.

## BAN list

- **BAN-DB-041 — Check-then-act without a lock or constraint.** Banned: reading a value, deciding in application code, then writing — with no row lock, version check, atomic conditional update, or database constraint making the decision safe under concurrency. Defeats: DET-CODE-030. Bad: two simultaneous withdrawals each read a balance of 100, each pass the `>= 80` check, and the account ends at −60. Instead: one atomic `UPDATE ... SET balance = balance - $amt WHERE id = $id AND balance >= $amt`, or lock the row with `SELECT ... FOR UPDATE` inside the transaction. Severity: BLOCK.
- **BAN-DB-042 — The swallowed serialization failure.** Banned: catching a deadlock/serialization error (or any write error), logging it, and returning success anyway. Defeats: DET-CODE-005. Bad: `catch (e) { log(e) }` around a funds transfer, after which the API returns `{ ok: true }` and no money moved. Instead: retry with backoff per DB-085; if retries exhaust, return a typed error the caller can act on. Severity: BLOCK.
- **BAN-DB-043 — The escaped async write.** Banned: starting an asynchronous write inside a transaction without awaiting it, so the write survives (or vanishes) independently of commit/rollback. Defeats: DET-CODE-023. Bad: `db.insert(auditLog)` is called unawaited inside the transaction; the transaction rolls back the payment but the audit row claiming it happened stays. Instead: await the write inside the transaction, or write an outbox row in the same transaction and publish after commit. Severity: WARN.
- **BAN-DB-044 — The double-applying retry.** Banned: a retryable write operation with no idempotency key or uniqueness guard, so a timeout-and-retry applies its effect twice. Defeats: DET-CODE-030. Bad: a payment capture times out at the gateway, the worker retries, and the customer is charged twice with two ledger rows nobody can pair. Instead: the caller supplies an idempotency key stored under a unique constraint in the same transaction as the effect; a retry finds the existing row and returns its result. Severity: BLOCK.

## Gates

- **G-DB-041 — Concurrency test.** Verifies: DB-082, DB-084. Check: automated — an integration test fires two parallel requests at the same contended operation (double-spend, double-book) against a fixture and asserts exactly one effect and one clean rejection. Pass: one effect, one rejection, no negative or duplicated state. Fail: block shipment. Recorded in: progress.md.
- **G-DB-042 — Transaction-wrap check.** Verifies: DB-081, DB-090. Check: automated grep plus review — list the service methods that perform more than one write and assert each is wrapped in an explicit transaction call; any multi-write method without one fails the check. Pass: every multi-write method wrapped. Fail: block shipment. Recorded in: progress.md.
- **G-DB-043 — Forced serialization-failure test.** Verifies: DB-085, DB-084. Check: automated — a staging test runs two serializable transactions against one row to force a serialization failure and asserts the operation retries and completes exactly once. Pass: one completion, zero duplicate effects, no raw 500. Fail: block shipment. Recorded in: progress.md.
- **G-DB-044 — Boundary review.** Verifies: DB-086. Check: manual — read the body of every transaction introduced in the change and confirm it contains no external HTTP call, queue publish, or unawaited async write. Pass: zero findings. Fail: warn and hold merge until restructured. Recorded in: progress.md.

## Anti-patterns

- **The optimistic shrug.** "Concurrency is unlikely on this path" — said about a path money flows through, by someone who has not checked the traffic. Catch it: if two callers *can* run it at once, the test in G-DB-041 decides, not the shrug.
- **Lock everything.** `SELECT ... FOR UPDATE` on whole tables as the answer to every race, until deadlocks become the outage of the week. Catch it: lock the smallest contended row set, in one documented order (DB-087).
- **The retry storm.** Immediate retries with no backoff and no cap turn a one-second blip into a self-inflicted denial of service. Catch it: every retry loop names its backoff and its maximum attempts.
- **Invisible atomicity.** The author assumes the ORM "probably wraps it in a transaction" and never checks the autocommit behavior. Catch it: read the boundary in the code (DB-090); if you cannot point at it, it does not exist.

## Examples

- [Example 1 — The atomic conditional update](examples/example-1.md) — corrects DB-082.
- [Example 2 — Optimistic locking with a version column](examples/example-2.md) — corrects DB-083.
- [Example 3 — An idempotent retried write](examples/example-3.md) — corrects DB-084.

## Recall anchors

- If two callers can run it at once, it is a concurrency problem now.
- Lock the row, check the version, or make the update atomic — pick one, on purpose.
- A retry without an idempotency key is a second charge waiting for a timeout.
- Transactions never span an HTTP call.
- Serialization failures are retried with backoff — never swallowed, never raw 500s.

## Checklist

- [ ] Every multi-write operation runs inside one explicit transaction (DB-081, DB-090, G-DB-042).
- [ ] Contended records (money, inventory, state transitions) use a row lock, a version check, or an atomic conditional update (DB-082).
- [ ] The concurrency test proves exactly one effect under parallel attempts (G-DB-041).
- [ ] Every retryable operation is idempotent (DB-084).
- [ ] Deadlock/serialization failures are caught, logged, and retried with backoff (DB-085, G-DB-043).
- [ ] No transaction body contains an external call or an unawaited write (DB-086, DB-089, G-DB-044).
