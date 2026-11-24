# frontend-state

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Redux principles (single source of truth, read-only state, pure reducers), summarized at — https://www.freecodecamp.org/news/an-intro-to-redux-and-how-state-is-updated-in-a-redux-application-839c8334d1b1/ ; TanStack Query, Important Defaults (the server-state boundary) — https://tanstack.com/query/latest/docs/framework/react/guides/important-defaults
- **Depends on:** frontend-core
- **Feeds into:** data-fetching, client-routing, pwa-offline

## When to use / Do NOT use

- **Use when:** deciding where a piece of client-side state lives; introducing or refactoring a store; debugging views that disagree with each other; making view state shareable through the URL.
- **Do NOT use when:** the data comes from the server — fetching, caching, freshness, and refetch belong to data-fetching, and server data is never stored in this layer (FE-184). Do not use this skill to pick a state library's API details; it governs ownership and flow, not vendor syntax.

## Rules

1. **FE-181 — Classify before storing.** Every piece of state is classified before it is stored: local to one component, shared across the app (store), shareable view state (URL), or server data (not this layer — data-fetching).
2. **FE-182 — One owner, one update path.** Each shared fact has exactly one owner and one path by which it changes; two components holding copies of the same fact is a defect.
3. **FE-183 — No in-place mutation.** Shared state is never mutated directly from arbitrary components; changes go through the store's actions, reducers, or setters, so every change is traceable.
4. **FE-184 — Server data is never mirrored.** Server responses are never copied into the client store and hand-synchronized; the query cache (data-fetching) is their only home.
5. **FE-185 — The DOM is not a source of truth.** State is not stored in CSS classes, data attributes, or hidden inputs; the DOM renders state, it does not hold it.
6. **FE-186 — Shareable state lives in the URL.** Filters, selected tab, pagination, and sort order live in the URL, so refresh, the back button, and shared links land on the same view.
7. **FE-187 — Derived values are computed, not stored.** Anything calculable from stored state (totals, counts, filtered lists) is derived at read time, never kept as a second stored copy that can drift.
8. **FE-188 — Ownership is documented.** Each store slice records its owner fact, who may write it, and who reads it; an undocumented slice is treated as unowned and reviewed.
9. **FE-189 — Client flags are not session truth.** A client-side boolean (for example `isLoggedIn` in a store) never substitutes for the server's session and authorization checks; it may mirror them for display, and the server decides.
10. **FE-190 — Inherited state boundary.** The WCPM §9 engineering rules and the DAT parameter family's state/fetching boundary apply as cited in docs/WCPM_MAPPING.md §2.2 and §2.4, and state work is designed to pass the G-ENG gate family.

**Architecture must never leak into the UI.** State is the user's situation, not the store's. Store names, slice names, state-machine names, and cache keys must never appear in the UI, in labels, or in error text; a stale or missing piece of state is expressed as what the user sees and can do, never as which store or query failed. The interface shows the user's world as it is; the machinery that holds it stays invisible.

## BAN list

- **BAN-FE-091 — Hand-synchronized server mirror.** Banned: copying server data into a global store and keeping it current with manual sync code. Defeats: DET-FAKE-004. Bad: the orders list is fetched once, stored in Redux, and patched by hand after each mutation — the dashboard shows frozen numbers the API no longer agrees with. Instead: read through the query cache and invalidate on mutation (data-fetching). Severity: BLOCK.
- **BAN-FE-092 — DOM as source of truth.** Banned: reading application state back from classes, data attributes, or hidden inputs. Defeats: DET-FAKE-016. Bad: whether the panel is "saved" is read from a `data-saved` attribute, so profile edits appear to work and do not stick after reload. Instead: state lives in the store; the DOM only renders it (FE-185). Severity: BLOCK.
- **BAN-FE-093 — Client flag as authorization truth.** Banned: gating data or actions on a client-side flag instead of the server's session check. Defeats: DET-FAKE-002. Bad: the app hides the admin route when `state.user.isAdmin` is false and the API serves the data to anyone who asks. Instead: the API authorizes every request; the flag only shapes display (FE-189). Severity: BLOCK.
- **BAN-FE-094 — The same fact stored twice.** Banned: keeping one fact in two places (store plus component state, or two slices) with independent updates. Defeats: DET-FAKE-005. Bad: the cart count lives in the header component and the cart page separately; they disagree after an update and reset differently on reload. Instead: one owner (FE-182); every other view derives or subscribes. Severity: WARN.

## Gates

- **G-FE-091 — Trace test.** Verifies: FE-182, FE-187. Check: manual — for each shared fact, name its owner and update path from the slice documentation, change it in one view, and confirm every dependent view updates without a reload. Pass: every fact traces and propagates. Fail: block shipment. Recorded in: progress.md.
- **G-FE-092 — Mutation lint.** Verifies: FE-183. Check: automated where the stack provides one — run the store's immutability lint (for example a Redux-style rule forbidding direct state mutation outside reducers). Pass: zero violations. Fail: block shipment. If the stack has no such rule, its absence is recorded in progress.md and G-FE-091 carries the weight. Recorded in: progress.md.
- **G-FE-093 — URL state round-trip.** Verifies: FE-186. Check: automated — Playwright sets filters, tab, and page; reloads; opens the same URL in a fresh page. Pass: both pages render the identical view state. Fail: block shipment. Recorded in: progress.md.
- **G-FE-094 — Store mirror scan.** Verifies: FE-184. Check: automated — grep the store slices for assignments of API response payloads (response types, `fetch`/`axios` results written into reducers). Pass: no hand-mirrored server data in the store. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The god store.** Every value in the app, server and UI alike, is dumped into one global store. Catch it: if the store holds fetched lists, it has absorbed data-fetching's job (FE-184).
- **Prop-drilling denial.** State is threaded through eight components instead of being classified and owned. Catch it: a prop passed through three or more components that do not use it is unclassified state.
- **Context as dumping ground.** One provider holds unrelated facts, so any change re-renders everything and ownership is unknowable. Catch it: if a slice's readers cannot be listed, FE-188 has failed.
- **Stored derivations.** A total is kept in state next to the items it sums, and the two drift apart. Catch it: any stored number that could be recomputed from other stored state is suspect (FE-187).

## Examples

- [Example 1 — Server mirror replaced by the query cache](examples/example-1.md) — corrects FE-184.
- [Example 2 — Filters lost on refresh moved into the URL](examples/example-2.md) — corrects FE-186.
- [Example 3 — Two cart counts replaced by one owner](examples/example-3.md) — corrects FE-182.

## Recall anchors

- Classify before you store: local, shared, URL, server.
- One fact, one owner, one update path.
- Server data is never mirrored by hand.
- The DOM renders state; it never holds it.
- If it can be computed, do not store it.

## Checklist

- [ ] Every shared fact has a named owner and update path (FE-182, FE-188).
- [ ] Trace test passes for all shared facts (G-FE-091).
- [ ] No server payloads are stored in client slices (G-FE-094).
- [ ] Filters, tab, and pagination survive reload and link sharing (G-FE-093).
- [ ] No state is read back from the DOM (FE-185).
- [ ] No client flag substitutes for a server session check (FE-189).
- [ ] Mutation lint is clean, or its absence is recorded (G-FE-092).
