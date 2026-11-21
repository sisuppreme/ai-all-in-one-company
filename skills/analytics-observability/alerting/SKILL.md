# alerting

## Metadata

- **Owner department:** D12 Analytics & Observability (AN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Google, *The Site Reliability Workbook*, "Alerting on SLOs" — https://sre.google/workbook/alerting-on-slos/ ; Google, *Site Reliability Engineering*, "Monitoring Distributed Systems" — https://sre.google/sre-book/monitoring-distributed-systems/ ; PROJECT_ANATOMY.md, "Alerting"
- **Depends on:** monitoring (owns the signals and SLOs this policy alerts on)
- **Feeds into:** incident-response (D6 — consumes the pages this policy fires)

## When to use / Do NOT use

- **Use when:** defining or changing alert policy for a project: which conditions page, at what threshold, at what severity tier, with what payload, and how alert quality is reviewed over time.
- **Do NOT use when:** the question is on-call mechanics — rotations, escalation execution, incident command, postmortems (incident-response, D6, owns those; this skill's policy is what D6's mechanics execute), infrastructure saturation plumbing (D6 consumes this policy for its hosts; D12 sets the policy), or which signals exist at all (monitoring owns signal coverage; this skill alerts on the signals monitoring provides).

## Rules

1. **AN-121 — Boundary: D12 owns policy, D6 owns mechanics.** This skill decides what pages, at what threshold, and with what signal quality. D6 owns the on-call rotation, the escalation execution, and the incident response the page triggers. Neither side silently redefines the other's half: a threshold change is a policy change here; a rotation change is a mechanics change there.
2. **AN-122 — Page on symptoms, never on causes alone.** Pages fire on what users experience: error-budget burn against a user-facing SLO, or a failed synthetic check on a critical flow. CPU, disk, memory, or a single host are causes — they are ticket or dashboard material unless they are themselves the user-visible symptom.
3. **AN-123 — Thresholds are derived from the error budget.** Paging alerts use the Workbook's multi-window, multi-burn-rate form. For a 99.9% SLO over a 30-day window: page at burn rate 14.4 over 1h/5m windows (2% of budget consumed), page at 6 over 6h/30m (5%), ticket at 1 over 3d/6h (10%); in each paging pair the short window is 1/12 of the long window and proves the burn is still happening. For any other SLO target or window, recompute the rates from the same budget-consumption logic — never copy these numbers onto a different SLO.
4. **AN-124 — Three severity tiers, honestly assigned.** Every alert is exactly one of: page (a human acts now), ticket (a human acts in working hours), or dashboard-only (informational, never routed as an alert). Anything burning slower than the paging rates in AN-123 is a ticket; "page everything to be safe" is a policy failure, not caution.
5. **AN-125 — Every page is actionable at the hour it fires.** The person paged must be able to do something that changes the outcome. If the correct response is "wait" or "ignore", the alert is reclassified to a lower tier, re-thresholded, or deleted — it is not endured.
6. **AN-126 — Complete payload or it does not ship.** Every alert carries: what is broken, the user impact, the runbook link, the dashboard link, and the escalation path. A paging alert without a runbook link does not ship.
7. **AN-127 — Every alert has a named owner.** Each alert rule names its owning team or person in the alert configuration itself. An ownerless alert is a defect: nobody is responsible for its threshold, its runbook, or its retirement.
8. **AN-128 — Routing is verified, not assumed.** Pages route through the alert manager with deduplication and grouping to the current on-call, never to a hardcoded individual or a channel nobody watches. A business-hours product may route to a monitored team inbox instead of a pager only where a named human demonstrably receives and acts on it.
9. **AN-129 — Silence is time-boxed and recorded.** Every silence or inhibition carries a reason and an expiry. An expired silence still in effect, or a silence with no expiry, is a defect; a permanently muted alert is fixed or deleted, never left pretending to protect anything.
10. **AN-130 — Alert quality is measured and pruned.** Track pages per period and the share that required action. On the review cadence, any alert that fired repeatedly with no action taken is fixed, demoted a tier, or deleted; a falling action share triggers an alert-review task, not greater tolerance for noise.
11. **AN-131 — Missing data is itself an alert.** If the metrics pipeline, an exporter, or the external synthetic check stops reporting, a dead-man's-switch alert fires through an independent path. "No data" never reads as "zero errors", and an external check on the public endpoints feeds the same paging path as internal alerts, so a total host or network failure still pages someone.
12. **AN-132 — Low-traffic mode is explicit.** Where request volume is too low for a burn rate to be meaningful, the policy says so and switches to longer windows, ticket-only tiers, and synthetic-check pages on critical flows. A threshold that can never fire, or that fires on ordinary noise, is a defect either way.

## BAN list

- **BAN-AN-061 — Alerts that reach nobody.** Banned: alert rules firing into an unmonitored channel, an unused chat room, a former team member's address, or no rule existing at all for downtime or error burn. Defeats: DET-INF-012. Bad: the error-rate alert posts to a Slack channel the team archived last quarter; a two-hour outage is discovered from user complaints. Instead: route pages through the alert manager to the current on-call and prove receipt with the G-AN-062 fire drill. Severity: BLOCK.
- **BAN-AN-062 — Cause-threshold paging.** Banned: a paging alert on a raw cause threshold — "CPU > 80% for 1 minute" — while the user-facing error rate has no alert of its own. Defeats: DET-INF-011. Bad: the pager fires on every deploy's CPU spike and stays silent through an afternoon of checkout 500s, because nothing alerts on the golden signals. Instead: page on SLO burn rate per AN-123; chart and ticket causes under monitoring. Severity: BLOCK.
- **BAN-AN-063 — A page with no way to act.** Banned: shipping a paging alert with no runbook link, no dashboard link, or no stated user impact, so the person paged starts from a blank page at 3 a.m. Defeats: DET-INF-029. Bad: "ALERT: latency high" arrives with a metric name and nothing else; the responder improvises while the incident clock runs. Instead: attach what is broken, user impact, runbook link, dashboard link, and escalation path per AN-126 — the G-AN-063 lint blocks anything less. Severity: BLOCK.
- **BAN-AN-064 — The permanent mute.** Banned: silencing a noisy alert indefinitely — no expiry, no ticket, no threshold fix — instead of repairing or deleting it. Defeats: DET-INF-012. Bad: a flapping disk alert is muted "until we get to it" in March; in November the disk fills during a launch and nothing pages. Instead: time-box the silence with a reason and a linked fix task per AN-129, or delete the alert at the AN-130 review. Severity: WARN.
- **BAN-AN-065 — Blind when the pipeline dies.** Banned: an alerting setup with no dead-man's switch and no external check, so a dead metrics pipeline, dead host, or dead network path presents as a quiet, healthy system. Defeats: DET-INF-028. Bad: the monitoring VM fails at midnight; every internal check dies with it and the team learns of the outage from social media. Instead: an independent external synthetic check plus an absence-of-data alert per AN-131, both feeding the paging path. Severity: BLOCK.

## Gates

- **G-AN-061 — Alert rules check.** Verifies: AN-123. Check: automated — run `promtool check rules` (or the alerting platform's equivalent validator) over the alert rule files in CI on every change to them. Pass: the validator exits 0 and every paging rule's windows and burn rates match the values derived for its SLO in the policy document. Fail: block the change. Recorded in: progress.md.
- **G-AN-062 — Fire drill.** Verifies: AN-126, AN-128. Check: automated in staging — stop a staging service (or fire the test alert) and time the result. Pass: a page reaches the current on-call channel within the documented time, deduplicated, carrying the runbook link and dashboard link. Fail: block shipment of the alert configuration; fix routing before any production reliance on it. Recorded in: progress.md.
- **G-AN-063 — Alert-config lint.** Verifies: AN-124, AN-126, AN-127. Check: automated — lint the alert configuration and assert every paging alert has a runbook link, a dashboard link, a stated user impact, a severity tier, and a named owner. Pass: zero paging alerts missing any field. Fail: block the change; the alert does not ship incomplete. Recorded in: progress.md.
- **G-AN-064 — Inventory audit.** Verifies: AN-129, AN-130. Check: automated — a scheduled report lists alerts with no runbook link, silences past their expiry, and alerts that fired three or more times in the period with no linked incident or action. Pass: the list is empty, or every listed item has a fix, demote, or delete task from the review. Fail: each unresolved item is recorded as a defect. Recorded in: progress.md.
- **G-AN-065 — Dead-man's-switch test.** Verifies: AN-131. Check: automated in staging — halt the metrics exporter/pipeline for the staging service. Pass: the absence-of-data alert fires within the documented window through the independent path, and the external synthetic check still reports. Fail: block reliance on the alerting setup until absence alerts as reliably as presence. Recorded in: progress.md.

## Anti-patterns

- **The deploy metronome.** An alert fires on every deploy and is acknowledged on reflex, so the one time it means something it is acked too. Catch it: the G-AN-064 audit's fired-with-no-action list — if a deploy-shaped pattern is on it, the alert is measuring deploys, not health.
- **The hero's phone number.** Escalation works because one named person's personal device is the real target, whatever the rotation says. Catch it: run the fire drill with that person unreachable; if the page dies with them, routing was never real (AN-128).
- **Threshold folklore.** Numbers like "80% for 1 minute" copied from a tutorial, with no SLO and no budget fraction behind them. Catch it: ask of any threshold, "which SLO, and what share of its budget does this consume?" — no answer, no alert (AN-123).
- **Dashboard theater.** Forty charts glow green in a tab nobody opens while no alert exists for the same signals — monitoring as decoration. Catch it: if a signal matters enough to chart, its burn has a tier under AN-124; if it does not, the chart is the decoration.

## Examples

- [Example 1 — The CPU page that fired on every deploy](examples/example-1.md) — violates/corrects AN-122.
- [Example 2 — The alert that posted to a dead channel](examples/example-2.md) — violates/corrects AN-128.
- [Example 3 — The alert muted since March](examples/example-3.md) — violates/corrects AN-129.

## Recall anchors

- Page on symptoms and burn rate; causes get tickets and dashboards.
- Thresholds are derived from the error budget, never copied.
- No runbook link, no page — incomplete alerts do not ship.
- Silence has an expiry; a permanent mute is a deleted alert lying.
- Missing data pages too: quiet is not the same as healthy.

## Checklist

- [ ] Every paging alert derives from a named SLO with budget-derived windows and burn rates (AN-123).
- [ ] No page fires on a cause alone; causes are ticketed or charted (AN-122).
- [ ] Every paging alert carries impact, runbook link, dashboard link, escalation path, and a named owner (G-AN-063).
- [ ] Fire drill reached the current on-call within the documented time (G-AN-062).
- [ ] All silences carry a reason and an unexpired time box (AN-129).
- [ ] The inventory audit is clean, or every noisy alert has a fix/demote/delete task (G-AN-064).
- [ ] Dead-man's switch and external check verified in staging (G-AN-065).
- [ ] Low-traffic services run the explicit low-traffic mode, not silent thresholds (AN-132).
