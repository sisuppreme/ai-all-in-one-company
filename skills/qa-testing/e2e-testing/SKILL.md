# e2e-testing

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Playwright, "Best Practices" — https://playwright.dev/docs/best-practices ; Stripe, "Testing" (test and decline cards) — https://docs.stripe.com/testing ; Ham Vocke, "The Practical Test Pyramid" — https://www.martinfowler.com/articles/practical-test-pyramid.html
- **Depends on:** unit-testing, integration-testing, test-data
- **Feeds into:** qa-gates, browser-verification

## When to use / Do NOT use

- **Use when:** a user flow the business cannot afford to break — signup, login, the core transaction, the top admin action — needs proof against a deployed build, including its failure paths and its resistance to fake functionality.
- **Do NOT use when:** the behavior can be proven at the unit or integration layer — push it down the pyramid instead. Do not use e2e to re-verify component rendering (visual-regression) or one-off rendered-truth checks of a live URL (browser-verification).

## Rules

1. **QA-041 — Critical flows only.** The suite covers signup, login, the core transaction, and the top admin action. Every journey names the revenue or risk it protects; a journey that cannot name one is removed or pushed down the pyramid.
2. **QA-042 — No fixed sleeps.** Waiting is always a web-first assertion on visible state or a wait on a named network response. `waitForTimeout` and hand-rolled sleep helpers do not appear in the suite.
3. **QA-043 — Full isolation.** Every test provisions its own account and data through the UI or a setup API, uniquely names its records, and passes when run alone, in any order, and in parallel with the rest of the suite.
4. **QA-044 — Locate by role and label.** Elements are located with `getByRole`, `getByLabel`, or `getByText`. CSS and XPath selectors are forbidden; where no accessible name exists, the fix is a `data-testid` in the app plus a comment in the test naming why.
5. **QA-045 — Deployed build, real browsers.** The suite runs in CI against a preview or staging deployment, never a dev server, in Chromium plus at least one of Firefox or WebKit. The build SHA and environment URL are recorded with the run.
6. **QA-046 — Persistence probe on every mutation.** After any create, edit, or delete, the journey reloads the page and re-reads the value from a fresh render; a sign-out/sign-in re-read is required for account-level data. Asserting the immediate UI state alone is not proof.
7. **QA-047 — Failure paths are journeys.** Each covered flow has at least one negative journey: the provider decline card produces a visible decline, the invalid form shows field errors and writes nothing, and a killed dependency degrades visibly instead of hanging or faking success.
8. **QA-048 — Network write assertion.** Every mutating journey asserts the write actually left the browser: the expected request (method and path) is observed, and the persisted value from QA-046 matches what was sent.
9. **QA-049 — Second-account convergence.** For shared or multi-user data, a journey creates data as account A and verifies account B sees exactly what the permissions model promises — no more, no less.
10. **QA-050 — Failure artifacts are mandatory.** Every CI failure uploads trace, screenshot, and video. A failure without artifacts is re-run locally to reproduce it before any triage or code change.
11. **QA-051 — Flakes are defects, not noise.** A retry-pass is logged as a flake with a filed ticket. A test that flakes twice in seven days is quarantined with a named owner and an expiry date; CI retry settings never silently absorb a recurring failure.
12. **QA-052 — Admission rule for new journeys.** A new e2e test is admitted only with a written note naming the lower layer that cannot cover the case. No note, no merge.

## BAN list

- **BAN-QA-021 — Success-card-only payment journey.** Banned: a checkout journey that pays only with a success test card and never exercises a decline. Defeats: DET-FAKE-007. Bad: the suite pays with the always-approve card, asserts the confirmation page, and ships while real declines also "succeed." Instead: add the documented decline-card journey asserting a visible decline and no created order. Severity: BLOCK.
- **BAN-QA-022 — Toast-only assertion.** Banned: asserting a success toast or banner after a mutation without reloading and re-reading the persisted value. Defeats: DET-FAKE-016. Bad: the profile test saves a new name, asserts "Profile updated," and ends — the edit never persisted. Instead: reload, re-read the field from a fresh render, and sign out/in before asserting. Severity: BLOCK.
- **BAN-QA-023 — Shared seeded account.** Banned: journeys that log in as a shared demo or seed account and assert on its pre-staged data. Defeats: DET-FAKE-014. Bad: every test signs in as demo@example.com and asserts on the same fixture orders. Instead: provision a fresh, uniquely named account inside the test and assert only on data that test created. Severity: BLOCK.
- **BAN-QA-024 — Sleep synchronization.** Banned: fixed sleeps used to wait for the app to catch up before asserting state. Defeats: DET-FAKE-022. Bad: `await page.waitForTimeout(5000)` before asserting the "Synced" indicator, which passes while sync is actually broken. Instead: assert the indicator with a web-first assertion that auto-waits for the real state. Severity: BLOCK.
- **BAN-QA-025 — Assertion-free journey.** Banned: a journey that performs actions and asserts only that the page loaded or the success message appeared, never that a record exists. Defeats: DET-FAKE-015. Bad: the contact-form test submits, sees "Message sent," and passes while the form posts nowhere. Instead: assert the stored submission (admin view, API read, or second-account check) after the success message. Severity: BLOCK.

## Gates

- **G-QA-021 — Suite green on the preview deployment.** Verifies: QA-041, QA-045. Check: automated — CI runs `npx playwright test` against the preview URL as a required status check. Pass: exit code 0 with the build SHA and environment recorded on the run. Fail: block merge. Recorded in: progress.md.
- **G-QA-022 — Seeded-fault negative control.** Verifies: QA-046, QA-048. Check: automated — in a throwaway build, disable one covered submit handler (or change one assertion target's text) and run the matching journey. Pass: the journey exits non-zero; a green run against a seeded fault means the test cannot fail. Fail: block release and repair the test before any further e2e sign-off. Recorded in: progress.md.
- **G-QA-023 — Provider test-mode decline suite.** Verifies: QA-047. Check: automated — run the payment journey set with the provider's documented test and decline cards. Pass: exit code 0, every decline card produces a visible decline, and the order count is unchanged after each decline. Fail: block release of any payment-touching change. Recorded in: progress.md.
- **G-QA-024 — Sleep and selector lint.** Verifies: QA-042, QA-044. Check: automated — `grep -rEn "waitForTimeout|sleep\(" tests/e2e` and a selector scan for XPath/CSS locators in the same folder. Pass: both scans return zero matches (grep exit 1). Fail: block merge until the wait or locator is rewritten. Recorded in: progress.md.

## Anti-patterns

- **Ice-cream-cone drift.** The e2e count climbs every sprint while the unit layer stays flat, because UI tests feel like proof. Catch it: compare journey count against admission notes (QA-052) at each review; growth without notes is drift.
- **Mock-verified journeys.** The critical API is stubbed at the network layer, so the journey verifies the mocks and the real integration is never exercised end to end. Catch it: list stubbed routes per journey; a stub on the flow's own backend is a finding.
- **Full-suite-only green.** Tests pass in the full run but fail when executed individually — shared state is leaking between them. Catch it: run each new journey standalone before merge (QA-043 makes this a pass/fail fact, not a vibe).
- **Desktop-Chromium monoculture.** The suite is green on one viewport and one engine while the support matrix promises mobile widths and WebKit. Catch it: diff the CI browser/viewport matrix against the project's stated support matrix.

## Examples

- [Example 1 — The decline card is a journey, not an afterthought](examples/example-1.md) — corrects QA-047, BAN-QA-021.
- [Example 2 — Reload before you believe the toast](examples/example-2.md) — corrects QA-046, BAN-QA-022.
- [Example 3 — Replace the sleep with an assertion](examples/example-3.md) — corrects QA-042, BAN-QA-024.

## Recall anchors

- Few journeys, critical flows, real browsers.
- Never sleep; assert the state you actually need.
- Reload and re-read — the toast is not proof.
- The decline card declines, or the suite is lying.
- A test that cannot fail verifies nothing.

## Checklist

- [ ] Every journey names the revenue or risk it protects (QA-041).
- [ ] Sleep and selector lint returns zero matches (G-QA-024).
- [ ] Each journey passes standalone and in parallel (QA-043).
- [ ] Every mutation is followed by a reload and re-read (QA-046).
- [ ] Decline, invalid-input, and dead-dependency journeys exist for covered flows (QA-047).
- [ ] Seeded-fault control made its journey fail (G-QA-022).
- [ ] Failure artifacts (trace, screenshot, video) are uploaded from CI (QA-050).
- [ ] New journeys carry a lower-layer admission note (QA-052).
