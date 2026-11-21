# Example 1 — Whole-table list endpoint replaced by a clamped maximum

## Before

```js
// The client picks the page size. A single request can pull the
// entire table into memory and return it.
app.get("/api/users", requireAuth, async (req, res) => {
  const limit = Number(req.query.limit ?? 50);
  const users = await db.users.list({ limit });
  res.json(users);
});
```

## After

```js
// The maximum is configuration with an owner; requests above it are
// clamped, never executed as asked.
const MAX_PAGE_SIZE = config.get("limits.list.maxPageSize"); // 200, owner: api-team

app.get("/api/users", requireAuth, async (req, res) => {
  const requested = Number(req.query.limit ?? 50);
  const limit = Math.min(Math.max(requested, 1), MAX_PAGE_SIZE);
  const users = await db.users.list({ limit });
  res.json({ data: users, pageSize: limit, maxPageSize: MAX_PAGE_SIZE });
});
```

Note: the slop version executed whatever page size the client asked for; the corrected version clamps every list request to the documented maximum — BE-304.
