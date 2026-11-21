# sdk-design

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Stripe, server-side SDKs (one API behavior, official SDKs in seven languages) — https://docs.stripe.com/sdks/server-side ; Semantic Versioning 2.0.0 — https://semver.org/ ; PROJECT_ANATOMY.md, "API implementation"
- **Depends on:** api-building, rest-conventions, error-handling
- **Feeds into:** sdk-embeddables, third-party-apis

## When to use / Do NOT use

- **Use when:** building, generating, or reviewing a client library for an API you own — its models, client object, retry and timeout behavior, error types, versioning, and release packaging.
- **Do NOT use when:** designing the API itself (api-architecture, rest-conventions), consuming a third party's SDK (third-party-apis), or building embeddable widgets and scripts for other sites (sdk-embeddables). This skill governs libraries that wrap your own API.

## Rules

1. **BE-081 — One contract, two readers.** The SDK is generated from, or hand-maintained against, the same OpenAPI contract the server is contract-tested against. The SDK and the server may never be tested against different truths.
2. **BE-082 — Typed models for every resource.** Requests and responses are typed models mirroring the contract. The public surface never exposes untyped maps or raw JSON for a modeled resource.
3. **BE-083 — One client object.** A single client owns base URL, authentication, timeouts, and retries, configured once at construction. There are no global settings and no per-call surprises.
4. **BE-084 — Retries only where safe.** The SDK retries only idempotent operations, or requests carrying an idempotency key — and the same key is reused across retries. Attempts are bounded, with backoff.
5. **BE-085 — Timeouts are mandatory and configurable.** Every call has a timeout; the default is finite and documented, and the consumer can change it. An SDK call that can hang forever will.
6. **BE-086 — Errors are typed exceptions.** Failures surface as typed exceptions mapped from problem details, preserving status, problem `type`, and the correlation ID. Errors are never swallowed and never reduced to a bare string or a null.
7. **BE-087 — Semver, tracking the API major.** SDK versions follow Semantic Versioning and track the API major version they speak. A breaking SDK change is a major bump, whatever its size.
8. **BE-088 — Quickstart and changelog ship with every release.** The quickstart is runnable as written and completes the documented first task using only the README. Every release carries a changelog entry naming what changed.
9. **BE-089 — A raw escape hatch always exists.** Consumers can reach the underlying HTTP layer — custom path, headers, and body — for fields and endpoints the SDK has not modeled yet, without forking the library.
10. **BE-090 — Deprecations get a full cycle.** A deprecated method is announced in the changelog and marked in code (doc comment / deprecation attribute) for at least one minor cycle before removal, with the replacement named.

## BAN list

- **BAN-BE-041 — Silent retry of a non-idempotent call.** Banned: an SDK retry policy that replays POST creates (or other non-idempotent operations) on timeout or 5xx without an idempotency key. Defeats: DET-CODE-030. Bad: the network stalls after the server commits an order; the SDK retries; the customer now has two orders and two charges. Instead: retry only idempotent operations, or attach one idempotency key at the first attempt and reuse it on every retry (BE-084). Severity: BLOCK.
- **BAN-BE-042 — Swallowed errors.** Banned: SDK code that catches a failure and returns `null`, an empty object, or a default value, so the caller cannot tell failure from an empty result. Defeats: DET-CODE-005. Bad: `catch { return null; }` around the payment call — a declined card and a successful charge both reach the caller as "no object." Instead: throw the typed exception mapped from the problem-details response, with status and correlation ID intact (BE-086). Severity: BLOCK.
- **BAN-BE-043 — Divergent hand-rolled behavior.** Banned: an SDK method that behaves differently from the raw API — extra defaults the server does not apply, business rules re-implemented client-side, responses transformed beyond the contract's mapping. Defeats: DET-CODE-027. Bad: the SDK silently caps a discount at 20% while the API allows 30%, so SDK users and raw-API users get different prices for the same cart. Instead: the SDK is a faithful transport for the contract; rules live server-side, and any mapping the SDK performs is generated from the contract (BE-081). Severity: WARN.
- **BAN-BE-044 — No timeout.** Banned: shipping a client whose calls have no timeout, or a default of infinity, so a stalled server or network hangs the consumer's process indefinitely. Defeats: DET-CODE-006. Bad: a batch job using the SDK freezes for six hours on one dead connection, holding its worker and its lock. Instead: set a finite documented default timeout on the client object, configurable per client and per call (BE-085). Severity: WARN.

## Gates

- **G-BE-041 — Quickstart execution test.** Verifies: BE-088. Check: automated — in CI, create a clean project, install the SDK as a consumer would, and execute the README quickstart verbatim against a test instance. Pass: the documented first task completes with no undocumented step. Fail: block the release. Recorded in: progress.md.
- **G-BE-042 — SDK-vs-contract conformance run.** Verifies: BE-081, BE-082, BE-086. Check: automated — execute the API's contract test suite through the SDK instead of raw HTTP; assert identical statuses, shapes, and error mappings. Pass: the full suite green through the SDK. Fail: block the release. Recorded in: progress.md.
- **G-BE-043 — Retry-safety test.** Verifies: BE-084. Check: automated — against a stub server that commits a create and then drops the response, call the SDK's create method; assert exactly one server-side record exists afterward. Pass: one effect, whether the SDK declined to retry or reused its idempotency key. Fail: block the release. Recorded in: progress.md.
- **G-BE-044 — Timeout test.** Verifies: BE-085. Check: automated — point the SDK at a stub server that accepts the connection and never responds; assert the call fails with the typed timeout error within the configured bound plus tolerance. Pass: bounded failure with the typed error. Fail: block the release. Recorded in: progress.md.

## Anti-patterns

- **The helpful SDK.** The library "fixes" inputs, fills defaults, and hides server errors behind fallbacks, so the consumer debugs the SDK's opinions instead of the API's answers. Catch it: compare one failing call's raw HTTP exchange with what the SDK reported; anything lost in between is help that harms.
- **Version drift.** The SDK's docs and models describe last year's API while the server moved on, and the mismatch surfaces as phantom fields and missing ones. Catch it: run G-BE-042 — drift is exactly what a conformance suite exists to catch, and it only drifts when the suite is skipped.
- **The leaky transport.** Exceptions carry no mapping, so consumers parse HTTP status codes and raw bodies themselves — the SDK is a typed wrapper that stops at the exact moment it matters. Catch it: force one error of each class and read what the caller actually receives.
- **Quickstart rot.** The README's first example calls a method renamed two versions ago, so every new user's first experience is a stack trace. Catch it: the quickstart is code — if it is not executed in CI (G-BE-041), it is already rotting.

## Examples

- [Example 1 — Retry that duplicated an order, made safe with an idempotency key](examples/example-1.md) — corrects BE-084.
- [Example 2 — Catch-and-null replaced by a typed exception](examples/example-2.md) — corrects BE-086.
- [Example 3 — Hanging call given a mandatory, configurable timeout](examples/example-3.md) — corrects BE-085.

## Recall anchors

- The SDK and the server are tested against one contract.
- Retry only what is safe: idempotent, or keyed.
- No call hangs forever; every error is a typed exception.
- The quickstart is a test — if it doesn't run in CI, it's wrong.
- Semver, changelog, deprecation cycle: releases are a contract too.

## Checklist

- [ ] SDK models and behavior conform to the contract suite run through the SDK (G-BE-042).
- [ ] Retries are limited to idempotent operations or reuse one idempotency key (G-BE-043).
- [ ] Every call has a finite, configurable timeout (G-BE-044).
- [ ] Errors surface as typed exceptions preserving status, type, and correlation ID (BE-086).
- [ ] The README quickstart executes clean in a fresh project (G-BE-041).
- [ ] Version follows semver and tracks the API major; the changelog names the changes (BE-087, BE-088).
- [ ] A raw HTTP escape hatch exists for unmodeled fields (BE-089).
