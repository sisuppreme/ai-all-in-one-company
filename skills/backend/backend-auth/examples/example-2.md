# Example 2 — Theatrical reset replaced by a real credential change

## Before

```ts
app.post("/auth/reset", async (req, res) => {
  // Any code is accepted; nothing is checked and nothing changes.
  res.json({ ok: true, message: "Password updated" });
});
```

The user sees "Password updated," the old password keeps working, and an
attacker who finds the endpoint learns it demands nothing at all. The flow
performs a reset without performing one.

## After

```ts
app.post("/auth/reset/request", async (req, res) => {
  const user = await db.users.findByEmail(req.body.email);
  if (user) {
    const token = randomToken(32);
    await db.resetTokens.create({
      userId: user.id,
      tokenHash: sha256(token), // store the hash, email the token
      expiresAt: Date.now() + 30 * 60 * 1000,
      usedAt: null,
    });
    await queue.add("send-email", { to: user.email, template: "reset", token });
  }
  // Identical response whether or not the account exists (BE-108):
  res.status(202).json({ message: "If an account exists, a reset link is on its way" });
});

app.post("/auth/reset/complete", async (req, res) => {
  const record = await db.resetTokens.findByHash(sha256(req.body.token));
  if (!record || record.usedAt || record.expiresAt < Date.now()) {
    return res.status(400).json(problem(400, "Reset link is invalid or expired"));
  }
  await db.transaction(async (tx) => {
    await tx.users.setPasswordHash(record.userId, await argon2.hash(req.body.newPassword));
    await tx.resetTokens.markUsed(record.id);
    await tx.sessions.revokeAllForUser(record.userId); // every existing session dies
  });
  res.status(204).end();
});
```

The token is single-use and expiring, only its hash is stored, completing
the reset actually replaces the credential, and every session opened before
the reset is revoked — so a reset after a compromise locks the attacker out
instead of leaving their session alive.

Note: corrects BE-107 — a reset is a credential change: single-use expiring token, stored credential replaced, all existing sessions revoked.
