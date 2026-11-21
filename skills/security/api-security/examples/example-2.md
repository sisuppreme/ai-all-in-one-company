# Example 2 — Allowlist serializer instead of the raw record

## Before

```js
// Returns the whole stored record, including fields never meant for clients
app.get('/users/:id', requireAuth, async (req, res) => {
  const user = await db.users.findById(req.params.id);
  res.json(user); // leaks passwordHash, emailVerifiedToken, internalNotes
});

// And the write side mass-assigns whatever the client sends
app.patch('/users/:id', requireAuth, async (req, res) => {
  await db.users.update(req.params.id, req.body); // client can set role: 'admin'
  res.status(204).end();
});
```

## After

```js
const publicUser = (u) => ({
  id: u.id,
  displayName: u.displayName,
  avatarUrl: u.avatarUrl,
});

const writableUserFields = ['displayName', 'avatarUrl', 'locale'];

app.get('/users/:id', requireAuth, async (req, res) => {
  const user = await db.users.findById(req.params.id);
  res.json(publicUser(user));
});

app.patch('/users/:id', requireAuth, async (req, res) => {
  const patch = pick(req.body, writableUserFields); // role is not writable here
  await db.users.update(req.params.id, patch);
  res.status(204).end();
});
```

Note: demonstrates SE-044 — responses and writes are filtered at property level by explicit allowlists (API3/BOPLA).
