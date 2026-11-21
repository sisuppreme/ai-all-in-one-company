# Example 1 — Price stale forever, fixed by TTL plus delete-on-write

## Before

The product page caches the price with no expiry and nothing invalidates it, so a database price change never reaches the site:

```text
Read path:   GET product:42:price  -> miss -> SELECT price_cents FROM products WHERE id = 42
             SET product:42:price 129900        (no TTL)
Write path:  UPDATE products SET price_cents = 119900 WHERE id = 42;
             (cache untouched — the site serves 129900 indefinitely)
```

## After

Every entry carries a TTL as a backstop, and the write path — inside the data-access layer — deletes the affected key in the same operation:

```text
Read path:   GET product:42:price  -> miss -> SELECT price_cents FROM products WHERE id = 42
             SET product:42:price 129900  EX 300        (TTL: 5 minutes)
Write path:  UPDATE products SET price_cents = 119900 WHERE id = 42;
             DEL product:42:price                        (delete-on-write)
Next read repopulates from the database: 119900.
```

**Corrects DB-242, DB-243** — every cached entry has a TTL, and invalidation is delete-on-write with the database as the only source of truth.
