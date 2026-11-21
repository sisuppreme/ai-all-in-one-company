# error-tracking

## Metadata

- **Owner department:** D12 Analytics & Observability (AN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OpenTelemetry, "Observability primer" — https://opentelemetry.io/docs/concepts/observability-primer/ ; OWASP, *Logging Cheat Sheet* — https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html ; PROJECT_ANATOMY.md, "Error handling" and "Logging"
- **Depends on:** logging
- **Feeds into:** alerting, monitoring, dashboards

## When to use / Do NOT use

- **Use when:** setting up or changing how unhandled errors are captured, grouped, scrubbed, triaged, and read at release time — for any client or server surface whose failures someone must learn about from the system, not from user complaints.
- **Do NOT use when:** the question is application log format, levels, or shipping (logging owns those; this skill consumes the correlation ID logging guarantees), alert routing and burn-rate policy (alerting owns the page; this skill owns the issues alerts point at), or fixing the defect itself (the owning department's skill fixes it; this skill makes sure it is seen, owned, and verified gone).

## Rules

1. **AN-161 — Every unhandled error is captured in the tracker.** Client and server unhandled errors are captured by the dedicated error tracker (Sentry is the reference implementation) at the boundary where they surface. An error users can hit that exists only in a log file — or nowhere — is a defect in the error handling itself, not a gap to note.
2. **AN-162 — Every event carries its context.** Each captured event carries a readable stack trace, the release version, the environment, and the request's trace/correlation ID, so an issue pivots straight into the logs and traces for the same request (per the OpenTelemetry correlation model). An event missing release or correlation ID is incomplete and fails G-AN-081.
3. **AN-163 — Context is scrubbed before it leaves.** A before-send scrubber with a denylist in the repo strips passwords, tokens, authorization headers, session IDs, card numbers, and direct personal identifiers from event payloads, breadcrumbs, and attached request data before transmission — enforcement lives in the scrubber, never in developer memory (OWASP Logging Cheat Sheet). Obvious placeholders only in examples and tests.
4. **AN-164 — Source maps ship with the release.** Source maps (and server symbolication inputs) are uploaded to the tracker as a step of the release pipeline. A release that ships without its maps uploaded is an incomplete release, because every stack from it is undebuggable minified offsets.
5. **AN-165 — Release and environment tags are mandatory.** Every event is tagged with the exact release and environment that produced it; untagged events cannot be attributed to a deploy, counted in release health, or recognized as regressions, and are treated as a capture defect.
6. **AN-166 — Grouping is curated.** Fingerprint rules merge one root cause into one issue and split distinct causes that share a generic message. A tracker where one bug appears as hundreds of issues gets ignored, which is the same as having no tracker; grouping rules are reviewed whenever issue volume jumps.
7. **AN-167 — Expected errors are not issues.** Handled, user-facing errors by design — validation failures, 404s for genuinely missing resources, denied permissions — are logged or counted as metrics, never captured as tracker issues. The tracker is reserved for defects; noise in it is how real defects get missed.
8. **AN-168 — Every issue has a named owner and a triage cadence.** New issues are assigned to a named owner within the project's stated triage window, and the tracker is triaged on that cadence whether or not anyone feels like it. An error nobody owns is a bug that ships twice; a tracker installed but never triaged is decoration.
9. **AN-169 — Priority follows user impact.** Issues are ranked by affected users and by whether the flow is revenue- or trust-critical, not by raw event count alone: a rare failure on the payment path outranks a frequent failure on a settings page.
10. **AN-170 — Regressions reopen, they do not restart.** A resolved issue whose error recurs in a newer release is flagged by the tracker as a regression of the original issue — with its history and owner — and pages or tickets by user impact. A regression silently opened as a brand-new issue loses the record that it was already "fixed" once.
11. **AN-171 — Release health is read at every deploy.** Crash-free sessions and crash-free users per release are checked after each deploy against the project's stated threshold; a release below threshold triggers a rollback or hotfix decision, recorded — not a hope that the numbers recover.
12. **AN-172 — Tracker configuration lives in the repo.** The SDK configuration, scrubbing denylist, fingerprint rules, and alert rules are versioned configuration in the repo, changed by reviewed commits. Setup that exists only in the tracker vendor's console does not exist for the next agent.

## BAN list

- **BAN-AN-081 — Swallowed errors.** Banned: empty catch blocks, caught-and-discarded exceptions, or a failure path that reports success — any pattern where an error happens and no system records it. Defeats: DET-INF-011. Bad: a failed payment throws, the catch block is empty, the user sees "Success," and the team learns about the lost orders from complaints a week later. Instead: let unhandled errors reach the tracker with stack and correlation ID, and show the user an honest failure state (AN-161, AN-162). Severity: BLOCK.
- **BAN-AN-082 — "The logs probably have it."** Banned: relying on log text as the error record — no dedicated tracker, no grouping, no release tags — so finding one bug means grepping raw output and counting occurrences by hand. Defeats: DET-INF-013. Bad: after a bad deploy, the only way to know what broke is to SSH in and read container output that the next redeploy will erase. Instead: capture errors in the tracker, grouped into issues with readable stacks and release tags (AN-161, AN-164, AN-165). Severity: BLOCK.
- **BAN-AN-083 — Stack traces served to users.** Banned: rendering raw exceptions, stack traces, SQL, or file paths in the user-facing error response while the same failure is captured nowhere server-side. Defeats: DET-INF-021. Bad: a 500 page shows the full framework stack trace with internal paths, and the tracker has no record of the error at all. Instead: return a generic error response with a correlation ID the user can quote, and capture the full detail in the tracker under that same ID (AN-161, AN-162). Severity: BLOCK.
- **BAN-AN-084 — The ownerless tracker.** Banned: a tracker that is installed and capturing, but whose new-issue alerts route to an unmonitored inbox or channel and whose issues have no named owner or triage cadence. Defeats: DET-INF-012. Bad: the tracker holds 300 unassigned issues, the alert email goes to a mailbox nobody opens, and a checkout defect runs for a month. Instead: route new-issue and regression alerts to the monitored on-call channel and assign every issue an owner within the triage window (AN-168, AN-170). Severity: WARN.

## Gates

- **G-AN-081 — Synthetic-error capture test.** Verifies: AN-161, AN-162, AN-165. Check: automated — in staging, trigger one known client error and one known server error through the test hooks; within 60 seconds query the tracker. Pass: each error appears exactly once, grouped as a single issue, with a de-minified stack naming real source lines, the correct release and environment tags, and a correlation ID that resolves to entries in the central log store. Fail: block the release; fix capture, maps, or tagging and re-run. Recorded in: progress.md.
- **G-AN-082 — Source-map upload check.** Verifies: AN-164. Check: automated — CI asserts the release pipeline's source-map upload step ran for the release being deployed and the uploaded artifact set matches the build output. Pass: upload step succeeded for this exact release. Fail: block the deploy; the release is incomplete. Recorded in: progress.md.
- **G-AN-083 — Scrub canary test.** Verifies: AN-163. Check: automated — in staging, trigger an error from a request carrying the canary values `CANARY-PASSWORD-EXAMPLE` and `CANARY-TOKEN-EXAMPLE`, then search the resulting tracker event (payload, breadcrumbs, request data) for both strings. Pass: zero occurrences anywhere in the event. Fail: block shipment; fix the denylist or scrubber and re-run. Recorded in: progress.md.
- **G-AN-084 — Regression drill.** Verifies: AN-170. Check: in staging, mark a known synthetic issue resolved, reintroduce its error, and inspect the tracker. Pass: the original issue is flagged as a regression with its history intact, not opened as a new issue, and the regression alert reaches the monitored channel. Fail: fix fingerprinting and regression settings before the next release. Recorded in: progress.md.
- **G-AN-085 — Triage and ownership audit.** Verifies: AN-168, AN-169. Check: automated-assisted — list every unresolved issue older than the project's triage window and every issue with no named owner. Pass: zero unowned issues and zero issues past the triage window without a recorded priority decision (impact-ranked per AN-169). Fail: triage before the next deploy; an audit that keeps failing is a BAN-AN-084 defect. Recorded in: progress.md.

## Anti-patterns

- **The 400-issue bug.** One root cause fragments into hundreds of issues because grouping was never curated, so the board reads as chaos and gets abandoned. Catch it: sort by event count — if the top events share a stack shape, the fingerprint rules are the defect (AN-166).
- **Resolve-and-forget.** Issues are marked resolved with no linked fix or release, so "resolved" means "we stopped looking" and the regression, when it comes, surprises everyone. Catch it: sample resolved issues — each should name the release that fixed it (AN-170, AN-171).
- **Count-chasing.** The board is worked top-down by raw event count, so the loudest cosmetic error gets fixed while a rare payment failure waits. Catch it: if the priority order cannot be explained in affected users and flow criticality, it is count order, not impact order (AN-169).
- **The muted tracker.** Ignore and snooze rules grow until the tracker goes quiet — not because the product improved, but because the team tuned the alarm off. Catch it: a sudden drop in new issues after a rule change is a signal about the rules, not about the code.

## Examples

- [Example 1 — The payment failure that displayed "Success"](examples/example-1.md) — violates/corrects AN-161.
- [Example 2 — The release nobody could debug](examples/example-2.md) — violates/corrects AN-164, AN-165.
- [Example 3 — The error event that carried a password](examples/example-3.md) — violates/corrects AN-163.

## Recall anchors

- If users can hit it, it is a tracked issue with a readable stack.
- Release tag and correlation ID on every event, or it cannot be used.
- The scrubber strips secrets; developers never have to remember to.
- An unowned error is a bug that ships twice.
- Release health is read at the deploy, not after the complaints.

## Checklist

- [ ] Unhandled client and server errors reach the tracker; no empty catch blocks or success-on-failure paths remain (BAN-AN-081).
- [ ] The synthetic-error test passes: grouped once, de-minified stack, release tag, correlation ID resolving in the log store (G-AN-081).
- [ ] The source-map upload step ran for this release and is asserted in CI (G-AN-082).
- [ ] The scrub canary test returns zero hits in the tracker event (G-AN-083).
- [ ] Expected errors (validation, by-design 404s) are metrics or logs, not tracker issues (AN-167).
- [ ] Every issue has a named owner within the triage window, prioritized by user impact (G-AN-085).
- [ ] The regression drill flags a reintroduced error as a regression, not a new issue (G-AN-084).
- [ ] Release health (crash-free sessions/users) is checked against threshold at this deploy (AN-171).
