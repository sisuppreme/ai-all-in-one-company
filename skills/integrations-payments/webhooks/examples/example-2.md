# Example 2 — Replacing check-then-insert with a unique constraint and a converging handler

Corrects IN-104 (and IN-106): deduplication is a database constraint on the provider event ID, and the handler sets state instead of incrementing it.

## Before

```js
async function handlePaymentSucceeded(event) {
  // Race: two concurrent duplicate deliveries both pass this check.
  const seen = await db.query("SELECT id FROM events WHERE provider_id = $1", [event.id]);
  if (seen.rows.length > 0) return;
  await db.query("INSERT INTO events (provider_id) VALUES ($1)", [event.id]);

  // Incrementing: one provider retry credits the customer twice.
  await db.query("UPDATE accounts SET credits = credits + $1 WHERE id = $2",
    [event.data.object.amount, event.data.object.metadata.accountId]);
}
```

## After

```sql
-- The constraint is the deduplication. A duplicate insert collides and
-- is acknowledged as already-received; there is no check to race.
CREATE UNIQUE INDEX events_provider_id_key ON events (provider_id);
```

```js
async function handlePaymentSucceeded(event) {
  const inserted = await db.query(
    `INSERT INTO events (provider_id, type, payload) VALUES ($1, $2, $3)
     ON CONFLICT (provider_id) DO NOTHING RETURNING id`,
    [event.id, event.type, event]
  );
  if (inserted.rows.length === 0) return; // duplicate delivery: no-op

  // Convergence: set the mirror to the payment's state, never add to it.
  // Replaying this event any number of times leaves the same balance.
  await db.query(
    `UPDATE orders SET status = 'paid', provider_payment_id = $1, paid_amount = $2
     WHERE id = $3`,
    [event.data.object.id, event.data.object.amount, event.data.object.metadata.orderId]
  );
}
```

Note: the "before" pair races on concurrent duplicates and double-credits on a retry; the "after" pair makes the duplicate collide on a unique constraint and converges state, per IN-104.
