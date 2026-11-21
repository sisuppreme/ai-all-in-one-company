# Example 3 — Logout that actually ends the session

## Before

```js
app.post('/logout', (req, res) => {
  res.clearCookie('sid'); // browser forgets it; the server-side session stays valid
  res.redirect('/login');
});
```

Anyone holding the old session ID — from a log, a shared machine, or a stolen cookie — replays it after "logout" and is still signed in.

## After

```js
app.post('/logout', async (req, res) => {
  await req.session.destroy(); // server-side record deleted in the same request
  res.clearCookie('sid');
  res.redirect('/login');
});
```

The replay gate (G-SE-013) captures the session ID, logs out, replays the ID, and requires a 401 or a redirect to login.

Note: corrects SE-027 — logout invalidates the session server-side, not just in the browser.
