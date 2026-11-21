# multitenancy-saas

## Metadata

- **Owner department:** D2 Architecture & System Design (AR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Microsoft Learn, multitenancy and Azure SQL Database (tenancy models, row-level security, noisy neighbor) — https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/sql-database ; Microsoft Learn, multitenancy tenancy models for Cosmos DB — https://learn.microsoft.com/en-us/azure/cosmos-db/multi-tenancy-vector-search
- **Depends on:** system-design, data-architecture, backend-auth
- **Feeds into:** tenant-isolation, schema-design, subscriptions

## When to use / Do NOT use

- **Use when:** a product serves more than one customer organization or consumer from one deployment and the isolation model must be chosen, implemented, or audited — tenancy model selection, tenant context handling, provisioning, per-tenant operations.
- **Do NOT use when:** the product is single-tenant by design — say so in ARCHITECTURE.md and stop. Do not use this skill for the database-level implementation of row-level security itself; that is tenant-isolation and schema-design, working from the model chosen here. Data-level isolation enforcement and its review — tenant scoping across tables, queries, jobs, and cache keys — belongs to tenant-isolation (D5); this skill owns only the model-level choice and audit.

## Rules

1. **AR-181 — Tenant is defined first.** State what a tenant is (customer organization, individual consumer, or sub-unit) before choosing any model; the definition drives isolation, billing, and data-sovereignty requirements.
2. **AR-182 — Model per layer, named from the catalog.** Choose per layer from the named models — shared schema with tenant key (pool), schema/database per tenant (silo), or hybrid (bridge) — and record the choice in an ADR citing the isolation, compliance, and cost trade-offs.
3. **AR-183 — Context is established at the edge.** Tenant context is resolved once, at the request boundary, from the authenticated principal or the subdomain, and propagated. Code never accepts a tenant ID from an unauthenticated request body.
4. **AR-184 — Every path is scoped.** Every query path — API, admin, reporting, export, and background jobs — is scoped by tenant. An unscoped path is a blocker defect.
5. **AR-185 — Isolation is platform-enforced.** Scoping is applied automatically (ORM filter, row-level security, middleware), never by each developer remembering a filter per query.
6. **AR-186 — Tenant key on every tenant-owned table.** The key is non-null, present from the first migration, and leads the index used by tenant-scoped queries.
7. **AR-187 — Per-tenant operations are designed.** Backup and restore granularity, data export, and tenant deletion (including legal erasure) are specified for the chosen model before the first tenant onboards.
8. **AR-188 — Provisioning is automated.** New tenants are created by an automated, tested procedure. Manual database edits are not a provisioning path.
9. **AR-189 — Noisy-neighbor controls are part of the model.** Per-tenant rate limits, quotas, and per-tenant usage observability ship with the design, not after the first incident.
10. **AR-190 — Hybrid placements are enumerated.** In a bridge model, a tenant catalog records which tenant lives in which store; routing reads the catalog, never a hardcoded list in code.
11. **AR-191 — Async work carries tenant context.** Background jobs and event consumers receive and propagate tenant context; work that arrives without it fails closed rather than running unscoped.
12. **AR-192 — Isolation is tested, not assumed.** The cross-tenant test suite is part of the design deliverable, and it runs in CI from the first tenant onward.

## BAN list

- **BAN-AR-091 — Tenant ID from the request body.** Banned: resolving the tenant from a client-supplied value in an unauthenticated request. Defeats: DET-CODE-019. Bad: `POST /invoices` accepts `tenant_id` in the JSON body, so any caller can read and write any tenant's invoices by changing one field. Instead: resolve the tenant from the authenticated principal (or the subdomain, verified against the session) at the edge and ignore body-supplied tenant values entirely. Severity: BLOCK.
- **BAN-AR-092 — Isolation by developer memory.** Banned: tenant scoping that depends on each query's author remembering to add the filter. Defeats: DET-CODE-020. Bad: most queries carry `WHERE tenant_id = ?`, the new reporting query does not, and one tenant's dashboard shows everyone's revenue. Instead: enforce scoping in the platform layer — row-level security or an ORM-level automatic filter — so an unscoped query returns nothing rather than everything. Severity: BLOCK.
- **BAN-AR-093 — Manual provisioning.** Banned: creating a tenant by hand-editing the production database. Defeats: DET-INF-004. Bad: onboarding a customer means an engineer runs remembered SQL inserts at midnight; one missed row leaves the tenant half-created with no error anywhere. Instead: a scripted, tested provisioning procedure that creates the tenant atomically and is exercised in staging on every release. Severity: BLOCK.
- **BAN-AR-094 — Unbounded shared tenants.** Banned: shared compute and storage with no per-tenant rate limit or quota. Defeats: DET-INF-023. Bad: one tenant's import job saturates the worker pool for six hours while every other tenant's requests time out. Instead: per-tenant rate limits and quotas at the edge and in the job queue, with per-tenant usage visible on a dashboard. Severity: WARN.

## Gates

- **G-AR-091 — Cross-tenant test suite.** Verifies: AR-184, AR-192. Check: automated — authenticate as tenant A and attempt reads, writes, and exports against tenant B's known resource IDs through every interface class (API, export, report, job trigger). Pass: every attempt returns 403 or 404 and writes nothing. Fail: block release; a single cross-tenant success is a P0 defect. Recorded in: progress.md. Execution: this gate is specified here and executed by D8 (QA & Testing) in its test harness, with auth fixtures owned by D4/D7 and tenant data fixtures owned by D5.
- **G-AR-092 — Tenant-key schema check.** Verifies: AR-186. Check: automated — script asserts every table flagged tenant-owned has a non-null tenant key column and an index leading with it. Pass: zero violations. Fail: block merge. Recorded in: progress.md. Execution: this gate is specified here (canonical — data-architecture G-AR-074 cites it) and executed by D8 (QA & Testing), with schema fixtures owned by D5.
- **G-AR-093 — Provisioning drill.** Verifies: AR-188. Check: automated — run the provisioning procedure in staging, then verify the new tenant can sign in, sees an empty workspace, and appears in the tenant catalog. Pass: tenant fully created with no manual step. Fail: block the release that changed provisioning. Recorded in: progress.md.
- **G-AR-094 — Noisy-neighbor review.** Verifies: AR-189. Check: manual — confirm per-tenant rate limits and quotas are configured and per-tenant usage metrics are visible on an operations dashboard. Pass: limits configured and metrics visible for every tenant. Fail: warn; schedule the fix before onboarding the next tenant. Recorded in: progress.md.

## Anti-patterns

- **Tenant_id sprinkling.** The column is added to the obvious tables while exports, search indexes, and file storage stay unscoped. Catch it: list every place tenant data can leave the system and check each one for scoping.
- **The god admin.** An internal admin console bypasses tenant scoping "temporarily" and becomes the largest cross-tenant surface in the product. Catch it: admin paths appear in the cross-tenant test suite like any other interface.
- **Silo sprawl.** Database-per-tenant adopted for a handful of tenants with no automation, until migrations and backups become per-tenant manual chores. Catch it: if provisioning and migration are not scripted, the silo model was chosen without its operating cost.
- **Untraceable usage.** Shared-everything metering means no tenant's consumption can be attributed, and invoices are assembled by hand. Catch it: pick one tenant and produce its usage for last month from the system alone; if a human had to estimate, metering failed.

## Examples

- [Example 1 — Tenant context from the edge, not the body](examples/example-1.md) — corrects AR-183.
- [Example 2 — The unscoped export, scoped and tested](examples/example-2.md) — corrects AR-184.
- [Example 3 — Provisioning as a tested procedure](examples/example-3.md) — corrects AR-188.

## Recall anchors

- Define the tenant before choosing the model.
- Context comes from the edge, never from the body.
- Every path is scoped — admin, exports, and jobs included.
- Isolation is enforced by the platform, not by memory.
- Provisioning is a procedure, not a person with SQL access.

## Checklist

- [ ] The tenant definition is written down and the per-layer model is chosen in an ADR (AR-181, AR-182).
- [ ] Tenant context is resolved once at the edge from the authenticated principal or subdomain (AR-183).
- [ ] Cross-tenant test suite passes: every cross-tenant attempt returns 403/404 and writes nothing (G-AR-091).
- [ ] Tenant-key schema check passes on every tenant-owned table (G-AR-092).
- [ ] Backup/restore granularity, export, and tenant deletion are specified for the model (AR-187).
- [ ] Provisioning drill passes in staging with no manual step (G-AR-093).
- [ ] Per-tenant rate limits, quotas, and usage metrics are in place (AR-189).
