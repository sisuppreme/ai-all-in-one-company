# integration-testing

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Ham Vocke, "The Practical Test Pyramid" — https://www.martinfowler.com/articles/practical-test-pyramid.html ; GitHub Docs, "Continuous integration" — https://docs.github.com/en/actions/get-started/continuous-integration
- **Depends on:** unit-testing, test-data
- **Feeds into:** e2e-testing, contract-testing, qa-gates

## When to use / Do NOT use

- **Use when:** verifying that real components work together — the API against a real database, real migrations, real HTTP, real transaction and permission behavior — before the e2e layer spends its budget on the same defects.
- **Do NOT use when:** the behavior is one module's logic with no collaborator (unit-testing covers it), or the claim is about a full user journey in a browser (e2e-testing). Do not use this layer to re-test what the unit layer already pins; the pyramid stays narrow at the top.

## Rules

1. **QA-021 — Real database, real migrations.** The database under test is a real instance of the production engine, started by the harness (throwaway container or ephemeral schema) and built by running the project's actual migrations. A hand-maintained test schema or a different in-memory engine is a failed setup, not a shortcut.
2. **QA-022 — Real HTTP path.** Tests drive the API over real HTTP — a booted server or the framework's test client running the full middleware stack (auth, validation, error handling). Calling route handlers or services directly is a unit test wearing a costume.
3. **QA-023 — Mocks only at the system edge.** The only collaborators replaced are third parties outside the project's control (payment providers, email APIs), and they are replaced by the provider's own sandbox or a contract-verified stub. The project's own database, API, queue, and cache are never faked.
4. **QA-024 — Write, then read back elsewhere.** Every write endpoint has at least one test that performs the write and reads the result back through a different surface — a read endpoint, a second endpoint, or a direct database query. Asserting on the write response alone proves nothing about persistence.
5. **QA-025 — Each test seeds exactly what it needs.** Tests create their own records through factories or fixtures with known values and assert on those records. No test asserts on ambient or pre-existing data it did not create.
6. **QA-026 — Cleanup by construction.** Isolation comes from a fresh database, an ephemeral schema, or a transaction rolled back at test end. Cleanup by deleting rows is forbidden: a delete can remove another test's data and hides the very persistence bugs this layer exists to catch.
7. **QA-027 — Tenant and permission boundaries are tested here.** For every tenant-scoped or role-scoped entity, at least one test proves a cross-tenant or unauthorized read returns nothing (empty result, 403, or 404) and a cross-tenant write is rejected with no state change.
8. **QA-028 — Multi-write operations are atomicity-tested.** Any operation that writes more than one record has a test that forces a failure partway (invalid second write, killed constraint) and asserts that no partial state persists after the error response.
9. **QA-029 — Failure paths are integration cases.** Provider declines, dependency timeouts, and downstream 5xx responses (from the edge stub) are tested at this layer: the API must return its documented error and must not record a success state.
10. **QA-030 — Deterministic and order-independent.** The layer passes with tests shuffled and with any single test run alone. Dependence on execution order, wall-clock time, or leftover state from another test is a defect in the suite.
11. **QA-031 — The layer's runtime is budgeted.** Slow tests are tagged and reported by name. The layer's total CI runtime budget is recorded in TESTING.md, and a breach fails the job like any other threshold.
12. **QA-032 — The layer must be able to fail.** A seeded fault — one migration reverted, one write path broken — must turn the suite red. A layer that has never been observed failing is decoration, and its green checkmark certifies nothing.

## BAN list

- **BAN-QA-011 — Hand-written fake of your own component.** Banned: replacing the project's own database, repository layer, or API with a hand-written in-memory fake inside integration tests. Defeats: DET-FAKE-010. Bad: the admin-save test runs against a `Map`-backed fake repository, passes, and ships an admin panel whose real save writes nothing. Instead: run against the real database built by the real migrations; stub only third parties at the system edge (QA-023). Severity: BLOCK.
- **BAN-QA-012 — Write asserted from the response only.** Banned: a write test whose only assertion is the write call's response body or status. Defeats: DET-FAKE-016. Bad: `PATCH /profile` returns `200 {name: "New Name"}` and the test passes, while the update is applied to request state and reverts on the next read. Instead: read the record back through a different surface and assert the stored value (QA-024). Severity: BLOCK.
- **BAN-QA-013 — Mock-call verification as proof of persistence.** Banned: asserting that a mocked store's `save()` was called as evidence that data persisted. Defeats: DET-FAKE-003. Bad: the signup test mocks the user store, verifies the mock was invoked, and passes while production registration discards the account. Instead: register against the real store, then sign in with the new credentials in the same test and assert the session works. Severity: BLOCK.
- **BAN-QA-014 — Delete verified on the list only.** Banned: a delete test that checks only that the item leaves a list response. Defeats: DET-FAKE-011. Bad: after `DELETE /items/42` the list no longer shows 42, so the test passes — but `GET /items/42` still returns the record and search still finds it. Instead: assert the record is unreachable through every surface: list, direct read, and search. Severity: BLOCK.
- **BAN-QA-015 — Assertions on ambient seed data.** Banned: tests that pass because a shared seed or fixture row exists, asserting on data the test did not create. Defeats: DET-FAKE-014. Bad: the search test finds "Acme Corp" because the seed file inserts it; when the seed changes, the test breaks — and while it passes, it proves nothing about records the system actually writes. Instead: the test creates its own uniquely named record and asserts on that record (QA-025). Severity: WARN.

## Gates

- **G-QA-011 — Clean-room green run.** Verifies: QA-021, QA-026. Check: automated — CI destroys all test volumes (`docker compose down -v` or the stack's equivalent) and runs the layer from a clean checkout with no pre-existing database, e.g. `npm run test:integration`; the command's exit code is the verdict. Pass: exit code 0. Fail: non-zero exit blocks merge. Recorded in: progress.md.
- **G-QA-012 — Reverted-migration negative control.** Verifies: QA-021, QA-032. Check: automated — a script reverts exactly one migration (e.g. `npm run db:migrate:undo`) against the test database and re-runs the layer. Pass: the run exits non-zero — the suite noticed the missing schema. Fail: a green run means the layer cannot detect schema drift; block merge and repair the layer before any other QA sign-off. Recorded in: progress.md.
- **G-QA-013 — Write/read-back coverage.** Verifies: QA-024, QA-027. Check: automated — a script lists every write route from the API's route table or OpenAPI document and greps the integration suite for a corresponding read-back test and, for tenant-scoped entities, a cross-tenant case; uncovered routes are printed by name. Pass: zero uncovered write routes. Fail: block merge until each gap has a test or a written waiver with owner and expiry in progress.md. Recorded in: progress.md.
- **G-QA-014 — Shuffled run inside the runtime budget.** Verifies: QA-030, QA-031. Check: automated — CI runs the layer with the runner's random-order flag under a hard timeout set to the TESTING.md budget, e.g. `timeout 600 npm run test:integration -- --shuffle`. Pass: exit code 0 within the timeout. Fail: non-zero exit or timeout blocks merge; the slowest tests are named in the job report. Recorded in: progress.md.

## Anti-patterns

- **The hand-synced test schema.** A `test-schema.sql` maintained by hand alongside the real migrations; it drifts a little each sprint, and the layer certifies a database production never runs. Catch it: search the repo for schema definitions outside the migrations folder — any hit is the tell.
- **The happy-path corridor.** Every integration test asserts a 2xx; there is no decline, no constraint violation, no cross-tenant attempt. Catch it: count the layer's non-2xx assertions; a layer with none has tested only the corridor where defects are rarest.
- **The shared kingdom fixture.** One giant seed dataset every test leans on; failures cascade across unrelated tests and nobody can say which test owns which row. Catch it: run any single test alone on an empty database — if it cannot set itself up, it lives in the kingdom.
- **The slow swamp.** The layer quietly re-tests unit-level logic at a hundred times the cost until CI takes an hour and the team moves it out of the merge gate "temporarily." Catch it: read the slowest-test report each week; anything duplicating a unit test's assertion is pushed back down the pyramid.

## Examples

- [Example 1 — Write asserted from the response, corrected to read-back](examples/example-1.md) — corrects QA-024.
- [Example 2 — Hand-maintained test schema, corrected to real migrations](examples/example-2.md) — corrects QA-021.
- [Example 3 — Missing tenant boundary, corrected to a cross-tenant test](examples/example-3.md) — corrects QA-027.

## Recall anchors

- Real database, real migrations, real HTTP — mocks only at the edge.
- A write is proven by reading it back somewhere else.
- Each test seeds its own data and cleans up by construction.
- If reverting a migration doesn't turn it red, it tests nothing.
- Slow is a budget breach, not a personality trait.

## Checklist

- [ ] The test database is created by the project's real migrations on the production engine (QA-021).
- [ ] No hand-written fake stands in for the project's own database, API, queue, or cache (QA-023).
- [ ] Every write endpoint has a read-back test through a different surface (QA-024, G-QA-013).
- [ ] Every tenant-scoped entity has a cross-tenant read/write test (QA-027).
- [ ] Multi-write operations have a partial-failure atomicity test (QA-028).
- [ ] The layer passes shuffled and single-test runs inside its runtime budget (QA-030, QA-031, G-QA-014).
- [ ] The reverted-migration negative control turned the suite red (G-QA-012).
- [ ] The layer runs green from a clean checkout with no pre-existing database (G-QA-011).
