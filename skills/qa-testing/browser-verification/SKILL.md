# browser-verification

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Playwright, "Best Practices" — https://playwright.dev/docs/best-practices ; DET-FAKE parameters, "How to run the check" (persistence + network tests) — skills/detection/fake/PARAMETERS.md
- **Depends on:** test-data
- **Feeds into:** qa-gates, bug-triage, visual-regression

## When to use / Do NOT use

- **Use when:** a build is about to be called done — release candidate, preview deployment, or production change — and someone must establish what a user actually meets: pages render clean, and every interactive claim survives the persistence and network tests in a real browser.
- **Do NOT use when:** the check belongs in the committed test suite (e2e-testing owns repeatable journeys) or is a static source scan (placeholder-scan owns that). This skill is the live, rendered-truth pass on the deployed artifact, not a substitute for either.

## Rules

1. **QA-061 — Verify the deployed artifact.** The pass runs against the preview deployment or production URL, never the dev server. The URL, build SHA, and environment are recorded at the top of the results; a result without them is not a result.
2. **QA-062 — Evidence per claim.** Every probed claim produces filed evidence — screenshot, network capture, or before/after values. A bare "looks fine" is not evidence and is never recorded as a pass.
3. **QA-063 — Errors are findings by default.** A console error or a failed (4xx/5xx) request on any loaded page is a finding. Whitelisting one requires a written reason filed with the results.
4. **QA-064 — Fresh accounts only.** Probes run on accounts created for this pass. A curated demo account is never used: staged content and seed data cannot hide behind it.
5. **QA-065 — Persistence test, every interactive feature.** Perform the action, reload the page, sign out and back in, then open the app in a second browser or account. The claimed effect must still be there and must be yours.
6. **QA-066 — Network test, every write.** Repeat each write action with the network tab open. A real write fires a server request, and the next read returns the changed state. No request, or a response the UI ignores, means the feature is simulated.
7. **QA-067 — Probe with novel inputs.** Search, filters, and AI features are probed with inputs the builder never saw: a gibberish string, a unique marker value created seconds earlier. Canned results cannot answer a novel probe; if they appear to, the feature is fake.
8. **QA-068 — Match the support matrix.** Viewports and browsers come from the project's stated support matrix. A desktop-width-only pass is recorded as exactly that, never as a full pass.
9. **QA-069 — Verify state changes on a second surface.** A delete is confirmed where the record should now be absent; an upload is confirmed by retrieving the file back; an admin save is confirmed from the surface that consumes it. The acting screen's own confirmation proves nothing.
10. **QA-070 — Run the negative probes.** A deliberately wrong password must fail, an invalid form must error, a decline path must decline. A pass that never tried to fail has verified only the happy path.
11. **QA-071 — Load every route.** Every route in the sitemap or route list is loaded at least once during the pass, including error, empty, and settings states — not only the pages the builder suggested.
12. **QA-072 — Verdicts are filed, not chatted.** Each interactive feature gets a recorded verdict (real / fake / blocked) with its evidence in progress.md. A fake verdict is filed as a defect the same day, naming the DET-FAKE parameter it matches.

## BAN list

- **BAN-QA-031 — The "looks fine" verdict.** Banned: declaring a feature verified because its page renders and its controls respond visually, without running the persistence and network tests. Defeats: DET-FAKE-010. Bad: the admin settings page toggles, shows "Saved", and is signed off — nothing was ever written to the server. Instead: perform the save, reload, sign out and back in, and confirm the value on the surface that consumes it, with the network capture filed. Severity: BLOCK.
- **BAN-QA-032 — Verifying on the demo account.** Banned: running probes on the seeded or curated demo account the builder prepared. Defeats: DET-FAKE-014. Bad: the demo account's dashboard is full of activity, so the product "works" — a fresh account sees an empty shell whose counters never move. Instead: create fresh accounts for the pass and probe with those. Severity: BLOCK.
- **BAN-QA-033 — Toast-as-proof.** Banned: recording an edit as saved because a success toast or banner appeared, without a reload and re-read. Defeats: DET-FAKE-016. Bad: "Profile updated ✓" is screenshotted as evidence; after reload the old values are back, because the toast fired from local state. Instead: reload, sign out and back in, and file the before/after values from the re-read. Severity: BLOCK.
- **BAN-QA-034 — The demo-script probe.** Banned: probing search or an AI feature using only the example queries printed in the UI or the demo script. Defeats: DET-FAKE-008. Bad: typing the suggested query returns polished results, so search is passed — the same results return for any input, including gibberish. Instead: probe with a gibberish string and a unique marker created during the pass; the results must track the input. Severity: BLOCK.
- **BAN-QA-035 — Silent error whitelisting.** Banned: dismissing console errors or failed requests during the pass as "known noise" with no written reason filed. Defeats: DET-FAKE-022. Bad: every save fires a 500 that the UI hides behind a "Synced" indicator; the pass notes "some console noise" and ships it. Instead: file each error as a finding, or attach the written reason it is harmless. Severity: WARN.

## Gates

- **G-QA-031 — Route smoke pass.** Verifies: QA-063, QA-071. Check: automated — `npx playwright test smoke/routes.spec.ts` loads every route in the project's route list and fails on any console error, any response ≥400, or a blank render; the command's exit code is the verdict. Pass: exit 0 with the route count matching the route list. Fail: block the release; each failure is filed as a finding. Recorded in: progress.md.
- **G-QA-032 — Two-test protocol record.** Verifies: QA-062, QA-065, QA-066. Check: automated — a script counts the interactive features on the release checklist and greps the verification log in progress.md for a persistence-test and network-test entry with an evidence link for each; exit non-zero on any gap. Pass: one complete entry per feature. Fail: block the release until the missing probes are run and recorded. Recorded in: progress.md.
- **G-QA-033 — Seeded-fake negative control.** Verifies: QA-065, QA-066, QA-067. Check: automated — in a throwaway build, one write endpoint is stubbed to return success without persisting; the probe script is run against it and must exit non-zero and name the feature as fake. Pass: the seeded fake is caught. Fail: the verification procedure itself fails — no release verdict from this pass is trusted until the probe is fixed and the control passes. Recorded in: progress.md.
- **G-QA-034 — Pass header and matrix coverage.** Verifies: QA-061, QA-064, QA-068. Check: automated — a script confirms the results record names the URL, build SHA, environment, and the fresh account IDs used, and that the viewport/browser list matches the project's support matrix file. Pass: all fields present and the matrix fully covered. Fail: the pass is recorded as partial, naming the uncovered cells; a partial pass does not clear a release. Recorded in: progress.md.

## Anti-patterns

- **The happy-path stroll.** The pass clicks through the golden path only — valid login, valid form, suggested query — and never tries a wrong password, an empty state, or a decline. Catch it: the probe list contains no negative case; QA-070 exists because this stroll is the default.
- **Retry until green.** A probe that fails intermittently is re-run until it passes, and the pass is what gets recorded. Catch it: the results show one attempt per probe and no failure history; intermittency is a finding, not a nuisance to launder.
- **Evidence evaporation.** Screenshots and captures are taken during the pass but never filed; a week later the verdict exists only in chat scrollback. Catch it: every verdict in progress.md must resolve to an evidence link that still opens.
- **Viewport tunnel vision.** The pass runs at one desktop width and is reported as "verified". Catch it: compare the results' viewport list against the support matrix before accepting the verdict (G-QA-034 automates this).

## Examples

- [Example 1 — A profile edit that only existed in local state](examples/example-1.md) — corrects QA-065, QA-066.
- [Example 2 — Search that answered everything with the same results](examples/example-2.md) — corrects QA-067.
- [Example 3 — A route nobody clicked that was broken](examples/example-3.md) — corrects QA-063, QA-071.

## Recall anchors

- Rendered is not verified — probe the claim.
- Reload, re-login, second browser: the effect must survive all three.
- No request, no write; toast is not proof.
- Fresh accounts, novel inputs — never the demo script.
- Errors are findings until a written reason says otherwise.

## Checklist

- [ ] Results record names URL, build SHA, environment, and fresh account IDs (G-QA-034).
- [ ] Route smoke pass exits 0 across the full route list (G-QA-031).
- [ ] Every interactive feature has a persistence-test and network-test entry with evidence (G-QA-032).
- [ ] Negative probes run: wrong password, invalid form, decline path (QA-070).
- [ ] Search/AI features probed with gibberish and a unique marker (QA-067).
- [ ] Seeded-fake negative control caught by the probe script (G-QA-033).
- [ ] Viewport/browser coverage matches the support matrix, or the pass is recorded as partial (QA-068).
- [ ] Every fake verdict filed as a defect naming its DET-FAKE parameter (QA-072).
