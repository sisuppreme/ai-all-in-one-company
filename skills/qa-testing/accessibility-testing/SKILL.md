# accessibility-testing

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://playwright.dev/docs/accessibility-testing
- **Depends on:** e2e-testing, browser-verification
- **Feeds into:** qa-gates, bug-triage

## When to use / Do NOT use

- **Use when:** Any release ships user-facing pages or flows; a covered page, state, or widget changes; an accessibility defect needs retest after D13/D3 remediation.
- **Do NOT use when:** The task is fixing the barrier itself (remediation belongs to D13 accessibility-i18n and D3 frontend) or setting the conformance target (D13 owns the standard; this skill executes the tests).

## Rules

1. **QA-101 — Axe runs in CI on every covered page and state.** `@axe-core/playwright` scans each key page and state (default, error, empty, dialog) in CI; any violation fails the build.
2. **QA-102 — Zero violations is the pass bar.** A violation is fixed or filed as a defect with an owner and a date. It is never suppressed in the scan config without a defect-ticket reference in the suppression comment.
3. **QA-103 — Seeded-fault control proves the suite works.** Removing one form label in a throwaway branch must make the CI axe suite fail. A suite that stays green on a seeded fault is broken, and its green results count for nothing until fixed.
4. **QA-104 — Keyboard-only walkthrough every release.** Each named critical flow is completed keyboard-only: Tab order is logical, focus is visible at every stop, no traps, every action reachable and operable.
5. **QA-105 — Screen-reader pass before release.** The top journeys are run with NVDA or VoiceOver before release; every barrier found is filed as a defect, not fixed informally.
6. **QA-106 — Every interactive element is exercised keyboard-only.** Every form control, dialog, and interactive widget on a covered page is reached and operated by keyboard at least once per release.
7. **QA-107 — Test the states users actually meet.** Error states, empty states, loading states, and open dialogs are scanned and walked, not just pristine pages.
8. **QA-108 — Checks run on the real rendered page.** Contrast and label checks execute against the rendered page in a real browser, never against design files or component stories alone.
9. **QA-109 — Findings are defects with the WCAG criterion named.** Each defect records the criterion (e.g., WCAG 2.4.7 Focus Visible), the page and state, and the evidence (axe rule ID or walkthrough step). Remediation is D13/D3's; detection and retest are this skill's.
10. **QA-110 — A scan is never reported as conformance.** Release notes state exactly what ran — "axe scan clean on pages X; keyboard walkthrough and screen-reader pass done on flows Y" — and never call a scan result "WCAG compliant." Playwright's own documentation states automated tests detect only some accessibility problems.
11. **QA-111 — No defect closes without a retest.** After remediation, the exact check that failed (axe rule or walkthrough step) is re-run and its passing result recorded on the defect before closure.
12. **QA-112 — Coverage is an explicit list.** The key pages, states, and critical flows under test are named in the project test plan. An unlisted page is untested, never implicitly passed.

## BAN list

- **BAN-QA-051 — Invisible focus indicator shipped.** Banned: `outline: none` (or equivalent) on interactive elements with no visible replacement focus style. Defeats: DET-UX-018. Bad: `button:focus { outline: none; }` merged because the default outline "looked ugly." Instead: style a visible focus indicator (e.g., a 2px+ outline with sufficient contrast) and verify it in the keyboard walkthrough. Severity: BLOCK.
- **BAN-QA-052 — Keyboard trap in a dialog or widget.** Banned: a modal, menu, or custom widget that captures Tab with no keyboard escape route. Defeats: DET-UX-016. Bad: a cookie dialog where Tab cycles forever inside and Esc does nothing. Instead: Esc closes the dialog and focus returns to the element that opened it; the walkthrough must prove the exit. Severity: BLOCK.
- **BAN-QA-053 — Placeholder text as the only label.** Banned: a form control whose only accessible name is its `placeholder` attribute. Defeats: DET-UX-022. Bad: `<input placeholder="Email">` with no `<label>` and no `aria-label`. Instead: give every control a persistent visible label (or `aria-label` where a visible label is impossible) and let the axe label rule verify it. Severity: BLOCK.
- **BAN-QA-054 — Focus stranded when a dialog closes.** Banned: closing a dialog or completing navigation leaves focus on `<body>` or a removed element, so keyboard and screen-reader users restart from the top. Defeats: DET-UX-017. Bad: after "Delete item" confirms, focus resets to the page top and the user re-tabs through the whole header. Instead: return focus to the invoking element (or the logical next heading/control) and assert the landing spot in the walkthrough. Severity: BLOCK.
- **BAN-QA-055 — Meaning carried by color alone passes untested.** Banned: a state (error, success, required, selected) communicated only by a color change, accepted because the test suite never checks for a non-color cue. Defeats: DET-UX-021. Bad: an invalid field shown only with a red border; the axe scan is green and the release ships. Instead: require an icon, text message, or `aria-invalid` plus described error, and add a walkthrough step that identifies the state with color ignored. Severity: BLOCK.

## Gates

- **G-QA-051 — CI axe suite.** Verifies: QA-101, QA-102, QA-108. Check: `npm run test:a11y` (Playwright + `@axe-core/playwright` over the coverage list). Pass: exit code 0 with zero violations reported. Fail: block merge and release; fix or file per QA-102. Recorded in: progress.md.
- **G-QA-052 — Seeded-fault negative control.** Verifies: QA-103. Check: in a throwaway branch, remove one form label, then run `npm run test:a11y`. Pass: exit code is non-zero and the `label` violation is reported; branch discarded afterward. Fail: the suite is invalid — block release and repair the suite before trusting any green run. Recorded in: progress.md.
- **G-QA-053 — Keyboard walkthrough record.** Verifies: QA-104, QA-106, QA-107. Check: `scripts/check-a11y-walkthrough.sh <release>` exits 0 only when the release's walkthrough file exists with every step of every named critical flow checked, including error and dialog states. Pass: exit code 0. Fail: block release until the walkthrough is actually performed and recorded. Recorded in: progress.md.
- **G-QA-054 — Screen-reader pass record.** Verifies: QA-105, QA-109, QA-111. Check: `scripts/check-a11y-sr-pass.sh <release>` exits 0 only when the pass record names the screen reader and version, the flows covered, and the defect ID filed for each finding (or an explicit "no findings"). Pass: exit code 0. Fail: block release. Recorded in: progress.md.

## Anti-patterns

- **Scan-green theater.** The release is announced as accessible because axe is green, while the keyboard walkthrough was quietly skipped. Catch it: G-QA-053/G-QA-054 records missing or dated after the release note.
- **Pristine-page testing.** Scans and walkthroughs only ever see default states; the error dialog — where users actually get stuck — is never opened during testing. Catch it: the coverage list names states, not just pages.
- **Criterion-free defects.** Findings filed as "the button looks wrong" with no WCAG criterion, page, or evidence, so D13 cannot prioritize and nobody can retest. Catch it: sample open defects against QA-109 before release.
- **Shrinking coverage.** A failing page is dropped from the scan config so the suite goes green, instead of being fixed or ticketed. Catch it: diff the coverage list every release; a removal needs a defect reference, same as a suppression.

## Examples

- [Example 1 — The label that had to fail](examples/example-1.md) — violates/corrects QA-103.
- [Example 2 — "WCAG compliant" from a scan](examples/example-2.md) — violates/corrects QA-110.
- [Example 3 — Focus lost when the dialog closed](examples/example-3.md) — violates/corrects QA-104.

## Recall anchors

- Two layers, both mandatory: machine scan plus human hands.
- A green suite that cannot fail is not a suite — seed a fault and watch it catch.
- A scan result is evidence, never a conformance claim.
- Test the states users meet: error, empty, dialog — not the pristine page.
- Every finding is a defect with a criterion, an owner, and a retest.

## Checklist

- [ ] Axe suite covers every page and state on the coverage list and exits 0 (QA-101, QA-112).
- [ ] Seeded-fault control ran this release and the suite failed as designed (QA-103).
- [ ] No scan suppression lacks a defect-ticket reference (QA-102).
- [ ] Keyboard walkthrough completed and signed for every named critical flow (QA-104, QA-106).
- [ ] Screen-reader pass done on the top journeys; findings filed with criteria named (QA-105, QA-109).
- [ ] Error, empty, and dialog states were scanned and walked, not just default states (QA-107).
- [ ] Remediated defects were retested with the original failing check before closure (QA-111).
- [ ] Release note states exactly what ran, with no conformance claim (QA-110).
