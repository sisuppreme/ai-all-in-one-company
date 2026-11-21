# Example 2 — Separating reference data from sample data

## Before

```text
seeds/seed.sql            -- roles + plans AND 500 fake users AND demo orders,
                          -- run by one command in every environment, including production.
```

## After

```text
seeds/reference.sql       -- roles, plans, lookup values only. Runs everywhere,
                          -- including production, through the release process.
seeds/sample.sql          -- synthetic users/orders for development only.
                             Refuses to run unless APP_ENV is development or test.

# Commands make the separation structural, not a flag someone can forget:
#   pnpm seed:reference        (wired into the production deploy pipeline)
#   pnpm seed:sample           (development only; the production pipeline
#                               never references it — verified by gate G-DB-032)
```

Corrects DB-061 (reference data and sample data are separate classes with separate entry points) and DB-068 (production receives reference data only).
