# Example 2 — Rotation at login defeats fixation

## Before

```js
app.post('/login', async (req, res) => {
  const user = await authenticate(req.body.email, req.body.password);
  req.session.userId = user.id; // same anonymous session ID, now authenticated
  res.redirect('/account');
});
```

An attacker who plants their own anonymous session ID in the victim's browser (via a subdomain or a shared device) owns the session after the victim logs in — the planted ID was never replaced.

## After

```js
app.post('/login', async (req, res) => {
  const user = await authenticate(req.body.email, req.body.password);
  await req.session.regenerate(); // new ID issued; pre-login ID invalidated server-side
  req.session.userId = user.id;
  res.redirect('/account');
});
```

The fixation gate (G-SE-012) logs in with a recorded pre-login ID and asserts the post-login ID differs and the old ID is rejected.

Note: corrects SE-023 — a new session ID is issued at authentication and the pre-login ID is discarded.
