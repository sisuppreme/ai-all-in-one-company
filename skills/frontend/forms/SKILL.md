# forms

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** W3C WAI, Developing for Web Accessibility (labels, instructions, error help) — http://www.w3.org/WAI/tips/developing/ ; NN/g, Empty-State Interface Design (form-adjacent state copy) — https://www.nngroup.com/articles/empty-state-interface-design/ ; inherited Web Craft Pro Max rules R-11.4-1…R-11.4-5, mapped in docs/WCPM_MAPPING.md
- **Depends on:** component-library, ui-states
- **Feeds into:** frontend-core, data-fetching

## When to use / Do NOT use

- **Use when:** building or reviewing any form — signup, checkout, settings, search-with-filters, multi-step flows — its labels, validation, error handling, and submission behavior.
- **Do NOT use when:** the question is server-side validation rules or persistence (D4 owns those; this skill owns what the user sees and how the form behaves), or the surface is a single button with no input (component-library covers it).

## Rules

1. **FE-241 — Every control has a visible, associated label.** Each input carries a `<label>` tied by `for`/`id` (or wrapping), visible at all times. Placeholder text is never the only label.
2. **FE-242 — Instructions come before the field.** Format hints, constraints, and password rules appear before or within the label and are tied to the control with `aria-describedby`, where forms-mode screen readers encounter them — never revealed only after a failed submit.
3. **FE-243 — Validation fires on blur and submit, never earlier.** No error appears before the user's first blur or first submit attempt (inherited R-11.4-2). Keystroke-by-keystroke scolding is prohibited.
4. **FE-244 — Errors are inline, named, and summarized.** Each error sits next to its field, names the field and the fix in plain text, and is wired with `aria-invalid` + `aria-describedby`. On submit, an error summary appears at the top and focus moves to it. One error per field at a time; never blame the user.
5. **FE-245 — Entered data survives errors.** A validation failure, a timeout, a reload, or back navigation never clears what the user typed (inherited R-11.4-1). The user fixes the one bad field, not the whole form.
6. **FE-246 — Use `autocomplete` for known data.** Name, email, address, payment, and one-time-code fields carry the standard `autocomplete` tokens so browsers and password managers can fill them.
7. **FE-247 — Required is marked in text.** Required fields say so in words ("required" in the label or legend), not by color or a bare asterisk alone; optional fields in a mostly-required form are marked "optional" instead.
8. **FE-248 — Submission is idempotent from the user's side.** The submit control disables on submit, retries reuse one idempotency key, and double-clicks cannot create duplicate records. Success ends in a confirmation (with ui-states), never silence.
9. **FE-249 — Multi-step flows stay short and honest.** 3–5 steps (target ≤3) with a progress indicator showing honest step counts; forms with legal, financial, or irreversible consequences include a review step before submission (inherited R-11.4-3). Multi-step forms save progress so the user can leave and resume.
10. **FE-250 — Signup stays minimal.** Signup targets ≤3 fields, hard maximum 5; any field beyond 3 needs a written justification in the project notes (inherited R-11.4-4).

## BAN list

- **BAN-FE-121 — Placeholder as the only label.** Banned: an input whose placeholder is its sole label, disappearing the moment the user types. Defeats: DET-UX-022. Bad: `<input placeholder="Email address">` with no `<label>` — after typing, the field is anonymous. Instead: a visible, associated label (FE-241); the placeholder may show an example format only. Severity: BLOCK.
- **BAN-FE-122 — Color-only error signals.** Banned: marking an error with only a red border or red text color, with no message. Defeats: DET-UX-021 (see also DET-UX-005). Bad: the email field turns red on submit and nothing anywhere says why. Instead: inline text naming the field and the fix, wired per FE-244. Severity: BLOCK.
- **BAN-FE-123 — Form wipes input on error.** Banned: clearing entered values when validation fails or the request errors. Defeats: DET-UX-007. Bad: one bad postal code empties the entire checkout form. Instead: preserve every value and flag only the bad field (FE-245). Severity: BLOCK.
- **BAN-FE-124 — Double-submit creates duplicates.** Banned: a submit path where a double-click, retry, or refresh-resubmit creates a second record or charge. Defeats: DET-UX-024. Bad: impatient double-click on "Place order" produces two orders. Instead: disable on submit plus a server-honored idempotency key (FE-248). Severity: BLOCK.
- **BAN-FE-125 — Submit that goes nowhere.** Banned: a form whose submit shows a success-looking state without a real request behind it. Defeats: DET-UX-003. Bad: "Request a demo" shows a thank-you message; nothing is sent or stored anywhere. Instead: a real endpoint, a real confirmation, and an error state when the request fails. Severity: BLOCK.

## Gates

- **G-FE-121 — axe-core form rules in CI.** Verifies: FE-241, FE-244, FE-247. Check: automated — run axe-core against every form page in CI and fail the build on label, `aria-invalid`, or describedby violations. Manual form (tool-form substitution): where no browser, axe-core runtime, or CI is available, perform the manual form inspection instead — verify every field has a persistent programmatic label, `aria-invalid` is set only on fields in error, and every error is tied to its field by `aria-describedby` — and record it in progress.md as a tool-form substitution for this gate; the automated axe-core run remains required wherever tooling exists. Pass: 0 violations (automated) or zero findings under the manual form. Fail: block shipment. Recorded in: progress.md.
- **G-FE-122 — Keyboard-only submit test.** Verifies: FE-243, FE-244, FE-245. Check: automated — Playwright, keyboard only: submit the empty form and assert focus lands on the error summary; correct all but one field, resubmit, and assert the remaining error names its field and every previously entered value is still present. Shape-adapted form: for a single-field form, the same assertions reduce to that field — submit it empty and assert focus lands on the error summary and the error names the field; enter an invalid value, resubmit, and assert the entered value is still present and the error still names the field; correct it and assert the submit succeeds. Pass: all assertions green. Fail: block shipment. Recorded in: progress.md.
- **G-FE-123 — Double-submit test.** Verifies: FE-248. Check: automated — Playwright double-clicks the submit control (and fires a duplicate request with the same idempotency key); assert exactly one record exists afterward. Pass: one record. Fail: block shipment. Recorded in: progress.md.
- **G-FE-124 — Screen-reader pass on the primary form.** Verifies: FE-242, FE-244, FE-247. Check: manual — complete the primary form with a screen reader in forms mode: every label, hint, and required marker is announced, and each error is reachable and understandable without sight. **Human-required:** this gate's evidence is a human listening to a real screen reader; no automated or agent-produced substitute satisfies it, and autonomous completion is blocked until the human pass is recorded. Agent-evidence form (interim evidence only — it prepares and de-risks the human pass but never replaces it): the agent records the G-FE-121 scan result, the G-FE-122 keyboard-test result, and an accessibility-tree audit of the form (every label, hint, required marker, and error association present in the tree) in progress.md, marks this gate human-required, and records a human-evidence waiver request naming the human pass still owed. Pass: the form is fully completable by ear, evidenced by the recorded human pass. Fail: warn, fix before release. Recorded in: progress.md.

## Anti-patterns

- **The asterisk mystery.** A form peppered with red asterisks and a footnote "* required" three screens away. Catch it: if a user must hunt for the legend, required state is not marked in text (FE-247).
- **The scolding form.** Errors phrased as accusations or codes — "Invalid input!", "Error 422". Catch it: read each message aloud; if it doesn't name the field and the fix, it fails FE-244's plain-text rule.
- **The helpful reset.** A "Clear form" button placed beside Submit, or a cancel that silently discards a long form. Catch it: any control that destroys input needs a confirmation and a reason to exist at all.
- **Validation theater.** Green checkmarks on every field as the user types, errors flashing mid-word. Catch it: if feedback appears before first blur, FE-243 is violated even when it looks polished.

## Examples

- [Example 1 — Placeholder-only input replaced by a labeled control](examples/example-1.md) — corrects FE-241.
- [Example 2 — Wiped form and generic error replaced by inline errors with data preserved](examples/example-2.md) — corrects FE-244 and FE-245.
- [Example 3 — Double-click duplicates replaced by idempotent submission](examples/example-3.md) — corrects FE-248.

## Recall anchors

- Label first: visible, associated, never placeholder-only.
- Validate on blur and submit — never on the first keystroke.
- Errors name the field and the fix, inline and in a focused summary.
- Never lose the user's work.
- One submit, one record — no matter how many clicks.

## Checklist

- [ ] Every control has a visible associated label and hints before the field (FE-241, FE-242).
- [ ] axe-core form pass is clean in CI, or the manual form inspection is recorded as a tool-form substitution (G-FE-121).
- [ ] Keyboard-only submit test passes: focus on summary, errors name fields, data survives (G-FE-122).
- [ ] Double-submit test proves exactly one record (G-FE-123).
- [ ] Required fields are marked in text; autocomplete tokens are set (FE-246, FE-247).
- [ ] Screen-reader pass completed on the primary form (G-FE-124, human-required — agent-evidence form recorded until the human pass lands).
- [ ] Multi-step flows show honest progress and save/resume works (FE-249).
