# Example 2 — Hand-maintained test schema, corrected to real migrations

## Before

The test harness builds its database from `test/schema.sql`, a file someone
copied from production months ago and edits by hand when a test complains:

```yaml
# CI setup, before
- run: psql $TEST_DATABASE_URL -f test/schema.sql
- run: npm run test:integration
```

A new migration adds a `NOT NULL` column with a default in production. The
hand-copied schema never gets the column, so the integration layer stays
green while the real deploy fails — the suite certified a database that
production never runs.

## After

The harness starts a throwaway database and builds it with the project's
own migration command — the same code path as a production deploy:

```yaml
# CI setup, after
- run: docker compose up -d db-test
- run: npm run db:migrate        # the project's real migrations, in order
- run: npm run test:integration
```

`test/schema.sql` is deleted. Schema drift between test and production is
now impossible by construction, and reverting one migration turns the
suite red (the G-QA-012 negative control proves it on every change).

Note: corrects QA-021 — the database under test is created by the project's real migrations, never a hand-maintained test schema.
