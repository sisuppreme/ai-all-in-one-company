# Example 3 — Unifying mixed version placement on the path segment

## Before

The API grew three schemes at once: the original endpoints live under `/v1/…`, a newer module takes a `?version=2` query parameter, and a partner integration versions by an `Accept-Version` header. Support cannot answer "which version are you on?" and the docs need a page just to explain the placements.

## After

The house profile is applied uniformly: every public endpoint carries its major version in the path segment (`/v1/…`, `/v2/…`). The query-parameter module is republished under `/v2/`, the header-versioned integration is migrated to `/v1/` with its consumers notified, and the old placements are retired through the standard deprecation window. One sentence now states the scheme: "The major version is the first path segment."

## Note

Corrects AR-089 (the version identifier lives in one placement — the path segment for public HTTP APIs — and is never mixed).
