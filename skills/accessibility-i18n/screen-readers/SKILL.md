# screen-readers

## Metadata

- **Owner department:** D13 Accessibility & i18n (AC)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** ARIA Authoring Practices Guide (APG), W3C — https://www.w3.org/WAI/ARIA/apg/ ; WCAG 2.2, W3C — https://www.w3.org/TR/WCAG22/
- **Depends on:** wcag (name/role/value and status-message criteria), accessibility-audit (its smoke-test pass consumes this skill's matrix)
- **Feeds into:** accessibility-testing, keyboard-accessibility, inclusive-copy

## When to use / Do NOT use

- **Use when:** Building or reviewing anything a screen-reader user must operate or understand — forms, custom widgets, dynamic updates, data tables, navigation — and when running the screen-reader test pass for a release.
- **Do NOT use when:** The defect is purely visual (contrast, focus visibility — wcag / keyboard-accessibility), the question is which law applies (accessibility-law), or the work is a full conformance evaluation (accessibility-audit runs this skill's test matrix as one of its passes).

## Rules

1. **AC-041 — Native semantics first; ARIA is the last resort.** Use the native HTML element for every control and structure (`<button>`, `<nav>`, `<table>`, `<label>`). Add ARIA only where no native element expresses the widget, per the first rule of ARIA use: no ARIA is better than bad ARIA. A role bolted onto a `<div>` is a defect until the full APG pattern (AC-046) is implemented.
2. **AC-042 — Every interactive element has an accessible name that matches its visible label.** The computed accessible name must contain the visible text label (WCAG 2.5.3 Label in Name), so speech-input and screen-reader users refer to the same control by the same words. Icon-only controls get a name from `aria-label` or visually hidden text that states the action ("Close dialog", not "X").
3. **AC-043 — Headings are a navigation outline, not font sizing.** Headings nest in logical order without skipped levels, each heading text describes the section it opens, and visual size is set with CSS. Screen-reader users navigate by the heading list; an outline that reads as nonsense is a failed page even if it looks right.
4. **AC-044 — Landmarks are few and labeled when repeated.** One `<main>`, one `<nav>` per navigation region; when a landmark type repeats (two `<nav>`s, multiple `<section>`s with `aria-label`), each instance carries a distinct accessible name so the landmark list is usable.
5. **AC-045 — Images: real alt text or empty alt, never a file name.** Informative images get alt text conveying the information the image carries in context; purely decorative images get `alt=""` so they are skipped. File names ("IMG_2043.jpg"), "image", and redundant phrases ("image of") fail this rule.
6. **AC-046 — Custom widgets implement the APG pattern exactly or are replaced.** A custom tabs, menu, combobox, or grid ships with the APG roles, states, properties, and full keyboard model for that pattern — all of it, not the visible half. If the team cannot implement the whole pattern, the widget is rebuilt on native elements.
7. **AC-047 — Dynamic changes are announced by live regions, politely by default.** Status changes (save confirmations, cart totals, step changes, toasts) go through an `aria-live="polite"` region (WCAG 4.1.3); `assertive` is reserved for errors that block the current task. Announcements never move focus — the user hears the change and stays where they are.
8. **AC-048 — Reading order and focus order match the visual order.** DOM order is the single source of sequence: content reads in the same order it is seen, and no CSS (`order`, absolute positioning, grid placement) reorders meaning visually without the DOM agreeing. Multi-column visual layouts built from a scrambled DOM fail this rule.
9. **AC-049 — Data tables use real table semantics with header association.** Data tables are `<table>` markup with `<th>` header cells and `scope` (or `headers`/`id` for complex tables), so a cell is announced with its row and column headers. Layout tables and div-grids presenting tabular data are prohibited; a genuine grid widget follows the APG grid pattern instead.
10. **AC-050 — Language is declared so pronunciation is right.** The document carries a correct BCP 47 `lang`, and any in-page language change is wrapped with its own `lang` (WCAG 3.1.1, 3.1.2). A screen reader pronouncing French text with English rules is a markup defect, not a user problem.
11. **AC-051 — Test in a fixed screen-reader matrix, navigating the way users navigate.** The project fixes its matrix in writing (department default: NVDA + Chrome and JAWS + Chrome on Windows, VoiceOver + Safari on macOS and iOS, TalkBack + Chrome on Android) and records the combinations and date per journey. Testers move by headings, landmarks, link lists, and form-control lists — not only by linear reading — because that is how screen-reader users actually navigate. Untested combinations are stated residual risk, never implied coverage.
12. **AC-052 — Form state is programmatic, not visual.** Required fields expose their required state, invalid fields set `aria-invalid="true"`, and each field's error text and instructions are associated with `aria-describedby`, so the error is announced with the field when the user reaches it — not painted red somewhere on the page.

## BAN list

- **BAN-AC-021 — Clickable divs and spans as controls.** Banned: `<div>`/`<span>` elements with click handlers acting as buttons, links, or tabs, with no role, accessible name, or keyboard path. Defeats: DET-NONE — no DET parameter names this signal; pattern owned by this skill. Bad: `<div class="tab" onclick="showPanel(2)">Billing</div>` — focus never reaches it and a screen reader announces nothing. Instead: use a native `<button>` (or the full APG tabs pattern with `role="tablist"`, arrow-key model, and `aria-selected`). Severity: BLOCK.
- **BAN-AC-022 — Placeholder text as the only label.** Banned: form fields labeled only by placeholder text that vanishes on typing. Defeats: DET-UX-022. Bad: `<input placeholder="Email address">` with no `<label>` — the field announces unreliably and is unidentifiable once filled. Instead: give every field a persistent visible `<label>` (or `aria-label` where a visible label is genuinely impossible) and let the placeholder show a format example only. Severity: BLOCK.
- **BAN-AC-023 — Silent dynamic changes.** Banned: content that changes on screen — success toasts, totals, step indicators, filtered results — with no live-region announcement, so the change exists only visually. Defeats: DET-UX-011. Bad: clicking "Save" shows a green toast for three seconds; a screen-reader user hears nothing and cannot tell the save happened. Instead: route the confirmation through an `aria-live="polite"` status region that announces "Profile saved" without moving focus (AC-047). Severity: BLOCK.
- **BAN-AC-024 — Focus dropped to the document top.** Banned: closing a dialog, submitting a form, or changing views in a way that resets focus and the reading position to the top of the document (or nowhere). Defeats: DET-UX-017. Bad: after dismissing a settings dialog, the screen-reader user is returned to the page header and must re-navigate to where they were. Instead: return focus to the control that opened the dialog, and on view change move focus to the new view's heading (AC-048). Severity: BLOCK.
- **BAN-AC-025 — Errors announced visually only.** Banned: validation errors shown as red borders or a distant error banner while the field itself carries no programmatic error state or associated message. Defeats: DET-UX-005. Bad: a banner at the top reads "2 errors" and the card-number field is outlined in red; at the field, the screen reader announces only "Card number, edit text". Instead: set `aria-invalid="true"` on the field and associate the specific error text with `aria-describedby`, with a polite/assertive announcement per AC-047 and AC-052. Severity: BLOCK.

## Gates

- **G-AC-021 — Automated name/role scan in CI.** Verifies: AC-041, AC-042, AC-045, AC-052. Check: run `npx @axe-core/cli <each key URL> --tags wcag2a,wcag2aa,wcag22aa` in CI (or the project's axe-core job) and fail the build on `button-name`, `link-name`, `label`, `image-alt`, and `aria-required-attr` violations. Pass: zero violations of those rules on every key template. Fail: block merge. Recorded in: progress.md.
- **G-AC-022 — Accessibility-tree name/role assertion.** Verifies: AC-042, AC-044, AC-049. Check: scripted pass over the rendered accessibility tree of each key page (e.g. Playwright's accessibility snapshot): assert every interactive node has a non-empty accessible name and a valid role, repeated landmarks have distinct names, and every data-table cell resolves to at least one header. Pass: zero unnamed interactive nodes, zero unlabeled repeated landmarks, zero headerless data cells. Fail: block release. Recorded in: progress.md.
- **G-AC-023 — Screen-reader smoke pass on primary journeys.** Verifies: AC-043, AC-048, AC-051. Check: manual pass — execute each primary journey in at least one desktop (NVDA + Chrome) and one mobile (VoiceOver + Safari or TalkBack + Chrome) combination from the project's fixed matrix, navigating by headings, landmarks, and form controls; log pass/fail per journey with the AT/browser versions and date. Pass: every primary journey completable end to end in both combinations, with names, roles, and order as designed. Fail: block release. Recorded in: progress.md.
- **G-AC-024 — Live-region announcement test.** Verifies: AC-047, AC-052. Check: with a screen reader running, trigger each dynamic change in the primary journeys (save, add-to-cart, step advance, a blocking validation error, a failed submit) and record what is announced and where focus sits afterward. Pass: every change is announced by the correct live region and focus never moves on a status announcement. Fail: block release. Recorded in: progress.md.
- **G-AC-025 — Heading and landmark outline review.** Verifies: AC-043, AC-044. Check: extract the heading outline and landmark list for each key template (headings-map tool or the screen reader's headings/landmarks dialogs during G-AC-023) and read them as a standalone table of contents. Pass: the outline alone describes the page's structure accurately, with no skipped levels and no heading whose text is styling noise ("Welcome!", "Section 2"). Fail: block release. Recorded in: progress.md.

## Anti-patterns

- **ARIA wallpaper.** Sprinkling roles and labels over broken markup — `role="button"` on a div with no keyboard handler, `aria-label` on a non-interactive wrapper — until the code *mentions* accessibility everywhere and provides it nowhere. Catch it by asking, for every ARIA attribute, what a screen reader does differently because it exists (AC-041).
- **Linear-read testing only.** Testing by tabbing or reading top to bottom once, then declaring the page screen-reader friendly — while the heading list is garbage and the link list is forty "click here"s. Catch it by navigating one journey using only the headings dialog and the form-controls list (AC-051).
- **One-combination claim.** Testing in NVDA alone and writing "screen-reader accessible" in the release notes. Combinations differ, especially on custom widgets and live regions. Catch it by checking the claim against the project's fixed matrix and its recorded test dates (AC-051).
- **Visually hidden text dumps.** Stuffing paragraphs of screen-reader-only text onto a page to compensate for visible copy that makes no sense — doubling maintenance and announcing a different product than sighted users see. Catch it by comparing the announced content against the visible content: they must say the same thing (inclusive-copy owns the copy fix).

## Examples

- [Example 1 — Div tab bar vs. native buttons with names](examples/example-1.md) — violates/corrects AC-041.
- [Example 2 — Silent save toast vs. polite live region](examples/example-2.md) — violates/corrects AC-047.
- [Example 3 — Styled text vs. a real heading outline](examples/example-3.md) — violates/corrects AC-043.

## Recall anchors

- Native element first; ARIA only where HTML runs out.
- No name, no control — if it can't be announced, it doesn't exist.
- Headings are the table of contents; write them like one.
- Changes speak politely; only blocking errors interrupt.
- DOM order is reading order — never let CSS tell a different story.

## Checklist

- [ ] Every interactive element has an accessible name containing its visible label (AC-042).
- [ ] No clickable div/span controls remain; custom widgets implement the full APG pattern (AC-041, AC-046).
- [ ] Heading outline reads as an accurate table of contents with no skipped levels (AC-043, G-AC-025).
- [ ] All informative images have real alt text; decorative images have `alt=""` (AC-045).
- [ ] Every dynamic change is announced by a live region without moving focus (AC-047, G-AC-024).
- [ ] Form errors are programmatic: `aria-invalid` plus `aria-describedby` error text (AC-052).
- [ ] Primary journeys passed in one desktop and one mobile matrix combination, versions and date recorded (AC-051, G-AC-023).
