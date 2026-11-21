# Example 2 — Edge rate limiting for auth paths

## Before

No CDN/WAF rate-limit rules exist. The login endpoint relies on application code alone:

```text
POST /login            -> unlimited attempts per IP
POST /password-reset   -> unlimited attempts per IP
POST /api/checkout     -> unlimited attempts per IP
```

A scripted run of 500 login attempts from one IP receives 500 normal responses.

## After

Rate-limit rules are configured at the edge, stricter for unauthenticated traffic:

```text
Rule: path in {/login, /password-reset, /signup}, unauthenticated
      -> 10 requests / minute / IP, then 429 for 10 minutes
Rule: path = /api/checkout, unauthenticated
      -> 20 requests / minute / IP, then 429 for 10 minutes
Alert: sustained rule hits for 15 minutes -> operator notification
```

The same scripted run now receives 429 responses once the threshold is crossed.

Note: demonstrates DO-185 — edge rate limiting on login, reset, signup, and paid-cost paths, with alerting on sustained abuse (DO-186).
