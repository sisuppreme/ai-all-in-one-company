# Example 2 — "Backups are on," said the handover

**Skill:** project-takeover
**Rules exercised:** DX-182 (inventory before opinion), DX-186 (every handover claim re-verified or stays `claimed`), DX-190 (risk-map disposition), DX-192 (production data and backups verified, never assumed)
**Violations in the Before:** BAN-DX-092 (handover claims accepted as verified)
**Gates referenced:** G-DX-091 (inventory completeness), G-DX-095 (freeze and exit — restore status honestly recorded)

**Scenario:** A small SaaS team takes over `invoiceyard`, a billing app, from its solo founder, who is leaving the company. The handover is a single 45-minute call and a two-page delivery note. The note states, in confident language:

- "Tests pass."
- "Deployed from `main`."
- "Backups run nightly to object storage."
- "The `legacy-reports` service is unused — safe to ignore."
- "The monthly export cron was disabled months ago."

The production Postgres database holds live customer invoices. There is no other copy of that data anywhere the inheriting team controls.

---

## Before

The inheriting lead writes the takeover summary directly from the delivery note, converting each statement into a fact:

> "State on takeover: test suite green, production deployed from `main`, nightly backups to object storage confirmed, `legacy-reports` unused, export cron disabled."

In the inventory, every one of those items is marked `verified` — although nobody on the new team has run the tests, checked which commit production is running, listed the backup bucket, or looked for the cron. The takeover closes in a week. The summary is filed and believed.

Three months later, a bad migration corrupts the invoices table and the team goes to restore from last night's backup. What they find:

- The backup bucket contains objects — but the most recent successful backup job run predates the handover. The job has been failing silently, and because "backups are on" was recorded as verified, nobody checked it during takeover.
- There is no restore procedure and a restore has never been performed, by anyone. The first attempted restore happens during an incident, under time pressure, against production data.
- Two of the other claims were also wrong — the test suite had pre-existing failures, and the "disabled" export cron was still enabled in one environment — but those are discovered later, one at a time, each as its own small surprise.

This is BAN-DX-092: inventory items marked `verified` on the predecessor's word. It defeats DX-186 (a claim is not a fact until the inheritor reproduces it) and DX-192 (a backup that has never been restore-tested is `claimed`, and the honest risk entry is "no verified recovery path"). G-DX-091 would also have failed: the inventory could not be diffed against independent sources — bucket listing, scheduler listing, deployed commit — because nobody looked at them.

## After

The same handover call and the same delivery note, handled under this skill. The note is treated as a list of claims to test, not as the takeover report.

**Inventory marks (DX-182, DX-186).** Each statement from the note enters the inventory as `claimed` on day one — that is its starting state, not a judgment on the founder's honesty:

| Claim from handover | How it was checked | Resulting mark |
|---|---|---|
| "Tests pass" | Full suite run by the inheritor during baselining (DX-187) | `verified` as *false as stated* — suite runs, with pre-existing failures recorded in the baseline with their output |
| "Deployed from `main`" | Deployed commit queried from the hosting provider and compared with `main` HEAD | `verified` — production is two commits behind `main`; the two commits are inventoried, not deployed during takeover |
| "Backups run nightly" | Backup job history and bucket listing inspected directly | Stays `claimed` — job is scheduled nightly, but recent runs show failures; no successful recent backup can be confirmed |
| "`legacy-reports` is unused" | No independent evidence of non-use yet (no traffic logs reviewed, service still deployed) | Stays `claimed`, and the service is *not* deleted or disabled — see BAN-DX-095 |
| "Export cron was disabled" | Scheduler listing for every environment checked | `verified` as *false in one environment* — still enabled in staging; recorded as a finding |

**The restore test (DX-192).**
Because the invoices database is the most critical store, the inheritor performs a restore during takeover: the most recent available backup is restored into a non-production environment, the app is pointed at the restored copy, and the invoice totals are spot-checked against production counts. Two outcomes are possible, and both are recorded honestly:

- If the restore succeeds: backups move to `verified`, with the restore date and environment recorded in the inventory. The claim is now a fact the inheritor personally reproduced.
- If it fails or no usable backup exists (the outcome the failed job history points to here): the inventory keeps backups as `claimed`, and the top of the risk map — not a footnote — carries the entry **"no verified recovery path"** for the production invoices store, with a named owner.

In this case the restore attempt exposes that the newest restorable backup is stale, so "no verified recovery path" stands at the top of the report at exit, exactly as G-DX-095 requires: the restore status is recorded as it is, not as hoped.

**Risk-map dispositions (DX-190).**

| Finding | Disposition |
|---|---|
| Backup job failing; no verified recovery path for production invoices DB | `stabilize-now` — enabling/verifying a backup for production data is DX-191 stabilization; fixing the job and completing a successful restore test close this row |
| Export cron still enabled in staging despite handover claim | `stabilize-now` if it can send or export real data; otherwise `register` with the staging-only scope recorded — disposition chosen from evidence, not from the note |
| Test suite has pre-existing failures (per DX-187 baseline) | `register` — tech-debt register ID recorded in the row |
| Production two commits behind `main` | `schedule` — deploy decision is post-takeover work, with the two commits named in the row |
| "`legacy-reports` unused" unverified | `accept` is *not* available on the founder's word alone; row stays open as `schedule` — gather non-use evidence while the system runs observed, post-takeover |

**Report language (DX-186).**
The takeover report never restates a `claimed` item as fact. It writes "backups: scheduled nightly per the delivery note; recent job runs failing; restore test performed on [date] with [result]" — not "backups confirmed." Where the founder was right, the report says so with the check that proved it; where the note was wrong, the baseline and the job history, not an argument, carry the correction.

**Difference:** in the Before, the first restore attempt happens during an incident, three months after the team certified recovery they never tested. In the After, the restore attempt happens in week one, in a non-production environment, and the takeover either exits with a verified recovery path or exits honestly declaring — at the top of the report, with an owner — that there isn't one yet.
