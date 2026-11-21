# D5 Example — Schema and Seed Data for Orders and Users

## Scenario

D5 designs the first production schema for the SaaS (users, plans, orders)
and the seed system that supports development and demos. The scenario is
data handling itself, so the sample rows below are synthetic fixtures —
labeled as such in the data, per the seed-data rules they demonstrate.

## Before

```sql
CREATE TABLE users (
  id SERIAL, name VARCHAR(100), email VARCHAR(255),   -- no UNIQUE
  created VARCHAR(30)                                  -- dates as strings
);
CREATE TABLE orders (
  id SERIAL, user_email VARCHAR(255),                  -- no foreign key
  total FLOAT,                                         -- money as float
  status VARCHAR(20)                                   -- any string allowed
);
-- invariant enforced in app code: "an email may register only once"
```

```ts
// seed.ts — runs in every environment, including production
await db.insert(users, [
  { name: "Sarah Mitchell", email: "sarah.mitchell@gmail.com" },
  { name: "James Carter",  email: "j.carter@outlook.com" },
  { name: "Admin", email: "admin@app.io", password: "admin123" },
]);
await db.insert(plans, [ { name: "Pro", price: 12.00 } ]); // plain INSERTs, re-runs duplicate
```

## What the skills caught

- **BAN-DB-001 — App-only invariants**: email uniqueness lives in a code
  comment. **DB-002 — Invariants live in the database**; two racing
  signups both pass the app check — **BAN-DB-003 — Check-then-insert on a
  natural key**.
- **DB-005 — Money is never a float**: `total FLOAT` will drift by cents.
  **DB-006 — Time is `timestamptz`**: string dates sort wrong and carry
  no zone. **DB-004 — Foreign keys are complete**: `user_email` as a
  string reference can point at nobody. Gate **G-DB-002** fails.
- **BAN-DB-035 — Real-looking fake people**: plausible names with
  real-domain emails — **DET-FAKE-014 — Seed data shipped as real
  users**. **DB-064 — Visibly synthetic** and **DB-065 — Labeled in the
  data** both fail; the synthetic-data scan **G-DB-033** flags the file.
- **BAN-DB-034 — Seed credentials that work in production**: `admin123`
  on an admin account, in a seed that runs everywhere. **DB-066**.
- **BAN-DB-033 — The non-idempotent seed**: plain INSERTs duplicate rows
  on every re-run, violating **DB-062 — Idempotent or broken**; the
  double-run test **G-DB-031** fails.
- One seed for all environments violates **DB-061 — Two classes, kept
  separate** and **DB-068 — Production gets reference data only**; the
  production pipeline scan **G-DB-032** blocks the deploy.

## After

```sql
CREATE TABLE users (
  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,                       -- invariant in the database
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE orders (
  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  user_id BIGINT NOT NULL REFERENCES users(id),
  total_cents INTEGER NOT NULL CHECK (total_cents >= 0),  -- money as integer cents
  status TEXT NOT NULL CHECK (status IN ('pending_payment','paid','refunded','failed')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

Seeds split into the two classes (**DB-061**). Reference data — the plan
catalog the operator actually sells — is versioned and rides the release
(**DB-070**), applied after migrations (**DB-063**), idempotently:

```sql
INSERT INTO plans (code, name, price_cents) VALUES ('pro', 'Pro', 1200)
ON CONFLICT (code) DO UPDATE SET price_cents = EXCLUDED.price_cents;
```

Development fixtures live in a separate dev-only file guarded by an
environment check that refuses production: users are visibly synthetic
(`fixture+001@example.invalid`, names like "Fixture User 001", a
`synthetic` flag set in the row itself — **DB-064**, **DB-065**), and no
fixture carries a usable credential (**DB-066**).

## Skills used

- [schema-design](../skills/database/schema-design/SKILL.md)
- [seed-data](../skills/database/seed-data/SKILL.md)
- [migrations](../skills/database/migrations/SKILL.md)
- [data-access](../skills/database/data-access/SKILL.md)
