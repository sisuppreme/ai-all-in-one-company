# Example 1 — The callback that trusted the redirect

Corrects IN-164 — ID tokens are validated server-side, every time.

## Before

```js
// OAuth callback route
app.get('/auth/callback', async (req, res) => {
  const { id_token } = await exchangeCode(req.query.code);
  // Decode (not verify) the payload and trust it
  const payload = JSON.parse(Buffer.from(id_token.split('.')[1], 'base64url'));
  const user = await users.findOrCreate({ email: payload.email });
  req.session.userId = user.id;
  res.redirect('/dashboard');
});
```

Anyone can post a self-made JWT with any `email` in the payload and be signed in as that person — the signature is never checked, so the "login" accepts any input (DET-FAKE-001).

## After

```js
// OAuth callback route
app.get('/auth/callback', async (req, res) => {
  if (req.query.state !== req.session.oauthState) throw new Error('state mismatch');
  const { id_token } = await exchangeCode(req.query.code);
  // Verify signature against the issuer's JWKS, plus iss, aud, exp, nonce
  const payload = await verifyIdToken(id_token, {
    jwksUri: ISSUER_JWKS_URI,
    issuer: EXPECTED_ISS,
    audience: CLIENT_ID,
    nonce: req.session.oauthNonce,
  });
  const identity = await identities.findOrCreate({
    iss: payload.iss,
    sub: payload.sub,
    email: payload.email,
  });
  req.session.userId = identity.userId;
  res.redirect('/dashboard');
});
```

Forged or tampered tokens fail signature verification; a token issued to another app fails `aud`; a replayed token fails `nonce`. Only a validated identity creates a session.
