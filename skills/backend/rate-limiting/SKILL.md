# rate-limiting

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Stripe, "Rate limits", https://edge-docs.stripe.com/rate-limits ; OWASP API Security Top 10 (2023), API4 Unrestricted Resource Consumption, https://orca.security/resources/blog/owasp-api-security-top-10/
- **Depends on:** api-building, backend-auth
- **Feeds into:** api-documentation, sdk-design, monitoring (D12)

## When to use / Do NOT use

- **Use when:** any endpoint is reachable by untrusted traffic — which is every public endpoint — and when setting or reviewing limits, limiter keys, expensive-operation caps, or 429 behavior.
- **Do NOT use when:** the limit in question is a provider's own quota imposed on the product from outside (that is capacity planning in D11's third-party-apis), or application-level fairness inside a job queue (queues-jobs owns job concurrency).

## Rules

1. **BE-301 — Limits per route class.** Limits are set per route class, not as one global guess: a generous per-account ceiling for ordinary reads, strict limits on authentication and other sensitive flows, and separate caps for expensive operations.
2. **BE-302 — Unspoofable keys.** Limiter keys derive from the authenticated account ID, or from a client IP verified through a trusted proxy chain. A forwarding header from an untrusted hop is never a key.
3. **BE-303 — Independent auth limits.** Login, signup, and password-reset endpoints carry their own per-account and per-IP limits, budgeted independently of general traffic, so credential stuffing cannot hide inside it.
4. **BE-304 — Bounded operations.** Every list, export, and search endpoint enforces a maximum page size and a query-cost ceiling. Requests above the maximum are clamped or rejected, never executed as asked.
5. **BE-305 — Concurrency caps on expensive work.** Search, export, AI calls, and upload processing carry an in-flight concurrency cap in addition to a rate, because their cost is concurrent load, not request count.
6. **BE-306 — The 429 contract.** A rejection returns 429 with a machine-readable body that names the limit that was hit and a `Retry-After` value. "Try again later" with no number is a contract violation.
7. **BE-307 — Metered downstream budgets.** Calls that cost money — SMS, email sends, paid third-party APIs — carry their own tighter per-account budgets, separate from compute limits.
8. **BE-308 — Limits are owned configuration.** Every limit value lives in configuration with a named owner and a review note. A numeric limit literal in handler code that nobody can explain is a defect.
9. **BE-309 — Good clients can survive.** The documented client behavior — honor `Retry-After`, back off exponentially with jitter — is published with the API, so legitimate clients ride out limits instead of amplifying them.
10. **BE-310 — Limit telemetry.** 429 counts are metered per route class and key type, and a sustained rise is alerted on. A limit silently rejecting real users is an incident discovered by telemetry, not by complaints.

## BAN list

- **BAN-BE-151 — The unbounded endpoint.** Banned: list, export, or search endpoints with no maximum page size or cost ceiling. Defeats: DET-CODE-033. Bad: `GET /users?limit=10000000` returns the whole table and takes the service down with it. Instead: clamp to the documented maximum and enforce a cost ceiling (BE-304). Severity: BLOCK.
- **BAN-BE-152 — The spoofable key.** Banned: keying the limiter on a client-supplied forwarding header with no trusted proxy chain behind it. Defeats: DET-CODE-020. Bad: the limiter reads `X-Forwarded-For` directly, so rotating the header resets the caller's budget on every request. Instead: key on the authenticated account ID or a verified client IP (BE-302). Severity: BLOCK.
- **BAN-BE-153 — Auth inside the general budget.** Banned: login and reset endpoints limited only by the global ceiling, with no per-account or per-IP limit of their own. Defeats: DET-CODE-033. Bad: a credential-stuffing run against one account proceeds at the full global rate because nothing stricter applies. Instead: independent, strict auth limits (BE-303). Severity: BLOCK.
- **BAN-BE-154 — The magic-number limit.** Banned: rate limits buried as unexplained numeric literals in handler code, with no owner and no review note. Defeats: DET-CODE-009. Bad: `if (count > 37) reject()` — nobody knows why 37, whose limit it is, or what changing it breaks. Instead: named configuration with an owner (BE-308). Severity: WARN.

## Gates

- **G-BE-151 — Burst test.** Verifies: BE-301, BE-303, BE-306. Check: automated — scripted traffic above each documented limit asserts 429 responses carrying `Retry-After` and the limit's name, while a second key and normal-rate traffic on the same routes pass unaffected. Pass: all assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-BE-152 — Spoof test.** Verifies: BE-302. Check: automated — send requests with rotating forged `X-Forwarded-For` values from one real source; assert the caller's budget does not reset and the limit still engages. Pass: budget unchanged by forged headers. Fail: block shipment. Recorded in: progress.md.
- **G-BE-153 — Bound scan.** Verifies: BE-304, BE-305. Check: automated — request every list, export, and search endpoint with extreme page-size and cost parameters; assert responses are clamped to the documented maxima and expensive routes refuse excess concurrency. Pass: all clamped. Fail: block shipment. Recorded in: progress.md.
- **G-BE-154 — Limit config audit.** Verifies: BE-308. Check: automated grep plus config review — every limiter value resolves to a configuration entry carrying an owner; handler code contains no bare numeric limit literals. Pass: zero unexplained literals. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The cliff edge.** A limit set just above today's normal traffic, so a launch-day spike or one enthusiastic integration locks out real users. Catch it: compare each limit against observed peak traffic and ask what headroom was intended.
- **Session-key theater.** The limiter keys on session ID, so an abuser who opens unlimited sessions has unlimited budget. Catch it: ask what the key costs the caller to mint a fresh one.
- **Silent shedding.** 429s are returned but never metered, so the first sign of an over-tight limit is user complaints. Catch it: look for the 429 metric; its absence is the finding.
- **Retry amplification.** Clients retry rejected requests immediately and in lockstep because no `Retry-After` or jitter guidance was ever published. Catch it: read the 429 body and the client docs as a new integrator would.

## Examples

- [Example 1 — Whole-table list endpoint replaced by a clamped maximum](examples/example-1.md) — corrects BE-304.
- [Example 2 — Forwarded-header keying replaced by account keying](examples/example-2.md) — corrects BE-302.
- [Example 3 — Bare 429 replaced by the 429 contract](examples/example-3.md) — corrects BE-306.

## Recall anchors

- Every endpoint is capped: rate, page size, cost, concurrency.
- Key on what the caller cannot forge.
- Auth gets its own stricter budget, always.
- 429 is a contract: name the limit, give a number, say when to retry.
- A limit nobody can explain is an outage or a hole.

## Checklist

- [ ] Every route class has a documented limit (BE-301).
- [ ] Burst test green: 429s carry the contract, other keys unaffected (G-BE-151).
- [ ] Forged forwarding headers do not reset any budget (G-BE-152).
- [ ] List, export, and search endpoints clamp to documented maxima (G-BE-153).
- [ ] Auth endpoints carry independent per-account and per-IP limits (BE-303).
- [ ] Metered downstream calls carry their own budgets (BE-307).
- [ ] All limit values live in owned configuration, no magic numbers (G-BE-154).
