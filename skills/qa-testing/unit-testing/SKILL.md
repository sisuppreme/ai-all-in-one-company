# unit-testing

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://www.martinfowler.com/articles/practical-test-pyramid.html
- **Depends on:** test-strategy
- **Feeds into:** qa-gates, integration-testing

## When to use / Do NOT use

- **Use when:** writing or reviewing tests for a single module, function, or class — pricing math, validation, parsing, state transitions, permission checks — that can be proven without a database, network, or browser.
- **Do NOT use when:** the behavior only exists across real collaborators (database, HTTP layer, another service) — use integration-testing; or across a full user journey — use e2e-testing. Do not stretch a unit test into either by mocking the collaborators away.

## Rules

1. **QA-001 — One test file per module, fast runner, first job.** Each module has a matching test file run by the stack's fast runner (Vitest, pytest, JUnit); the unit suite is the first CI job and finishes within the wall-time budget in TESTING.md.
2. **QA-002 — Every test asserts a specific expected value.** A test states the exact output, state, or side effect it expects. A test whose only assertion is "does not throw" is labeled a smoke test and never counts toward coverage of logic.
3. **QA-003 — Tests are isolated and order-independent.** Each test arranges its own inputs; no shared mutable fixtures, no reliance on another test's leftovers. The suite passes with tests shuffled and with any single test run alone.
4. **QA-004 — No real network, database, filesystem, or wall-clock.** Time and randomness are injected as parameters or fakes controlled by the test; a unit test that sleeps, reads the real clock, or opens a socket is defective.
5. **QA-005 — Assert behavior, not implementation.** Assert on return values and observable side effects, never on private internals or call-by-call mock choreography that a behavior-preserving refactor would break.
6. **QA-006 — Doubles live at the unit boundary only.** External collaborators (payment API, email sender) may be replaced by test doubles; the unit under test and the project's own modules are never doubled.
7. **QA-007 — A bug fix lands with its failing test.** The regression test is written first or in the same commit as the fix, so the bug is permanently pinned; a fix with no test is incomplete work.
8. **QA-008 — Coverage is a floor signal, not a target.** Coverage exists to expose untested code. Uncovered branches in money, auth, and data-loss paths are closed first; a coverage percentage is never reported as proof of quality on its own.
9. **QA-009 — The suite must be able to fail.** Mutating one assertion's expected value in a core module — or running a mutation-testing sample on core modules — must turn the suite red; a suite that stays green under mutation is reopened as a defect.
10. **QA-010 — Flaky unit tests are defects, not weather.** A test that passes on re-run without a code change is quarantined with an owner and expiry date, or fixed; silent retries that launder intermittency into green are not permitted at this layer.

## BAN list

- **BAN-QA-001 — Assertion-free coverage gaming.** Banned: a test that executes the code under test and asserts nothing (or only that no exception was thrown) while counting toward logic coverage. Defeats: DET-CODE-012. Bad: `test("totals", () => { cart.total(); });` — the frozen-fixture dashboard passes this test forever. Instead: assert the exact expected total for named inputs, e.g. `expect(cart.total()).toBe(4200)`. Severity: BLOCK.
- **BAN-QA-002 — Doubling the unit under test.** Banned: mocking or stubbing the module being tested, or a hand-written fake of the project's own logic, so the test verifies the double's canned answers. Defeats: DET-FAKE-008. Bad: search tests stub `search()` itself to return a fixed result list, then "verify" ranking. Instead: run the real unit; double only the external index client at the boundary. Severity: BLOCK.
- **BAN-QA-003 — Tautological fixture assertion.** Banned: asserting that the code returns the same hardcoded constant the implementation itself contains, so test and code can be wrong together. Defeats: DET-FAKE-014. Bad: implementation returns seed user `"admin@example.com"`; test asserts the return equals `"admin@example.com"` copied from the seed. Instead: compute the expectation independently in the test (from the rule or a worked example) and assert against that. Severity: BLOCK.
- **BAN-QA-004 — Disabling a failing test to go green.** Banned: `.skip`, `xit`, commented-out assertions, or a deleted test used to make the suite pass without a fix or a tracked quarantine (owner + expiry, per QA-010). Defeats: DET-FAKE-022. Bad: `test.skip("rejects expired token")` committed with the note "fix later," suite reported green. Instead: fix the code or the test; if neither is possible now, quarantine it as a tracked defect with an owner and expiry date, and report the suite as carrying a known failure. Severity: BLOCK.

## Gates

- **G-QA-001 — Seeded-fault (mutation) gate.** Verifies: QA-002, QA-009. Check: in CI, run `scripts/mutation-spotcheck.sh` — it flips one expected value in a core-module test (or runs the mutation sample), runs the unit suite, and requires a non-zero exit; it then restores the file and requires exit 0. Pass: suite exits non-zero under mutation and 0 after restore. Fail: block merge; the hollow test is a defect. Recorded in: progress.md.
- **G-QA-002 — Isolation and shuffle gate.** Verifies: QA-003. Check: CI runs the suite twice — `npm test -- --sequence.shuffle` (Vitest) / `pytest -p no:cacheprovider --random-order` equivalent for the stack — and once per test file in isolation; all runs must exit 0. Pass: every run exits 0. Fail: block merge; the order-dependent test is fixed, not re-run until green. Recorded in: progress.md.
- **G-QA-003 — Assertion-presence gate.** Verifies: QA-002. Check: CI runs `scripts/check-assertions.sh`, which scans unit test files and exits 1 if any test body contains no assertion call (`expect(`, `assert`, `should`) and is not labeled `smoke`. Pass: script exits 0. Fail: block merge until each flagged test asserts a specific value or is relabeled smoke. Recorded in: progress.md.
- **G-QA-004 — Wall-time budget gate.** Verifies: QA-001. Check: the CI unit job declares a timeout equal to the budget in TESTING.md (config inspection: `grep -n "timeout" .github/workflows/*.yml` shows the value); the platform kills and fails the job on breach. Pass: timeout present and the job completes inside it. Fail: block merge; slow tests are profiled and pushed down or fixed, never absorbed by raising the timeout without a TESTING.md change. Recorded in: progress.md.

## Anti-patterns

- **Snapshot everything.** Giant snapshots nobody reads, regenerated with `--update` whenever they fail — the diff is the test, and approving it unread deletes the test. Catch it: a snapshot update in a PR with no explanation of the intended change.
- **Test-name theater.** Names promise behavior the body never checks: `rejects expired token` that only exercises a valid token. Catch it: read the body against the name before reading the result.
- **Slow creep.** Unit tests quietly boot the framework, open connections, and load fixtures until the "fast" job takes twenty minutes and developers stop running it locally. Catch it: the suite's wall time trends up across releases while test count barely moves.
- **Copy-paste suites.** The same test block duplicated across modules, drifting apart until half the copies assert stale behavior. Catch it: near-identical test bodies in three or more files with different expectations.

## Examples

- [Example 1 — Assertion-free test becomes a real assertion](examples/example-1.md) — violates/corrects QA-002.
- [Example 2 — Shared mutable fixture becomes isolated arrange](examples/example-2.md) — violates/corrects QA-003.
- [Example 3 — Wall-clock dependency becomes injected time](examples/example-3.md) — violates/corrects QA-004.

## Recall anchors

- A test that cannot fail is decoration, not proof.
- Assert a value, not a vibe: exact expectation or it is a smoke test.
- Shuffle it, run it alone — isolation is part of the test.
- Double the boundary, never the unit.
- Coverage finds untested code; it never proves tested code is right.

## Checklist

- [ ] Every test asserts a specific expected value, or is labeled smoke (QA-002).
- [ ] Suite passes shuffled and with each test file run alone (QA-003, G-QA-002).
- [ ] No real network, database, filesystem, or wall-clock access in any unit test (QA-004).
- [ ] Doubles exist only at external boundaries; the unit under test runs for real (QA-006).
- [ ] Any bug fixed in this change has its failing test in the same commit (QA-007).
- [ ] Seeded-fault gate ran and the suite went red under mutation (G-QA-001).
- [ ] No skipped or disabled tests without a tracked owner and expiry date (QA-010).
