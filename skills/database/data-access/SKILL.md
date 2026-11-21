# data-access

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Encore, "Postgres Row-Level Security for Multi-Tenant SaaS" (scoping enforced in the database as backstop) — https://encore.dev/articles/postgres-row-level-security-multi-tenant ; PROJECT_ANATOMY.md Part 3
- **Depends on:** schema-design, sql-fundamentals, tenant-isolation
- **Feeds into:** caching, read-replicas, query-performance

## When to use / Do NOT use

- **Use when:** writing or reviewing any code that reads or writes the database — repositories, models, query builders, background jobs, admin tooling.
- **Do NOT use when:** designing the schema itself (schema-design), tuning a specific slow query (query-performance), or writing one-off migration SQL (migrations). The layer's rules still bind any code that ships; throwaway scripts that touch production data follow them too.

## Rules

1. **DB-181 — One layer owns the database.** All access goes through a single layer (repositories, ORM models, or query builders). No SQL is constructed in controllers, views, or templates.
2. **DB-182 — Everything is parameterized.** Values reach SQL only as bound parameters. Identifiers (table and column names) come only from allowlists, never from request input.
3. **DB-183 — Tenant scoping lives in the layer.** The layer applies tenant scope to every query, backed by row-level security in the database. No call site is responsible for remembering to scope.
4. **DB-184 — Lists are paginated, with a ceiling.** Every list method requires pagination parameters and enforces a hard maximum page size, whatever the caller asks for.
5. **DB-185 — Every call has a statement timeout.** A runaway query is killed by the database and surfaces as a typed error, instead of piling up behind a hung request.
6. **DB-186 — Writes answer for themselves.** A write returns the persisted entity or raises an explicit, typed error. A silent no-op write is forbidden in all paths.
7. **DB-187 — Transaction boundaries are explicit.** Services open and close transactions through the layer's declared boundary; the layer never hides a partial commit behind a helper.
8. **DB-188 — Raw SQL stays inside the layer.** When the ORM cannot express a query, raw SQL is allowed inside the layer only — still parameterized, still reviewed, still scoped.
9. **DB-189 — Generated SQL is inspected.** Each new query's generated SQL is read at least once in development logs before it ships; ORM output is never trusted unread.
10. **DB-190 — Connection config is injected.** Hosts, roles, and credentials come from environment configuration. No connection detail is hardcoded in source.

## BAN list

- **BAN-DB-091 — String-built SQL.** Banned: constructing SQL by interpolating or concatenating values into the query text. Defeats: DET-CODE-017. Bad: `"SELECT * FROM users WHERE email = '" + email + "'"` — one crafted email address reads the whole table. Instead: a bound parameter, `WHERE email = $1`, on every value, every time (DB-182). Severity: BLOCK.
- **BAN-DB-092 — The swallowed write.** Banned: catching a write failure and continuing as if the write succeeded. Defeats: DET-CODE-005. Bad: an update wrapped in a try/catch that logs nothing and returns success; the user sees "saved" and the row never changed. Instead: propagate a typed error and let the caller decide; writes confirm persistence (DB-186). Severity: BLOCK.
- **BAN-DB-093 — The unbounded list method.** Banned: a repository or endpoint method that returns every matching row with no pagination contract. Defeats: DET-CODE-033. Bad: `findAllOrders()` loads the full table into the controller and into memory. Instead: mandatory pagination parameters with a hard maximum page size (DB-184). Severity: BLOCK.
- **BAN-DB-094 — Hardcoded connection config.** Banned: production hosts, roles, or credentials written as literals in data-access code. Defeats: DET-INF-007. Bad: a repository class contains the production database password so a new hire can "just run it". Instead: environment-injected configuration, with secrets held in secret storage (DB-190). Severity: BLOCK.

## Gates

- **G-DB-091 — Layer-boundary lint.** Verifies: DB-181, DB-188. Check: automated — a grep/import scan fails the build if SQL construction (query strings, query-builder entry points) appears outside the data-access package. Pass: zero matches outside the layer. Fail: block shipment. Recorded in: progress.md.
- **G-DB-092 — Parameterization scan.** Verifies: DB-182. Check: automated — static analysis flags string concatenation or interpolation inside query construction anywhere in the codebase. Pass: no findings. Fail: block shipment. Recorded in: progress.md.
- **G-DB-093 — Timeout behavior test.** Verifies: DB-185, DB-186. Check: automated — an integration test runs a query past the statement timeout and asserts it is killed and surfaces as a typed error, and that a forced write failure raises instead of returning success. Pass: both assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-DB-094 — Tenant-scope test.** Verifies: DB-183. Check: automated — an integration test authenticates as tenant A and attempts reads and writes against tenant B's rows through the layer on every tenant-owned entity. Pass: zero rows visible, zero writes accepted. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Controller SQL "just this once".** A one-off query pasted into a handler during a rush, then copied into three more handlers. Catch it: the boundary lint exists precisely because "once" is how scattering starts.
- **ORM magic trust.** Generated SQL is never read until production slows down and nobody recognizes the query in the slow log. Catch it: DB-189 — read each new query's SQL in development, once, on purpose.
- **Retry fog.** The layer silently retries failed writes, so a non-idempotent insert lands twice and the duplicate looks like a user error. Catch it: retries belong to explicitly idempotent operations, declared as such.
- **The god repository.** One class owns every table, every transaction, and every exception policy, so no rule can be enforced inside it. Catch it: if the layer cannot state its own boundaries, it has already lost them.

## Examples

- [Example 1 — Interpolated query replaced by a bound parameter](examples/example-1.md) — corrects DB-182.
- [Example 2 — Controller SQL replaced by a paginated repository method](examples/example-2.md) — corrects DB-181, DB-184.
- [Example 3 — Swallowed write failure replaced by a typed error](examples/example-3.md) — corrects DB-186.

## Recall anchors

- One layer owns the database; nothing else talks to it.
- Values are parameters; identifiers are allowlisted.
- Scoping is the layer's job, backed by RLS — never the call site's memory.
- Every list is paginated; every call has a timeout.
- A write returns the row or raises — silence is a defect.

## Checklist

- [ ] No SQL construction exists outside the data-access layer (G-DB-091).
- [ ] The parameterization scan is clean (G-DB-092).
- [ ] Tenant-scope tests pass for every tenant-owned entity (G-DB-094).
- [ ] List methods enforce pagination with a hard maximum page size (DB-184).
- [ ] Statement timeouts are set, and the timeout test passes (G-DB-093).
- [ ] New queries had their generated SQL inspected in development (DB-189).
