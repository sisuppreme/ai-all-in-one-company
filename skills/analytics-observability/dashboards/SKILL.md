# dashboards

## Metadata

- **Owner department:** D12 Analytics & Observability (AN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** PROJECT_ANATOMY.md, "Monitoring" ; Google, *Site Reliability Engineering*, "Monitoring Distributed Systems" — https://sre.google/sre-book/monitoring-distributed-systems/
- **Depends on:** monitoring (owns the signals), product-analytics (owns the product metrics rendered)
- **Feeds into:** alerting, incident-response (D6), performance-optimization

## When to use / Do NOT use

- **Use when:** building, changing, or reviewing any dashboard — product overview, per-service golden-signal view, or incident view — and when deciding whether a panel earns its place on one.
- **Do NOT use when:** the question is which signals exist or how they are collected (monitoring owns the signals; this skill owns their presentation), what a product metric means (product-metrics, D1, owns definitions; product-analytics owns measurement), or infrastructure saturation telemetry itself (D6 owns hosts and clusters; this skill consumes that telemetry, never redefines it).

## Rules

1. **AN-141 — Dashboards are code.** Every dashboard is defined in the repo (provisioning JSON or the platform equivalent), reviewed in the same change process as code, and deployed from the repo to every environment. A dashboard that exists only in a web console does not exist for this skill's purposes.
2. **AN-142 — Every panel answers a named question.** Each panel states the question it answers and the decision or action its reading triggers. A panel nobody can state the question for is removed in the same change that notices it.
3. **AN-143 — Query and definition are visible.** Every panel exposes the query or expression that produces it and names the metric definition it renders (from the metrics document or the service's SLI definitions). A number whose computation cannot be inspected from the dashboard is not trusted and not shipped.
4. **AN-144 — Computed from live records only.** Every figure is computed from the live event stream, metrics store, or underlying records at read time (or at the panel's stated aggregation cadence under AN-145). No panel renders a constant, a fixture, a typed-in value, or a value copied from an earlier reading.
5. **AN-145 — Refresh cadence is stated and honest.** Each panel or dashboard states how fresh its data is: the aggregation interval and the expected lag. The word "live" or "real-time" appears only on panels whose data is actually current within the stated lag; a periodically aggregated panel is labeled with its period.
6. **AN-146 — One golden-signal template, every service.** Per-service dashboards are generated from a single template covering latency, traffic, errors, and saturation. A new service gets its dashboard by instantiation, not by hand-drawing; a service with no generated instance is a coverage defect.
7. **AN-147 — Percentiles, never averages.** Latency panels show percentile bands (p50/p95/p99 at minimum) with successful and failed requests charted separately. Error panels show both rate and count. No panel presents a mean latency as its headline figure.
8. **AN-148 — Units, thresholds, and windows on every panel.** Each panel shows its units, an SLO or threshold line where one exists, and a default time window appropriate to its question (an incident panel defaults to hours, a capacity panel to weeks). A panel the reader must mentally rescale or re-window before it means anything is unfinished.
9. **AN-149 — Annotations are on by default.** Deploy markers and incident markers are overlaid on every service dashboard. A graph that forces the reader to reconstruct "what changed" from memory or another tool fails this rule.
10. **AN-150 — Three layers, kept separate.** Dashboards live in exactly one layer: the product overview (D1's metrics, from product-analytics), the per-service golden-signal view (AN-146), or the incident view (the service dashboard annotated per AN-149, arranged for diagnosis). Product figures are not mixed into service panels, and service internals do not crowd the overview.
11. **AN-151 — A stale or empty panel is a surfaced defect.** When a panel's query returns no data for its stated window, the dashboard shows that state explicitly and the gap is logged as a defect against the data source. A silently blank panel that a reader can mistake for "zero" or "healthy" is a failure of this skill, not of the reader.
12. **AN-152 — Pruning is part of maintenance.** On the dashboard review cadence recorded in progress.md, every panel is re-asked the AN-142 question. Panels with no named question, no reader, or no decision are deleted; the deletion is recorded with the reason.

## BAN list

- **BAN-AN-071 — Frozen figures.** Banned: a panel whose value comes from a constant, fixture, seeded sample data, or a hand-typed number instead of a query over live records. Defeats: DET-FAKE-004. Bad: the overview's "Revenue today" panel is a text card reading "$4,820", typed at launch; it reads $4,820 every day for a quarter. Instead: the panel runs the revenue query against live records, with its definition visible per AN-143. Severity: BLOCK.
- **BAN-AN-072 — Console-only dashboards.** Banned: a dashboard created or edited only in the web console, with no corresponding definition in the repo — or a production dashboard hand-edited until it drifts from the repo version. Defeats: DET-INF-024. Bad: during an incident someone fixes the error panel in the console; three months later a redeploy from the repo silently restores the broken panel. Instead: every change lands in the repo definition first and deploys from it (AN-141). Severity: BLOCK.
- **BAN-AN-073 — Fake "live" panels.** Banned: labeling a panel "live" or "real-time" when its data is a periodic aggregate, a cached snapshot, or a client-side timer animating values no query produced. Defeats: DET-FAKE-018. Bad: the "live visitors" widget increments on a random timer while the analytics pipeline batches hourly; support quotes its number to a customer as current. Instead: label the panel with its true aggregation period and lag per AN-145, or wire it to the actual stream before using the word "live". Severity: BLOCK.
- **BAN-AN-074 — Averages as the latency story.** Banned: a latency panel or alert whose headline figure is a mean, with no percentile view, so the tail users actually feel is invisible. Defeats: DET-INF-011. Bad: the service dashboard shows "avg latency 120 ms" and stays green while p99 sits at 4 s and the slowest decile of checkouts times out. Instead: chart p50/p95/p99 bands with success and error latency separate (AN-147). Severity: BLOCK.
- **BAN-AN-075 — The tutorial dashboard.** Banned: shipping the platform's sample or tutorial dashboard — host CPU, memory, a homepage ping — as the service's monitoring view while the user-facing endpoints and their error rates are unmeasured. Defeats: DET-INF-011. Bad: the "production dashboard" charts VM CPU for a service whose checkout endpoint returns unmeasured 500s for two days. Instead: instantiate the golden-signal template (AN-146) so the service's latency, traffic, errors, and saturation are the default view. Severity: WARN.

## Gates

- **G-AN-071 — Data-change movement test.** Verifies: AN-144. Check: automated — in a test environment, create one record a chosen panel counts (one completed order, one signup), wait exactly one stated refresh cycle (AN-145), and re-read the panel; then delete the record and re-read after another cycle. Pass: the figure moves by exactly +1, then exactly −1. Fail: block the dashboard's release; the panel is treated as a frozen-figure defect under BAN-AN-071. Recorded in: progress.md.
- **G-AN-072 — Provisioning and drift check.** Verifies: AN-141. Check: automated — deploy all dashboard definitions from the repo to a scratch instance and load each one; then export the production dashboards and diff them against the repo versions. Pass: every dashboard renders with zero datasource errors, and the production diff is empty. Fail: block shipment; reconcile the drift into the repo before release. Recorded in: progress.md.
- **G-AN-073 — Template coverage check.** Verifies: AN-146. Check: automated — list every service in the service registry and assert each has a dashboard instance generated from the golden-signal template with all four signal groups present. Pass: coverage is 100%. Fail: generate the missing instances before the service's next release. Recorded in: progress.md.
- **G-AN-074 — Panel completeness lint.** Verifies: AN-142, AN-143, AN-145, AN-148. Check: automated — lint the dashboard definitions in the repo: every panel carries a question/decision note, a query, a named metric definition, units, a stated refresh cadence, and (where an SLO exists) a threshold line. Pass: zero panels missing any required field. Fail: block the dashboard change until the fields are present. Recorded in: progress.md.
- **G-AN-075 — Freshness check.** Verifies: AN-151. Check: automated — query every panel on the product overview and each service dashboard for its stated window (last 24 hours for the overview) and assert each returns data or an explicit no-data state that is logged as a defect. Pass: no panel is silently blank. Fail: open a defect against the data source before the dashboard is cited in any report. Recorded in: progress.md.

## Anti-patterns

- **The wallboard museum.** Forty panels accumulate because adding is free and deleting feels risky; nobody reads past the first row and the three panels that matter drown. Catch it: at review, ask each panel when it last changed a decision — silence is a deletion vote (AN-152).
- **Screenshot status reports.** A static export of a dashboard is pasted into a report and quoted for weeks after the data moved on. Catch it: link the live dashboard and state the reading time; a figure with no "as of" is a screenshot, not a status.
- **Green-by-construction thresholds.** Threshold lines set so wide the panel can never turn red, because a red panel once caused an uncomfortable meeting. Catch it: compare each threshold against the SLO it claims to represent; a threshold looser than the SLO is decoration (AN-148).
- **One window for everything.** Every panel defaults to the same 30-day window, so today's outage is averaged into invisibility on the incident view. Catch it: check the default window against the panel's layer — incident panels default to hours (AN-148, AN-150).

## Examples

- [Example 1 — The revenue panel that read the same number for a quarter](examples/example-1.md) — violates/corrects AN-144.
- [Example 2 — The incident fix that lived only in the console](examples/example-2.md) — violates/corrects AN-141.
- [Example 3 — "Average latency 120 ms" while the tail timed out](examples/example-3.md) — violates/corrects AN-147.

## Recall anchors

- If it isn't in the repo, it isn't a dashboard.
- Every panel: a named question, a visible query, a stated cadence.
- A figure that cannot move when the data moves is not a metric.
- Percentiles or it didn't happen — averages hide the tail.
- A panel nobody can name the decision for gets deleted.

## Checklist

- [ ] Every dashboard is defined in the repo and deploys from it with zero drift (G-AN-072).
- [ ] The data-change test moved a panel figure by exactly the known amount (G-AN-071).
- [ ] Every service in the registry has a golden-signal instance from the one template (G-AN-073).
- [ ] Every panel names its question, decision, query, definition, units, and refresh cadence (G-AN-074).
- [ ] Latency panels show percentile bands; no mean is a headline figure (AN-147).
- [ ] Deploy and incident annotations are on for every service dashboard (AN-149).
- [ ] No panel is silently blank; every no-data state is logged as a defect (G-AN-075).
- [ ] Panels with no named question or decision were deleted at this review, with reasons recorded (AN-152).
