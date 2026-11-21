# Example 1 — Parameterized query

Note: demonstrates SE-002 — queries use bound parameters, never string-built SQL (BAN-SE-001, DET-CODE-017).

## Before

```js
// Order lookup: the request value is interpolated straight into the query.
// A request to /orders/1 OR 1=1 -- returns every order in the table.
app.get("/orders/:id", async (req, res) => {
  const rows = await db.query(
    `SELECT id, user_id, total FROM orders WHERE id = ${req.params.id}`
  );
  res.json(rows);
});
```

## After

```js
// The value travels as a bound parameter ($1); the database treats it as
// data, never as SQL, whatever the client sends.
app.get("/orders/:id", async (req, res) => {
  const rows = await db.query(
    "SELECT id, user_id, total FROM orders WHERE id = $1",
    [req.params.id]
  );
  res.json(rows);
});
```
