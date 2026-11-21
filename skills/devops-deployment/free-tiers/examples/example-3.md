# Example 3 — Expiring free database with no expiry recorded

## Before

A free PostgreSQL instance is created on day one of the project and loaded with the seed data and early user records. Nobody records that the free tier expires the instance 30 days after creation. On day 30 — launch week — the database is deleted by the provider, and the only copy of the data goes with it.

## After

On creation day, the free-tier sheet gains a row: "PostgreSQL (free) — expires 30 days after creation; created 2026-11-21, expires 2026-12-21; reminder set for 2026-12-14; before expiry: export a full backup and migrate to the named paid/first-step database." The expiry is checked at every launch review, and the migration step is scheduled work, not a surprise.

Note: corrects DO-167 — the expiry date of a time-limited free resource is recorded the day it is created, with a reminder and a migration step ahead of it.
