# validation

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OWASP Input Validation Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html ; OWASP API Security Top 10 (2023) — https://orca.security/resources/blog/owasp-api-security-top-10/
- **Depends on:** api-architecture
- **Feeds into:** api-building, backend-auth, file-uploads

## When to use / Do NOT use

- **Use when:** any data crosses a trust boundary into the server — request bodies, query and path parameters, headers, uploaded filenames, webhook payloads. If the server is about to trust it, store it, or act on it, this skill runs first.
- **Do NOT use when:** shaping URLs or status codes (rest-conventions), formatting the error response itself (error-handling), or checking who the caller is (backend-auth, rbac). Validation decides whether input is acceptable; it does not decide identity or permission.

## Rules

1. **BE-041 — Schema at the edge.** Every inbound payload — body, query, path, headers — is parsed through a declared schema (types, formats, lengths, ranges, allowlists, unknown-field policy) at the edge of the handler, before any business logic or persistence runs.
2. **BE-042 — Server-side always.** Browser or client validation is a UX aid, never a control. Every rule the client checks is checked again on the server; an endpoint that relies on the form is unvalidated.
3. **BE-043 — Allowlist over denylist.** Enumerate what is accepted. Write endpoints reject unknown fields outright, so extra properties in the body cannot be mass-assigned to the record (OWASP API3:2023, broken object property level authorization).
4. **BE-044 — Semantic checks follow syntactic ones.** After shape checks pass, verify meaning: date ranges are ordered, quantities are positive, and referenced objects exist and are visible to this caller.
5. **BE-045 — Validate the canonical form.** Decode first — URL encoding, Unicode normalization, path resolution — then validate the decoded value. A check against the raw string is bypassed by an alternate spelling of the same attack.
6. **BE-046 — Size before parse.** Body-size, field-count, and string-length caps run before schema work, so the validation layer itself cannot be exhausted by the payload it is checking.
7. **BE-047 — Failures are specific and total.** A failed validation returns `422` problem details listing each field and the rule it broke, and writes nothing — no partial record, no side effects, no queued jobs.
8. **BE-048 — Invariants live once, server-side.** A business rule (discount caps, eligibility, limits) is defined in exactly one server-side place. The client may mirror it for UX, but the server copy is the only enforcement.
9. **BE-049 — The schema is the contract schema.** The validation schema and the OpenAPI schema are one source, or are diffed in CI. Two hand-maintained copies will drift, and the drift is always in the permissive direction.
10. **BE-050 — Rejection is the safe default.** When a validator errors, times out, or meets a shape it does not recognize, the request is rejected. Validation never fails open.

## BAN list

- **BAN-BE-021 — Trusting the browser's validation.** Banned: a server endpoint that accepts and stores a payload because the shipped form checks it. Defeats: DET-CODE-019. Bad: the price field is validated in React, so a hand-sent request stores `price: -500` and the store owes the buyer money. Instead: parse every payload through the server-side schema at the handler's edge (BE-041, BE-042). Severity: BLOCK.
- **BAN-BE-022 — Mass assignment.** Banned: binding the request body directly to a record (`create(req.body)`, `Object.assign(user, req.body)`) so client-sent fields like `isAdmin`, `role`, or `balanceCents` are persisted. Defeats: DET-FAKE-021. Bad: a profile update accepts `{ "isAdmin": true }` and the account promotes itself. Instead: allowlist the writable fields in the schema and reject unknown fields on write endpoints (BE-043). Severity: BLOCK.
- **BAN-BE-023 — Denylist as the only defense.** Banned: "validation" that string-matches known-bad fragments (`<script>`, `' OR 1=1`) instead of allowlisting shape and parameterizing queries. Defeats: DET-CODE-017. Bad: a search filter blocks the exact string `' OR 1=1` but passes `' oR '1'='1` and forty other spellings to a concatenated query. Instead: validate type and range against an allowlist schema, and bind values as parameters — never concatenate input into a query (BE-043). Severity: BLOCK.
- **BAN-BE-024 — Duplicated rule, divergent constants.** Banned: the same business rule implemented independently on client and server with different values, so the layers disagree about what is allowed. Defeats: DET-CODE-027. Bad: the client caps discounts at 20% while the server caps them at 30%; support discovers the gap from a customer screenshot. Instead: define the invariant once server-side (BE-048); the client mirror is generated from, or tested against, that definition. Severity: WARN.

## Gates

- **G-BE-021 — Boundary test pack.** Verifies: BE-041, BE-047, BE-050. Check: automated — for each endpoint, run the boundary pack: wrong types, oversized strings, missing required fields, inconsistent ranges, malformed encodings; assert `422` problem details and zero state change in the database after each case. Pass: every case rejected with no partial write. Fail: block shipment. Recorded in: progress.md.
- **G-BE-022 — Schema-drift check.** Verifies: BE-049. Check: automated — diff the runtime validation schemas against the OpenAPI document in CI. Pass: zero differences. Fail: block merge. Recorded in: progress.md.
- **G-BE-023 — Mass-assignment probe.** Verifies: BE-043. Check: automated — send create/update requests carrying privileged extra fields (`role`, `isAdmin`, `ownerId`, `balanceCents`) and assert each is rejected or ignored and the stored record is unchanged in those fields. Pass: no privileged field is ever set from the request. Fail: block shipment. Recorded in: progress.md.
- **G-BE-024 — Canonicalization probe.** Verifies: BE-045. Check: automated — submit encoded and alternate-spelling variants of rejected values (double-encoded traversal filenames, Unicode-confusable names, mixed-case injection strings) and assert the decoded form is what gets validated and rejected. Pass: every variant rejected. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Mid-handler validation.** Checks are sprinkled through the handler, after the first write has already happened, so a late failure leaves early effects behind. Catch it: read one handler top to bottom and mark the first persistence call — every validation must sit above it.
- **The permissive schema.** `additionalProperties: true` and unconstrained strings everywhere, chosen "for flexibility." Catch it: the schema that accepts everything validates nothing; count how many fields have no type, length, or range.
- **Client-mirror drift.** The frontend rule was updated in a redesign; the server rule still enforces last year's value, and nobody noticed because the client hides the failure. Catch it: pick two core rules and read both implementations side by side (BE-048).
- **Error soup.** Every failure returns "Invalid input" with no field named, so legitimate users cannot fix their request and support cannot help. Catch it: submit one request with two bad fields — the response must name both.

## Examples

- [Example 1 — Mass assignment closed by an allowlist schema](examples/example-1.md) — corrects BE-043.
- [Example 2 — Canonical-form validation of an uploaded filename](examples/example-2.md) — corrects BE-045.
- [Example 3 — Validate-all-then-write replaces a partial write](examples/example-3.md) — corrects BE-047.

## Recall anchors

- Nothing is trusted until the schema says so — server-side, at the edge.
- Allowlist what is accepted; reject what is unknown.
- Decode first, then validate the canonical form.
- A failed validation writes nothing.
- One invariant, one home: the server.

## Checklist

- [ ] Every payload (body, query, path, headers) passes a declared schema before business logic (BE-041).
- [ ] Write endpoints reject unknown fields; the mass-assignment probe passes (G-BE-023).
- [ ] Size and count caps run before schema parsing (BE-046).
- [ ] Validation failures return 422 problem details naming each field and rule, with zero state change (G-BE-021).
- [ ] Encoded/alternate spellings are validated in canonical form (G-BE-024).
- [ ] Validation schemas and the OpenAPI document diff clean in CI (G-BE-022).
- [ ] Business invariants exist in exactly one server-side place (BE-048).
