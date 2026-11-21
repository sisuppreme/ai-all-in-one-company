# seed-data

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Prisma documentation, "Seeding" — https://www.prisma.io/docs/orm/v6/prisma-migrate/workflows/seeding
- **Depends on:** migrations
- **Feeds into:** unit-testing, integration-testing, data-quality

## When to use / Do NOT use

- **Use when:** writing or reviewing seed scripts, reference data, development fixtures, or anything that puts rows into a database outside a user action.
- **Do NOT use when:** designing tables (use schema-design), changing schema (use migrations), or generating test data inside a single test's setup (that belongs to the test; this skill governs shared seeds and shipped reference data).

## Rules

1. **DB-061 — Two classes, kept separate.** Seeds come in exactly two classes: (a) required reference data — roles, plans, lookup values — that production also receives through the release process; (b) development-only sample data. The two classes live in separate files/entry points with separate commands. One seed file that does both is a defect.
2. **DB-062 — Idempotent or broken.** Seed scripts upsert by natural key. Running a seed twice produces identical row counts and identical content; a seed that duplicates on re-run is broken, however convenient.
3. **DB-063 — After migrations, never instead of them.** Seeds run against the migrated schema, after the migration set completes. Seed code never creates or alters tables.
4. **DB-064 — Visibly synthetic.** Sample data is synthetic and obviously so: email addresses on reserved domains (`example.test`, `example.com`), clearly placeholder names. Sample data that could be mistaken for a real person is a defect.
5. **DB-065 — Labeled in the data.** Sample records are labeled where they live — a seeded flag, a reserved domain, a dedicated tenant — so any reader, report, or export can tell them from real records without asking anyone.
6. **DB-066 — No production-capable credentials.** No seed creates credentials that work in production. Development logins are documented as development-only and blocked by an environment check in the seed itself, not by convention.
7. **DB-067 — Never copied from production.** Sample data is generated, not harvested. Production records are never copied into seeds — not even "anonymized" by hand.
8. **DB-068 — Production gets reference data only.** The production seed path delivers roles, plans, and lookup values — never demo users, demo testimonials, demo orders, or demo metrics. A production dashboard populated by seed data is fake functionality and fake content at the same time.
9. **DB-069 — Seeds are code, not dumps.** Seed scripts are versioned, reviewed, and re-runnable like migrations. A one-off SQL dump committed once and never maintained is not a seed; it is archaeology.
10. **DB-070 — Reference changes ride the release.** A change to reference data (a new plan, a renamed role) ships through the same review and release process as a migration, in the same change as the code that depends on it.

## BAN list

- **BAN-DB-031 — Production records as seed material.** Banned: copying real production records (users, orders, messages) into development or test seeds, including hand-"anonymized" copies. Defeats: DET-INF-003. Bad: a developer exports the users table, shuffles the names in a spreadsheet, and commits it as `seeds/dev.sql`; real email addresses, phone numbers, and order histories are now in git history forever. Instead: generate synthetic records with a script (DB-064) and mark them in the data (DB-065). Severity: BLOCK.
- **BAN-DB-032 — Sample data shipped to production.** Banned: letting the sample-data seed run in production, or shipping demo users, demo testimonials, or demo metrics in a production database. Defeats: DET-FAKE-014. Bad: the launched site's homepage testimonial carousel is the seeded "Acme Corp" quote, and the admin login is the seeded demo account. Instead: the production pipeline runs the reference-data seed only (DB-068); the sample seed is absent from the production path by construction, verified by G-DB-032. Severity: BLOCK.
- **BAN-DB-033 — The non-idempotent seed.** Banned: seed scripts written as plain unconditional `INSERT`s that add a fresh copy of every row on each run. Defeats: DET-CODE-030. Bad: CI runs the seed before each test batch; by Friday the plans table holds five copies of "Pro," and every lookup by plan name is a coin toss. Instead: upsert by natural key (`ON CONFLICT ... DO UPDATE` or the engine's equivalent) and prove it with the double-run test (G-DB-031). Severity: WARN.
- **BAN-DB-034 — Seed credentials that work in production.** Banned: seed-created logins whose credentials authenticate anywhere outside development (a shared `admin / password123`, a demo account created by a seed that also runs in production). Defeats: DET-CODE-018. Bad: the seeded admin account from the tutorial is live on the production site with its documented password. Instead: development logins are created only by the sample seed, which refuses to run when the environment is production (DB-066). Severity: BLOCK.
- **BAN-DB-035 — Real-looking fake people.** Banned: sample records that imitate real people — plausible personal names paired with real email domains, real phone-number ranges, or real addresses — without a seeded label. Defeats: DET-FAKE-014. Bad: a sample user "Sarah Khan <sarah.khan@gmail.com>" receives a real password-reset email during a staging test, and a support agent cannot tell the account is fake. Instead: reserved domains, obviously placeholder names, and the seeded flag (DB-064, DB-065). Severity: WARN.

## Gates

- **G-DB-031 — Double-run test.** Verifies: DB-062, DB-063. Check: automated — CI migrates an empty database, runs the full seed, records per-table row counts, runs the seed a second time, and asserts identical counts plus a successful application boot. Pass: identical counts, app boots. Fail: block shipment. Recorded in: progress.md.
- **G-DB-032 — Production pipeline scan.** Verifies: DB-061, DB-068. Check: automated — CI greps the production deploy pipeline configuration for the sample-seed command/entry point; the reference-seed step must be present and named, the sample step must be absent. Pass: zero sample-seed references in the production path. Fail: block shipment. Recorded in: progress.md.
- **G-DB-033 — Synthetic-data scan.** Verifies: DB-064, DB-066. Check: automated — grep seed files for email addresses on non-reserved domains and for credential literals outside the documented development-login list; zero hits allowed. Pass: zero hits. Fail: block shipment. Recorded in: progress.md.
- **G-DB-034 — Class separation check.** Verifies: DB-061. Check: automated — a script asserts reference and sample seeds live in separate paths and that the production seed command imports/loads only the reference module. Pass: separation holds by file layout, not by a flag someone can forget. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The fossil dump.** A SQL dump committed once at project start, drifting further from the schema every month, failing a little differently on each new machine. Catch it: ask when the seed last ran green from an empty database; if nobody knows, it is a fossil.
- **Anonymization theater.** Real records with names shuffled by hand, still re-identifiable from emails, timestamps, and amounts. Catch it: if any field in the seed came from a production export, the whole file is production data (BAN-DB-031).
- **Seed creep.** Tests, demos, and screenshots quietly come to depend on specific fake users and their exact data, so the seed can never change. Catch it: change one sample record's name; whatever breaks was depending on sample data as if it were a contract.
- **The helpful demo account.** A "temporary" demo login created for a sales walkthrough that survives into the production launch checklist. Catch it: list every account the seeds create and ask, for each one, in which environments it can authenticate.

## Examples

- [Example 1 — An idempotent reference seed](examples/example-1.md) — corrects DB-062.
- [Example 2 — Separating reference data from sample data](examples/example-2.md) — corrects DB-061, DB-068.
- [Example 3 — Synthetic, labeled sample users](examples/example-3.md) — corrects DB-064, DB-065.

## Recall anchors

- Two classes: reference data ships, sample data never does.
- Run the seed twice; the second run changes nothing.
- Synthetic, labeled, reserved domains — never copied from production.
- No seed creates a credential that works in production.
- Sample data in a production surface is fake content, full stop.

## Checklist

- [ ] Reference and sample seeds are separate files with separate commands (DB-061, G-DB-034).
- [ ] The double-run test passes with identical row counts (DB-062, G-DB-031).
- [ ] The production pipeline contains no sample-seed step (DB-068, G-DB-032).
- [ ] Sample records use reserved domains and carry a seeded label (DB-064, DB-065, G-DB-033).
- [ ] No production record was copied into any seed file (DB-067).
- [ ] Development logins are environment-guarded and cannot authenticate in production (DB-066).
