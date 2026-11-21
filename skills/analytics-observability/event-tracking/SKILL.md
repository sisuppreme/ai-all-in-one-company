# event-tracking

## Metadata

- **Owner department:** D12 Analytics & Observability (AN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Twilio Segment, "Naming conventions: why you need them for clean data" — https://www.twilio.com/en-us/resource-center/naming-conventions-for-clean-data ; Segment documentation, "Data Collection Best Practices" (tracking plan guidance) — https://segment-docs.netlify.app/docs/protocols/tracking-plan/best-practices/
- **Depends on:** product-analytics
- **Feeds into:** product-analytics, experimentation-platform, revenue-analytics

## When to use / Do NOT use

- **Use when:** adding, renaming, or removing an analytics event; writing or changing instrumentation code; reviewing a funnel or report that looks wrong; setting up validation for a new analytics platform.
- **Do NOT use when:** the question is which metrics the product should report (product-metrics, D1; measurement setup is product-analytics), what an experiment's result means (experimentation-platform), or whether revenue figures reconcile (revenue-analytics). This skill owns the event taxonomy as a contract, not the conclusions drawn from it.

## Rules

1. **AN-021 — The plan precedes the code.** The tracking plan is a versioned file in the repo recording, per event: name, properties with types, required/optional status, owner, and the question the event answers. No event is emitted that is not in the plan; adding an event means editing the plan first, in the same change.
2. **AN-022 — One naming convention, enforced mechanically.** Events are Object-Action in past tense under one casing standard, and properties under one casing standard, chosen once and never varied (Segment's reference: Title Case events such as "Order Completed", snake_case properties). A name that deviates from the convention is a defect even if it is spelled correctly.
3. **AN-023 — No dynamic values in event names.** An event name contains no product names, IDs, prices, search terms, or user data. The varying value goes in a property; one event per value turns one report row into hundreds and fragments every funnel built on it.
4. **AN-024 — Property keys are fixed by the plan.** The property set of an event is exactly the set the plan declares, with the declared types. Keys are never generated from data (no key per product, per error message, or per user), and a property that arrives with the wrong type is a violation, not a variant.
5. **AN-025 — Name the outcome, not the widget.** Events record what the user accomplished ("Order Completed", "Subscription Started"), not which control they touched ("Checkout Button Clicked"). Outcome names survive redesigns and count successes; widget names count clicks that may have failed.
6. **AN-026 — No personal data in events.** Event names and property values carry no emails, personal names, phone numbers, or free text that can contain personal data. People are referenced by opaque IDs only. Consent and retention rules themselves are D14's; this rule is their enforcement point in the event stream.
7. **AN-027 — Every event has an owner and a question.** An event with no named owner, or whose plan entry cannot state the decision it informs, is not added. Prefer fewer, well-shaped events with rich properties over an event per button.
8. **AN-028 — Emit only through the wrapper.** Application code emits events through one typed wrapper (generated from the plan or checked against it), never through raw platform calls scattered across the codebase. The wrapper is the single point where names and property shapes can be enforced.
9. **AN-029 — Validate in the debug view before release.** Before a release ships, the primary flows are run in a test session and every expected event is confirmed in the platform's debug or realtime view: correct name, correct properties, correct types, fired once. An event first seen in production data was never validated.
10. **AN-030 — No firing before consent state.** Non-essential events do not fire until the visitor's consent state is known, and never fire when consent is denied. Consent state is recorded with the session so reports can state their coverage honestly (rules: D14 cookie-consent, privacy-laws).
11. **AN-031 — Renaming is a breaking change.** Renaming or removing an event ships with a plan version bump, a migration note naming the reports and funnels it affects, and a deprecation window in which the change is announced. A silent rename splits history into two incomparable series.
12. **AN-032 — Sweep production for violations.** On a fixed cadence, recent production events are checked against the plan: any emitted name absent from the plan, and any property shape violating it, is filed as a defect with an owner. A non-empty violation list is a bug in the pipeline, not a curiosity.

## BAN list

- **BAN-AN-011 — Event-name variants.** Banned: two or more live spellings or casings of one event ("Signup Completed", "SignUp Completed", "signed_up"). Defeats: DET-CON-017. Bad: a redesign ships `signed_up` alongside the existing "Signup Completed", and the activation funnel silently halves. Instead: one canonical name per event, emitted only through the AN-028 wrapper and checked by the AN-022 lint. Severity: BLOCK.
- **BAN-AN-012 — Personal data in event properties.** Banned: property values carrying emails, names, or free-text user input (e.g. `user_email: "a@b.com"`, `search_query` holding typed personal text). Defeats: DET-CON-003. Bad: a "Support Requested" event ships the user's typed message, email included, into the analytics store. Instead: reference the person by opaque ID and keep content in the system of record; properties carry IDs, categories, and counts only. Severity: BLOCK.
- **BAN-AN-013 — Validation that never gates.** Banned: a tracking-plan lint or schema check that runs as an advisory warning while merges and releases proceed on failure. Defeats: DET-INF-002. Bad: CI prints "3 unplanned events" on every build for a quarter; nobody reads it, and the taxonomy rots anyway. Instead: the lint is a required check — an unplanned event or wrong-typed property fails the build (G-AN-011). Severity: BLOCK.
- **BAN-AN-014 — Silent renames and removals.** Banned: renaming, repurposing, or deleting an event in code without a plan version bump and migration note. Defeats: DET-CON-015. Bad: "Trial Started" is repurposed to fire at payment instead of signup; the dashboard contradicts last quarter's report and nobody can say when it changed. Instead: follow AN-031 — bump the plan version, write the migration note, announce the deprecation window. Severity: BLOCK.

## Gates

- **G-AN-011 — Tracking-plan lint.** Verifies: AN-021, AN-022, AN-024. Check: automated — CI runs the plan validator over the build's emitted-event manifest (or the wrapper's schema) against `tracking-plan` in the repo, e.g. `node scripts/validate-tracking-plan.js --plan analytics/tracking-plan.json --src src/`; any event absent from the plan, any name breaking the casing convention, and any property with a wrong type exits non-zero. Pass: validator exits 0 as a required status check. Fail: block the merge. Recorded in: progress.md.
- **G-AN-012 — Debug-view validation.** Verifies: AN-025, AN-029. Check: manual with tooling — before release, run the primary conversion and retention flows in a test session with the platform's debug/realtime view open; confirm each planned event appears once, with the planned name, properties, and types. Pass: every expected event observed exactly as planned. Fail: block the release; fix instrumentation and re-run. Recorded in: progress.md.
- **G-AN-013 — Plan-diff review.** Verifies: AN-031. Check: automated plus review — a CI script diffs `tracking-plan` on the change; any removed or renamed event without a plan version bump and a migration-note file in the same change exits non-zero. Pass: no unplanned removals; every breaking change carries its bump and note. Fail: block the merge. Recorded in: progress.md.
- **G-AN-014 — Production violation sweep.** Verifies: AN-023, AN-026, AN-032. Check: automated — a scheduled job lists distinct event names and property keys received in the last 7 days and diffs them against the plan, e.g. `node scripts/audit-live-events.js --plan analytics/tracking-plan.json --days 7`; output is the violation list. Pass: the list is empty. Fail: file each violation as a defect with an owner before the next release. Recorded in: progress.md.

## Anti-patterns

- **The pageview-only strategy.** The snippet is installed, automatic pageviews are counted, and the team calls it tracking. Catch it: ask which business question the instrumentation answers; if the answer is a pageview chart, no planned event exists yet (AN-021).
- **Event-per-button sprawl.** Every control gets its own event, so the taxonomy has hundreds of names and no outcomes. Catch it: count events that name a widget instead of an accomplishment (AN-025) and fold them into one outcome event with a property.
- **Instrumenting to the dashboard.** Events are added because a chart someone wants needs a field, with no plan entry, owner, or question. Catch it: any event whose plan entry cannot state its decision is removed or justified (AN-027).
- **Fixing it in the report.** Analysts merge variants with report-side aliases and filters instead of fixing emission. Catch it: an alias table in a reporting tool is a symptom; the fix belongs in the wrapper and the plan, and the sweep (G-AN-014) will keep finding the variants until it lands.

## Examples

- [Example 1 — One signup, three event names](examples/example-1.md) — violates/corrects AN-022.
- [Example 2 — The product name inside the event name](examples/example-2.md) — violates/corrects AN-023.
- [Example 3 — The email address riding in a property](examples/example-3.md) — violates/corrects AN-026.

## Recall anchors

- Plan first, code second — no event exists outside the plan.
- One event, one spelling, forever; a rename is a breaking change.
- Values go in properties; names stay fixed.
- Name the outcome, not the widget.
- If the lint cannot fail the build, it is decoration.

## Checklist

- [ ] Every emitted event is in the tracking plan with properties, types, owner, and question (AN-021, AN-027).
- [ ] All names follow the single casing convention; no variants exist (AN-022).
- [ ] No event name contains a dynamic value; no property key is generated from data (AN-023, AN-024).
- [ ] No personal data appears in any event name or property value (AN-026).
- [ ] All emission goes through the typed wrapper (AN-028).
- [ ] Primary flows were run and every event confirmed in the debug view (G-AN-012).
- [ ] The plan lint is a required, passing CI check (G-AN-011).
- [ ] Any rename or removal carries a version bump and migration note (AN-031, G-AN-013).
