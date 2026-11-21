# Example 3 — Implicit flow in a single-page app

Corrects IN-161, IN-170 — Authorization code flow with PKCE for every client; tokens never travel in URLs.

## Before

```js
// SPA login: implicit flow
const authorizeUrl =
  `https://provider.example/authorize?response_type=token` +
  `&client_id=${CLIENT_ID}&redirect_uri=${location.origin}/callback`;

// Callback page: read the token out of the URL fragment
const token = new URLSearchParams(location.hash.slice(1)).get('access_token');
localStorage.setItem('access_token', token);
localStorage.setItem('isLoggedIn', 'true');
```

The token leaks into browser history, logs, and any script on the page, and the "session" is a storage flag anyone can edit (DET-FAKE-002).

## After

```js
// SPA login: authorization code flow with PKCE (S256)
const verifier = randomString(64);
const challenge = base64url(await sha256(verifier));
sessionStorage.setItem('pkce_verifier', verifier);
const state = randomString(32);
sessionStorage.setItem('oauth_state', state);

location.href =
  `https://provider.example/authorize?response_type=code` +
  `&client_id=${CLIENT_ID}&redirect_uri=${encodeURIComponent(location.origin + '/callback')}` +
  `&code_challenge=${challenge}&code_challenge_method=S256&state=${state}`;

// Callback page: hand the code to YOUR server, which exchanges it
// (with the verifier) and sets the app's own HttpOnly session cookie.
await fetch('/auth/callback', {
  method: 'POST',
  body: JSON.stringify({
    code: new URLSearchParams(location.search).get('code'),
    state: new URLSearchParams(location.search).get('state'),
    verifier: sessionStorage.getItem('pkce_verifier'),
  }),
});
```

The browser only ever holds a one-time code; the token exchange and session live server-side, and the redirect URI is an exact registered string.
