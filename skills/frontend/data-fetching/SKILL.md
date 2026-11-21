# data-fetching

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** TanStack Query, Important Defaults — https://tanstack.com/query/latest/docs/framework/react/guides/important-defaults
- **Depends on:** frontend-state, ui-states
- **Feeds into:** frontend-core, data-visualisation, pwa-offline

## When to use / Do NOT use

- **Use when:** reading or mutating server data from the client; setting up a query cache; fixing duplicate requests, stale renders, race conditions, or fetches scattered through components.
- **Do NOT use when:** the state never leaves the client — that is frontend-state. Do not use this skill to design the API itself (endpoints, payloads, status codes); that is D2/D4's architecture and backend work — this skill governs how the client consumes it.

## Rules

1. **FE-201 — All server reads go through the query layer.** Reads use the dedicated query cache (TanStack Query, or framework loaders/actions in Next.js/Nuxt-style stacks). Fetch-on-mount `useEffect` sprawl across components is forbidden.
2. **FE-202 — Query keys mirror the API.** Keys follow a stable scheme that names the resource and its parameters (`['orders', { status }]`, `['orders', id]`), so caching, deduplication, and invalidation behave predictably.
3. **FE-203 — Freshness is a decision per data type.** `staleTime` is set deliberately for each query based on how fast its data changes; accepting a global default without considering the data is not a decision.
4. **FE-204 — Stale responses cannot win.** Requests are keyed or cancellable so that fast navigation or changing parameters cannot let an older, slower response overwrite a newer view.
5. **FE-205 — Every outcome lands in the state matrix.** Each query's loading and error outcomes render through the view's ui-states matrix; errors are never swallowed silently and never leave a blank region.
6. **FE-206 — Retries come from the query layer.** Failed queries retry with the layer's backoff defaults; hand-rolled retry loops in components are forbidden.
7. **FE-207 — Mutations update exactly what they affect.** A mutation invalidates or optimistically updates precisely the affected queries. Optimistic updates always carry a rollback path that runs on failure.
8. **FE-208 — Production renders real server data only.** No fixture, canned, or hard-coded response stands in for a live endpoint in a production path; demo data is labeled as demo wherever it legitimately appears (WCPM DAT family, docs/WCPM_MAPPING.md §2.4).
9. **FE-209 — One in-flight request per key.** The same endpoint is never fetched repeatedly for one page render; shared data is requested once and served to all consumers from the cache.
10. **FE-210 — Offline behavior is designed.** Losing connectivity mid-session produces the designed error state, and reconnecting recovers through the query layer's refetch — not a manual reload (with ui-states).
11. **FE-211 — Inherited fetching law.** The WCPM §9 engineering rules apply as cited in docs/WCPM_MAPPING.md §2.2, and fetching work is designed to pass the G-ENG gate family.

## BAN list

- **BAN-FE-101 — Canned responses as live data.** Banned: shipping fixture or hard-coded responses presented as live server data. Defeats: DET-FAKE-008. Bad: search returns the same twelve canned results whatever the user types, rendered as real matches. Instead: query the real endpoint through the query layer; if the endpoint does not exist yet, the feature does not ship (FE-208). Severity: BLOCK.
- **BAN-FE-102 — Unkeyed requests racing.** Banned: issuing requests whose responses can arrive out of order and overwrite the current view. Defeats: DET-FAKE-022. Bad: typing in a filter fires a request per keystroke; the slowest response lands last and the list shows results for a query the user deleted. Instead: key the query by its parameters so only the current key's data renders (FE-204). Severity: BLOCK.
- **BAN-FE-103 — Swallowed errors.** Banned: empty `catch` blocks, silent fallbacks, or error paths that render nothing. Defeats: DET-VIS-032. Bad: `catch {}` around the fetch leaves a blank panel when the API is down. Instead: the error outcome renders the view's designed error state with a retry (FE-205). Severity: BLOCK.
- **BAN-FE-104 — Optimistic update with no rollback.** Banned: applying an optimistic change that stays on screen when the mutation fails. Defeats: DET-FAKE-011. Bad: Delete removes the row instantly; the request fails, but the row stays gone until a manual reload — a delete that only hides. Instead: snapshot the affected queries, roll back on error, and show the error state (FE-207). Severity: BLOCK.
- **BAN-FE-105 — Fixture filtering sold as search.** Banned: filtering or sorting a local fixture client-side while presenting it as server search over the real dataset. Defeats: DET-FAKE-017. Bad: "Search all 40,000 products" filters the 50 records bundled with the page. Instead: send the query to the server and render its results, with the result count from the server (FE-208). Severity: BLOCK.

## Gates

- **G-FE-101 — Network-count cache test.** Verifies: FE-201, FE-203, FE-209. Check: automated — Playwright navigates view A → B → A while counting requests; the shared endpoint is requested once, then served from cache with background revalidation per its `staleTime`. Pass: exactly one network request for the shared endpoint across the sequence. Fail: block shipment. Recorded in: progress.md.
- **G-FE-102 — Race test.** Verifies: FE-204. Check: automated — a test delays the first of two parameter changes so its response arrives after the second's, then asserts the view renders the second (current) key's data. Pass: the final render matches the current parameters. Fail: block shipment. Recorded in: progress.md.
- **G-FE-103 — Offline drill.** Verifies: FE-205, FE-210. Check: manual — go offline mid-session on the main views; confirm the designed error state appears, then reconnect and confirm recovery without a manual reload. Pass: error state and recovery both behave as designed. Fail: block shipment. Recorded in: progress.md.
- **G-FE-104 — Rollback test.** Verifies: FE-207. Check: automated — a test forces a mutation to fail after its optimistic update and asserts the UI reverts to the pre-mutation data and shows the error state. Pass: full rollback with a visible error. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **useEffect fetch sprawl.** Every component fetches its own copy of shared data on mount. Catch it: count requests for one endpoint on one page load — more than one means the query layer was bypassed (FE-201).
- **One global loading boolean.** A single app-level spinner flag flips for every query, so unrelated views flicker together. Catch it: loading must be per query and land in each view's own state matrix (FE-205).
- **Invalidate-everything mutations.** Any mutation refetches the entire cache "to be safe." Catch it: if a mutation's invalidation list is the whole key space, FE-207 was not applied.
- **Retry storms.** Failed requests retry immediately, in render, forever. Catch it: watch the network tab on a down API — retries must follow the layer's backoff, not the render cycle (FE-206).

## Examples

- [Example 1 — Per-component fetches replaced by one keyed query](examples/example-1.md) — corrects FE-201, FE-202.
- [Example 2 — Stale response overwriting a newer view](examples/example-2.md) — corrects FE-204.
- [Example 3 — Optimistic delete with rollback](examples/example-3.md) — corrects FE-207.

## Recall anchors

- Server state lives in the query cache, nowhere else.
- Keys mirror the API; freshness is chosen per data type.
- A stale response never overwrites a newer view.
- Optimistic always rolls back.
- Errors render a state; they are never swallowed.

## Checklist

- [ ] All server reads go through the query layer; no fetch-on-mount sprawl (FE-201).
- [ ] Query keys follow the resource scheme; `staleTime` is set per data type (FE-202, FE-203).
- [ ] Network-count test: shared endpoint requested once across A → B → A (G-FE-101).
- [ ] Race test: the current key's data is what renders (G-FE-102).
- [ ] Offline drill: designed error state appears and recovers on reconnect (G-FE-103).
- [ ] Failed mutations roll back their optimistic updates (G-FE-104).
- [ ] No fixture or canned response stands in for a live endpoint (BAN-FE-101).
