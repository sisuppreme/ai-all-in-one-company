# activation-metrics

## Metadata

- **Owner department:** D18 Customer Experience (CX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Amplitude, "Driving product engagement by obsessing over activation" — https://amplitude.com/blog/getting-started-activation
- **Depends on:** event-tracking
- **Feeds into:** user-onboarding, trial-conversion, growth-experiments

## When to use / Do NOT use

- **Use when:** defining or changing the activation event, setting an activation target, building or auditing an activation dashboard or funnel report, diagnosing onboarding drop-off or funnel drop-off (where users abandon before first value, and why), or aiming onboarding at a measurable first-value moment.
- **Do NOT use when:** building the analytics pipeline, event instrumentation, or dashboard tooling itself — D12 (analytics-observability) owns the platform. This skill defines which activation events, windows, and thresholds D18 reads from that platform; it does not operate the platform.

## Rules

1. **CX-081 — Boundary: definitions here, platform in D12.** D12 owns event pipelines, storage, and dashboard tooling. This skill owns the activation definition — the event, the window, and the thresholds — that every D18 surface reads from the platform. A platform or dashboard change never silently changes the metric.
2. **CX-082 — One event.** Activation is exactly one defined event: the first action by which a user receives the product's core value. If a small set is unavoidable, the set carries one shared written definition and is reported as one metric, never as several competing ones.
3. **CX-083 — Signup is not activation.** Account creation, email verification, and profile completion are never the activation event. They are funnel steps before it.
4. **CX-084 — The written definition matches the instrumented event.** The event name in the written definition is identical to the event name in the tracking plan, and the event demonstrably fires in a test session. A definition naming an event that does not exist or does not fire is void.
5. **CX-085 — Every rate carries its window.** Each reported activation rate states its window (e.g., within the first session, within 7 days of signup). A rate published without a window is not a metric and is not reported.
6. **CX-086 — Validated against retention on own data.** The definition is validated by cohort analysis on this product's data: users who complete the event within the window retain better at a stated horizon (e.g., day 30) than users who do not. Before any validation run, the definition records the minimum retention delta and the horizon in advance; validation passes only when the measured delta meets that pre-recorded threshold. An unvalidated definition is labeled a hypothesis everywhere it appears.
7. **CX-087 — Thresholds come from the product's own baseline.** Activation targets and alert thresholds are computed from this product's measured baseline and recorded with that computation. No target is set from an external benchmark, article, or another product's published rate.
8. **CX-088 — Borrowed milestones are hypotheses only.** Another product's famous activation milestone may be tested as a candidate event under CX-086. It is never adopted as the definition or the target before it passes validation on this product's data.
9. **CX-089 — One definition everywhere.** Product, marketing, CX, and data surfaces report the same event, the same window, and the same cohort rule. No surface reports a local variant; a needed change goes through CX-091 and applies everywhere at once.
10. **CX-090 — The denominator is the signup cohort.** The activation rate is activated users divided by the signup cohort of the stated period. It is never computed over "active users," sessions, or any base that excludes the users who never activated.
11. **CX-091 — Revalidation triggers.** The definition is re-validated under CX-086 whenever the core value action, the packaging, or the target segment changes materially, and any change to the event or window is dated and annotated on every trend report so old and new definitions are never spliced into one line.
12. **CX-092 — Reported counts reconcile with raw events.** Every published activation count and rate must reconcile with an independent computation from raw events for the same cohort and period. A discrepancy blocks reporting until it is explained and fixed at the source.

## BAN list

- **BAN-CX-041 — Signup relabeled as activation.** Banned: counting account creation as the activation event in any dashboard, report, or claim. Defeats: DET-FAKE-004. Bad: the dashboard reports "activation rate: 100%" because every signup is counted as activated, so real value actions never move the figure. Instead: count only the defined core-value event within its window over the signup cohort (CX-082, CX-083, CX-090). Severity: BLOCK.
- **BAN-CX-042 — The borrowed milestone.** Banned: adopting another product's famous activation milestone, or its published activation rate, as this product's definition or target. Defeats: DET-FAKE-004. Bad: activation is defined as "invited three teammates" because a famous collaboration tool uses it, while this product's solo users receive core value without ever inviting anyone — the metric never moves when value is delivered. Instead: treat the milestone as a hypothesis and validate it against this product's retention data before adopting it (CX-086, CX-088). Severity: BLOCK.
- **BAN-CX-043 — Seed and test accounts in the cohort.** Banned: including seed, demo, staff, or test accounts in activation cohorts or counts. Defeats: DET-FAKE-014. Bad: the launch-week activation rate is computed over a cohort in which a third of the "users" are the team's seeded demo accounts, all of which performed the activation event during setup. Instead: exclude flagged non-customer accounts from the cohort at query time and state the exclusion in the report (CX-090, CX-092). Severity: BLOCK.
- **BAN-CX-044 — The scripted live counter.** Banned: a "live activations" or "users activated today" indicator driven by a timer, a random increment, or any source other than the real event stream. Defeats: DET-FAKE-018. Bad: the marketing page shows an activations-today counter that ticks up every few seconds overnight, when no signups are occurring. Instead: compute the indicator from the real event stream with its refresh period labeled, or remove it (CX-092). Severity: BLOCK.
- **BAN-CX-045 — Segment counts that cannot reconcile.** Banned: publishing activation breakdowns (by plan, channel, or segment) whose counts are produced from a fixed summary that does not match the underlying event query. Defeats: DET-FAKE-017. Bad: the by-channel activation counts sum to 1,240 while the headline rate for the same period is computed over 1,180 signups, and nobody can say which is right. Instead: derive every breakdown from the same raw-event query as the headline figure and assert the segments sum to it (CX-092). Severity: BLOCK.

## Gates

- **G-CX-041 — Funnel reconciliation.** Verifies: CX-089, CX-090, CX-092. Check: automated — a scheduled query independently computes the previous month's signup-cohort activation rate from raw events and diffs it against the dashboard figure for the same cohort and window. Pass: the figures match exactly, or differ only by a stated rounding rule recorded with the definition. Fail: block external reporting of the metric until reconciled. Recorded in: progress.md.
- **G-CX-042 — Definition-consistency check.** Verifies: CX-082, CX-084. Check: automated — a script asserts the event name in the written definition exists verbatim in the tracking plan and fires at least once in an instrumented test session. Pass: name matches and the event fires. Fail: block shipment of any surface reporting activation. Recorded in: progress.md.
- **G-CX-043 — Cohort validation run.** Verifies: CX-086, CX-088. Check: scheduled query plus manual review — first confirm the definition records a minimum retention delta and horizon set before the run; then compute the stated-horizon retention of the activated cohort vs. the non-activated cohort from raw events on this product's data. Pass: the measured retention delta meets or exceeds the pre-recorded minimum delta at the recorded horizon, and the result, threshold, horizon, and date are recorded with the definition. Fail: the definition is downgraded to "hypothesis" in every surface until a candidate event passes. Recorded in: progress.md.
- **G-CX-044 — Threshold provenance audit.** Verifies: CX-087. Check: manual — for every activation target or alert threshold in dashboards, docs, and decks, trace the number to a recorded baseline computation on this product's data. Pass: every number traces to an own-data baseline. Fail: any number traceable only to an external source is removed or replaced before the report ships. Recorded in: progress.md.
- **G-CX-045 — Revalidation and change control.** Verifies: CX-089, CX-091. Check: manual — on any change to the core value action, packaging, or target segment, confirm a revalidation run (G-CX-043) is scheduled; on any definition change, confirm the change date is annotated on every trend report. Pass: revalidation scheduled and annotations present. Fail: trend reporting freezes at the last consistently defined period. Recorded in: progress.md.

## Anti-patterns

- **Window shopping.** Quietly widening the window (7 days to 30 days) so the rate rises, without restating historical figures under the new window. Catch it: any window change appears in the definition's dated change log and history is recomputed or the trend line is broken visibly at the change.
- **Denominator shopping.** Reporting activation as a share of "active users" in the periods when the honest signup-cohort rate looks bad. Catch it: the denominator is named next to every rate; if it is not the signup cohort, the figure is not the activation rate.
- **Event stuffing.** Adding more events to the activation set until the rate looks healthy, instead of testing which single event predicts retention. Catch it: every candidate event must face the CX-086 retention comparison on its own before joining the set.
- **Validation theater.** Running the cohort comparison once at launch and treating the definition as permanently proven while the product changes around it. Catch it: the definition records its last validation date and the triggers in CX-091; a stale date means the metric is reported as unvalidated.

## Examples

- [Example 1 — Replacing "signed up" with a validated activation event](examples/example-1.md) — corrects CX-082, CX-083.
- [Example 2 — Reconciling a dashboard rate against raw events](examples/example-2.md) — corrects CX-092.
- [Example 3 — Replacing a copied benchmark target with an own-baseline target](examples/example-3.md) — corrects CX-087, CX-088.

## Recall anchors

- Activation is the first value received — never the signup.
- One event, one window, one definition, everywhere.
- A rate without a window is not a metric.
- Thresholds come from your own baseline, never a benchmark.
- If the dashboard and the raw events disagree, the dashboard is wrong until proven otherwise.

## Checklist

- [ ] The activation event is one named core-value action, defined in writing (CX-082).
- [ ] Signup and account-setup steps are excluded from the event (CX-083).
- [ ] The written event name matches the tracking plan and fires in a test session (G-CX-042).
- [ ] Every reported rate states its window and its signup-cohort denominator (CX-085, CX-090).
- [ ] The definition has a recorded, dated retention validation on this product's data (G-CX-043).
- [ ] Every target traces to an own-data baseline computation (G-CX-044).
- [ ] Dashboard figures reconcile with an independent raw-event computation (G-CX-041).
- [ ] Revalidation triggers and definition-change annotations are in place (G-CX-045).
