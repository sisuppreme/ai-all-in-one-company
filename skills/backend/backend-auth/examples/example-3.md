# Example 3 — Enumerating login errors replaced by one generic failure

## Before

```ts
app.post("/auth/login", async (req, res) => {
  const user = await db.users.findByEmail(req.body.email);
  if (!user) {
    return res.status(404).json({ error: "No account with that email" });
  }
  if (!(await argon2.verify(user.passwordHash, req.body.password))) {
    return res.status(401).json({ error: "Wrong password" });
  }
  // …
});
```

Two different answers turn the login form into an account-existence oracle:
an attacker feeds it an email list and keeps every address the API confirms
has an account, then aims password attacks only at those.

## After

```ts
app.post("/auth/login", async (req, res) => {
  const user = await db.users.findByEmail(req.body.email);
  // Verify against a dummy hash when the account does not exist, so the
  // work performed — and the response — are the same in both cases.
  const hash = user?.passwordHash ?? DUMMY_ARGON2_HASH;
  const passwordOk = await argon2.verify(hash, req.body.password);

  if (!user || !passwordOk) {
    return res.status(401).json(problem(401, "Invalid email or password"));
  }
  // …issue the session (BE-103, BE-104)
});
```

Unknown account and wrong password now produce the same status, the same
body, and near-identical timing. The form still tells a real user everything
they need — "that combination did not work" — and tells an enumerator
nothing.

Note: corrects BE-108 — failed-login responses are identical for an unknown account and a wrong password; the endpoint never confirms whether an account exists.
