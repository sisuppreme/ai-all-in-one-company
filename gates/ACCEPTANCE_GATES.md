# ACCEPTANCE_GATES.md — The acceptance gate register (69 gates)

This file is the **single source** for the acceptance-gate criteria inherited from Web Craft Pro Max §12.3. Skills, playbooks, and QA documents cite gate IDs from this register; they never restate the criteria. If a criterion ever changes, it changes here, and every citation of the ID inherits the change. (This is the repo's "cite, never restate" rule — see `docs/WCPM_MAPPING.md` §3.)

**Count ruling.** This register holds exactly **69 gates**: G-DES 6, G-MOT 10, G-VIS 9, G-SCH 11, G-ENG 14, G-EXP 11, G-INT 8. The inherited source file's own §12 acceptance check says "68" — that is a known error inside the source, recorded in `docs/WCPM_MAPPING.md` §1, and it is not copied here or anywhere else in this repo. The ten skill-release QA gates (G-QA-01…G-QA-10) are **not** part of this register; they live in `gates/QA_PROTOCOL_GATES.md`, counted separately, never merged into the 69.

**How gates run** (from the source, §12.3 preamble): Every gate returns PASS, FAIL, N/A, or BLOCKED. A failed MANDATORY gate (class M) blocks delivery. At most 3 ADVISORY gates (class A) may be open at delivery. Fix-and-retest: max 3 attempts per gate; never fix by weakening the threshold. Gate IDs are stable; new gates take the next number in their family.

Criteria below are reproduced verbatim from the source register (one line each, as the source states them). Verification is owned by D8 (with D9, D13, and D6 as noted per family in `docs/WCPM_MAPPING.md` §2.3).

---

## G-DES — Design (6 gates)

| Gate | Criterion (one line) | Class |
|---|---|---|
| G-DES-01 | 0 P0 parameters AND rubric ≥90 AND every category ≥7 AND zero F1–F8 auto-fails (§3) | M |
| G-DES-02 | No attractor cluster (CLU-01–CLU-06) matches the site's overall look (≥3 of its tells) | M |
| G-DES-03 | Section order is not the canonical template order (4+ of 7 in canonical sequence fails) | M |
| G-DES-04 | No two sections share identical width, padding, and scaffolding (≥3 distinct rhythms) | M |
| G-DES-05 | 0 fabricated items (testimonials, logos, statistics, awards, people); every statistic sourced | M |
| G-DES-06 | Distinguishable from a component-library default at a 5-second glance | A |

## G-MOT — Motion (10 gates)

| Gate | Criterion (one line) | Class |
|---|---|---|
| G-MOT-01 | ≤800 ms per UI animation; ≤600 ms per entrance/transition/cascade (named exemptions only) | M |
| G-MOT-02 | Hover/press/focus/toggle feedback ≤200 ms; press feedback starts on pointer-down | M |
| G-MOT-03 | Stagger: per-item delay 40–80 ms; total ≤600 ms; ≤8 items; rest render instantly | M |
| G-MOT-04 | Every user-triggerable animation is interruptible; no input locked out by motion | M |
| G-MOT-05 | With animations disabled, 100% of content visible and every control usable | M |
| G-MOT-06 | Full reduced-motion support (CR-09): no translation/scale/rotation/parallax/autoplay/infinite under `reduce` | M |
| G-MOT-07 | ≥55 fps sustained, zero frames >33 ms, under 4× CPU (every page) and 6× CPU (heaviest page) | M |
| G-MOT-08 | Motion interruptible in both scroll directions; every scroll-triggered animation fires both ways | M |
| G-MOT-09 | 0 bare `ease`/`ease-in`/`ease-out`/`ease-in-out`/`linear` keywords for visible motion | A |
| G-MOT-10 | 3D degrades to a static fallback; cursor never traps/hides/misrepresents; scroll never hijacked | M |

## G-VIS — Visual (9 gates)

| Gate | Criterion (one line) | Class |
|---|---|---|
| G-VIS-01 | Designed type system (≥2 typefaces or 1 family with a designed ramp; display tightened per §6) | M |
| G-VIS-02 | Committed colour decision (1 dominant + ≤2 accents; no indigo-to-violet gradient hero) | M |
| G-VIS-03 | 0 banned uplift verbs or filler in prominent positions (CPY-01 list, Appendix A) | M |
| G-VIS-04 | Every page names ≥1 specific person, number, place, or outcome; 0 generic headlines | M |
| G-VIS-05 | 0 unrelated stock photos; 0 blurry/low-res assets; 0 missing social image | M |
| G-VIS-06 | 0 emoji as UI icons; icon set has a chosen stroke, size, and colour | M |
| G-VIS-07 | Primary, secondary, and tertiary actions visually distinct | M |
| G-VIS-08 | All spacing on the project's scale (0 off-scale values); ≥1 deliberate rhythm break | A |
| G-VIS-09 | 0 GL tells at P0/P1 on any 3D scene + §7.6 mechanics compliance (§7) | M |

## G-SCH — Search (11 gates)

| Gate | Criterion (one line) | Class |
|---|---|---|
| G-SCH-01 | Unique title per page (50–60 chars, never over 70); unique description 120–155 chars (ceiling 160) | M |
| G-SCH-02 | Canonical URL on every public page; target returns 200, is indexable, and does not redirect | M |
| G-SCH-03 | Every JSON-LD block parses, uses valid schema.org properties, and passes the validator | M |
| G-SCH-04 | One canonical name, URL, and stable `@id` per entity site-wide | M |
| G-SCH-05 | Core answer block (40–60 words) under the first H2 on content pages | M |
| G-SCH-06 | Every statistic carries number + named source + date inline | M |
| G-SCH-07 | `FAQPage` schema exists only where a real FAQ is visible; schema mirrors it exactly | M |
| G-SCH-08 | Every article shows a visible byline (real full name, linked author page) and a true "last updated" date | M |
| G-SCH-09 | Core content (text, headings, pricing, specs, contact) in the initial HTML without JavaScript | M |
| G-SCH-10 | Every new content page has ≥2 incoming internal links from related existing pages | A |
| G-SCH-11 | Hreflang reciprocity + alternate-URL liveness (multilingual sites only; N/A otherwise) | M |

## G-ENG — Engineering (14 gates)

| Gate | Criterion (one line) | Class |
|---|---|---|
| G-ENG-01 | Type check 0 errors; lint 0 errors; production build exit 0 | M |
| G-ENG-02 | Lab (mobile, throttled slow 4G): LCP ≤2.0 s; TBT ≤200 ms (INP proxy); CLS ≤0.05. Field p75: INP ≤150 ms | M |
| G-ENG-03 | TTFB ≤600 ms; FCP ≤1.8 s; Speed Index ≤3.0 s; TTI ≤3.5 s; main-thread work within budget | M |
| G-ENG-04 | Page weight budgets hold per page type (§9; e.g. landing ≤1,000 KB total, JS ≤170 KB) | M |
| G-ENG-05 | Single JS file ≤100 KB; single route chunk ≤50 KB; single CSS file ≤50 KB; hero/LCP image ≤150 KB | M |
| G-ENG-06 | 0 main-thread tasks over 50 ms; hydration within 500 ms on the target device | M |
| G-ENG-07 | 0 console errors on every created/changed page; 0 failed requests (≥400) from the site | M |
| G-ENG-08 | Lighthouse (mobile, throttled): Performance ≥90, Accessibility 100, Best Practices ≥90, SEO ≥90 | A |
| G-ENG-09 | Every protected route redirects anonymous visitors; every wrong-role attempt denied | M |
| G-ENG-10 | 100% of database queries parameterized; all user content escaped at render | M |
| G-ENG-11 | 0 secrets, keys, tokens, or connection strings in client code, logs, screenshots, or the report | M |
| G-ENG-12 | Lockfile committed; 0 floating versions in production; dependency audit recorded | M |
| G-ENG-13 | Every async surface has loading, empty, and error states; error messages name the next step | M |
| G-ENG-14 | 0 unused components/imports, 0 TODO/FIXME, 0 commented-out blocks in the shipped bundle | A |

## G-EXP — Experience (11 gates)

| Gate | Criterion (one line) | Class |
|---|---|---|
| G-EXP-01 | No horizontal overflow at any tested width (minimum ladder 320/768/1440; §11) | M |
| G-EXP-02 | Complete, usable design at 320 px minimum; content reflows to a 320 px equivalent | M |
| G-EXP-03 | Primary tap targets 48×48 px preferred (SHOULD), 44×44 px minimum (MUST); inputs 44 px (48 px mobile touch) | M |
| G-EXP-04 | Keyboard-only use works end to end; visible focus indicator on every interactive element | M |
| G-EXP-05 | axe-core (or equivalent) reports 0 violations at WCAG 2.2 AA on every created/changed page | M |
| G-EXP-06 | Contrast WCAG 2.2 AA: normal text ≥4.5:1; large text (≥24 px, or ≥18.66 px bold) ≥3:1 | M |
| G-EXP-07 | At least one key page tested in a second browser engine at desktop width | M |
| G-EXP-08 | Every form passes the full matrix (valid, empty, invalid, server rejection, success, no double-submit) | M |
| G-EXP-09 | Every list/search/dashboard/inbox has a designed empty state; every async surface shows loading | M |
| G-EXP-10 | Every route renders by direct URL and by in-app navigation; back/forward through ≥3 pages works | M |
| G-EXP-11 | Consent banner: accept/reject equal prominence, 1 click each, granular ≤2 clicks, no pre-ticked boxes, no wall, no nagging | M |

## G-INT — Integration (8 gates)

| Gate | Criterion (one line) | Class |
|---|---|---|
| G-INT-01 | The 2–3 flows nearest each change re-exercised; 0 new console errors, failed requests, or regressions | M |
| G-INT-02 | The build reproduces from a clean checkout (no `node_modules`, no cache, no build output) | M |
| G-INT-03 | The app starts within 60 seconds of the start command (to first successful health check) | M |
| G-INT-04 | A 3–5 line rollback plan exists for every Tier 3 change (revert, detect, verify) | M |
| G-INT-05 | Analytics events fire only after consent where required; no banned fields collected | M |
| G-INT-06 | Production deploy has explicit owner approval naming the release, the address, and the source | M |
| G-INT-07 | Expected cost change stated (or "no cost change") before the deploy | A |
| G-INT-08 | The delivery report is complete and honest (file list, evidence, one label per claim, defect log) | M |
