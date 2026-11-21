# test-data

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://playwright.dev/docs/best-practices
- **Depends on:** test-strategy
- **Feeds into:** qa-gates, placeholder-scan, e2e-testing, integration-testing

## When to use / Do NOT use

- **Use when:** creating, reviewing, or fixing the data any test, seed script, fixture, or demo environment runs on — factories, builders, fixtures, seed scripts, test database lifecycle, or production-shaped data requests.
- **Do NOT use when:** designing production seed/reference data itself (countries, plans, tax tables as shipped product data) — use seed-data (D5); or deciding data retention and privacy policy — use D14's privacy skills. This skill governs data manufactured for testing and demos.

## Rules

1. **QA-241 — Manufactured, never harvested.** All test data is created by code — factories, builders, or fixtures versioned with the tests that use them. No test data originates from a database export, a spreadsheet, or a manual insert.
2. **QA-242 — Tests own their data.** A test reads only data it created or explicitly loaded in its own setup. Shared mutable fixtures that tests read and write are prohibited; order dependence traced to shared data is a defect in the fixture, not in the test order.
3. **QA-243 — Valid by default.** A factory call with zero overrides produces a record that passes every validation and constraint of the real model. If a legal record needs overrides, fix the factory defaults, not the call sites.
4. **QA-244 — Deterministic generation.** Every random-looking value comes from a seeded generator whose seed is fixed in the repo or logged by the run. Wall-clock time is never read directly: dates and timestamps are computed relative to an injected clock.
5. **QA-245 — The harness owns the lifecycle.** The test database is created by the project's migrations, populated per test or per suite, and destroyed or reset by the harness afterward. No test depends on rows left behind by a previous run, and no cleanup is done by hand.
6. **QA-246 — Synthetic data is labeled synthetic, end to end.** Every seed or fixture record carries a machine-readable marker (for example an `is_seed` flag or a reserved seed email domain) that survives into API responses and screens in non-production environments. Generated people and records are never presented as real users, customers, or activity.
7. **QA-247 — The seed path refuses production.** The seed entry point checks the environment before writing anything and exits non-zero when the environment is production, unless an explicit demo flag is set — and demo-flagged seeding still writes only marker-carrying records (QA-246).
8. **QA-248 — No production data in test environments.** Production rows are never copied into test, CI, staging, or development databases — including "anonymized" copies that keep real names, emails, or phone numbers. When production shape is needed, generate the same shape synthetically; any exception is sanitized under D14's privacy rules before it leaves production.
9. **QA-249 — Fixtures contain no real personal details.** Fixture people are invented: names created for the fixture, email addresses on reserved domains (`example.com`, `example.org`), phone numbers from reserved fictional ranges. A real person's details in a fixture file are a privacy defect, not a convenience.
10. **QA-250 — Reference data comes from the shared fixtures.** Countries, plans, currencies, and other shared reference data are loaded from the same fixtures development uses. Test-local copies that can drift from the shared set are prohibited.

## BAN list

- **BAN-QA-121 — Production database copy as test data.** Banned: restoring a production dump (full or partial) into any test, CI, staging, or development database. Defeats: DET-FAKE-014. Bad: a nightly production backup is restored into staging, so tests and demos run on real customer accounts. Instead: generate production-shaped synthetic data with factories at comparable volume, or sanitize under D14's privacy rules before any non-production use. Severity: BLOCK.
- **BAN-QA-122 — Seed users shipped as real customers.** Banned: seed or fixture accounts, testimonials, or activity presented in production as real users or social proof. Defeats: DET-FAKE-014. Bad: the seed script creates 50 "customers" with praise quotes that appear on the production homepage. Instead: keep seed accounts in development and demo environments only, behind the QA-247 environment guard, marker-carrying, and excluded from the production seed path. Severity: BLOCK.
- **BAN-QA-123 — Real personal details in fixtures.** Banned: real names paired with real email addresses, phone numbers, or other personal details of real people anywhere in fixture or seed files. Defeats: DET-FAKE-014. Bad: a fixture user carries the developer's real Gmail address and a real customer's phone number "just for one test." Instead: invent fixture people with `example.com` addresses and reserved fictional phone numbers (QA-249). Severity: BLOCK.
- **BAN-QA-124 — Identical staged notifications for every account.** Banned: seeding every account with the same pre-written notification or activity feed presented as real events. Defeats: DET-FAKE-013. Bad: every new test and demo account starts with "John liked your post" and three scripted comments. Instead: generate notifications from real events inside the test; fresh accounts start with an empty feed, and demo notifications are labeled demo data. Severity: BLOCK.

## Gates

- **G-QA-121 — Isolation proof.** Verifies: QA-242, QA-245. Check: in CI, run the full suite with randomized test order, then run each test file standalone (the framework's shuffle and per-file modes). Pass: both runs fully green. Fail: block merge; the failing test's data dependencies are fixed, not reordered. Recorded in: progress.md.
- **G-QA-122 — Seed/production refusal check.** Verifies: QA-247. Check: invoke the project's seed command with production environment variables set (for example `APP_ENV=production npm run db:seed`, substituting the project's actual command). Pass: the command exits non-zero and writes zero rows. Fail: block release until the guard exists. Recorded in: progress.md.
- **G-QA-123 — Fixture personal-data scan.** Verifies: QA-246, QA-249. Check: run the placeholder-scan sweep over fixture and seed directories, including `grep -rEi '@(gmail|yahoo|hotmail|outlook|icloud)\.com' tests/ fixtures/ db/` plus a marker audit of every fixture user record. Pass: zero real-domain hits and every fixture user carries the synthetic marker. Fail: block merge; replace the data, do not allow-list it. Recorded in: progress.md.
- **G-QA-124 — Determinism check.** Verifies: QA-244. Check: run the data-generating test files twice with the fixed seed and diff the generated fixture snapshots or database dumps between runs. Pass: byte-identical output. Fail: block merge until the unseeded source is seeded or clock-injected. Recorded in: progress.md.

## Anti-patterns

- **Override sprawl.** Every call site overrides four or five factory fields to get a legal record — the defaults are wrong and every test teaches the wrong shape. Catch it by grepping factory calls for override counts before review.
- **Calendar rot.** Fixtures hardcode dates ("expires 2025-01-01", "trial ends next week" as a literal) that silently flip test results as the calendar moves. Catch it by searching fixtures for literal dates outside the injected-clock helper.
- **The golden shared account.** One beloved login (`test@test.com`) that every test and demo depends on, whose state nobody can state. Catch it by searching tests for shared credentials or a single hardcoded user ID.
- **One-row world.** Every fixture set has exactly one to three rows, so pagination, empty states, limits, and N+1 behavior are never exercised. Catch it by checking that at least one fixture set per list-shaped feature exceeds one page of results.

## Examples

- [Example 1 — Factory data instead of a production copy](examples/example-1.md) — violates/corrects QA-241, QA-248.
- [Example 2 — Seed script that refuses production](examples/example-2.md) — violates/corrects QA-247.
- [Example 3 — Labeled synthetic fixture people](examples/example-3.md) — violates/corrects QA-246, QA-249.

## Recall anchors

- Manufactured, deterministic, disposable — data a test did not make is data it cannot trust.
- A fresh account starts empty; a fresh database starts synthetic.
- The seed command must refuse production on its own, not by policy.
- Real people never appear in fixtures — invented names, reserved domains.
- If tests only pass in one order, the fixture is the bug.

## Checklist

- [ ] All test data is produced by factories, builders, or fixtures versioned with the tests (QA-241).
- [ ] The full suite passes with randomized order and per-file standalone runs (G-QA-121).
- [ ] Factories produce valid records with zero overrides (QA-243).
- [ ] Generators are seeded and time comes from an injected clock (QA-244).
- [ ] Every seed/fixture record carries the synthetic marker (QA-246).
- [ ] The seed command exits non-zero under production environment variables (G-QA-122).
- [ ] No production rows and no real personal details exist in any fixture or seed file (QA-248, QA-249, G-QA-123).
