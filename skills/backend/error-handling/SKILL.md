# error-handling

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** RFC 9457 (Problem Details for HTTP APIs), https://ftp.kaist.ac.kr/rfc/rfc9457.html ; OWASP Error Handling Cheat Sheet, https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html
- **Depends on:** api-building, validation
- **Feeds into:** error-tracking (D12), api-documentation, sdk-design

## When to use / Do NOT use

- **Use when:** designing how any backend reports failure — error responses, exception translation, logging of errors, status-code choice — or auditing an API whose failures all look the same or leak internals.
- **Do NOT use when:** the question is which status code a successful or conventional response carries in general (rest-conventions owns the convention sheet; this skill owns the failure path), or frontend display of errors (D3's ui-states).

## Rules

1. **BE-281 — One exit path.** Every handler ends in exactly one of two exits: the success serializer or the single global error handler. No handler formats its own error response.
2. **BE-282 — Problem details only.** Client-facing errors are RFC 9457 problem details — `type`, `title`, `status`, `detail`, `instance` — with extension members for per-field validation errors and a correlation ID. No other error shape exists in the API.
3. **BE-283 — Typed errors inside.** Domain code raises typed errors that carry a problem type. Raw library and framework exceptions are translated at the boundary into those types, never formatted ad hoc per handler.
4. **BE-284 — No internals out.** A response never contains a stack trace, SQL fragment, table or column name, file path, framework version, or a downstream provider's raw payload.
5. **BE-285 — Full truth inside.** The complete exception, request context, and the same correlation ID the client received are written to structured logs and error tracking. What the client must not see, the operator must.
6. **BE-286 — Classified by who can fix it.** Every error class is one of: caller-fixable (4xx with actionable detail), conflict (409/412), dependency failure (502/503 with retry guidance), or ours (500, alerted). The classification decides the status and the detail level.
7. **BE-287 — No swallowed errors.** An error is handled, translated, or propagated. Empty catches and catch-log-continue-as-if-success are forbidden; best-effort cleanup is the only exception, and it carries a comment stating why failure is safe.
8. **BE-288 — Fail closed.** An error inside an authorization, validation, or payment step denies the operation. No error path defaults to allow, skip, or proceed.
9. **BE-289 — Distinct signals.** Different failures produce different problem types and messages a client can act on. One generic message reused for every failure is forbidden.
10. **BE-290 — Every 5xx is observable.** Each 5xx response corresponds to a log record and a metric carrying the same correlation ID. A 5xx nobody can find afterward is a defect in this skill, not bad luck.

## BAN list

- **BAN-BE-141 — The empty catch.** Banned: catch blocks that are empty, comment-only, or log the error and continue as if the operation succeeded. Defeats: DET-CODE-005. Bad: the payment call throws, the catch logs "oops," and the handler returns 200 "Order placed." Instead: translate the failure into a typed error or propagate it (BE-283, BE-287). Severity: BLOCK.
- **BAN-BE-142 — One message for everything.** Banned: returning the same generic error body for validation failures, missing records, and outages alike. Defeats: DET-CODE-022. Bad: bad input, a deleted record, and a dead database all produce 500 "Something went wrong." Instead: classified problem details, distinct per failure class (BE-286, BE-289). Severity: BLOCK.
- **BAN-BE-143 — The leaking error.** Banned: error responses containing stack traces, SQL, internal paths, or provider payloads. Defeats: DET-CODE-020. Bad: a 500 page prints the ORM stack trace and the query, table names included, because the framework's debug error page reached production. Instead: a generic 500 problem to the client, the full exception to the logs (BE-284, BE-285). Severity: BLOCK.
- **BAN-BE-144 — Fail-open on error.** Banned: an exception inside an authorization or validation check causing the request to be allowed. Defeats: DET-FAKE-021. Bad: the permission service times out, the catch defaults to `allowed = true`, and the privileged action runs. Instead: deny the operation on any check error (BE-288). Severity: BLOCK.
- **BAN-BE-145 — The naked boundary call.** Banned: network, filesystem, or database calls with no timeout and no defined failure path. Defeats: DET-CODE-006. Bad: `await fetch(url)` followed directly by `.json()` — one hung provider hangs every request behind it. Instead: timeout plus a typed failure translated into a classified problem (BE-283, BE-286). Severity: BLOCK.

## Gates

- **G-BE-141 — Error-shape contract test.** Verifies: BE-282, BE-284, BE-289. Check: automated suite that forces each error class (validation, not-found, conflict, dependency down, unexpected) and asserts the problem-details shape, the correct status, distinct `type` values, and the absence of internal markers (stack frames, SQL keywords, absolute paths) in every body. Pass: all assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-BE-142 — Negative-path fuzz run.** Verifies: BE-281, BE-287. Check: automated — fuzz and negative inputs across endpoints; assert no unhandled-exception response (framework error page, empty 500, dropped connection) ever reaches a client. Pass: zero unhandled responses. Fail: block shipment. Recorded in: progress.md.
- **G-BE-143 — Swallow scan.** Verifies: BE-287. Check: automated lint/grep for empty catch blocks and catch blocks whose only action is a log call followed by a success flow; allowlisted best-effort cleanup must carry its justifying comment. Pass: zero unexplained hits. Fail: block shipment. Recorded in: progress.md.
- **G-BE-144 — Correlation trace.** Verifies: BE-285, BE-290. Check: manual step in staging — trigger a 500, take the correlation ID from the response body, and locate the full exception in the logs or error tracking under that ID. Pass: found, complete, same ID. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Catch-log-rethrow noise.** The same exception is logged at every layer it passes, so one incident produces five stack traces and no one knows which is the cause. Catch it: count log records per correlation ID.
- **Error-code soup.** Each handler invents its own numeric codes with no registry, so two codes mean the same thing and one code means three. Catch it: ask for the code list; if it lives only in the handlers, it is soup.
- **The apologetic 200.** Failures return HTTP 200 with an `"error"` field in the body, so monitors and clients see success. Catch it: grep responses for error fields on 200 paths.
- **Retrying the permanent.** Caller-fixable 4xx failures are retried by jobs and clients as if they were outages, hammering the API with requests that can never succeed. Catch it: check which classes the retry policy treats as retryable.

## Examples

- [Example 1 — One generic 500 replaced by classified problem details](examples/example-1.md) — corrects BE-286, BE-289.
- [Example 2 — Empty catch around a payment replaced by typed translation](examples/example-2.md) — corrects BE-283, BE-287.
- [Example 3 — Stack trace in the response replaced by generic-out, full-in logging](examples/example-3.md) — corrects BE-284, BE-285.

## Recall anchors

- Two exits only: success serializer or the one error handler.
- Problem details out, full exception in — same correlation ID.
- Classify by who can fix it; that decides status and detail.
- Nothing is swallowed; nothing fails open.
- Different failures get different signals.

## Checklist

- [ ] All error responses are problem details from the single handler (BE-281, BE-282).
- [ ] Error-shape contract test green, no internal markers in any body (G-BE-141).
- [ ] Fuzz run produced zero unhandled-exception responses (G-BE-142).
- [ ] Swallow scan clean or every hit justified in a comment (G-BE-143).
- [ ] A staging 500 traces from response correlation ID to full log record (G-BE-144).
- [ ] Security and validation checks deny on error (BE-288).
- [ ] Every 5xx emits a log record and a metric with its correlation ID (BE-290).
