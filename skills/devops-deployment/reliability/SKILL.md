# reliability

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://sre.google/workbook/alerting-on-slos/ ; https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html ; https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html
- **Depends on:** backup-recovery, monitoring, rollback
- **Feeds into:** incident-response, scaling, cloud-costs

## When to use / Do NOT use

- **Use when:** Setting or auditing a production service's reliability system — SLOs and error budgets, golden-signal monitoring, burn-rate alerting, backup and restore assurance, and the disaster-recovery plan.
- **Do NOT use when:** Executing backups or restore jobs themselves — that is backup-recovery (this skill verifies placement, cadence, and evidence). Running an incident in progress — that is incident-response. Choosing replica counts and autoscaling ceilings — that is scaling.

## Rules

1. **DO-261 — Every production service has a written SLO.** The SLO names the SLI (the exact measured ratio, e.g., successful requests / total requests), the target percentage, and the rolling window; it lives in the project's reliability register, not in a slide deck. A service with no SLO has no reliability standard.
2. **DO-262 — The error budget gates release pace.** Remaining budget is computed from the SLI and displayed where the team plans work; when the budget for the window is exhausted, feature releases pause and reliability work takes priority until the budget recovers. The pause is a rule, not a negotiation held during an outage.
3. **DO-263 — Golden signals are monitored for every production service.** Latency, traffic, errors, and saturation each have a dashboard or recorded query per service; a signal with no query behind it counts as unmonitored.
4. **DO-264 — Paging alerts fire on error-budget burn rate.** Alerts use multi-window burn-rate thresholds against the SLO (per the SRE Workbook method), not raw cause metrics; alert rule files pass `promtool check rules` (or the platform equivalent) in CI.
5. **DO-265 — Every paging alert is symptom-based, actionable, and carries a runbook link.** If the on-call cannot act on it, it is deleted or demoted to a ticket; the alert annotation links the runbook section that handles it.
6. **DO-266 — Every alert routes to a named responder path.** Each paging alert terminates at a named on-call rotation — for a single operator, the operator plus a stated escalation contact — and the routing is test-fired after any change. An alert that lands in a channel nobody watches is no alert.
7. **DO-267 — An independent external probe watches the public URL.** The probe runs outside the hosting provider's failure domain, checks the public URL on a stated interval, and pages through the same path as internal alerts, so detection survives the host dying.
8. **DO-268 — Backups live outside the primary failure domain.** Backup storage sits in a different account, region, or provider than the primary data; this skill verifies the placement on the quarterly review (execution is owned by backup-recovery).
9. **DO-269 — Restores are rehearsed on a written cadence, with timings recorded.** Each drill records the date, the backup restored, the measured duration, and the operator; a backup with no drill record inside its cadence window counts as untested.
10. **DO-270 — Every service names RTO and RPO targets and a DR strategy tier.** The chosen tier — backup-and-restore, pilot light, warm standby, or multi-site active — is written next to the targets it can actually meet; the tier is chosen deliberately, not inherited from a tutorial default.
11. **DO-271 — Disaster recovery is a game day, not a document.** Failover is executed on the recorded cadence and the measured RTO/RPO are filed against the DO-270 targets; a plan that has never been run is a hypothesis and is labeled as one.
12. **DO-272 — Reliability is reviewed quarterly against evidence.** The review checks: SLO inventory current, budget status per service, last restore drill date and duration, last DR game day date and measured RTO/RPO, and a sample of alerts for runbook linkage. Findings go into progress.md with owners.
13. **DO-273 — The project's reliability posture is declared, with a promotion trigger.** Project docs state the posture (validation on free tiers, with the specific rules waived named; or production, all rules apply) and the event that forces promotion — first real user, first payment, or first promised availability commitment, whichever comes first.

## BAN list

- **BAN-DO-131 — Backup declared done with no restore test.** Banned: marking backup work complete, or reporting a service as protected, when no restore drill record exists inside the cadence window. Defeats: DET-INF-009. Bad: the launch checklist says "Backups: enabled ✓" and nobody has ever restored one. Instead: run a restore drill, record date and measured duration, and only then report the service as protected. Severity: BLOCK.
- **BAN-DO-132 — Backups inside the primary failure domain.** Banned: the only copy of the backups lives in the same account, region, or provider failure domain as the primary data. Defeats: DET-INF-010. Bad: nightly database dumps are stored on a bucket in the same cloud account whose compromise or outage would take the primary down too. Instead: replicate backups to a separate account, region, or provider and verify the placement at the quarterly review. Severity: BLOCK.
- **BAN-DO-133 — Alerts that reach nobody.** Banned: paging rules whose notifications terminate in an unmonitored inbox, a muted channel, or a rotation with no named responder. Defeats: DET-INF-012. Bad: burn-rate alerts post to a chat channel the team muted during a noisy week and never unmuted. Instead: route alerts to the named on-call path and test-fire after every routing change. Severity: BLOCK.
- **BAN-DO-134 — In-host monitoring as the only detection.** Banned: relying solely on monitoring that runs on the same host or provider as the service, with no independent external probe. Defeats: DET-INF-028. Bad: when the VPS dies, its own monitoring dies with it and the outage is discovered from user complaints hours later. Instead: run an external probe on the public URL from outside the provider, paging through the same path as internal alerts. Severity: BLOCK.
- **BAN-DO-135 — Golden-signal blind spot.** Banned: shipping a production service with no recorded query or dashboard for one or more of latency, traffic, errors, or saturation. Defeats: DET-INF-011. Bad: the team can see CPU on the host but has no error-rate or latency view, so a slow-burn failure is invisible until the budget is gone. Instead: record a query or dashboard per golden signal per service before launch, and re-check the inventory at the quarterly review. Severity: WARN.

## Gates

- **G-DO-131 — SLO inventory audit (automated).** Verifies: DO-261, DO-273. Check: for each service in the deploy manifest, grep the reliability register for its SLO entry — `for s in $(cat deploy/services.txt); do grep -q "^## $s" docs/reliability.md || echo "MISSING $s"; done`. Pass: no MISSING lines; every production service has an SLI, target, and window on record. Fail: block shipment until the register covers every service. Recorded in: progress.md.
- **G-DO-132 — Alert rule lint (automated).** Verifies: DO-264. Check: run `promtool check rules alerts/*.yml` (or the platform's rule validator) as a CI step. Pass: exit code 0. Fail: block merge until the burn-rate rules validate. Recorded in: progress.md.
- **G-DO-133 — Runbook link check (automated).** Verifies: DO-265. Check: script extracts every runbook URL from the alert rule annotations and requests each (`curl -sfI <url>`); report any non-2xx/3xx response. Pass: 100% of paging alerts link a reachable runbook. Fail: block shipment; fix the link or demote the alert. Recorded in: progress.md.
- **G-DO-134 — Restore drill currency (manual).** Verifies: DO-269, DO-270. Check: open the drill log and confirm the latest entry for each production data store is dated inside its cadence window and its measured duration is at or under the service's RTO target. Pass: every store has a current, in-target drill. Fail: block any "protected" claim for that service and schedule the drill before the next release. Recorded in: progress.md.
- **G-DO-135 — External probe page test (manual).** Verifies: DO-266, DO-267. Check: in staging (or a maintenance window), make the public URL fail and confirm the external probe pages the named responder path; record the time from failure to page. Pass: page arrives through the production routing within the probe interval plus one minute. Fail: block shipment — detection that dies with the host is not detection. Recorded in: progress.md.

## Anti-patterns

- **Alert wallpaper.** Dozens of cause-based alerts (CPU, disk, connection counts) fire on every deploy until the channel is ignored in practice; catch it by listing alerts that fired in the last 30 days with no action taken — each one is a deletion or demotion candidate.
- **SLO theater.** A target like 99.99% copied from a blog post with no SLI query behind it; catch it by asking for the query that computes the SLI — if none exists, the SLO is decoration and the budget math is fiction.
- **Budget amnesia.** The error budget is exhausted, but feature releases continue at full pace because nobody looked at the number during planning; catch it by putting remaining budget at the top of the planning agenda, not in a dashboard nobody opens.
- **Drill deferral.** The restore drill and the DR game day are always scheduled for "next quarter," so the plan ages untested while the system drifts; catch it by checking drill dates at the quarterly review — a date that keeps moving is a finding, not a schedule.

## Examples

- [Example 1 — An SLO that can gate a release](examples/example-1.md) — violates/corrects DO-261, DO-262.
- [Example 2 — A burn-rate alert with a runbook](examples/example-2.md) — violates/corrects DO-264, DO-265.
- [Example 3 — A restore drill on record](examples/example-3.md) — violates/corrects DO-268, DO-269, DO-270.

## Recall anchors

- No SLO, no standard: an unmeasured service is an unkept promise.
- The error budget is the release valve — when it is spent, features wait.
- Alerts page symptoms and link runbooks; causes get tickets.
- Detection must survive the host: probe from outside.
- An unrestored backup is a hope, not a backup.

## Checklist

- [ ] Every production service has an SLO entry with SLI, target, and window (DO-261).
- [ ] Remaining error budget is computed and visible where work is planned (DO-262).
- [ ] All four golden signals have a dashboard or recorded query per service (DO-263).
- [ ] Paging alerts are burn-rate based and the rule files pass lint in CI (DO-264).
- [ ] Every paging alert is actionable and links a reachable runbook (DO-265, G-DO-133).
- [ ] Alerts route to a named responder path and were test-fired after the last change (DO-266).
- [ ] An external probe watches the public URL and pages through the production path (DO-267, G-DO-135).
- [ ] Latest restore drill per data store is in-cadence and within RTO; RTO/RPO and DR tier are on record (DO-269, DO-270).
