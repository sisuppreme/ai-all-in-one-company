# data-architecture

## Metadata

- **Owner department:** D2 Architecture & System Design (AR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** MongoDB Manual, data modeling (embed vs reference by access pattern) — http://mongodocs.github.io/core/data-modeling-introduction.html ; Database-per-service and data ownership patterns — https://microservices.io/
- **Depends on:** system-design, requirements-writing
- **Feeds into:** schema-design, tenant-isolation, migrations

## When to use / Do NOT use

- **Use when:** a project needs its data model designed or changed: choosing structures for a relational or document store, deciding embed vs reference, placing data ownership across services, or reviewing a schema before migrations are written.
- **Do NOT use when:** the model already exists and the task is writing or reviewing the migrations themselves — go to migrations and schema-design instead. Do not use this skill to tune individual queries in a settled schema; that is query-performance.

## Rules

1. **AR-141 — Access patterns first.** List the reads and writes each main screen and job performs before choosing any structure; a schema designed from nouns alone is sent back.
2. **AR-142 — Every entity maps.** Every entity in the requirements maps to a schema object, and every relationship is declared as a foreign key, a reference, or an explicit documented decision to denormalize with its consistency cost stated.
3. **AR-143 — Typed facts, typed columns.** Dates, money, enums, and statuses use typed columns, never strings. Money is integer minor units or a decimal type, never float.
4. **AR-144 — One writable home per fact.** The same fact has exactly one writable home; copies are read models with a named synchronization mechanism and a stated staleness bound.
5. **AR-145 — Index from named queries.** Every query used by a main screen is backed by an index, proven with the database's explain-plan tool, not assumed.
6. **AR-146 — Embed vs reference is decided per relationship.** Embed what is read together and owned together; reference what is shared or independently growing. The decision is recorded for each relationship, not defaulted for the whole store.
7. **AR-147 — One owner per store.** Cross-service data is owned by one service; other services hold references or replicated read models, never shared write access to another service's tables.
8. **AR-148 — Migrations only.** Schema evolution happens only through versioned migrations; manual edits to a live schema are forbidden.
9. **AR-149 — Tenant key from the first migration.** In any multitenant design, tenant-owned tables carry the tenant key from the first migration; retrofitting it later is treated as a redesign, not a migration.
10. **AR-150 — Constraints live in the database.** Integrity invariants (non-null, uniqueness, referential integrity, value ranges) are enforced by database constraints, not by application code alone.
11. **AR-151 — Denormalization is a documented decision.** Every denormalized field names its source of truth and the path that keeps it current; an undocumented copy is a defect.
12. **AR-152 — Every migration has a way back.** Each migration is reversible, or ships with a documented forward-fix procedure; an irreversible migration with neither is not merged.

## BAN list

- **BAN-AR-071 — Stringly-typed facts.** Banned: storing dates, money, enums, or statuses as free-text strings. Defeats: DET-CODE-025. Bad: `orders.status` is a VARCHAR holding 'paid', 'Paid', and 'PAID' from different code paths, and the revenue report silently misses two of the three. Instead: an enum or lookup type with a check constraint, and money as integer minor units. Severity: BLOCK.
- **BAN-AR-072 — Two writable homes for one fact.** Banned: the same fact stored in two places, both writable, updated by different code. Defeats: DET-CODE-007. Bad: the customer's email lives in `users` and `billing_customers`; support updates one, invoices go to the other. Instead: one owning table; the second consumer gets a read model with a named sync mechanism. Severity: BLOCK.
- **BAN-AR-073 — Shared write access across services.** Banned: one service writing directly into another service's tables. Defeats: DET-CODE-014. Bad: the reporting service runs `UPDATE orders SET ...` during its nightly job, bypassing every invariant the orders service enforces. Instead: call the owning service's API, consume its events, or build a replicated read model. Severity: BLOCK.
- **BAN-AR-074 — Unbounded, unindexed main-screen query.** Banned: a query behind a main screen with no index support and no row limit. Defeats: DET-CODE-033. Bad: the admin order list runs `SELECT * FROM orders ORDER BY created_at DESC` over two million rows on every page load. Instead: an index on the sort/filter columns, cursor pagination, and explain-plan evidence attached to the change. Severity: BLOCK.

## Gates

- **G-AR-071 — Migration build check.** Verifies: AR-142, AR-148. Check: automated — CI applies all migrations to an empty database and diffs the resulting schema against the declared model. Pass: migrations apply cleanly and the diff is empty. Fail: block merge. Recorded in: progress.md.
- **G-AR-072 — Explain-plan evidence.** Verifies: AR-145. Check: automated — the test harness runs EXPLAIN for each named main-screen query against a production-shaped dataset. Pass: every query uses its intended index; no sequential scan over a large table. Fail: block the schema change until the index exists. Recorded in: progress.md.
- **G-AR-073 — Duplicate-fact audit.** Verifies: AR-144, AR-151. Check: manual — pick three core facts and trace each to its single writable home, naming the sync mechanism for every copy found. Pass: 3 of 3 facts have exactly one writable home. Fail: block release until the duplicate is demoted to a read model. Recorded in: progress.md.
- **G-AR-074 — Tenant-key schema check (citation).** Verifies: AR-149. Check: automated — this requirement is verified by the canonical tenant-key schema check, G-AR-092 in multitenancy-saas (every tenant-owned table carries a non-null tenant key with a leading index); run that gate for the full procedure and pass criteria. Single-tenant projects record the exemption in ARCHITECTURE.md. Recorded in: progress.md.

## Anti-patterns

- **Noun-per-table modeling.** One generic table per requirement noun, with JSON blob columns absorbing every attribute nobody modeled. Catch it: ask for the access-pattern list; if it does not exist, the tables came from nouns.
- **Index astrology.** Indexes added "just in case," with no named query behind them, bloating writes while the slow query still scans. Catch it: every index should name the query it serves; an index that cannot is removed.
- **The temporary shared database.** Services coupled through one schema "until we split later," with the split never scheduled. Catch it: count the services writing to one schema; more than one means the shortcut became the architecture.
- **Premature sharding.** Data split across nodes or databases before any measured bottleneck exists. Catch it: ask for the load figure that forced the split; "future scale" without a number is the tell.

## Examples

- [Example 1 — Typing a status and a price](examples/example-1.md) — corrects AR-143.
- [Example 2 — One writable home for the customer email](examples/example-2.md) — corrects AR-144.
- [Example 3 — Embed vs reference, decided per relationship](examples/example-3.md) — corrects AR-146.

## Recall anchors

- Access patterns first, nouns last.
- Every fact has one writable home.
- Typed facts get typed columns; money is never float.
- Indexes are proven with explain plans, not assumed.
- Evolution happens only through migrations.

## Checklist

- [ ] The access-pattern list exists and every main screen and job is on it (AR-141).
- [ ] Every requirement entity maps to a schema object; every relationship is declared (AR-142).
- [ ] No stringly-typed dates, money, enums, or statuses; money is integer minor units or decimal (AR-143).
- [ ] Duplicate-fact audit passed: 3 of 3 core facts traced to one writable home (G-AR-073).
- [ ] Explain-plan evidence attached for every named main-screen query (G-AR-072).
- [ ] Tenant-owned tables carry the tenant key from the first migration, or the single-tenant exemption is recorded (AR-149).
- [ ] Every migration is reversible or carries a forward-fix procedure (AR-152).
