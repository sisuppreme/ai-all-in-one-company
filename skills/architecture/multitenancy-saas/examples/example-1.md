# Example 1 — Tenant context from the edge, not the body

## Before

```http
POST /api/invoices
{ "tenant_id": 42, "customer": "Acme", "amount_minor": 5000 }
```

The handler trusts `tenant_id` from the body. Anyone — signed in or not — can
create or, with the matching GET, read invoices for any tenant by changing
one number.

## After

The tenant is resolved in middleware from the authenticated session (the
principal's tenant claim, cross-checked against the subdomain) and stored in
request context. Handlers read the tenant from context only; a `tenant_id`
field in a request body is ignored and its presence is logged. The
cross-tenant test suite includes this exact request and asserts a 403.

Note: corrects AR-183 — tenant context is established once, at the edge, from the authenticated principal; code never accepts a tenant ID from an unauthenticated request body.
