# pwa-offline

## Metadata

- **Owner department:** D3 Frontend, Design & Motion (FE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** MDN, Offline and background operation — https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation ; inherited Web Craft Pro Max rules R-11.7-1 and R-11.7-2, mapped in docs/WCPM_MAPPING.md
- **Depends on:** frontend-core, data-fetching
- **Feeds into:** ui-states, client-routing

## When to use / Do NOT use

- **Use when:** a web app claims installability or offline capability, or a service worker or web app manifest is being added or changed.
- **Do NOT use when:** the site is content-only with no app behavior and no offline claim (frontend-core suffices), or the question is native-app offline storage (out of scope for this repo's web phase).

## Rules

1. **FE-281 — The manifest is complete and correct.** Name, short name, icons in all required sizes including a maskable icon, theme and background colors, display mode, start URL, and scope are all present and accurate (inherited R-11.7-1).
2. **FE-282 — Manifest and service worker ship as a pair.** A manifest without a working service worker, or a service worker with no manifest, is a defect — the pair ships together or not at all.
3. **FE-283 — Every resource class has a named strategy.** The app shell is precached at `install`; static assets go cache-first; data goes network-first or stale-while-revalidate. The strategy per class is written down in the project notes before the worker is coded.
4. **FE-284 — Cache names are versioned and old caches are cleaned.** Cache names carry the app version, and `activate` deletes every cache that is not the current version, so updates actually reach users.
5. **FE-285 — The offline experience is designed.** Losing connectivity shows the product's own offline page or state, in the design system — never the browser's default error page (inherited R-11.7-2).
6. **FE-286 — The update flow is part of the design.** When a new service worker is waiting, the user is told a new version is available (or the update applies on next navigation by design) — no user is stranded on a weeks-old cached app.
7. **FE-287 — Offline scope is stated honestly.** If only the shell and cached pages work offline, the UI says so. Claim PWA capability only for what the core task can actually do offline.
8. **FE-288 — Queued actions sync without data loss.** Actions taken offline (form submissions, edits) are queued locally and synced on reconnect; a reconnect never silently drops or duplicates them (inherited R-11.7-2).
9. **FE-289 — Install is offered, never forced.** The install prompt appears only after real engagement, and dismissing it is final for the session (inherited R-11.7-1).
10. **FE-290 — Private responses stay out of shared caches.** Authenticated API responses and per-user data are network-only, or cached under a per-user key with an explicit lifetime — never in a cache another user of the same browser could be served.

**Architecture must never leak into the UI.** Offline capability is a promise, never a technical report. Cache names, service-worker states, sync-queue contents, and storage details must never surface in the UI — an offline state says what the user can still do and what will happen when they reconnect, in plain words, never naming the cache, the worker, or the sync mechanism. The app works offline; how it does so stays invisible.

## BAN list

- **BAN-FE-141 — Browser-default offline error.** Banned: shipping a service worker whose fetch failures surface the browser's "no internet" page. Defeats: DET-UX-010. Bad: user opens the app on a train and gets the browser dinosaur instead of the product. Instead: precache a designed offline page and serve it for failed navigations (FE-285). Severity: BLOCK.
- **BAN-FE-142 — Cache-everything-forever.** Banned: one cache-first handler for every request with an unversioned cache name and no cleanup. Defeats: DET-VIS-032. Bad: a pricing fix ships, but returning users are served the month-old cached app indefinitely — the UI presents a state that no longer exists. Instead: per-class strategies, versioned names, `activate` cleanup (FE-283, FE-284). Severity: BLOCK.
- **BAN-FE-143 — Half a PWA.** Banned: a manifest with no service worker (or the reverse) shipped while the site claims to be installable/offline-capable. Defeats: DET-VIS-032. Bad: the install banner appears, the app "installs," and the first offline open fails completely. Instead: ship the pair together or make no PWA claim (FE-282). Severity: BLOCK.
- **BAN-FE-144 — Offline claims beyond offline reality.** Banned: marketing or UI copy claiming the app "works anywhere, even offline" when only the shell is cached. Defeats: DET-VIS-032. Bad: the landing page promises full offline work; offline, every data screen is an error. Instead: state the real scope in the UI (FE-287). Severity: WARN.

## Gates

- **G-FE-141 — Lighthouse installability audit in CI.** Verifies: FE-281, FE-282. Check: automated — run Lighthouse's installability/PWA checks against the production build in CI. Pass: installable, manifest valid, service worker registered and controlling the page. Fail: block shipment. Recorded in: progress.md.
- **G-FE-142 — Offline reload test.** Verifies: FE-283, FE-285, FE-287. Check: automated — Playwright: load the app online, switch the context to offline, reload, and either complete the stated core task or arrive at the designed offline state. Pass: core task completes or the designed offline state renders — never a browser error. Fail: block shipment. Recorded in: progress.md.
- **G-FE-143 — Update drill.** Verifies: FE-284, FE-286. Check: manual — deploy a build with a bumped service-worker version to a test install; confirm the update path offered to the user works and the previous version's caches are gone in DevTools. Pass: new version active after the designed flow, old caches deleted. Fail: warn, fix before release. Recorded in: progress.md.
- **G-FE-144 — Cache contents inspection.** Verifies: FE-283, FE-290. Check: manual — DevTools Application tab: service worker active, manifest parses, and cache contents match the written strategy table class for class, with no authenticated responses in shared caches. Pass: contents match the strategy. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The immortal cache.** The app "never updates" for returning users after every deploy. Catch it: if support answers bugs with "hard-refresh," FE-284/FE-286 were skipped.
- **The offline fig leaf.** An offline page exists but every real screen still dies without a network. Catch it: run G-FE-142 against the core task, not just the home page.
- **Strategy by default.** The worker was copied from a tutorial — one runtime cache for everything, API calls included. Catch it: ask for the written strategy table (FE-283); if none exists, the worker is unreviewed.
- **Install-begging.** An install prompt on first paint, before the user has done anything. Catch it: if the prompt precedes engagement, FE-289 is violated no matter how pretty the banner is.

## Examples

- [Example 1 — Cache-everything handler replaced by per-resource strategies](examples/example-1.md) — corrects FE-283.
- [Example 2 — Browser error offline replaced by a designed offline page](examples/example-2.md) — corrects FE-285.
- [Example 3 — Unversioned cache replaced by versioned caches with cleanup](examples/example-3.md) — corrects FE-284.

## Recall anchors

- Manifest and service worker ship together, or not at all.
- Every resource class has a strategy and a lifetime.
- Offline shows the product's page, never the browser's.
- Versioned caches; activate cleans up.
- Claim only the offline scope that actually works.

## Checklist

- [ ] Manifest complete: names, icons incl. maskable, colors, display, start URL, scope (FE-281).
- [ ] Lighthouse installability audit green in CI (G-FE-141).
- [ ] Written strategy table exists and the worker implements it class for class (FE-283).
- [ ] Offline reload test passes on the core task or designed offline state (G-FE-142).
- [ ] Update drill done: new version reaches users, old caches deleted (G-FE-143).
- [ ] No authenticated responses in shared caches (FE-290, G-FE-144).
- [ ] Offline scope stated honestly in the UI (FE-287).
