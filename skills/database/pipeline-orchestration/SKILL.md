# pipeline-orchestration

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Apache Airflow documentation, "Concepts" — https://airflow.apache.org/docs/apache-airflow/2.0.0/concepts.html
- **Depends on:** ci-cd, monitoring, alerting
- **Feeds into:** etl-pipelines, data-ingestion, backup-recovery

## When to use / Do NOT use

- **Use when:** pipelines need scheduling, dependencies, retries, and backfills under one system of record — an orchestrator (Apache Airflow's model: workflows as code-defined DAGs, tasks with explicit states) is being adopted or its discipline tightened.
- **Do NOT use when:** the job is application request handling or a CI build (use ci-cd). Orchestration owns data-pipeline time: when things run, in what order, and what happens when they fail.

## Rules

1. **DB-361 — Everything runs under the orchestrator.** No production pipeline runs on a bare cron entry or a manually started script outside the orchestrator. If it moves production data on a schedule, it is a DAG.
2. **DB-362 — Every task declares its contract.** Each task declares: schedule, dependencies, retry count and backoff, timeout, and alert target. A task missing any of the five is not production-ready.
3. **DB-363 — Tasks are idempotent.** A task retried or re-run for the same window produces the same result as one clean run. Orchestration retries are only safe because the tasks underneath converge (etl-pipelines owns the load semantics; this skill owns the assumption).
4. **DB-364 — Freshness SLAs alert first.** Every pipeline has a freshness SLA. A breach alerts the pipeline's owner before consumers notice stale data.
5. **DB-365 — Backfill is first-class.** Backfilling a historical range uses the same DAG and the same code path as scheduled runs, with the range as a parameter — never a side script.
6. **DB-366 — DAGs are versioned code.** Orchestrator configuration and DAG code live in the repository and change through review, like application code. The running system is deployed from the repo, never edited in place.
7. **DB-367 — Run history is kept.** Run state and logs are retained long enough to audit the most recent failure of every pipeline without asking anyone what happened.
8. **DB-368 — Final failure reaches a human.** When retries are exhausted, the failure alerts a named target — a person or a monitored channel. A failure recorded only in a log file has alerted nobody.
9. **DB-369 — Dependencies are explicit, never timed.** Task ordering is declared as dependencies in the DAG. Sequencing by cron offsets ("job B starts 20 minutes after job A usually finishes") is forbidden.
10. **DB-370 — One place shows every pipeline's health.** The orchestrator's UI or API shows every pipeline's last successful run, and that view is checked on a schedule against each pipeline's window.

## BAN list

- **BAN-DB-181 — The bare-cron pipeline.** Banned: a production data pipeline scheduled by a standalone cron entry outside the orchestrator. Defeats: DET-INF-004. Bad: three cron lines on one server move the billing data nightly; the server is rebuilt, the crontab is not restored, and the data silently stops for a week. Instead: the pipeline is a DAG under the orchestrator with declared retries and alerts (DB-361, DB-362). Severity: BLOCK.
- **BAN-DB-182 — The silent failure.** Banned: a pipeline whose final failure notifies nobody — no alert target, or an alert sent where no one reads it. Defeats: DET-INF-012. Bad: the DAG fails on Friday night; the failure sits in the orchestrator's log, dashboards go stale, and the team learns about it from a customer on Monday. Instead: exhausted retries alert a named, monitored target (DB-368), and freshness SLAs alert before consumers notice (DB-364). Severity: BLOCK.
- **BAN-DB-183 — The unbounded task.** Banned: a task with no timeout and no retry policy, free to hang forever or to fail permanently on its first error. Defeats: DET-CODE-033. Bad: a task deadlocks against the source database at 02:00 and is still "running" at noon, blocking every downstream task while the DAG looks merely slow. Instead: every task declares a timeout and a retry count with backoff (DB-362); a hang becomes a failure, and a failure becomes an alert. Severity: BLOCK.
- **BAN-DB-184 — The server-edited DAG.** Banned: editing DAG code or orchestrator configuration directly on the production server. Defeats: DET-INF-024. Bad: an engineer patches a schedule in the live DAG file during an incident; the next deployment from the repository silently reverts it and the incident recurs. Instead: the change goes through the repository and the normal deploy (DB-366). Severity: BLOCK.

## Gates

- **G-DB-181 — Freshness audit.** Verifies: DB-364, DB-370. Check: automated — query the orchestrator's API and assert every production pipeline shows a last successful run within its schedule window plus its freshness SLA. Pass: all pipelines inside their windows. Fail: alert the owning team and block the pipeline's next promotion until the gap is explained. Recorded in: progress.md.
- **G-DB-182 — Kill test.** Verifies: DB-362, DB-368, DB-363. Check: automated — in staging, terminate a running task and assert (a) it retries per its declared policy, (b) exhausting retries fires the alert to the named target, (c) no partial output is published downstream. Pass: all three hold. Fail: block shipment. Recorded in: progress.md.
- **G-DB-183 — Declaration scan.** Verifies: DB-362, DB-369. Check: automated — lint the DAG definitions and assert every task declares schedule, dependencies, retry count/backoff, timeout, and alert target, and that no dependency is expressed as a time offset. Pass: zero tasks missing a field, zero timed dependencies. Fail: block the DAG's release. Recorded in: progress.md.
- **G-DB-184 — Cron census.** Verifies: DB-361. Check: automated — scan production hosts' crontabs and scheduler configurations for data-pipeline jobs and diff against the orchestrator's DAG list. Pass: zero pipeline jobs outside the orchestrator. Fail: block; the stray job is migrated into a DAG before it runs again. Recorded in: progress.md.

## Anti-patterns

- **Cron lasagna.** Wrapper scripts call wrapper scripts that call the real job, each layer added during some past incident. Catch it: trace one pipeline's invocation from schedule to code; more than one hop outside the orchestrator means the layers are hiding the real entry point (DB-361).
- **The retry storm.** Retries are immediate and frequent, so a struggling source system is hammered by its own consumers until it falls over. Catch it: retry declarations show backoff (DB-362); a retry policy with no delay is a denial-of-service plan against your own source.
- **Green but stale.** Every DAG run succeeds, yet the data is old because an upstream source quietly delivered nothing. Catch it: freshness is measured on the data's arrival, not on the run's exit code (DB-364); success with zero new records is a signal, not a pass.
- **The unmonitored mailbox.** Alerts technically exist but go to a distribution list nobody reads. Catch it: name the human or channel that acknowledges the alert (DB-368) and test it in the kill test (G-DB-182); an unacknowledged test alert fails the gate.

## Examples

- [Example 1 — A cron chain replaced with a declared DAG](examples/example-1.md) — corrects DB-361.
- [Example 2 — A silent failure wired to a named alert target](examples/example-2.md) — corrects DB-368.
- [Example 3 — A hand-run backfill replaced with a first-class backfill](examples/example-3.md) — corrects DB-365.

## Recall anchors

- If it moves production data on a schedule, it is a DAG.
- Every task declares five things: schedule, dependencies, retries, timeout, alert.
- Dependencies are declared, never timed.
- Exhausted retries reach a human, not a log file.
- Backfill is a run with a range, not a side script.

## Checklist

- [ ] Every production pipeline appears in the orchestrator; the cron census is clean (G-DB-184).
- [ ] Every task declares schedule, dependencies, retries/backoff, timeout, alert target (G-DB-183).
- [ ] The kill test retries, alerts a named target, and publishes nothing partial (G-DB-182).
- [ ] Every pipeline's last success is inside its freshness window (G-DB-181).
- [ ] DAG code and configuration diff clean against the repository (DB-366).
- [ ] Run state and logs are retained through the last failure of every pipeline (DB-367).
- [ ] Backfill of a test range runs the same DAG as the schedule (DB-365).
