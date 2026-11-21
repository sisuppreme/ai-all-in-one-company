# schema-design

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Ruby on Rails Guides, "Active Record Migrations" (schema conventions) — https://guides.rubyonrails.org/v7.1.3/active_record_migrations.html
- **Depends on:** data-architecture
- **Feeds into:** migrations, sql-fundamentals, tenant-isolation, data-access

## When to use / Do NOT use

- **Use when:** creating or changing any table, column, constraint, or index; reviewing a schema proposed by a person or a model; deciding types for money, time, and identifiers.
- **Do NOT use when:** writing queries against an existing schema (use sql-fundamentals), moving a schema between versions (use migrations), or choosing a NoSQL store (use nosql-patterns).

## Rules

1. **DB-001 — Model from the domain.** Entities and relationships are modeled first, then mapped to tables: one table per aggregate root, relationships as foreign keys. A table that mirrors a screen or an API payload instead of the domain is redesigned before it ships.
2. **DB-002 — Invariants live in the database.** Every invariant the business depends on exists as a database constraint (`NOT NULL`, `UNIQUE`, `CHECK`, or a foreign key), not only as an application check. If the app is the only thing enforcing it, the rule is not yet implemented.
3. **DB-003 — Keys.** Every table has a primary key. Surrogate keys (UUID or identity) are the default; natural keys (email, SKU, slug) are additionally protected by a unique constraint.
4. **DB-004 — Foreign keys are complete.** Every foreign key column is indexed, and every foreign key declares explicit `ON DELETE` behavior. A foreign key with the engine default delete behavior chosen by silence is a defect.
5. **DB-005 — Money is never a float.** Money is stored as integer minor units or `numeric` with an explicit scale. `float`, `double precision`, and `real` columns never hold money.
6. **DB-006 — Time is `timestamptz`.** Timestamps are stored as `timestamptz`; local-time strings and `timestamp without time zone` are not used for recorded events.
7. **DB-007 — Normalize by default.** The schema is normalized to 3NF. Denormalization happens only for a measured read pattern, and the reason is recorded in SCHEMA.md next to the duplicated field.
8. **DB-008 — Nullability is deliberate.** Each nullable column is a decision, not a default. A nullable column whose meaning is not obvious from its name is documented in SCHEMA.md.
9. **DB-009 — Soft delete is a product decision.** Rows are hard-deleted unless a written retention rule (legal hold, audit, undo window) requires soft delete; the rule names the retention period and who can see deleted rows.
10. **DB-010 — SCHEMA.md moves with the schema.** SCHEMA.md is updated in the same change as the migration that alters the schema. A schema change whose documentation lands "later" does not merge.
11. **DB-011 — The dump is generated.** The committed schema file is produced by the migration run. It is never edited by hand to match a database.

## BAN list

- **BAN-DB-001 — App-only invariants.** Banned: enforcing a business invariant (non-negative balance, one active subscription per user) only in application code with no database constraint behind it. Defeats: DET-CODE-030. Bad: the service checks `if (balance >= amount)` before decrementing; two concurrent withdrawals both pass the check and the account goes negative. Instead: add the `CHECK`/`UNIQUE` constraint the invariant implies, and let the database reject the second write. Severity: BLOCK.
- **BAN-DB-002 — Hand-applied production schema.** Banned: changing the production schema by hand in a SQL console, or enabling ORM auto-sync (`synchronize: true` and equivalents) against production. Defeats: DET-INF-018. Bad: an `ALTER TABLE` run in a console during an incident; no file records it and staging diverges from production from that day. Instead: every schema change is a versioned migration applied by the runner (see migrations). Severity: BLOCK.
- **BAN-DB-003 — Check-then-insert on a natural key.** Banned: "look up the email, insert if absent" (and the same shape for slugs, SKUs, idempotency keys) without a unique constraint on that key. Defeats: DET-CODE-030. Bad: a double-submitted signup inserts two rows for one email; every later lookup by email is ambiguous. Instead: declare `UNIQUE` on the natural key and upsert or handle the constraint violation. Severity: BLOCK.
- **BAN-DB-004 — EAV / JSON-blob core entities.** Banned: modeling a core entity (orders, users, payments) as entity-attribute-value rows or one untyped JSON blob column to "stay flexible." Defeats: DET-CODE-015. Bad: `entities(id, attrs jsonb)` holds orders, so no column can be constrained, indexed, or reported on. Instead: real tables and columns for the core model; JSONB is reserved for genuinely variable, non-queried attributes. Severity: WARN.

## Gates

- **G-DB-001 — Schema lint.** Verifies: DB-003, DB-004. Check: automated — CI queries the live catalog of the migrated test database and fails on any violation of the invariant: every table has a primary key, every foreign key column is indexed, and every index and constraint the schema declares exists in the live catalog. The catalog query takes the database's native form — PostgreSQL: `pg_catalog`/`information_schema`; SQLite: `sqlite_master` and `PRAGMA index_list`; MySQL: `information_schema`. Pass: zero findings. Fail: block shipment. Recorded in: progress.md.
- **G-DB-002 — Constraint-presence check.** Verifies: DB-002. Check: automated — a script reads the invariants listed in SCHEMA.md and asserts each names a constraint that exists in the live catalog of the test database. The catalog query takes the database's native form — PostgreSQL: `pg_constraint`/`information_schema`; SQLite: `sqlite_master` and `PRAGMA foreign_key_list`/`PRAGMA index_list`; MySQL: `information_schema` (`TABLE_CONSTRAINTS`/`KEY_COLUMN_USAGE`). The invariant is engine-independent: every listed invariant maps to a named constraint in whichever catalog the chosen engine exposes. Pass: every listed invariant maps to a named constraint. Fail: block shipment. Recorded in: progress.md.
- **G-DB-003 — Type audit.** Verifies: DB-005, DB-006. Check: automated — grep migration files for `float|double precision|real` on money-named columns and for `timestamp without time zone`; zero hits allowed. Pass: zero hits. Fail: block shipment. Recorded in: progress.md.
- **G-DB-004 — Documentation freshness.** Verifies: DB-010, DB-011. Check: automated — CI fails a change that adds or edits a migration without touching SCHEMA.md, and fails if the committed schema dump differs from a fresh migration run's output. Pass: docs and dump both current. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The nullable swamp.** Every column is nullable "to be safe," so no row means anything definite. Catch it: count nullable columns per table; each one you cannot justify in a sentence gets a `NOT NULL` and a default or a documented reason.
- **The god table.** One table accretes every feature's columns (users gain `last_coupon_code`, `temp_import_flag`, …). Catch it: if a column is meaningful for only one feature or one row type, it belongs in its own table.
- **Premature denormalization.** A value is copied into a second table "for performance" with no measured slow query behind it. Catch it: ask for the `EXPLAIN` that forced the copy; if none exists, normalize and delete the copy.
- **Phantom constraints.** The ORM model declares `unique: true` or a validation, everyone believes the database enforces it, and the actual catalog has no such constraint because sync never ran. Catch it: dump the real constraints from `pg_constraint` and diff against what the models claim.

## Examples

- [Example 1 — Money and time types](examples/example-1.md) — corrects DB-005, DB-006.
- [Example 2 — An invariant becomes a constraint](examples/example-2.md) — corrects DB-002, DB-003.
- [Example 3 — A complete foreign key](examples/example-3.md) — corrects DB-004.

## Recall anchors

- If the app is the only enforcer, the invariant does not exist.
- Money is integer minor units or numeric — never float.
- Every foreign key: indexed, with an explicit ON DELETE.
- SCHEMA.md changes in the same commit as the schema.
- The schema dump is generated, never edited.

## Checklist

- [ ] Every business invariant in the design exists as a named database constraint (DB-002, G-DB-002).
- [ ] Every table has a primary key; every natural key has a unique constraint (DB-003).
- [ ] Every foreign key column is indexed and declares ON DELETE behavior (DB-004, G-DB-001).
- [ ] No money column uses a floating-point type; timestamps are timestamptz (DB-005, DB-006, G-DB-003).
- [ ] Any denormalized field names its measured reason in SCHEMA.md (DB-007).
- [ ] SCHEMA.md and the generated schema dump are updated in this change (DB-010, DB-011, G-DB-004).
