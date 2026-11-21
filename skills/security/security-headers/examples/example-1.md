# Example 1 — CSP rebuilt as a real-origin allowlist

Demonstrates SE-163: the Content-Security-Policy names only origins the app actually loads from.

## Before

The app is a server-rendered dashboard. It loads its own bundled script, one font file from Google Fonts, and avatars from its own storage. It ships a CSP copied from a framework tutorial:

```text
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://unpkg.com https://cdnjs.cloudflare.com; style-src 'self' 'unsafe-inline' https:; img-src 'self' data: https:
```

Any injected script tag executes (`unsafe-inline`), and a script hosted on any of three CDNs the app never uses is trusted — the policy blocks almost nothing.

## After

The built pages were inventoried: scripts only from `'self'`, styles from `'self'` and `fonts.googleapis.com`, fonts from `fonts.gstatic.com`, images from `'self'` and the app's storage host. The policy now says exactly that, and is enforced:

```text
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' https://storage.example.com; frame-ancestors 'none'; base-uri 'self'; form-action 'self'
```

The header sheet records the inventory and its date, and gate G-SE-082 fails CI if a source outside the inventory appears.
