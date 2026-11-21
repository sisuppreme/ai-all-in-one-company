# Example 1 — Typing a status and a price

## Before

```sql
CREATE TABLE orders (
  id          SERIAL PRIMARY KEY,
  status      VARCHAR(50),          -- 'paid', 'Paid', 'PAID', 'refunded' all occur
  total       DOUBLE PRECISION,     -- 19.99 stored as 19.989999999999998
  placed_on   VARCHAR(10)           -- '03/11/2026' — March 11 or November 3?
);
```

The revenue report filters `status = 'paid'` and silently drops the other two
spellings; the refund job sums floats and is off by cents every month.

## After

```sql
CREATE TYPE order_status AS ENUM ('pending', 'paid', 'shipped', 'refunded', 'cancelled');

CREATE TABLE orders (
  id          SERIAL PRIMARY KEY,
  status      order_status NOT NULL DEFAULT 'pending',
  total_minor INTEGER NOT NULL CHECK (total_minor >= 0),  -- cents; currency in a separate column
  currency    CHAR(3) NOT NULL,
  placed_at   TIMESTAMPTZ NOT NULL
);
```

The type system rejects the bad spellings at write time, money arithmetic is
exact, and the date is unambiguous.

Note: corrects AR-143 — typed facts get typed columns; money is integer minor units or decimal, never float.
