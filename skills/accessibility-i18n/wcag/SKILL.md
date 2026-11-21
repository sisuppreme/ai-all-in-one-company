# wcag

## Metadata

- **Owner department:** D13 Accessibility & i18n (AC)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** WCAG 2.2, W3C — https://www.w3.org/TR/WCAG22/ ; "What's New in WCAG 2.2", W3C WAI — https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- **Depends on:** none (this skill fixes the conformance target every other D13 skill builds or tests against)
- **Feeds into:** accessibility-audit, keyboard-accessibility, screen-readers, accessibility-law, reduced-motion, inclusive-copy

## When to use / Do NOT use

- **Use when:** Building or changing any interface that must conform — this skill is the conformance discipline itself: how each WCAG criterion is met by construction in design tokens, markup, and interaction code, at the project's fixed target of WCAG 2.2 Level AA.
- **Do NOT use when:** Running an evaluation and producing findings (that is accessibility-audit — it audits against the target this skill sets), mapping laws to a pinned version (accessibility-law), or deep work owned by a sibling skill (keyboard-accessibility, screen-readers, reduced-motion). This skill states the criteria-level requirements those skills implement in detail.

## Rules

1. **AC-021 — Fix the target in writing before build.** Every project records its target as "WCAG 2.2 Level AA" in its project files before interface work starts. Where a contract or law pins an older version (EN 301 549/EAA pins 2.1 AA; Section 508 pins 2.0 AA), the pin is recorded alongside; building to 2.2 AA satisfies the older pins in almost every case, because 2.2 only removes the obsolete 4.1.1 Parsing. Claims are always stated against a named version and level — never bare "WCAG compliant."
2. **AC-022 — Contrast floors, computed from the actual palette.** Normal text ≥4.5:1 (1.4.3); large text ≥3:1 (1.4.3); UI component boundaries and meaningful graphics ≥3:1 against adjacent colors (1.4.11). Ratios are computed from the real token values and re-checked in every state (hover, focus, disabled-looking, placeholder, error) — never eyeballed from a design mock.
3. **AC-023 — Color is never the only carrier of meaning (1.4.1).** Every state or distinction shown in color (error, success, required, chart series, selected) is paired with a redundant cue: text, icon, pattern, or position. If a screen still reads correctly in grayscale, this rule passes.
4. **AC-024 — Focus is visible and never fully hidden.** Every interactive element shows a visible focus indicator (2.4.7), and a focused component is never entirely obscured by author-created content such as sticky headers, cookie banners, or chat widgets (2.4.11). Sticky chrome ships with `scroll-margin` (or equivalent) sized so focused elements clear it.
5. **AC-025 — Pointer targets meet the size floor.** Targets are at least 24×24 CSS px, or have equivalent spacing so a 24px circle centered on the target does not overlap another target (2.5.8). Where space allows, the design target stays in the 44px class; the 2.5.8 floor is a minimum, not a goal.
6. **AC-026 — Everything is keyboard-operable, in logical order, with no traps.** All functionality works by keyboard alone (2.1.1); focus can always move on or out of every component (2.1.2); focus order follows the visual and reading order (2.4.3) with no positive `tabindex` values. Custom widgets follow the sibling keyboard-accessibility skill's APG models.
7. **AC-027 — Name, role, and value are programmatic; status is announced.** Every component exposes its name, role, value, and state to assistive technology (4.1.2) — native HTML elements first, ARIA only where HTML has no equivalent. Status messages (toasts, result counts, save confirmations) are announced via live regions without moving focus (4.1.3).
8. **AC-028 — Text alternatives and persistent labels.** Informative images carry real alt text and decorative images carry `alt=""` (1.1.1) — never a file name. Every form field has a persistent, programmatically associated visible label (1.3.1, 3.3.2); a placeholder may show a format example only. A control's accessible name matches or contains its visible label (2.5.3).
9. **AC-029 — The 2.2 interaction additions are built in.** Every dragging movement has a single-pointer alternative that needs no path-based gesture (2.5.7). Authentication offers a path with no cognitive-function test as the only option — no memorized codes, puzzles, or blocked paste (3.3.8).
10. **AC-030 — Help is consistent and entry is never redundant.** Help mechanisms (contact link, chat, help page) appear in the same relative order on every page that has them (3.2.6). Information the user already gave in the same process is pre-filled or selectable, never re-typed, except where re-entry is essential or security-required (3.3.7).
11. **AC-031 — Conformance is inherited from the design system.** Design tokens are mapped to the criteria they satisfy: each text/background pair to 1.4.3/1.4.11, each target-size token to 2.5.8, each focus style to 2.4.7/2.4.11. A component built entirely from mapped tokens inherits its conformance; a token change re-triggers the mapping check for every criterion that token serves.
12. **AC-032 — Claims are per criterion, per full page, per complete process.** Conformance applies to full pages and complete processes (a checkout fails if step 3 fails), using only accessibility-supported technologies, with non-interference from any non-conforming content on the page. Results are reported per criterion — never as a blanket claim that a page or product "is accessible."

## BAN list

- **BAN-AC-011 — Focus outline removed for looks.** Banned: `outline: none` (or an equivalent reset) on interactive elements with no equal-or-better focus indicator replacing it. Defeats: DET-UX-018. Bad: global reset `*:focus { outline: none; }` shipped because outlines "looked messy" in review. Instead: keep a designed `:focus-visible` indicator on every interactive element, styled from the mapped focus token (AC-024, AC-031). Severity: BLOCK.
- **BAN-AC-012 — Color-only state.** Banned: conveying error, success, required, or selection state by color change alone, with no text, icon, or position cue. Defeats: DET-UX-021. Bad: invalid fields get a red border only; in grayscale the form gives no hint which fields failed. Instead: pair every color signal with a redundant cue — an error icon plus a text message naming the problem (AC-023). Severity: BLOCK.
- **BAN-AC-013 — Placeholder as the only label.** Banned: a form field whose sole label is placeholder text that disappears on input. Defeats: DET-UX-022. Bad: checkout fields labeled only by placeholders ("Card number", "Expiry"), unlabeled once filled and unnamed to screen readers. Instead: give every field a persistent visible `<label>`; use the placeholder, if at all, for a format example such as "MM / YY" (AC-028). Severity: BLOCK.
- **BAN-AC-014 — Sub-floor pointer targets.** Banned: shipping standalone interactive targets smaller than 24×24 CSS px without the 2.5.8 spacing exception. Defeats: DET-UX-019. Bad: 16×16 px icon buttons packed edge-to-edge in a data-table row, including a delete action. Instead: size targets to at least 24×24 CSS px (44px class where space allows) or space them so the 24px circles do not overlap (AC-025). Severity: WARN.
- **BAN-AC-015 — Overlay widget claimed as conformance.** Banned: installing a third-party "accessibility overlay" or toolbar and treating any criterion as met because of it, instead of fixing the underlying code. Defeats: DET-NONE — no DET parameter names this signal; pattern owned by this skill. Bad: low-contrast controls left at 2.6:1 with a note that "the overlay's contrast button resolves 1.4.3." Instead: fix the code and tokens so the criterion is met by construction and verified by the gates below; an overlay changes nothing about the rendered page for users who never open it. Severity: BLOCK.

## Gates

- **G-AC-011 — Palette contrast computed by script.** Verifies: AC-022, AC-031. Check: run the project contrast script (e.g. `node scripts/check-contrast.mjs design-tokens.json`), which parses every text/background and component-boundary token pair — including hover, focus, placeholder, and error states — and computes the WCAG ratio from the actual hex values. Pass: every normal-text pair ≥4.5:1, every large-text and non-text pair ≥3:1, zero pairs skipped. Fail: block shipment. Recorded in: progress.md.
- **G-AC-012 — Automated criterion rules pass in CI.** Verifies: AC-027, AC-028. Check: run axe-core in CI over the changed screens (`npx @axe-core/cli <changed URLs>` or the project CI job) and confirm the rules mapped to 4.1.2, 1.1.1, and label criteria report zero violations. Manual form (tool-form substitution): where no browser or axe-core runtime is available, perform the G-AC-015 criterion checklist by hand for the criteria mapped to 4.1.2, 1.1.1, and labels — inspect each changed screen's name/role/value exposure (AC-027), text alternatives, and label association (AC-028) in the accessibility tree and the source — and record it in progress.md as a tool-form substitution for this gate; the automated run remains required wherever tooling exists. Pass: zero violations on the mapped rule set (automated) or zero unmet criteria under the manual form. Fail: block shipment. Recorded in: progress.md.
- **G-AC-013 — Focus spot-verification on changed screens.** Verifies: AC-024, AC-026. Check: manual pass — Tab through every changed screen; at each stop confirm the indicator is visible and not entirely covered by sticky headers, banners, or widgets; confirm focus enters and leaves every component (no trap) in reading order. Pass: every stop identifiable, none obscured, none trapped. Fail: block shipment. Recorded in: progress.md.
- **G-AC-014 — Target sizes measured.** Verifies: AC-025. Check: measure the rendered bounding boxes of all standalone interactive elements on changed screens (DevTools or a Playwright bounding-box script). Pass: every target ≥24×24 CSS px, or its 24px centered circle overlaps no other target. Fail: block shipment. Recorded in: progress.md.
- **G-AC-015 — Per-release criterion checklist for changed screens.** Verifies: AC-021, AC-032. Check: open the release checklist; for each changed screen, confirm every criterion its changes touch is marked met / not met with the verifying method named (script, CI, or manual pass). Pass: zero unmarked affected criteria, and the target line still reads "WCAG 2.2 Level AA" (or the recorded pinned version). Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Criterion cherry-picking.** Declaring "AA" because the easy criteria pass while an untested one (focus order, live regions) was never checked. Catch it by requiring every claim to name its criterion and method (AC-032) — an unexamined criterion is an unmade claim.
- **Single-viewport conformance.** Checking criteria only at desktop width, so 400% reflow, zoom, and small-viewport target spacing are never exercised. Catch it by spot-checking changed screens at 320 CSS px width and 200%/400% zoom before sign-off.
- **ARIA wallpaper.** Bolting roles and `aria-*` attributes onto broken markup to make a scanner quiet down, instead of switching to the native element that carries the semantics for free. Catch it by asking, for every ARIA attribute in review: "what native element or attribute does this replace, and why can't we use it?" (AC-027).
- **Stale token map.** A palette or focus-style token changes, but the token-to-criterion map is not updated, so inherited conformance silently stops being true. Catch it by diffing token changes against the map in review; any unmapped token change reopens G-AC-011.

## Examples

- [Example 1 — Eyeballed contrast vs. computed token pairs](examples/example-1.md) — violates/corrects AC-022.
- [Example 2 — Focus buried under a sticky header vs. visible, unobscured focus](examples/example-2.md) — violates/corrects AC-024.
- [Example 3 — Drag-only reordering vs. single-pointer alternative](examples/example-3.md) — violates/corrects AC-029.

## Recall anchors

- Target is named: WCAG 2.2 AA, in writing, before build.
- Contrast is computed from real tokens — never eyeballed.
- Focus visible, focus never fully hidden.
- 24×24 minimum; 44 is the design habit.
- Conformance is per criterion, by construction — never by overlay.

## Checklist

- [ ] Project files record the target "WCAG 2.2 Level AA" plus any law/contract pin (AC-021).
- [ ] Contrast script passes on all token pairs in all states (G-AC-011).
- [ ] No state is carried by color alone anywhere in the changed screens (AC-023).
- [ ] Keyboard walk of changed screens: visible focus at every stop, none obscured, none trapped (G-AC-013).
- [ ] All targets measured at ≥24×24 CSS px or spacing-equivalent (G-AC-014).
- [ ] Every field has a persistent label; every informative image has real alt text (AC-028).
- [ ] Drag actions have a single-pointer alternative; login has a non-cognitive-test path (AC-029).
- [ ] Release checklist marks every affected criterion with its verifying method (G-AC-015).
