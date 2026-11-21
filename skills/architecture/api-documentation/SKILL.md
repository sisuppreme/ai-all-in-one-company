# api-documentation

## Metadata

- **Owner department:** D2 Architecture & System Design (AR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OpenAPI Specification 3.1.0 — https://spec.openapis.org/oas/v3.1.0 ; Redocly CLI lint and bundle in the docs pipeline (tooling survey) — https://apidog.com/blog/open-source-cli-tools-api-design/
- **Depends on:** api-architecture, api-versioning
- **Feeds into:** api-versioning

## When to use / Do NOT use

- **Use when:** producing or repairing an API's reference documentation; setting up docs generation from the OpenAPI document; auditing published docs against the running API.
- **Do NOT use when:** the contract itself is still being designed (api-architecture) or does not exist — documentation cannot be generated from a contract that was never written. Do not use this skill to hand-write a reference that duplicates the spec.

**House profile (shared with api-architecture and api-versioning):** the reference is generated from the OpenAPI document; errors are documented in the shared Problem Details format (`type`, `title`, `status`, `detail`); property names in examples are `snake_case`; each version's docs publish under its own path segment and stay reachable for the version's whole lifetime.

## Rules

1. **AR-101 — Generated, never hand-maintained.** The reference documentation is generated from the OpenAPI document. Paths, schemas, and status codes are never edited by hand in a parallel document.
2. **AR-102 — The spec is the boundary.** If it is not in the OpenAPI document, it is not documented; if it is in the document, it renders in the reference. Side wikis are never the source of truth.
3. **AR-103 — Errors are documented for every endpoint.** Every operation documents its error responses in the shared Problem Details format. A "TODO: document errors" note shipped as final is a blocking defect.
4. **AR-104 — Examples are real and executed.** Examples are real requests with realistic, non-sensitive data, and every example payload is verified by executing it against a running instance — fields, types, and required values accepted by the real API, not checked by eye.
5. **AR-105 — Authentication is a complete flow.** Auth is documented as a walkthrough: obtain the credential, send it, its expiry and refresh behavior, and the failure response. "Use your API key" is not documentation.
6. **AR-106 — Humans write only the layer generation cannot.** Human-written docs are limited to the authentication walkthrough, one runnable example per endpoint group, the error catalog, and the changelog. Everything else is generated.
7. **AR-107 — Docs version with the API.** Documentation publishes with the API version it describes, under that version's path; older versions' docs stay reachable for the whole deprecation window defined by api-versioning.
8. **AR-108 — Changelog in the same change.** Each release updates the docs changelog in the same change as the contract change. A contract change without its changelog entry is incomplete.
9. **AR-109 — No sensitive data in examples.** Example payloads never contain real credentials, tokens, personal data, or production identifiers — realistic shape, synthetic values.

## BAN list

- **BAN-AR-051 — "TODO: document errors" shipped as final.** Banned: publishing documentation with error sections left as TODOs or omitted. Defeats: DET-CODE-011. Bad: the reference lists 24 endpoints; 19 have no error responses documented, and the other five say "TODO: document errors". The first integrator discovers the error contract in production. Instead: every operation documents its Problem Details error responses before the docs publish (AR-103). Severity: BLOCK.
- **BAN-AR-052 — The parallel hand-written wiki.** Banned: a hand-maintained wiki or doc page that restates paths, fields, or status codes from the spec. Defeats: DET-CODE-007. Bad: the wiki says `POST /orders` returns 200 with a `total` field; the spec and the service say 201 with `total_price`. Integrators trust whichever they found first. Instead: generate the reference from the OpenAPI document and delete the restated pages, keeping only the human layer (AR-101, AR-106). Severity: BLOCK.
- **BAN-AR-053 — The example the API rejects.** Banned: an example payload the real API would refuse — wrong field names, wrong types, missing required values. Defeats: DET-CODE-004. Bad: the quickstart example posts `{"amount": "10.00"}` as a string and omits the required `currency`; copy-pasting it returns 422, and the docs' credibility goes with it. Instead: execute every example against a running instance in CI and fix the example or the API until it passes (AR-104). Severity: BLOCK.
- **BAN-AR-054 — Documented endpoints that do not exist.** Banned: reference entries for endpoints the service does not route. Defeats: DET-CODE-003. Bad: the docs describe `GET /reports/monthly`, generated from a spec draft; the endpoint was never built and returns 404. Instead: the docs are generated from the shipped spec and the example-execution gate proves every documented path responds (AR-102, AR-104). Severity: BLOCK.

## Gates

- **G-AR-051 — Example execution.** Verifies: AR-104, AR-109. Check: automated — CI executes every documented example request (at minimum three per endpoint group, all of them where the suite is small) against a staging instance and asserts the documented status code and response shape. Pass: every executed example matches its documentation. Fail: block docs publication. Recorded in: progress.md.
- **G-AR-052 — Documentation lint.** Verifies: AR-102, AR-103, AR-105. Check: automated — Spectral/Redocly rules over the OpenAPI document require a description and at least one example on every operation, a Problem Details error response on every operation, and a declared security scheme; the string "TODO" anywhere in the document fails the build. Pass: zero lint errors. Fail: block merge. Recorded in: progress.md.
- **G-AR-053 — Docs-to-routes diff.** Verifies: AR-101, AR-102. Check: automated — a script compares the paths in the published OpenAPI document against the running service's route table. Pass: zero documented-but-unrouted paths and zero routed-but-undocumented public paths. Fail: block release. Recorded in: progress.md.

## Anti-patterns

- **Screenshot documentation.** Request and response examples pasted as images — unsearchable, uncopyable, and stale the moment the API moves. Catch it: if an example cannot be pasted into a terminal, it is not an example (AR-104).
- **The marketing reference.** A reference page written as sales copy, with adjectives where the parameter tables should be. Catch it: a reader should be able to build a client from the page alone; if they still have questions a spec field would answer, the page is a brochure.
- **Changelog as commit dump.** The docs changelog generated raw from commit messages, full of "fix stuff" and merge noise. Catch it: changelog entries are written for consumers — what changed, whether it breaks, what to do (AR-108).
- **One-version docs.** Publishing new docs over the old URL while the old API version is still inside its deprecation window. Catch it: if a v1 consumer can no longer reach v1 docs, AR-107 was broken to save a deploy step.

## Examples

- [Example 1 — Replacing "TODO: document errors" with the error catalog](examples/example-1.md) — corrects AR-103.
- [Example 2 — An executed example replacing one the API rejects](examples/example-2.md) — corrects AR-104.
- [Example 3 — Retiring a hand-written wiki for a generated reference](examples/example-3.md) — corrects AR-101, AR-106.

## Recall anchors

- Generated from the spec — never hand-maintained in parallel.
- Not in the OpenAPI document? Not documented.
- Every example is executed, not eyeballed.
- Errors are documented for every endpoint, in Problem Details.
- Docs version with the API; old versions stay reachable.

## Checklist

- [ ] The reference is generated from the current OpenAPI document (AR-101).
- [ ] Every operation documents its error responses; no TODOs remain (G-AR-052).
- [ ] Every documented example executes successfully against a running instance (G-AR-051).
- [ ] Authentication is documented as a complete flow, including failure (AR-105).
- [ ] The docs-to-routes diff shows zero mismatches (G-AR-053).
- [ ] The changelog entry landed in the same change as the contract (AR-108).
- [ ] Examples contain synthetic values only — no real credentials or personal data (AR-109).
