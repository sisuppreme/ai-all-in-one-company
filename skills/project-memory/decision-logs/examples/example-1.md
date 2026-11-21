# Example 1 — Reversal by supersession, not rewrite

## Before

ADR-0007 originally read "We will store application data in SQLite." After the team switches to Postgres, the file is quietly edited:

```markdown
# 0007 — Application database

## Status
Accepted

## Decision
We will store application data in Postgres.
```

The record now claims Postgres was the decision all along. progress.md, two runbooks, and a handover note that cited "ADR-0007 (SQLite)" contradict the file, and nobody can tell when or why the database changed.

## After

ADR-0007 is left exactly as accepted, with only its Status line updated:

```markdown
# 0007 — Application database

## Status
Superseded by ADR-0019

## Decision
We will store application data in SQLite.
```

And a new record carries the reversal:

```markdown
# 0019 — Move application data to Postgres

## Status
Accepted — 2026-11-21, decided by the tech lead

## Context
ADR-0007 chose SQLite for a single-node deployment. The deployment is now
multi-node (fact-sheet: deployment topology), which SQLite file locking
cannot serve.

## Decision
We will store application data in Postgres. This supersedes ADR-0007.

## Consequences
Positive: concurrent writers across nodes. Negative: a database service
must now be provisioned, backed up, and monitored; local development
needs a Postgres container instead of a file.
```

Note: demonstrates PM-108 — an accepted record is immutable except for Status; a reversal is a new ADR that supersedes and links to the old one (defeats BAN-PM-051).
