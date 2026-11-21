# rollback

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Kubernetes Docs, "Deployment" (rolling back a Deployment) — https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
- **Depends on:** deployment-strategies, ci-cd
- **Feeds into:** incident-response, reliability

## When to use / Do NOT use

- **Use when:** preparing a release so it can be reversed, responding to a bad deploy, or checking that the return path to the last good version actually exists and has been rehearsed.
- **Do NOT use when:** choosing the promotion pattern itself (deployment-strategies owns that; this skill owns reversing it), or when the failure is data loss rather than a bad release (D5 backup-recovery owns restore).

## Rules

1. **DO-301 — The rollback action is written before the release ships.** The runbook names the exact command or console step that restores the previous version (for example `kubectl rollout undo deployment/<name>`), before merge. A rollback step first named during the incident does not count.
2. **DO-302 — The previous version stays deployable.** Artifacts are immutable and versioned; the prior artifact (image digest, platform build, or blue/green idle environment) is retained and redeployable until the new version clears its observation window.
3. **DO-303 — Rollback is the default first response to a bad deploy.** When a release breaches its abort thresholds, roll back first and diagnose second. Fix-forward is the exception and needs a written justification in the incident record.
4. **DO-304 — Flagged releases roll back by flag flip first.** If the change shipped behind a feature flag, the first rollback action is flipping the flag off — seconds, no redeploy. Artifact rollback follows only if the flag flip does not clear the fault.
5. **DO-305 — Data changes expand and contract.** A migration never drops or renames a column/table in the same release that stops using the old shape; the contract step ships at least one release later, so the old code runs against the new schema throughout the rollback window.
6. **DO-306 — Every migration has a down path or a documented exception.** Each migration ships with a reversal, or with a written forward-fix plan recorded as an explicit exception in the release checklist. "Irreversible, undocumented" blocks the release.
7. **DO-307 — The live version is always knowable.** Deploy records map production → artifact digest → commit SHA, so the rollback target (the previous record) is identified from the record, not from memory.
8. **DO-308 — Rollback is drilled and timed.** On a set cadence, staging runs the drill: deploy a deliberately broken version, execute the documented rollback, and record the time for the previous version to serve healthy traffic against a stated target (for example 5 minutes).
9. **DO-309 — Rollback triggers are named in advance.** The release record names the metric thresholds and the person/role authorized to call a rollback, matching the abort conditions set by deployment-strategies. No threshold, no release.
10. **DO-310 — Recovery is verified, not assumed.** After rollback, the restored version passes its health check and a key-route smoke test before the incident is declared mitigated; the result is recorded with the rollback timestamp.
11. **DO-311 — Rollback preserves the evidence.** Logs, deploy records, and the bad artifact are kept after rollback; the faulty release is never deleted before the postmortem has what it needs.
12. **DO-312 — A rolled-back release does not re-ship unchanged.** The same artifact is not promoted again until the fault is fixed and the fix is visible as a new version with its own deploy record.

## BAN list

- **BAN-DO-151 — In-place overwrite deploy.** Banned: the deploy copies new files over the live release, leaving no previous artifact to return to. Defeats: DET-INF-017. Bad: deploy script runs `rsync -a build/ /var/www/app/` and the rollback plan reads "redeploy from main and hope." Instead: deploy each release as a new immutable, versioned artifact and switch traffic to it, keeping the previous artifact live-capable. Severity: BLOCK.
- **BAN-DO-152 — Destructive migration in the retiring release.** Banned: dropping or renaming a schema element in the same release that stops reading/writing the old shape. Defeats: DET-INF-018. Bad: release 1.4 removes all reads of `users.name_old` and its migration runs `DROP COLUMN name_old`, so rolling back to 1.3 breaks against the new schema. Instead: expand in 1.4 (add the new shape, dual-write), contract in 1.5 or later once 1.3 is no longer a rollback target. Severity: BLOCK.
- **BAN-DO-153 — Migration with no down path and no exception.** Banned: a migration file with no reversal and no documented forward-fix plan. Defeats: DET-INF-018. Bad: `migrations/0042_add_billing.sql` exists only as an `up` script applied by hand in a SQL console, with nothing recorded about what ran on production. Instead: ship the migration through the pipeline with a down script, or record the forward-fix exception in the release checklist before merge. Severity: BLOCK.
- **BAN-DO-154 — Tearing down the return path at deploy time.** Banned: deleting the previous artifact, draining the idle blue/green environment, or pruning rollout history as part of the same action that ships the new version. Defeats: DET-INF-017. Bad: the deploy job ends with `docker image prune -a`, removing the last good image minutes after the new one starts. Instead: retain the previous version until the observation window closes and the release is declared good. Severity: BLOCK.

## Gates

- **G-DO-151 — Staging rollback drill.** Verifies: DO-301, DO-302, DO-308. Check: in staging, deploy a deliberately broken version, then execute the exact rollback command written in the runbook (for example `kubectl rollout undo deployment/<name>`) and time it; confirm both revisions appear in rollout/deploy history. Pass: previous version serves healthy traffic within the stated target time. Fail: block shipment of the release process until the drill passes. Before a staging environment is provisioned, this gate's disposition is a recorded provisioning waiver per the §6.3 protocol; it unblocks when a staging environment is provisioned and the drill can run against a deployed release. Recorded in: progress.md.
- **G-DO-152 — Deploy-record and retention audit.** Verifies: DO-302, DO-307. Check: script reads the last deploy record, resolves production → artifact digest → commit SHA, and confirms the previous artifact still exists in the registry/platform (`docker manifest inspect <image>@<previous-digest>` or platform build list). Pass: record resolves and previous artifact is present. Fail: block the next release. Recorded in: progress.md.
- **G-DO-153 — Migration down-path check.** Verifies: DO-305, DO-306. Check: CI step lists migration files added by the change and fails unless each has a matching down/reversal file or an exception entry in the release checklist. Pass: every new migration has a down path or a recorded exception. Fail: block merge. Recorded in: progress.md.
- **G-DO-154 — Runbook rollback-step check.** Verifies: DO-301, DO-309. Check: grep the runbook/release checklist for the release's rollback command and named abort thresholds before the production deploy job runs. Pass: exact command and thresholds present. Fail: block the deploy. Recorded in: progress.md.

## Anti-patterns

- **Rollback theater.** A rollback paragraph exists in the wiki but has never been executed; the first real attempt happens during an outage and discovers the old artifact is gone. Catch it: no drill record in the last cadence window means the path is unproven, whatever the document says.
- **Half rollback.** Code returns to the previous version while config, flags, or schema stay in the new state, leaving a combination no version was tested in. Catch it: the rollback record must list every layer touched (artifact, flag, config, schema) and its end state.
- **Silent rollback.** The operator rolls back and tells nobody; monitoring "recovers," users see inconsistent behavior, and the postmortem never happens. Catch it: a rollback with no incident/status entry in the deploy record is a process failure even when it works.
- **Rollback amnesia.** Nobody records why the release was rolled back, so the same fault is rediscovered from scratch next release. Catch it: the deploy record for the bad version must carry the fault summary before it is closed.

## Examples

- [Example 1 — Runbook rollback step written before release](examples/example-1.md) — violates/corrects DO-301.
- [Example 2 — Expand-and-contract instead of a destructive migration](examples/example-2.md) — violates/corrects DO-305.
- [Example 3 — Flag flip as the first rollback action](examples/example-3.md) — violates/corrects DO-304.

## Recall anchors

- Rollback is a repoint to a kept artifact, never a forward fix under pressure.
- If the rollback step is not written before the release, it does not exist.
- Flag flip first; artifact rollback second.
- Expand now, contract next release — the old code must run on the new schema.
- A rollback that was never drilled is a hope, not a plan.

## Checklist

- [ ] Runbook names the exact rollback command for this release (DO-301).
- [ ] Previous artifact retained and confirmed present in the registry/platform (DO-302).
- [ ] Abort thresholds and the authorized rollback caller are in the release record (DO-309).
- [ ] Flagged changes list the flag flip as the first rollback action (DO-304).
- [ ] Every new migration has a down path or a recorded exception (DO-306).
- [ ] No schema element is dropped or renamed in the release that retires its use (DO-305).
- [ ] Last staging rollback drill passed within its target time (DO-308).
- [ ] Deploy record maps production → artifact digest → commit SHA (DO-307).
