# admin-tools

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Django admin documentation — https://docs.djangoproject.com/en/4.2/ref/contrib/admin/ ; Stripe, PCI compliance guidance (SAQ A scope, hosted card collection) — https://stripe.com/guides/pci-compliance
- **Depends on:** rbac, backend-auth, api-building
- **Feeds into:** user-reporting, incident-response

## When to use / Do NOT use

- **Use when:** staff need to operate the product — look up users, correct data, refund, moderate, configure — through a surface that is safer than a database console and more honest than a demo panel.
- **Do NOT use when:** the surface is for end users; that is the product itself. Do not build admin actions as a parallel write path around the domain services — admin tooling rides the same service layer, or it will diverge from the product it operates.

## Rules

1. **BE-161 — Same service layer.** Admin actions call the same domain services users hit, so validation, authorization, and side effects match the product. There is no admin-only write path into the database.
2. **BE-162 — Mutations persist and propagate.** An admin change is done only when it survives reload and is visible on every user-facing surface it affects. A confirmation toast is not evidence.
3. **BE-163 — Dashboards compute live.** Every figure on an admin dashboard is computed from current records at view time, or on a stated refresh cycle. No fixture or constant renders as a metric.
4. **BE-164 — Audit record on every mutation.** Each admin mutation writes actor, action, target, before/after values, and timestamp — as part of the action, not as a later courtesy.
5. **BE-165 — Scoped staff roles.** Staff access is least-privilege by role and enforced server-side (see rbac). A read-only role cannot mutate by calling the endpoint directly.
6. **BE-166 — Destructive actions are two-step.** Refunds, bans, and data corrections are prepared, shown for confirmation with their effect stated, then executed. Where the domain allows, they are reversible or compensatable.
7. **BE-167 — Card data never renders.** Admin screens show at most card brand + last 4, taken from the provider's card object. A full PAN is never displayed, stored, or logged; card collection stays with the provider (SAQ A scope).
8. **BE-168 — Stricter staff sessions.** Admin sessions idle out faster than user sessions, and high-impact actions require re-authentication at the moment of execution.
9. **BE-169 — Repeated fixes become tools.** If support performs the same manual fix twice, it becomes an admin tool with validation and an audit trail. Raw SQL against production is not an operating procedure.
10. **BE-170 — A separate, staff-authenticated surface.** The admin app authenticates staff independently of the user app. A user session, however privileged in the product, opens nothing here.

## BAN list

- **BAN-BE-081 — The save-nothing panel.** Banned: an admin edit that shows "Saved" while writing nothing, or writing only to local component state. Defeats: DET-FAKE-010. Bad: staff change a price, the toast confirms, and the storefront keeps the old price forever. Instead: route the edit through the domain service and confirm only after the persisted value is read back (BE-162). Severity: BLOCK.
- **BAN-BE-082 — The fixture dashboard.** Banned: dashboard metrics rendered from constants or seed fixtures presented as live figures. Defeats: DET-FAKE-004. Bad: "Revenue this month: $48,200" is a literal in the dashboard component; real orders never move it. Instead: compute from live records; a metric that cannot be computed displays "unavailable", never an invented number. Severity: BLOCK.
- **BAN-BE-083 — Full PAN on screen or in logs.** Banned: rendering, storing, or logging a full card number anywhere in admin tooling. Defeats: DET-CODE-029. Bad: the payment detail page prints the full number from the provider webhook payload, and the request logger writes it to disk. Instead: store and display only brand + last 4 from the provider's card object, and redact card-shaped strings in logs. Severity: BLOCK.
- **BAN-BE-084 — Hidden-URL access control.** Banned: protecting admin routes only by an unlinked URL, or by a client-side role check, while the endpoints accept ordinary user sessions. Defeats: DET-FAKE-021. Bad: `/internal-ops` is unlisted; any signed-in user who guesses it can issue refunds. Instead: separate staff authentication plus a server-side role check on every admin route (BE-165, BE-170). Severity: BLOCK.

## Gates

- **G-BE-081 — Limited-role denial test.** Verifies: BE-165. Check: automated — authenticate as the read-only staff role and attempt a mutation (price change, refund) through the UI and by direct API call. Pass: both refused server-side with 403 and no state change. Fail: block shipment. Recorded in: progress.md.
- **G-BE-082 — Audit-completeness test.** Verifies: BE-164. Check: automated — perform a test refund in staging, then query the audit log. Shape-adapted form: where the product has no refunds (or no payments at all), perform instead the most consequential audited staff mutation the product does have — a record deletion, a role or permission change, a status override — and query the audit log for that mutation; the evidence bar is identical. Pass: a record exists with actor, action, target, before/after values, and timestamp. Fail: block shipment. Recorded in: progress.md.
- **G-BE-083 — PAN-pattern scan.** Verifies: BE-167. Check: automated — run a Luhn-validated card-number pattern scan over admin templates, rendered staging pages, and application logs. Pass: zero full-PAN matches; brand + last-4 formats pass. Fail: block shipment and purge the contaminated log. Recorded in: progress.md.
- **G-BE-084 — Persistence round-trip.** Verifies: BE-161, BE-162. Check: automated — change a product price as staff, reload the admin view, then fetch the public product page as an anonymous visitor. Shape-adapted form: where the product has no prices or no public page, change any staff-editable record instead and compare the admin view against the surface that record is actually read from — the end-user view, the API response, or the next reader's view — with the same three-way agreement required. Pass: all three views agree on the new price (or, under the shape-adapted form, on the changed record). Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The shared god login.** One "superuser" account for the whole team, so audit records name a role instead of a person. Catch it: read the audit log — if every actor is the same name, accountability is already gone.
- **Confirmation theater.** A confirm dialog that describes a different effect than the one executed ("Delete draft" that deletes the live record). Catch it: read the confirm text against the service call it triggers, word by word.
- **The export-everything button.** One click downloads the entire user table "for support", unscoped and unlogged. Catch it: grep admin routes for bulk export; each one needs scoping, an audit record, and a reason.
- **The shadow write path.** A quick admin endpoint that updates the table directly, skipping the service's validation and side effects — no emails sent, no caches invalidated, no ledger entry. Catch it: search admin handlers for data-layer writes outside the service layer (BE-161).

## Examples

- [Example 1 — A price edit that persists through the service layer](examples/example-1.md) — corrects BE-161.
- [Example 2 — A dashboard metric computed from records](examples/example-2.md) — corrects BE-163.
- [Example 3 — A refund as a two-step, audited action](examples/example-3.md) — corrects BE-166.

## Recall anchors

- Admin actions ride the same services users hit.
- If it didn't persist and propagate, it didn't happen.
- Every mutation writes its audit record.
- Brand + last 4 is all a screen may ever show.
- A fix done twice by hand becomes a tool.

## Checklist

- [ ] Every admin mutation round-trips: reload and the read surface agree (G-BE-084).
- [ ] The read-only staff role is refused mutations server-side (G-BE-081).
- [ ] A test refund (or the shape-adapted audited mutation) produced a complete audit record (G-BE-082).
- [ ] The PAN scan over pages and logs is clean (G-BE-083).
- [ ] Destructive actions are two-step, with the effect shown before execution (BE-166).
- [ ] Staff sessions time out faster than user sessions; high-impact actions re-authenticate (BE-168).
- [ ] No admin handler writes the database outside the service layer (BE-161).
