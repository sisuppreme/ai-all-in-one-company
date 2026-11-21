# Example 3 — Cache outage taking the site down, fixed by database fallback

## Before

Reads treat a cache error as fatal: when Redis restarts, every product page returns a 500 instead of reading the database:

```text
def product_price(id):
    price = redis.get(f"product:{id}:price")   # raises ConnectionError when Redis is down
    if price is None:
        price = db.query("SELECT price_cents FROM products WHERE id = $1", id)
        redis.set(f"product:{id}:price", price)
    return price
# The exception escapes before the fallback runs. Cache down = site down.
```

## After

Cache access is wrapped so any cache failure degrades to a database read; the drill (G-DB-124) verifies this with the cache stopped:

```text
def product_price(id):
    try:
        price = cache.get(key_for("product", id, field="price"))
        if price is not None: return price
    except CacheUnavailable:
        pass                                    # fall through to the database
    price = db.query("SELECT price_cents FROM products WHERE id = $1", id)
    try: cache.set(key_for("product", id, field="price"), price, ttl=300)
    except CacheUnavailable: pass               # caching is best-effort
    return price
# Cache down = slower responses, correct data. Verified by the cache-down drill.
```

**Corrects DB-246** — the application runs correctly with the cache flushed or down; a cache failure never becomes wrong data or an outage.
