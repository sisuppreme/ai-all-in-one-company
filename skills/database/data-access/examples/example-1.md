# Example 1 — Interpolated query replaced by a bound parameter

## Before

The login lookup builds SQL by concatenating user input directly into the query text:

```sql
-- Built in application code as a string:
SELECT id, password_hash
FROM users
WHERE email = '<value of the email form field, concatenated in>';
-- Submitting  ' OR '1'='1  as the email turns the predicate into a tautology
-- and returns the first user in the table.
```

## After

The same lookup passes the value as a bound parameter; the database treats it as data, never as SQL:

```sql
-- Query text is constant; $1 is bound by the driver:
SELECT id, password_hash
FROM users
WHERE email = $1;
-- Bind: $1 = the submitted email, whatever it contains.
```

**Corrects DB-182** — all values reach SQL as bound parameters; string-built SQL fails lint and review.
