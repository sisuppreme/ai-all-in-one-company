# UI/UX Upscaler — Spec 07: Frameworks

> Companion spec to `skills/frontend/ui-ux-upscaler/SKILL.md`. Framework-agnostic core
> + concrete per-framework guidance for the upgrade.
> **SCOPE: web apps ONLY** (native: adaptation note in `02-theme-decision.md` §8 only).
> **Architecture-leak rule:** framework choices, file names, and component names are
> never user-facing. A component named `PostgresTable` that renders a leak is doubly
> wrong — rename the user-facing string AND the component if its name can reach the
> UI (e.g. via error boundaries or dev overlays) — see `09-architecture-leak.md` §3.5.

## 1. Framework-agnostic core (applies to every stack)

| Core piece | Rule |
|---|---|
| Token architecture | One token source (CSS custom properties on `:root`, with a `prefers-color-scheme`
  variant and a `prefers-reduced-motion` block beside it). Tokens are the ONLY source
  of colour/spacing/radii/shadows/durations/easings. Framework token layers (Tailwind
  config, MUI theme, CSS-in-JS theme) CONSUME the custom properties — they do not
  duplicate them. Two token sources = a token-sprawl defect (Pass 1 failure mode). |
| CSS custom properties | Named by role (`--surface`, `--text`, `--accent`, `--dur-fast`, `--ease-out`),
  never by value (`--blue-500` is a value name; `--accent` is a role name). Role names
  survive a palette change; value names do not. Token names use user/material concepts,
  never stack terms (`09-architecture-leak.md` §2). |
| Single animation loop | One rAF loop per page (`05-motion-system.md` §1): a passive position recorder +
  lerped displayed progress + change-guarded DOM writes. Framework re-renders never
  drive scroll motion (see §2–§4 per framework). |
| Audit/score workflow | Framework-independent steps (`01-audit-and-scoring.md` §4–§5): inventory, rendered
  walk at 1440/390 px, codebase greps, automated passes (axe, Lighthouse, Playwright
  no-JS / reduced-motion / observer-stub), leak sweep, score. The tools differ per
  stack; the steps and the evidence standard do not. |
| Behaviour freeze | The upgrade is presentation-layer first (Protocol Step 2). Routes, data, APIs, and
  outcomes are frozen during the upgrade; any structural change is justified in the
  audit file before it is touched. The freeze is enforced by the regression baseline
  (`10-regression-rollback.md` §1) — not by good intentions. |

## 2. React

### 2.1 Component-level token consumption

- Tokens are consumed via CSS custom properties in the component's stylesheet (or the
  framework's CSS layer), NOT via JS theme objects that duplicate them. A component
  that reads `theme.colors.accent` from a JS object while a `--accent` custom property
  exists has two token sources — collapse them (the custom property wins; the JS object
  reads it via `getComputedStyle` only where JS genuinely needs the value, e.g. canvas).
- Class composition: one class per state (`.btn`, `.btn--loading`), state classes
  toggled by the component's state — never inline styles for token values. Inline
  styles are reserved for genuinely dynamic values (a progress fill's scaleX, a
  scrubbed transform) and even those read tokens for their durations/easings.

### 2.2 Avoiding re-render jank in the scroll loop

- The shared loop (§1) lives OUTSIDE React state. Scroll progress is stored in a
  `ref` (or a module-level variable), never in `useState` — a `setState` per animation
  frame re-renders the tree and is the single most common React jank source in upgrades.
- Components that need scroll-driven values subscribe via a ref + direct DOM write
  (`ref.current.style.transform = ...` inside the loop's render callback, change-guarded
  per `05` §1.1) or via CSS custom properties set on a container (`--scroll-progress`)
  that CSS consumes — the CSS path is preferred (zero JS per frame per element).
- `React.memo` on scroll-affected subtrees is not a fix for a state-driven loop; fixing
  the loop's storage is. Memoise only after the loop is ref-based, and measure before/after.
- Lists: virtualise or paginate long lists before animating them (a 200-row table with
  a per-row reveal is S-5 + S-14 combined — see `04-component-upgrades.md` §6 for the
  stagger cap of 12 rows).

### 2.3 Suspense / skeleton patterns

- Route-level `Suspense` boundaries wrap the route's content; the fallback is the
  route's skeleton (matching the layout, `04` §16), NOT a generic spinner. A Suspense
  fallback that does not match the layout causes layout shift when content lands.
- Data loading inside a component uses the component's own skeleton (same rule).
  Skeletons show only for waits ≥300 ms — implement with a delayed-show (a 300 ms
  timer before the skeleton mounts; if data arrives first, no skeleton ever appears).
- Error boundaries: the fallback UI is a user-concept error state (`04` §17, L-C3) —
  never the error's `message`, stack, or component name. Log the technical detail to
  the error service; show the user the next step. An error boundary that renders
  `error.message` is an architecture leak (`09` §3.5).

### 2.4 React-specific pitfalls

- `useEffect` for scroll listeners: the listener is passive and records position only;
  the loop is created once (module scope or a singleton hook), not per component.
  A component that creates its own rAF loop is a Pass 5 failure.
- StrictMode double-effects: the loop must tolerate mount/unmount/remount without
  creating a second loop (guard by a module-level "loop alive" flag).
- Hydration (SSR/Next.js): hidden reveal states are JS-gated (added after hydration),
  never server-rendered — a server-rendered `opacity: 0` is stranded content for every
  user whose JS fails (BAN-FE-051).

## 3. Vue

### 3.1 Component-level token consumption

- Same rule as React (§2.1): CSS custom properties are the token source; the Vue
  theme (if any) consumes them. Scoped styles consume tokens via `var(--accent)` —
  scoped CSS does not scope custom properties, which is correct: tokens are global by design.
- Do not duplicate tokens into Vue's `provide/inject` theme objects. If a value is
  needed in JS (canvas, charts), read it from `getComputedStyle(document.documentElement)`.

### 3.2 Avoiding re-render jank in the scroll loop

- Scroll progress lives in a non-reactive store (a plain object / `ref` outside the
  reactive system, or `markRaw`) — never in reactive `data`/`ref` that triggers
  re-renders per frame. Vue's reactivity is the same trap as React's `useState` here.
- Scroll-driven styles are applied via direct DOM writes in the loop or via CSS
  custom properties on a container (`:style="{ '--scroll-progress': ... }"` on a
  container is acceptable ONLY if that binding updates at most once per frame through
  the shared loop — a per-component binding that updates independently is a second loop).
- `v-memo` on scroll-affected subtrees is a secondary optimisation, not the fix.

### 3.3 Suspense / skeleton patterns

- `<Suspense>` with a layout-matching skeleton fallback (same 300 ms delayed-show rule
  as React §2.3). Async components (`defineAsyncComponent`) use the same skeleton as
  their loading component — never the framework's default spinner.
- Error handling (`onErrorCaptured` / error boundaries): user-concept fallback UI only
  (L-C3); technical detail goes to the error service, never the screen.

### 3.4 Vue-specific pitfalls

- Watchers on scroll position: a `watch` on a reactive scroll value that writes styles
  is a per-frame handler by another name — replace with the shared loop.
- Transitions (`<Transition>`): use for route/component state changes (200–240 ms,
  token easings); do NOT use `<Transition>` for scroll-linked motion — that is the
  loop's job. A scroll reveal implemented as a Vue transition on a scroll event is
  BAN-FE-056 with a framework costume on.

## 4. Plain HTML / CSS / JS (progressive enhancement, no-build-step path)

### 4.1 Structure

- Tokens: a single `tokens.css` (`:root` custom properties + `prefers-color-scheme` +
  `prefers-reduced-motion` blocks). Every other stylesheet consumes `var(--*)`.
  No build step is needed for this — a `<link>` is enough.
- Motion: a single `motion.js` (~5–8 KB) implementing the shared loop, the observer
  setup, the watchdogs, and the reduced-motion gating. One file, no dependencies,
  loaded with `defer`. If `motion.js` fails to load, the page is the designed static
  page (content visible — the JS-gating rule means nothing is hidden without it).
- Components: progressive enhancement — every component works as plain HTML first
  (a form submits, a tab list is anchor links, a modal is a `<details>`/anchor fallback),
  and JS enhances it. The no-JS pass (`05` §6.4 test 1) is trivially satisfied when
  this discipline holds, which is the point.

### 4.2 No-build-step token introduction

- Add `tokens.css` first (Pass 1) with the extracted values as the initial token values
  (so the visual change is zero — see §5). Then replace hard-coded values file by file
  with `var(--*)` references. A page that looks identical after Pass 1 has passed Pass 1.
- Class naming: BEM or equivalent (`.card`, `.card__title`, `.card--featured`) — the
  naming convention matters less than its consistency; record the convention in the
  audit file and lint for it (a second naming convention appearing mid-upgrade is a
  Pass 1 failure mode).

### 4.3 Plain-JS pitfalls

- One `motion.js`, one loop. A second script that adds its own scroll listener is a
  Pass 5 failure — grep for `addEventListener('scroll'` across ALL scripts at Pass 5 exit.
- `IntersectionObserver` with a `rootMargin` of `0px 0px -10% 0px` for reveals; the
  watchdog is a `setTimeout` per element (1500 ms after first entry, `05` §6.2).
- No framework means no error boundary: `window.onerror` shows nothing to the user
  (it logs to the error service); user-facing errors are rendered by the app's own
  error-state markup (`04` §17).

## 5. Introducing tokens into a codebase with hard-coded values

### 5.1 Codemod strategy

1. **Count first:** grep the codebase for hard-coded values (hex, rgb, px spacing,
   durations) and record the counts per file in the audit file. A codemod run without
   a before-count cannot prove it worked.
2. **Tokenise values, not files:** build the token file from the VALUE inventory
   (the 8 most-rendered colours, the spacing scale actually used) — not by walking
   files alphabetically. Values that appear once are either merged into the nearest
   token (ΔE < 8 for colour; ±4 px for spacing) or recorded as defects.
3. **Codemod in three sweeps:** (a) colours — replace hex/rgb literals with
   `var(--*)` (or the framework equivalent); (b) spacing/radii/shadows; (c) durations/
   easings. One sweep per commit, each verified by its grep returning 0 and by the
   screenshot diff (<0.5% pixel change on non-token areas).
4. **Guard the seams:** third-party CSS (component libraries, embeds) is EXCLUDED
   from the greps (record the exclusion list); values inside it are not the app's to
   tokenise — but a third-party component that renders user-facing stack text (e.g. a
   default error page) is still a leak and is overridden, not accepted (`09` §3.5).
5. **Lint lock:** after the codemod, add the lint that fails the build on a hard-coded
   value outside the token file (the design-tokens literal lint, extended to motion —
   motion G-FE-043). Without the lint, hard-coded values return within a week.

### 5.2 The no-hard-coded-values rule (enforcement)

- After Pass 1, the rule is: no colour, spacing, radius, shadow, duration, or easing
  literal outside the token file (excluding 1 px hairlines, recorded, and third-party
  CSS, listed). The rule is enforced by the lint, not by review — review catches
  intent, lint catches literals.
- Exceptions are recorded in the audit file with a reason and a re-check date. An
  unrecorded exception found by the lint is a Pass 1 failure, not a warning.

## 6. Keeping the upgrade shippable incrementally

### 6.1 Per-route / per-component rollout

- Roll out per route family (landing → content → dashboard → forms → settings), in
  the order of highest traffic / highest defect density first (audit §6). Each family
  goes through all 7 passes before the next family starts ONLY if the team is small;
  larger teams may pipeline (family A in Pass 5 while family B is in Pass 3) — but a
  family never skips a pass, and the pass order within a family is never reordered.
- Per-component rollout inside a family: the component inventory (`01` §1) is the
  rollout list; each component is upgraded, state-matrix-tested, and merged independently.

### 6.2 Flag strategy

- **Branch:** the upgrade lives on its own branch (`upscale/<app>`) until the gate
  passes (`11-scoring-shipping.md` §4). Never upgrade on `main` — a half-upgraded
  `main` is unshippable by definition. Full branch/flag/rollback spec: `10-regression-rollback.md`.
- **Flags:** one flag per route family (`upscale.landing`, `upscale.dashboard`, …),
  plus one flag per high-risk pass (Pass 5 motion: `upscale.motion.<family>`).
  Flags are boolean, server- or build-time (record which), and default OFF. A flag
  flips ON only when that family's regression checklist is green (`10` §2) AND its
  per-family gate score passes (`11` §1).
- **Flag hygiene:** flags are removed in the pass that follows their flip (the cleanup
  commit is part of the pass, not "later"). A flag older than 2 passes is a defect —
  it means the old code path is still shipped alongside the new one.
- **Rollback:** each flag's OFF state is the rollback (see `10` §4). Rolling back is
  flipping a flag, not reverting a merge — which is why the branch + flag discipline
  exists.

### 6.3 What "shippable" means mid-upgrade

At any point during the upgrade, `main` is shippable (the upgrade is on its branch)
and the upgrade branch is shippable per-family (families whose flags are ON have passed
their checklists). A mid-upgrade state where no family can ship is a planning failure,
not a technical one — re-plan the rollout order (§6.1) before writing more code.

## 7. Cross-reference map

| This file's section | Where it is used |
|---|---|
| §1 core | Pass 1 (tokens), Pass 5 (loop) — `03-staged-passes.md` |
| §2–§4 frameworks | Implementation of `05-motion-system.md` §1 per stack |
| §5 codemod | Pass 1 execution detail |
| §6 incremental rollout | `10-regression-rollback.md` (branch/flag/rollback); `11-scoring-shipping.md` (per-family gates) |
