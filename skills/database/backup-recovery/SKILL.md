# backup-recovery

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** PROJECT_ANATOMY.md Part 5, *Backups* (restore-tested discipline); pgvector documentation (PostgreSQL point-in-time recovery as a platform property) — https://access.crunchydata.com/documentation/pgvector/0.8.3/pdf/pgvector.pdf
- **Depends on:** schema-design, migrations
- **Feeds into:** read-replicas, data-warehousing

## When to use / Do NOT use

- **Use when:** setting up or reviewing a production database's backup schedule, retention, restore procedure, or recovery objectives — and before any launch that puts real data at risk.
- **Do NOT use when:** the data is disposable development state, or the question is deploy rollback of code (that is the deployment skill's ground). A replica is not a backup: replication faithfully copies deletions and corruption, and this skill never counts it as one.

## Rules

1. **DB-201 — Backups are automated and scheduled.** Periodic base backups plus continuous WAL archiving for point-in-time recovery on PostgreSQL (or the engine's equivalent), running without human initiation.
2. **DB-202 — Retention is written, and one copy lives elsewhere.** Retention tiers (daily/weekly/monthly) are stated in writing, and at least one copy sits outside the primary provider account and region.
3. **DB-203 — Restore drills run on a schedule.** At least quarterly, a drill restores into a scratch environment; the measured RTO (elapsed time) and RPO (recovery point achieved) are recorded in the runbook.
4. **DB-204 — A missed backup alerts like an outage.** Backup jobs are monitored; a failed or skipped backup pages with the same urgency as downtime.
5. **DB-205 — Keys live apart from backups.** Backup credentials and encryption keys are stored separately from the backups themselves, so one compromise does not yield both.
6. **DB-206 — Deletion is a separate privilege.** Deleting backups requires a distinct permission from routine operations; the role that runs the app cannot erase its recovery path.
7. **DB-207 — Per-tenant restore limits are documented.** For the chosen tenancy model, the runbook states what a single-tenant restore actually is (in shared schema: row extraction, not a file restore) and how long it takes.
8. **DB-208 — Restore is a scripted procedure.** The drill and the real thing run the same script: restore to scratch, apply WAL to the target timestamp, run the migrations check and a smoke query suite, record results.
9. **DB-209 — Unrestored means unproven.** A backup counts as existing only after at least one restore from that backup chain has succeeded. Before that, it is a hypothesis.
10. **DB-210 — Other recovery paths get their own drills.** Replica promotion and warehouse reload are separate recovery paths from backup restore; each is rehearsed on its own, not assumed covered by the backup drill.

## BAN list

- **BAN-DB-101 — No backups configured.** Banned: running a production database with no scheduled backup job of your own. Defeats: DET-INF-008. Bad: the database runs for months on provider defaults; the first incident discovers there is nothing to restore. Instead: scheduled base backups plus WAL archiving in place before launch (DB-201). Severity: BLOCK.
- **BAN-DB-102 — The untested backup.** Banned: treating a backup schedule as recovery capability without ever completing a restore. Defeats: DET-INF-009. Bad: nightly dumps accumulate for a year; during the first outage the newest archive turns out to be corrupt and unrestorable. Instead: a scripted quarterly restore drill with measured RTO/RPO recorded (DB-203, DB-208). Severity: BLOCK.
- **BAN-DB-103 — Backups in the primary failure domain.** Banned: keeping every backup copy on the same host, account, or region as the production database. Defeats: DET-INF-010. Bad: backups sit in the same cloud account; the account compromise (or provider failure) takes the data and its backups together. Instead: at least one copy outside the primary provider account and region (DB-202). Severity: BLOCK.
- **BAN-DB-104 — Backup secrets inside the backup script.** Banned: committing a backup script or config that carries the storage credentials it uses. Defeats: DET-INF-005. Bad: the nightly script in the repo contains the object-storage access key in plain text, readable by anyone with repo access. Instead: credentials in secret storage, referenced at runtime, stored apart from the backups (DB-205). Severity: BLOCK.

## Gates

- **G-DB-101 — Restore-drill record is current.** Verifies: DB-203, DB-209. Check: process — the runbook holds a drill record from within the current quarter: date, recovery point achieved, elapsed duration, smoke-suite result. Pass: a complete, current record exists. Fail: block any launch or major migration until a drill completes. Recorded in: progress.md.
- **G-DB-102 — Backup freshness check.** Verifies: DB-201, DB-204. Check: automated — monitoring asserts the newest successful backup is younger than the schedule allows and alerts otherwise. Pass: freshness within the window. Fail: block shipment of data-affecting changes. Recorded in: progress.md.
- **G-DB-103 — Off-domain copy check.** Verifies: DB-202. Check: automated — the backup inventory shows at least one completed copy in a different provider account or region within the retention window. Pass: copy present and current. Fail: warn, escalating to block at launch. Recorded in: progress.md.
- **G-DB-104 — Scripted restore run.** Verifies: DB-203, DB-208. Check: automated — the drill script restores the latest backup chain to a scratch instance, applies WAL to a target timestamp, runs the migrations check and smoke queries, and records its exit code and duration. Pass: exit code zero with all smoke queries green. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Snapshot theater.** Provider snapshots are switched on, never inspected, and their retention is unknown — the appearance of a backup strategy without its substance. Catch it: ask for the last restore record; snapshots without one are decoration.
- **The runbook in one head.** Exactly one person has ever performed a restore, and the steps exist only in their memory. Catch it: the drill is run by whoever is on call, from the script, or it does not count.
- **The easy-path drill.** A tiny staging database is restored in seconds and production readiness is declared. Catch it: drills run against a production-shaped backup, and the measured RTO is the one recorded.
- **Quiet retention shrink.** Retention is trimmed a little at a time to save storage cost until the history everyone assumed exists is gone. Catch it: retention changes are reviewed like schema changes, against DB-202's written tiers.

## Examples

- [Example 1 — No backups to a scheduled, tiered backup policy](examples/example-1.md) — corrects DB-201, DB-202.
- [Example 2 — Untested dump to a scripted quarterly restore drill](examples/example-2.md) — corrects DB-203.
- [Example 3 — Same-account backups to an off-domain copy with separate keys](examples/example-3.md) — corrects DB-202, DB-205.

## Recall anchors

- A backup never restored is a hypothesis, not a backup.
- Schedule it, monitor it, and let a miss page like an outage.
- One copy outside the primary account and region, always.
- Keys apart from backups; deletion behind its own privilege.
- Drill the restore quarterly and record the real RTO and RPO.

## Checklist

- [ ] Automated base backups plus WAL archiving are running (DB-201).
- [ ] Retention tiers are written and an off-domain copy is verified (DB-202, G-DB-103).
- [ ] The latest restore drill is recorded with measured RTO/RPO (G-DB-101).
- [ ] The scripted restore run passes end to end (G-DB-104).
- [ ] Backup freshness monitoring is live and alerting (G-DB-102).
- [ ] Backup credentials are stored apart from the backups, and deletion needs its own privilege (DB-205, DB-206).
