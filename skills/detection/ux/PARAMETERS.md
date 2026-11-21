# DET-UX — UX Detection Parameters (X-UX)

Purpose: expose products that were AI-assembled to look finished but never usability-tested — controls that do nothing, flows that dead-end, states that were never built. Every parameter is checked against real behavior, not screenshots. A parameter fires only when the check below reproduces the failure.

How to run the check: (1) walk the primary flow end-to-end (sign-up, purchase, core task) exactly as a first-time user; (2) walk each secondary flow; (3) repeat the primary flow keyboard-only; (4) repeat it on a small mobile viewport. Record the parameter ID, the exact click path, and the observed result for every hit.

### DET-UX-001 — Dead primary call-to-action
- **Signal:** The main CTA on a landing page, pricing page, or dashboard ("Get started", "Buy", "Save").
- **AI-typical:** Button is rendered but has no handler, an empty `href`, or opens nothing; clicking produces no navigation, modal, or state change.
- **Professional:** Every visible control performs its labeled action or is visibly disabled with a reason.
- **Check:** Click each primary CTA in a fresh session; confirm a real destination or state change occurs within one second.
- **False positives:** A CTA disabled until a prerequisite (e.g., unchecked terms box) is legitimate if the prerequisite is visible and explained nearby.
- **Severity:** blocker
- **Source:** https://www.nngroup.com/articles/ten-usability-heuristics/
- **Fix:** frontend-core, ui-states

### DET-UX-002 — Placeholder and dead-end links
- **Signal:** Footer, nav, and in-copy links pointing to `#`, `javascript:void(0)`, or routes that return a blank page or soft 404.
- **AI-typical:** Full link lists generated for appearance; half resolve to nothing or reload the same page.
- **Professional:** Links are shipped only when their destination exists; unbuilt sections are omitted, not faked.
- **Check:** Extract all links on key pages; click each and record any that stay on-page, 404, or render empty content.
- **False positives:** A `#` anchor that scrolls to a real on-page section is fine; verify the target element exists.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** frontend-core

### DET-UX-003 — Form submits nowhere
- **Signal:** Contact, sign-up, or checkout forms whose submit produces a success-looking response with no data stored or sent.
- **AI-typical:** Submit handler shows a toast or redirects but has no backend call; refreshing shows the submission never existed.
- **Professional:** Submission persists server-side and is retrievable (confirmation email, record in account, admin view).
- **Check:** Submit unique test data; verify it exists afterward via the confirmation channel or a second session.
- **False positives:** A demo or sandbox mode is acceptable only when clearly labeled as a demo before submission.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** forms, frontend-state
- **See also:** DET-FAKE-015 (same defect: UX-003 owns the user-facing symptom — a success response with nothing behind it; FAKE-015 owns the verdict via the persistence/network test)

### DET-UX-004 — No validation on any field
- **Signal:** Forms accepting empty required fields, malformed emails, negative prices, or past dates without complaint.
- **AI-typical:** Inputs are plain text boxes; validation exists neither client-side nor server-side, so garbage reaches storage or crashes later steps.
- **Professional:** Required, format, and range rules are enforced at entry and re-checked server-side.
- **Check:** Submit each form empty, then with deliberately malformed values per field; note anything accepted unchanged.
- **False positives:** A deliberately free-form field (notes, search) may accept anything; required and typed fields may not.
- **Severity:** blocker
- **Source:** https://baymard.com/research-articles/inline-form-validation
- **Fix:** forms
- **See also:** DET-CODE-019 (same missing validation from the code side: CODE-019 owns the boundary/schema verdict; UX-004 owns the field-level behavior)

### DET-UX-005 — Errors surfaced only after submit, far from the field
- **Signal:** A multi-field form that reports mistakes only in a banner after submission, forcing the user to hunt for the offending field.
- **AI-typical:** One generic banner at the top; fields are not highlighted and focus stays at the submit button.
- **Professional:** Inline validation flags the field as it is completed, and any submit-time summary links focus to each error.
- **Check:** Enter one invalid value mid-form; confirm feedback appears at that field before submission is attempted.
- **False positives:** Very short forms (one or two fields) may validate on submit if the error appears adjacent to the field and receives focus.
- **Severity:** major
- **Source:** https://baymard.com/research-articles/inline-form-validation
- **Fix:** forms, ui-states

### DET-UX-006 — Generic, coded, or blaming error messages
- **Signal:** Messages such as "Something went wrong", "Error 422", "Invalid input", or "You entered the wrong password".
- **AI-typical:** Raw exception text or a single catch-all string reused for every failure; no cause, no remedy.
- **Professional:** The message names the exact problem, states the fix in plain language, and never blames the user.
- **Check:** Trigger three distinct errors (format, duplicate account, network failure); compare wording — each must be specific and actionable.
- **False positives:** A deliberately vague credential error ("email or password incorrect") is a security practice, not slop, if it still offers a recovery path.
- **Severity:** major
- **Source:** https://www.nngroup.com/articles/error-message-guidelines/
- **Fix:** forms, ui-states
- **See also:** DET-CODE-022 (CODE-022 owns the code-level cause — a single generic error body; UX-006 owns the user-facing message quality)

### DET-UX-007 — User input destroyed on error
- **Signal:** After a failed submit, page reload, or back navigation, previously entered fields come back empty.
- **AI-typical:** Form state lives only in the failed request; one bad field wipes ten good ones, including long text entries.
- **Professional:** All valid input is preserved through errors and navigation; only the invalid field needs attention.
- **Check:** Fill every field, make one invalid, submit; confirm all other values survive. Repeat with browser Back.
- **False positives:** Password and card fields are legitimately cleared for security; all other fields must persist.
- **Severity:** major
- **Source:** https://baymard.com/research-articles/adaptive-validation-error-messages
- **Fix:** forms, frontend-state

### DET-UX-008 — No loading state on asynchronous actions
- **Signal:** Buttons and views that give no feedback between click and result on slow actions (save, upload, search, page load).
- **AI-typical:** Interface appears frozen; users click again or abandon, and long loads show a blank white screen.
- **Professional:** Feedback within a second — spinner, skeleton, or progress — matched to the wait, with layout held stable.
- **Check:** Throttle the network (Slow 3G profile), trigger each async action, and record what is shown during the wait.
- **False positives:** Actions that genuinely complete near-instantly from cache need no indicator; verify under throttling, not on a fast local network.
- **Severity:** major
- **Source:** https://www.nngroup.com/articles/ten-usability-heuristics/
- **Fix:** ui-states, frontend-state
- **See also:** DET-VIS-032 (VIS-032 owns the designed state set including loading; UX-008 owns the behavior during real asynchronous waits)
- **See also:** DET-CODE-026 (CODE-026 covers missing state handling in code across all state types; UX-008 covers the loading behavior specifically)

### DET-UX-009 — Blank empty states
- **Signal:** Lists, dashboards, inboxes, or search containers that show empty space when they contain no items.
- **AI-typical:** The component renders nothing; the user cannot tell whether the feature is broken, loading, or genuinely empty.
- **Professional:** The empty state explains why it is empty and offers the direct next action (create, import, clear filters).
- **Check:** Use a fresh account with no data; visit every list and dashboard view and record which show unexplained blank areas.
- **False positives:** A truly self-evident empty canvas (a new blank document editor) needs no message; data containers do.
- **Severity:** major
- **Source:** https://www.nngroup.com/articles/empty-state-interface-design/
- **Fix:** ui-states, user-onboarding
- **See also:** DET-VIS-032 (VIS-032 owns the designed empty state; UX-009 owns the unexplained blank the user actually sees)
- **See also:** DET-CODE-026 (CODE-026 covers missing state handling in code across all state types; UX-009 covers the empty-container behavior)

### DET-UX-010 — Failed loads render as blank screens or endless spinners
- **Signal:** A view whose data request fails shows a permanent spinner, an empty shell, or a white page.
- **AI-typical:** Only the success path was built; the error branch of the fetch was never implemented.
- **Professional:** Failures show a plain-language error state with a retry action, and partial content stays visible where possible.
- **Check:** Block the API domain or force 500 responses; load each data view and observe the result and recovery options.
- **False positives:** A brief spinner that resolves to a real error message within a reasonable timeout passes; a spinner with no timeout does not.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** ui-states, frontend-state
- **See also:** DET-VIS-032 (VIS-032 owns the designed error state; UX-010 owns the failed-load dead end and its recovery)
- **See also:** DET-CODE-026 (CODE-026 covers the unimplemented error branch in code across all state types; UX-010 covers the user-facing failure)

### DET-UX-011 — No confirmation after a completed action
- **Signal:** After saving, sending, deleting, or paying, nothing tells the user the action succeeded.
- **AI-typical:** The button returns to idle and the screen is unchanged; users repeat the action or leave unsure it worked.
- **Professional:** Success is confirmed by a visible state change, message, or updated content the user can verify.
- **Check:** Perform each mutating action and record the feedback; then verify the result independently (reload, second view).
- **False positives:** Direct-manipulation actions with an immediately visible result (dragging an item to a new list) are their own confirmation.
- **Severity:** major
- **Source:** https://www.nngroup.com/articles/ten-usability-heuristics/
- **Fix:** ui-states, frontend-state

### DET-UX-012 — Destructive actions without confirmation or undo
- **Signal:** Delete, cancel-subscription, or discard buttons that execute instantly and irreversibly on one click.
- **AI-typical:** A single click permanently removes data; there is no confirm step, no undo window, no trash.
- **Professional:** Destructive actions require confirmation naming the consequence, or execute with a visible undo period.
- **Check:** On test data, click each destructive control once and observe whether anything intercepts the action.
- **False positives:** Low-stakes, easily recreated items (removing a tag) may skip confirmation if undo exists; account and content deletion may not.
- **Severity:** major
- **Source:** https://www.nngroup.com/articles/ten-usability-heuristics/
- **Fix:** ui-states, frontend-core

### DET-UX-013 — Primary flow breaks mid-way
- **Signal:** A step inside checkout, onboarding, or a wizard that cannot be completed — a button that stalls, a step that loops, a required field that rejects valid input.
- **AI-typical:** Each screen was generated in isolation; the hand-off between steps was never exercised end-to-end.
- **Professional:** The complete primary flow is walkable by a first-time user with valid data, start to confirmation.
- **Check:** Complete the full primary flow with fresh valid data in one sitting; log every point requiring a workaround, reload, or guess.
- **False positives:** An intentional gate (payment, identity verification) is a designed pause if it explains itself and resumes the flow afterward.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** frontend-core, frontend-state, user-onboarding

### DET-UX-014 — Navigation dead ends
- **Signal:** Pages reachable in the flow that offer no forward action and no working route back — confirmation screens without links, error pages without exits, orphaned settings pages.
- **AI-typical:** Terminal screens generated as static endpoints; the user's only exit is the browser Back button or editing the URL.
- **Professional:** Every screen provides a clear next step and a route to the main navigation.
- **Check:** At each step of the primary and secondary flows, stop and find an on-screen exit other than browser Back; record any screen lacking one.
- **False positives:** A focused checkout may suppress global navigation deliberately, but must still offer a working exit or cancel path.
- **Severity:** major
- **Source:** https://www.nngroup.com/articles/ten-usability-heuristics/
- **Fix:** frontend-core, user-onboarding

### DET-UX-015 — Same action, different behavior across screens
- **Signal:** Identical labels or icons doing different things in different sections ("Save" that sometimes auto-saves, sometimes opens a dialog; a trash icon that sometimes confirms, sometimes not).
- **AI-typical:** Each screen was generated separately, so patterns drift; users must relearn controls per page.
- **Professional:** A control's label, appearance, and behavior are consistent product-wide; platform conventions are followed.
- **Check:** Pick three repeated controls (save, delete, close) and exercise each in three different sections; compare behavior step by step.
- **False positives:** Genuinely different actions deserve different labels; the failure is same label, different behavior — or different labels, same behavior.
- **Severity:** major
- **Source:** https://www.nngroup.com/articles/ten-usability-heuristics/
- **Fix:** frontend-core, ui-states

### DET-UX-016 — Keyboard trap
- **Signal:** A modal, carousel, date picker, or embedded widget that keyboard focus can enter but cannot leave.
- **AI-typical:** Custom widgets capture Tab or cycle focus internally with no escape key handling.
- **Professional:** Focus can always move on or out with Tab/Shift+Tab or a documented key, per WCAG 2.1.2 No Keyboard Trap.
- **Check:** Keyboard-only: Tab into every interactive component on the page, then Tab and Shift+Tab out of each; record any component that cannot be exited.
- **False positives:** A modal legitimately cycles focus while open — it passes if Esc or its close control releases focus back to the page.
- **Severity:** blocker
- **Source:** https://www.w3.org/TR/WCAG22/
- **Fix:** keyboard-accessibility, accessibility-audit

### DET-UX-017 — Focus lost or stranded after dialogs and navigation
- **Signal:** Closing a modal, submitting a form, or changing views drops focus to the top of the document or nowhere visible.
- **AI-typical:** No focus management exists; keyboard and screen-reader users restart from the page top after every interaction.
- **Professional:** Focus moves deliberately — into a dialog on open, back to the trigger on close, to the heading or result on view change.
- **Check:** Keyboard-only: open and close each dialog, submit a form with an error, and follow a route change; note where focus lands each time.
- **False positives:** Moving focus to an error summary after a failed submit is correct behavior, not loss — it fails only when focus lands nowhere meaningful.
- **Severity:** major
- **Source:** https://www.w3.org/TR/WCAG22/
- **Fix:** keyboard-accessibility, frontend-core

### DET-UX-018 — Focus indicator removed or invisible
- **Signal:** Interactive elements with `outline: none` and no replacement style, so keyboard users cannot see where they are.
- **AI-typical:** Global CSS resets strip outlines for visual cleanliness and no `:focus-visible` style is added back.
- **Professional:** Every focusable element shows a clearly visible indicator when reached by keyboard (WCAG 2.4.7 Focus Visible).
- **Check:** Tab through each page watching the indicator continuously; flag any stop where the focused element cannot be identified visually.
- **False positives:** Mouse-only styling differences are fine; the indicator must appear for keyboard focus specifically (`:focus-visible` satisfies this).
- **Severity:** major
- **Source:** https://w3c.github.io/wcag/understanding/focus-visible
- **Fix:** keyboard-accessibility, accessibility-audit

### DET-UX-019 — Touch targets below minimum size
- **Signal:** Icon buttons, table-row actions, and dense link clusters whose tappable area is under 24×24 CSS pixels (WCAG 2.5.8 minimum) or tightly packed against neighbors.
- **AI-typical:** Desktop-density controls shipped unchanged to mobile; mis-taps hit adjacent actions, sometimes destructive ones.
- **Professional:** Targets meet at least the WCAG minimum, with platform-sized targets (Material 48dp, Apple 44pt) for primary controls.
- **Check:** On a mobile viewport, measure the bounding boxes of icon buttons and row actions in DevTools; tap-test dense clusters for mis-hits.
- **False positives:** Inline links inside a paragraph and targets covered by the WCAG spacing exception are exempt; standalone icon buttons are not.
- **Severity:** major
- **Source:** https://www.w3.org/TR/WCAG22/
- **Fix:** layout-responsive, accessibility-audit

### DET-UX-020 — Interactive text and controls unreadable at real sizes
- **Signal:** Button labels, links, placeholder text, and field borders rendered in low-contrast gray on light backgrounds.
- **AI-typical:** Pale "minimal" palettes applied uniformly; placeholders and disabled-looking labels fall below WCAG contrast (4.5:1 text, 3:1 non-text).
- **Professional:** Text and control boundaries meet WCAG 1.4.3 and 1.4.11 ratios in every state, including hover and placeholder.
- **Check:** Sample the contrast ratio of button text, links, placeholders, and input borders with a contrast tool on each template.
- **False positives:** Genuinely disabled controls are exempt from contrast minimums — but only if they are actually disabled and their state is explained.
- **Severity:** major
- **Source:** https://www.w3.org/TR/WCAG22/
- **Fix:** accessibility-audit, frontend-core

### DET-UX-021 — Meaning carried by color alone
- **Signal:** Errors marked only by a red border, success only by green, required fields only by a colored asterisk, chart series distinguished only by hue.
- **AI-typical:** Color is the fastest styling lever, so state is encoded purely in color with no icon, text, or position cue.
- **Professional:** Every color signal is paired with a redundant cue — text, icon, or label — per WCAG 1.4.1 Use of Color.
- **Check:** View key screens in grayscale (DevTools rendering emulation); confirm errors, states, and required fields are still identifiable.
- **False positives:** Decorative color with no informational role needs no redundant cue; the test applies only where color carries meaning.
- **Severity:** major
- **Source:** https://www.w3.org/TR/WCAG22/
- **Fix:** accessibility-audit, ui-states

### DET-UX-022 — Placeholder text used as the only label
- **Signal:** Form fields whose sole label is placeholder text that vanishes on typing.
- **AI-typical:** Clean-looking label-less fields; once filled, the user cannot verify what a field asked, and screen readers get no reliable label.
- **Professional:** Every field has a persistent visible label; placeholders, if present, show format examples only.
- **Check:** Fill each form completely, then re-read it: any field whose purpose is no longer identifiable from its label fails.
- **False positives:** A single search box with a labeled search icon and accessible name is an accepted exception; multi-field forms are not.
- **Severity:** major
- **Source:** https://www.nngroup.com/articles/error-message-guidelines/
- **Fix:** forms, accessibility-audit

### DET-UX-023 — Mobile layout breaks the primary task
- **Signal:** At a small viewport the primary CTA falls off-screen, content requires horizontal scrolling, or fixed bars overlap the controls they sit above.
- **AI-typical:** A desktop layout is squeezed by breakpoints never tested against the actual flow; sticky headers and chat bubbles cover buttons.
- **Professional:** The primary flow is fully completable one-handed at 360px wide, with nothing essential obscured or off-canvas.
- **Check:** At 360×640, complete the primary flow by touch only; log every horizontal scroll, overlap, or unreachable control.
- **False positives:** Wide data tables may scroll horizontally if the pattern is deliberate and key columns stay fixed; the primary task flow may not.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** layout-responsive, frontend-core
- **See also:** DET-VIS-038 (page-level horizontal overflow is VIS-038's visual defect; UX-023 owns the primary-task verdict at small widths)
- **See also:** DET-VIS-037 (adjacent: VIS-037 covers layouts that stack without adapting; UX-023 covers the task flow that breaks as a result)

### DET-UX-024 — Submit can be fired twice
- **Signal:** A submit or pay button that stays active during processing, so a double-click or impatient retry creates duplicate orders, posts, or charges.
- **AI-typical:** No pending state on the button and no idempotency behind it; duplicates appear in the resulting list.
- **Professional:** The control disables or shows a processing state on first activation, and the operation is idempotent server-side.
- **Check:** On a throttled connection, double-click the primary submit; inspect the result for duplicates.
- **False positives:** Deliberate repeat actions (add-another-item) are separate controls by design; the payment/final-submit control itself must lock.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 7
- **Fix:** forms, frontend-state, ui-states
- **See also:** DET-CODE-030 (CODE-030 owns the server-side cause — no idempotency, constraint, or transaction; UX-024 owns the still-active control that lets the user fire twice)

### DET-UX-025 — Search and filter dead ends
- **Signal:** A search or filter combination returning zero results shows a blank area with no explanation and no way to broaden or reset.
- **AI-typical:** The results component renders an empty list; the active filters are invisible and there is no clear-filters action.
- **Professional:** The no-results state says what matched nothing, shows the active constraints, and offers to clear or adjust them.
- **Check:** Search for a nonsense term, then apply an impossible filter combination; record whether a recovery path is offered in both cases.
- **False positives:** An admin or log viewer may show a plain "no records" line if filters remain visible and editable; consumer search may not dead-end.
- **Severity:** minor
- **Source:** https://www.nngroup.com/articles/empty-state-interface-design/
- **Fix:** ui-states, frontend-core

### DET-UX-026 — Session expiry silently destroys work
- **Signal:** A long form or editor that times out and discards everything when the user returns or submits.
- **AI-typical:** No autosave, no expiry warning, no draft recovery; the first sign of timeout is total data loss.
- **Professional:** Work is autosaved or draft-preserved, expiry is warned in advance, and re-login restores the in-progress state.
- **Check:** Start the longest form, wait past the session timeout (or expire the session manually), submit, and observe what survives.
- **False positives:** Short single-step forms with no meaningful work product are exempt; multi-step and long-text flows are not.
- **Severity:** major
- **Source:** https://www.w3.org/TR/WCAG22/
- **Fix:** frontend-state, forms

### DET-UX-027 — Requirements revealed only by failing
- **Signal:** Password rules, file-type limits, character counts, and required fields are discoverable only by submitting and being rejected.
- **AI-typical:** Constraints live in validation code but are never stated in the interface; users guess, fail, and retry.
- **Professional:** Requirements are stated up front at the field, and required versus optional is marked before any input.
- **Check:** Before typing anywhere, read each form and list which constraints you can learn from the screen alone; any rule learnable only from an error fails.
- **False positives:** Constraints that genuinely depend on other answers (a date that must follow a chosen start date) may be revealed contextually — before submission, not after.
- **Severity:** minor
- **Source:** https://baymard.com/research-articles/inline-form-validation
- **Fix:** forms, user-onboarding

### DET-UX-028 — Modal that cannot be dismissed
- **Signal:** A dialog, paywall, or cookie banner with no visible close control, no Esc handling, and no click-outside path, blocking the page behind it.
- **AI-typical:** The dialog was generated as a static overlay; dismissal logic was never wired, or the only exit is completing the embedded form.
- **Professional:** Every modal offers an obvious close affordance and Esc dismissal, except where a forced decision is genuinely required and explained.
- **Check:** Open each dialog; try, in order, the close control, Esc, and clicking the backdrop; record any dialog that survives all three.
- **False positives:** A truly blocking decision (confirming a destructive action, accepting updated terms to continue a regulated service) may require a choice — but must still offer a real choice, including cancel.
- **Severity:** blocker
- **Source:** https://www.nngroup.com/articles/ten-usability-heuristics/
- **Fix:** ui-states, keyboard-accessibility, frontend-core
