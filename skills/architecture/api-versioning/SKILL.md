# api-versioning

## Metadata

- **Owner department:** D2 Architecture & System Design (AR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Semantic Versioning 2.0.0 — https://semver.org/ ; Google, "Compatibility" (breaking vs non-breaking change lists) — https://cloud.google.com/apis/design/compatibility/ ; Breaking-change gate design — https://www.api-contract-testing.com/api-contract-fundamentals-tool-selection/breaking-change-detection/
- **Depends on:** api-architecture
- **Feeds into:** api-documentation

## When to use / Do NOT use

- **Use when:** an API change must be classified as breaking or safe; a major version is being introduced; a version is being deprecated or removed; a consumer asks what a version number promises.
- **Do NOT use when:** the API does not exist yet (api-architecture designs v1), or the version in question is a library/package version with no API consumers — though the same semver rules are a sound default there too.

**House profile (shared with api-architecture and api-documentation):** the major version sits in the path segment (`/v1/…`) and nowhere else; deprecations are signaled with `Deprecation` and `Sunset` headers plus a changelog entry; within a major version only backward-compatible changes ship.

## Rules

1. **AR-081 — Breaking is an enumerated list, not a feeling.** Removing or renaming a field, method, or enum value; changing a field's type; changing a resource name format; or changing visible behavior is breaking. Adding interfaces, methods, fields, or enum values is safe. The classification follows the list, never intuition.
2. **AR-082 — Unlisted means breaking.** A change the list does not cover is treated as breaking until a recorded ruling says otherwise. The benefit of the doubt goes to consumers.
3. **AR-083 — Additive only within a major version.** Inside a major version, only backward-compatible changes ship: additive fields, new endpoints, new enum values where consumers tolerate unknowns. Anything else waits for the next major.
4. **AR-084 — Breaking under the same major is release-blocking.** A breaking change that reaches a release under the existing major version is a release-blocking defect, however small it looks.
5. **AR-085 — Every version has a changelog.** Each version carries a changelog entry connecting the version to its changes. "Latest" is never the only nameable version of the API.
6. **AR-086 — Deprecation needs three artifacts first.** Before a deprecation window starts, all three exist: the sunset date, the migration path, and the consumer notification (docs plus `Deprecation`/`Sunset` headers). A window announced without them has not started.
7. **AR-087 — Removal waits for the date and the check.** The old version is removed only after the announced sunset date has passed and a consumer check shows no remaining traffic (or named consumers who accepted the cutoff in writing).
8. **AR-088 — Consumers must tolerate unknowns.** The contract states that consumers ignore unknown fields and enum values. This obligation is what makes additive changes safe, and it is written down, not assumed.
9. **AR-089 — One placement, never mixed.** The version identifier lives in the path segment for public HTTP APIs, per the house profile. Header-based and query-parameter versioning never appear in the same API.
10. **AR-090 — Old and new run side by side.** During a deprecation window both major versions are deployed and supported; a flag-day cutover, where the old version dies the moment the new one ships, is forbidden for public APIs.

## BAN list

- **BAN-AR-041 — The quiet breaking change.** Banned: shipping a breaking change under the same major version. Defeats: DET-INF-026. Bad: `GET /v1/orders` renames `total_price` to `grand_total` in a "minor" release; every v1 client breaks on deploy day and the version number's promise turns out to be worthless. Instead: ship the rename in `/v2/`, run both side by side, and deprecate v1 with the full artifact set (AR-084, AR-086). Severity: BLOCK.
- **BAN-AR-042 — The random version bump.** Banned: version numbers bumped without a change classification behind them. Defeats: DET-CODE-028. Bad: the API jumps from 1.0 to 3.0 for a typo fix in a description, then stays at 3.0 through a field removal; consumers can infer nothing from any number. Instead: classify the change against the enumerated list first (AR-081); the bump follows the classification — patch for safe fixes, major for breaking changes. Severity: WARN.
- **BAN-AR-043 — The silent removal.** Banned: removing a deprecated version with no sunset date, no migration path, or no consumer notification. Defeats: DET-INF-028. Bad: `/v1/` starts returning 404 one Monday morning; the changelog says nothing, the headers said nothing, and two partners learn about it from their own error alerts. Instead: publish the sunset date, the migration path, and the notification first; remove only after the date and the consumer check (AR-086, AR-087). Severity: BLOCK.
- **BAN-AR-044 — Mixed version placement.** Banned: version identifiers in more than one location in the same API. Defeats: DET-CODE-014. Bad: most endpoints are `/v1/…`, newer ones take `?version=2`, and one partner API versions by header; nobody can state the API's versioning scheme in one sentence. Instead: path segment only, per the house profile, for every endpoint (AR-089). Severity: WARN.

## Gates

- **G-AR-041 — Breaking-change diff.** Verifies: AR-081, AR-083, AR-084. Check: automated — CI runs `oasdiff breaking <last-shipped-spec> <new-spec>`; any breaking finding fails the build unless the change also bumps the major version and lands with an ADR recording the approved break. The tool is pinned in the repo; if it cannot run in the sandbox, the fallback is a manual field-by-field diff against the compatibility list, recorded in progress.md. Pass: no unapproved breaking findings. Fail: block release. Recorded in: progress.md.
- **G-AR-042 — Deprecation artifact check.** Verifies: AR-086, AR-087. Check: automated — for any version marked deprecated, a script confirms the changelog contains its sunset date and migration link, and a probe of the running service confirms responses carry `Deprecation` and `Sunset` headers. Pass: all three artifacts present. Fail: block the deprecation announcement. Recorded in: progress.md.
- **G-AR-043 — Runtime version matches the tag.** Verifies: AR-085, AR-089. Check: automated — query the deployed service's metadata/health endpoint and compare its reported API version with the release tag and the path segments it serves. Pass: exact match. Fail: block release. Recorded in: progress.md.

## Anti-patterns

- **Semver as marketing.** Major bumps timed to launches ("Version 5 is here!") rather than to compatibility. Catch it: ask what broke; if nothing did, the number is a press release, not a version (AR-081).
- **The permanent beta.** An API kept at `v0` or "beta" for years so breaking changes need no window. Catch it: a public API with real consumers is a versioned API, whatever its label says; apply AR-086 when it changes.
- **Deprecation by blog post.** The sunset is announced in a blog post or a sales email but never in the changelog or the response headers consumers actually see. Catch it: run G-AR-042; if the artifacts are not where consumers look, the window has not started.
- **Tolerance assumed, not contracted.** Additive changes shipped as "safe" while nothing obliges consumers to ignore unknown fields — and one strict-parser client breaks on every new field. Catch it: if AR-088's sentence is not in the contract, the change is not yet safe.

## Examples

- [Example 1 — A field rename shipped as v2, not as a quiet v1 break](examples/example-1.md) — corrects AR-084.
- [Example 2 — A complete deprecation package for retiring v1](examples/example-2.md) — corrects AR-086, AR-087.
- [Example 3 — Unifying mixed version placement on the path segment](examples/example-3.md) — corrects AR-089.

## Recall anchors

- Breaking is a list, not a feeling; unlisted means breaking.
- Additive only, inside a major version.
- Deprecation = sunset date + migration path + notification, before the window.
- Removal waits for the date and the consumer check.
- Path segment, one placement, never mixed.

## Checklist

- [ ] The change is classified against the enumerated compatibility list (AR-081).
- [ ] The breaking-change diff passes, or the break is approved with a major bump and an ADR (G-AR-041).
- [ ] The version has a changelog entry connecting it to its changes (AR-085).
- [ ] The contract states consumers must ignore unknown fields and enum values (AR-088).
- [ ] Any deprecation has its sunset date, migration path, and notification in place (G-AR-042).
- [ ] Old and new majors run side by side for the whole window (AR-090).
- [ ] The deployed version matches the release tag (G-AR-043).
