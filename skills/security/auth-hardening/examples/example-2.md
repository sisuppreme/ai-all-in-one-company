# Example 2 — Login endpoint gains throttling and generic errors

## Before

```js
app.post('/login', async (req, res) => {
  const user = await db.users.findByEmail(req.body.email);
  if (!user) return res.status(404).json({ error: 'No account for that email' });
  if (user.passwordHash !== sha256(req.body.password))
    return res.status(401).json({ error: 'Wrong password' });
  return res.json({ session: createSession(user) });
});
```

No rate limit, account enumeration via distinct errors, and a fast hash — an open invitation to credential stuffing.

## After

```js
app.post('/login',
  rateLimit({ key: req => req.body.email + ':' + req.ip,
              limit: config.auth.loginLimit, delayAfter: 5 }),
  async (req, res) => {
    const user = await db.users.findByEmail(req.body.email);
    const ok = user && await argon2.verify(user.passwordHash, req.body.password);
    await logAuthEvent({ email: req.body.email, ip: req.ip, success: !!ok });
    if (!ok) return res.status(401).json({ error: 'Invalid email or password' });
    return res.json({ session: createSession(user) });
  });
```

One generic failure response, per-account-plus-IP throttling with progressive delay, KDF verification, and every attempt logged.

## Note

Corrects SE-065 (strictest rate limits on auth), SE-066 (progressive delay), and SE-067 (generic failure responses).
