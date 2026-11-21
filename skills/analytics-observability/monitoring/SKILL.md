# monitoring

## Metadata

- **Owner department:** D12 Analytics & Observability (AN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Google, *Site Reliability Engineering*, "Monitoring Distributed Systems" — https://sre.google/sre-book/monitoring-distributed-systems/ ; Google, *The Site Reliability Workbook*, "Alerting on SLOs" — https://sre.google/workbook/alerting-on-slos/
- **Depends on:** none — standalone: SLIs, SLOs, and metric choices are defined from the service's own user journeys and the metrics the service exposes, measured directly; no other skill's output is required to set them up. It feeds alerting, dashboards, and apm.
- **Feeds into:** alerting, dashboards, apm

## When to use / Do NOT use

- **Use when:** setting up or changing how a user-facing service is monitored: defining its SLIs and SLOs, choosing its metrics and labels, writing scrape/recording-rule configuration, adding synthetic journey checks, or deciding whether the service may honestly be called "monitored".
- **Do NOT use when:** the question is infrastructure or platform telemetry — hosts, clusters, networks, the deploy pipeline, infra saturation signals, or the mechanics of being on call (rotations, escalation plumbing). **D6 owns that layer; this skill consumes D6's telemetry as dependency context and never redefines it.** D12 owns product and application signals and SLO policy: what is measured on user-facing behavior, and what the targets are. Alert construction and paging policy belong to alerting; panel layout belongs to dashboards.

## Rules

1. **AN-101 — Every monitored service has written SLIs.** For each user-facing service, the repo records its service-level indicators as ratios over the requests users make — at minimum an availability SLI (good responses / total responses) and a latency SLI (responses under a stated threshold / total responses) — each with its numerator, denominator, and data source named. An SLI that exists only in a dashboard query is not defined.
2. **AN-102 — SLO targets are written policy.** Each SLI carries an SLO target and a rolling window (e.g. 99.9% over 30 days), recorded in the repo next to the SLI definition. Targets change only through a recorded decision, never by editing a dashboard; alerting's burn-rate thresholds derive from these targets, so an undocumented target means an unjustifiable alert.
3. **AN-103 — The four golden signals are the minimum set.** Every user-facing service charts latency, traffic, errors, and saturation continuously. The working view is per-endpoint: error rate and latency percentiles for each route users actually call. A service missing any signal is recorded as partially monitored, with the gap named.
4. **AN-104 — Percentiles, never averages.** Latency is reported at p50/p95/p99, with success latency and error latency charted as separate series. Averages are banned from dashboards, SLO reports, and alert conditions because they hide exactly the tail users feel.
5. **AN-105 — Symptoms before causes.** Monitoring is built from the user inward: the first question is always which user-facing SLI is degrading. Cause-level signals (host CPU, connection pools, queue depth) are investigated second, as explanation — never as the primary health view of a service.
6. **AN-106 — Boundary: D6's telemetry is consumed, not redefined.** Host, cluster, and platform saturation signals are D6's; this skill reads them as dependency context for a service's saturation view. If a needed infra signal does not exist, the gap is raised with D6 — this skill does not stand up a parallel infra-monitoring stack.
7. **AN-107 — Labels are low-cardinality by design.** User IDs, request IDs, full URLs, and error strings never become metric labels; they belong in logs and traces. Every new metric declares a cardinality budget (the label set and its expected series count), and adding a label is reviewed like adding a column to a database.
8. **AN-108 — Monitoring configuration is code and is checked.** Scrape configs, recording rules, and alert-rule files live in the repo under review. `promtool check rules` (or the platform equivalent) runs in CI on every change and must pass; a config that does not parse is a broken change, not a production surprise.
9. **AN-109 — Missing data is itself a signal.** An absent metric — scrape target down, exporter dead, pipeline stalled — raises an absence alert through alerting's dead-man's-switch pattern. A flat line at zero is reported as "no data", never read as zero errors or zero traffic.
10. **AN-110 — A monitor that cannot page anyone is a dashboard.** A service counts as monitored only when a breached SLO or golden-signal threshold can reach a named human through the alerting path. Charts with thresholds but no route to a person are reporting; the service is recorded as unmonitored until the path exists.
11. **AN-111 — Synthetic checks run the primary journeys.** The primary user journeys (sign-in, the core action, checkout where one exists) run as synthetic checks on a short interval from outside the serving infrastructure, emitting the same golden signals as real traffic. This keeps the journeys measured at low real volume and catches total-path failures internal checks cannot see.
12. **AN-112 — Low traffic gets honest windows, not false precision.** Where request volume is too low for stable percentiles or burn rates, figures are reported with their window and sample count, and windows are lengthened until the sample supports the claim. A p99 computed from eleven requests is labeled as such or not shown.

## BAN list

- **BAN-AN-051 — Homepage-ping monitoring.** Banned: calling a service monitored because an uptime check pings the homepage while its working endpoints are unmeasured. Defeats: DET-INF-011. Bad: a 60-second ping on `/` reports 100% uptime for a week in which the checkout endpoint returned 500s nobody counted. Instead: expose and chart all four golden signals per service, with error rate queryable per endpoint (AN-103). Severity: BLOCK.
- **BAN-AN-052 — Average latency as the latency view.** Banned: charting or alerting on mean response time as a service's latency signal. Defeats: DET-INF-011. Bad: the dashboard shows "average latency 180 ms" while the checkout p99 sits at 4.2 s and users abandon. Instead: chart p50/p95/p99 bands with success and error latency as separate series (AN-104). Severity: BLOCK.
- **BAN-AN-053 — Thresholds with no route to a human.** Banned: shipping monitoring whose only breach notification is a colored panel, an unmonitored channel, or an inbox nobody owns. Defeats: DET-INF-012. Bad: the error rate crosses its threshold at 02:00; the "alert" is a red dashboard tile discovered on Monday. Instead: wire every SLO breach to the alerting path with a named on-call owner before calling the service monitored (AN-110). Severity: BLOCK.
- **BAN-AN-054 — Internal-only checks for a public service.** Banned: relying solely on checks that run inside the same infrastructure they watch, so a total failure silences every check at once. Defeats: DET-INF-028. Bad: the host dies at night; internal probes die with it, no external check exists, and the team learns of the outage from users. Instead: run external synthetic checks on the primary journeys, feeding the same paging path (AN-111). Severity: BLOCK.
- **BAN-AN-055 — Unbounded label cardinality.** Banned: attaching per-user, per-request, per-URL, or free-text values as metric labels. Defeats: DET-INF-027. Bad: a `user_id` label on the request counter creates millions of series, the metrics store saturates and drops data, and every dashboard gaps at once. Instead: keep labels to the declared low-cardinality set and put identifiers in logs and traces (AN-107). Severity: WARN.

## Gates

- **G-AN-051 — Monitoring config check.** Verifies: AN-108. Check: automated — run `promtool check config` and `promtool check rules` (or the platform equivalents) over every monitoring config file changed, in CI. Local evidence form: where no Prometheus estate exists, run a config-lint equivalent over the monitoring and alert configuration files (a parser and schema check that fails on any malformed file) and record the substitution in progress.md; the `promtool` (or platform-equivalent) check against the live estate remains required before public launch. Pass: all files parse with zero errors. Fail: block the merge. Recorded in: progress.md.
- **G-AN-052 — Golden-signal coverage check.** Verifies: AN-101, AN-103. Check: automated — a script lists user-facing services from the service registry and queries the metrics backend for each service's latency, traffic, errors, and saturation series over the last 24 hours, plus a written SLI definition in the repo. Local evidence form: where no live metrics backend exists, record each service's four golden-signal SLI definitions in the repo with the instrumentation points named, and record the substitution in progress.md; the live-series check against the metrics backend remains required before public launch. Pass: every service has all four signals with live data and a recorded SLI. Fail: the service is recorded as unmonitored and the gap is a release defect. Recorded in: progress.md.
- **G-AN-053 — Synthetic journey signal check.** Verifies: AN-104, AN-111. Check: automated — run the synthetic checks for each primary journey, then force one journey to fail in staging; assert the journey's latency, traffic, and error series exist and the forced failure appears in the per-endpoint error view within one check interval. Pass: signals present and the failure is visible. Fail: block; the journey is unmeasured. Recorded in: progress.md.
- **G-AN-054 — Cardinality audit.** Verifies: AN-107. Check: automated — a scheduled query lists the highest-cardinality series and every label name in use; flag any label matching ID, URL, email, or free-text patterns and any metric above its declared budget. Pass: no flagged labels and no metric over budget. Fail: file a defect; block the merge that adds the offending label. Recorded in: progress.md.
- **G-AN-055 — Dead-man's-switch drill.** Verifies: AN-109, AN-110. Check: in staging, stop a service's exporter and confirm the absence alert reaches the named on-call channel within the documented time; repeat for the scrape target. Pass: both absence alerts arrive, labeled as missing data. Fail: monitoring for that service is declared non-functional until fixed. Recorded in: progress.md.

## Anti-patterns

- **The CPU-first dashboard.** The top chart is host CPU while the checkout endpoint's error rate is unmeasured — cause before symptom. Catch it: if the first panel is not a golden signal, rebuild the view from the user inward (AN-105).
- **The wall of charts.** Dozens of auto-generated panels nobody opens during an incident, with the three that matter on page four. Catch it: for each panel, name who reads it and when; silence means delete.
- **Cause-hunting first.** An incident opens with host graphs and deploy diffs before anyone checks which user journey is failing. Catch it: the first question is always "which SLI is burning?" — causes are the second step.
- **Tutorial thresholds.** SLO targets and alert thresholds copied from a blog post or a vendor default instead of derived from the service's users and error budget. Catch it: every target must trace to the written SLO policy (AN-102); no trace, no threshold.

## Examples

- [Example 1 — The homepage ping that called itself monitoring](examples/example-1.md) — violates/corrects AN-103.
- [Example 2 — The 180 ms average hiding a 4.2-second tail](examples/example-2.md) — violates/corrects AN-104.
- [Example 3 — The zero-error week that was a dead exporter](examples/example-3.md) — violates/corrects AN-109.

## Recall anchors

- Monitor the user's journey first; causes explain, symptoms decide.
- Percentiles or it didn't happen — averages hide the tail users feel.
- No written SLI and SLO, no claim of "monitored".
- Absent data is an alarm, never a zero.
- If it cannot page a human, it is a dashboard, not monitoring.

## Checklist

- [ ] Every user-facing service has written availability and latency SLIs in the repo (AN-101).
- [ ] SLO targets and windows are recorded as policy next to the SLIs (AN-102).
- [ ] Coverage check passes: all four golden signals live for every service (G-AN-052).
- [ ] Latency views show p50/p95/p99 with success and error series separated (AN-104).
- [ ] `promtool check rules` passes on all monitoring configuration (G-AN-051).
- [ ] Cardinality audit is clean: no ID/URL/free-text labels, no metric over budget (G-AN-054).
- [ ] Synthetic checks run the primary journeys from outside the infrastructure (G-AN-053).
- [ ] Exporter-outage drill produced an absence alert at the on-call channel (G-AN-055).
