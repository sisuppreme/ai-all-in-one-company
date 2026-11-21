# Example 3 — Shielded origin, HTTPS-only assets

## Before

The CDN fronts the site, but the origin still answers anyone, and pages reference plain-HTTP assets:

```html
<script src="http://static.example.com/app.js"></script>
```

```text
curl -sk https://origin.example.com/login   -> 200 (direct origin access works)
```

Edge rate limits are bypassable via the origin, and browsers show mixed-content warnings.

## After

The origin accepts CDN traffic only, and every asset URL is HTTPS:

```html
<script src="https://static.example.com/app.js"></script>
```

```text
curl -sk https://origin.example.com/login   -> 403 (origin restricted to CDN egress / authenticated origin pull)
curl -sI http://example.com/                -> 301 Location: https://example.com/
```

Note: demonstrates DO-187 and DO-189 — the origin is shielded so edge controls cannot be bypassed, and no `http://` asset references ship.
