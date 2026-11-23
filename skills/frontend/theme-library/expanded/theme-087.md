# Theme 087 — Calibration Standard No. 9 (50x Expansion)

A national metrology lab's quiet masterpiece, expanded to the full 50x standard. Identity preserved exactly from the original entry: the site is built to the discipline of the standard metre — everything measured, everything traceable, whitespace itself specified in millimetres. Minimalism with paperwork. The nine original signature elements are deepened, never redesigned (§6.1–§6.9); §6.10–§6.18 are the page-family elements the original layout implies. Every figure printed anywhere in this spec traces to the one Standard Record (§6.17).

## 1. Concept & world

Calibration Standard No. 9 is the website as a measuring instrument that has been left open on the bench. A national metrology laboratory — the people who keep the metre a metre — does not decorate its documents; it *issues* them. Every page in this theme is therefore treated as a certificate that happens to be readable on a screen: severe lab-white space, etched crosshair marks where a pencil would tick, certificate borders where a ruling pen would rule, and exactly one object in the whole building allowed to shine — the platinum-iridium standard bar, because in the real bureau there is exactly one object like it and it lives in a vault.

The mood is quiet authority. Nothing on the page asks for attention; things are simply *correct*, and correctness at this level of care reads as luxury. The visitor should feel the specific pleasure of a well-kept instrument: the dead-stop click of a counter landing on its certified value, a jaw closing to exactly the width of the thing it measures, a footer that signs and dates itself. The theme's drama is procedural — measurement performed in public, with the paperwork to prove it.

**The theme's one law: nothing is shown that was not measured, and nothing is measured that is not shown.** Every number, length, count and claim on the page is either (a) a measurement taken on the page itself — the hero line really is divided into 1,000 graduations, the vernier really reads scroll depth, the hover really reports an element's true rendered size — or (b) a figure declared once in the Standard Record (§6.17) and printed identically everywhere it appears. A figure that cannot be traced to (a) or (b) does not print. This law is the theme's immune system: it is what makes the minimalism honest instead of merely empty, and §10's quality gate audits it mechanically.

**Best-fit sites and audiences.** National and regional metrology institutes and standards bodies; calibration laboratories selling traceable measurement as a service; precision-instrument manufacturers (coordinate measuring machines, gauge blocks, laser interferometers, analytical balances); high-end manufacturing with a quality story (aerospace machining, watchmaking, optics); accreditation and certification bodies; scientific publishers of reference data. The audience is engineers, quality managers, procurement officers and the scientifically literate public — readers who check figures for a living and trust a page that shows its working.

**When NOT to use it.** Never for anything whose appeal is warmth, speed or appetite: restaurants, fashion, entertainment, children's products, consumer apps chasing delight. Never where the client cannot supply real figures — this theme has nowhere to hide invented numbers, and a build that fakes its record (§9) collapses into the exact slop it exists to refuse. Never for a content-heavy news or magazine layout: the whitespace discipline starves dense text. And never as a "clean corporate" shortcut — the severity is earned by procedure, and a team unwilling to run the procedure (§15) should choose another theme.

## 2. Palette

Five anchors, inherited unchanged. Seven derived tokens, each a measured mixture or a functional shade of an anchor — no new hues enter the building.

| Token | Hex | Role | Usage ratio | Pairing & contrast (measured for this expansion) |
|---|---|---|---|---|
| `--lab` | `#F5F4F0` | Lab white — the ground, the certificate paper | ~78% of pixels | Ground for `--etch` (15.34:1), `--trace` (8.27:1), `--seal` (6.37:1) |
| `--etch` | `#1D1D1B` | Etch black — all body text, etched lines, graduations | ~12% | On `--lab` 15.34:1 — the only colour body text may be set in |
| `--plat` | `#6E7276` | Platinum-iridium grey — hairlines, secondary marks, the bar's base tone | ~6% | On `--lab` 4.41:1 — **below AA for text**: marks, rules and large display only, never body or caption text |
| `--trace` | `#2E4A6B` | Traceability blue — links, the chain of traceability, interactive affordances | ~3% | On `--lab` 8.27:1; `--lab` on `--trace` 8.27:1 (filled buttons) |
| `--seal` | `#A62B25` | Seal red — the traceability seal and the certificate seal. Nothing else. Ever. | <0.5% | On `--lab` 6.37:1 — legible, but rationed by census (§10), not by contrast |
| `--plat-deep` | `#565A5E` | Derived — caption and certificate small print (the text-safe shade of platinum) | ~2% | On `--lab` 6.32:1 — the only grey text may be set in |
| `--lab-deep` | `#EBE9E2` | Derived — recessed panels, the unetched plate of the skeleton (§6.16), table row alternation | ~4% | `--etch` on it 13.90:1; `--trace` on it 7.49:1 |
| `--plat-pale` | `#DDDCD6` | Derived — certificate border fills, disabled fields, the jaw's body | fills only | 1.25:1 against `--lab` — a fill, never a text ground for anything but `--etch` (12.29:1) |
| `--hairline` | `#1D1D1B` at 18% | Derived — etched hairlines over `--lab` (borders, rules, crosshair arms) | lines only | Decorative-thin by design; any line carrying meaning is drawn in solid `--etch` |
| `--sheen-hi` | `#C7CACC` | Derived — the single highlight stop of the brushed-platinum sheen (§6.8) | one element | Exists only inside §6.8's gradient; forbidden in any other rule |
| `--sheen-mid` | `#9BA0A3` | Derived — the sheen's mid stop | one element | As above |
| `--sheen-lo` | `#7E8387` | Derived — the sheen's low stop | one element | As above |

**Pairing rules.** Text is `--etch` on `--lab` or `--lab-deep`, or `--plat-deep` for small print, or `--trace` for links. `--plat` never sets text below 24px and never sets body text at any size (4.41:1 is a measured fact, not a style preference). Forbidden pairings, measured: `--trace` on `--etch` (1.86:1), `--seal` on `--etch` (2.41:1), `--plat` on `--etch` (3.48:1) — the theme has no dark surfaces for these to occur on, and the gate (§10) greps for them anyway. `--seal` appears only where §6.7 or §6.9 licenses it; a red hover state, a red error banner, a red sale badge are all census violations.

**Dark-mode behaviour.** There is none, by ruling. The artefact is a printed certificate; certificates are not issued in negative. The theme does not ship a `prefers-color-scheme: dark` variant and does not invert: under an OS dark setting the page remains lab white, exactly as a PDF of a calibration certificate does. This is stated in the build (§15, step 3) so no well-meaning implementer "fixes" it. The one concession to environment: forced-colors mode is honoured structurally — borders, focus outlines and the seal's *position* survive as system colours, because a certificate under assistive rendering must still read as a certificate.

## 3. Typography

Two families, inherited: **Inter** for display and body, **IBM Plex Mono** for certificates, measurements and every numeral that carries a unit. The discipline is in the weights: **Inter ships in exactly two weights — 400 and 600.** No 700, no 800, no black display weight; a bureau does not shout, and emphasis is achieved by size and space, never by a heavier cut. IBM Plex Mono ships in 400 only.

| Role | Font | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Display (hero) | Inter 600 | 64px / 1.02 | −0.02em | Set to the measure of the hero line (§6.1); max two lines |
| Heading 2 | Inter 600 | 40px / 1.10 | −0.015em | Section titles; always preceded by its section number in mono |
| Heading 3 | Inter 600 | 28px / 1.18 | −0.01em | Sub-sections, card titles |
| Body | Inter 400 | 17px / 1.65 | 0 | Measure 62–70ch; the page's default voice |
| Lead | Inter 400 | 21px / 1.55 | 0 | First paragraph of a section only |
| Caption / small print | Inter 400, `--plat-deep` | 13px / 1.50 | 0 | Certificate small print, figure notes |
| Data / measurement | IBM Plex Mono 400 | 15px / 1.45 | 0 | Every value with a unit; tabular by font, not by CSS |
| Label / eyebrow | IBM Plex Mono 400, uppercase | 12px / 1.40 | +0.08em | The only letterspaced text on the page |
| Certificate text | IBM Plex Mono 400 | 13px / 1.60 | 0 | Footer certificate (§6.9) and form confirmations (§6.13) |

**Type laws.** (1) **Two weights only** — a build that loads a third Inter weight fails the gate; faux-bold is a firing offence. (2) **Every figure carries its unit**, set in the same mono run, separated by a thin space: `1 000 mm`, `20.0 °C`, `±0.5 px`. Thousands take a thin space, never a comma — the bureau follows SI brochure style. (3) **Numerals in prose are mono.** A sentence that mentions 4 812 instruments sets the number in IBM Plex Mono inline; numbers are data wherever they occur. (4) **No italics.** Inter's italic is not loaded; emphasis in prose is a mono run or a heading. A certificate does not lean. (5) **Uncertainty is typography, not decoration**: the `±` sign and its value are set whenever a tolerance is claimed, in the same size as the value — never shrunk, never greyed into `--plat`. (6) Display tracking is negative and fixed (−0.02em); the only positive tracking on the page is the mono label's +0.08em.

## 4. Layout language

The page is laid out **at scale**. At the reference viewport (≥1200px), the theme declares **1px = 1mm**: the hero metre line (§6.1) is 1 000px long because it is one metre long, the content measure is 1 000px because the certificate is one metre wide, and the margins are specified — and printed in the margin by §6.6's readout culture — in millimetres. This is not a metaphor the copy makes; it is a conversion the CSS enforces and the record (§6.17) declares, so any builder can check any length on the page against the page's own ruler.

**Grid.** A 12-column grid inside the 1 000px measure, 24px gutters, baseline unit 4px. All spacing tokens are millimetre values at the reference scale: `--sp-4`, `--sp-8`, `--sp-12`, `--sp-24`, `--sp-40`, `--sp-64`, `--sp-96`, `--sp-160` (px at reference, mm by declaration). Section separation is `--sp-160` — 160mm of specified emptiness, the theme's signature luxury. Nothing in the theme is spaced by eye; every gap is a token, and every token is a number of millimetres the record can be audited against.

**Section choreography.** Sections are *benches*: each opens with a mono label (`SECTION 04 — TOLERANCES`) and an etched crosshair at its top-left registration corner, is ruled top and bottom by certificate hairlines, and closes with its figures stated. Density is low and even — a section that needs more room takes more vertical millimetres, never smaller type or tighter leading. Whitespace is the primary material and is treated as *specified*, not leftover: the empty 160mm between sections is as designed as any element, and §9 names filling it as a failure mode.

**Fixed furniture.** The vernier scale (§6.2) rules the right page edge for the full document height. The margin column (the outer 160px at reference) is the page's notebook: crosshair readouts (§6.6), the self-verifying crosshair (§6.4) and re-verification notes live there, never in the text column. Certificate borders — a double hairline frame, outer `--etch` 1px, inner `--hairline` at 4px inset — enclose exactly three things on any page: the hero, the conversion form (§6.13), and the footer certificate (§6.9). A fourth bordered block is a gate failure.

**Scale at other sizes.** 768–1199px: the declared scale is 0.75px = 1mm; the measure is fluid to 92vw and the vernier converts (§6.2). <768px: the scale is 0.5px = 1mm, declared *out of the vernier's certified range* — the instrument says so rather than pretend (§6.2). The metre line never exceeds the viewport; at <768px it is drawn at the available width and its printed length is the measured width in millimetres at the declared scale — the line is re-measured, not cropped (§6.1).

## 5. Full motion system

Motion in a metrology lab is the motion of instruments: jaws closing, lines being etched, needles settling **dead**. The theme's absolute rule, from which every spec below follows: **no easing may overshoot.** No spring, no bounce, no elastic, no anticipation — a value that passes its target and comes back is, in this world, a measurement error performed for entertainment. Every curve below is monotonic; §10 audits the cubic-beziers by their control points.

**Named easings** (the only five in the theme):

| Token | Curve | Used for |
|---|---|---|
| `--ease-etch` | `cubic-bezier(0.4, 0, 0.2, 1)` | Lines drawing themselves — graduations, chain links, rules |
| `--ease-settle` | `cubic-bezier(0.22, 1, 0.36, 1)` | Dead-stop landings — counters' final approach, headline setting to measure |
| `--ease-gauge` | `linear` | Anything scrubbed to scroll — the vernier jaw, the pinned metre cascade |
| `--ease-stamp` | `cubic-bezier(0.7, 0, 0.2, 1)` | The seal press (§6.7) — fast in, hard stop, no rebound |
| `--ease-verify` | `cubic-bezier(0.85, 0, 0.15, 1)` | The crosshair's correction snap (§6.4) — a tiny, exact adjustment |

**The shared loop.** All scrubbed values — vernier jaw position, pinned-metre cascade progress, chain draw progress — are driven by **one** `requestAnimationFrame` loop lerping toward their scroll targets at factor **0.16**: stiff and prompt, like a good instrument, landing without oscillation because the lerp is critically damped by construction. No element runs its own scroll listener or its own loop. Time-based animation (the hero division, counters, the crosshair's drift) runs on the same loop's clock. If the loop is not running — JS off, loop error — every element is already in its final state in the DOM (see each element's fallback).

**Every motion term, translated or refused:**
- *Scroll-triggered reveals* — the measuring wipe (§6.3) and etch-in section rules; content is never hidden awaiting them (pre-states are JS-armed only).
- *Scroll-driven / scrubbed* — the vernier jaw (§6.2), the pinned spec metre (§6.11), the traceability chain draw (§6.14).
- *Parallax* — **refused.** Parallax is deliberate misregistration between layers; registration is this theme's religion. Depth is expressed by etched shading (§6.15), never by layers travelling at different rates. The single exception that is not one: the margin crosshair (§6.4) corrects its own half-pixel drift — motion *toward* registration.
- *Pinned sections* — the spec section's metre (§6.11) pins for exactly its cascade; the pin distance is declared in the record.
- *Masked line reveals* — headline lines rise from behind an etched rule (§6.1), the mask being the rule itself.
- *Blur-to-sharp* — **refused.** A blurred value is an unreadable value; the lab does not publish out-of-focus figures. Images arrive by measurement (§6.3), text by etching.
- *Kinetic typography* — refused except one licensed act: the hero headline *sets to measure* (§6.1) — its width becomes the line's width. Type otherwise never moves.
- *Marquee* — **refused.** Nothing in a standards bureau scrolls sideways under its own power. The only horizontally travelling object on the page is the vernier jaw, and the visitor's scroll moves it.
- *Counters* — dead-stop only (§6.5); the last digit lands, it does not settle, bounce or roll past.
- *Progress indicator* — the vernier (§6.2): progress as a reading, in millimetres and section-tenths, not a bar.
- *SVG line-draw* — the chain of traceability (§6.14) and certificate border alignment (§6.9), `--ease-etch` or scrubbed `--ease-gauge`.
- *Image scale-in-frame* — replaced by the caliper wipe (§6.3): images are admitted at their measured width, at scale 1.000 — a measured object is not zoomed.
- *Hover / magnetic / tilt* — hover is measurement (§6.6). Magnetic pull is refused (a pointer is not a magnet near a standard). Tilt is rationed to the original's specified **0.5°** on framed plates (§6.15) — a stated angle, applied by transform, identical for every frame.
- *Custom cursor* — **refused**, standing rule. The crosshair is an instrument printed on the page, never a pointer replacement.
- *Skeleton loading* — the unetched plate (§6.16): a blank certificate plate with border and labels, filled by etching.
- *Page transitions* — the re-verification (§6.16): outgoing page's certificate border aligns with the incoming page's before the swap.
- *Ambient loops* — exactly one licensed: the self-verifying crosshair (§6.4), on a ~10s cycle. The platinum sheen (§6.8) fires once per page, ever, and is not a loop.
- *Reduced motion* — the standard at rest: every value printed with its uncertainty, every line fully drawn, the crosshair still, the jaw printed at its reading (§5 of each element; global variant in §10's gate).

## 6. Signature elements

The nine original signature elements (§6.1–§6.9) are deepened, never redesigned. §6.10–§6.18 are the page-family elements the original layout implies — the certificate masthead, the pinned spec table, the instrument cards, the calibration-request form, the chain of traceability, the etched plates, the re-verification transition, the Standard Record itself, and the out-of-tolerance 404. All eighteen draw every figure from the one Standard Record (§6.17). Where a number appears in an element's spec — a count, a length, a certificate number — it is the number that element ships with.

### 6.1 The dividing metre (hero)

**What & why.** On load, one horizontal line draws across the hero and then *divides*: 10 graduations etch in, then 100, then 1,000, cascading outward from the centre in a precise stagger, until the hero contains a complete metre rule at the page's declared scale. The headline then sets to exactly the line's measure — its width becomes the line's width. This is the theme's thesis performed once, at the top: the hero does not picture the unit, it *enacts* the definition of the unit, and the page's ruler and the page's subject are the same object. It merges with content because the line is immediately put to work — it is the same metre the vernier (§6.2) reads against, the spec section (§6.11) pins, and the footer certificate (§6.9) cites.

**Structure.** An inline SVG spanning the content measure (1 000px at reference), height 46px: one baseline path, and three `<g>` layers of graduation ticks — 10 major (24px tall), 100 medium (14px), 1 000 minor (7px) — generated at build time as real SVG line elements (never a background image, so the graduations are inspectable and countable). Tick lengths encode value: this is a ruler, not a texture. Beneath the SVG, the printed caption in mono: `1 METRE · 1 000 GRADUATIONS · SCALE 1 PX = 1 MM`. The headline is a DOM `<h1>` whose container is exactly the SVG's width. The fully divided metre is the SVG's static state in the HTML; JavaScript arms the un-divided pre-state (ticks at `stroke-dashoffset` hidden / opacity 0 via a JS-added class) only after first paint proves the loop runs.

**Motion spec.** Total sequence 2 200ms. Phase 1 (0–800ms): the baseline draws left-to-right, `--ease-etch`. Phase 2 (700–1 300ms): the 10 major graduations etch in a centre-out stagger, 30ms apart, each a 120ms `--ease-etch` draw. Phase 3 (1 100–1 700ms): the 100 medium ticks, centre-out, 6ms stagger, 90ms each. Phase 4 (1 500–2 100ms): the 1 000 minor ticks, centre-out, 1.2ms stagger (a visible cascade wave, ~600ms across), 60ms each. Phase 5 (1 900–2 200ms): the headline's two lines rise from behind the etched rule that underlines the metre (masked reveal, translateY 100%→0, `--ease-settle`, 60ms stagger) and the caption prints. Trigger: first paint + 200ms, once per page load; on repeat views within a session it replays in a 900ms short form (phases compressed proportionally) because a returning visitor is re-verifying, not discovering.

**Choreography timeline.** 0ms baseline starts · 800ms baseline complete · 700ms first major tick (centre) · 1 300ms majors done · 1 100ms first medium tick · 1 700ms mediums done · 1 500ms first minor tick · 2 100ms minors done — the metre is whole · 1 900ms headline line 1 rises · 1 960ms line 2 · 2 200ms caption printed; the crosshair (§6.4) arms.

**State matrix.** *Rest (pre-trigger / no-JS):* the complete divided metre and headline, printed — the hero is finished in this state. *Dividing:* as above; the headline is present in the DOM and readable by assistive tech throughout (only its visual mask is armed). *Divided:* static; the metre becomes the hero's furniture and the reference for §6.6 hover readings in the hero. *Scrolled-past:* never replays, never un-divides — a metre does not forget its graduations. *Disabled (SVG unsupported — effectively never):* the caption and a 1px CSS rule carry the hero; the printed caption still states the count. *Touch:* identical — the sequence is time-triggered on every device.

**Content-merge.** The line's length is the content measure; the headline is set to it; the caption states its count; §6.17's record declares its 1 000 graduations as figure R1, and §6.11's pinned metre is this same line's sibling in the spec section. Remove the animation and nothing is lost; remove the line and the hero has no width, no title measure and no subject — they are one element.

**Breakpoints.** ≥1200px: line 1 000px, all 1 000 minor ticks rendered. 768–1199px: line = 92vw at the declared 0.75px = 1mm scale (printed length recomputed and captioned, e.g. `920 MM AT 0.75 SCALE` — the caption is generated from the measured width, never hard-coded); minor ticks render every 2nd graduation below 900px line width to avoid moiré, with the caption noting `MINOR GRADUATIONS SHOWN EVERY 2 MM`. <768px: line = 92vw at 0.5 scale; majors and mediums only; caption states the shown count honestly. The division cascade timings are unchanged; tick *counts shown* change, and the caption always prints the truth about which.

**Edge cases & failure modes.** Slow device: if the first 30 frames of phase 4 average >24ms, the minor cascade switches from stagger to a two-step etch (left half, right half, 200ms each) — the metre still completes on schedule. Tab hidden mid-division: the loop sleeps; on return, if elapsed >3 000ms the metre snaps to fully divided (watchdog state) rather than resuming a stale cascade. Headline longer than two lines: the copy rules (§12) cap it; a third line would break the measure, so the build lints headline length at 64 characters. Viewport resized mid-sequence: the SVG is viewBox-scaled, ticks do not re-flow; the sequence continues against the viewBox, not the pixels.

**Fallback & watchdog.** The divided metre is the static DOM state; JS arms the pre-state only after the loop's first frame. **Watchdog: 3 000ms** from trigger — if division is incomplete (loop error, jank storm), all ticks snap to drawn and the headline unmasks. With JS disabled the hero is simply complete. No figure in the hero waits on the animation: the caption's numbers are printed in the HTML.

**Reduced motion.** No drawing, no cascade: the complete metre, headline and caption are printed at rest. The hero is a photograph of a ruler — which is to say, a ruler.

**Accessibility.** The SVG is `aria-hidden="true"`; its meaning is carried by the caption as real text (`1 METRE · 1 000 GRADUATIONS`). The `<h1>` is a normal heading, first in focus and reading order; the mask never removes it from the accessibility tree. Contrast: headline `--etch` on `--lab` 15.34:1; caption `--plat-deep` on `--lab` 6.32:1.

**Performance & mobile variant.** 1 110 SVG line elements ≈ 38KB uncompressed markup, ~9KB gzipped; the draw is `stroke-dashoffset` on composited layers — no layout, no paint of text. Frame cost during cascade ≤0.8ms. Mobile: fewer ticks (above), same budget; the SVG is inline (no request).

**Tokens.** `--lab`, `--etch`, `--hairline`, `--plat-deep`, `--ease-etch`, `--ease-settle`, `--metre-length: 1000` (record R1), `--divide-dur: 2200ms`, `--divide-short: 900ms`.

### 6.2 Vernier progress jaw (page-edge scale)

**What & why.** A vernier scale is fixed down the right page edge for the document's full height; its sliding jaw tracks scroll, and a mono readout beside the jaw states the visitor's depth two ways: in millimetres of the reference build and in sections-and-tenths (`DEPTH 4 096 MM · SECTION 6.4`). This is the theme's progress indicator, and it merges with content because it is not a metaphor for progress — it is a *reading*: the page declares its own reference length in the record (§6.17, R2: 6 400mm, 9 sections), the jaw's position is the scroll fraction of that length, and both printed numbers derive from the single fraction by arithmetic a visitor can check. Progress bars lie by design (they fill); a vernier reports.

**Structure.** A fixed right-edge rail (28px wide at reference): an SVG main scale divided into 9 section bands, each subdivided into 10 tenths — 90 minor divisions over the rail's full height — plus a jaw: a 34px-tall platinum-pale block with an etched index line and a vernier sub-scale of 10 divisions compressed into 9 tenths' length (a real vernier: the jaw's zero and the coincident line are how the tenth is read). The readout is a mono `<div>` riding with the jaw, right-aligned into the margin. The rail's bands are labelled with section numbers 1–9. All scale geometry is generated from the record's two numbers (9 sections, 6 400mm reference length) at build time.

**Motion spec.** The jaw's target is the scroll fraction `f = scrollY / (docHeight − viewportHeight)`, clamped 0–1. The shared loop (§5) lerps the jaw's rendered position toward the target at 0.16 — the reading glides like a real jaw pushed along a scale and lands dead when scrolling stops; there is no separate "settle" animation because the lerp *is* the settle. The readout text updates when the displayed value changes: mm = `round(f × 6 400)`, section = `floor(f × 9) + 1` with tenths = `round((f × 9 mod 1) × 10)`. Text updates are throttled to value changes only (no per-frame DOM text churn). At `f = 0` the jaw sits at the rail head and the readout prints `DEPTH 0 MM · SECTION 1.0`.

**Choreography timeline.** Continuous and scrubbed — no beats. On load: jaw at the restored scroll position (scroll restoration is honoured; the jaw never animates from zero to a restored depth — it *starts* at the reading). On scroll start: jaw moves within one frame. On scroll stop: jaw lands within ~180ms (lerp tail) and the readout's final value prints.

**State matrix.** *Rest:* jaw at current reading, readout printed. *Scrolling:* jaw lerps; readout updates on change. *Scrolled to foot:* jaw at rail foot, readout `DEPTH 6 400 MM · SECTION 9.9` → at exactly f = 1, `SECTION 9.9` caps (there is no section 10.0; the last tenth is the footer's). *Disabled (no JS):* the rail and its 9 numbered bands print statically without a jaw — the scale remains as the page's section map, which is true without the reading. *Touch:* identical; the jaw never intercepts touch (the rail is `pointer-events: none`).

**Content-merge.** The bands are the page's real sections — band *n* is section *n*, and the section's own header (§4) prints the same number. The readout's mm figure is the record's declared reference length made positional. A visitor who distrusts the jaw can count sections; the instrument invites the check.

**Breakpoints.** ≥1200px: full rail, mm + section readout. 768–1199px: rail 24px; readout in mm at the declared 0.75 scale (the fraction arithmetic is unchanged — the record's 6 400mm is a property of the build, not the viewport) and section-tenths. <768px: the rail leaves the edge and becomes a 3px bottom rule with the jaw as a 18px block; the readout prints section-tenths only, plus the printed note `MM READOUT OUT OF CERTIFIED RANGE BELOW 768 PX` in the footer's certificate (§6.9) — an instrument out of its range says so (§4), it does not fake precision.

**Edge cases & failure modes.** Document shorter than expected (a sparse page type): the record's reference length is per-page-type (§7); a page built without declaring its length ships the rail with section bands only and no mm readout — declared absence, not a wrong number. Content loads late and document height grows (images, fonts): `f` is recomputed from live heights every frame, so the jaw's *fraction* stays true even as the document changes under it; the mm figure is of the reference build and does not drift. Scrolling back up: the jaw retraces exactly — the lerp is symmetric, there is no "visited" state. Browser find-in-page jumps: the jaw lands on the new fraction within the lerp tail; no special case.

**Fallback & watchdog.** The rail is static SVG in the DOM; only the jaw's transform and the readout text are JS-driven. **Watchdog: 1 200ms** — if the loop has not updated the jaw within 1 200ms of a scroll event (loop death), the jaw snaps to the true fraction and the readout prints the true values; a dead instrument must read correctly or not at all, and this one reads correctly. With JS disabled: static rail, no jaw, no readout — nothing false is printed.

**Reduced motion.** The jaw does not lerp: it cuts to the current fraction on scroll (position updates are information, not animation, and are preserved), the readout updates identically. No glide, no tail.

**Accessibility.** The whole rail is `aria-hidden="true"` and excluded from focus — it duplicates information (position in page) that the document structure already gives assistive tech, and announcing depths would be noise. It never overlaps content (reserved edge margin at ≥768px; bottom rule at <768px sits below the footer safe area). Readout contrast: `--plat-deep` on `--lab` 6.32:1 for the ≥768px margin printing.

**Performance & mobile variant.** One transform on one element per frame from the shared loop; text writes only on value change (≤ ~12/sec at full-speed scroll). Cost ≤0.1ms/frame. Mobile variant is the bottom-rule form above; the SVG bands are not rendered <768px (the rule is a div), saving the 90-division SVG entirely.

**Tokens.** `--plat-pale`, `--etch`, `--hairline`, `--plat-deep`, `--ease-gauge`, `--lerp: 0.16`, `--page-length-mm: 6400` (record R2), `--page-sections: 9` (record R2), `--rail-w: 28px`.

### 6.3 Caliper measuring wipe (image reveal)

**What & why.** Every image on the page is admitted the way an object is admitted to a lab: it is measured first. As an image scrolls into view, a caliper jaw closes from the frame's right edge to the image's true rendered width; the readout in the margin prints that width (`W 640 PX · 160.0 MM`); only then does the image appear inside its etched frame, at exactly the width the jaw stopped at. The reveal *is* the procedure, and it merges with content because the measurement is real — the jaw stops at the element's measured `offsetWidth`, and the printed figure is that measurement, not a caption written in advance. An image that cannot be measured is not shown with a fake number; the fallback prints no figure at all.

**Structure.** Each measured image is a `<figure class="caliper">` containing: the `<img>` at its final size from first paint (never scaled by the effect), an etched frame (double hairline, §4), an SVG caliper overlay — a fixed jaw at the left frame edge and a sliding jaw (a platinum-pale rule with an etched index line) that translates across the frame — and a mono readout line under the frame, pre-printed with the image's *declared* dimensions from its `width`/`height` attributes as `DECLARED 640 × 400 PX` (the paperwork) which the live measurement then confirms or corrects.

**Motion spec.** Trigger: the figure's top crosses 82% of the viewport height. The sliding jaw starts at the frame's right edge +8px and closes leftward-to-target — calipers close *onto* the object: jaw target = the image's right edge, i.e. jaw travel = frame width − image width… for the standard full-measure figure (image fills its frame), the jaw instead starts at the *left* jaw and sweeps to the right edge, reading the width as it goes; the readout counts in step with the jaw's position (mm at the declared scale, one decimal). Duration: 620ms, `--ease-settle` — the jaw decelerates onto the object and stops dead; it never passes the edge and returns (overshoot is a mis-measurement, §5). At the stop: a 90ms hold, the readout prints final `MEASURED 640 PX · 160.0 MM ✓ WITHIN DECLARED` (or the discrepancy, below), the overlay jaw fades to 18% (it stays, faintly, as the frame's right rule — the instrument remains on the bench), and the image — which was present but veiled by a `--lab-deep` plate at full opacity — is unveiled by the plate sliding away with the jaw's last 120ms. Total felt duration ~740ms.

**Choreography timeline.** t=0 figure crosses 82% line · 0–620ms jaw sweeps, readout counting · 620ms jaw lands dead on the right edge · 620–710ms hold, verdict prints · 600–740ms veil plate exits with the jaw's tail, image revealed at scale 1.000 · 740ms figure at rest, jaw ghosted as frame rule.

**State matrix.** *Rest (pre-trigger):* veiled plate with the declared dimensions printed — a covered object on the bench, fully captioned; the `<img>` is loaded and in the DOM (alt text available). *Measuring:* as above; the figure is not interactive. *Measured:* image visible, measured readout printed beneath the declared line, jaw ghosted. *Scrolled-past:* never re-measures on the same page view; scrolling back up shows the finished figure. *Re-measure:* a viewport resize that changes the image's rendered width by >2px re-arms a single re-measure (400ms short form) and updates the readout — instruments are re-checked when conditions change, and the readout notes `RE-MEASURED AFTER RESIZE`. *Disabled (no JS):* no veil, no jaw — the image prints with its declared dimensions only. *Touch:* identical, scroll-triggered.

**Content-merge.** The number the visitor reads is the number the browser measured; the declared-vs-measured pair is the lab's whole epistemology in one figure caption. On the worked example (§8) the discrepancy case is shown deliberately: a plate declared 640px that renders at 638px (a 2px border the declarant forgot) prints `MEASURED 638 PX — DECLARED 640 PX · Δ2 PX NOTED` and shows the image anyway — the lab reports discrepancies, it does not hide objects.

**Breakpoints.** ≥1200px: full sweep + counting readout. 768–1199px: sweep 480ms, readout prints final values only (no counting — a smaller bench, a shorter procedure). <768px: no sweep; the veil lifts in a 160ms fade as the figure enters, readout prints measured values statically. The measurement still happens (it is arithmetic, not animation); only the theatre is rationed.

**Edge cases & failure modes.** Image fails to load: the jaw still measures the frame (the frame has the declared size), the readout prints `OBJECT NOT RECEIVED — FRAME MEASURED 640 PX`, and the figure shows the etched empty frame with the alt text as its caption — a missing object is a recorded event, not a broken-image icon. Image wider than its frame (authoring error): the jaw stops at the frame edge and the readout prints the overflow as a negative tolerance — visible, honest, and a build bug the gate (§10) catches by screenshot audit. Very tall images: the trigger is the figure's top; the sweep runs regardless of how much of the image is on screen. Lazy-loaded images below the fold: `loading="lazy"` is forbidden on measured figures — the veil is the loading state, and an unloaded object cannot be measured; images are eager with `fetchpriority` by distance.

**Fallback & watchdog.** **Watchdog: 1 200ms** from trigger — if the sweep has not completed (loop stall, image decode hang), the veil lifts, the jaw snaps to the measured edge, and the readout prints the measured values with the note `READING TAKEN WITHOUT SWEEP`. No figure may wait on its jaw: content first, ceremony second, always.

**Reduced motion.** No sweep, no veil: the image is present, the jaw rests ghosted at the measured edge, the readout prints declared and measured values statically. The measurement (the content) survives intact; only the motion is stood down.

**Accessibility.** The `<img>` carries real alt text; the veil is a decorative overlay (`aria-hidden`) that never removes the image from the accessibility tree. The readout is plain text under the figure. Focus order is untouched — figures are not focusable unless they contain a link, and the sweep never moves focus. The measured/declared text is `--plat-deep` on `--lab` (6.32:1); the verdict line is `--etch` (15.34:1).

**Performance & mobile variant.** One transform (jaw) + one text update per figure, on the shared loop; figures measure once. The overlay SVG is 6 elements. Cost per active sweep ≤0.3ms/frame; typically ≤2 sweeps concurrent. Mobile: the fade variant — near-zero cost. The veil plate is a background colour, not a filter — no compositing cost.

**Tokens.** `--lab-deep`, `--plat-pale`, `--etch`, `--hairline`, `--plat-deep`, `--ease-settle`, `--wipe-dur: 620ms`, `--wipe-short: 480ms`, `--trigger-line: 82%`.

### 6.4 Self-verifying crosshair (the one ambient loop)

**What & why.** In the margin, one etched crosshair — the mark that sits at the registration corner of the current section — slowly drifts off its true position by about half a pixel over ~10 seconds, detects the error, and corrects itself with a tiny snap; a mono note beneath it logs `RE-VERIFIED · DRIFT 0.5 PX · CORRECTED`. This is the theme's only ambient loop, and it merges with content because it is not decoration idling: it is the page's calibration schedule made visible, the proof-by-demonstration that in this building even the ornaments are checked. It also carries real information — each correction increments a count that the footer certificate (§6.9) prints (`THIS PAGE RE-VERIFIED ITSELF N TIMES WHILE YOU READ`), so the loop is wired into the page's paperwork.

**Structure.** An inline SVG crosshair (two 18px arms, centre circle 3px) positioned at the current section's registration corner in the margin column, plus a mono log line under it (12px, `--plat-deep`). The crosshair's true position is its layout position; the drift is a CSS transform on the SVG (sub-pixel translate), so "correction" is the transform returning to exactly `translate(0, 0)`. A tiny state machine in the shared loop drives phases: hold → drift → detect → correct → log. The log line shows only the most recent event plus the running count: `RE-VERIFIED ×3 · LAST DRIFT 0.5 PX`.

**Motion spec.** Cycle ≈ 11.4s, deliberately not a round number (a 10.0s loop would be a screensaver's period; instruments are serviced on schedules, and the schedule here is 11.4s ± a seeded jitter of ±0.7s per cycle, derived from a `data-seed` so two builders' pages behave identically). *Hold* 6.0s: crosshair true. *Drift* 4.2s: transform eases toward a seeded offset of 0.4–0.6px on a seeded diagonal (`--ease-etch` reversed — slow, creeping, the way real instruments drift). *Detect* 0.3s: stillness — the crosshair is measurably wrong and nothing moves; the pause is the point. *Correct* 120ms: `--ease-verify` snap to (0,0). *Log* at the snap: the log line's count increments (text swap, no animation) and the footer's count (§6.9) is the same number, updated in the same frame.

**Choreography timeline.** 0.0s true · 6.0s drift begins · 10.2s drift complete (0.5px off) · 10.5s detection pause ends · 10.62s snap to true · 10.62s log increments · 11.4s (±jitter) next cycle.

**State matrix.** *Rest:* between cycles the crosshair is true and the log shows the last event — a resting instrument with its service sticker. *Drifting / correcting:* as above; the crosshair is never interactive. *Scrolled:* the crosshair belongs to the section in view; on section change it re-registers to the new section's corner *at true position* (a fresh instrument at a fresh bench — the drift count persists, the drift does not teleport). *Disabled (no JS):* the crosshair prints true, the log prints `RE-VERIFICATION REQUIRES OFFLINE INSTRUMENT` — no: it prints `RE-VERIFIED ×0 · AUTOMATED CHECK NOT RUNNING`, which is the truth. *Touch:* identical; nothing here is pointer-driven.

**Content-merge.** The count it accumulates is printed in the footer certificate as part of the page's self-certification; the drift value (0.5px) is the same ±0.5px that appears as the page's stated uncertainty (§6.5, §6.9) — the theme's signature tolerance, demonstrated rather than merely claimed. Remove the loop and the footer loses a line and the margin loses its proof; the element is load-bearing paperwork.

**Breakpoints.** ≥1200px and 768–1199px: full cycle in the margin column. <768px: there is no margin column, so the crosshair moves to the current section's header rule (inline, left of the section label) and the cycle runs identically; the log line sits under the section label. The drift amplitude is unchanged — 0.5px is 0.5px on any screen, which is rather the theme's point.

**Edge cases & failure modes.** Tab hidden: the loop sleeps; on return the cycle restarts at *hold* from true position (never mid-drift — a returning visitor must never catch the instrument wrong without seeing it corrected). Long pages: only the in-view section's crosshair exists — it is one element re-registered per section, not one per section (a page with nine crosshairs all drifting is a clock shop, not a bureau). Reduced-motion visitors (below) never see drift at all. If the footer is absent (a page type without the certificate, §7), the count is not printed anywhere and the log line carries it alone — the record stays consistent.

**Fallback & watchdog.** The crosshair's DOM state is *true position*; drift is a JS-applied transform. **Watchdog: 13 000ms** — if a cycle has not completed a correction within 13s of starting (loop fault), the transform is cleared to (0,0) and the log prints `CORRECTION APPLIED BY WATCHDOG` — even the failure is filed honestly. If JS never runs, the crosshair is simply a crosshair, true forever, log ×0.

**Reduced motion.** The crosshair never drifts. The log prints `RE-VERIFIED · HELD TRUE BY REDUCED-MOTION SETTING` once, and the footer count stays ×0 with the same explanation available. Stillness is a legitimate instrument state and is labelled as one.

**Accessibility.** Entirely `aria-hidden="true"`: the drift is sub-visual by design and its log is a duplicate of the footer's printed count. It occupies no focus, announces nothing. For low-vision visitors the element simply does not exist — which is correct, because its information content (the count) is available in full-size text in §6.9.

**Performance & mobile variant.** One sub-pixel transform on one small SVG, phase changes a few times per 11.4s: cost is unmeasurable (<0.01ms/frame amortised). Mobile: identical cost; only the placement changes. This is the cheapest element in the theme and the one that must never be cut for performance (§14) — cutting the proof to save nothing is the theme's definition of false economy.

**Tokens.** `--etch`, `--hairline`, `--plat-deep`, `--ease-etch`, `--ease-verify`, `--drift-amount: 0.5px`, `--cycle: 11.4s`, `--page-uncertainty: ±0.5px` (record R5).

### 6.5 Dead-stop counters (certified values)

**What & why.** Every figure that counts on this page counts to its certified value and **stops dead** — the final digit lands at full value with no overshoot, no settle bounce, no easing tail past the figure. One figure is licensed to do more: the page's uncertainty first prints a rough estimate, `±2 PX`, and then *corrects itself* to the certified `±0.5 PX` — the only counter allowed a second act, because a correction is not an error but a procedure. The element merges with content because the values are the site's actual certified data from the record (§6.17): on the reference build, four counters — `4 812` instruments certified in 2025 (R3), `20.0 °C` the laboratory reference temperature (R4), `1 000 MM` the metre (R1), and `±0.5 PX` the page's own uncertainty (R5). Marketing counters count *up to impress*; these count *to attest*.

**Structure.** Each counter is a mono `<span class="counter">` inside a ruled data cell (label above in mono caps, value, unit, and beneath, the tolerance or source line: `SOURCE: STANDARD RECORD R3`). The final value is the element's text content in the HTML from first paint — the count is a visual performance over a printed fact. JS reads the target from the text itself (never from a data attribute that could disagree with the print), so the animation cannot land anywhere the print didn't already say.

**Motion spec.** Trigger: the cell enters the viewport (top crosses 78%). Count duration scales with magnitude at a fixed digit rate: the value sweeps from 0 (or from the minimum sensible start — temperature counts from 0.0 °C) to target over `min(1 600ms, 400ms + 90ms × digits)` — 4 812 takes 1 600ms, 20.0 takes 760ms, 1 000 takes 1 600ms (4 digits + separator handling). The approach curve is `--ease-settle` mapped so the *displayed* value is `round(target × easedProgress)` — display values are integers/declared decimals at every frame, never raw floats: a counter that flashes `4 811.37` instruments is a slot machine. The final frame sets exactly the printed string. **The uncertainty correction:** `±2 PX` prints first (it is the rough estimate, set in `--plat-deep`), holds 900ms after the other counters land, then the `2` is struck with an etched line (120ms draw) and `0.5` sets beside it in `--etch` over 240ms — a correction performed in the open, initialled by the log convention of §12.

**Choreography timeline.** (A four-cell bank entering together.) 0ms cells cross 78% · 0–1 600ms 4 812 counts · 0–760ms 20.0 counts, lands dead at 760ms · 0–1 600ms 1 000 counts · 1 600ms all landed · 2 500ms ±2 PX struck · 2 740ms ±0.5 PX set · bank at rest, every value exactly as printed in the HTML.

**State matrix.** *Rest (pre-trigger):* final values printed — a visitor who never triggers the count (or has no JS) reads the certified figures, which is the entire point. *Counting:* as above; values are display-only, the DOM text is swapped per frame and restored exactly. *Landed:* static forever; scrolling away and back never recounts (a certificate is not re-issued because you looked away). *Scrolled-past without triggering* (fast scroll through): if the cell exits the top before triggering, the count is skipped and the printed value simply stands — no debt is carried. *Disabled:* printed values only. *Touch:* identical.

**Content-merge.** The counters are the record's figures (R1, R3, R4, R5) in the page's data cells; the same figures appear in §6.17's table and in the footer certificate's checked-values line (§6.9), and §10's figure audit greps that all printings match character-for-character (thin spaces included). The animation is a demonstration of the theme's claim about numbers; the numbers are the content.

**Breakpoints.** ≥1200px: four cells in a row. 768–1199px: two by two. <768px: stacked, one per row; count durations shortened 25% (a phone is not a bench) but the dead-stop rule is unchanged — rationing time is allowed, rationing exactness is not. The uncertainty correction sequence is never shortened away; it is the element's signature.

**Edge cases & failure modes.** A target with decimals (20.0): the decimal digit is part of the count (19.9 → 20.0 lands exactly; intermediate values show one decimal, always). A target of 0 or negative tolerances: not countable — such values print statically by rule (a counter that counts to ±0.5 from 0 is the correction sequence's job, handled above, not the sweep's). Content longer than the record (a fifth counter added by an editor): it must be added to the record first (§6.17) or the figure audit fails the build — counters may not be invented at the page level. Frame drops during the sweep: the displayed value is computed from elapsed time, not frame count, so jank compresses the sweep but the landing is still exact and on schedule.

**Fallback & watchdog.** **Watchdog: 2 000ms** from trigger — any counter not landed is set to its printed string immediately. Because the printed string *is* the target, the watchdog is a restore, not a guess. No-JS: values stand as printed.

**Reduced motion.** No sweep, no correction theatre: all values print at their certified figures, including `±0.5 PX` directly (the rough estimate is not shown — showing a wrong figure to a reduced-motion visitor and never correcting it would be a lie by omission; the correction's *result* is what prints).

**Accessibility.** Counters are never in a live region — a screen reader reads the final printed value once, as text, because the DOM text at rest is the value. During the sweep the span is `aria-hidden` with a visually-hidden static twin carrying the final value (the standard pattern: performance for the sighted, fact for everyone). Cell labels are real text. Contrast: values `--etch` 15.34:1; the struck rough estimate `--plat-deep` 6.32:1.

**Performance & mobile variant.** ≤4 concurrent counters, one text write per counter per frame on the shared loop: ≤0.2ms/frame worst case. Mobile: durations −25%, same code path. The struck-correction is one SVG line draw.

**Tokens.** `--etch`, `--plat-deep`, `--hairline`, `--ease-settle`, `--count-max: 1600ms`, `--trigger-line: 78%`, plus record figures R1/R3/R4/R5 (§6.17).

### 6.6 Crosshair hover readout (inspection is measurement)

**What & why.** Hovering any *measured element* — an image figure (§6.3), a data cell (§6.5), an instrument card (§6.12), the platinum bar (§6.8), a spec table (§6.11) — centres an etched crosshair on that element and prints its true dimensions in the margin: `W 640 PX · H 400 PX · 160.0 × 100.0 MM AT SCALE`. The dimensions are not metadata; they are read live from the element's rendered box at hover time. This merges with content because it turns the visitor's curiosity into the lab's core act — inspection *is* measurement here — and because it is genuinely useful: on a site about measurement, the honest answer to "how big is this, really?" is always available and always true.

**Structure.** Measured elements carry `data-measure` (a build-time marker, no values — values are never declared, only taken). The crosshair is a single reusable SVG (two 22px arms + centre ring) absolutely positioned over the hovered element's centre; the readout is a single mono block in the margin column at the element's vertical level (on <768px, a line directly beneath the element). Both are one shared instance moved between elements — there is never more than one inspection on the page, as there is one pair of hands on a bench.

**Motion spec.** On hover intent (pointer rests 120ms — a brush-past is not an inspection): the crosshair etches in over 140ms (`--ease-etch`, arms draw from centre outward), the element's frame gains a 1px `--trace` registration outline (the one place trace blue touches content boxes: *this object is on the bench*), and the readout prints — W and H appear as integers the moment they are read (reading is instant; only the crosshair's drawing takes time). On leave: crosshair and outline fade in 120ms, the readout remains for 600ms then clears to the margin's resting content (the last reading stays available to be copied — inspectors write things down). Frame tilt is *not* part of this element; the specified 0.5° tilt belongs to §6.15's plates and never combines with inspection (a tilted object cannot be honestly measured, and the readout of a tilted element would print its bounding box — so measured elements are never the tilting ones; the two sets are disjoint by build rule).

**Choreography timeline.** 0ms pointer rests · 120ms intent confirmed, outline prints · 120–260ms crosshair arms draw · 140ms readout prints W×H and mm conversion · leave: 0–120ms crosshair fades · +600ms readout clears.

**State matrix.** *Rest:* no crosshair; margin shows the section's resting note. *Hover (fine pointer):* as above. *Focus (keyboard):* a measured element that is also focusable (cards with links, the bar's region) shows the same crosshair + readout on focus — inspection is not a pointer privilege; the readout appears in the margin and is also the element's `aria-describedby` target (§ below). *Active (touch tap):* first tap on a measured element = inspection (crosshair + readout, no navigation); second tap = the element's action, if any. *Scrolled-past / element removed:* the shared instance detaches cleanly; a readout never points at a vacancy. *Disabled (no JS):* no readouts — and nothing on the page claims dimensions it cannot take, because all printed dimensions elsewhere are either declared (labelled DECLARED, §6.3) or measured by build-time instruments (the record).

**Content-merge.** The readout's mm conversion uses the declared scale (§4) — it teaches the page's own system while reporting. On the spec page, hovering the platinum bar (§6.8) prints its length as `1 000.0 MM` — the one readout with no pixel figure beside it, because at reference scale they are the same number, and the margin notes `THE STANDARD: PX AND MM AGREE`.

**Breakpoints.** ≥1200px: margin readout. 768–1199px: margin readout, arms 18px. <768px: no margin — the readout prints as a mono line directly under the element, crosshair arms 14px; tap-to-inspect as above. The measurement arithmetic is identical at every size; only the printing moves.

**Edge cases & failure modes.** Element partially off-screen: the crosshair centres on the *visible* centre only if the true centre is off-screen — no: it centres on the true centre and if that is off-screen the readout still prints (the numbers are the content; the crosshair is the ceremony) with the note `CENTRE OFF-SCREEN`. Element resizing during hover (responsive image swap): the readout re-reads on a 300ms debounce and prints the new values with `RE-MEASURED`. Nested measured elements (a card containing a figure): the innermost measured element wins — you inspect the object, not its shelf. Rapid pointer movement across many elements: the 120ms intent delay means a sweep inspects nothing — by design.

**Fallback & watchdog.** The readout is a live reading; if the shared loop is dead the element simply never arms — **watchdog: 400ms** after hover intent, if the crosshair has not drawn, the readout prints anyway (numbers before ceremony, as §6.3). If `getBoundingClientRect` returns zeros (display:none content), nothing prints — a hidden object has no dimensions and the page says nothing rather than `0 × 0`.

**Reduced motion.** The crosshair prints instantly (no draw), the outline prints instantly, the readout identical. Inspection is information; reduced motion removes only its 140ms of theatre.

**Accessibility.** The readout block has `role="status"` with `aria-live="off"` by default — hover readings must not chatter — but when inspection is triggered by *keyboard focus*, the readout becomes the focused element's description via `aria-describedby`, so the measurement is available to screen-reader users on demand. Touch targets: measured elements that are interactive keep ≥44px targets; the crosshair is `aria-hidden` decoration over a real text reading. Readout contrast `--plat-deep` 6.32:1, values `--etch` 15.34:1.

**Performance & mobile variant.** One rect read per inspection (forced reflow is acceptable at hover frequency; it is cached per element until resize). No per-frame cost at rest. Mobile variant is the under-element printing above; the rect read is the same.

**Tokens.** `--trace`, `--etch`, `--plat-deep`, `--hairline`, `--ease-etch`, `--hover-intent: 120ms`, `--readout-hold: 600ms`, `--scale` (per breakpoint, §4).

### 6.7 Traceability seal click (the reader builds the paper trail)

**What & why.** Clicking a *certified element* — a data cell, an instrument card, a chain node, the bar — presses the red traceability seal beside it: a circular seal in `--seal` (the theme's only red) that scales in with a dry, hard stop, reading `TRACEABLE · STANDARD No. 9 ·` around its rim and the element's record reference at its centre. Simultaneously, a line is appended to the footer certificate (§6.9): `SEALED BY VISITOR — TOLERANCE TABLE, §6.11 · REF R7`. The visitor is literally assembling the page's paper trail as they read. It merges with content because the seal is not a like-button: it certifies *that specific element's* traceability to the record, its reference is the element's real record key, and the certificate it feeds is the page's thesis (§6.9). An element without a record reference cannot be sealed — the build forbids `data-seal` without `data-ref`.

**Structure.** The seal is an inline SVG (outer ring, inner ring, rim text on a circular path, centre ref in mono) cloned per sealed element from one `<template>`. The stamp target is a reserved 56px seal dock at the element's top-right — reserved in layout from first paint (an empty etched circle outline, `--hairline`, prints where a seal *would* go: the dock is part of the element's design, so stamping never shifts layout by a single pixel). The certificate line is a real `<li>` appended to the footer certificate's sealed-items list (§6.9), with the element's name and ref as printed text.

**Motion spec.** On click: the seal scales from 1.35 → 1.0 over 130ms with `--ease-stamp` (fast in, hard stop — a stamp does not ease out, it *lands*), opacity 0→1 in the first 40ms, and at landing a 1px `--seal` registration ring pulses outward exactly 6px and fades over 220ms (the ink's squeeze-out — the only radial effect in the theme, licensed here because it is what ink does). No bounce: scale never goes below 1.0 (§5's law; a stamp that rebounds is a stamp lifted and re-struck, a different and dishonest gesture). The certificate line appends at the same frame (no animation — paperwork files instantly). A sealed element's dock outline turns solid `--seal` at 30% — a filed copy mark. Unsealing: a second click does *not* remove the seal (a certificate, once issued, is not un-issued); instead the dock note prints `ALREADY SEALED · LINE 3 OF CERTIFICATE`. The state persists for the session (`sessionStorage` list of refs) so a reload keeps the visitor's trail — paperwork survives the visit.

**Choreography timeline.** 0ms click · 0–40ms seal fades in at 1.35 scale · 40–130ms scale lands to 1.0 · 130ms ink ring emits · 130–350ms ring fades at 6px · 130ms certificate line appended in footer · 350ms element at sealed rest.

**State matrix.** *Rest (unsealed):* empty etched dock — the invitation is a printed circle, not a button begging. *Sealing:* as above. *Sealed:* seal at rest in dock, dock outline filed-mark, certificate line present. *Re-click:* the `ALREADY SEALED` note (mono, in the dock's caption position, 1 600ms then fades to the persistent small line `SEALED · SEE CERTIFICATE`). *Focus:* certified elements that are sealable are focusable buttons or contain a real "Seal this" button (§ Accessibility) — the seal action is never a bare div click. *Disabled (no JS):* docks print empty and the certificate's sealed list prints its static line `NO SEALS APPLIED THIS VISIT` — an honest empty record, not a hidden feature. *Touch:* tap = click, identical timings.

**Content-merge.** The seal's centre text is the element's record reference (R1–R8 and per-element keys from §6.17); the certificate line names the element as the page names it. The count of seals is printed in the footer (`VISITOR SEALS APPLIED: N`) and is therefore a figure on the page that §6.17's law covers: it is a measurement (a count of events that happened), printed from the event log, never estimated.

**Breakpoints.** ≥1200px and 768–1199px: dock 56px, seal full size. <768px: dock 44px, rim text drops the outer legend and keeps the centre ref + `No. 9` (a small stamp is a smaller stamp, not a different one); timings unchanged. Layout reservation holds at every size — CLS from stamping is 0 by construction and §10 measures it.

**Edge cases & failure modes.** Sealing everything: licensed and expected — the certificate list grows; past 12 seals the footer list scrolls within its ruled area (max-height with the certificate's own scrollbar styling: a longer certificate, not a taller page surprise — the footer's outer dimensions are reserved for 12 lines + the scroll state). Element sealed, then the element is re-measured (§6.3 resize case): the seal stands (the *identity* was certified, not the width). Print stylesheet: seals print — a visitor who prints the page gets their seals on the paper, in red if the printer allows; the certificate list prints in full. Session restore mid-list: refs re-stamp instantly without animation on load (paperwork, not theatre).

**Fallback & watchdog.** **Watchdog: 400ms** — if the stamp animation has not landed (loop stall), the seal snaps to its rest state and the line appends; the *record* must never depend on the animation completing. If the footer certificate is absent on a page type (§7), seals still stamp and the count is kept in the session log, printed instead in the page's closing record line (§6.18 pattern) — the trail always has somewhere true to go.

**Reduced motion.** The seal appears at rest scale (no press, no ink ring), the line appends. The certification — the content — is unchanged; only the striking of the stamp is stood down.

**Accessibility.** Each sealable element has an associated real `<button class="seal-btn">` (visually the dock itself, 44px minimum target) with `aria-pressed` reflecting state and an accessible name like `Apply traceability seal to Tolerance Table`. On sealing, an `aria-live="polite"` announcement: `Sealed. Certificate line 3 added.` The seal SVG is decorative (the state is in the button and the certificate text). Focus outline: 2px `--trace` offset 2px — visible, on-brief, never the seal red (focus is navigation, not certification).

**Performance & mobile variant.** One SVG clone + one DOM append per seal; the press is one transform on a 56px node. Negligible. Mobile: same, smaller dock. The session list is a few dozen bytes.

**Tokens.** `--seal`, `--hairline`, `--etch`, `--plat-deep`, `--trace`, `--ease-stamp`, `--seal-dock: 56px`, `--seal-dock-sm: 44px`.

### 6.8 The one platinum element (the standard bar)

**What & why.** Exactly one element in the entire theme carries a brushed platinum sheen: the standard-metre bar in the spec section (§6.11) — a representation of the platinum-iridium prototype metre, drawn as a long bar with an X-shaped cross-section hinted by two etched lines, its length printed as `1 000.0 MM`. When the bar first enters view, the sheen — a soft diagonal band of `--sheen-hi/mid/lo` — moves across it **once, slowly**, and never again: not on re-scroll, not on hover, not on any later visit in the session. Luxury rationed to a single object, exactly as the original specifies, because in the bureau the prototype is the only object kept like this, and a page where everything gleams is a page where nothing is the standard. It merges with content because the bar *is* the content of the spec section — the physical referent of every length on the site — and its sheen is the visitor's one permitted moment of awe, spent on the right object.

**Structure.** A `<figure class="standard-bar">`: an SVG bar (length = the content measure, height 54px) — the bar body filled `--plat`, top face a lighter plane, the X-section shown in a small end-cap detail at the left (the prototype's actual cross-section, drawn true), two etched fiducial lines near the ends marking the defined metre between them (the metre is the distance *between the lines*, as the real definition ran — a detail the caption states). The sheen is a `<linearGradient>` band in a clipped overlay rect, translated across by transform. The caption beneath, mono: `THE STANDARD · PLATINUM–IRIDIUM · THE METRE IS THE DISTANCE BETWEEN THE FIDUCIAL LINES`. The sheen overlay's gradient stops are the only rules in the codebase allowed to reference `--sheen-*` (§2) — §10's platinum census greps for them.

**Motion spec.** Trigger: the bar's centre crosses 60% of viewport height, once per session (flag in `sessionStorage`; a new session is a new visit to the vault and may see it once more). The band starts at −20% of bar length and travels to 120% over 2 800ms, `--ease-settle` — slow, even, decaying at the ends; band width 18% of bar length, soft edges (gradient alpha 0 → 0.55 → 0). Simultaneously the two fiducial lines brighten from `--plat-deep` to `--etch` over the same 2 800ms and stay at `--etch` (the definition, once seen, stays seen — within the session the lines remain at full etch; next session they start quiet again). Nothing else on the page moves. After the pass, the overlay is removed from the DOM — the sheen cannot be re-triggered by any means short of a new session, including devtools class fiddling with the trigger (the node is gone).

**Choreography timeline.** 0ms bar centre crosses 60% · 0–2 800ms band travels −20% → 120% · 0–2 800ms fiducial lines deepen · 2 800ms band exits, overlay removed · bar at rest, lines etched, forever (this session).

**State matrix.** *Rest (pre-trigger):* the bar printed matte in `--plat` planes, fiducial lines in `--plat-deep` — a complete, honest figure; the sheen is an event, not a property the figure lacks. *Sheening:* as above; the bar is not interactive during or after. *Post-sheen:* matte bar, etched lines. *Scrolled-past before trigger* (fast scroll): if the bar exits the top before its centre held 60% for 300ms, the sheen is *not* spent — it arms for the next genuine encounter (scrolling back up to it counts). A visitor who never dwells on the bar never sees the sheen, and the page is complete without it — rationing includes the possibility of missing it, like a vault viewing you didn't book. *Disabled:* matte bar, lines at `--etch` (print the definition at full strength when the ceremony can't run). *Touch:* identical trigger.

**Content-merge.** The bar's printed length is record R7 (= R1: 1 000.0mm — the same metre as the hero's line, in metal). §6.6's hover readout on the bar prints the theme's one special reading (`PX AND MM AGREE`). §6.11's spec table beneath it lists the bar's own tolerances. The sheen's gradient tokens exist only here. Every thread of the theme's luxury budget is spent on the object the whole site is *about*.

**Breakpoints.** ≥1200px: bar = full measure (1 000px), height 54px. 768–1199px: bar = 92vw, height 44px; the printed length remains `1 000.0 MM` (the bar *represents* the metre; at 0.75 scale its screen length is 750px and the caption gains `SHOWN AT 0.75 SCALE` — representation labelled, never passed off as the thing). <768px: bar = 92vw, height 34px, end-cap detail simplified to a square section mark; sheen band width 24%, duration 2 200ms (a shorter bar, a proportionally shorter pass).

**Edge cases & failure modes.** The one unforgivable bug class: a second sheen. Any other element found with a `--sheen-*` token, a gradient sweep, or a shine hover fails the build (§9, §10) — the census is a grep, not a judgement call. Bar near the page top on short pages (spec page variant, §7): the 60% trigger may be met at load — the sheen then plays after a 600ms delay post-load (after §6.1's division if both are present; two ceremonies never overlap — if the hero division is running, the sheen queues until it lands +400ms). Print: the bar prints matte with etched lines; no sheen on paper, obviously, and the caption carries the meaning.

**Fallback & watchdog.** **Watchdog: 3 200ms** after trigger — if the band has not completed (loop stall), the overlay is removed and the fiducial lines set to `--etch`: the end state is reached without the journey, and no state exists in which the bar is left half-lit. No-JS: matte bar, etched lines, full caption.

**Reduced motion.** The sheen never plays. The fiducial lines print at `--etch` from the start. The visitor loses a gleam and keeps the standard — the correct trade, stated here so no implementer "compensates" with a fade.

**Accessibility.** The figure's meaning is its caption (real text) plus alt text on the SVG's `<title>`: `The platinum–iridium standard metre bar; the metre is the distance between its two fiducial lines.` The sheen is `aria-hidden` motion over a described object. Contrast: caption `--plat-deep` 6.32:1; the bar's own planes are decorative fills (no text sits on the bar).

**Performance & mobile variant.** One gradient overlay transform for 2 800ms, once: the cheapest luxury in the library. The overlay is one rect; the gradient is GPU-friendly. Mobile: shorter pass, same single node. §14 protects this element's budget line explicitly — it may not be cut, only (under reduced motion) stood down.

**Tokens.** `--plat`, `--sheen-hi`, `--sheen-mid`, `--sheen-lo`, `--plat-deep`, `--etch`, `--ease-settle`, `--sheen-dur: 2800ms`, plus record R7 (§6.17).

### 6.9 Certificate footer (the page certifies itself)

**What & why.** The footer is a calibration certificate *for the website itself*, enclosed in the double certificate border (§4): it states the page's measured width, its type sizes verified against §3's spec, its uncertainty (`±0.5 PX`), the count of times the page re-verified itself while being read (§6.4), the visitor's seal lines (§6.7), a signature (`THE KEEPER OF STANDARD No. 9`), a date, and the next calibration due — one year from the build date. On page transition, the incoming page's certificate border aligns exactly with the outgoing one's before the swap (§6.16). It merges with content because it is the theme's thesis signed: a site about traceability that did not certify itself would be a sermon its preacher ignores. Every value on it is either measured live (page width, re-verification count, seal count) or declared in the record (uncertainty, due date) — the law (§1) holds to the last line of the page.

**Structure.** A `<footer>` in the certificate border containing a mono table of checked values (label / measured / specified / verdict columns — the page's own §6.5-style data, in certificate register): rows for content width (measured live at print time, in px and mm at scale), display type size (64px as specified in §3), body size (17px), the re-verification count (§6.4), visitor seals applied (§6.7, with the appended lines as an ordered list above the table), uncertainty (R5), build date and next-due date (R8), and the signature line. The width row is genuinely live: a small script measures `document.documentElement` content width when the footer first enters view and prints the result — on the reference build it reads `1 000 PX · 1 000.0 MM · WITHIN SPEC`.

**Motion spec.** The certificate itself is static — certificates do not animate. Three licensed motions only: (1) the width row's value counts dead-stop (§6.5's machinery, 900ms) when the footer first enters view, because it is a measurement being taken; (2) seal lines append instantly on §6.7 events (paperwork); (3) the re-verification count increments in place when §6.4 logs (a text swap). The border-alignment on transition belongs to §6.16. The signature is a printed name in mono, never a script font — a bureau signs in type or not at all.

**Choreography timeline.** Footer enters view: 0–900ms width counts to its measured value, lands dead · the verdict word `WITHIN SPEC` prints at 900ms · all else already printed.

**State matrix.** *Rest:* the complete certificate, all rows printed with build-time values; the live rows (width, counts) show their last measured values — on first paint before any measurement, the width row prints `TO BE MEASURED ON VIEWING` (an honest pending state, never a guessed number). *Seals appended:* the list grows (§6.7's 12-line rule). *No-JS:* every row prints its build-time declared value; the width row prints the *specified* width labelled `SPECIFIED — NOT MEASURED THIS VISIT`; counts print ×0 with their explanations (§6.4/§6.7). The certificate is complete and truthful in every state — that is what makes it a certificate. *Touch:* identical.

**Content-merge.** This is the destination of half the theme's systems: §6.4's count, §6.7's lines, §6.5's uncertainty, §6.1's metre (cited as the width's reference), §3's type spec (verified against). It is also the page's actual footer — navigation links, legal lines and contact live *inside* the certificate as its final rows (`ISSUED BY`, `ENQUIRIES`), so the theme never has a second, lesser footer beneath the signed one.

**Breakpoints.** ≥1200px: four-column table. 768–1199px: two columns (label+measured, specified+verdict stacked). <768px: single column rows, each row a ruled block; the border remains double at all sizes (a certificate's border is not a responsive luxury). The seal list's 12-line scroll area becomes 8 lines.

**Edge cases & failure modes.** The width measurement surprises: on a viewport where the content is fluid (768–1199), the measured width will *not* be 1 000px — the verdict then prints the measured value against the *breakpoint's* specified width (the record declares per-breakpoint specs, §6.17) so the verdict stays meaningful. If it ever falls outside its breakpoint spec (a build bug), the certificate prints `OUT OF SPEC — ΔN PX` in `--etch` (never hidden, never red-shamed — red is rationed): the page reports its own defect in its own footer, which is the most on-theme failure mode in the library and a genuine debugging gift. Dates: the due date is build date + 1 year from the record; a stale build (served after its due date) prints `CALIBRATION OVERDUE — RENEWAL PENDING` — sites, like instruments, go out of calibration, and this one admits it.

**Fallback & watchdog.** **Watchdog: 1 500ms** after the footer enters view — if the width measurement has not printed, it prints the specified value labelled as specified-not-measured. Everything else is static text; there is nothing else to fall back from.

**Reduced motion.** The width prints without counting. All else identical.

**Accessibility.** The certificate is a real `<table>` with a `<caption>` (`Calibration certificate for this page`) and proper header cells — screen readers get the table, not a picture of one. The signature and dates are text. Contrast: mono `--etch` 15.34:1 and `--plat-deep` 6.32:1 on `--lab`. The footer is last in focus order, as footers are; its links are ordinary links with the theme's focus outline.

**Performance & mobile variant.** One measurement + ≤1 count per page view; the table is static HTML. Negligible at every size; the mobile single-column form is the same nodes restyled.

**Tokens.** `--etch`, `--plat-deep`, `--hairline`, `--seal` (the certificate's own seal, printed once at the signature — the footer's one licensed red besides visitor seals), `--ease-settle`, plus record R5/R8 (§6.17).

### 6.10 Certificate masthead (navigation)

**What & why.** The site's header is the top of the certificate: the bureau's name set as a certificate title (`BUREAU OF STANDARDS — STANDARD No. 9` in mono label register over an Inter 600 wordmark), a hairline rule beneath, and the navigation as a row of *index entries* — each link printed with its section number and its depth in the site measured in pages (`02 · SERVICES · DEPTH 1`). A thin etched rule under the nav carries a sliding index mark that sits under the current section — the masthead's only motion, borrowed from the vernier's grammar: position, reported. It merges with content because the header is not a banner above the document; it is the document's first ruled block, and its index numbers are the same section numbers the vernier (§6.2) and section headers (§4) use — one numbering system for the whole artefact.

**Structure.** A `<header>` with: mono eyebrow (bureau line), wordmark, nav as an ordered list of links (number + name + depth), and the index-mark rule (a 1px `--hairline` track with a 28px `--etch` mark). A compact variant (on scroll past 240px) collapses the eyebrow and wordmark to one line — the certificate's letterhead shortens, it does not become a different header. The current-page entry is marked by the index mark and by `aria-current`, and its number is set in `--trace`.

**Motion spec.** Index mark: on navigation or on scroll-spy section change, the mark slides to the active entry over 240ms `--ease-settle` (dead stop, no overshoot — a mark that wobbles past its entry is misregistered). Compact collapse: on crossing 240px scroll, the eyebrow fades (120ms) and the header height animates 96px → 56px over 200ms `--ease-etch`; expanding reverses it. Scroll-spy updates are driven by the shared loop's section register (the same one §6.4 re-registers against) — one source of "where am I" for the whole page.

**Choreography timeline.** Page load: mark at the current entry (no slide — it *starts* registered). Section change while scrolling: within one frame of the section register changing, mark slides 240ms. Scroll past 240px: collapse 200ms, once per crossing.

**State matrix.** *Rest:* full letterhead, mark registered. *Compact:* past 240px — one-line letterhead, nav intact (navigation is never the thing collapsed away). *Hover:* a nav link's number turns `--trace` and a hairline underline etches left-to-right 120ms. *Focus:* 2px `--trace` outline; the index mark does not follow focus (the mark reports scroll position, not keyboard position — two facts, two indicators, never conflated). *Disabled (no JS):* full letterhead always, mark printed under the current page's entry server-side. *Touch:* no hover states; tap targets ≥44px tall in both header forms.

**Content-merge.** The nav numbers are the site's real section indices, used identically by §6.2's bands and §4's section labels; the depth figure is the page's true depth in the site tree (printed from the build's sitemap data, not invented). A nav entry whose depth is wrong is a record error, caught by the same audit culture as every other figure (§10).

**Breakpoints.** ≥1200px: full letterhead, all entries inline. 768–1199px: entries inline, eyebrow shortened to `STANDARD No. 9`. <768px: the nav becomes a ruled index panel behind a `CONTENTS` button (the word MENU does not exist in this theme's vocabulary, §12) — the panel is a certificate-bordered block listing the same numbered entries full-width; the index mark rule is hidden (the panel *is* the index). Compact form <768px keeps the CONTENTS button reachable at 56px header height.

**Edge cases & failure modes.** Many sections (a deep site): past 7 entries, the nav switches to two ruled rows at ≥1200px rather than shrinking type (type sizes are spec, §3 — they do not flex to fit furniture). Long page titles in the panel: wrap to two lines, never truncate with ellipsis — a certificate does not abbreviate its own entries. Scroll-spy at page foot: the last section owns the mark (the footer certificate is section 9's territory on the reference build).

**Fallback & watchdog.** All header states are CSS classes on static HTML; the collapse and mark are JS-driven but the header is fully usable without them. **Watchdog: 600ms** — if the loop is dead, the header is forced to full form and the mark to the current page's entry (the server-side state): a stuck-compact header on a dead page would trap the nav's context, so the watchdog restores the letterhead.

**Reduced motion.** No slide, no collapse animation: the mark cuts to position; the header still compacts (height change is layout information) but instantly at the threshold.

**Accessibility.** A real `<nav>` with an ordered list; `aria-current="page"` on the active entry; the CONTENTS button is a `<button aria-expanded>` controlling the panel; skip-link (`SKIP TO CONTENT — SECTION 1`) is the page's first focusable element, styled as a mono label. Header contrast: wordmark `--etch` 15.34:1, numbers `--plat-deep` 6.32:1, active `--trace` 8.27:1.

**Performance & mobile variant.** The mark is one transform; collapse is one height animation on the header (layout cost confined to the header's own box, content below is in normal flow and shifts once — the shift is the design, declared, and happens before first content paint on restored scroll positions by applying the compact class pre-paint from the scroll register). Mobile panel is the same list, restyled.

**Tokens.** `--etch`, `--plat-deep`, `--trace`, `--hairline`, `--ease-settle`, `--ease-etch`, `--header-h: 96px`, `--header-h-compact: 56px`.

### 6.11 The spec table & the pinned metre (spec section)

**What & why.** The spec section is the theme's workshop floor: a full tolerance table — quantity, nominal, tolerance, measured, verdict — above which the metre line *pins* for the length of the table while its graduations cascade in step with the rows the visitor passes. Each row, as it crosses the pinned line, has its measured value checked: the verdict cell prints `WITHIN` (or, for the one deliberately honest row, `AT LIMIT`). The pinning merges ruler and data into one act: you read the tolerances *under* the metre they were measured with, and the cascade of graduations is paced by the rows themselves — scroll is the feed rate of the inspection. This is the section §6.8's bar presides over (the bar sits at its head) and the section the worked example (§8B) builds end-to-end.

**Structure.** A section with: the standard bar (§6.8) at its head; a pin container of height = table height + 60vh scroll distance, inside which a sticky stage holds a second metre SVG (a sibling of §6.1's, 100 medium graduations — the working rule, not the hero's full division) above a real `<table>`. Rows are build-time HTML with all values printed; the cascade state is a scrubbed value `p ∈ [0,1]` over the pin range mapping to graduations drawn (0–100) and to the active row index. Verdict cells are printed text; the "checking" is a visual registration — an etched crosshair (§6.6's grammar) that sits in the active row's margin cell.

**Motion spec.** Pin range: the stage sticks when the section top reaches 12% of viewport and releases after the table's full height + 60vh of scroll. Graduations draw scrubbed `--ease-gauge` (linear, via the shared lerp at 0.16): at pin progress p, `round(p × 100)` medium ticks are etched. Row activation: the row whose centre is nearest the pinned line's vertical position is *under inspection* — its margin crosshair prints (instant, it is a registration mark) and its measured value bolds — no: values never bold (two weights only, and 600 is for headings); the active row's background rules to `--lab-deep` and its crosshair prints. That is the whole emphasis system: a ruled highlight, honestly flat. On release, all 100 ticks stand etched and the table scrolls away complete.

**Choreography timeline.** (Scrubbed; percentages of pin range.) 0%: stage sticks, 0 ticks. 0–100%: ticks etch linearly with scroll; rows activate in sequence, ~1 row per 9% on the reference table (11 rows). 100%: 100 ticks, last row inspected, stage releases.

**State matrix.** *Rest (pre-pin):* the table fully printed, the working rule fully etched — the section reads perfectly without ever pinning (pinning is a ceremony over a complete table). *Pinned:* as above. *Released:* complete table, complete rule. *Scrolled back up:* the scrub reverses exactly — ticks un-draw? No: graduations, once etched in a session, stay etched (§6.1's law: a metre does not forget); on reverse, only the row activation retraces. The cascade is a ratchet, the inspection is a reading. *Disabled (no JS):* no pin (CSS sticky is also disabled by the no-JS class — a sticky stage without its scrub would strand the table's top rows), table and full rule print statically. *Touch:* identical scrub.

**Content-merge.** The table's figures are the record's tolerances for the worked instrument (§6.17's chain values appear as rows); the pinned rule is the same metre as §6.1 at working resolution; the bar at the head is the physical standard the table traces to. The section is the theme's argument in one screen: standard → rule → measurements → verdicts.

**Breakpoints.** ≥1200px: full pin, 100 ticks. 768–1199px: pin range shortened (table height + 30vh), ticks 50 (every 2nd) — caption under the rule notes `WORKING RULE SHOWN AT 50 DIVISIONS`. <768px: **no pin** — a pinned table on a phone is a trap; the rule prints fully etched above the table, rows activate by the 82% line (§6.3's trigger grammar) as a ruled highlight only. The table itself becomes stacked row-blocks <768px (label above value), all values preserved.

**Edge cases & failure modes.** Table longer than the pin budget (an editor adds 30 rows): the pin range is computed from the table's actual height at build time, so the scrub stretches — rows activate faster, ticks still complete exactly at release; the build warns past 20 rows (a spec table that long should be split into two benches, §7). A row's measured value outside tolerance: prints `OUT OF TOLERANCE — Δ…` and the row is *kept* — the theme never hides a failing row (§9); the reference build ships all rows within, with one AT LIMIT, because a table with a doctored failure teaches the wrong lesson and a table with a real one belongs to the client's data, not the demo's. Resize during pin: the scrub recomputes from live geometry each frame; the ratchet (etched ticks) only ever grows.

**Fallback & watchdog.** **Watchdog: 900ms** — if the pin is engaged but the loop has not updated the scrub for 900ms, the stage unsticks (class removed), all ticks etch, and the table stands complete in flow. A stuck pin is the one failure that can strand content in this theme, so it owns the shortest leash relative to its risk. CSS-only safety net: the sticky stage has a `max-height` and the pin container a definite height, so even a total JS+CSS failure degrades to a long section, never an overlapping one.

**Reduced motion.** No pin, no cascade: rule fully etched, table printed, row highlight still follows scroll position by cut (position is information). The section loses its ceremony and none of its content.

**Accessibility.** A real `<table>` with `<th scope>` and a `<caption>`; the pin never changes reading order (the stage is the table's natural position, stuck). Row activation is visual only — verdicts are printed text in every state, so nothing about a row's status is motion-dependent. The stacked <768px form uses the same table markup with CSS display changes and keeps header association via `data-th` printed labels.

**Performance & mobile variant.** The scrub is one lerped value driving a `stroke-dasharray` window on a pre-rendered 100-tick group (ticks are drawn by revealing a mask, not by toggling 100 nodes) + one row class change per activation. ≤0.4ms/frame. Mobile: no pin, no mask — near zero.

**Tokens.** `--etch`, `--hairline`, `--lab-deep`, `--plat-deep`, `--ease-gauge`, `--lerp: 0.16`, `--pin-extra: 60vh`, `--rule-divisions: 100`.

### 6.12 Instrument cards (the catalogue)

**What & why.** The listing unit for instruments and services: a ruled card — no shadow, no rounding, a certificate's grandchild — carrying the instrument's name (Inter 600, 28px), its portrait (admitted by §6.3's caliper), and three certified figures in mono (range, resolution, uncertainty), each figure tracing to the record or to the client's product data declared in the build manifest. A card's whole surface is its link to the detail page, and its footer line is a seal dock (§6.7): the card can be sealed from the listing, because a procurement officer shortlisting instruments *is* building a paper trail. The card merges with content by refusing every catalogue cliché — no price bursts, no star ratings, no "NEW" flashes: in this world an instrument is its specification, and the card is a small certificate that happens to be clickable.

**Structure.** An `<article>` with double-hairline top rule, figure (§6.3), `<h3>` name, a definition list of the three figures (dt = quantity in mono caps, dd = value + unit + tolerance), a one-line application note in body text, and the footer row: `DETAIL →` link text and the §6.7 seal dock (44px in cards). Cards sit in the §4 grid — 3 per row at reference — separated by `--sp-64` of specified emptiness; there is no card background (the page is the ground; rules, not boxes, divide).

**Motion spec.** Cards enter by etching: as a row crosses the 82% line, each card's top rule draws left-to-right (300ms, `--ease-etch`, 90ms stagger across the row) and its figure is measured (§6.3 runs its own timeline). The card body is never hidden — the rule draws *above* fully printed content (the pre-state is only the rule's dashoffset). Hover: the card's registration outline prints in `--trace` and §6.6's crosshair readout becomes available on the figure; the card does not lift, scale or shadow — objects on a bench do not levitate when inspected.

**Choreography timeline.** (A 3-card row.) 0ms row crosses 82% · 0/90/180ms rules draw · §6.3 sweeps run per figure on their own triggers · ~740ms row fully admitted.

**State matrix.** *Rest:* complete printed card. *Hover/focus:* trace outline + readout availability; the whole-card link shows the theme's focus outline on keyboard focus. *Sealed:* §6.7 state in the dock; the card's certificate line exists in the footer. *Out of service:* a real state for real catalogues — an instrument withdrawn from service prints its figures struck through with an etched line and the line `WITHDRAWN FROM SERVICE · DATE` — the card remains (records are kept), the link is removed. *Disabled:* static cards, all content, docks empty. *Touch:* tap = navigate (the figure's tap-inspect of §6.6 yields to the card link: on touch, the first tap on the *figure only* inspects; taps elsewhere navigate — the distinction is printed in the build notes so two builders implement the same card).

**Content-merge.** The three figures are the product's certified data; the application note is written in §12's bench register; the seal dock wires the listing into §6.9's certificate. A card with marketing copy instead of figures is a §9 failure, caught by lint (a card must contain exactly three `dd` values with units).

**Breakpoints.** ≥1200px: 3 per row. 768–1199px: 2 per row. <768px: 1 per row, figures in a 3-column mono strip under the name (the data survives the layout), dock 40px. Rule-draw stagger is per row at every size.

**Edge cases & failure modes.** Long instrument names (real ones are long): two lines at 28px, then the figures — the card grows; cards in a row are not equalised (a bench is not a grid of identical boxes; row alignment is by top rule). Missing figure (a product without a certified uncertainty): the dd prints `NOT YET CERTIFIED` — an honest gap in the data, never a borrowed number. Many cards: pagination is the vernier pattern (§11), and each page of the catalogue is a "bench" with its own bench number.

**Fallback & watchdog.** **Watchdog: 1 000ms** — rules snap drawn if the loop stalls (§6.3's own watchdog covers figures). No-JS: complete cards.

**Reduced motion.** Rules printed, figures admitted without sweep (§6.3's variant), no stagger. Cards are fully themselves, still.

**Accessibility.** The whole-card link uses the stretched-link pattern with the instrument name as the link text (never "click here"); the seal button is a separate focus stop after the link. The figures' `<dl>` is read as data. Withdrawn cards are `aria-disabled` regions with the withdrawal as text. Contrast per §2 throughout; the trace outline is 8.27:1 against the ground.

**Performance & mobile variant.** Rule draws are dashoffset on one path per card; figures per §6.3. A 9-card page: ≤0.5ms/frame during entry, zero at rest. Mobile: single column, same nodes.

**Tokens.** `--etch`, `--hairline`, `--trace`, `--plat-deep`, `--lab-deep`, `--ease-etch`, `--sp-64`, `--card-dock: 44px`.

### 6.13 Calibration request form (the conversion)

**What & why.** The theme's conversion section is a calibration request, presented as what it actually is: an application for a certificate. The form lives inside the certificate border (§4's third licensed enclosure), its fields are ruled lines with mono labels and *units*, and on submission it does not say "Thanks!" — it issues a certificate number, derived arithmetically from a count printed on the page: the form's preamble prints `CERTIFICATES ISSUED THIS YEAR: 1 137` (record R6), and the visitor's confirmation reads `YOUR REQUEST IS CERTIFICATE No. 1 138` — the next number in the book, because theirs is now in the book. The confirmation line also appends to the footer certificate (§6.9), like a seal. It merges with content because the conversion *is* the lab's real transaction, and its confirmation obeys the theme's law: the number is not generated, it is *taken* — from the printed count, by addition, in the open.

**Structure.** A `<form>` in the certificate border: preamble (the printed count R6 + what happens next, in bench register), four fields — Instrument (text, with example), Serial No. (text, mono), Quantity to calibrate (number, unit `INSTRUMENTS`), Requested turnaround (select: `STANDARD 10 DAYS` / `EXPEDITED 5 DAYS` — real options with real consequences, priced in the client's data) — a declaration checkbox (`I DECLARE THIS INSTRUMENT WILL BE PRESENTED AS DESCRIBED`), and the submit button: a filled `--trace` block reading `SUBMIT FOR CERTIFICATION`. The confirmation replaces the form *in the same border* (the border never moves): a certificate block with the issued number, the submitted values restated as measured facts, and the line `A COPY HAS BEEN FILED IN THIS PAGE'S CERTIFICATE ↓`.

**Motion spec.** Field interaction: the active field's ruled line etches from `--hairline` to solid `--etch` (160ms) and its label's mono caps turn `--trace`; no floating labels (labels in a laboratory are printed, they do not perform). Validation: on submit, each field is *checked* in order — a crosshair (§6.6's mark) prints beside each valid field (120ms stagger), and an invalid field's rule turns `--seal`— no: red is rationed (§2 census) — an invalid field's rule doubles (two etched lines) and its error prints beneath in `--etch` mono: `SERIAL No. REQUIRED — AN INSTRUMENT WITHOUT A NUMBER CANNOT BE CERTIFIED`. On success: the form cross-fades to the confirmation over 300ms `--ease-settle`, and the certificate number counts dead-stop from 1 137 to 1 138 (the increment made visible — one count, honestly small: a 400ms two-step count, `1 137 → 1 138`, no thousands-sweep theatre for an increment of one).

**Choreography timeline.** Submit: 0ms fields check in order (120ms stagger) · errors print at their field's check beat · success path: last check +100ms → 300ms cross-fade → confirmation printed, number steps 1 137 → 1 138 over 400ms · footer line appends at the fade's end.

**State matrix.** *Rest:* the full form, preamble count printed. *Editing:* field states as above; entered values persist through validation errors (paperwork is not shredded for a mistake). *Invalid:* doubled rule + mono error per field; focus moves to the first invalid field; the error is also the field's `aria-describedby`. *Submitting:* button disables and reads `MEASURING…` for the (simulated or real) round trip, capped by the watchdog below. *Confirmed:* the certificate block; the form is gone from the tab order; a `REQUEST ANOTHER` text link resets to a fresh form whose preamble count now prints 1 138 — the book has moved on, and a second request would be No. 1 139 (the count is state, kept client-side for the session and printed identically in §6.9's filed copy). *Disabled (no JS / form endpoint down):* the form still posts to its endpoint by native submission; the confirmation page is the same certificate block server-rendered — the ceremony is an enhancement of a working form, never the form itself.

**Content-merge.** The issued number's derivation is printed on the page (preamble + confirmation show the arithmetic); the filed copy lands in §6.9; the turnaround options are the lab's real service levels. Nothing about the conversion is decorative: remove the motion and a visitor can still request calibration and receive a numbered certificate — which is precisely the standard the theme sets for every element.

**Breakpoints.** ≥1200px: two-column field grid inside the border (Instrument + Serial paired, Quantity + Turnaround paired). 768–1199px: single column, border retained. <768px: single column, fields full-width at 17px (no iOS zoom), the preamble count stays at the top — the derivation must remain visible at the moment of submission on every device.

**Edge cases & failure modes.** The count is contested state: two visitors in the same session (a shared kiosk) — the session count is per-browser and the confirmation prints `No. 1 138 (THIS TERMINAL'S COPY)` if a second request follows, an honest scoping of the claim. Endpoint failure on submit: the form prints `REQUEST NOT FILED — NETWORK FAULT · YOUR ENTRIES ARE KEPT ABOVE` and retains all values; no certificate number is shown (an unissued number must never print). Quantity 0 or negative: invalid, error in bench register (`QUANTITY 0 — THERE IS NOTHING TO MEASURE`). Extremely long serial numbers: mono field scrolls, never wraps into the label.

**Fallback & watchdog.** **Watchdog: 2 500ms** on the submitting state — past it, the form declares the network fault state above rather than spinning (the theme has no spinners, §11; a measuring state that never resolves is a broken instrument and is labelled one).

**Reduced motion.** No cross-fade, no count step: the confirmation prints with No. 1 138 already set; field checks print instantly. The arithmetic — the content — is untouched.

**Accessibility.** Real `<label>`s, `aria-describedby` errors, `aria-invalid` on failed fields, focus management to first error and to the confirmation heading (`tabindex="-1"`) on success. The confirmation is announced via `role="status"`. Targets ≥44px; the declaration checkbox is a real checkbox at 20px with a 44px label target. Error text `--etch` 15.34:1 (never red, never grey).

**Performance & mobile variant.** The form is static HTML; the ceremony is a handful of class changes and one small count. Negligible cost at all sizes. Mobile: native form behaviour preserved (enter key submits from the last field per platform convention).

**Tokens.** `--trace`, `--etch`, `--hairline`, `--plat-deep`, `--lab`, `--ease-settle`, `--ease-etch`, plus record R6 (§6.17).

### 6.14 The chain of traceability (the drawn argument)

**What & why.** Metrology's central idea, drawn: an unbroken chain of comparisons from the SI definition of the metre down to the visitor's own bench instrument, each link labelled with its uncertainty, each uncertainty larger than the one above — `DEFINITION ±0` → `KEY COMPARISON ±0.0002 MM` → `STANDARD No. 9 ±0.001 MM` → `WORKING STANDARD ±0.005 MM` → `YOUR BENCH ±0.02 MM` (record R9: a declared ×5 series). As the visitor scrolls, an etched line draws itself down the chain, node by node; at each node the uncertainty prints. It merges with content because it is not an illustration *of* the site's claim — it *is* the claim, in the only form that can be checked: a chain whose every link is named and numbered. A calibration business that cannot show this chain has nothing to sell; the theme draws it as a scroll ceremony so the visitor *travels* the traceability they are buying.

**Structure.** A vertical SVG spine (2px `--etch`) with five node stations — each a small etched square (the gauge-block glyph) — beside which a ruled block carries the node's name (Inter 600), its custodian line (mono: who holds this link), and its uncertainty (mono, large). The draw is a `stroke-dashoffset` scrub on the spine plus per-node etch-ins. All five uncertainties are printed in the HTML at rest; the record (§6.17) holds the series and §10's audit checks the ×5 progression arithmetically — a chain with a wrong ratio fails the build like a wrong sum.

**Motion spec.** Scrubbed to scroll over the section's own height (`--ease-gauge` via the shared lerp): the spine draws from node 1 to node 5 as the section traverses the viewport centre band; each node, when the spine reaches it, etches its square (160ms) and its uncertainty counts dead-stop from the previous node's value to its own (§6.5's machinery at 500ms per node — the growth of uncertainty is *counted through*, so the visitor watches precision being spent). Node blocks' rules draw as their nodes etch. The final node's block is styled as the visitor's bench — its custodian line reads `HELD BY: YOU` — and its square is the only node drawn in `--trace`: the chain ends at the reader, in the colour of action.

**Choreography timeline.** (Scrubbed, % of section traversal.) 0% spine at node 1, `±0` printed (the definition costs nothing — it is exact by definition, and the caption says so) · 25% node 2 etches, counts to ±0.0002 · 50% node 3 — Standard No. 9, counts to ±0.001 · 75% node 4, ±0.005 · 100% node 5, ±0.02, the trace square prints; the closing line etches beneath: `EVERY LENGTH ON THIS SITE HANGS FROM THIS CHAIN`.

**State matrix.** *Rest (pre-scroll):* the full chain printed, spine fully drawn, all uncertainties at final values — the argument is complete at rest. *Drawing:* scrubbed as above; nodes ahead of the spine are printed but unetched (their squares are hairline outlines — present, awaiting their link). *Drawn:* full chain, closing line printed. *Scrolled back up:* the spine stays drawn (a chain, once linked, is linked — the ratchet rule of §6.11); node highlights retrace. *Disabled:* the printed chain. *Touch:* identical scrub.

**Content-merge.** The chain's middle node is §6.8's bar and §6.11's table's authority; its values are record R9; its closing line makes the site's every other figure (§6.5's counters, §6.12's cards) a dependent of this section. It is the only element whose removal would falsify the rest of the page — the definition of load-bearing.

**Breakpoints.** ≥1200px: spine at the measure's left third, blocks alternating right (a drawn document). 768–1199px: spine at left 24px, all blocks right of it. <768px: the spine becomes a left rule at 12px, blocks full-width right; uncertainties set at 20px mono (the numbers are the section — they do not shrink below legibility to preserve a layout).

**Edge cases & failure modes.** A client whose real chain has 4 or 6 links: the record declares the count and the series; the SVG generates from the record (nodes are data-driven at build time) — but the ×5 audit becomes a *monotonicity* audit (each link strictly larger than the last), because a chain whose uncertainty shrinks downward is a physical impossibility and the build must say so. Very small uncertainties (a length lab working in nanometres): the mono values print as declared (`±0.2 NM`) — units are part of the record, never normalised away. The section on a short page (about page, §7) may run in its short form: 3 nodes (definition → Standard No. 9 → bench) with a printed note `CHAIN SHOWN ABRIDGED · FULL CHAIN ON THE STANDARD PAGE` — abridgement labelled, never silent.

**Fallback & watchdog.** **Watchdog: 1 500ms** after the section enters — if the scrub has not engaged, the spine snaps fully drawn and all counts land. At rest and no-JS, the chain is complete print.

**Reduced motion.** Full chain printed; no draw, no counting-through. The argument survives intact — it was always an argument, not a trick.

**Accessibility.** The chain is also a real ordered list in the DOM (the SVG is `aria-hidden`; the `<ol>` carries name, custodian and uncertainty as text in order) — a screen reader receives the chain as a chain. Node blocks are list items; the closing line is a paragraph. Contrast: uncertainties `--etch` 15.34:1; the trace square is decorative beside text that carries its meaning.

**Performance & mobile variant.** One dashoffset scrub + ≤5 small counts on the shared loop: ≤0.3ms/frame during traversal, zero at rest. Mobile: same system, single-column geometry.

**Tokens.** `--etch`, `--hairline`, `--trace`, `--plat-deep`, `--ease-gauge`, `--ease-settle`, `--lerp: 0.16`, plus record R9 (§6.17).

### 6.15 Etched plates (image treatment & the licensed tilt)

**What & why.** Photographs in this theme are treated as *etched plates*: converted to a restrained duotone of `--etch` over `--lab` with a fine etched line-screen (an SVG pattern of hairlines at 45°, 3px pitch, 8% opacity) laid over the image, captioned like plates in a proceedings volume — `PLATE IV — THE VAULT, LOOKING NORTH · MEASURED WIDTH 640 PX` (the width supplied by §6.3's admission). And here lives the theme's one licensed tilt: a framed plate, on hover, tilts by **exactly 0.5°** — the original's specified angle — because a plate on a bench is picked up and angled to the light by a stated amount, not "a bit". It merges with content because the treatment is the lab's reproduction standard: the same plate, treated the same way, on every page, its caption carrying its measured admission data — photography filed as evidence.

**Structure.** A `<figure class="plate">` (§6.3's figure, extended): the admitted image, an overlay `<svg>` with the line-screen `<pattern>`, the etched double-rule frame, and a caption block (plate number in mono, title in Inter, measured line from §6.3's readout). The duotone is applied at asset-build time (the served image is already duotone — no CSS filter at runtime, so no per-frame cost and no filter-support failure mode); the line-screen is the only runtime layer. The tilt applies to the frame group (image + screen + frame together — the *plate* tilts, never the image inside its frame, which would be a crop error performed as a flourish).

**Motion spec.** Tilt: on hover (fine pointer), the plate rotates to 0.5° over 300ms `--ease-settle`, pivoting on its bottom-left corner (a plate is lifted by one corner); on leave, returns to 0.0° over 300ms. The angle is a token (`--plate-tilt: 0.5deg`) — a build that "improves" it to 2° fails §10's token audit. The line-screen does not move (a screen that swims is a moiré generator). Plates are *never* in the §6.6 measured set while tilting — the disjoint-set rule of §6.6: a plate's §6.3 admission happens flat, and its readout is taken flat; the tilt is a viewing courtesy after measurement, and §6.6 simply does not arm on plates (their dimensions were already published by §6.3 — inspection would be a second measurement of a published value).

**Choreography timeline.** Hover: 0ms intent (120ms, §6.6's grammar) · 120–420ms rotation 0 → 0.5° · hold while hovered · leave: 300ms return to 0.0°. No other beats; a plate has one gesture.

**State matrix.** *Rest:* flat plate, full caption. *Hover:* tilted 0.5°, held. *Focus:* plates are not focusable unless linked; a linked plate shows the trace outline at 0° (keyboard users get registration, not tilt — tilt without a pointer's intent is motion without a reader). *Active/touch:* no tilt on touch (no hover to hold it); tap follows the link if any. *Scrolled-past:* flat. *Disabled:* flat plate, caption complete. The tilt has no memory — it is never a state the page is *in*, only a courtesy while a hand is on the plate.

**Content-merge.** Plate numbers are sequential across a page and cited by the text (`AS PLATE IV SHOWS`) — the plates are part of the document's reference system, like figures in a paper. The duotone + screen make photography from any source sit inside the theme's material world (a colour photo dropped raw into this theme is §9's loudest failure). The measured caption ties each plate back to §6.3's procedure.

**Breakpoints.** ≥1200px: plates at their measured widths in the text column or full-measure for hero plates. 768–1199px: same, tilt retained (fine pointers exist here). <768px: plates full-column-width; **no tilt** (touch-first context; the gesture's precondition is absent) and the line-screen pitch loosens to 4px (fine screens alias on small, dense displays — the pattern adapts, the treatment remains).

**Edge cases & failure modes.** Images that must stay colour (a client's product whose colour is its identity): the theme's answer is a printed exemption — the plate caption gains `REPRODUCED IN COLOUR BY EXEMPTION` and the frame gains a third hairline. Exemptions are labelled, rare (≤1 per page, §10 census), and never silent — the moment colour enters unlabelled, the material world breaks. Dark photographs: duotone mapping is done at build with the plate's levels checked against the `--lab` ground so a night photograph does not become a black rectangle; the build pipeline fails plates whose mean luminance after mapping falls outside the declared band. Screen pattern over faces: portraits are discouraged by the theme (§1's world has instruments, not personalities); if used, the screen pitch over the plate is unchanged — the treatment does not negotiate.

**Fallback & watchdog.** The served asset is final (duotone baked), so there is no runtime treatment to fail. **Watchdog: 300ms** — if the tilt transition is interrupted (pointer leaves mid-tilt, loop stall), the plate is set to the nearer of 0° / 0.5° by state, never left at an unlicensed angle like 0.23°: in this theme even an accident must resolve to a specified value.

**Reduced motion.** No tilt, ever. The plate is flat, screened, captioned — complete.

**Accessibility.** Alt text describes the photograph's content (the treatment is not the content); the line-screen overlay is `aria-hidden` and pointer-transparent. The caption's measured line duplicates §6.3's text pattern. Tilt is hover-only and conveys nothing — no information is angle-dependent.

**Performance & mobile variant.** Zero runtime image cost (baked duotone); the screen pattern is a tiny repeating SVG (GPU-cached); the tilt is one transform on one node. Mobile: no tilt, looser screen — cheaper still.

**Tokens.** `--etch`, `--lab`, `--hairline`, `--plat-deep`, `--ease-settle`, `--plate-tilt: 0.5deg`, `--screen-pitch: 3px`, `--screen-pitch-sm: 4px`.

### 6.16 Re-verification (page transition & the unetched plate)

**What & why.** Moving between pages in this theme is a *re-verification*: the outgoing page's certificate border (§6.9) holds while the incoming page's border draws itself into exact alignment over it — same inset, same double rule — and only when the two registrations coincide does the content swap. The metaphor is the practice: a document is not replaced until its successor is checked against it. Loading states follow the same law: content that has not arrived is shown as an **unetched plate** — the certificate border and the mono labels printed, the plate area blank `--lab-deep` with the line `AWAITING ETCHING` — because in this world a placeholder is a form not yet filled, and it should look like one, not like a shimmering ghost of content it is pretending to be. It merges with content because the border it aligns is the page's own certificate frame (§6.9/§4): the transition literally checks the new page against the old page's standard before admitting it.

**Structure.** The transition is a same-document view-transition (or SPA route swap) choreographed in CSS: both pages share the `.cert-frame` geometry (identical inset tokens), the outgoing frame is snapshotted in place, the incoming frame's double rule draws (dashoffset, 260ms `--ease-etch`), a registration crosshair at each corner prints as its corner aligns, and the content cross-fades 120ms at the moment all four corners register. The skeleton is a server-rendered block: border + section label + `AWAITING ETCHING` + the *declared* dimensions of the coming content (`PLATE 640 × 400 PX — DECLARED`), so the layout the skeleton reserves is the layout the content will occupy (the declaration is §6.3's paperwork, reused).

**Motion spec.** Full transition budget 480ms: 0–260ms incoming border draws · corners register at their draw beats (top-left 60ms, top-right 130ms, bottom-right 200ms, bottom-left 260ms) · 260–380ms content cross-fade · 380–480ms outgoing frame fades to nothing. If the incoming content is not ready at 480ms, the frame holds with its unetched plate and the line `ETCHING IN PROGRESS — CONTENT NOT YET ADMITTED` — the frame never lies about containing something it doesn't. Back/forward navigation uses the identical ceremony reversed in direction (the draw runs counter-clockwise) — direction encodes history, a small true thing.

**Choreography timeline.** As above; the invariant is that the swap beat (content fade) never precedes the fourth corner's registration.

**State matrix.** *Rest:* a complete page in its frame. *Transitioning:* as above; the outgoing content remains readable until the swap beat (never a blank flash — a document is on the desk until its replacement is verified). *Loading (cold navigation):* the frame + unetched plate print within 100ms (they are server-rendered shell), content etches in per-element as it arrives (each element's own admission: §6.3 for images, rule-draws for sections). *Failed load:* the plate's line becomes `CONTENT NOT RECEIVED — THE FRAME REMAINS` with a retry link; the frame, nav and footer are fully functional — a failed page in this theme is a form with a missing enclosure, not a dead end. *Disabled (no JS / no view-transitions API):* plain navigation, full page loads, no ceremony — the site is a set of documents and behaves as documents do. *Touch:* identical.

**Content-merge.** The aligned object is the certificate border that §6.9 signs and §6.13's form lives in — one frame grammar for arrival, conversion and certification. The skeleton's declared dimensions are the same declarations §6.3 measures against, so a skeleton that reserves the wrong size produces a *measurable* discrepancy at admission — the system catches its own lies.

**Breakpoints.** ≥1200px and 768–1199px: full ceremony. <768px: the border draw shortens to 160ms and the content fade to 80ms (a phone's desk is smaller; the check is not skipped, it is brisk), corners still register in order. Skeleton geometry identical at all sizes (the frame is the frame).

**Edge cases & failure modes.** Rapid successive navigations: a second navigation during a transition cancels to the newest target — the frame holds, the draw restarts for the new page; two swaps never queue (documents are not stacked). Extremely fast loads (cached page): the ceremony still runs its 480ms — no, it does not: if content is ready before the draw completes, the draw *accelerates* to finish in the remaining content-ready time, minimum total 240ms — the check is performed, at the speed the facts allow; a ceremony that delays ready content is theatre, and §9 names it. Browser without view-transitions: a class-based fallback performs the same beats with fixed-position frame clones; if that fails, plain navigation (above).

**Fallback & watchdog.** **Watchdog: 900ms** — if registration has not completed (API fault, stalled draw), the swap happens unceremoniously and the frame prints complete. A transition may never hold a visitor hostage; the certificate serves the reader, not the reverse.

**Reduced motion.** No draw, no fade: instant navigation (the browser's default), skeleton plates still used for loading (they are information, not motion). Borders print complete on arrival.

**Accessibility.** Route changes move focus to the new page's `<h1>` (or the skip target) and announce the page title via the document title + an `aria-live` route announcer used only for SPA swaps. The transition is visual only; the unetched plate's text (`AWAITING ETCHING`, declared dimensions) is real text a screen reader can read — loading state is content here, not a spinner's silence. Focus is never inside the outgoing page at swap time (it is moved at the swap beat, not before).

**Performance & mobile variant.** The frame clone is 4 rules + 4 marks; the draw is dashoffset. Skeleton blocks are static HTML with a background colour — zero animation cost while waiting (no shimmer loop exists in this theme, anywhere, §11). Mobile: shorter beats, same nodes.

**Tokens.** `--etch`, `--hairline`, `--lab-deep`, `--plat-deep`, `--ease-etch`, `--transition-dur: 480ms`, `--transition-min: 240ms`, `--frame-inset: 4px`.

### 6.17 The Standard Record (the page's declared figures)

**What & why.** Every theme at 50x has a record; this theme's record is its soul, because the theme's law (§1) is that every figure traces to a measurement or to *this table*. The Standard Record is a declared data block — in the build, a single `record.json` (or front-matter object) from which §6.1's caption, §6.2's scales, §6.5's counters, §6.9's certificate, §6.13's count and §6.14's chain are all *generated or audited*. It is also printed on the site itself, on the Standard page, as a ruled table any visitor may inspect: the bureau publishes its constants. It merges with content because it is not an implementation detail — it is the theme's constitution, and printing it is the difference between a site that *looks* rigorous and one that *is*.

**Structure.** A table of record entries: key, value, unit, source (where the figure comes from — a definition, a count, a measurement campaign), and the elements that print it. The reference build's record:

| Key | Value | Source | Printed by |
|---|---|---|---|
| R1 | 1 000 graduations = 1 000 mm | The SI definition, enacted | §6.1, §6.5, §6.8 |
| R2 | Page length 6 400 mm · 9 sections (home) | The build's declared geometry | §6.2 |
| R3 | 4 812 instruments certified, 2025 | The bureau's annual count | §6.5 |
| R4 | 20.0 °C ± 0.1 °C reference temperature | Laboratory condition log | §6.5 |
| R5 | ±0.5 px — this page's uncertainty | The theme's declared screen tolerance | §6.4, §6.5, §6.9 |
| R6 | 1 137 certificates issued this year | The certificate register | §6.13, §6.9 |
| R7 | The bar: 1 000.0 mm between fiducial lines | R1, in metal | §6.8 |
| R8 | Build date + 1 year = next calibration due | The build pipeline | §6.9 |
| R9 | Chain series ×5: 0 · 0.0002 · 0.001 · 0.005 · 0.02 mm | The bureau's chain of comparisons | §6.14, §6.11 |

**Motion spec.** The record, as printed on the Standard page, does not animate — constants do not perform. Its *consumers* animate (§6.5's counters land on R3, §6.14's counts step through R9), and the record table itself is admitted with the plain rule-draw of §4 sections. One licensed behaviour: on the Standard page, each row's "printed by" cell links to the element, and hovering a row prints §6.6's crosshair in the row's margin — the record can be inspected like anything else in the building.

**Choreography timeline.** None of its own. (Stated explicitly so no implementer invents one: a constants table with a choreography timeline is a constants table that has misunderstood itself.)

**State matrix.** *Rest:* the table, complete. *Stale:* if the build's record is older than its review date (the record carries one, like everything in the building), the Standard page prints `RECORD DUE FOR REVIEW — FIGURES STAND AS LAST VERIFIED` above the table — figures are never silently stale here. *Contested:* a figure found wrong in production is not quietly edited: the record keeps the old value struck through with the corrected value beside it and a dated note (the §6.5 correction grammar, applied to the constitution itself) until the next build. *Disabled:* the table is static HTML; the build-time generation it feeds is a pipeline concern, not a runtime one.

**Content-merge.** This element *is* the merge: it is the single source that §6.1–§6.16 draw from, and §10's figure audit is a mechanical comparison of the rendered pages against it. A theme element that prints a number not in the record is not a style error; it is a constitutional violation, and the build fails.

**Breakpoints.** The printed table: ≥1200px five columns; 768–1199px four (source folds under value); <768px stacked rows. The record *data* is identical at every size — constants do not have breakpoints.

**Edge cases & failure modes.** A client who cannot supply a figure (a young lab with no annual count yet): the record entry is declared as `NOT YET ESTABLISHED` and every consumer prints exactly that (§6.5's counters refuse unestablished values and print statically) — an honest gap in the constitution, never a plausible invention. Record drift between pages (a hand-edited page diverging): the audit (§10) compares rendered output to the record at build time, so drift is a build failure, not a production surprise. Two records (multi-site bureau): each site declares its own record and prints its own key prefix — records are never shared silently.

**Fallback & watchdog.** The record is build-time data and static print; it has no runtime to fail. Its watchdog is procedural: §15's build order places the record *first* (step 1) and §10's audit *last*, so a build cannot ship pages whose figures outran their constitution.

**Reduced motion.** Nothing to reduce. The table prints.

**Accessibility.** A real table with caption (`The Standard Record — every figure on this site, and where it is printed`), header cells, and text values. The struck-through correction state uses `<del>`/`<ins>` semantics, not just styling.

**Performance & mobile variant.** One static table; the build-time generation it drives *saves* runtime cost (values are baked, not fetched). No mobile variant beyond the table's responsive form.

**Tokens.** `--etch`, `--plat-deep`, `--hairline`, plus every record key R1–R9 as build-time constants (`--record-r1` … exposed to CSS only where an element legitimately needs the value as a number, e.g. §6.2's `--page-length-mm`).

### 6.18 Out of tolerance (the 404)

**What & why.** The 404 in this theme is a failed measurement report. The page sought was measured against the site's register and **not found within tolerance**: the report prints the requested path as the object, `NOT FOUND` as the reading, and the register's nearest entries as the *closest measured values* (the three real pages whose paths are nearest the requested one — computed from the sitemap, printed with their distances in the register's terms). It merges with content because it refuses the genre's jokes (no lost-in-space puns in a bureau) and instead does the lab's actual job on a missing object: it files a report, states the discrepancy, and points to the nearest known quantities — which happen to be exactly what a lost visitor needs.

**Structure.** A certificate-bordered block (§4's frame, borrowed for the report — the fourth enclosure on this page type only, licensed because a report is a certificate of a negative result): object line (the requested path, mono, as entered), reading line (`NOT FOUND WITHIN THE REGISTER`), the discrepancy note (`THE REGISTER CONTAINS N ENTRIES` — N from the build's sitemap, record-audited), the three nearest entries as ruled links with their section numbers (§6.10's grammar), and a closing line: `IF THIS OBJECT SHOULD EXIST, ITS ABSENCE HAS BEEN LOGGED` — with the log being real where the platform supports it (the 404 is recorded server-side; the claim is only printed where the build wires the log, §15 step 12).

**Motion spec.** Almost none, specified as such: the report prints complete; the border draws once on arrival (260ms, §6.16's grammar, if the visitor arrived by in-site navigation — a cold arrival prints the border whole). The nearest-entries' rules draw with the §4 section etch. That is all. A 404 that performs is a 404 apologising with theatre; this one files its report and stands still.

**Choreography timeline.** Arrival: border (if drawn) 0–260ms · report already readable from 0ms (text never waits for the border) · still thereafter.

**State matrix.** *Rest:* the report. *Near miss* (the path differs from a real page by one character — a typo the register can prove): the report's reading line adds `NEAREST REGISTER ENTRY DIFFERS BY ONE CHARACTER` and the first link is that page, labelled as the probable object — the lab suggests, it does not silently redirect (a silent redirect destroys the measurement; the visitor is told what was found). *Truly absent:* the standard report. *Disabled:* identical, minus the border draw. There is no interactive state; the links are links.

**Content-merge.** The register it cites is the site's real sitemap; the nearest entries are computed, not curated; the log claim is wired or not printed. Even the error page obeys the law: every figure on it (N entries, the distances implied by ordering) traces to the register.

**Breakpoints.** ≥1200px: report in the measure, nearest entries as three ruled rows. 768–1199px: same, rows full width. <768px: same, stacked; the requested path wraps in mono (never truncated — the object is named in full on its own report, however long its name).

**Edge cases & failure modes.** A requested path that is long or hostile (injection attempts in the URL): the path is printed *escaped as text*, always — the report quotes the object, it never executes it. A 404 for an asset (missing image): not this page — assets fail as §6.3's `OBJECT NOT RECEIVED` within their figure, keeping the report page for documents. Repeated 404s in a session: the report does not escalate, apologise harder, or change — a register does not get embarrassed; the third identical report is identical.

**Fallback & watchdog.** The page is static; **watchdog: not applicable beyond §6.16's border rule (900ms global)** — if the border draw stalls it prints whole. Stating "not applicable" here is itself the spec: no implementer should invent a loading state for a page whose entire content is one report.

**Reduced motion.** Border prints whole. Identical otherwise.

**Accessibility.** The report is the page's `<h1>` region text (`PAGE NOT FOUND WITHIN TOLERANCE` as the heading, the report beneath); status is conveyed in words, not colour (there is no red anywhere on this page — a missing page is a measurement result, not an alarm). Links are descriptive (`02 · SERVICES — CALIBRATION` — never "click here"). HTTP status is a real 404.

**Performance & mobile variant.** A static page, the lightest on the site; the nearest-entry computation is build-time for known patterns and a tiny runtime edit-distance over the sitemap (≤ a few hundred entries, <1ms) where the platform serves dynamic 404s. Mobile: same page, stacked.

**Tokens.** `--etch`, `--plat-deep`, `--hairline`, `--trace`, `--ease-etch`, `--frame-inset: 4px`.

## 7. Page application map

**Home.** The full ceremony: §6.10 masthead, §6.1 dividing metre hero (record R1/R2 declared for this page: 6 400mm, 9 sections), §6.5 counter bank (R3, R4, R1, R5), §6.14 chain (full five links), §6.12 a bench of three featured instruments, §6.11 a shortened spec table (6 rows — the full table lives on the Standard page), §6.13 the request form, §6.9 certificate footer. The home page is the bureau's public room: every system appears once, in order, like instruments laid out for an inspection.

**Listing (instruments / services).** Benches of §6.12 cards, paginated by the vernier pattern (§11): each results page is a numbered bench, its count printed (`BENCH 2 OF 5 · 9 INSTRUMENTS PER BENCH`) — counts from the catalogue data, audited like any figure. Filters are ruled mono selects labelled as *sorting the register*, never playful chips. §6.3 admits every card portrait; §6.2's vernier reads the listing's own declared length (the record is per-page-type: listing pages declare their sections and length in their own record extension).

**Detail (one instrument).** The instrument's own certificate page: name and portrait (§6.3, measured large), its full §6.11 spec table (all rows, pinned), its place in the chain (§6.14 short form — the three links from Standard No. 9 down to *this* instrument, its own uncertainty as the final node: the chain made personal), its service history as a ruled log (dates, certificates issued, next due — real client data), and §6.13's form pre-addressed to this instrument (the Instrument field pre-filled and printed as such). The detail page is where the theme's systems converge on a single object.

**The Standard page (about the bureau).** The institution's self-description: §6.8's bar lives here in its fullest form if it is not on Home (the bar exists on **one** page of the site — the census is per-site for the bar, §10), §6.17's record printed in full, §6.14's full chain, the laboratory conditions (R4 and its log), and the bureau's own certificate history. This is the page the theme was born for; other pages borrow its authority.

**Contact / request.** §6.13 at full size, plus the bureau's bench locations as ruled blocks (address, hours — printed as data with units where honest: `RESPONSE WITHIN 2 WORKING DAYS` is a figure and must be one the bureau keeps). No map embed (a map is an unmeasured picture in this theme; the address is text, and a `PLATE` (§6.15) of the building may accompany it).

**404.** §6.18, as specified. **Search results** (if the site has search): a register extract — ruled rows, each result's section number and a one-line measured description (the line from its own record or its first certified figure); no thumbnails except §6.15 plates where the result is an instrument. **Checkout equivalents** (paid calibration bookings): the theme routes payment *out* — the request (§6.13) issues the certificate number, and payment, if any, happens on the provider's own pages linked plainly as `PAYMENT IS HANDLED BY [PROVIDER] — THIS CERTIFICATE RECORDS THE REQUEST, NOT THE PAYMENT`. A theme whose law is traceability does not dress a third-party checkout in its own certificate border; honesty about the boundary is the design.

## 8. Worked examples

### 8A. The hero — "The metre, enacted" (home page, top)

**Build.** §6.10 masthead (full letterhead). Below it, inside the certificate border (§4): the mono label `SECTION 01 — THE UNIT`; the §6.1 SVG metre at 1 000px; the headline `Every length you trust was checked against this line.` — two lines, set at 64px Inter 600, its container exactly 1 000px wide so the second line's measure *is* the metre; beneath, the lead paragraph (21px) stating the bureau's purpose in bench register; the caption `1 METRE · 1 000 GRADUATIONS · SCALE 1 PX = 1 MM` under the rule.

**Scroll/timeline.** Load: masthead static; border printed. +200ms §6.1's sequence runs (baseline 800ms, divisions cascade centre-out, headline rises from behind its rule at 1 900ms, caption at 2 200ms). The visitor's first scroll: §6.2's jaw is already reading (`SECTION 1.x`); §6.4's crosshair sits at section 1's corner, first drift at +6s. Nothing else moves. The hero's whole performance is one definition, enacted once, then stillness — the stillness is the brand.

### 8B. Mid-page — the spec section with the bar (Standard page)

**Build.** Section label `SECTION 05 — TOLERANCES`. §6.8's bar at the head (matte, fiducial lines quiet). §6.11's table beneath: 11 rows — the chain's quantities (length, and the worked instrument's range/resolution/uncertainty rows drawn from R9's family) with nominal / tolerance / measured / verdict; one row `AT LIMIT` (the 0.02mm bench row, measured exactly at its limit — printed as such, the section's honest row).

**Scroll timeline.** Bar centre crosses 60%: the sheen passes once (2 800ms), fiducial lines deepen to `--etch`. Scroll continues: the stage pins at 12% viewport; graduations etch scrubbed 0→100 as the 11 rows pass under inspection (~9% of pin range per row), each row ruling to `--lab-deep` with its margin crosshair as it centres; the AT LIMIT row's verdict prints in `--etch` (never red). Release: 100 ticks etched, table complete, §6.14's chain begins below — the visitor has just read tolerances under the metre, and now walks the chain those tolerances hang from. Sequence is argument.

### 8C. Conversion — the calibration request (home page, section 08)

**Build.** §6.13's form in its certificate border: preamble `CERTIFICATES ISSUED THIS YEAR: 1 137 · YOURS WILL BE No. 1 138` — the derivation stated *before* the ask, because in this theme the terms print first. Fields per §6.13; the worked visitor enters a dial gauge, serial `DG-2210`, quantity 3, standard turnaround, declares, submits.

**Submit timeline.** Fields check in order with margin crosshairs (4 × 120ms stagger); 300ms cross-fade; confirmation: `CERTIFICATE No. 1 138` with the count stepping 1 137 → 1 138 (400ms), the request restated as measured facts (`INSTRUMENT: DIAL GAUGE · SERIAL DG-2210 · QUANTITY 3 · TURNAROUND: STANDARD 10 DAYS`), the filed-copy line, and — same frame — §6.9's footer gains the line `FILED — CERTIFICATE No. 1 138 · DIAL GAUGE DG-2210`. The visitor scrolls to the foot of the page and finds their own paperwork in the page's certificate: the conversion's proof is not a toast, it is an entry in the register they have been reading all along.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The decorative ruler.** Ticks that measure nothing — a ruler graphic whose graduations don't correspond to the scale, the width, or anything. *Cure:* every scale on the page is generated from the record and reads something real (§6.1, §6.2, §6.11). If a tick doesn't count, it doesn't print.
2. **The bounce.** Any overshoot, spring or elastic anywhere — in this theme it is not a style slip, it is a false measurement performed in public. *Cure:* the five easings of §5, audited by control points (§10).
3. **Invented figures.** "Over 10 000 instruments calibrated!" with a plus sign and no source. *Cure:* the record (§6.17) or silence; approximations wear `±` or don't print.
4. **Fake precision.** `±0.0001 PX` — decimals beyond the instrument's power, precision as costume. *Cure:* figures carry the significant digits of their source (R9's series is the model); the audit checks digit counts against the record.
5. **A second shine.** A glossy button, a gradient hero, a sheen hover — any gleam outside §6.8. *Cure:* the platinum census (§10): `--sheen-*` tokens exist in exactly one rule; gradients elsewhere are build failures.
6. **Red as an accent.** Seal red on a sale badge, an error banner, a hover state. *Cure:* the seal census — red appears in §6.7's stamps and §6.9's one certificate seal, nowhere else; errors are etched double-rules and words (§6.13).
7. **Counters that perform.** Rolling odometers, slot-machine digits, counts that ease *past* the value and settle back. *Cure:* §6.5's dead-stop rule; displayed values are always valid values of the quantity.
8. **Hidden content behind ceremony.** A reveal that can strand an image or a paragraph if a trigger misses. *Cure:* every pre-state is JS-armed over a complete DOM, every element carries its watchdog (§6.x), and §10 drills them.
9. **Generic minimalism.** White space and Inter with the instruments removed — the theme mistaken for "clean corporate". *Cure:* the law (§1). If the page could belong to a bank, the build has failed; the paperwork is the personality.
10. **Filling the whitespace.** A sidebar, a promo block, a newsletter box wedged into the 160mm section gaps "for conversion". *Cure:* the gaps are specified (§4); conversion lives in §6.13's bordered form, where it is *more* credible, not in the margins.
11. **A script-font signature.** A flourish font on the certificate, clip-art seals, a wax-effect badge. *Cure:* the signature is mono type (§6.9); the seal is drawn geometry (§6.7); anything clip-arty fails review by eye instantly.
12. **Numbers in proportional type.** Figures set in Inter, wobbling widths in tables, misaligned decimals. *Cure:* type law 3 (§3) — numerals are mono, everywhere, including inline prose.

## 10. Quality gate

All twelve checks are blocking; a build that fails one does not ship, and the gate is signed by someone other than the builder (§15).

1. **Figure audit.** Every number rendered on every page is extracted and compared against §6.17's record (and per-page extensions): exact match including thin-space grouping and decimals. Any unmatched figure fails.
2. **Easing audit.** Every `cubic-bezier` in the CSS is one of §5's five; a script verifies no curve's output overshoots its target (control-point check). Any spring/elastic keyword fails.
3. **Platinum census.** `grep` for `--sheen-` returns exactly the §6.8 rule set; the bar appears on exactly one page of the site.
4. **Seal census.** `--seal` appears only in §6.7 and §6.9 rules; a screenshot pass confirms no red anywhere else at any scroll position or state.
5. **Watchdog drill.** With the shared loop forcibly stalled, every element reaches its final state within its watchdog budget (§6.1 3 000ms, §6.3 1 200ms, §6.5 2 000ms, §6.9 1 500ms, §6.11 900ms, §6.16 900ms) and no content is stranded — tested with JS-throttling, not by reading the code.
6. **No-JS pass.** With JavaScript disabled, every page is complete: all figures printed, all images present, the form submittable, the certificate filled with its declared (labelled) values.
7. **Reduced-motion pass.** With `prefers-reduced-motion`, no element animates except position-cut updates (§6.2's jaw, §6.11's row highlight); the uncertainty prints directly as ±0.5px (§6.5).
8. **Dead-stop test.** Counters are screen-recorded at 240fps (or frame-stepped): no displayed value ever exceeds its target; the final frame equals the printed string character-for-character.
9. **CLS test.** Sealing (§6.7), measuring (§6.3) and the header collapse (§6.10) produce zero layout shift (docks and frames are reserved); measured CLS for the page < 0.01 excluding the declared header collapse.
10. **Contrast audit.** The §2 pairings as measured; specifically `--plat` sets no text under 24px anywhere (grep for the token in text contexts + visual pass).
11. **Chain audit.** §6.14's uncertainties strictly increase downward and match R9's declared series/ratios.
12. **Certificate truth.** The footer's live width measurement is verified against an independent measurement of the rendered page; the verdict printed is the verdict earned (including `OUT OF SPEC` if that is the truth on some viewport — the gate checks the *honesty*, not the comfort).

## 11. Component inventory

Every component a real site in this theme needs, with its themed treatment. Components the theme refuses are listed with their in-theme replacement — a refusal without a replacement is a gap, and gaps get filled with slop.

- **Primary button.** Filled `--trace` block, `--lab` mono-caps label (`SUBMIT FOR CERTIFICATION`): the colour of action, the register of paperwork. Hover: darkens one declared step (`--trace` at 88% lightness — a token, not a filter). No shadow, no radius.
- **Secondary button.** Etched outline (1px `--etch`), `--etch` label; hover fills `--lab-deep`. Used for `REQUEST ANOTHER`, `RETURN TO THE REGISTER`.
- **Text link.** `--trace`, underlined by a hairline that etches to solid on hover (§6.10's grammar). Visited links turn `--plat-deep` — a link that has been followed is a filed copy, and looks it.
- **Form inputs.** Ruled-line fields (§6.13): mono label above, value in Inter 17px (mono for serials/numbers), the rule doubles on error. No boxes, no floating labels, no placeholder-as-label (placeholders carry *examples*, labelled `E.G.`).
- **Select.** A ruled field with an etched chevron; options are the real service levels with their figures (§6.13).
- **Checkbox / radio.** Drawn squares/circles in `--etch` hairline, checked by an etched cross — a tick drawn by §6.6's crosshair grammar, never a filled blob. 20px box, 44px label target.
- **Spec table.** §6.11's pattern: mono data, ruled rows, verdict column in words. The only table style on the site.
- **Data cell / stat.** §6.5's pattern: label, mono value with unit, source line. Never a bare number in a coloured blob.
- **Badge / chip.** *Refused as decoration.* The theme's equivalent is the **certified mark**: a small etched square + mono text (`CERTIFIED · R9`) printed beside a figure — a claim with a reference, or nothing.
- **Alert.** *No coloured banners.* An out-of-tolerance notice is a ruled block with a doubled `--etch` rule and mono text (§6.13's error grammar); urgency is expressed in words (`OUT OF TOLERANCE — Δ2 PX`), never in red (census, §10).
- **Toast.** *Refused* — nothing floats in a laboratory. Replacement: the **filed line** — confirmations append to §6.9's certificate or print in place (§6.13). If a message has nowhere to file, it is not sent.
- **Modal.** The **certificate viewer**: a certificate-bordered panel (the fourth licensed border use, for documents) used to view a full certificate or the record (§6.17) without leaving the page. It opens by its border drawing (§6.16's grammar, 260ms), closes by Esc/backdrop, and prints completely if JS fails (it is a document — it can also simply be a page, and on <768px it *is* a page).
- **Tabs.** Ruled index tabs: mono labels over a hairline, the active tab's rule solid `--etch` with its section number — §6.10's nav grammar at section scale. Content switches by cut (documents change pages, they do not slide).
- **Accordion.** The **gauge fold**: a ruled row whose etched chevron rotates exactly 90.0° (a specified angle) and whose content is revealed by its bottom rule drawing down — used for the chain's custodian details and FAQ-equivalents (`QUESTIONS OF PROCEDURE`).
- **Pagination.** The **vernier pattern**: `BENCH 2 OF 5` with prev/next as ruled links and page numbers as scale divisions — the current bench's division is etched solid. (§6.12's listings.)
- **Breadcrumb.** The **register path**: `REGISTER / INSTRUMENTS / DIAL GAUGE DG-2210` in mono, each level a link, separators etched slashes — the object's filing path, which in this world is a real concept.
- **Progress.** Only §6.2's vernier (reading) and §6.11's cascade (inspection). No bars, no spinners, anywhere.
- **Spinner / loader.** *Refused.* Loading is §6.16's unetched plate: a labelled blank, with declared dimensions. A site that knows what is coming says so; it does not spin.
- **Skeleton.** §6.16's unetched plate, as above.
- **Search input.** A ruled field in the masthead's compact form, labelled `SEARCH THE REGISTER`; results per §7's register extract.
- **Tooltip.** The **margin note**: hover/focus on a term prints its definition in the margin in mono (`TOLERANCE — THE PERMITTED DIFFERENCE`), §6.6's placement. Terms are defined from the theme's own glossary; a tooltip with a dark bubble is refused.
- **Toggle switch.** *Refused as a widget.* Settings in this world are declared values: a preference is a ruled radio pair (`MOTION: FULL / REDUCED — AS YOUR SYSTEM DECLARES`) that reports the system's state rather than pretending to be a machine part.
- **Card.** §6.12's pattern, the only card.
- **Footer.** §6.9's certificate, the only footer.
- **404 / empty states.** §6.18's report; empty search results print `THE REGISTER RETURNS NO ENTRY FOR "…" · N ENTRIES SEARCHED` — a measurement of absence, with N true.

## 12. Copywriting voice

Two registers, and the page never confuses them. **The Certificate register** — for certificates, records, confirmations, the footer: third person, past tense, passive where honest (`WAS MEASURED`, `IS CERTIFIED`), every claim carrying its figure and its source. **The Bench register** — for body copy, labels, errors, empty states: plain imperatives and short declaratives, present tense, the voice of a technician who respects the reader's time (`PRESENT THE INSTRUMENT AS DESCRIBED`). Neither register ever markets. There are no superlatives in either: a bureau does not have "world-class" anything; it has a chain (§6.14) and the chain is the boast.

**Headline style.** A statement of fact with a figure in it, or a definition. ✓ `Every length you trust was checked against this line.` ✓ `Calibration, with the paperwork.` ✗ `Precision Redefined!` ✗ `The Future of Measurement Is Here` — futures are not measured; headlines here could be read aloud in a standards committee without embarrassment.

**Label style.** Mono caps, quantity-first: `SECTION 04 — TOLERANCES`, `DEPTH 4 096 MM`, `CERTIFICATES ISSUED THIS YEAR: 1 137`. A label that cannot be given a number is given a section number instead.

**Error voice.** Bench register, specific, with the consequence and the remedy: ✓ `SERIAL No. REQUIRED — AN INSTRUMENT WITHOUT A NUMBER CANNOT BE CERTIFIED.` ✓ `QUANTITY 0 — THERE IS NOTHING TO MEASURE.` ✗ `Oops! Something went wrong.` ✗ `Invalid input` (invalid *how*, by how much, against which spec — the theme's errors state the Δ where a Δ exists).

**Empty-state voice.** A measurement of absence: ✓ `THE REGISTER RETURNS NO ENTRY FOR "MICROMETER" · 214 ENTRIES SEARCHED.` ✓ (sealed list, empty) `NO SEALS APPLIED THIS VISIT.` ✗ `Nothing here yet!` — "yet" is a promise; the register makes none.

**Fixed strings (verbatim, never paraphrased).** (1) The uncertainty: `UNCERTAINTY OF THIS PAGE: ±0.5 PX`. (2) The chain's close: `EVERY LENGTH ON THIS SITE HANGS FROM THIS CHAIN`. (3) The form's filed line: `A COPY HAS BEEN FILED IN THIS PAGE'S CERTIFICATE`. (4) The crosshair's log: `RE-VERIFIED · DRIFT 0.5 PX · CORRECTED`. (5) The 404's reading: `NOT FOUND WITHIN THE REGISTER`. A build that rewords any of these has edited the bureau's forms without authority (§10's audit greps them).

**Numbers in copy.** Always with units, always thin-space grouped, always the record's digits (§3's laws). Rounding in prose is forbidden: if the figure is 4 812, the sentence does not say "nearly five thousand" — approximation is what `±` is for.

## 13. Scroll choreography map

The home page, top to footer, in order — every beat, what fires, and what the visitor sees. (Other page types substitute their §7 elements into the same grammar.)

1. **Load.** Masthead printed; hero border whole; §6.1 arms. *Seen:* a certificate, complete, about to demonstrate its first line.
2. **+200ms → 2 400ms.** §6.1 divides the metre; headline sets to measure; caption prints. *Seen:* the unit, defined in public.
3. **First scroll.** §6.2's jaw begins reading (Section 1.x); §6.4's crosshair registers at section 1's corner; its first drift cycle runs at +6s. *Seen:* the page keeping its own instruments running.
4. **Section 02 — the counters.** Cells cross 78%: §6.5 counts land dead; at +2 500ms the uncertainty corrects itself ±2 → ±0.5px. *Seen:* figures arriving like measurements, and one honest correction.
5. **Section 03 — featured instruments.** §6.12's row rules etch; §6.3's jaws measure each portrait; readouts print declared vs measured. *Seen:* objects admitted by procedure.
6. **Section 04 — the chain.** §6.14's spine draws down the five links; uncertainties count through ×5 steps; the closing line etches. *Seen:* the argument the whole site hangs from.
7. **Section 05 — tolerances.** §6.11's stage pins; 100 graduations cascade as 11 rows pass inspection; the AT LIMIT row rules to `--lab-deep`. (On the Standard page, §6.8's sheen precedes this beat — once.) *Seen:* data read under its own ruler.
8. **Section 06 — plates.** §6.15 plates at rest; a hover lifts one by the licensed 0.5°. *Seen:* evidence, handled carefully.
9. **Section 07 — services.** Ruled blocks (§7's contact pattern); nothing animates but rules etching — a quiet bench before the ask.
10. **Section 08 — the request.** §6.13's bordered form; the preamble's count (1 137) already implies the visitor's number. On submit: checks, cross-fade, No. 1 138, and the footer gains its filed line in the same frame. *Seen:* the conversion filed, not celebrated.
11. **Section 09 — the certificate.** §6.9: the width counts to its measured value and earns its verdict; the visitor's seals and filed lines are already in it; §6.4's count stands at however many re-verifications the reading took. *Seen:* the page, signing itself, with the visitor's own paperwork inside the signature block.
12. **Reverse pass.** Scrolling up retraces readings (jaw, highlights) and reverses nothing that was *issued*: divisions stay divided, the chain stays drawn, counters stay landed, seals stay sealed. The page's memory is a ratchet because a register's memory is a ratchet.

## 14. Whole-page performance budget

This theme is deliberately light — its luxury is whitespace and arithmetic, not payload — and the budget says so in numbers.

| Line | Budget (home page) | Notes |
|---|---|---|
| Total transferred weight | ≤ 420KB | Including fonts (subset Inter 400/600 + Plex Mono 400, `font-display: swap` with metric-matched fallbacks so the swap never shifts a measure) |
| Inline SVG (all scales, seals, chain) | ≤ 60KB raw | §6.1's 1 110 ticks dominate; generated at build, gzipped ~14KB |
| JavaScript | ≤ 28KB gz | One shared loop, the state machines of §6.3–§6.7, §6.11, §6.13; no framework |
| Images | ≤ 220KB | Duotone plates (§6.15) compress hard by nature; §6.3's figures eager by distance |
| Frame budget (shared loop) | ≤ 1.6ms/frame | All scrubbed values + active ceremonies; measured on a mid-tier laptop at 4× CPU throttle for sign-off |
| Long tasks | none > 50ms | Tick generation is build-time; nothing parses 1 000 nodes at runtime |
| CLS | < 0.01 | Docks, frames and skeleton dimensions are reserved (§6.7, §6.16) |

**Cut order when the budget is exceeded.** (1) §6.15's line-screen pitch loosens (fewer pattern tiles painted). (2) §6.1's minor-tick cascade becomes the two-step etch (§6.1's own slow-device path) at all sizes. (3) §6.11's cascade drops to 50 divisions with its caption note. (4) Plate images re-encode at lower quality within the duotone band. (5) §6.16's transition shortens to its 240ms minimum.

**Never cut.** The watchdogs (they are the content's guarantee), §6.4's crosshair (cost ≈ 0; cutting it saves nothing and removes the proof), §6.8's single sheen (2 800ms once — the theme's entire luxury spend), any printed figure, and the no-JS completeness of any page. A build that meets budget by removing paperwork has optimised the wrong thing and fails §10 regardless of its numbers.

## 15. Build-order checklist

In sequence; each step is checkable before the next begins.

1. **Write the record first.** §6.17's `record.json` with R1–R9 (and per-page extensions), sourced from the client's real figures. No record, no build — pages written before the record will invent numbers, and invented numbers are the one unforgivable defect.
2. **Build the static page.** Every page complete in HTML: all figures printed from the record, all images present, form submittable, certificate filled with declared values. This static build must pass §10 checks 1, 6, 10, 11, 12 *before any animation exists*.
3. **Lay the tokens.** §2's palette (including the no-dark-mode ruling), §3's two weights + mono, §4's scale and spacing tokens, §5's five easings — as CSS custom properties with the exact names the elements cite.
4. **Etch the furniture.** §6.10 masthead, §4's section grammar, certificate borders, §6.2's static rail (bands from the record).
5. **The shared loop.** One rAF loop, lerp 0.16, the scroll register and section register; §6.2's jaw wired to it. Verify the loop's death leaves every current element complete (watchdog pattern established here, reused by all later steps).
6. **Hero.** §6.1 with its JS-armed pre-state and 3 000ms watchdog; session short-form replay.
7. **Counters.** §6.5, targets read from printed text; the ± correction sequence; dead-stop frame test rigged (§10 check 8).
8. **Admission.** §6.3's caliper on all figures; §6.15's plates (duotone baked in the asset pipeline, with the luminance band check).
9. **Inspection.** §6.6's shared crosshair + readout (with the §6.15 disjoint-set rule), §6.4's crosshair cycle + footer count wiring.
10. **The spec section.** §6.11's pin + cascade ratchet + watchdog unstick; §6.8's bar and its once-per-session sheen, with the census grep added to CI at this step (a second sheen must fail the *build*, not the review).
11. **The chain.** §6.14 generated from R9; monotonicity audit in CI.
12. **Conversion & certificate.** §6.13's form (native submission first, ceremony second), §6.9's live width measurement and seal/filed-line appends; the 404 log wired or its claim removed (§6.18).
13. **Transitions & 404.** §6.16's re-verification + unetched plates; §6.18's report with register-computed nearest entries.
14. **Reduced-motion & no-JS passes.** Full §10 checks 6–7 on every page type; the reduced variants are built here as *variants*, not patched later.
15. **The gate.** §10's twelve checks run end-to-end by a non-builder; the figure audit's output (every rendered number, matched) is filed with the build — the expansion's last act is, fittingly, paperwork.
