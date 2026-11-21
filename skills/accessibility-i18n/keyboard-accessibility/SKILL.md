# keyboard-accessibility

## Metadata

- **Owner department:** D13 Accessibility & i18n (AC)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** ARIA Authoring Practices Guide (APG), W3C — https://www.w3.org/WAI/ARIA/apg/ ; WCAG 2.2, W3C — https://www.w3.org/TR/WCAG22/
- **Depends on:** wcag (fixes the WCAG 2.2 AA target this skill builds to)
- **Feeds into:** accessibility-audit, accessibility-testing, screen-readers

## When to use / Do NOT use

- **Use when:** Building or fixing any interactive UI — navigation, forms, dialogs, menus, custom widgets, drag interactions — so every function is reachable and operable with keyboard alone, in a visible, logical order.
- **Do NOT use when:** Running a scoped conformance evaluation (accessibility-audit finds and records; this skill fixes), testing with a screen reader (screen-readers), or deciding pointer target sizes (wcag / the design system — this skill covers keyboard operation only).

## Rules

1. **AC-081 — Native interactive elements first.** Use `<button>`, `<a href>`, `<input>`, `<select>`, and `<textarea>` for anything interactive; they bring focusability, key handling, and roles for free. A custom widget is built only when no native element fits, and then it implements the APG keyboard model for its pattern in full (AC-089).
2. **AC-082 — Everything operable by pointer is operable by keyboard alone (WCAG 2.1.1).** Every action a mouse or touch user can perform — open, close, submit, sort, filter, delete, drag — is reachable by Tab/Shift+Tab and activatable with Enter and/or Space as the element's pattern requires. If a function has no keyboard path, it does not ship.
3. **AC-083 — No keyboard trap anywhere (WCAG 2.1.2).** Focus can always move away from every component using only the keyboard, including embedded third-party widgets (chat, payment, video iframes). The one exception is a modal dialog, which holds focus only while open and releases it on close (AC-088).
4. **AC-084 — Focus order follows the visual and logical reading order (WCAG 2.4.3).** Tab order comes from DOM order, which is arranged to match the reading order. Positive `tabindex` values (any value above 0) are forbidden — `tabindex="0"` and `tabindex="-1"` are the only permitted values.
5. **AC-085 — The focus indicator is always visible (WCAG 2.4.7).** Every interactive element shows a clear focus indicator in every state (hover, active, disabled-adjacent). The browser outline is never removed unless replaced in the same change by an indicator of equal or better visibility (contrast and thickness) applied via `:focus-visible` or an equivalent.
6. **AC-086 — Focus is never fully obscured by sticky chrome (WCAG 2.4.11).** A focused element must not be entirely hidden by sticky headers, cookie banners, or chat widgets. Sticky elements are paired with `scroll-margin-top` (or the inline equivalent) on focusable content so a scrolled-to focused element clears the chrome.
7. **AC-087 — A bypass block precedes repeated navigation (WCAG 2.4.1).** Every page with repeated navigation opens with a skip link ("Skip to main content") as the first focusable element; it is visible on focus and activating it moves focus to the main content region, not merely scrolls to it.
8. **AC-088 — Dialogs manage focus deliberately.** On open, focus moves into the dialog (first focusable element or the dialog itself); while open, Tab and Shift+Tab cycle inside it; Esc closes it; on close, focus returns to the element that invoked it. A dialog that drops focus to the document body on close fails this rule.
9. **AC-089 — Composite widgets follow the APG keyboard model exactly.** Inside tabs, menus, listboxes, grids, and toolbars, arrow keys move between items, Tab moves into and out of the component as one stop, Home/End jump to the ends, and Esc closes and returns focus to the trigger. Do not invent a per-project key model.
10. **AC-090 — Focus moves on route change or content replacement only by decision.** After a route change, focus lands on a deliberate target (the page heading or main region with `tabindex="-1"`). After dynamic insertion or removal, focus stays on the invoking control or moves to the inserted content's logical start — never silently resets to the top of the document while the user is mid-task.
11. **AC-091 — Every drag or pointer gesture has a keyboard equivalent.** Sliders respond to arrow keys, sortable lists offer keyboard move commands (e.g. select with Space, move with arrows, drop with Space), and drag-to-reorder, drag-to-resize, and drawing surfaces each ship a non-drag path to the same result.
12. **AC-092 — Character-key shortcuts are off by default or remappable (WCAG 2.1.4).** Single printable-character shortcuts are active only when the relevant component has focus, or can be turned off or remapped by the user. Shortcuts never override browser or assistive-technology keys.

## BAN list

- **BAN-AC-041 — Keyboard trap.** Banned: any component — including a third-party embed — that focus can enter but cannot leave with the keyboard alone. Defeats: DET-UX-016. Bad: a chat widget iframe captures Tab focus; the user tabs forever inside the chat and never reaches the checkout button. Instead: fix or configure the embed so focus exits with Tab/Shift+Tab (or Esc), and verify it in the keyboard walk before launch. Severity: BLOCK.
- **BAN-AC-042 — Removed or invisible focus indicator.** Banned: `outline: none` (or `outline: 0`) on interactive elements, or a custom focus style too faint to see, shipped for looks. Defeats: DET-UX-018. Bad: global CSS sets `*:focus { outline: none; }`; keyboard users tab through the nav with no idea where they are. Instead: keep the native outline or supply a visible `:focus-visible` indicator of equal or better contrast and thickness (AC-085). Severity: BLOCK.
- **BAN-AC-043 — Pointer-only control.** Banned: an interactive element that responds only to mouse/touch — a clickable `<div>` with a click handler, or a menu that opens only on hover — with no focus stop and no key operation. Defeats: DET-UX-001. Bad: the primary "Buy now" card is a `<div onclick>`; keyboard focus skips it entirely and the CTA is dead for keyboard users. Instead: use a native `<button>` or link, or implement the full APG pattern with focusability, key handling, role, and name. Severity: BLOCK.
- **BAN-AC-044 — Dialog that strands focus.** Banned: a modal that, on close, leaves focus on the removed element or resets it to the document body, so the keyboard user restarts from the page top. Defeats: DET-UX-017. Bad: closing "Delete item?" with Esc drops focus to `<body>`; the user must tab through 60 header and nav stops to get back to the list. Instead: store the invoking element on open and restore focus to it on close (AC-088). Severity: BLOCK.
- **BAN-AC-045 — Undismissable modal.** Banned: a modal, lightbox, or interstitial that cannot be closed with the keyboard (no Esc handling and no focusable close control). Defeats: DET-UX-028. Bad: a promo lightbox whose only close affordance is a hover-revealed × in the corner; a keyboard user who tabs in can never dismiss it. Instead: support Esc and provide a labeled, focusable close button reachable in the dialog's tab cycle. Severity: BLOCK.

## Gates

- **G-AC-041 — Positive-tabindex and outline lint (automated).** Verifies: AC-084, AC-085. Check: run `grep -rnE 'tabindex="[1-9][0-9]*"|tabIndex=\{[1-9]' src/` (must return zero matches) and the project's CSS lint rule flagging `outline: none|0` on `:focus` selectors with no replacement indicator in the same rule block. Pass: zero positive tabindex values and zero unreplaced outline removals in the codebase. Fail: block shipment. Recorded in: progress.md.
- **G-AC-042 — Scripted Tab-order walk (automated).** Verifies: AC-082, AC-084, AC-085, AC-086. Check: a Playwright script loads each primary page, presses Tab repeatedly, and records `document.activeElement` at each stop; assert (a) every interactive element in the page is reached, (b) the stop sequence matches the DOM/reading order, and (c) each focused element's computed style shows a visible indicator (non-`none` outline, box-shadow, or border change) and its bounding box is not fully covered by sticky chrome. Pass: all assertions green on all primary pages. Fail: block shipment. Recorded in: progress.md.
- **G-AC-043 — No-mouse journey completion (manual).** Verifies: AC-082, AC-091. Check: with the mouse disconnected or pointer input disabled, complete each primary journey (register, search → detail, add to cart → checkout, submit a form with an error and correct it) using only Tab, Shift+Tab, Enter, Space, arrow keys, and Esc. Pass: every journey completes with no step requiring a pointer and no drag action lacking a keyboard equivalent. Fail: block shipment. Recorded in: progress.md.
- **G-AC-044 — Dialog focus test.** Verifies: AC-083, AC-088. Check: for every dialog, menu, and lightbox: open it from the keyboard; confirm focus lands inside it; Tab through a full cycle and confirm focus stays inside; close with Esc and confirm focus is back on the invoking element; repeat for any third-party embed, confirming focus can also leave it. Pass: all dialogs pass all four steps. Fail: block shipment. Recorded in: progress.md.
- **G-AC-045 — Skip-link check.** Verifies: AC-087. Check: on every page template, press Tab once from the top of the page: the skip link must be the first stop and visible; activate it and confirm focus (not just scroll position) moves into the main content, so the next Tab lands on the first main-content control. Pass: every template passes. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Click-through sign-off.** Testing a flow by clicking through it and declaring it "works", when no one ever tabbed through it. Catch it by asking for the G-AC-043 record — if there is no no-mouse run, the flow was never keyboard-tested.
- **Focus reset after every update.** Live regions and partial-page updates that bounce focus back to the top of the document after each change, forcing keyboard users to re-tab through the header dozens of times per task. Catch it by watching `document.activeElement` across an update during the keyboard walk (AC-090).
- **Fake focus highlight.** A custom widget that paints a "focused" style on the visually highlighted item while real DOM focus sits elsewhere (often on a hidden input), so the highlight and the keyboard diverge. Catch it by comparing the highlighted item against `document.activeElement` at each arrow-key step.
- **Separate "keyboard mode".** Shipping keyboard support as a special toggle, alternate page, or "accessible version" instead of making the one product operable. Catch it in review: if the fix lives anywhere other than the component itself, it is this anti-pattern.

## Examples

- [Example 1 — Clickable div card vs. native button](examples/example-1.md) — violates/corrects AC-081, AC-082.
- [Example 2 — Focus-stranding dialog vs. managed dialog](examples/example-2.md) — violates/corrects AC-088.
- [Example 3 — Positive tabindex and removed outline vs. DOM order and visible focus](examples/example-3.md) — violates/corrects AC-084, AC-085.

## Recall anchors

- If a mouse can do it, the keyboard can do it — or it does not ship.
- Tab order is DOM order; positive tabindex is banned.
- Never remove the outline without a better one in the same change.
- Dialogs: focus in on open, trapped while open, returned on close.
- First Tab stop on every page: the skip link.

## Checklist

- [ ] All interactive elements are native elements or full APG-pattern widgets (AC-081, AC-089).
- [ ] Every pointer operation, including drag, has a working keyboard path (AC-082, AC-091).
- [ ] No keyboard trap exists anywhere, including third-party embeds (AC-083).
- [ ] Lint is clean: zero positive tabindex values, zero unreplaced outline removals (AC-084, AC-085, G-AC-041).
- [ ] Scripted Tab-order walk passes on all primary pages, focus visible and unobscured at every stop (G-AC-042, AC-086).
- [ ] Primary journeys completed with no mouse (G-AC-043).
- [ ] Every dialog traps focus while open, closes with Esc, and returns focus to its invoker (AC-088, G-AC-044).
- [ ] Skip link is the first Tab stop on every template and moves focus to main content (AC-087, G-AC-045).
