# test-strategy

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://www.martinfowler.com/articles/practical-test-pyramid.html
- **Depends on:** none (consumes the project's acceptance criteria from D1)
- **Feeds into:** unit-testing, integration-testing, e2e-testing, browser-verification, visual-regression, accessibility-testing, load-testing, chaos-testing, contract-testing, security-testing, qa-gates, test-data, bug-triage, placeholder-scan

## When to use / Do NOT use

- **Use when:** starting a project, before any test suite is written; when the architecture changes materially; when a new test type is proposed; at each release, for the strategy-to-suite audit.
- **Do NOT use when:** writing or fixing an individual suite (use that layer's skill, executing against this strategy); setting merge-gate wiring or thresholds (qa-gates — this skill decides what must be proven, qa-gates wires the proof into CI).

## Rules

1. **QA-201 — One strategy document.** The strategy lives in TESTING.md at the repo root, is committed before the suites grow, and is the single place that names layers, environments, and budgets; a strategy that lives in a slide deck, wiki, or chat thread does not exist.
2. **QA-202 — Pyramid allocation in numbers.** TESTING.md states the target count or share per layer (unit / integration / e2e) and a wall-clock runtime budget per layer; "mostly unit tests" without numbers fails this rule.
3. **QA-203 — Every acceptance class maps to a layer.** Each requirement class in the project's acceptance criteria names at least one test layer that can catch its failure; a class with no layer is moved to the Accepted Risks section (QA-204), never left unmapped.
4. **QA-204 — Exclusions are written, with reasons.** TESTING.md carries an explicit Not Tested / Accepted Risks section: each entry names what is not tested, why, and who accepted the risk; silence is a gap, a written exclusion is a decision.
5. **QA-205 — E2E admission is earned.** A flow earns an e2e test by revenue or risk (signup, login, the core transaction, the top admin action); the PR adding one names the lower layer that cannot cover the case, or the test is pushed down the pyramid.
6. **QA-206 — Quality attributes are assigned, not assumed.** Visual, accessibility, load, chaos, contract, and security testing each appear in TESTING.md with an owning D8 skill, the environment they run in, and their cadence (per-PR, nightly, per-release); an attribute with no owner is untested by definition.
7. **QA-207 — Environment and cadence matrix.** TESTING.md states where each layer runs — local, CI per-PR, merge/nightly, or release pipeline; expensive gates (full-browser e2e, load, chaos) are scheduled explicitly, and "nightly" entries name the job that runs them so they cannot silently become "never."
8. **QA-208 — Flake budget is a number.** TESTING.md sets a maximum flake rate per suite; a flaky test is quarantined only as a tracked state with a named owner and an expiry date recorded in the strategy's quarantine list.
9. **QA-209 — Thresholds trace to a source document.** Every numeric threshold in the strategy (latency percentiles, error rates, Core Web Vitals budgets) cites the budget or SLO document it comes from; loosening a threshold is a reviewed change to that source document, never an edit inside a test PR.
10. **QA-210 — Every suite has a named owner.** TESTING.md lists each suite with its owning skill; a suite with no owner is adopted or deleted at the next strategy review — unowned suites are not run and not reported.
11. **QA-211 — New test types enter the strategy first.** A new kind of testing is added to TESTING.md (layer, budget, owner, cadence) in a reviewed change before its first test lands in the repo.
12. **QA-212 — Fake-functionality coverage is mapped.** For every interactive feature class in the DET-FAKE family (auth, payments, uploads, forms, counters, exports), TESTING.md names which skill runs its persistence and network probe — placeholder-scan, browser-verification, or e2e-testing — so no claimed effect goes unprobed.

## BAN list

- **BAN-QA-101 — Deck-only strategy.** Banned: presenting a strategy deck or document as the project's verification while no committed TESTING.md or running suites stand behind it. Defeats: DET-FAKE-022. Bad: a "QA Strategy" slide set claims full coverage; CI runs only a build step. Instead: write TESTING.md with layers, budgets, and owners, and land the first suite it names before claiming any coverage. Severity: BLOCK.
- **BAN-QA-102 — Coverage percentage as proof.** Banned: reporting a coverage number (or a green dashboard) as evidence the product works, when the tests behind it assert nothing. Defeats: DET-CODE-012. Bad: "92% coverage" in the release note from tests that call functions without asserting on outputs, so the figure never moves when behavior breaks. Instead: pair every coverage claim with the layer census (G-QA-102) and seeded-fault evidence that the suites can fail. Severity: BLOCK.
- **BAN-QA-103 — Staged-account verification claimed as coverage.** Banned: counting manual click-throughs on a curated demo account as test coverage for a flow. Defeats: DET-FAKE-014. Bad: checkout is "verified" by clicking through a seeded demo store whose data every account shares. Instead: cover the flow with an isolated automated journey that provisions its own account and data (e2e-testing), and record the demo pass as exploratory only. Severity: BLOCK.
- **BAN-QA-104 — Unnumbered budgets.** Banned: strategy language like "keep e2e small" or "suites stay fast" with no counts, runtimes, or flake ceiling. Defeats: DET-FAKE-005. Bad: TESTING.md says "a small e2e suite"; a year later it holds 400 journeys and takes three hours, with nothing ever in breach. Instead: state the e2e count ceiling, per-layer runtime budgets, and flake ceiling as numbers the census gate can check. Severity: WARN.

## Gates

- **G-QA-101 — Strategy document and mapping audit.** Verifies: QA-201, QA-203. Check: `test -f TESTING.md && python3 scripts/qa/check_strategy_map.py` — the script exits non-zero if TESTING.md is missing, contains TODO/TBD placeholders, or any acceptance-criteria class lacks a named layer or an Accepted Risks entry. Pass: exit 0. Fail: block the release; fix the map or record the risk. Recorded in: progress.md.
- **G-QA-102 — Layer census within budgets.** Verifies: QA-202, QA-205, QA-210. Check: CI runs `node scripts/qa/layer-census.mjs --budgets TESTING.md --fail-on-breach`; it counts tests and wall time per layer and exits non-zero when a count, runtime, or unowned suite breaches the strategy. Pass: exit 0. Fail: block merge; push tests down the pyramid, adopt, or delete. Recorded in: progress.md.
- **G-QA-103 — Accepted risks are explicit.** Verifies: QA-204. Check: `python3 scripts/qa/check_risks.py` exits non-zero if the Accepted Risks section is absent, empty, or any entry lacks a reason or a named acceptor. Pass: exit 0. Fail: block the release until every exclusion is written and owned. Recorded in: progress.md.
- **G-QA-104 — Flake budget and quarantine hygiene.** Verifies: QA-208. Check: `python3 scripts/qa/flake_report.py --max-rate 0.02` exits non-zero when a suite's measured flake rate exceeds the TESTING.md ceiling or any quarantined test lacks an owner or a future expiry date. Pass: exit 0. Fail: block the release; fix, extend with justification, or delete the flaky test. Recorded in: progress.md.

## Anti-patterns

- **Ice-cream-cone drift.** The e2e count grows every release while the unit layer stays flat, because UI tests are easier to add than to argue about; catch it in the census trend before the suite takes hours.
- **Retrofitted strategy.** TESTING.md is written after the suites exist and describes whatever was built, so it can never find a gap; catch it by checking the file's first commit predates the suites it governs.
- **Borrowed strategy.** A strategy copied from another project, with its flows, thresholds, and risks intact; catch it by sampling three entries and confirming each names this project's flows and budget documents.
- **Review theater.** The strategy is "reviewed" each release with no diff, no census output, and no decisions recorded; catch it by requiring the review to attach the G-QA-102 census result.

## Examples

- [Example 1 — Mapping acceptance criteria to layers](examples/example-1.md) — violates/corrects QA-203.
- [Example 2 — Numbered budgets replace "small and fast"](examples/example-2.md) — violates/corrects QA-202.
- [Example 3 — A written exclusion with an accepted risk](examples/example-3.md) — violates/corrects QA-204.

## Recall anchors

- No TESTING.md, no strategy — a deck is not verification.
- Every acceptance class maps to a layer, or it is a written accepted risk.
- Budgets are numbers the census can breach, not adjectives.
- A flow earns e2e by revenue or risk, and names why lower layers cannot cover it.
- Unowned suites are adopted or deleted, never silently kept.

## Checklist

- [ ] TESTING.md exists at the repo root and predates the suites it governs (QA-201).
- [ ] Per-layer counts/shares and runtime budgets are stated as numbers (QA-202).
- [ ] Every acceptance-criteria class maps to a named layer or an Accepted Risks entry (QA-203, QA-204).
- [ ] Visual, accessibility, load, chaos, contract, and security each have an owner, environment, and cadence (QA-206).
- [ ] Each layer's environment and cadence are named, including the nightly job names (QA-207).
- [ ] Flake ceiling is set and every quarantined test has an owner and expiry (QA-208).
- [ ] Every threshold cites its source budget/SLO document (QA-209).
- [ ] DET-FAKE probe ownership is mapped for every interactive feature class (QA-212).
