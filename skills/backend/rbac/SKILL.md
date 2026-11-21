# rbac

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** NIST CSRC, "Role Based Access Control" — https://csrc.nist.gov/projects/role-based-access-control ; OWASP API Security Top 10 (2023), API1/API5 — https://orca.security/resources/blog/owasp-api-security-top-10/
- **Depends on:** backend-auth, api-building
- **Feeds into:** admin-tools, user-reporting

## When to use / Do NOT use

- **Use when:** the product has more than one kind of user (member, moderator, staff, tenant admin) and any operation must be restricted by who is asking — which is to say, on every multi-role API, before the first protected route ships.
- **Do NOT use when:** the only question is *who* the caller is — that is backend-auth. RBAC starts after authentication, at the question of what this identity may do. Do not use a feature flag as a permission system; flags hide features, they do not authorize (see feature-flags).

## Rules

1. **BE-121 — Deny by default.** A route with no policy entry is unreachable, not open. Access exists only where the permission matrix grants it.
2. **BE-122 — Enforced on the server, per request.** Every protected operation runs its permission check inside the handler or in middleware bound to the route. UI visibility is presentation, never the check.
3. **BE-123 — Role comes from the server record.** The role that authorizes a request is read from the server-side session or user record. A role, flag, or header supplied by the client is ignored.
4. **BE-124 — Two checks, not one.** Function-level authorization (may this role call this operation at all — OWASP API5) and object-level authorization (may this identity act on this record — OWASP API1) are checked separately; passing one never implies the other.
5. **BE-125 — The matrix is a document.** The permission matrix (roles × operations) lives in the repo, and the authorization tests are generated from it. A route with no matrix row does not ship.
6. **BE-126 — Tenant scope is part of the check.** A role grants rights inside one tenant context only. Every check carries the tenant; an admin of tenant A has no rights in tenant B.
7. **BE-127 — Assignment is privileged and logged.** Granting or revoking a role is an admin-only operation, recorded in the audit log with actor, target, old role, new role, and timestamp.
8. **BE-128 — Denials are logged.** Every denied privileged attempt is recorded with actor, target, and timestamp. A silent denial hides an attack in progress.
9. **BE-129 — Roles are least-privilege sets.** Each role holds the minimum permissions its job needs. A catch-all admin role used for routine operations is a defect.
10. **BE-130 — Policy changes are code changes.** The matrix and the policy code change through the same review as code. There is no runtime role-editing path outside the audited assignment operation (BE-127).

## BAN list

- **BAN-BE-061 — Cosmetic permissions.** Banned: enforcing a permission only by hiding UI controls while the endpoint answers any authenticated caller. Defeats: DET-FAKE-021. Bad: the "Delete user" button renders only for admins, but `DELETE /users/:id` succeeds for a member token replayed with curl. Instead: check the permission server-side on every request and return 403. Severity: BLOCK.
- **BAN-BE-062 — The client-stored admin flag.** Banned: treating a client-stored value (`isAdmin: true` in localStorage, a role field in the request body) as authorization evidence. Defeats: DET-FAKE-002. Bad: the frontend sets `isAdmin` after login and the API trusts the header the frontend sends from it; editing storage grants admin. Instead: read the role from the server-side session record on every request (BE-123). Severity: BLOCK.
- **BAN-BE-063 — The unguarded new route.** Banned: shipping a route with no policy entry so it defaults to open. Defeats: DET-CODE-020 (nearest match — no DET parameter names this exact signal). Bad: `GET /admin/export` is added for a demo with no middleware and returns the full user table to anyone who finds the URL. Instead: deny-by-default policy table — the route returns 403 until a matrix row grants a role access. Severity: BLOCK.
- **BAN-BE-064 — The client copy decides.** Banned: implementing the permission rule in the frontend as the deciding copy while the server re-derives it with different conditions. Defeats: DET-CODE-027. Bad: the client allows refunds under $500 by its own constant; the server's limit is $200, so the UI promises actions the API rejects — or the reverse, and the API accepts what the UI forbade. Instead: the server is the only enforcement; the client mirrors the matrix for display and defers every decision to the server's response. Severity: WARN.

## Gates

- **G-BE-061 — Authorization matrix test.** Verifies: BE-121, BE-122, BE-124. Check: automated — the CI suite generated from the permission matrix requests every protected endpoint as each role, as an anonymous caller, and as a different user, asserting 401/403 and no record data in denied responses. Pass: every matrix cell matches its expected outcome. Fail: block shipment. Recorded in: progress.md.
- **G-BE-062 — Cross-tenant access test.** Verifies: BE-126. Check: automated — seed two tenants; as tenant A's admin, attempt read, write, and delete on tenant B's records by direct ID. Pass: zero cross-tenant successes. Fail: block shipment. Recorded in: progress.md.
- **G-BE-063 — Client-trust scan.** Verifies: BE-123. Check: automated — grep the API codebase for role or permission values read from request bodies, headers, or client storage (`isAdmin`, `req.body.role`, `req.headers['x-role']`); every hit is reviewed by hand. Pass: zero hits outside the server-side session-record lookup. Fail: block shipment until removed. Recorded in: progress.md.
- **G-BE-064 — Audit-log completeness check.** Verifies: BE-127, BE-128. Check: automated — in staging, perform one role grant and one denied admin attempt, then query the audit log for both. Pass: both records exist with actor, target, and timestamp. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Role explosion.** A new role per user or per ticket (`admin_jane`, `support_temp2`) until the matrix is unreadable. Catch it: count roles — if roles approach the user count, the varying part belongs in assignments or object-level checks, not new roles.
- **Scattered ifs.** Every handler hand-rolls its own role condition, so the same rule reads three ways in three files. Catch it: grep for role comparisons outside the policy module; each one is drift waiting for a victim.
- **The happy-role test suite.** Tests prove admins *can* act and never prove members *cannot*. Catch it: read the matrix test — every grant cell needs its denial twin, or the suite certifies only the safe half.
- **The stale matrix.** The document lists roles the code retired months ago, and reviewers approve against it. Catch it: diff matrix rows against live routes at release; a row with no route, or a route with no row, fails review (BE-125).

## Examples

- [Example 1 — A hidden button replaced by a server-side check](examples/example-1.md) — corrects BE-122.
- [Example 2 — The object-level check a role check cannot replace](examples/example-2.md) — corrects BE-124.
- [Example 3 — Tenant added to the permission check](examples/example-3.md) — corrects BE-126.

## Recall anchors

- Deny by default: a route with no policy entry is closed.
- The server checks; the UI only hides.
- The authorizing role comes from the server record, never the request.
- Function-level and object-level are two different checks.
- Every grant and every denial lands in the audit log.

## Checklist

- [ ] The permission matrix is in the repo and every route has a row (BE-125).
- [ ] Matrix test passes for every role, including anonymous and other-user cells (G-BE-061).
- [ ] Cross-tenant test passes with zero successes (G-BE-062).
- [ ] No role is read from the request or client storage anywhere (G-BE-063).
- [ ] Role grants, revocations, and denied admin attempts appear in the audit log (G-BE-064).
- [ ] Roles are least-privilege sets; no routine catch-all admin (BE-129).
