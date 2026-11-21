# queues-jobs

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** BullMQ production patterns — attempts, backoff, failed set as DLQ — https://railway.com/guides/bullmq-jobs-retry-dlq ; NestJS queue retries and dead-letter handling — https://soundscode.com/nestjs/nest-queue-retries
- **Depends on:** api-building, error-handling
- **Feeds into:** notifications, media-processing, realtime

## When to use / Do NOT use

- **Use when:** work is slow, retryable, or owed to a third party — email, media processing, webhook delivery, provider calls, scheduled work — and a user request should not wait for it or lose it.
- **Do NOT use when:** the caller needs the result to answer the request; synchronous work that is fast and local stays in the handler. Do not use a queue to hide a missing retry policy — an unconfigured queue loses work more quietly than a function call, not less.

## Rules

1. **BE-181 — Slow or third-party work is a job.** Email, media processing, webhook delivery, and provider calls are enqueued, never executed inside the request that triggered them. The request returns; the worker owns delivery.
2. **BE-182 — Enqueue with the state change.** The job is enqueued in the same database transaction as the state change that causes it (transactional outbox where the store and the queue differ). A crash between the two loses neither.
3. **BE-183 — The retry policy is explicit.** Every job type declares max attempts and exponential backoff with jitter, and names which failures are permanent. The library default — commonly 1 attempt — is never accepted silently.
4. **BE-184 — Handlers are idempotent.** Delivery is at-least-once, so a handler can run twice for the same job with a single effect. The idempotency guard is part of the handler, not a hope about the queue.
5. **BE-185 — Payloads carry IDs.** A job payload holds record IDs and the handler re-reads the record at execution time. A payload that embeds the object acts on a stale snapshot.
6. **BE-186 — The dead-letter queue is a destination.** Exhausted jobs land in an inspectable failed set / DLQ that is alerted on and replayable by an operator. A job that vanishes after its last attempt is lost work.
7. **BE-187 — Permanent failures fail fast.** A failure class that cannot succeed on retry (bad address, provider 4xx) skips the remaining attempts and goes straight to the DLQ with its reason recorded.
8. **BE-188 — Recurring jobs register once.** Scheduled jobs are registered idempotently at deploy, so a redeploy never creates a duplicate schedule.
9. **BE-189 — Progress reads job state.** Any user-facing progress, sync, or "processing" indicator is read from the job's real state. No timer, estimate, or assumption renders as progress.
10. **BE-190 — Queues are monitored.** Queue depth and oldest-job age are metrics with alert thresholds. A growing queue is an incident, not a backlog to admire.
11. **BE-191 — Every job type has an owner.** Each registered job type names an owner, its max-attempts value, and its DLQ before it ships. An unregistered job type found in code fails review.

## BAN list

- **BAN-BE-091 — Fire-and-forget side effects.** Banned: calling the email, payment, or webhook provider inline or as an unawaited promise with no queue, so a crash or rejection silently drops the work. Defeats: DET-CODE-023. Bad: `sendReceiptEmail(order)` is called without await or catch; a provider outage loses every receipt with no trace anywhere. Instead: enqueue the job in the same transaction as the order (BE-182) and let the worker own delivery. Severity: BLOCK.
- **BAN-BE-092 — Default-attempt jobs.** Banned: shipping a job type with the library's default attempt count and no backoff — choosing "lose the work" by omission. Defeats: DET-CODE-006. Bad: the queue is created with no options; the first transient provider error is also the last attempt, and the failure path is a log line. Instead: declare max attempts, exponential backoff with jitter, and the permanent-failure classes in the job's registration (BE-183). Severity: BLOCK.
- **BAN-BE-093 — The unguarded handler.** Banned: a handler with no idempotency guard on its effect (charge, send, create), so at-least-once redelivery performs the effect twice. Defeats: DET-CODE-030. Bad: the worker restarts mid-job, the payment job runs again, and the customer is charged twice for one order. Instead: key the effect on the job's idempotency key or a unique constraint and check before acting (BE-184). Severity: BLOCK.
- **BAN-BE-094 — Progress by stopwatch.** Banned: rendering "Processing… 80%" or "Sync complete" from elapsed time or a fixed script while the job is queued, failed, or never ran. Defeats: DET-FAKE-022. Bad: the UI animates to "Done" in three seconds; the transcode job is still waiting behind forty others. Instead: poll or stream the job's actual state and render only that (BE-189). Severity: BLOCK.

## Gates

- **G-BE-091 — Failure-injection test.** Verifies: BE-183, BE-184. Check: automated — in staging, kill the worker mid-job and make the provider fail the first two attempts; assert the job retries with backoff and the effect occurs exactly once. Local-harness form: where no staging environment exists, run the same drill against a local queue and worker processes — kill the local worker mid-job and make the local provider stub fail the first two attempts — under the same assertions, with the results recorded in progress.md; the staging form remains required before launch. Pass: one effect, job completed, attempts logged. Fail: block shipment. Recorded in: progress.md.
- **G-BE-092 — DLQ drill.** Verifies: BE-186, BE-187. Check: automated — submit a job whose target permanently fails (an invalid recipient address); assert it fast-fails or exhausts into the DLQ, an alert fires, and an operator replay after the input is fixed succeeds. Local-harness form: where no staging environment exists, run the same drill against a local queue and worker processes with a permanently failing target, under the same assertions, with the results recorded in progress.md; the staging form remains required before launch. Pass: parked, alerted, replayable. Fail: block shipment. Recorded in: progress.md.
- **G-BE-093 — Transactional-enqueue test.** Verifies: BE-182. Check: automated — in a test harness, force a crash at the commit boundary of a state change; then scan for orphans in both directions. Pass: no state change exists without its job, and no job without its state change. Fail: block shipment. Recorded in: progress.md.
- **G-BE-094 — Registry audit.** Verifies: BE-188, BE-191. Check: automated — diff the job types referenced in code against the job registry, asserting each has an owner, max attempts, backoff, and DLQ; deploy twice and assert recurring registrations did not duplicate. Pass: full coverage, no duplicate schedules. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The invisible backlog.** The queue grows for days and the first symptom is user complaints. Catch it: ask for the current oldest-job age; if nobody can state it, monitoring is decorative (BE-190).
- **Retry storms.** Every failed job retries at the same fixed interval, so a provider outage becomes a self-inflicted flood at the moment the provider recovers. Catch it: read the backoff configuration — no growth, no jitter, no cap is the tell.
- **The job that does everything.** One handler type branching on a `kind` field into twelve behaviors, impossible to retry, monitor, or kill separately. Catch it: count the branches in the largest handler; each behavior deserves its own job type with its own policy.
- **Cron by redeploy.** "Scheduled" work that runs because someone redeployed, or a `setInterval` living in the web process. Catch it: search the web tier for timers; schedules belong to the queue system, registered once (BE-188).

## Examples

- [Example 1 — A receipt email moved from fire-and-forget to a transactional job](examples/example-1.md) — corrects BE-182.
- [Example 2 — A retry policy and DLQ for webhook delivery](examples/example-2.md) — corrects BE-183.
- [Example 3 — An idempotent payment handler](examples/example-3.md) — corrects BE-184.

## Recall anchors

- Slow, retryable, or owed to a third party: it is a job.
- Enqueue in the same transaction as the state change.
- Delivery is at-least-once; handlers are idempotent.
- The library's default attempts is a decision — never accept it silently.
- Exhausted jobs park in the DLQ: alerted, inspectable, replayable.

## Checklist

- [ ] Every job type is registered with owner, max attempts, backoff, and DLQ (G-BE-094).
- [ ] Failure-injection test: exactly one effect after a mid-job kill and provider failures (G-BE-091).
- [ ] DLQ drill: the failed job is parked, alerted, and replayable (G-BE-092).
- [ ] No state change exists without its job, and no job without its state change (G-BE-093).
- [ ] Payloads carry IDs only; handlers re-read at execution time (BE-185).
- [ ] User-facing progress reads real job state (BE-189).
- [ ] Queue depth and oldest-job age have alert thresholds (BE-190).
