# Example 1 — Cookie attributes made explicit

## Before

```js
// Session cookie set with framework defaults, nothing declared.
res.cookie('sid', sessionId);
```

The rendered response carries `Set-Cookie: sid=9f31…; Path=/` — no `Secure`, so the session also travels over plain HTTP; no `HttpOnly`, so any script on the page can read it; no `SameSite`, so cross-site requests carry it wherever the browser default allows.

## After

```js
// Attributes declared from the project session policy, on every issue and rotation.
res.cookie('sid', sessionId, {
  secure: true,
  httpOnly: true,
  sameSite: 'lax',
  path: '/',
});
```

The gate (G-SE-011) captures every `Set-Cookie` in the login and authenticated flows and asserts all three attributes are present.

Note: corrects SE-024 — cookie attributes are set explicitly per cookie; framework defaults are verified, not assumed.
