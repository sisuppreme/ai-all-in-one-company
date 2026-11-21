# Example 1 — Parameterizing a search query

## Before

```sql
-- Built by string interpolation in the endpoint (shown as the final SQL for input q = x' OR '1'='1):
SELECT id, email FROM users WHERE email LIKE '%x' OR '1'='1%';
-- ...and the sort parameter interpolated directly: ORDER BY ${sort}
```

## After

```sql
-- The value is a bound parameter ($1); it can only ever match literally:
SELECT id, email
FROM users
WHERE email LIKE '%' || $1 || '%'
ORDER BY created_at DESC
LIMIT 50;

-- The sort direction/column is chosen from a server-side allowlist, never from raw input:
--   { "newest": "created_at DESC", "oldest": "created_at ASC", "email": "email ASC" }
-- An unknown sort token is rejected with a 400 before any SQL is built.
```

Corrects DB-021 (every value reaches SQL as a bound parameter) and DB-022 (identifiers come only from allowlists).
