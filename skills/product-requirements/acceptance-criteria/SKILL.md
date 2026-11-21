# acceptance-criteria

## Metadata

- **Owner department:** D1 Product & Requirements (PR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Gherkin reference (Cucumber project; mirror of the official reference) — https://mirror.niser.ac.in/cran/web/packages/cucumber/vignettes/reference-gherkin.html ; Abstracta, "A Guide to Good Cucumber Practices" — https://abstracta.us/blog/testing-tools/a-guide-to-good-cucumber-practices
- **Depends on:** user-stories, requirements-writing
- **Feeds into:** user-stories, scope-control

## When to use / Do NOT use

- **Use when:** a story is being readied for build and its confirmation must be written; business rules (limits, seats, refunds, permissions) need scenarios that decide them explicitly, before code does.
- **Do NOT use when:** the story itself is not yet in template form (fix it in user-stories first) or the criteria would only restate the story — that is the failure this skill exists to prevent. Do not write criteria after the code to describe whatever was built.

## Rules

1. **PR-101 — Gherkin form.** Criteria are written as scenarios: Given a context, When one action or event, Then an observable outcome — in the customer's domain language.
2. **PR-102 — One behavior, one When.** Each scenario tests exactly one behavior and contains exactly one When. Two Whens means two scenarios.
3. **PR-103 — Observable Thens only.** Every Then states an outcome a test can pass or fail. Adjectives ("works correctly", "is fast", "looks fine") are rejected at review on sight.
4. **PR-104 — Failure cases are mandatory.** Every business rule named in the story gets at least one scenario, including its failure case: boundary values, empty or none cases, duplicates, and permission failures.
5. **PR-105 — Declarative, not imperative.** Scenarios state the rule that holds, not the clicks that get there. UI mechanics appear only when the mechanic itself is the rule.
6. **PR-106 — Customer language and canonical names.** Scenarios use the customer's domain terms, and entity, plan, and product names match the fact sheet exactly.
7. **PR-107 — Written before build, together.** Criteria are drafted by product, engineering, and QA together before build starts. Criteria written after the code are a defect, not documentation.
8. **PR-108 — Frozen per iteration.** Criteria are frozen once the iteration starts. A change re-opens the story for re-estimation instead of being absorbed silently.
9. **PR-109 — Executable or checklist, never dropped.** Scenarios run in the project's BDD suite where one exists. Where none exists, they run as a signed manual checklist with the same pass/fail discipline — executor and date recorded per scenario.
10. **PR-110 — Total coverage for Must stories.** Every Must-priority story in a release maps to at least one passing scenario before the release ships.
11. **PR-111 — Undefined steps fail.** A scenario referencing a step with no definition fails the suite. It is never skipped or left marked pending at release time.

## BAN list

- **BAN-PR-051 — Criteria copied from the story.** Banned: acceptance criteria that restate the story text as their own test. Defeats: DET-CON-028. Bad: AC for the export story reads "The export works as described in the story." Instead: a scenario with a stated context, one action, and the observable file contents the export must produce. Severity: BLOCK.
- **BAN-PR-052 — Happy-path only.** Banned: a scenario set with no failure case for a rule involving limits, money, or permissions. Defeats: DET-CON-028. Bad: the seat-limit story is tested only at 4 of 5 seats used, so the refusal behavior is decided by the code. Instead: add the boundary scenario at 5 of 5 and the refusal scenario at 6. Severity: BLOCK.
- **BAN-PR-053 — The adjective Then.** Banned: a Then clause whose assertion is an adjective or an unmeasured quality. Defeats: DET-CON-028. Bad: "Then the page loads quickly and looks clean." Instead: "Then the results render within 2.0 seconds for a 500-row dataset, with the totals row visible above the fold." Severity: BLOCK.
- **BAN-PR-054 — The unpriced money rule.** Banned: acceptance criteria for a billing story that never assert the amount charged equals the amount displayed. Defeats: DET-CON-016. Bad: the upgrade scenario checks "plan changes to Pro" but never the prorated charge, and checkout later bills a different figure than the pricing page showed. Instead: the Then states the exact charge, the proration basis, and the entitlement change. Severity: BLOCK.

## Gates

- **G-PR-051 — BDD suite run.** Verifies: PR-110, PR-111. Check: automated — run the project's BDD suite (Cucumber or the stack's equivalent): every Must story in the release maps to at least one passing scenario, and the suite is configured to fail on undefined steps. Pass: 100% of Must stories mapped and green. Fail: block the release. Recorded in: progress.md.
- **G-PR-052 — Gherkin lint.** Verifies: PR-102, PR-103. Check: automated — lint all scenario files: exactly one When per scenario; every Then contains an observable assertion (a number, a state, a message, or a file condition); adjective-only Thens are flagged from the banned-term list. Pass: zero violations. Fail: block story sign-off. Recorded in: progress.md.
- **G-PR-053 — Failure-case coverage.** Verifies: PR-104. Check: manual — for each business rule in the release's stories, list its failure scenario; rules touching money, limits, or permissions must each have one. Pass: 100% of such rules covered. Fail: block build start for the uncovered story. Recorded in: progress.md.
- **G-PR-054 — Checklist degradation check.** Verifies: PR-109. Check: manual — for projects with no BDD runner, confirm the signed checklist exists, names an executor and a date per scenario, and records pass or fail per scenario for this release. Pass: a complete checklist covers every scenario in the release. Fail: block the release. Recorded in: progress.md.

## Anti-patterns

- **Scenario sprawl.** Thirty scenarios per story, most duplicating one rule with trivial variations. Catch it: group scenarios by the rule they test; duplicates beyond boundary values are noise that hides the missing failure case.
- **Implementation narration.** Scenarios that read like test scripts ("click the blue button, then the modal opens, then…"). Catch it: if a redesign would break the wording but not the rule, the scenario was written imperatively — rewrite it declaratively.
- **Retro-fitted criteria.** Scenarios written to match what the code already does, including its bugs. Catch it: compare criteria dates against build dates; criteria must predate the code they confirm (PR-107).
- **Pending-step parking.** Failing or unwritten scenarios parked as "pending" indefinitely so the suite stays green. Catch it: count pending steps at release; the count must be zero (PR-111).

## Examples

- [Example 1 — From story-copy criteria to a real scenario](examples/example-1.md) — corrects PR-101.
- [Example 2 — Boundary and failure scenarios for a seat limit](examples/example-2.md) — corrects PR-104.
- [Example 3 — Rewriting an imperative scenario declaratively](examples/example-3.md) — corrects PR-105.

## Recall anchors

- Given, When, Then — one When, one behavior.
- If a test cannot fail it, the Then is wrong.
- Every rule gets its failure case.
- Behavior, not buttons.
- Criteria are written before build and frozen for the iteration.

## Checklist

- [ ] Every scenario has exactly one When (G-PR-052).
- [ ] Every Then asserts an observable outcome (PR-103).
- [ ] Every money, limit, or permission rule has a failure scenario (G-PR-053).
- [ ] Criteria were drafted before build, with product, engineering, and QA (PR-107).
- [ ] The BDD suite is green with zero undefined or pending steps (G-PR-051), or the signed checklist is complete (G-PR-054).
- [ ] Every Must story in the release maps to a passing scenario (PR-110).
- [ ] Entity and plan names match the fact sheet exactly (PR-106).
