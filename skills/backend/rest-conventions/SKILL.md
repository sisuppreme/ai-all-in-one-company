# rest-conventions

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Zalando RESTful API Guidelines — http://opensource.zalando.com/restful-api-guidelines/ ; RFC 9110 HTTP semantics summary — https://apiguide.dev/specifications/http-semantics
- **Depends on:** api-architecture, api-versioning
- **Feeds into:** api-building, api-documentation, sdk-design

## When to use / Do NOT use

- **Use when:** designing new endpoints, reviewing an API surface for consistency, or writing the project's convention sheet — paths, methods, status codes, pagination, casing, and versioning all follow one written convention.
- **Do NOT use when:** implementing a single handler's internals (api-building), formatting error bodies in depth (error-handling), or validating payloads (validation). This skill fixes the shape of the surface; other skills build behind it.

## Rules

1. **BE-021 — One convention sheet per API.** Before endpoints are added, the API has a written convention sheet derived from RFC 9110 semantics and one published style guide. The sheet is enforced by linting the OpenAPI document in CI, not by memory.
2. **BE-022 — Resources are plural noun collections.** Paths name resources (`/orders`, `/users/{id}/orders`), in kebab-case, nested only where ownership is real. A path segment names a thing, never an action.
3. **BE-023 — No verbs in URLs.** Non-CRUD actions are modeled as sub-resources (`POST /orders/{id}/cancellations`) or, where the chosen guide prescribes it, `POST /orders/{id}:cancel`. `POST /cancelOrder` is never acceptable.
4. **BE-024 — Methods keep their RFC 9110 meaning.** GET is safe and side-effect-free; PUT replaces the whole resource; PATCH modifies part of it; DELETE removes it. Repeating a PUT or DELETE lands on the same end state.
5. **BE-025 — Status codes follow the decision rule.** `201` + `Location` on create, `204` on empty success, `400` malformed, `409` state conflict, `412` precondition failed, `422` business-rule rejection. An error is never returned with `200`.
6. **BE-026 — One pagination style, from day one.** Every list endpoint paginates — cursor preferred for large or fast-changing collections — with a documented maximum page size. Retrofitting pagination later breaks clients that assumed complete results.
7. **BE-027 — One casing and query grammar.** One field-casing rule for JSON bodies, and one filtering/sorting grammar (`?status=open&sort=-createdAt` style) applies to every endpoint in the API.
8. **BE-028 — Released versions are never silently mutated.** The major version appears in the path only when a breaking change ships, and a superseded version gets an announced deprecation window before removal.
9. **BE-029 — Evolution is additive or it is a new major.** Adding optional fields or new endpoints is compatible evolution; removing, renaming, or re-typing a field is breaking and follows BE-028.
10. **BE-030 — Errors are problem details everywhere.** Every error response from every endpoint is RFC 9457 `application/problem+json` (see error-handling). An endpoint with its own error shape is a convention violation even if the shape is reasonable.

## BAN list

- **BAN-BE-011 — Verb in the URL.** Banned: paths that name operations instead of resources (`/getOrders`, `/createUser`, `/deleteItem`). Defeats: DET-CODE-014. Bad: `POST /api/submitOrder` sits beside `GET /api/orders`, so the same API speaks RPC and REST at once. Instead: model the resource — `POST /orders` creates, `GET /orders` lists, `DELETE /orders/{id}` removes (BE-023). Severity: WARN.
- **BAN-BE-012 — Error returned as 200.** Banned: a success status carrying an error body (`200 { "success": false, "error": "…" }`). Defeats: DET-CODE-022. Bad: a failed payment returns `200` with `"error": "card declined"`, so clients, caches, and monitors all record a success. Instead: return the decision-rule status with a problem-details body — `402`/`422` with `type`, `title`, and `detail` (BE-025, BE-030). Severity: BLOCK.
- **BAN-BE-013 — Unbounded list endpoint.** Banned: a list endpoint that returns the whole collection with no pagination or maximum page size. Defeats: DET-CODE-033. Bad: `GET /events` serializes 2.1 million rows into one response because the demo dataset had ten. Instead: paginate from day one with the API's one style and a capped page size (BE-026). Severity: BLOCK.
- **BAN-BE-014 — Per-endpoint invention.** Banned: an endpoint that invents its own casing, pagination style, or filter grammar instead of following the convention sheet. Defeats: DET-CODE-014. Bad: three list endpoints in one API use offset, page-number, and cursor pagination, and fields flip between `snake_case` and `camelCase` by author. Instead: follow the sheet (BE-021, BE-027); if the sheet is wrong, change the sheet and every endpoint together. Severity: WARN.

## Gates

- **G-BE-011 — OpenAPI convention lint.** Verifies: BE-021, BE-022, BE-023, BE-027. Check: automated — run the OpenAPI linter (Spectral/Redocly) with the ruleset encoding the convention sheet over the API description in CI. Pass: zero lint errors. Fail: block merge. Recorded in: progress.md.
- **G-BE-012 — Status-code audit.** Verifies: BE-024, BE-025, BE-030. Check: automated — a script exercises create, delete, malformed-request, and business-rejection paths against a running instance and asserts the decision-rule status and a problem-details body for each. Pass: every sampled path returns the prescribed status and shape. Fail: block shipment. Recorded in: progress.md.
- **G-BE-013 — New-endpoint convention review.** Verifies: BE-026, BE-028, BE-029. Check: manual — for each new or changed endpoint, diff its path, pagination, casing, and versioning against the convention sheet using the sheet's checklist. Pass: no unexplained deviation; a deliberate deviation updates the sheet in the same change. Fail: warn, and resolve before release. Recorded in: progress.md.

## Anti-patterns

- **Guide shopping.** Zalando is cited for one endpoint, Google's AIPs for the next, and neither for the third, so the API has three accents. Catch it: ask which single guide the convention sheet derives from; if the answer is a list, the sheet does not exist yet.
- **RPC creep.** Every genuinely new capability arrives as a verb endpoint because modeling it as a resource takes ten more minutes. Catch it: count verb paths each release; the number only grows in one direction.
- **Version sprawl.** v1 through v4 are all live, none deprecated, and bug fixes land in whichever version the reporter used. Catch it: list the versions a new client is told to use; more than one current version is sprawl.
- **The permanent beta path.** `/v0` or `/beta` endpoints become load-bearing for real clients while still claiming the right to change without notice. Catch it: any path with production traffic is a released version under BE-028, whatever its name says.

## Examples

- [Example 1 — Verb URLs remodeled as resources](examples/example-1.md) — corrects BE-023.
- [Example 2 — 200-with-error replaced by problem details](examples/example-2.md) — corrects BE-025, BE-030.
- [Example 3 — Offset pagination replaced by cursors on a live feed](examples/example-3.md) — corrects BE-026.

## Recall anchors

- Paths name things; methods do the verbs.
- Errors are never 200.
- One pagination style, one casing, one grammar — from day one.
- Additive evolves; breaking versions.
- If it deviates, change the sheet and every endpoint together.

## Checklist

- [ ] The convention sheet exists and names its source guide (BE-021).
- [ ] OpenAPI lint with the convention ruleset is green in CI (G-BE-011).
- [ ] No path contains a verb; actions are sub-resources (BE-023).
- [ ] Sampled paths return decision-rule statuses with problem-details errors (G-BE-012).
- [ ] Every list endpoint paginates in the one style, with a max page size (BE-026).
- [ ] No released version was silently mutated; breaking changes follow BE-028.
