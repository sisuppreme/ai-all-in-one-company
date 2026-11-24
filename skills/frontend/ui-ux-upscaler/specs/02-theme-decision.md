# UI/UX Upscaler — Spec 02: Theme Decision

> Companion spec to `skills/frontend/ui-ux-upscaler/SKILL.md`. Expands Protocol
> v1.3.0 Step 3. Authority: `skills/frontend/design-intelligence/SKILL.md` §1, §6, §7;
> `skills/frontend/theme-library/EXPANSION-STANDARD.md`.
> **SCOPE: web apps ONLY.** Native mobile apps get an adaptation note only (§7),
> not full specs. All tokens, breakpoints, and motion values below are web values.
> **Architecture-leak rule (standing, top priority):** the theme system expresses
> user-facing concepts ONLY — it never names stack internals. See
> `09-architecture-leak.md`. A theme decision that surfaces a DB name, a route count,
> an endpoint, a module name, or a tech-stack label is void, however good it looks.

## 1. Inputs — collect before deciding anything

Collect all seven inputs in writing, in the audit file (§4 of `01-audit-and-scoring.md`).
A decision made with a missing input is recorded as `DECISION-INCOMPLETE` and blocks
Pass 1 (`03-staged-passes.md`).

| # | Input | How to collect it (existing app, not a blank brief) | Failure if skipped |
|---|---|---|---|
| I-1 | Brand personality (one primary) | Pick ONE: institutional / craft / playful / rebellious / serene / precise / luxurious. Evidence: the app's own copy, logo, pricing tone, support voice — quote 3 verbatim lines. Two personalities = undecided; pick the one the paying audience sees. | Theme family cannot be chosen (§1.2 of design-intelligence) |
| I-2 | Industry + what the product actually does | One sentence in user concepts only: "X helps <audience> do <job>." No stack terms (see `09-architecture-leak.md` §2 — "PostgreSQL-backed" is not an industry). | Theme metaphor chosen for the stack, not the job |
| I-3 | Audience + their job | Who, what they came to do, how often they return, what device they are on (measure: analytics device split, or state "unknown — assumed desktop-first, verify in Pass 3"). Trust level: burned-before / neutral / enthusiastic. | Dial set for the builder's taste, not the audience (FE-322) |
| I-4 | Content type per page family | Per family: conversion / story / catalogue / tool / reference. A dashboard is a tool; a pricing page is conversion; a docs index is reference. One page family, one type — mixed types get split. | Layout family wrong for the page's job |
| I-5 | Existing identity audit | Token extraction (§3): live palette (top 8 colours by rendered area), typefaces in use, spacing rhythm, existing motion (if any), logo + wordmark, imagery style. Record hex values measured from screenshots, not from the brand deck (the deck and the app often disagree — the app wins). | "Deepening" deepens a deck identity the app never had |
| I-6 | Identity strength score | Score 0–10: 0–3 generic starter (no own palette/type/motion, copy could describe a competitor); 4–6 partial identity (own colour or own type, but inconsistent — ≥3 competing blues, ≥2 body faces); 7–10 strong identity (consistent palette/type, recognisable at 390 px with the logo removed, copy in a distinct voice). Score with evidence: 3 screenshots + the token-extraction table. | Wrong branch of the decision tree (§2) |
| I-7 | Constraints | Hard constraints with numbers: performance budget (see `05-motion-system.md` §7), accessibility level (WCAG AA minimum), browser support floor, rollout constraint (per-route flag? big-bang?), content that must not move (legal copy, regulated labels). | A theme chosen that the app cannot ship |

## 2. Decision tree

```
START: I-6 identity strength + I-5 extraction complete?
  ├─ NO → stop. Complete §1 first. No theme decision without inputs (FE-321).
  └─ YES
      ├─ I-6 ≥ 7 AND identity is not generic AI slop (see test §2.1)
      │    └─ BRANCH A — DEEPEN own identity (§3)
      ├─ I-6 4–6
      │    ├─ The inconsistent parts are fixable by tokenisation alone
      │    │   (one palette, one type scale, no structural change needed)?
      │    │    ├─ YES → BRANCH A (deepen), with a recorded "repair list" (§3.5)
      │    │    └─ NO (identity conflicts with itself: e.g. playful colours +
      │    │         institutional copy, or two competing visual languages)
      │    │         → BRANCH B — ADOPT a library theme (§4)
      │    └─ (If the team cannot agree whether it is fixable: default to B.
      │         A disputed identity is not a strong identity.)
      └─ I-6 ≤ 3
           └─ BRANCH B — ADOPT a library theme (§4)
```

### 2.1 Thresholds that decide each branch — the numbers

| Threshold | Value | Why this number |
|---|---|---|
| Deepen floor | I-6 ≥ 7 | Below 7 there is not enough consistent identity to deepen; deepening a 5 produces a polished version of an incoherent brand |
| Adopt ceiling | I-6 ≤ 3 | At ≤3 the "identity" is the starter template; keeping it keeps the slop |
| Grey-zone repair test | Fixable by tokens alone = all inconsistencies are value-level (hex, size, spacing), zero are structural (layout family, section order, component set) | If a structural change is needed to make the identity coherent, the identity was never the structure — adopt |
| Logo-removal test | Identity recognisable at 390 px with logo + name removed | Pass = deepen-eligible; fail = the identity lives only in the logo, adopt |
| Copy-swap test | Hero + section copy with the company name replaced by a competitor's still reads as this company | Pass = own voice exists; fail = generic copy, adopt (and rewrite copy in Pass 2) |
| Stakeholder veto | The paying audience (I-3) would distrust the current identity | Audience veto (FE-322) overrides I-6: a 7 that the audience distrusts goes to Branch B |

### 2.2 What never decides the branch

- Builder taste ("I like dark themes"). Recorded as a bias, not a reason.
- Trend ("everyone is doing bento now"). A layout family is chosen by content type (§1.2 of design-intelligence), not fashion.
- Effort ("deepening is less work"). Deepening a weak identity costs more rework than adopting; effort is not a decision input.
- The stack. The theme never names stack internals (`09-architecture-leak.md`); the stack therefore cannot argue for a theme. "We're a Postgres shop" is not a theme input.

## 3. Branch A — Deepen an existing identity

### 3.1 Token extraction from the live app

1. Screenshot every route family at 1440 px. Sample the 8 largest rendered colour areas
   (eyedropper on screenshots, not from CSS — CSS may declare colours nothing renders).
2. Record: hex, rendered-area %, role it actually plays (ground / text / accent / error /
   success), contrast vs its real background (measured, not assumed).
3. Collapse to a token set: at most 2 grounds, 1–2 text colours, 1 accent, 1 error, 1 success.
   Every colour beyond that set is either merged into the nearest token (ΔE < 8) or
   recorded as a defect (A-series, `01-audit-and-scoring.md` §3) to be removed in Pass 1.
4. Hard rule: the extracted palette is the *starting* palette. If two extracted colours
   fail contrast at their real usage (e.g. accent text at 2.1:1), the token is fixed in
   Pass 1 — deepening never preserves an inaccessible colour. Record the fix in the audit.

### 3.2 Type-scale recovery

1. Inventory every rendered font size + face + weight on the app (DevTools computed
   styles on 3 routes per family, or a crawl script — record the method).
2. Fit one modular scale: ratio 1.25 (quiet/institutional) or 1.333 (expressive);
   body 16–18 px; display sizes only from the scale. Off-scale sizes are drift:
   each is either snapped to the nearest scale step (Δ ≤ 2 px) or recorded as a
   deliberate exception with a reason.
3. Assign registers: display / heading / body / caption / data (mono, tabular numerals
   where numbers are compared). If the app currently uses one face for everything,
   the recovery adds a second face only if the brand personality (I-1) supports it;
   otherwise the scale is carried by weight + size alone, and that is recorded as a
   deliberate restraint, not a gap.
4. Line length: prose 45–75 ch; data tables exempt (tabular, not prose).

### 3.3 Motion-system derivation from the brand's own material language

Do not import a library theme's motion. Derive motion from what the brand already is:

| Brand material (from I-5) | Motion language derived from it | Forbidden import |
|---|---|---|
| A ledger/accounting product whose core act is balancing | Draw-and-balance: lines draw, columns settle to real totals, one settle dip (see design-intelligence §7 Example A) | Bounce, elastic, particle rain |
| A repair/craft product whose core act is mending | Break-then-mend: fracture → seam draw in bursts, one-way only (theme #41 Kintsugi pattern, adapted — not copied) | Smooth dash-draw (reads as a loading bar) |
| A data/instrument product whose core act is measuring | Instrument motion: gauges fill, needles settle with damped overshoot ≤1.5%, readouts count to real values | Marquee, kinetic type on data |
| A commerce product whose core act is showing the thing | Product-in-use motion: the object assembles / drapes / opens as you scroll; nothing animates between visitor and buy button | Parallax over the buy button |
| No discernible material (identity is only a colour + logo) | Stop. This is not a deepen-eligible identity — return to §2.1; Branch B. | Inventing a material ("let's add floating orbs") |

Motion tokens derived here are named after the brand's material (`--ease-settle`,
`--dur-mend`), not after a generic library. Durations: micro-interactions 120–240 ms;
reveals 400–640 ms; choreographed sequences 900–2000 ms; nothing over 2000 ms without
a recorded reason. Easings are named cubic-bezier values, recorded in the token file.

### 3.4 Scroll-system derivation

Same rule: the scroll signature comes from the brand's own job. A study app's scroll
signature is a progress spine that holds the reader's place (design-intelligence §7
Example C). A finance app's is a ledger line that balances as totals arrive. A
catalogue's is a shelf that fills. If no scroll signature can be derived from the
job, the page ships dial 2 (quiet reveals + counters for real numbers only) and the
absence is recorded — never a generic progress bar pasted on (scroll-experiences FE-114).

### 3.5 Grey-zone repair list (I-6 4–6 → Branch A)

List every inconsistency with its fix and its pass: e.g. "3 competing blues
(#2563EB buttons, #1D4ED8 links, #3B82F6 focus rings) → single `--accent #1D4ED8`,
Pass 1; focus ring becomes accent + 2 px offset outline, Pass 4." If the repair list
exceeds 12 items, re-run §2.1: the identity is probably a 3 in a 5's clothing — adopt.

### 3.6 Deepen — exit criteria

- Token file exists; grep for hard-coded values outside it returns 0 (§3.1 step 3).
- Type scale fitted; off-scale inventory closed (snapped or excepted in writing).
- Motion language derived from brand material (§3.3 table) with tokens + durations.
- Dial set per page family (see §5), recorded with reasons.
- **Leak check:** the deepened identity names no stack internals — the token names,
  the motion names, and every label use user concepts only (`09-architecture-leak.md`
  §5). A token named `--postgres-blue` or a section titled "Our 12 pages" fails this
  exit criterion outright.

## 4. Branch B — Adopt a library theme

### 4.1 Reading the canonical spec (the only build source)

- Read `skills/frontend/theme-library/expanded/theme-NNN.md` in full — concept, palette,
  typography, layout, full motion system, signature elements, component inventory,
  copy voice, worked examples, scroll map, performance budget, build order.
- NEVER build from the one-line catalog summary, the theme's name, or a screenshot of
  its demo. The summary is an index entry, not a spec. A build whose only source is
  the summary is a failed adoption — it will be a palette-only reskin (S-10).
- Read the theme's §10 quality gate before building; the gate is the acceptance test.

### 4.2 Mapping the theme onto the app's real content

| Theme system | Mapping rule for an existing app |
|---|---|
| Palette anchors (5, per EXPANSION-STANDARD) | Map by ROLE, not by hex loyalty: the theme's ground becomes the app's ground; its accent becomes the app's single accent. If the app's brand colour conflicts with the theme's accent, the theme's accent wins for UI chrome and the brand colour survives only in the logo — record the conflict and the ruling. Usage ratios from the theme spec are preserved ±5 percentage points. |
| Typography (faces + scale) | Adopt the theme's faces and scale whole. If the app's stack cannot load the theme's display face (licensing, weight), substitute the nearest face in the same class (serif→serif) and record the substitution + the measured difference (x-height, cap height). Never keep the app's old body face "because it's already loaded" — that is S-10 by another name. |
| Motion system (every term, in the theme's language) | Adopt the theme's durations/easings/tokens verbatim; translate each technique into the app's content (see `05-motion-system.md` §2). A technique with no job on this app's content is recorded as absent-with-reason, never silently dropped and never replaced by a generic equivalent. |
| Signature elements (5–20 per app, `06-signature-elements.md`) | Do NOT transplant the theme's demo elements wholesale. Re-derive elements from the app's own content using the theme's material language (§6 of this file's companion spec). The theme's demo jar becomes the app's own vessel only if the app has something to hold. |
| Layout language | Adopt the theme's grid, spacing rhythm, section choreography. Existing pages are re-laid-out into it in Pass 3 — this is the pass where "adopt" becomes visible; a Pass 3 that changes nothing adopted nothing. |
| Copy voice | Adopt the theme's headline/label/error/empty-state voice (§9 of EXPANSION-STANDARD) for every new or rewritten string. Existing copy is rewritten only where it violates the voice or leaks architecture (`09-architecture-leak.md` §6) — do not rewrite working copy for style alone. |

### 4.3 Theme shortlist method (how the specific theme is picked)

1. From design-intelligence §1.2, take the theme FAMILY for the (personality + content
   type) row. That yields 3–6 candidate themes, never the whole 150.
2. For each candidate, run the metaphor test (§1.4 of design-intelligence): can the
   brand's own content live in this world without explanation? Score each candidate
   0–2 (0 = needs explaining, 1 = fits with a sentence, 2 = the content IS the world).
   Keep only 2s; if none scores 2, take the nearest row's family and record the deviation.
3. Tie-break by the app's hardest page: which candidate's motion system survives the
   app's densest page (dashboard table, checkout) without fighting it? The theme that
   needs the least bending on the hardest page wins.
4. Record the shortlist, the scores, the winner, and the rejected candidates with
   one-line reasons each. A decision record with no rejected alternative fails G-FE-161.

### 4.4 Adopt — exit criteria

- Canonical spec read (record theme number + file path + version/date read).
- Mapping table (§4.2) filled for palette, type, motion, layout, copy voice.
- Shortlist + scores + rejected alternatives recorded.
- Dial set per page family (§5).
- **Leak check:** the adopted theme is applied to user-facing concepts only. The theme's
  world (jars, trains, ledgers) is built from the app's user-visible content — never
  from its tables, endpoints, or modules. A signature element named after a database
  table fails this exit criterion (`09-architecture-leak.md` §4).

## 5. The motion-intensity dial per page family

One dial per page (design-intelligence §1.3, FE-323). Set it here, in the decision
record — never per section, never by taste mid-build. Changing a dial mid-build needs
a written reason in the audit file.

| Page family | Default dial | Dial range allowed | What changes the dial |
|---|---|---|---|
| Landing / marketing | 3 (Alive) | 2–4 | 4 if story-led launch; 2 if trust-first B2B with burned-before audience |
| Dashboard / tool | 2 (Quiet) | 1–2 | 1 if data-dense or repeat-visit daily tool; never above 2 (spectacle in a tool is a defect) |
| Form / checkout / settings | 1–2 | 1–2 | 1 at payment/auth steps; 2 elsewhere in the flow. Never above 2. |
| Content / listing | 2 (Quiet) | 2–3 | 3 for feature stories; 2 for indexes/listings (reveals once per session) |
| Onboarding | 3 (Alive) | 2–3 | 2 if the onboarding is long (>5 steps) — motion fatigue compounds |
| Empty / error states | 1 (Still) | 1 | Never above 1: a person hitting an error needs clarity, not choreography |

Dial deviations above the row's range need a written reason citing FE-322 (audience
trust) or a measured performance proof — "it looks better" is not a reason.

## 6. Worked reasoning examples (both paths)

### 6.1 Example D1 — Deepen: "Harbour Books" (fictional used-book marketplace)

- **Brief:** craft personality; buyers browsing second-hand books, sellers listing
  from home; content type catalogue + story; audience returns weekly, mostly mobile
  (62% Android, mid-range). Existing identity I-6 = 8: consistent warm paper palette
  (#F5EFE0 ground, #2B2118 ink, #9A3B26 lacquer-red accent), one serif display face
  (Fraunces) + humanist body, copy in a distinct voice ("Every book has had a life
  before yours"), logo-removal test passes.
- **Choices (Branch A):** deepen. Tokens extracted from live app (8 colours → 6 tokens;
  2 near-duplicate browns merged). Type scale fitted at ratio 1.333, body 17 px.
  Motion derived from the material: books are shelved, thumbed, passed on — motion
  language is *shelving*: cards slide onto the shelf (translateY 12 px → 0, 420 ms,
  `--ease-shelf cubic-bezier(.3,.7,.3,1)`), the "passed-on" count ticks like a library
  stamp. Scroll signature: a shelf that fills as the catalogue loads — the shelf IS
  the listing count. Dial: catalogue 3, story pages 3, checkout 1, seller dashboard 2.
- **Rejected alternative:** adopting theme #41 Kintsugi. Reason: the metaphor is close
  (mended things) but wrong — Harbour's story is continuity and passing-on, not breakage
  and repair; gold seams would imply the books are damaged. The brand's own material
  (shelves, stamps, marginalia) already supplies a motion language, so adoption would
  replace a working identity with a borrowed one (FE-331: adapt, never abandon — here
  there is nothing to abandon).
- **Leak check:** the deepened system names no internals. The seller dashboard's old
  label "PostgreSQL listings table: 1,204 rows" becomes "1,204 books on your shelf"
  (`09-architecture-leak.md` pair L-3). Token names are `--paper`, `--ink`,
  `--lacquer` — user/material concepts, never stack terms.

### 6.2 Example D2 — Adopt: "Fieldnote" (fictional field-survey SaaS, before: generic)

- **Brief:** precise/technical personality; environmental surveyors logging field
  readings; content type tool + reference; audience on mid-range Android in sunlight,
  gloves on, one hand free. BEFORE identity I-6 = 2: default Inter, indigo gradient
  hero, starter bento, copy swappable with any SaaS ("Streamline your workflow").
- **Choices (Branch B):** adopt. Family from §1.2: precise/technical → instrument/signal
  themes. Shortlist: #63 Sonar Room (2 — the surveyor's world IS a signal room:
  readings arrive as pings), #76 Ice Core Archive (1 — depth metaphor fits, but ice
  is not the surveyor's material), #3 Redacted Archive (1 — fits the report side,
  fights the field side). Winner: #63 Sonar Room, canonical spec
  `skills/frontend/theme-library/expanded/theme-063.md` read in full.
  Mapping: sonar palette (dark lab ground, one signal green) becomes the field app's
  ground/accent; mono-forward type with tabular numerals everywhere (readings compared
  in sun); motion: readings arrive as sonar pings (240 ms ring, `--ease-ping`), the
  survey route draws as a sweep line on the map — the sweep IS the day's route.
  Dial: field tool 2, marketing 3, settings 1.
- **Rejected alternative:** deepening the existing identity. Reason: I-6 = 2 — there is
  nothing to deepen; tokenising the indigo gradient would produce a polished starter
  (S-10). Also rejected: #76 Ice Core Archive — the depth metaphor would need
  explaining to a surveyor whose job is lateral coverage, not depth (§1.4 test fails).
- **Leak check:** the sonar theme is applied to user-visible readings only. The old
  settings line "API endpoint: /v2/readings · table: field_readings" becomes "Your
  readings sync when you're back in signal" (`09-architecture-leak.md` pair L-6).
  No signature element is named after a table, endpoint, or service.

## 7. How the decision is recorded in the audit file

In `UI-UPGRADE-AUDIT.md` §4, record exactly: inputs I-1–I-7 (one line each, with
evidence pointers); I-6 score + the two test results (logo-removal, copy-swap);
branch (A/B) + the threshold row from §2.1 that decided it; theme (Branch A: "own
identity, deepened" + material language name; Branch B: theme number + canonical spec
path + date read); dial table per page family (§5); rejected alternative + reason;
leak check result (pass/fail + the `09-architecture-leak.md` §5 checklist reference).
A §4 missing any of these is an incomplete decision record and fails G-FE-161.

## 8. Adaptation note — native mobile apps (not full specs)

This spec is web-only. If the same product also ships a native app: carry the
decision (branch, theme family, dial per page family, palette roles, type pairing)
across, but re-derive the motion system in the native platform's own idioms
(platform transitions, haptics where the platform supports them, no web scroll
choreography — native scroll is the platform's, not the theme's). Do not copy web
durations/easings into native code: re-measure them on device. The leak rule applies
unchanged on native: no DB names, table names, endpoints, or module names in any
user-facing native surface either (`09-architecture-leak.md` §3.5).

## 9. Cross-reference map

| This file's section | Where it is used |
|---|---|
| §1 inputs, §2 tree | SKILL.md Step 3; audit file §4 |
| §3 deepen | `03-staged-passes.md` Passes 1–2, 5–6 (derived motion) |
| §4 adopt | `03-staged-passes.md` Passes 1–7 (mapping table is the build source) |
| §5 dial table | `05-motion-system.md` §4 (dial enforcement); `08-case-studies.md` (per-study dials) |
| §6 examples | Model for the decision records in `08-case-studies.md` |
| §8 native note | Scope boundary — no further native specs exist in this skill |
