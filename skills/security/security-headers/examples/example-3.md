# Example 3 — HSTS enabled in safe stages

Demonstrates SE-165: Strict-Transport-Security is enabled only after every host it covers serves valid HTTPS.

## Before

During the first HTTPS setup, the edge config is copied from a hardening guide and switched on in one step:

```text
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

The apex site is on HTTPS, but `legacy.example.com` still serves plain HTTP and `status.example.com` has an expired certificate. Browsers that receive the header now refuse both subdomains, and the preload submission makes the lock-in effectively permanent — two working services go down because of the control meant to protect them.

## After

HSTS is staged and each step is recorded in the header sheet:

```text
# Stage 1 — apex only, short lifetime, while subdomains are migrated:
Strict-Transport-Security: max-age=86400

# Stage 2 — after `curl -sI https://` succeeds with a valid certificate
# for the apex and every subdomain (gate G-SE-083):
Strict-Transport-Security: max-age=31536000; includeSubDomains

# Stage 3 — preload submitted only after one full stage-2 period
# with zero HTTPS incidents; the submission date is recorded in the sheet.
```

No browser is ever told to insist on HTTPS for a host that cannot serve it.
