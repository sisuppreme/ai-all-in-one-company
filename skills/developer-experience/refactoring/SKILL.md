# refactoring

## Metadata

- **Owner department:** D15 Developer Experience (DX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://martinfowler.com/articles/workflowsOfRefactoring/fallback.html ; https://deepwiki.com/gmoral/Books/7.3-refactoring:-improving-the-design-of-existing-code
- **Depends on:** none — standalone: restructuring decisions are made from the code under change itself, read directly, with behavior pinned by the project's existing tests; no other skill's output is an input. It feeds legacy-migration and tech-debt.
- **Feeds into:** legacy-migration, tech-debt

## When to use / Do NOT use

- **Use when:** code must be restructured — duplication removed, names clarified, a function decomposed, coupling reduced — to make a coming feature or fix easy, or while reading unfamiliar code (comprehension refactoring); the work changes internal structure only.
- **Do NOT use when:** observable behavior must change (that is a feature or fix change, committed separately), a whole system or module is being replaced (use legacy-migration), or the goal is measurable performance improvement (benchmarked performance work, its own change type).
- **Cross-reference:** the commented-out-code pattern banned here as BAN-DX-054 is also banned as standing debt in tech-debt (BAN-DX-042); the two entries cover the same pattern in different moments.

## Rules

1. **DX-101 — Behavior is the contract.** A refactoring leaves observable behavior identical: same outputs, API responses, persisted data, side effects, and error behavior for every input. Any change that alters observable behavior is not a refactoring — it is reclassified, renamed, and reviewed as the feature, fix, or rewrite it actually is.
2. **DX-102 — Safety net before structure.** The full relevant test suite is run and green before the first structural step. Where the area lacks tests, the first step is characterization tests that pin current behavior — including its quirks — and they land in their own preceding commit before any restructuring begins.
3. **DX-103 — Two hats, never both.** While refactoring, no features are added and no bugs are fixed; while adding features, no opportunistic restructuring is folded in. Switching hats is explicit: the refactoring commits and the behavior commits are separate, so each can be reviewed and reverted on its own.
4. **DX-104 — Small, named steps.** Each step is one named transformation from the refactoring catalog (Extract Function, Inline Variable, Change Function Declaration, Rename, Move, …), small enough that the suite runs between steps. A step too big to describe with one catalog name is split before it is committed.
5. **DX-105 — Red means stop and back up.** If the suite goes red mid-refactoring, work stops and the last step is undone or corrected; the suite is never pushed through, and the failure is never "fixed" by adjusting the code's behavior or the test. Two consecutive red steps mean the step size is too large — halve it.
6. **DX-106 — Tests are read-only during a refactoring.** No test file is added to, edited, or deleted inside a refactoring change (characterization tests under DX-102 land before it, separately). A test that appears to need changing is evidence the change alters behavior: stop and reclassify under DX-101.
7. **DX-107 — Refactor toward a named pressure.** Every refactoring change states the design pressure it answers — duplication, coupling, unclear names, runaway complexity — in its description. "Cleaner," "nicer," or "more modern" is not a pressure and does not justify a change.
8. **DX-108 — Rule of Three for abstractions.** A shared abstraction is extracted only when the same logic or shape appears for the third time. The first occurrence is written plainly; the second is duplicated deliberately and noted; the third triggers the extraction.
9. **DX-109 — The public surface does not move.** Exported symbols, API routes, and contracts are byte-identical before and after a refactoring. A change that must alter the public surface uses legacy-migration techniques (branch by abstraction, parallel change), not a refactoring commit.
10. **DX-110 — Preparatory refactoring precedes the feature.** When a feature is hard to add because of the code's shape, the order is: first make the change easy (refactoring commits, suite green), then make the easy change (feature commits). The two phases are never interleaved in one commit.
11. **DX-111 — Performance work is not refactoring.** An optimization changes a measurable quality, so it is benchmarked before and after, states its target metric, and is labeled as its own change type. It is never smuggled in under a "refactor" label, where its behavior risk would escape review.
12. **DX-112 — Replaced code is deleted in the same change.** Once an extraction or move lands, the superseded implementation is deleted — not commented out, not kept "just in case." Version control is the archive; anything worth remembering about the old shape goes to the changelog or decision log.

## BAN list

- **BAN-DX-051 — Tests edited to fit the refactor.** Banned: modifying, weakening, or deleting a test inside a refactoring change so the suite passes against restructured code. Defeats: DET-CODE-012. Bad: the extracted pricing function rounds differently, so the assertion is relaxed from `toBe(19.99)` to `toBeCloseTo(20)` and the PR is labeled "refactor." Instead: the failing test is proof of a behavior change — restore the exact behavior, or split the rounding change out as its own fix commit with its own test change (DX-101, DX-106). Severity: BLOCK.
- **BAN-DX-052 — Big-bang rewrite committed as a "refactor."** Banned: replacing a module in one unreviewable diff — hundreds of lines changed at once — under a refactoring label. Defeats: DET-CODE-031. Bad: a 900-line PR titled "refactor checkout" rewrites the module wholesale; no reviewer can separate structure from behavior, and revert means losing everything. Instead: decompose the work into named catalog steps, one commit each, suite green between steps; if the module truly needs replacement, run it as legacy-migration (DX-104). Severity: BLOCK.
- **BAN-DX-053 — Speculative abstraction for a single use.** Banned: extracting a generic framework, strategy layer, or configuration-driven engine around logic that exists exactly once, "for future flexibility." Defeats: DET-CODE-015. Bad: one discount calculation is wrapped in a `RuleEngine` with pluggable strategies because "other discount types are coming." Instead: write the single case plainly; extract only at the third real occurrence (DX-108). Severity: WARN.
- **BAN-DX-054 — Old implementation left commented out.** Banned: keeping the superseded code as a commented block above or below its replacement "in case we need it." Defeats: DET-CODE-010. Bad: 70 lines of the old tax function sit commented out over the new one for two releases, rotting against APIs that no longer exist. Instead: delete it in the same change — git history recovers it exactly — and note the replacement in the changelog (DX-112). Severity: BLOCK.
- **BAN-DX-055 — Restructuring untested code with no net.** Banned: beginning structural changes in an area with no test coverage and no characterization tests, on the strength of reading the code carefully. Defeats: DET-CODE-013. Bad: the legacy billing module has zero tests; the agent restructures it over a day and reports "behavior preserved" because nothing visibly broke in manual spot-checks. Instead: pin current behavior with characterization tests first, in their own commit, then refactor under them (DX-102). Severity: BLOCK.

## Gates

- **G-DX-051 — Suite-green invariant (automated).** Verifies: DX-101, DX-102, DX-105. Check: run the project's full test suite on the base commit and on the refactoring branch (`<test-command>` per stack.md, e.g. `npm test`); compare results, and list modified test files: `git diff --name-only <base>...HEAD -- '*test*' '*spec*' 'tests/'`. Pass: identical pass/fail sets on both runs and zero test files modified. Fail: block shipment; the change is reclassified or the behavior restored. Recorded in: progress.md.
- **G-DX-052 — Public surface diff (automated).** Verifies: DX-109. Check: diff the exported surface between base and branch — for a library, the generated type/symbol listing; for an API, the OpenAPI contract (`git diff <base>...HEAD -- openapi.yaml` or the project's contract snapshot). Pass: the surface diff is empty. Fail: block shipment; move the surface change to legacy-migration (branch by abstraction / parallel change). Recorded in: progress.md.
- **G-DX-053 — Commit separation audit (automated).** Verifies: DX-103, DX-110. Check: `git log --format='%h %s' <base>..HEAD` — every commit in the change is a single-type change (`refactor:` commits contain no behavior change; no `feat:`/`fix:` commit is interleaved inside the refactoring range), and per-commit size stays reviewable: `git diff --stat <base>...HEAD` shows no single commit rewriting a whole module. Pass: clean separation, no mixed commits. Fail: block shipment; split the commits and resubmit. Recorded in: progress.md.
- **G-DX-054 — Characterization-first ordering (automated).** Verifies: DX-102. Check: for any module the change restructures that lacked coverage at base, `git log --format='%h %s' --reverse <base>..HEAD -- <module>` shows a test-only commit adding characterization tests for that module before the first structural commit touching it. Pass: ordering holds for every previously untested module. Fail: block shipment; write and land the characterization tests first. Recorded in: progress.md.
- **G-DX-055 — Deletion and step review (manual).** Verifies: DX-104, DX-112. Check: read the full diff; confirm each commit maps to one named catalog transformation, every superseded implementation is deleted (search the diff and the resulting files for large commented-out blocks), and the change description names the design pressure answered (DX-107). Pass: all three confirmed. Fail: warn once; on repeat, block shipment and split or complete the deletion. Recorded in: progress.md.

## Anti-patterns

- **Boy-scout sprawl.** "Leave it cleaner than you found it" applied to every file a feature happens to touch, until a two-file feature ships as a forty-file diff nobody can review. Catch it by counting files outside the change's stated scope before committing — sprawl is visible in `git status`, not in intentions.
- **Perpetual preparation.** Preparatory refactoring that never arrives at the feature: the code is made "easy to change" week after week while the change itself is never made. Catch it by checking the plan — if a preparatory phase has no feature commit scheduled directly after it, the preparation is the project, and it stops.
- **Rename churn.** Names changed to match personal taste, then changed again next quarter by the next reader, generating history noise and merge conflicts with zero comprehension gain. Catch it by asking what a new reader would misunderstand about the current name; if the answer is "nothing," the rename is churn.
- **Refactoring during a freeze.** Structural work started while a release is stabilizing or an incident is open, when every diff should be minimal and behavior-focused. Catch it on the calendar, not in the code: if the team is in freeze or firefighting, the refactoring waits.

## Examples

- [Example 1 — Extract Function under a green suite](examples/example-1.md) — violates/corrects DX-104, DX-102.
- [Example 2 — The behavior change hiding in a "refactor"](examples/example-2.md) — violates/corrects DX-101, DX-103, DX-106.
- [Example 3 — Characterization tests before touching legacy billing](examples/example-3.md) — violates/corrects DX-102.

## Recall anchors

- Refactoring changes structure, never behavior — anything else gets a new name.
- No net, no refactoring: characterization tests come first.
- Two hats: never refactor and change behavior in the same commit.
- Red suite means back up one step — never push through, never edit the test.
- Extract at the third occurrence, delete the old code in the same change.

## Checklist

- [ ] Full suite was green on the base commit before the first structural step (DX-102, G-DX-051).
- [ ] Previously untested areas got characterization tests in a preceding, separate commit (DX-102, G-DX-054).
- [ ] No test file is modified anywhere in this change (DX-106, G-DX-051).
- [ ] Every commit is a single named transformation; no feature or fix is mixed in (DX-103, DX-104, G-DX-053).
- [ ] Public surface diff (symbols / OpenAPI) is empty (DX-109, G-DX-052).
- [ ] The change description names the design pressure answered (DX-107).
- [ ] No abstraction was extracted before its third occurrence (DX-108).
- [ ] All superseded code is deleted, none commented out (DX-112, G-DX-055).
- [ ] Suite result after the change matches the base run exactly, recorded in progress.md (G-DX-051).
