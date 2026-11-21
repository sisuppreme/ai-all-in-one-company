# api-architecture

## Metadata

- **Owner department:** D2 Architecture & System Design (AR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Zalando RESTful API Guidelines — https://opensource.zalando.com/restful-api-guidelines/ ; Google API design and compatibility rules — https://cloud.google.com/apis/design/compatibility/ ; Lint and diff tooling survey — https://apidog.com/blog/open-source-cli-tools-api-design/
- **Depends on:** system-design, domain-driven-design
- **Feeds into:** api-versioning, api-documentation, api-paradigms

## When to use / Do NOT use

- **Use when:** designing a new HTTP API or a new resource surface on an existing one; reviewing an OpenAPI draft before implementation; settling naming, error, pagination, or idempotency conventions for a service.
- **Do NOT use when:** the interface is not resource-oriented HTTP (api-paradigms decides the paradigm first), the question is only how an accepted design evolves (api-versioning), or the work is documenting an existing contract (api-documentation).

**House profile (applies to this skill, api-versioning, and api-documentation — one style, no mixing):** Zalando-based. Resource names are plural nouns; property names are `snake_case`; custom actions are sub-resources (e.g., `POST /orders/{id}/cancellations`); errors use the Problem Details format (`type`, `title`, `status`, `detail`) everywhere; collections paginate with cursors; the major version sits in the path segment (`/v1/…`); deprecations are signaled with `Deprecation` and `Sunset` headers.

## Rules

1. **AR-061 — Contract first.** The OpenAPI document is drafted and reviewed before implementation, and is written or updated in the same change as any API behavior change. Code that changes behavior without touching the contract is incomplete.
2. **AR-062 — Resources from the domain.** Resources and their relationships are identified from the domain model, with stable identifiers. An endpoint that cannot name its resource is a design smell to resolve, not to route around.
3. **AR-063 — One error format.** Every endpoint returns errors in the house Problem Details format (`type`, `title`, `status`, `detail`). Per-endpoint error shapes are a blocking defect.
4. **AR-064 — Every list paginates.** Every list endpoint paginates (cursor preferred) and states its ordering in the contract. An unbounded list response is forbidden.
5. **AR-065 — Filtering and sorting are first-version features.** Collection endpoints define their filter and sort parameters in the first version, per the house profile; bolting them on later is a breaking-change risk, not a plan.
6. **AR-066 — Mutations state their idempotency story.** Every mutating endpoint is one of: a safe/idempotent method by semantics, protected by an idempotency key, or explicitly documented as non-idempotent with a retry warning. Silence on idempotency is a defect.
7. **AR-067 — Names follow the house profile.** Resource names are plural nouns; verbs appear only as named sub-resource actions (`/orders/{id}/cancellations`); property names are `snake_case`. No endpoint invents its own convention.
8. **AR-068 — Auth is in the contract.** Every operation declares its security requirement in the OpenAPI document (scheme and, where applicable, scope). An operation with no declared security is treated as an oversight, not as public-by-default.
9. **AR-069 — One profile, applied uniformly.** The house profile named in this skill is the only style guide for the API. Where the profile is silent, the gap is resolved once, recorded, and applied everywhere — never per endpoint.
10. **AR-070 — Breaking changes leave this skill.** Any change the compatibility list classifies as breaking is routed to api-versioning (major bump plus deprecation window); it never ships quietly inside an existing version.

## BAN list

- **BAN-AR-031 — Per-endpoint error shapes.** Banned: each endpoint inventing its own error body. Defeats: DET-CODE-014. Bad: `GET /orders` fails with `{"error": "nope"}`, `POST /orders` with `{"message": ..., "code": 7}`, and `GET /invoices` with a plain-text 500; every client writes three error parsers. Instead: the house Problem Details body (`type`, `title`, `status`, `detail`) from every endpoint (AR-063). Severity: BLOCK.
- **BAN-AR-032 — The unbounded list.** Banned: a list endpoint that returns the whole collection. Defeats: DET-CODE-033. Bad: `GET /customers` returns all 40,000 customer records in one response because "it's an internal tool for now." Instead: cursor pagination with a stated ordering and a default and maximum page size, in the first version (AR-064). Severity: BLOCK.
- **BAN-AR-033 — Verbs as resources.** Banned: endpoints named for actions instead of resources (`/createOrder`, `/getInvoices`, `/deleteUser`). Defeats: DET-CODE-008. Bad: the API surface is 30 POST endpoints with verb names; HTTP methods and resources carry no meaning and every client hardcodes RPC-style paths. Instead: plural-noun resources with HTTP methods for the standard operations and sub-resource actions for the rest (`POST /orders`, `POST /orders/{id}/cancellations`) (AR-067). Severity: WARN.
- **BAN-AR-034 — Code-first drift.** Banned: shipping an API behavior change while the OpenAPI document stays untouched. Defeats: DET-CODE-032. Bad: a field is renamed in the service to fix a bug; the contract, the generated docs, and the partner's client all keep the old name until production traffic fails. Instead: the contract is edited in the same change, reviewed as the contract, and the diff gate in api-versioning classifies the rename as breaking (AR-061). Severity: BLOCK.

## Gates

- **G-AR-031 — OpenAPI lint.** Verifies: AR-063, AR-064, AR-067, AR-068. Check: automated — CI runs Spectral (or Redocly CLI) with the house ruleset against the OpenAPI file: operationIds and descriptions present, error responses use the Problem Details schema, list operations declare pagination parameters, property names match `snake_case`. The linter version is pinned in the repo; if the sandbox cannot run it, the fallback is the documented manual ruleset walk, recorded in progress.md. Pass: zero lint errors. Fail: block merge. Recorded in: progress.md.
- **G-AR-032 — Contract tests.** Verifies: AR-061, AR-063. Check: automated — contract tests generated from the OpenAPI document run against the implementation in CI and assert status codes, response shapes, and the error format on failure paths. Pass: all contract tests green. Fail: block merge. Recorded in: progress.md.
- **G-AR-033 — Spec-diff design review.** Verifies: AR-062, AR-066, AR-069. Check: manual — before implementation starts, a reviewer reads the OpenAPI diff: resources trace to the domain model, every mutation states its idempotency story, and every deviation from the house profile is recorded as a profile decision. Pass: no unresolved findings. Fail: block implementation. Recorded in: progress.md.

## Anti-patterns

- **The chat-message contract.** Endpoint behavior agreed in prose messages and never written into the OpenAPI document. Catch it: if a consumer's question can only be answered from a chat thread, AR-061 was skipped and the contract does not exist.
- **Pagination as a retrofit.** "We'll add pagination when it gets slow." Catch it: any list endpoint without a cursor in v1 is a future breaking change already scheduled (AR-064).
- **The god resource.** One resource (`/things`) absorbing unrelated concepts because naming the real resources took effort. Catch it: if a resource's fields fall into two groups that are never read together, there are two resources (AR-062).
- **Profile à la carte.** snake_case on one endpoint, camelCase on the next; errors in Problem Details here, ad-hoc JSON there — each locally defensible. Catch it: run G-AR-031 and read two endpoints side by side; uniformity is the profile's whole value (AR-069).

## Examples

- [Example 1 — One error format replacing per-endpoint shapes](examples/example-1.md) — corrects AR-063.
- [Example 2 — Cursor pagination replacing an unbounded list](examples/example-2.md) — corrects AR-064.
- [Example 3 — Verb endpoints remodeled as resources](examples/example-3.md) — corrects AR-067.

## Recall anchors

- Contract first, code second — same change, every time.
- One error format: Problem Details, everywhere.
- Every list paginates; every mutation states its idempotency story.
- Plural nouns, snake_case, sub-resource actions — the house profile.
- Breaking change? Stop — api-versioning owns it.

## Checklist

- [ ] The OpenAPI document was drafted or updated in the same change as the behavior (AR-061).
- [ ] OpenAPI lint passes with the house ruleset (G-AR-031).
- [ ] Contract tests run against the implementation and pass (G-AR-032).
- [ ] Every error response uses the Problem Details format (AR-063).
- [ ] Every list endpoint paginates with a stated ordering (AR-064).
- [ ] Every mutating endpoint states its idempotency story (AR-066).
- [ ] Every operation declares its security requirement (AR-068).
- [ ] Names follow the house profile with no per-endpoint exceptions (AR-067, AR-069).
