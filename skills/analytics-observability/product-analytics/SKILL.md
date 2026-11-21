# product-analytics

## Metadata

- **Owner department:** D12 Analytics & Observability (AN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Segment, "Data Collection Best Practices" — https://segment-docs.netlify.app/docs/protocols/tracking-plan/best-practices/ ; PROJECT_ANATOMY.md, "Analytics"
- **Depends on:** product-metrics (D1 — owns metric definitions), event-tracking
- **Feeds into:** web-analytics (D9), dashboards, experimentation-platform, revenue-analytics

## When to use / Do NOT use

- **Use when:** setting up or changing product analytics for a project: choosing what to measure, writing the tracking plan, instrumenting flows, defining identity and consent behavior, or building the product dashboards a team actually reads.
- **Do NOT use when:** the question is infrastructure telemetry (hosts, clusters, deploy pipeline — D6 owns it; this skill consumes it, never redefines it), search/acquisition reporting (web-analytics, D9, consumes this skill's tracking plan), or the legal rules for consent and retention themselves (privacy-laws and cookie-consent, D14, own the rules; this skill enforces them in instrumentation).

## Rules

1. **AN-001 — Tracking plan before instrumentation.** No event is implemented before the shared tracking plan exists in the repo: every metric maps to the events and properties that compute it, the platform that stores them, and the review cadence that reads them. D1's product-metrics owns the definitions; this skill owns measurement against them.
2. **AN-002 — No undefined metric ships.** A metric appears on a dashboard or in a report only when its definition and its source events are written in the metrics document. A number nobody can define is removed, not footnoted.
3. **AN-003 — Identity is decided once, in writing.** The plan states what the anonymous ID is, when `identify` happens, and how pre- and post-login behavior stitches. Changing identity rules later requires a plan amendment and a note on which historical data is affected.
4. **AN-004 — Consent before collection.** Non-essential analytics does not fire before the visitor's consent state is known, and never fires when consent is denied. Consent state itself is recorded, so every report can state its coverage honestly instead of implying a full census.
5. **AN-005 — Few, well-shaped events.** Prefer a small set of events with rich properties over one event per button. Every event in the plan names the question it answers and its owner; an event with neither is not added.
6. **AN-006 — Boundary: one tracking plan, two consumers.** This skill owns product and application signals and the shared tracking plan. D9's web-analytics consumes the same plan for search and acquisition reporting — it does not create a parallel event taxonomy. Event names and definitions change only through the plan, so both consumers keep reading the same numbers.
7. **AN-007 — Validate before release.** Before any release that touches instrumentation, the primary conversion and retention flows are run in a test session and every expected event is confirmed in the platform's debug or realtime view: present, correctly named, correctly parameterized.
8. **AN-008 — No unplanned events.** Application code emits only events that exist in the tracking plan. A new measurement need amends the plan first (AN-001); code that emits an unlisted event fails review.
9. **AN-009 — No personal data in properties.** Event properties never carry email addresses, names, free-text user input, or other direct identifiers as values. The user ID is the platform's identifier and nothing else; the PII rules themselves are D14's, the enforcement here is structural.
10. **AN-010 — Metrics are computed from live records.** Every reported figure is computed from the event stream or the underlying records at read time. A figure that cannot move when the underlying data changes is not a metric and never appears on a dashboard.
11. **AN-011 — Recurring data-quality review.** On the cadence named in the plan, review the event stream for orphan events (firing but unplanned), unplanned volume anomalies, and broken funnels; log findings and fixes in the project's progress.md.
12. **AN-012 — Every dashboard has an audience and a decision.** Each dashboard states who reads it and what decision it informs. A dashboard nobody acts on is deleted, not archived forever.

## BAN list

- **BAN-AN-001 — Frozen dashboard numbers.** Banned: a dashboard or report figure rendered from a constant, a fixture, or a hand-typed value instead of the live event stream. Defeats: DET-FAKE-004. Bad: the overview shows "Active users: 1,240" from a value typed into the dashboard config at launch; it reads 1,240 in month three. Instead: compute the figure from the event stream at read time, with its definition from AN-002 attached. Severity: BLOCK.
- **BAN-AN-002 — Collection before consent.** Banned: loading or firing non-essential analytics before consent state is known, or continuing to fire after consent is denied, while the privacy notice promises consent-based collection. Defeats: DET-CON-028. Bad: the analytics snippet sits in the page head and fires a pageview on first load, seconds before the consent banner is answered. Instead: initialize the platform only after consent resolves, and record the consent state per AN-004. Severity: BLOCK.
- **BAN-AN-003 — Undefined statistics presented as fact.** Banned: reporting a quantitative claim ("10,000 active users", "38% conversion") that has no written definition and no source events behind it. Defeats: DET-CON-011. Bad: a launch report claims 10,000 active users; no document defines "active", and the figure is a pageview count relabeled. Instead: cite the metric's definition and source events from the metrics document, or cut the claim. Severity: BLOCK.
- **BAN-AN-004 — Duplicate or variant event names.** Banned: emitting the same action under two or more names or spellings (`signup`, `sign_up`, `Signup Completed`) so reports silently fragment. Defeats: DET-CON-017. Bad: the web app fires `checkout_started` and the API fires `checkoutStarted`; the funnel report counts half of each and trusts both. Instead: one canonical name per action, fixed in the tracking plan, with variants aliased or removed at the emitter. Severity: WARN.
- **BAN-AN-005 — Two definitions of one metric.** Banned: letting two dashboards or reports compute the same named metric differently, so the product contradicts itself depending on where it is read. Defeats: DET-CON-015. Bad: the overview counts a "weekly active user" as any pageview; the retention report counts only users who completed the core action; both are quoted in the same meeting. Instead: one definition in the metrics document, computed identically everywhere; a genuinely different measure gets a different name. Severity: BLOCK.

## Gates

- **G-AN-001 — Tracking-plan diff on a scripted session.** Verifies: AN-001, AN-007, AN-008. Check: automated — run the primary conversion and retention flows in a test session with event capture on; diff the captured events against the tracking plan: every planned event fired with the correct name and property shape, and zero unplanned events fired. Pass: the diff is empty in both directions. Fail: block the release; fix instrumentation or amend the plan first. Recorded in: progress.md.
- **G-AN-002 — Consent test.** Verifies: AN-004. Check: automated — open a fresh session with consent denied and exercise the main flows while logging network requests; then repeat with consent granted. Pass: zero analytics requests in the denied session, and events flow in the granted session. Fail: block shipment. Recorded in: progress.md.
- **G-AN-003 — Metric definition audit.** Verifies: AN-002, AN-006, AN-012. Check: list every metric shown on every live dashboard and report; for each, confirm a written definition and named source events exist in the metrics document and that the stated audience and decision are recorded. Pass: 100% of displayed metrics trace to a definition. Fail: remove or define the untraceable metrics before the next report ships. Recorded in: progress.md.
- **G-AN-004 — Property payload scan.** Verifies: AN-009. Check: automated — scan the events captured in the G-AN-001 session for email-shaped strings, and for property keys outside the plan's declared set. Pass: no email-shaped value appears in any property, and no undeclared key is present. Fail: block the release; strip the property at the emitter. Recorded in: progress.md.
- **G-AN-005 — Live-data movement check.** Verifies: AN-010. Check: perform one known action the metric counts (complete one test conversion), wait one stated refresh cycle, and re-read the dashboard figure. Pass: the figure moved by exactly the known amount. Fail: treat the panel as a frozen-number defect under BAN-AN-001 and block the report. Recorded in: progress.md.

## Anti-patterns

- **The 40-panel overview.** Every event anyone ever requested gets a panel; nobody reads past the first row, and the three numbers that matter drown. Catch it: ask of each panel, "what decision did this change last month?" — silence means delete (AN-012).
- **Retroactive identity repair.** Launching with anonymous-only tracking, then trying to stitch months of pre-login behavior onto accounts after the fact. Catch it: if the plan has no written stitching rule before launch, that repair is already scheduled (AN-003).
- **Screenshot reporting.** Numbers copied from a realtime view into a deck before the events were ever validated, then quoted as results. Catch it: any figure that cannot name the validated event stream behind it is a screenshot, not a measurement (AN-007).
- **Pageviews as strategy.** The snippet is installed, auto-collected pageviews accumulate, and the team calls it an analytics setup while no conversion or retention flow is instrumented. Catch it: if the plan's event list is empty, there is no setup yet (AN-001, AN-005).

## Examples

- [Example 1 — The dashboard number that never moved](examples/example-1.md) — violates/corrects AN-010.
- [Example 2 — Pageviews-only "analytics" becomes a measurement plan](examples/example-2.md) — violates/corrects AN-001.
- [Example 3 — Analytics firing before the consent answer](examples/example-3.md) — violates/corrects AN-004.

## Recall anchors

- No metric without a written definition and named source events.
- Plan first, instrument second — code emits only what the plan lists.
- Consent state is known before anything fires, and is itself recorded.
- D12 owns the tracking plan; D9 reads it, never forks it.
- A figure that cannot move is not a metric.

## Checklist

- [ ] Tracking plan is in the repo; every metric maps to events, a platform, and a review cadence (AN-001).
- [ ] Identity rules (anonymous ID, identify moment, stitching) are written in the plan (AN-003).
- [ ] Scripted-session diff against the plan is empty in both directions (G-AN-001).
- [ ] Consent-denied session produced zero analytics requests (G-AN-002).
- [ ] Every displayed metric traces to a definition in the metrics document (G-AN-003).
- [ ] Captured payloads contain no email-shaped values or undeclared keys (G-AN-004).
- [ ] A known test action moved its dashboard figure by exactly that amount (G-AN-005).
- [ ] Every live dashboard names its audience and the decision it informs (AN-012).
