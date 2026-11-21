# logging

## Metadata

- **Owner department:** D12 Analytics & Observability (AN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OWASP, *Logging Cheat Sheet* — https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html ; OpenTelemetry, "Observability primer" — https://opentelemetry.io/docs/concepts/observability-primer/ ; PROJECT_ANATOMY.md, "Logging"
- **Depends on:** none — standalone: log format, field set, and redaction rules are defined against the application's own code and the events it emits, inspected directly; this is the base layer the rest of D12 reads from. It feeds monitoring, alerting, error-tracking, and apm.
- **Feeds into:** monitoring, alerting, error-tracking, apm

## When to use / Do NOT use

- **Use when:** setting up or changing how an application logs: the log format and field set, correlation IDs, levels, redaction, shipping to a central store, or retention — for any service whose behavior someone will need to reconstruct later.
- **Do NOT use when:** the question is infrastructure or platform telemetry — hosts, clusters, networks, the deploy pipeline, infra saturation, or the mechanics of being on call (D6 owns those; this skill consumes D6's telemetry, never redefines it). This skill owns the application-signal discipline: what the application itself records, in what shape, and how long it is kept. Alert policy on top of logs is alerting's; the SLOs logs serve are D12 policy, the paging plumbing is D6's.

## Rules

1. **AN-081 — One logger, one format.** Every service logs through the shared logger, which emits single-line JSON with the fixed field set: timestamp (UTC, ISO 8601), level, service, environment, trace ID, request ID, message, plus structured context fields. A line missing a standard field is a defect, not a style choice.
2. **AN-082 — Boundary: application signals here, infrastructure with D6.** This skill defines what the application logs and how those logs are shaped, shipped, and retained. Host, cluster, and platform logs, the collector's infrastructure, and on-call mechanics belong to D6; where an incident needs both, the trace ID (AN-083) is the join, and neither side redefines the other's signals.
3. **AN-083 — Correlation ID on every request-scoped line.** A trace/request ID is generated or accepted at ingress and propagated across every service, queue, and background-job boundary the request crosses. A log line that cannot be tied to its request is of forensic value only by luck.
4. **AN-084 — Levels are a contract.** `error` means a human may need to act; `warn` means degraded but handled; `info` means a business-significant event; `debug` is detail for active diagnosis. Debug logging is off by default in production and is raised per service, temporarily, with the raise recorded.
5. **AN-085 — Secrets and personal data are never logged.** Passwords, tokens, authorization headers, session IDs, card numbers, and direct personal identifiers are redacted by the logger's field denylist before a line is written — enforcement lives in the logger, never in developer memory (OWASP Logging Cheat Sheet). The denylist is configuration in the repo, reviewed like code.
6. **AN-086 — Log the event, not the data dump.** Log lines carry named context fields (order ID, status, duration, outcome), never serialized request bodies, whole objects, or full payloads: a dump leaks whatever the object happens to contain and buries the fact that matters.
7. **AN-087 — Logs ship off the host.** Logs are shipped by a collector or shipper to a central, searchable store; a file on the host or container stdout is transport, never the record — containers are ephemeral, so local logs are lost logs. Retention is tiered (hot search window, then archive, then deletion) on the schedule D14's rules set.
8. **AN-088 — No raw console logging in production paths.** Free-text `console.log`-style calls in server production paths are a lint failure with a count of zero; all production logging goes through the shared logger so the field set, redaction, and shipping of AN-081/085/087 always apply.
9. **AN-089 — An error is logged once, as an error.** A failure is logged at the boundary that handles it, at `error` level, with its stack and correlation ID, and captured by error-tracking. Empty catch blocks and failures logged at `info` or `warn` so dashboards stay green are defects: the error signal must be able to tell the truth.
10. **AN-090 — Log volume is a budget.** Noisy success-path logging at scale is a defect: it buries errors and bills like them. High-cardinality identifiers (user IDs, request IDs) belong in log fields, where they are searchable — never in metric labels, which is monitoring's rule and this skill's hand-off.
11. **AN-091 — Retention and deletion reach the log store.** The retention schedule is written down per environment, and a deletion request that covers logs is executed against the central store and its archives, with the execution recorded; "the vendor probably handles it" is not a retention policy (the rules are D14's; this skill implements them for logs).
12. **AN-092 — Logging configuration lives in the repo.** The field set, level defaults, denylist, and retention tiers are versioned configuration, changed by reviewed commits. A logging change that exists only in a vendor console does not exist for the next agent.

## BAN list

- **BAN-AN-041 — Logs that die with the container.** Banned: application logs written only to a local file or host stdout, never shipped, so a restart or redeploy erases the only record of what the service did. Defeats: DET-INF-013. Bad: after a redeploy, the team debugs a payment failure from memory because the previous container's logs vanished with it. Instead: ship every line through the collector to the central store before the work is called done (AN-087). Severity: BLOCK.
- **BAN-AN-042 — Secrets or personal data in log lines.** Banned: logging credentials, tokens, authorization headers, card data, or personal identifiers — in a field, in a dumped object, or in an error message — whether the store is local or central. Defeats: DET-INF-021. Bad: a login handler logs the submitted form, and the central store accumulates every user's password in searchable plain text. Instead: redact by the logger's denylist (AN-085) and log identifiers and outcomes, never values (AN-086). Severity: BLOCK.
- **BAN-AN-043 — Swallowed or downgraded errors.** Banned: empty catch blocks, or logging a real failure at `info`/`warn` (or as "handled") so error rates and dashboards read healthy while users hit failures. Defeats: DET-INF-011. Bad: a checkout exception is caught, logged as `info: "checkout note"`, and discarded; the errors golden signal reads zero during an outage users are reporting. Instead: log the failure once at `error` with stack and correlation ID and let error-tracking capture it (AN-089). Severity: BLOCK.
- **BAN-AN-044 — The debug firehose left on.** Banned: shipping or leaving a service at debug/trace verbosity in production, so log volume saturates disk or the central store and drowns the error signal. Defeats: DET-INF-027. Bad: a debug flag set during an incident is never reverted; three weeks later the log volume has tripled, retention silently shrank, and the disk-full alert is the first symptom. Instead: debug is off by default, raised per service for a bounded time, and reverted with the incident (AN-084, AN-090). Severity: WARN.

## Gates

- **G-AN-041 — Production-path logging lint.** Verifies: AN-081, AN-088. Check: automated — run the repo lint/grep suite over server production paths (e.g. `grep -rnE "console\.(log|debug)|print\(" src/ --include="*.ts" --include="*.js"` outside test and logging-module files, plus a schema spot-check that logger call sites pass the standard field set). Pass: zero raw console calls and zero missing-field call sites. Fail: block the release. Recorded in: progress.md.
- **G-AN-042 — Redaction canary test.** Verifies: AN-085, AN-086. Check: automated — in staging, submit a request carrying the canary values `CANARY-PASSWORD-EXAMPLE` and `CANARY-TOKEN-EXAMPLE` through the login and one authenticated flow, then search the central log store for both strings. Pass: zero occurrences in any field, message, or stack. Fail: block shipment; fix the denylist or the call site and re-run. Recorded in: progress.md.
- **G-AN-043 — Schema validation of shipped lines.** Verifies: AN-081. Check: automated — sample the most recent 1,000 lines per service from the central store and validate each against the field-set schema (required keys present, timestamp parses as ISO 8601 UTC, level in the allowed set). Pass: 100% of sampled lines validate. Fail: block the release for the failing service. Recorded in: progress.md.
- **G-AN-044 — Trace-join test.** Verifies: AN-083, AN-089. Check: pick one failed request from the error tracker, take its trace ID, and query the central store for that ID in every service the request touched. Pass: each service returns entries under the same trace ID, including the `error` line with its stack. Fail: fix propagation at the silent boundary before the next release. Recorded in: progress.md.
- **G-AN-045 — Restart persistence test.** Verifies: AN-087, AN-091. Check: automated-assisted — note a marker log line in a non-production instance, restart or redeploy the instance, then query the central store for the marker and confirm the configured retention settings on the store match the written schedule. Pass: the pre-restart line is still queryable and retention matches the schedule. Fail: treat as a BAN-AN-041 defect and block promotion. Recorded in: progress.md.

## Anti-patterns

- **The data-dump line.** Logging the whole request or object "just in case," so the one field that matters hides inside two kilobytes of noise — and whatever sensitive value the object carried ships with it. Catch it: if a line cannot be read at a glance, it is a dump, not an event (AN-086).
- **Log-and-throw at every layer.** Each layer logs the same exception and rethrows, so one failure becomes five `error` lines and every count of errors is inflated. Catch it: search one trace ID — the failure should appear exactly once, at the handling boundary (AN-089).
- **Prose messages.** Log text written as full sentences with values interpolated ("User 42 failed to check out because…") instead of a stable message plus fields, so nothing can be grouped, counted, or alerted on. Catch it: if the same event cannot be found with one exact-match search, it was written as prose.
- **Localhost observability.** Logging verified only against a developer machine's console, where every line looks fine, while the deployed service's format, shipping, and retention were never exercised. Catch it: any logging claim not backed by a query against the central store is unverified (G-AN-043, G-AN-045).

## Examples

- [Example 1 — Console breadcrumbs become structured logs](examples/example-1.md) — violates/corrects AN-081, AN-088.
- [Example 2 — The login handler that logged passwords](examples/example-2.md) — violates/corrects AN-085.
- [Example 3 — The failure no one could reconstruct](examples/example-3.md) — violates/corrects AN-083, AN-087.

## Recall anchors

- One logger, one JSON field set — no exceptions in production paths.
- Every line carries its trace ID, or it cannot be used.
- The logger redacts; developers never have to remember to.
- Error means a human may need to act — never log a failure as less.
- If it is not in the central store, it did not happen.

## Checklist

- [ ] All production logging goes through the shared logger; the raw-console lint count is zero (G-AN-041).
- [ ] Every request-scoped line carries trace and request IDs across services and jobs (AN-083).
- [ ] The denylist covers passwords, tokens, authorization headers, session IDs, and card numbers, and lives in the repo (AN-085).
- [ ] The redaction canary test returns zero hits in the central store (G-AN-042).
- [ ] Sampled shipped lines validate 100% against the field-set schema (G-AN-043).
- [ ] A failed request's trace ID returns entries from every service it touched (G-AN-044).
- [ ] Logs survive a restart in the central store, and retention matches the written schedule (G-AN-045).
- [ ] Debug verbosity is off in production, or raised per service with a recorded revert (AN-084).
