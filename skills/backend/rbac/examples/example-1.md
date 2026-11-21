# Example 1 — A hidden button replaced by a server-side check

## Before

The React client hides the delete button for non-admins, and the API trusts
that hiding:

```js
// client: {user.role === 'admin' && <button onClick={del}>Delete user</button>}

// server: no check at all
app.delete('/users/:id', async (req, res) => {
  await db.users.delete(req.params.id);
  res.status(204).end();
});
```

Any signed-in member who replays the request with curl deletes any user.
The permission exists only as a rendering condition.

## After

The route carries a policy entry, and the server enforces it on every
request. The client still hides the button — as presentation, not as the
check:

```js
// policy.js — the matrix from the repo, as data
const POLICY = {
  'users:delete': ['admin'],
  'users:read':   ['admin', 'support', 'member'],
};

function requirePermission(action) {
  return (req, res, next) => {
    const role = req.session.user.role; // server-side record, never the request
    if (!POLICY[action]?.includes(role)) {
      audit.denied({ actor: req.session.user.id, action, target: req.params.id });
      return res.status(403).json({ error: 'forbidden' });
    }
    next();
  };
}

app.delete('/users/:id', requirePermission('users:delete'), async (req, res) => {
  await db.users.delete(req.params.id);
  res.status(204).end();
});
```

A member's replayed request now gets 403, and the denial is in the audit
log. An action missing from `POLICY` grants nobody access.

Note: corrects BE-122 — every protected operation is authorized on the server, per request; UI visibility is never the check.
