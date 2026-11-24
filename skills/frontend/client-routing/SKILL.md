# client-routing

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** React Router data-router guide (loaders, error boundaries) — https://micropyramid.com/blog/react-router-for-navigation/ ; inherited Web Craft Pro Max rules R-5.2-3, R-10.1-4 and cure CD-06, mapped in docs/WCPM_MAPPING.md
- **Depends on:** frontend-core, data-fetching
- **Feeds into:** ui-states, frontend-state

## When to use / Do NOT use

- **Use when:** building or changing the route structure of a single-page app or hybrid site — defining routes, navigation, guards, deep links, or the 404 view.
- **Do NOT use when:** the site is a set of plain server-rendered pages with no client router (the server framework's routing and frontend-core apply), or the question is what data a route loads (data-fetching owns fetching; this skill owns the URL and navigation contract).

## Rules

1. **FE-221 — Every meaningful view has a real URL.** If a user would bookmark it, share it, or return to it, it is a route — not a component swapped by local state.
2. **FE-222 — No state-flag navigation.** Refresh, deep link, and the back/forward buttons must all land on the correct view. A view reachable only by clicking from another view is a defect.
3. **FE-223 — Loaders fetch before render, errors stay local.** Routes load their data in route loaders (or the framework equivalent) and each route carries an error boundary, so a failed route renders its error view inside the layout instead of crashing the app shell.
4. **FE-224 — Unknown paths render the designed 404.** A catch-all route shows the product's 404 view with a path back into the product (inherited cure CD-06: design the 404 and error pages). A blank screen on a bad URL is a defect.
5. **FE-225 — Guards are UX only.** A route guard may redirect an unauthenticated user to login, but protected data is authorized by the API on every request, never by the router. Hiding a route is not protecting it.
6. **FE-226 — Crawlable links for indexable pages.** Navigation to public pages uses plain `<a href>` links to indexable canonical URLs — no JavaScript-only navigation for indexable pages (inherited R-5.2-3).
7. **FE-227 — One canonical URL per public page.** Every public page carries a canonical URL that returns 200 and does not redirect (inherited R-10.1-4; gate G-SCH-02).
8. **FE-228 — Navigation manages scroll and focus.** On navigation, scroll is restored on back/forward and reset on new views, and focus moves to the new view's heading or main region so keyboard and screen-reader users start at the top of the new content, not stranded mid-page.
9. **FE-229 — No full-page reloads inside the SPA.** In-app navigation uses the router's link component; a full document reload between app views breaks FE-222's back/forward and scroll contract.
10. **FE-230 — Route changes are announced.** The document title updates on every route change, and route transitions expose the loading state owned by ui-states — a silent, frozen screen during navigation is a missing state, not a fast load.

**Architecture must never leak into the UI.** Routes are addresses for the browser, not labels for the user. Route paths, route counts, the route tree, and navigation internals must never surface — no sitemap-style counts ('12 pages'), no route names as headings, no URL-shaped text in the interface. Navigation shows destinations in the user's words; how many routes exist and how they are organised stays behind the interface.

## BAN list

- **BAN-FE-111 — State-flag navigation.** Banned: switching views with a state variable (`const [page, setPage] = useState('home')`) instead of routes. Defeats: DET-UX-014. Bad: the settings view exists only as `page === 'settings'`; refreshing on it returns to home and the URL never changes. Instead: define a route per view and navigate with the router. Severity: BLOCK.
- **BAN-FE-112 — Blank screen on an unknown URL.** Banned: a route table with no catch-all, so an unmatched path renders an empty shell. Defeats: DET-UX-010 (see also DET-VIS-032). Bad: `/setings` (typo) renders the header, the footer, and nothing between. Instead: a catch-all route rendering the designed 404 view (FE-224). Severity: BLOCK.
- **BAN-FE-113 — JavaScript-only navigation for indexable pages.** Banned: `<div onClick>` or button handlers as the only way to reach a public page. Defeats: DET-UX-002. Bad: product pages reachable only through a clickable card div; crawlers, middle-click, and open-in-new-tab all fail. Instead: real anchor links to canonical URLs (inherited R-5.2-3). Severity: BLOCK.
- **BAN-FE-114 — Router guard as the authorization boundary.** Banned: treating a client-side guard as protection for data the API serves without its own check. Defeats: DET-FAKE-002 (see also DET-VIS-032). Bad: `/admin` is hidden by a guard, but `GET /api/admin/users` answers any authenticated session. Instead: the guard redirects for UX; the API authorizes every request (FE-225). Severity: BLOCK.

## Gates

- **G-FE-111 — Cold-load and traversal pass.** Verifies: FE-221, FE-222, FE-224. Check: automated — Playwright: cold-load a nested route directly in a fresh tab and assert the correct view renders; traverse five views using link navigation plus back/forward and assert each lands correctly; load a nonsense URL and assert the designed 404 view appears. Pass: all assertions green. Fail: block shipment. Recorded in: progress.md.
- **G-FE-112 — Refresh sweep.** Verifies: FE-222. Check: manual — refresh the browser on every route in the route table during QA; each must return the same view with its data. Pass: every route survives refresh. Fail: block shipment. Recorded in: progress.md.
- **G-FE-113 — Authorization boundary probe.** Verifies: FE-225. Check: automated — request each guarded route's API endpoints with no credentials and with a non-privileged session (e.g. `curl -i https://<host>/api/admin/users`); assert 401/403 and no protected payload in any response. Pass: no endpoint leaks data. Fail: block shipment. Recorded in: progress.md.
- **G-FE-114 — Focus and scroll check.** Verifies: FE-228, FE-230. Check: manual browser verification — navigate by keyboard through three views; after each navigation, focus sits on the new view's heading/main region, the title has changed, and back returns the previous scroll position. Pass: all three behaviors observed. Fail: warn, fix before release. Recorded in: progress.md.

## Anti-patterns

- **The modal-as-route.** A "page" implemented as a full-screen modal over home: no URL, no back button, lost on refresh. Catch it: if closing it is the only way back, it should have been a route.
- **Redirect chains as architecture.** Legacy paths bouncing through two or three redirects to reach the real view. Catch it: follow every published URL; more than one hop is rework, and it breaks FE-227's canonical rule.
- **The guard forest.** Authorization logic smeared across a dozen route guards with slightly different conditions. Catch it: if two guards disagree about the same role, the rule belongs in one place — and the API check (FE-225) is the one that counts.
- **Query-string views.** Distinct views distinguished only by `?tab=` or `?view=` parameters that the router ignores, so links share one history entry. Catch it: if two "views" highlight different nav items but share a path, they are routes wearing a disguise.

## Examples

- [Example 1 — State-flag navigation replaced by real routes](examples/example-1.md) — corrects FE-222.
- [Example 2 — Missing catch-all replaced by a designed 404 route](examples/example-2.md) — corrects FE-224.
- [Example 3 — Guard-only protection replaced by guard plus API authorization](examples/example-3.md) — corrects FE-225.

## Recall anchors

- If a user would bookmark it, it is a route.
- Refresh, deep link, back button — all three must land correctly.
- Guards redirect; APIs authorize.
- Unknown path = designed 404, never a blank screen.
- Navigation moves focus and updates the title.

## Checklist

- [ ] Every meaningful view has its own route and URL (FE-221).
- [ ] Playwright cold-load/traversal/404 pass is green (G-FE-111).
- [ ] Refresh sweep done on every route (G-FE-112).
- [ ] API probe confirms no guarded data leaks (G-FE-113).
- [ ] Public navigation uses real anchor links to canonical URLs (FE-226, FE-227).
- [ ] Focus, title, and scroll behavior verified by keyboard (G-FE-114).
