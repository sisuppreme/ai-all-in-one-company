# ui-states

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Nielsen Norman Group, Designing Empty States in Complex Applications — https://www.nngroup.com/articles/empty-state-interface-design/ ; W3C WCAG technique C39, Using the CSS reduce-motion query — https://www.w3.org/WAI/WCAG22/Techniques/css/C39.html
- **Depends on:** component-library, data-fetching
- **Feeds into:** forms, client-routing, frontend-core

## When to use / Do NOT use

- **Use when:** building or reviewing any view that depends on data or an action's outcome — lists, dashboards, search results, submissions — and specifying its loading, empty, error, partial, and success behavior.
- **Do NOT use when:** the state belongs to a single component's visual variants (hover, focus, disabled styling) — that is component-library. Do not invent states for purely static content; a page with no data dependency has no loading state to design.

## Rules

1. **FE-161 — The state matrix comes first.** Before a data-dependent view is built, its states are specified in a matrix: loading, empty (first use / no results / cleared), error, partial, and success. A view built without the matrix is incomplete (DET-VIS-032).
2. **FE-162 — No silently blank containers.** Every view renders a designed state for every condition it can be in; an empty region where content failed or has not arrived is a defect (DET-VIS-032).
3. **FE-163 — Errors speak plainly.** Error copy names what happened and the next step, in the user's language. Raw error codes, stack text, and "No data" as the sole copy of any state are forbidden.
4. **FE-164 — Actions end visibly.** Every mutating action ends in a visible success confirmation or an error state with a retry path. Silent completion — the user guessing whether it worked — is a defect.
5. **FE-165 — Hover never gates.** Hover may enhance, but every hover reveal or action has a tap/click and a keyboard-focus equivalent (DET-VIS-042).
6. **FE-166 — Skeletons match the final layout.** Loading skeletons reproduce the shape of the content they precede, so the loading-to-loaded transition does not reflow the page (CLS budget, frontend-core).
7. **FE-167 — Empty states explain and offer.** An empty state says what belongs here and offers the next action; first-use, no-results, and cleared/filtered empties are different states with different copy and actions.
8. **FE-168 — Spinners are for short, bounded waits.** A bare spinner is used only where the wait is brief and the result's shape is unknown; content loads use skeletons (FE-166).
9. **FE-169 — Indicators report reality.** Progress bars, sync badges, and "saved" indicators reflect the actual operation state; a timer-driven or assumed success indicator is a fake state (DET-FAKE-022).
10. **FE-170 — State changes survive reduced motion.** Under `prefers-reduced-motion`, state changes remain fully legible without movement — no information is carried by animation alone (WCPM rule CR-09, cited per docs/WCPM_MAPPING.md §2.2).
11. **FE-171 — Inherited state law.** The WCPM §8 component-and-state rules and the BEH parameter family apply as cited in docs/WCPM_MAPPING.md §2.2 and §2.4, and state work is designed to pass the G-EXP gate family.

**Architecture must never leak into the UI.** States describe the user's situation, never the system's. Loading, empty, and error states must be written in user-facing concepts — what happened for the user and what they can do next — never in system terms: no endpoint names, no status codes as the message, no schema or field names, no mention of which service, module, or store failed. A failed save says the work is safe and how to retry; it never names the machinery that failed.

## BAN list

- **BAN-FE-081 — Blank container state.** Banned: a view that renders an empty region when data is empty, loading, or failed. Defeats: DET-VIS-032. Bad: a new account's dashboard is a white page with a sidebar because the list is empty. Instead: the designed empty state for that condition (FE-167). Severity: BLOCK.
- **BAN-FE-082 — Hover-only reveal.** Banned: content or actions reachable only by hovering. Defeats: DET-VIS-042. Bad: a card's Edit and Delete buttons appear only on mouse hover, unreachable on touch and by keyboard. Instead: always-visible actions, or a tap/focus-triggered menu (FE-165). Severity: BLOCK.
- **BAN-FE-083 — Raw error text to users.** Banned: showing error codes, exception text, or stack fragments in the UI. Defeats: DET-VIS-032. Bad: the page prints "Error 500: NullReference at OrdersController.cs:118". Instead: plain-language copy naming the problem and the retry step (FE-163), with the technical detail logged, not displayed. Severity: BLOCK.
- **BAN-FE-084 — Fake progress or sync state.** Banned: progress or "synced/saved" indicators driven by timers or optimism rather than the operation's real state. Defeats: DET-FAKE-022. Bad: an upload bar animates to 100% in two seconds while the request is still running, then shows "Saved". Instead: bind the indicator to the request lifecycle, including its failure state (FE-169). Severity: BLOCK.
- **BAN-FE-085 — One generic spinner for every wait.** Banned: a centered spinner as the loading state for every view regardless of duration or layout. Defeats: DET-VIS-032. Bad: a full dashboard, a table, and a settings form all load behind the identical spinner for several seconds. Instead: layout-matched skeletons for content loads (FE-166); spinners only for short bounded waits (FE-168). Severity: WARN.

## Gates

- **G-FE-081 — Four-state screenshot pass.** Verifies: FE-161, FE-162, FE-163. Check: manual — for each main view, capture four states: throttled network (loading), empty account (empty), blocked API request (error), completed action (success). Pass: all four states are designed and legible in every view. Fail: block shipment. Recorded in: progress.md.
- **G-FE-082 — Mocked-state render tests.** Verifies: FE-162, FE-167. Check: automated — Playwright tests mock empty and error API responses for the main views and assert the corresponding state components render with their next-action controls. Pass: all mocked states render as designed. Fail: block shipment. Recorded in: progress.md.
- **G-FE-083 — Hover-parity check.** Verifies: FE-165. Check: manual — walk every hover reveal in the interface using only touch tap and keyboard focus; confirm each has a working equivalent. Pass: zero hover-only paths. Fail: block shipment. Recorded in: progress.md.
- **G-FE-084 — Indicator honesty test.** Verifies: FE-169. Check: automated — a test kills the network mid-operation (upload, save, sync) and asserts the indicator shows the failure state, never success. Pass: the indicator tracks the real outcome. Fail: block shipment. Recorded in: progress.md.

## Intelligence — decisions & gates

> **Judgment layer.** These decisions apply the judgment layer above this skill — `skills/frontend/design-intelligence/SKILL.md` and the theme library (`skills/frontend/theme-library/`). Settle the theme's art direction there first, then decide here inside it; where a decision below and a rule above disagree, the rule above wins.

### Decision rules — designing states

| Decision | Read the situation | Decide |
|---|---|---|
| Loading treatment | The wait's shape and length | Known layout and a wait beyond ~300ms: skeleton (FE-166). Unknown shape or a short bounded wait: spinner (FE-168). Cached or instant: no indicator at all. |
| Empty-state investment | Whose moment it is | First-use empties are onboarding surfaces — invest in explanation and a first action. No-results empties are recovery surfaces — help the user change the query. Cleared empties are confirmations — keep them light (FE-167). |
| Error placement | How the user recovers | Field errors sit at the field; a failed view region is replaced by its error state with retry; a global outage takes the page. Toasts carry only non-critical notices, never the sole record of a failure. |
| Optimism | Whether failure is rare and the action reversible | Optimistic UI only where undo exists and failure is unlikely. Payments, permissions, and destructive actions show real pending, then real confirmation (FE-169). |
| Partial data | How critical each region is | Render what arrived; give the missing region its own visible gap state. Never hold the whole view hostage to its slowest widget. |
| Success visibility | The action's weight | Irreversible or destructive: an explicit confirmation state. Trivial and reversible: a lightweight inline confirmation is enough (FE-164). |
| Retry design | The failure's cause | Transient (network, timeout): automatic retry with backoff plus a manual retry. User-caused (validation): fix in place — a retry button for a form error is a dead end. |

### Self-check gate

- **G-FE-085 — Pre-ship intelligence self-check (states).** Verifies: FE-161, FE-162, FE-164, FE-166, FE-167, FE-169 as judgment, not just compliance. Check: manual — the builder scores each item pass/fail on the shipped views: (1) ★ a state matrix exists for every data-dependent view, and every cell of it has a designed render; (2) ★ kill the network mid-action: the interface lands on an error state with a retry path — never a spinner that outlives the test; (3) first-use, no-results, and cleared empties each carry their own copy and next action; (4) every mutation ends in a visible confirmation or an error — none end in silence; (5) skeletons match the layout that replaces them, with no visible reflow on load; (6) every hover reveal has a working touch and keyboard equivalent. Pass: both ★ items pass and at least 5 of 6 overall. Fail: fix, or log a written exception, before shipping. Recorded in: progress.md.

### Anti-pattern table — symptom → cause → fix

| Symptom | Cause | Fix |
|---|---|---|
| Missing empty state — a new user's dashboard is a blank page with a sidebar | The state matrix was skipped; only the success path was designed | Specify the matrix before building (FE-161); design each empty kind with copy and a next action (FE-167). |
| Missing error state — a failed fetch leaves a spinner turning forever | No timeout and no error branch were wired to the request | Every request gets an error state that names the problem and offers the next step (FE-162, FE-163). |
| Loading dead-end — the skeleton renders, the content never swaps in, and nothing ever fails visibly | The loading indicator is decorative, not bound to the request lifecycle | Bind indicators to real operation state, including failure (FE-169); test by killing the network (G-FE-084). |
| Toast-only failure — the error vanishes in four seconds and cannot be acted on | Errors were treated as notifications instead of states | Keep the failure as a persistent state with retry in place; a toast may supplement it, never replace it. |
| One empty for all empties — "No results found" greets a first-time user who has no data yet | First-use, no-results, and cleared conditions were conflated into one component | Treat them as three states with different copy and different actions (FE-167). |
| The skeleton lies — content arrives in a different shape and the page jumps | A generic skeleton was reused across unlike views | Mirror each view's real layout in its skeleton (FE-166). |
| Silent success — the save completes, nothing confirms, the user saves again and duplicates work | The mutation has no designed end state | Every action ends visibly: confirmation or error with retry (FE-164). |
| Fake "Saved" — the badge claims success while the request is still running, or has failed | The indicator is driven by a timer or by optimism | Drive it from the request outcome only, and assert its failure state under test (FE-169, G-FE-084). |

## Anti-patterns

- **Toast-only errors.** Failures appear as a toast that vanishes in four seconds, leaving no state and no retry. Catch it: if dismissing the toast erases the only record of the error, the state was never designed.
- **Empty state as dead end.** "Nothing here yet" with no explanation and no action. Catch it: an empty state with zero controls is a dead end, whatever its illustration.
- **Loading forever.** A spinner with no timeout and no error path, so a hung request hangs the interface. Catch it: block the API in testing — if the spinner outlives the test, there is no error state.
- **Success by silence.** The action completes and nothing changes on screen. Catch it: perform each mutation and watch for a confirmation; if you have to check another page to know, it failed FE-164.

## Examples

- [Example 1 — Blank list replaced by a designed empty state](examples/example-1.md) — corrects FE-167.
- [Example 2 — Raw error replaced by plain language with retry](examples/example-2.md) — corrects FE-163.
- [Example 3 — Hover-only card actions made reachable](examples/example-3.md) — corrects FE-165.

## Recall anchors

- Every view, every condition, a designed state.
- Errors name the problem and the next step.
- Hover enhances; it never gates.
- Indicators report reality or they are removed.
- Actions end visibly — never in silence.

## Checklist

- [ ] A state matrix exists for every data-dependent view (FE-161).
- [ ] Four-state screenshot pass is complete for all main views (G-FE-081).
- [ ] Mocked empty and error states render as designed (G-FE-082).
- [ ] No hover-only content or actions remain (G-FE-083).
- [ ] Progress and sync indicators track real outcomes under failure (G-FE-084).
- [ ] Empty states explain what belongs and offer the next action (FE-167).
- [ ] No raw error text reaches the UI (BAN-FE-083).
