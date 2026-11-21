# tenant-isolation

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Encore, "Postgres Row-Level Security for Multi-Tenant SaaS" — https://encore.dev/articles/postgres-row-level-security-multi-tenant
- **Depends on:** schema-design, multitenancy-saas
- **Feeds into:** data-access, backup-recovery, api-building

## When to use / Do NOT use

- **Use when:** the product serves more than one tenant (or will), and any table, query, job, or cache key touches tenant-owned data — including the first migration that creates a tenant-owned table.
- **Do NOT use when:** the product is genuinely single-tenant with no tenant concept (say so in the architecture doc and move on), or when choosing the tenancy model at the architecture level (that decision is multitenancy-saas; this skill enforces isolation inside the chosen model).

## Rules

1. **DB-101 — The model is chosen and written down.** The isolation model is explicit: shared schema with `tenant_id` + row-level security (the default for many-small-tenants SaaS), schema-per-tenant, or database-per-tenant when regulation, tenant size, or per-tenant restore demands it. The choice and its reason live in the architecture doc.
2. **DB-102 — Every tenant table carries `tenant_id`.** Every tenant-owned table — including child and join tables — has a non-null `tenant_id` column and an index on it. A tenant-owned table without one is a defect, however the application code behaves.
3. **DB-103 — RLS is on, forced, and two-way.** In the shared-schema model, row-level security is enabled and `FORCE`d on every tenant table, and each policy covers reads and writes: `USING` for what can be seen, `WITH CHECK` for what can be written.
4. **DB-104 — The app connects as a non-owner.** The application role does not own the tables and does not have `BYPASSRLS`. Owner, superuser, and bypass connections never serve request traffic; they exist for migrations and administration only.
5. **DB-105 — Context is transaction-local.** Tenant context is set per transaction (`SET LOCAL` or `set_config(name, value, true)`), so a pooled connection can never carry one tenant's context into another tenant's request. Session-level context under a connection pool is forbidden.
6. **DB-106 — Two layers, both present.** Application queries scope by tenant AND RLS backstops them. Either layer alone is insufficient: app-only scoping is one forgotten `WHERE` from a leak; RLS-only without app scoping hides bugs until they become incidents.
7. **DB-107 — Jobs and admin paths set context too.** Background jobs, cron tasks, and admin/support paths set tenant context explicitly per unit of work. A job that runs "for all tenants" iterates tenants with context set per tenant; it does not run context-free.
8. **DB-108 — Context comes from the session, not the request.** The tenant identity is derived from the authenticated session or token. A client-supplied tenant parameter is at most a claim to be checked against the session, never the source of context.
9. **DB-109 — New tables join the catalog the same day.** Any migration creating a tenant-owned table adds it to the RLS catalog check (G-DB-052) in the same change. A table the check does not know about is treated as unisolated.
10. **DB-110 — Exports and deletions go through context.** Per-tenant export and erasure operate with that tenant's context set, through the same mechanism as requests — never as hand-written cross-tenant SQL in application code.

## BAN list

- **BAN-DB-051 — Owner connections serving traffic.** Banned: the application connecting as the table owner, a superuser, or any role with `BYPASSRLS`, which silently disables every RLS policy on every query. Defeats: DET-CODE-020. Bad: the app connects as `postgres` "temporarily" during launch; a year later every cross-tenant test passes because policies never execute at all. Instead: a dedicated non-owner application role with `NOBYPASSRLS`, used by all request traffic (DB-104). Severity: BLOCK.
- **BAN-DB-052 — Session-level tenant context under a pool.** Banned: setting tenant context with a session-level `SET` (or an ORM connection hook that runs once per connection) while connections are pooled. Defeats: DET-CODE-030. Bad: request A sets `app.tenant_id = 5` on a pooled connection and returns it; request B for tenant 9 reuses the connection and reads tenant 5's rows. Instead: `SET LOCAL` / `set_config(..., true)` inside each transaction (DB-105), proven by the pool-leak test (G-DB-054). Severity: BLOCK.
- **BAN-DB-053 — Read-only policies.** Banned: an RLS policy with `USING` but no `WITH CHECK`, which restricts what a tenant can read while letting writes land in any tenant. Defeats: DET-CODE-019. Bad: a crafted request inserts an invoice with another tenant's `tenant_id`; the victim's billing page now shows a charge they never made. Instead: every policy carries `WITH CHECK (tenant_id = current_setting('app.tenant_id')::uuid)` or its equivalent (DB-103). Severity: BLOCK.
- **BAN-DB-054 — The tenant-less tenant table.** Banned: shipping a tenant-owned table without `tenant_id` and RLS because "we only have one customer so far." Defeats: DET-CODE-020. Bad: the invoices table launches tenant-less; when customer two signs up, isolation is retrofitted under time pressure and the join table is missed. Instead: `tenant_id`, index, and policy ship in the table's first migration (DB-102, DB-109). Severity: WARN.

## Gates

- **G-DB-051 — Cross-tenant test suite.** Verifies: DB-102, DB-103, DB-106. Check: automated — as tenant A, attempt select, insert, update, and delete against tenant B's rows on every tenant table; every attempt must return zero rows or fail. Pass: zero cross-tenant effects across all tables and verbs. Fail: block shipment. Recorded in: progress.md.
- **G-DB-052 — RLS catalog check.** Verifies: DB-103, DB-109. Check: automated — query `pg_class` (`relrowsecurity`, `relforcerowsecurity`) and `pg_policies`; assert every table on the tenant-table list has RLS enabled and forced and at least one policy with a `WITH CHECK` expression. Pass: full coverage. Fail: block shipment. Recorded in: progress.md.
- **G-DB-053 — Role check.** Verifies: DB-104. Check: automated — query `pg_roles` for the application's connection role; assert `rolbypassrls = false` and that the role owns no tenant tables. Pass: non-owner, no bypass. Fail: block shipment. Recorded in: progress.md.
- **G-DB-054 — Pool-leak test.** Verifies: DB-105. Check: automated — an integration test runs with a connection pool of size 1 and interleaves two tenants' requests; assert no response contains the other tenant's data. Pass: zero cross-tenant bytes. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Backstop theater.** RLS is enabled and the policy file looks beautiful, but the application connects as the owner, so no policy ever executes — and the test suite connects as the same owner, so it "passes." Catch it: run G-DB-053, then run one cross-tenant query as the actual application role.
- **The forgotten child table.** Orders are scoped and policy-covered; `order_items` are not, and the leak ships through the join. Catch it: the tenant-table list (DB-109) is built from the schema, not from memory.
- **Global admin convenience.** One "support mode" query path runs with no tenant context and no audit trail, and the team uses it daily. Catch it: grep for connections or code paths that skip the context setter; each one needs DB-107 treatment or deletion.
- **Tenant ID from the URL.** Scoping trusts a tenant identifier in the path or body that any user can edit, with the session never consulted. Catch it: change the identifier in a request and watch whose data comes back (DB-108).

## Examples

- [Example 1 — A tenant table with a complete policy](examples/example-1.md) — corrects DB-102, DB-103.
- [Example 2 — Transaction-local tenant context](examples/example-2.md) — corrects DB-105.
- [Example 3 — A non-owner application role](examples/example-3.md) — corrects DB-104.

## Recall anchors

- RLS is the backstop; the app still scopes every query.
- Owner connections make every policy a decoration.
- Context is set per transaction, or the pool will leak it.
- USING without WITH CHECK is a read-only promise and a write-side hole.
- Child and join tables are tenant tables too.

## Checklist

- [ ] The isolation model is chosen and recorded (DB-101).
- [ ] Every tenant-owned table has a non-null, indexed tenant_id — child and join tables included (DB-102, DB-109).
- [ ] RLS is enabled, forced, and carries WITH CHECK on every tenant table (DB-103, G-DB-052).
- [ ] The application role is a non-owner without BYPASSRLS (DB-104, G-DB-053).
- [ ] Tenant context is transaction-local and derived from the session (DB-105, DB-108, G-DB-054).
- [ ] The cross-tenant test suite passes on every table and verb (G-DB-051).
- [ ] Jobs and admin paths set context per unit of work (DB-107).
