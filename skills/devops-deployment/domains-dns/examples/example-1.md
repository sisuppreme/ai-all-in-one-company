# Example 1 — Apex pointed with a bare CNAME

Demonstrates DO-203: no bare CNAME at the apex.

## Before

The host instructs "point your domain at `app.hosting.example`", so the apex
gets a plain CNAME record:

```
@    CNAME  app.hosting.example
www  CNAME  app.hosting.example
```

The apex also needs MX records for mail and a TXT record for domain
verification. A CNAME at the apex conflicts with those records, so mail
delivery and verification break in ways that look unrelated to the change.

## After

The apex uses the DNS provider's CNAME flattening (ALIAS/ANAME), which
resolves the target to A records at query time and coexists with the other
apex records:

```
@    ALIAS  app.hosting.example   (flattened to A records by the provider)
www  CNAME  app.hosting.example
@    MX     10 mail.example.net
@    TXT    "verification-token-for-this-project"
```

Verification: `dig +short example.com A` returns the host's addresses, and
`dig +short example.com MX` still returns the mail servers.
