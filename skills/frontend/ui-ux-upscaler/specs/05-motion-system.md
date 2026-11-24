# UI/UX Upscaler — Spec 05: Motion System for Existing Apps

> Companion spec to `skills/frontend/ui-ux-upscaler/SKILL.md`. Expands Protocol
> Step 4 Passes 5–6. Authority: `skills/frontend/motion/SKILL.md` (FE-081–FE-097),
> `skills/frontend/scroll-experiences/SKILL.md` (FE-101–FE-115),
> design-intelligence §3 (motion judgment), §1.3 (dial).
> **SCOPE: web apps ONLY** (native: adaptation note in `02-theme-decision.md` §8 only).
> **Architecture-leak rule:** motion never carries stack information — counters animate
> real user numbers only (never record counts, never "12 tables synced"); progress
> indicators measure the user's progress, never the app's structure (`09-architecture-leak.md`).

## 1. The one shared lerped animation loop (never raw scroll handlers per element)

### 1.1 Contract

- Exactly ONE `requestAnimationFrame` loop per page drives ALL scroll-linked and
  time-based motion. Per-effect timers and competing loops are defects (motion FE-095).
  Recorded exception: a WebGL/canvas scene may run its own loop ONLY if it is the
  page's single spectacle element and the exception is recorded with its frame budget.
- The loop reads a TARGET progress (from a passive scroll listener or IntersectionObserver
  — recording position is all the listener may do) and eases the DISPLAYED value toward
  it with lerp. Every scroll effect reads the displayed value. Raw `scrollY` (or a raw
  ratio) is never applied to styles (scroll-experiences BAN-FE-056).
- Lerp factor: `0.12` default (weighty, settles in ~300 ms after scroll stops);
  `0.08` for heavy/pinned scenes (slower, more mass); `0.18` for light UI feedback
  (progress fills, counters). The factor is a token (`--lerp-default 0.12`), not a
  per-element improvisation.
- The loop writes transform/opacity ONLY (motion FE-083). Any animation of `width`,
  `height`, `top`, `left`, or margins needs a written exception with a measured frame
  budget — and the exception is per-element, per-pass, never global.
- The loop is change-guarded: a DOM write happens only when the displayed value moved
  by more than its epsilon (0.001 for progress, 0.5 px for translate). Unchanged values
  cost zero writes.
- The loop pauses when the tab is hidden (`visibilitychange`) and when no subscriber
  has moved in 2 s (idle sleep); it resumes on the next scroll/input event. A loop
  that runs forever on a static page is a performance defect.

### 1.2 Retrofit: replacing existing scroll handlers

1. Grep for `addEventListener('scroll'`, `onscroll`, and per-element observers doing
   style writes. Inventory each: what it moves, what it reads.
2. Replace in one pass per route family: each handler becomes a subscriber to the
   shared loop (it declares a target + a render function; the loop calls the render
   with the smoothed value). The old handler is deleted in the same commit — a
   handler left "just in case" is a second loop.
3. Verify per family: scroll profile before/after (long tasks, frame time); the
   after-profile must show zero scroll-linked long tasks >50 ms.

### 1.3 CSS scroll-driven timelines (preferred where supported)

Where the browser supports `animation-timeline: scroll()` / `view()`, prefer it for
reveals and parallax — the compositor does the work and there is no JS loop cost.
The smoothed-JS loop (§1.1) is the designed fallback for unsupported browsers
(scroll-experiences FE-108): the fallback must produce the same end states, and the
no-JS state is the designed static page (content simply present). Test both paths:
with timelines supported and with them force-disabled.

## 2. Every motion term — job, durations, easings, triggers, where it belongs

Each term below names its job (design-intelligence §3.1, motion FE-081). A term with
no job on this app's content is recorded as absent-with-reason, never silently dropped.

| Term | Job | Durations / easings (tokens) | Trigger | Where it belongs in an existing app |
|---|---|---|---|---|
| Scroll-triggered reveals | Land a section's message as it arrives | 400–640 ms, `--ease-out cubic-bezier(.3,.7,.3,1)`; stagger 40 ms, cap 8 items | Element enters viewport (IntersectionObserver, rootMargin 0px 0px -10% 0px); re-trigger on re-entry for marketing, once-per-session for dashboards/listings | Marketing sections, cards, section headings. NEVER a uniform fade-up on every section (BAN-FE-041) — vary distance (8–24 px), duration, and mask per section in the theme's language |
| Scroll-driven / scrub animation | Show change, process, or a journey | Scrubbed: progress-mapped, no fixed duration; smoothing lerp 0.12 | Scroll progress through a pinned or long section | A process the user must understand by descending (a ledger balancing, a route drawing, a vessel mending). Never where a labelled static diagram communicates as well |
| Parallax | Give a world depth | Layers ≤3 depths; offsets 0.94 / 1.0 / 1.06 of scroll; lerp 0.12 | Smoothed scroll progress | Hero/background layers, scene depth. NEVER over forms, tables, or checkout; never where text swims against its background |
| Pinned sections | Hold one moment while the story moves | Pin length 100–130 vh of scroll (100 vh stage + 0–30 vh travel); pin content static, world moves | Scroll progress through the pin | One moment per page that earns the viewport (a scene, a build-up). Never two pins competing in one viewport span; never pinning a paragraph that could simply be read |
| Smooth scrolling | Let scroll feel weighted, not stepped | Lerp 0.12 on the displayed progress; native scroll position never overridden | Always (the loop) | Every page. This is NOT scroll-jacking: position, direction, and speed stay the user's (scroll-experiences FE-103) |
| Progress indicator | Show position/progress through the document or task | Fill: transform scaleX, 200 ms per step; in-theme form (filling vessel, route line, depth gauge — a bare bar only when the theme is genuinely minimal) | Scroll progress (document) or completed steps (task) | Long articles/guides (document progress, in-theme); multi-step flows (step progress, honest — never jumps). Never the sole wayfinding (FE-106: structure carries position) |
| Staggered + masked reveals | Land a group as a sequence, not a block | Stagger 40 ms, cap 8 (total ≤320 ms + 640 ms item = ≤960 ms); mask: clip-path inset or translateY 12–24 px + fade | Group enters viewport | Card grids, feature lists, nav drawer links. Masked line reveals for display headings: 40 ms per letter, capped at 24 letters |
| Kinetic typography | Make type itself the event | Letter stagger 40 ms cap 24; word rise 12 px, 400 ms `--ease-out` | Hero/first viewport, once | Marketing hero lines, event date/venue. NEVER legal, instructional, or must-be-copyable text; never on data |
| Marquee | Keep a section alive with a moving band | 30–60 s per loop (slow enough to read), linear; pause on hover/focus; stops under reduced motion | In view (IntersectionObserver); pauses off-screen | Logo/press bands, in-theme tickers — ONLY where the theme calls for it and the content is genuinely a band. A marquee on a task page is a defect |
| Counters | Prove magnitude with real numbers | Count 600–1000 ms, `--ease-out`, tabular numerals, once (first view; never on repeat visits to a dashboard) | First entry into viewport | Real, sourced figures only (live totals, counted items). Invented/estimated numbers: the counter is removed, not reworded (S-9). Never count record/table/module totals (leak — `09` §2) |
| SVG line-draw | Show craft or a path | Draw 800–1400 ms per path, `--ease-draw cubic-bezier(.45,.05,.35,1)`; stepped bursts (5–13% bursts, 50–180 ms breaths) where the theme's material is a fracture/mend | Section enters / scrub target | A seam, a route, a signature, a real shape — the line must trace something real. A line that draws nothing meaningful is removed |
| Image scale-in-frame | Present the image as an object arriving | Scale 1.06→1.0, 600 ms `--ease-out`, inside a fixed frame (the frame never moves) | Image enters viewport | Cards, heroes, product images. The image grows inside its frame; the layout never shifts |
| Hover / magnetic / tilt micro-interactions | Reward the pointer, confirm an action | Hover 120–240 ms; magnetic pull ≤8 px, transform-only, lerp 0.12; tilt ≤6° on cards, 200 ms `--ease-out` | Pointer over / press | Buttons, cards, links — feather-light, transform-only. NEVER where the effect delays the click it decorates; touch gets tap/scroll equivalents |
| Custom cursor | — (see §5: system cursor only) | — | — | Nowhere by default. Feather-light exception only per §5. |
| Skeleton loading | Fill a real wait | Shimmer 1200 ms loop (transform-only band); shown only for waits ≥300 ms | Data fetch / route change exceeding 300 ms | Tables, cards, dashboards, modal content. Never for instant loads (a skeleton for a <300 ms wait feels slower than the load) |
| Page transitions | Connect two views as one object | Outgoing 160 ms fade; incoming 240 ms rise 12 px + fade; total ≤400 ms; shared-element where the theme supports it | Route change | Marketing + content routes. NEVER across payment, auth, or error states (continuity there reads as trickery) |
| Reduced motion | Deliver the complete static page | All of the above: off / final states | `prefers-reduced-motion: reduce` (media query + emulation test) | Every animation, same pass (motion FE-085). Parallax/auto-play off; counters at final values; reveals present; state changes legible without movement |

### 2.1 What "heavily used in every theme and on every page" means for an existing app

The standing requirement is that every motion term is PRACTICALLY USED, heavily, in
every theme and on every page — as each theme's own full motion system in its own
style, not copy-paste. For an existing app this is enforced per page family, not per
route: every page family must carry the terms its dial allows (§4), each in the theme's
material language, each naming its job (§2 table). A page family that carries only
reveals and hovers has not met the standard — the gap is recorded per term with a
reason ("not in-theme because…", motion FE-091) or the term is implemented. The
reason must cite the theme's material or the page's job — "we didn't get to it" is not
a reason.

## 3. Scroll choreography per page family

- **Landing:** hero choreography on load (≤2000 ms total, forced complete by 4000 ms
  watchdog) → section reveals staggered per section → one scrubbed/pinned moment where
  the story earns it → progress in-theme → footer as a designed section.
- **Dashboard:** reveals once per session (or not at all); counters once; no pinning
  inside the tool; the scroll signature is the data itself ticking (live values update
  with a 200 ms fade, not a re-animation).
- **Form/checkout:** no scroll choreography beyond quiet reveals (dial 1–2); the
  scroll's job is to stay out of the way. A pinned or scrubbed checkout step is a defect.
- **Content/listing:** reveals once per session; progress spine or in-theme progress
  that holds the reader's place; no pinning on index pages.

## 4. The motion-intensity dial per page type (enforcement)

Dial table: `02-theme-decision.md` §5 (landing 3, dashboard 2, form/checkout 1–2,
content/listing 2–3, onboarding 3, empty/error 1). Enforcement rules:

- The dial is set once, in the decision record (FE-323). Changing it mid-build needs
  a written reason in the audit file.
- Task flows dial down (design-intelligence §3.2): inside a form, checkout, settings
  screen, or dashboard, restraint wins by default. A dial-3 marketing page whose
  checkout is also dial 3 has failed the dial — the checkout is dial 1–2.
- Spectacle budget: ≤1 spectacle moment per 3 viewport heights (FE-328). Two
  spectacles in one viewport cancel each other and read as noise.
- Performance floor beats ambition: if a mid-range phone cannot hold frame rate, drop
  one dial level. Never drop content, readability, or the reduced-motion variant instead.
- Dial audit (Pass 5 exit): list every technique instance per page with its dial cost;
  any page whose instances exceed its dial is reworked, not excepted.

## 5. Cursor rule (standing — BAN-FE-164 / motion FE-093)

- **System cursor only, by default.** The normal OS cursor is the expectation.
- A custom cursor is permitted ONLY when ALL hold: transform-only; driven by the page's
  single rAF loop (§1); zero perceptible input lag (pointer-to-follower delay ≤16 ms,
  measured — any perceptible trailing is a defect, not a flourish); no physics that
  trails behind the pointer; fully removed under `prefers-reduced-motion`; never larger
  than 32 px; never `cursor: none` on interactive elements (the user must always see
  the real pointer over a control).
- A heavy cursor is a defect: if a custom cursor makes the pointer hard to move, it is
  removed in Pass 5 — not lightened, not tuned, removed. The Jar of Light verdict
  (2026-11-23) is the precedent: a cursor animation that ruins the page is rebuilt
  without it.
- Feather-light effects or none: the permitted feather-light set is hover responses ON
  the elements themselves (a link's underline drawing, a card's 2 px lift) — the cursor
  itself stays the system's.
- Verification: pointer-overshoot test (5 fast moves across the nav; 0 misses) +
  `cursor: none` grep = 0 (unless the feather-light exception is recorded with its
  measurement).

## 6. The no-stranded-content rule + fallback patterns

### 6.1 Rule

Every reveal or animation must have a fallback (motion FE-096, scroll-experiences
FE-112). If the animation never runs, the content is still fully visible. A reveal
that CAN leave content invisible is a build failure regardless of how it looks when
it works (BAN-FE-047).

### 6.2 Fallback patterns (use all three, layered)

| Pattern | How it works | Numbers |
|---|---|---|
| JS-gated hidden states | The hidden start state is added BY SCRIPT, never present in shipped CSS/HTML. With JS off, content is simply there (scroll-experiences FE-101). | Hidden class added only after the observer is confirmed alive. |
| Watchdog (force-reveal timeout) | A timer per reveal that lands the content in its final visible state even if the observer/timeline/trigger never fires. | Reveal watchdog: 1500 ms after the element first enters the viewport (or 2500 ms after page load, whichever is first). Hero mend: forced complete by 1200 ms, final by 4000 ms (theme #41 precedent). Section fracture→heal: force-healed 6000–7000 ms after first entry. |
| Timed reveal / visible-by-default | Where a watchdog is impractical (CSS-only timelines), the reveal is built as an enhancement on visible content: the content renders visible, and the animation replays a change on top of readable content (motion FE-086, BAN-FE-045). | Content is readable at t=0; the animation is a re-presentation, never the first presentation. |
| Re-trigger on re-entry | A fast/smooth scroll that skips a section cannot leave it blank: the section is verified visible when it is actually in view, not only when its threshold crossing was observed. | On every loop tick, check in-view elements' visibility state; any in-view element still hidden after its watchdog is force-revealed immediately. |

### 6.3 Reduced-motion variant (per animation, same pass)

Under `prefers-reduced-motion: reduce`: parallax and auto-playing motion off;
non-essential animation removed; counters at final values; signature elements present
in final states; state changes legible without movement (motion FE-085/097, W3C C39).
The static variant is a designed page, not a broken one: it keeps the theme's identity
(final-state elements, the type, the palette) and loses only movement.

### 6.4 How to test with animations disabled

1. **JS-off load (Playwright, every route):** all text present and visible. Gate G-FE-051.
2. **Observer-stub test (Playwright, every route):** disable IntersectionObserver;
   load; anchor-jump to mid-page positions; assert every section reaches full visibility
   within its fallback window (watchdog + 500 ms tolerance). Gate G-FE-056. Zero
   stranded sections under every failure mode.
3. **Reduced-motion emulation (Playwright, every route):** scroll the full page; assert
   parallax layers static, no scroll-linked animation running, all end states legible.
   Gate G-FE-052. Zero continuing non-essential animations.
4. **Slow-device test:** CPU-throttled (4×) mid-range profile; if frame time exceeds
   24 ms twice, the choreography thins (stagger collapses to 0, locks become 300 ms
   fades — the theme #41 precedent) but the content still lands. The mend still reads;
   the choreography thins.
5. **Fast-scroll test:** fling-scroll the full page; then scroll back up slowly. No
   section blank, no element covering content at any position (S-19 sweep at both
   viewports).

## 7. Whole-app performance budget

| Budget item | Limit | What gets cut first (in order) |
|---|---|---|
| Frame budget (scroll, mid-range phone, CPU 4× throttled) | 16.7 ms/frame target; no frame >50 ms; no scroll-linked long task >50 ms (hard: >200 ms total long tasks on a full scroll = fail) | 1st: ambient loops + particle counts (halve, then off). 2nd: parallax layers (3→1→0). 3rd: one dial level (§4). NEVER cut: content, readability, reduced-motion variant, fallbacks |
| Long tasks (any interaction) | No task >50 ms on the main thread during scroll or input; total long-task time on a full-page scroll ≤200 ms | As above; plus: defer non-visible work (below-fold observers idle until near viewport) |
| rAF loops | 1 per page (recorded WebGL exception only) | Merge loops; delete per-effect timers |
| Particles / ambient counts | Declared cap per system, page-wide total ≤140 concurrent (theme #41 dust cap precedent); firefly-style fields are tens, not thousands | Cap enforced by the emitter dropping particles, never by exceeding it |
| Animation properties | transform/opacity only | Any layout-property animation is removed or excepted in writing with a measured budget |
| Font weight (motion-adjacent) | Display + body faces ≤200 KB total, `font-display: swap` | Subset faces; drop a weight before dropping a face |
| JS bundle for motion | Motion/scroll code ≤15 KB gzipped (loop + observers + fallbacks) | The loop is shared; per-element code is data (declarations), not code |

### 7.1 Cheaper mobile variants (mandatory per element)

Every element states its mobile variant in its spec (`06-signature-elements.md` §3
format): at <768 px, stagger tightens (40 ms → 24 ms), offsets halve, durations
shorten to ≈70% of desktop, particle emission halves (26/s → 16/s, cap 140 → 80),
parallax layers drop to 1 or 0, pinned sections unpin (content stacks, the pin's
story is told statically). A mobile variant is not "the same, smaller" — it is a
specified cheaper version, and the spec names what is cut.

### 7.2 Profiling discipline

Profile a full-page scroll (fast, slow, trackpad-stepped) on a mid-range
CPU-throttled profile after Pass 5 and again after Pass 7 (with all signature
elements running). Record: longest task, total long-task time, frames >50 ms, and
the cut decisions made. The profile is evidence in the audit file §8; a pass that
ships without a profile has not exited.

## 8. Cross-reference map

| This file's section | Where it is used |
|---|---|
| §1 loop | `07-frameworks.md` §3 (framework loop implementations); Pass 5–6 checklists in `03-staged-passes.md` |
| §2 terms table | `04-component-upgrades.md` (per-component motion); `06-signature-elements.md` (element choreography) |
| §4 dial | `02-theme-decision.md` §5 (dial setting); `08-case-studies.md` (per-study dials) |
| §5 cursor | Standing rule — also in `01` §3.3, `03` Pass 5 checklist |
| §6 stranded-content | Gate tests G-FE-051/052/056; `01` §5 Cat. 6 scoring |
| §7 budget | `07-frameworks.md` §6 (incremental rollout keeps the budget); `08` regression evidence |
