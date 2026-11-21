# user-onboarding

## Metadata

- **Owner department:** D18 Customer Experience (CX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Appcues, "Build effective Checklists" — https://appcues.helpjuice.com/checklists/checklist-best-practices
- **Depends on:** activation-metrics
- **Feeds into:** activation-metrics, trial-conversion, help-center

## When to use / Do NOT use

- **Use when:** designing or changing any first-run experience — welcome step, setup checklist, product tour, tooltips, or onboarding messages — for a new user, role, or plan.
- **Do NOT use when:** teaching an existing user a newly shipped feature in context (that is contextual help, not onboarding), or when the product has no defined activation event yet — define it with activation-metrics first.

## Rules

1. **CX-061 — Activation first.** Onboarding is designed backwards from the activation event defined with activation-metrics. Every step exists because it moves a new user toward that event; a step that does not is removed.
2. **CX-062 — One core action, stated budget.** The flow's goal is the single core value action, and the maximum step count to reach it is written in the onboarding spec. The first-session path reaches it with no optional detour in between.
3. **CX-063 — Six items or fewer.** The checklist holds at most six items. Anything non-essential is cut or moved to contextual help that appears later, inside the doing.
4. **CX-064 — Event-bound completion.** A checklist item completes only when its real product event fires. Page views, elapsed time, and "Next" or "Got it" clicks never complete an item.
5. **CX-065 — Named event binding.** Every checklist item names the instrumented event it binds to, exactly as named in the tracking plan. An item with no named event is not shipped.
6. **CX-066 — Real data only.** Steps are completed with the user's own real data. Sample content is offered only as a clearly labeled, optional starting point that one action removes entirely — never pre-loaded records the user must delete to begin.
7. **CX-067 — Skippable and permanently dismissible.** Every step can be skipped, and the checklist and any tour can be dismissed permanently. Dismissal is stored on the account, so it holds across sessions and devices.
8. **CX-068 — Resume, never restart.** A returning user resumes at their recorded checklist state. Completed steps never replay, and a dismissed tour never refires on a later login.
9. **CX-069 — Plan- and role-scoped.** Steps teach only features the user's plan and role can actually use. Locked, unentitled, or role-invisible features never appear in the flow.
10. **CX-070 — Honest progress.** Progress indicators show real completed items over the real total. No progress bar advances on time or clicks, and onboarding copy carries no user counts, logos, or testimonials that are not real, current, and sourced.
11. **CX-071 — No forced gates.** Reaching the core action never requires inviting teammates, connecting an unrelated account, or completing profile fields the core action does not need. Such steps are optional and come after the core action, if at all.
12. **CX-072 — Measured per step.** Entry, completion, skip, and abandonment are instrumented per step. The flow is changed from per-step drop-off evidence — the worst step is fixed or removed — never redesigned on opinion alone.

## BAN list

- **BAN-CX-031 — The undismissable tour.** Banned: a modal tour that fires on every login and cannot be dismissed permanently. Defeats: DET-UX-028. Bad: a fourteen-step modal tour replays at every login and teaches features the user's plan does not include. Instead: a short checklist bound to real events, dismissible once and forever (CX-063, CX-067, CX-068). Severity: BLOCK.
- **BAN-CX-032 — The dead-end welcome.** Banned: onboarding that ends on a blank empty state with no visible path to the core action. Defeats: DET-UX-009. Bad: signup completes onto an empty dashboard — no data, no guidance, no first action offered. Instead: the empty state names the core action and starts it in one click (CX-062). Severity: BLOCK.
- **BAN-CX-033 — The placeholder workspace.** Banned: pre-loading dummy projects, records, or teammates presented as the user's own data. Defeats: DET-UX-002. Bad: the new workspace arrives filled with "Sample Project — delete me" entries the user must clear before real work fits. Instead: start empty with a guided first action, or offer labeled sample data that one action removes (CX-066). Severity: BLOCK.
- **BAN-CX-034 — Fake completion.** Banned: checklist items or progress that mark done on a page view, a timer, or a "Next" click rather than the real event. Defeats: DET-UX-011. Bad: "Create your first report" ticks because the user clicked through the tour slide about reports. Instead: the item ticks only when the report-created event fires (CX-064, CX-065). Severity: BLOCK.
- **BAN-CX-035 — The forced invite gate.** Banned: blocking the core action until the user invites teammates or completes unrelated requirements. Defeats: DET-UX-013. Bad: step three of four demands two teammate email addresses before the user can create anything. Instead: core action first; the invite is an optional step afterwards (CX-071). Severity: BLOCK.

## Gates

- **G-CX-031 — Fresh-account walkthrough.** Verifies: CX-061, CX-062, CX-064, CX-068. Check: automated — an end-to-end test creates a fresh account, onboards using only in-product guidance, and asserts the core value action is reached within the step budget in the spec, each checklist item ticks exactly when its named event fires (asserted in analytics), and a second login restarts nothing. Shape-adapted forms: where the product has no product analytics, each checklist tick is asserted against the event or state record the product does keep (server log, state transition, persisted record) instead of an analytics event; where joining needs no account (e.g. a name-only join), the walkthrough starts from a fresh first visit, "fresh account" means a first-time identity, and "a second login restarts nothing" means a return visit with the same identity restarts nothing. Pass: all assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-CX-032 — Event-binding audit.** Verifies: CX-065. Check: automated — a script diffs the checklist definition against the tracking plan; every item must name an event that exists and fires in a test session. Pass: 100% of items bound. Fail: block shipment until the item is bound or removed. Recorded in: progress.md.
- **G-CX-033 — Dismissal persistence test.** Verifies: CX-067, CX-068. Check: automated — dismiss the checklist and tour, log out and back in, then repeat under a second session; assert neither refires and recorded progress is unchanged. Pass: no refire, state intact. Fail: block shipment. Recorded in: progress.md.
- **G-CX-034 — Plan-scope audit.** Verifies: CX-069. Check: manual — walk the full flow on the lowest plan and under each role; list every feature a step references and confirm that plan and role can use it. Pass: zero out-of-scope references. Fail: remove or gate the step before release. Recorded in: progress.md.
- **G-CX-035 — Drop-off review.** Verifies: CX-072. Check: manual — on the review cadence, read the per-step funnel (entered, completed, skipped, abandoned); the highest drop-off step carries a fix, a removal, or a recorded decision with a reason. Pass: review held and worst step dispositioned. Fail: onboarding changes freeze until the review happens. Recorded in: progress.md.

## Anti-patterns

- **The feature parade.** The tour walks through every feature the team is proud of instead of the shortest path to the core action. Catch it: if a step's honest justification is "users should know this exists," it belongs in contextual help, not onboarding.
- **Day-based nagging.** Follow-up messages fire on elapsed time ("Day 3: finish your setup!") regardless of checklist state, emailing users who already finished. Catch it: every onboarding message branches on actual checklist state; a message that cannot name the state it targets is not sent.
- **Cosmetic personas.** Separate flows per persona that differ in wording and imagery but walk identical steps. Catch it: diff the step lists — if they match, merge the flows and keep the copy conditional.
- **Vanity completion.** The team celebrates a rising checklist completion rate while the activation rate is flat. Catch it: report the two rates side by side; completion is a means metric, activation is the outcome.

## Examples

- [Example 1 — Binding a checklist item to its real event](examples/example-1.md) — corrects CX-064.
- [Example 2 — Replacing a placeholder workspace with a real first action](examples/example-2.md) — corrects CX-066.
- [Example 3 — Removing a forced invite gate](examples/example-3.md) — corrects CX-071.

## Recall anchors

- Onboarding exists to reach one event: activation.
- An item is done when its event fires — never when it is viewed.
- Six items or fewer; everything else is contextual help.
- Dismissed means dismissed forever; returning means resuming.
- No dummy data, no fake progress, no forced invites.

## Checklist

- [ ] The activation event is defined and every step traces to it (CX-061).
- [ ] The step budget to the core action is written in the spec and met in the walkthrough (G-CX-031).
- [ ] Checklist holds six or fewer items (CX-063).
- [ ] Every item names an instrumented event and ticks only when it fires (G-CX-032).
- [ ] No dummy data ships; any sample content is labeled and removable in one action (CX-066).
- [ ] Dismissal persists across sessions and the flow resumes, never restarts (G-CX-033).
- [ ] No step references a feature outside the user's plan or role (G-CX-034).
- [ ] Per-step drop-off is instrumented and the worst step has a disposition (G-CX-035).
