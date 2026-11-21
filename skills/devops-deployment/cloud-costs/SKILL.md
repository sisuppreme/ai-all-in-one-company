# cloud-costs

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://learn.microsoft.com/cloud-computing/finops/framework/finops-framework ; https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html
- **Depends on:** free-tiers, infrastructure-as-code, scaling
- **Feeds into:** reliability, hosting

## When to use / Do NOT use

- **Use when:** the project spends anything on cloud resources, or is about to; when a bill, budget, or cost estimate is produced; when autoscaling, instance sizing, or commitment discounts are decided; when "optimisation" work is proposed.
- **Do NOT use when:** the stack runs entirely on free tiers and nothing is billed — free-tiers governs that posture, and this skill takes over the moment the first paid line item appears. Do not use this skill to choose providers; hosting does that.

## Rules

1. **DO-321 — Allocate at least 90% of spend.** Billing data is allocated to a named service and team via tags or separate accounts, following the FinOps Inform phase, until at least 90% of monthly spend carries an owner. Unallocated spend above 10% is recorded as a finding in the monthly review, not absorbed as overhead.
2. **DO-322 — Budget before workloads.** Every cloud account or billing project has a budget with alerts at multiple thresholds (actual and forecasted spend) before its first workload is created. An account with resources and no budget fails G-DO-162.
3. **DO-323 — Anomaly detection from day one.** Provider anomaly detection (for example AWS Cost Anomaly Detection) is enabled on every billing account when the account is created, because a misconfigured autoscaler or a runaway job bills hourly, long before a monthly review would notice.
4. **DO-324 — Tags are enforced at creation.** Mandatory allocation tags (service, team, environment) are applied by IaC defaults or provider tag policies at resource creation. Backfilling tags before an audit is not enforcement; a resource created in the console without tags fails G-DO-163.
5. **DO-325 — Report unit costs next to revenue.** Each month, compute at least one unit cost — cost per request, per active user, or per paying customer — from the allocated billing data and record it next to the matching revenue or usage figure. A total bill with no unit cost cannot show whether growth is efficient or just bigger.
6. **DO-326 — Every autoscaling ceiling is a recorded cost decision.** No autoscaler runs without a maximum (replicas, instances, concurrency). The maximum, the monthly cost at that maximum, and who approved it are recorded where the scaling configuration lives (see scaling); an unbounded autoscaler fails review under BAN-DO-161.
7. **DO-327 — Sweep waste on a cadence.** At least monthly, list idle instances, oversized databases, orphaned disks/snapshots/storage, and resources with no owner tag; each item is deleted, resized, or ticketed with a named owner and a decision date. A waste item carried for two consecutive sweeps with no decision is escalated in the monthly review.
8. **DO-328 — Rightsize from observed utilization, at least quarterly.** Instance and database sizes are reviewed at least once a quarter against observed p95 CPU/memory utilization over the trailing 30 days. Sizes set at launch and never revisited are presumed wrong in one direction or the other.
9. **DO-329 — Commitments only against a measured baseline.** Reserved capacity, savings plans, or committed-use discounts are bought only for the steady-state baseline proven by at least 30 days of allocated usage data. Committing to unmeasured workloads converts a discount into a fixed liability.
10. **DO-330 — Optimisation never removes protection.** Cost work never disables or degrades backups, monitoring, alerting, or redundancy. Those are the product's safety properties, not overhead; a savings proposal that touches them is rejected under BAN-DO-163 and the saving is found elsewhere.
11. **DO-331 — The first paid line item needs its recorded trigger.** While a project is in the $0 free-tier posture, no paid resource is created until the trigger named in the free-tier sheet fires (first real user, first payment, cap forecast) and the spend is recorded. A paid resource whose first notice is the invoice fails this rule.
12. **DO-332 — File a monthly cost review.** Each month produces a short review artifact: allocation percentage, budget and anomaly alert status, unit cost, waste actions taken and open, and the date of the last rightsizing review. The review is the Operate phase made visible; no artifact means the month's spend was unreviewed.

## BAN list

- **BAN-DO-161 — Unbounded autoscaling.** Banned: an autoscaler, function concurrency setting, or replica range with no maximum. Defeats: DET-INF-027. Bad: an HPA with `maxReplicas` unset scales to 60 pods overnight on a traffic spike from a stuck retry loop, and the first notice is the monthly invoice. Instead: set a maximum sized from the load-test ceiling in scaling, record the monthly cost at that maximum and its approver per DO-326. Severity: BLOCK.
- **BAN-DO-162 — Untagged console-created resources.** Banned: creating billable resources by hand in the provider console, outside IaC and without allocation tags. Defeats: DET-INF-024. Bad: a developer launches a large instance from the console for a "quick test"; it runs a side project for a year, appears in no stack, and its cost belongs to nobody. Instead: create resources through IaC with mandatory tags applied by default per DO-324, and terminate the resource the day the test ends. Severity: BLOCK.
- **BAN-DO-163 — "Savings" by removing protection.** Banned: presenting disabled backups, monitoring, alerting, or redundancy as a cost optimisation. Defeats: DET-INF-008. Bad: a cost review "saves" money by turning off database backups and deleting the second replica; the saving is real until the first incident, which is now unrecoverable. Instead: find the saving in waste — idle, oversized, or orphaned resources per DO-327 — and leave protection intact per DO-330. Severity: BLOCK.
- **BAN-DO-164 — Budget alert routed to nobody.** Banned: a budget or anomaly alert whose notifications go to an unmonitored inbox, a departed team member, or no destination at all. Defeats: DET-INF-012. Bad: the 80% budget alert fires into a shared mailbox nobody reads; the overrun is discovered from the invoice three weeks later. Instead: route budget and anomaly alerts to a channel a named on-call or owner reads, and prove delivery with a test notification at setup per DO-322 and DO-323. Severity: WARN.

## Gates

- **G-DO-161 — Allocation coverage (automated).** Verifies: DO-321, DO-324. Check: from the provider billing export (for example `aws ce get-cost-and-usage` grouped by the service tag over the last full month), compute tagged spend ÷ total spend. Pass: allocation ≥90%. Fail: block the monthly review sign-off; untagged sources are named as findings. Recorded in: progress.md.
- **G-DO-162 — Budget and anomaly coverage (automated).** Verifies: DO-322, DO-323. Check: `aws budgets describe-budgets` (or the provider equivalent) lists at least one budget with actual and forecasted alert thresholds for every account, and `aws ce get-anomaly-monitors` returns an active monitor. Pass: every account has both. Fail: block creation of new workloads in any uncovered account. Recorded in: progress.md.
- **G-DO-163 — Tag coverage at creation.** Verifies: DO-324. Check: sample the resources created since the last review from the billing export or resource inventory; count those missing any mandatory tag (service, team, environment). Pass: zero untagged billable resources. Fail: tag or terminate each offender and record how it bypassed IaC defaults. Recorded in: progress.md.
- **G-DO-164 — Monthly review freshness.** Verifies: DO-325, DO-327, DO-328, DO-332. Check: open the cost review artifact for the current month and confirm it records the allocation percentage, a unit cost, waste actions with owners, and a rightsizing review dated within the last quarter. Pass: all four present and current. Fail: the month's spend is marked unreviewed and the review is completed before the next billing cycle closes. Recorded in: progress.md.

## Anti-patterns

- **Invoice-driven management.** Costs are only ever looked at when the invoice arrives, so every surprise is a month old before anyone can act. Catch it by asking for this month's forecasted spend — if the answer needs the invoice, DO-322 and DO-323 were skipped.
- **Dashboard theatre.** A cost dashboard exists and looks impressive, but no review artifact, no waste tickets, and no decisions ever come out of it. Catch it by asking what changed because of the dashboard last month; visibility without the Operate loop is decoration.
- **Optimising the visible line.** Shaving the biggest line item (usually compute) while a quieter one — data transfer, storage growth, per-seat tooling — compounds unchecked. Catch it by reviewing the top five line items' month-over-month deltas, not just the largest absolute number.
- **Launch-size forever.** Production still runs the instance sizes guessed on day one, months after real utilization data exists. Catch it by comparing each major resource's size against its trailing-30-day p95 utilization; a mismatch with no ticket means DO-328 lapsed.
- **Preview sprawl billed as production.** Forgotten preview and staging environments run around the clock at production sizes. Catch it in the waste sweep: non-production environments carry schedules or smaller sizes, and anything unowned is terminated per DO-327.

## Examples

- [Example 1 — Autoscaler with no ceiling](examples/example-1.md) — violates/corrects DO-326.
- [Example 2 — Console instance nobody owns](examples/example-2.md) — violates/corrects DO-324.
- [Example 3 — "Optimisation" that deletes the backups](examples/example-3.md) — violates/corrects DO-330.

## Recall anchors

- Unallocated spend is a finding, not a rounding error.
- Budget alert before workloads, never after the invoice.
- Every autoscaling ceiling is a cost decision with a name on it.
- Never save money by switching off backups or monitoring.
- $0 until the recorded trigger fires; commitments only on measured baselines.

## Checklist

- [ ] At least 90% of last month's spend is allocated to a named service and team. (DO-321)
- [ ] Every account has a budget with actual and forecasted alerts, created before its workloads. (DO-322)
- [ ] Anomaly detection is active on every billing account and its alerts reach a named reader. (DO-323, BAN-DO-164)
- [ ] No autoscaler runs without a recorded maximum and approved cost at that maximum. (DO-326)
- [ ] The monthly waste sweep ran; every idle, oversized, or orphaned resource is deleted, resized, or ticketed with an owner and date. (DO-327)
- [ ] Rightsizing was reviewed within the last quarter against observed p95 utilization. (DO-328)
- [ ] No savings proposal touches backups, monitoring, alerting, or redundancy. (DO-330)
- [ ] The monthly cost review artifact is filed with allocation %, unit cost, and open waste actions. (DO-332)
