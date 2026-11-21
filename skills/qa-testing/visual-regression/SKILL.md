# visual-regression

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://playwright.dev/docs/test-snapshots
- **Depends on:** test-strategy, browser-verification
- **Feeds into:** qa-gates

## When to use / Do NOT use

- **Use when:** a project has pages or component states where layout is the product — marketing pages, dashboards, checkout, email-critical screens — and layout drift must fail a pull request mechanically.
- **Do NOT use when:** the check is behavioral rather than visual (use e2e-testing or browser-verification), or the surface is a native app or canvas game with no stable rendered layout (use manual review and record why in TESTING.md).

## Rules

1. **QA-081 — Pinned environment.** Baselines are generated and compared inside one pinned environment — same container image, browser build, and font set — and the image digest and browser version are recorded in the test config. A baseline produced on a developer machine is invalid.
2. **QA-082 — Baselines change only by reviewed PR.** A baseline file changes only in a pull request whose description names the intentional design change it accepts. Regenerating baselines inside a feature PR without that statement is a process violation, however green it makes the run.
3. **QA-083 — Coverage by inventory.** Every template in the page/state inventory carries at least three screenshots: default, empty, and error state. The inventory comes from the design system, not from which pages someone remembered.
4. **QA-084 — Mask dynamics, never widen tolerance.** Timestamps, avatars, ads, and other dynamic regions are masked in the test that captures them. The global pixel threshold stays at the small value set in TESTING.md; raising it requires a waiver recorded per qa-gates.
5. **QA-085 — Animations frozen.** Screenshot tests run with animations disabled (`animations: "disabled"` in the screenshot assertion), so motion can never become flake.
6. **QA-086 — Diff artifact before re-run.** A failing comparison uploads the expected, actual, and diff images as CI artifacts. Triage opens the diff image first; re-running the job before reading the diff is not triage.
7. **QA-087 — Viewports match the support matrix.** The screenshot set covers every viewport class in the project's support matrix, including one mobile width; a desktop-only suite is reported as desktop-only coverage.
8. **QA-088 — Seeded-change negative control.** On a schedule, a throwaway branch shifts a header by 20px and the visual job must fail with a diff artifact. A job that passes the seeded change is itself a defect and blocks release until fixed.
9. **QA-089 — Baseline-drift report per release.** Each release produces a count of baselines changed since the previous release tag. Mass changes with no matching design-change statement block the release.
10. **QA-090 — Environment changes are single events.** A font or browser-version upgrade is one deliberate, repo-wide baseline regeneration in its own PR — never a per-test fix scattered across feature PRs.
11. **QA-091 — Compare the built artifact.** Comparisons run in CI against the pull request's built application, with the build SHA recorded beside the results — never against a locally rendered dev server.
12. **QA-092 — Quarantine expires.** A screenshot test that flakes twice in a week is quarantined with a ticket and an expiry date, and the quarantine count is reported per release. Deleting the test or silently retrying it away is forbidden.

## BAN list

- **BAN-QA-041 — Baseline regeneration to green.** Banned: running the update-snapshots command to make a red visual run pass without a reviewed PR naming the design change. Defeats: DET-VIS-007. Bad: a spacing regression ships because the developer regenerated baselines in the same PR and the diff was never seen. Instead: keep the failure, open a baseline-only PR whose description states the intentional change, and let a reviewer read the diff images. Severity: BLOCK.
- **BAN-QA-042 — Threshold inflation.** Banned: raising the global pixel threshold or diff ratio to absorb failures instead of masking the dynamic region causing them. Defeats: DET-VIS-001. Bad: `maxDiffPixelRatio` raised to 0.25 so a timestamp stops failing — and a 12px padding collapse now passes too. Instead: mask the timestamp element in that one test and return the threshold to the value in TESTING.md. Severity: BLOCK.
- **BAN-QA-043 — Desktop-only coverage.** Banned: a visual suite whose viewports are all desktop widths while the support matrix includes mobile. Defeats: DET-VIS-038. Bad: the suite is green for months while the pricing table overflows horizontally on a 390px phone. Instead: add the mobile viewport from the support matrix to every inventory template's screenshot set. Severity: BLOCK.
- **BAN-QA-044 — Live-animation screenshots.** Banned: capturing screenshots while CSS animations or transitions run, so pass/fail depends on frame timing. Defeats: DET-VIS-040. Bad: the hero test flakes every few runs because the fade-up animation is mid-flight in half the captures. Instead: set `animations: "disabled"` on the screenshot assertion so every capture is the settled frame. Severity: BLOCK.
- **BAN-QA-045 — Default-state-only coverage.** Banned: screenshotting only the populated default state of a template, with no empty or error state. Defeats: DET-VIS-032. Bad: the dashboard's empty state renders its heading overlapped by the CTA, and no baseline exists to catch it. Instead: add the empty and error states from the inventory to the screenshot set before merging the template. Severity: BLOCK.

## Gates

- **G-QA-041 — Visual suite exit code.** Verifies: QA-081, QA-083, QA-085, QA-087. Check: `npx playwright test --grep @visual` in the pinned CI image. Pass: exit code 0 and the run report lists every inventory template with its default, empty, and error screenshots. Fail: block merge. Recorded in: progress.md.
- **G-QA-042 — Seeded-change control.** Verifies: QA-088. Check: the scheduled job applies a 20px header shift on a throwaway branch, runs `npx playwright test --grep @visual`, and asserts a non-zero exit plus a diff image in the artifacts. Pass: job fails as designed and the artifact exists. Fail: block release; the visual suite is treated as non-functional. Recorded in: progress.md.
- **G-QA-043 — Baseline-drift gate.** Verifies: QA-082, QA-089. Check: `git diff --name-only <last-release-tag>..HEAD -- '*-snapshots'` counts changed baselines; the release checklist requires a design-change statement for the count. Pass: every changed baseline traces to a reviewed baseline PR. Fail: block release. Recorded in: progress.md.
- **G-QA-044 — Threshold config audit.** Verifies: QA-084. Check: `grep -Rn "maxDiffPixelRatio" --include="*.ts" .` and compare each value against the cap in TESTING.md. Pass: no value exceeds the cap and no per-test threshold overrides exist without a waiver reference. Fail: block merge. Recorded in: progress.md.

## Anti-patterns

- **Bulk diff approval.** Approving a stack of baseline changes from thumbnail previews without opening a single full-size diff image; catch it by sampling three diffs at full size before approving any baseline PR.
- **Retry-as-fix.** Letting CI retries absorb a flaky screenshot test until the quarantine rule (QA-092) never triggers; catch it by reading first-attempt results, not final status, in the weekly flake count.
- **Stale baseline hoarding.** Baselines for deleted pages and renamed components still sitting in the repo, inflating drift counts and hiding real changes; catch it in the per-release drift report by listing baselines whose routes no longer exist.
- **Marketing-page tourism.** Forty screenshots of the landing page and none of the settings, billing, or error surfaces users actually hit; catch it by diffing the screenshot list against the page/state inventory, not against page traffic.

## Examples

- [Example 1 — Baseline regeneration to green](examples/example-1.md) — violates/corrects QA-082.
- [Example 2 — Threshold raised instead of masking](examples/example-2.md) — violates/corrects QA-084.
- [Example 3 — Desktop-only suite misses mobile overflow](examples/example-3.md) — violates/corrects QA-087.

## Recall anchors

- Baselines are reviewed diffs, not generated files.
- Mask the dynamic region; never widen the threshold.
- If a 20px shift passes, the suite is broken, not the page.
- Triage reads the diff image before anyone re-runs anything.
- A font or browser bump is one baseline event, not fifty fixes.

## Checklist

- [ ] Baselines were generated inside the pinned CI image, with its digest recorded (QA-081).
- [ ] Every baseline change sits in a reviewed PR naming the intentional design change (QA-082).
- [ ] Default, empty, and error states exist for every inventory template (QA-083).
- [ ] Dynamic regions are masked and the global threshold matches TESTING.md (QA-084).
- [ ] Animations are disabled in every screenshot assertion (QA-085).
- [ ] The latest seeded-change control failed the job and produced a diff artifact (QA-088).
- [ ] The release baseline-drift count is produced and explained (QA-089).
- [ ] No quarantined visual test is past its expiry date (QA-092).
