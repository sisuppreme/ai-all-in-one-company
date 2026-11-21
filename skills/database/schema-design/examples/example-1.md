# Example 1 — Money and time types

## Before

```sql
CREATE TABLE products (
  id          serial PRIMARY KEY,
  name        varchar(200),
  price       double precision,          -- money in a float: 19.99 becomes 19.989999...
  created_at  varchar(30)                -- local time as a string: "21/11/2026 6:44 PM"
);
```

## After

```sql
CREATE TABLE products (
  id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name        varchar(200) NOT NULL,
  price_cents integer NOT NULL CHECK (price_cents >= 0),  -- money as integer minor units
  created_at  timestamptz NOT NULL DEFAULT now()          -- one unambiguous instant
);
```

Corrects DB-005 (money is integer minor units or numeric, never float) and DB-006 (timestamps are timestamptz).
