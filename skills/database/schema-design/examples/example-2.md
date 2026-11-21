# Example 2 — An invariant becomes a constraint

## Before

```sql
-- Stock is decremented by application code that checks first:
--   if product.stock >= qty: product.stock -= qty; save(product)
-- Two concurrent checkouts both pass the check; stock ends negative.
CREATE TABLE products (
  id    bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  sku   varchar(40),              -- duplicates possible: nothing enforces uniqueness
  stock integer                   -- negative values possible: nothing enforces the floor
);
```

## After

```sql
CREATE TABLE products (
  id    bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  sku   varchar(40) NOT NULL UNIQUE,        -- natural key protected (DB-003)
  stock integer NOT NULL CHECK (stock >= 0) -- the invariant lives in the database (DB-002)
);

-- The decrement itself is one atomic statement; the CHECK rejects any result below zero:
UPDATE products SET stock = stock - 2 WHERE sku = 'WIDGET-1';
```

Corrects DB-002 (every business invariant exists as a database constraint) and DB-003 (natural keys are protected by a unique constraint).
