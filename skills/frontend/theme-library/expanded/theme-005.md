# Theme 5 — The Colophon (Expanded)

## 1. Concept & world

The Colophon takes the least-read pages of a fine book — the colophon leaf, the errata slip, the printer's mark, the "set in" note, the list of corrections nobody was meant to enjoy — and builds the entire site out of them. Every screen is a leaf. Every section is numbered like a folio. The site's furniture is bibliographic apparatus: running heads, hairline rules, fleurons, catchwords, imprint lines. Nothing on the page is decoration borrowed from the web; everything is borrowed from the back of a book printed with care.

The world is a single quiet room: a vellum page under warm light, set in a serif face with a long memory, annotated in rubric red by a careful hand. The emotional register is *aftermath and honesty* — the part of the book where the maker stops performing and simply states what was made, in what type, in how many copies, and what went wrong (the errata). That honesty is the theme's persuasion engine: a site that publishes its own corrections feels more trustworthy than a site that shouts.

Motion is ink density only. Nothing slides, bounces, scales, or flies. Things become *printed*: they gain ink from a pale impression to full density, the way a letterpress page darkens as the press settles. Stillness is the luxury good here. In a web full of parallax and tilt, a page that refuses to move — and instead deepens — reads as expensive.

**Best-fit sites and audiences**

- Publishers and small presses: catalogues, season lists, "about the house" pages, subscription offers. The audience already reads colophons for pleasure.
- Type foundries: specimen pages, release notes, licence terms. The apparatus (print-run data, leaf counts, folios) maps naturally onto foundry data (glyph counts, weights, version numbers).
- Museums, galleries, and archives: exhibition pages, collection notes, reading-room resources. The theme's restraint flatters objects that carry their own drama.
- Authors, editors, and print-adjacent craftspeople (binders, letterpress printers, paper makers) with a body of work to list plainly and well.
- Any brand whose product *is* the artefact and whose claim is craft: limited editions, numbered runs, small batches with stated quantities.

**When NOT to use it**

- Anything that must feel fast, loud, or urgent: sales events, product launches with countdown energy, gaming, sports, youth entertainment. Ink-density motion cannot manufacture excitement and should not try.
- Data-dense dashboards and tools: the single centered column and apparatus furniture fight against tables, filters, and dense controls. A tool wearing this theme looks like a book pretending to be software.
- Sites whose photography must dominate full-bleed: images here live inside hairline plate borders at column width; a portfolio that needs edge-to-edge imagery should choose another theme.
- Brands without real apparatus to show. The theme runs on facts — edition sizes, dates, places, names of typefaces. If a client cannot supply true colophon-grade facts, the page becomes a costume, and the anti-slop rules in §9 will fail it.

## 2. Palette

Four inks. No gradients anywhere in the theme — a gradient is a photograph of light, and this page is lit evenly, like a reading room. All colour is flat ink on vellum.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--vellum` | `#FAF7F0` | Page ground; the paper itself | ~78% of any viewport | Ground for all text. Against `--ink` the contrast is 15.4:1. Never used as a text colour except on `--ink` plates (rare, see §6.14). |
| `--ink` | `#1E1B16` | Primary text ink; rules at full strength; the printer's mark | ~17% | On `--vellum` 15.4:1 — passes AAA at every size including 11px apparatus. This is the only colour body text may use. |
| `--rubric` | `#A62B1F` | Rubrication: initial letters, underlines, the fleuron ornament, errata markers, the single accent per leaf | ~3%, never more | On `--vellum` 6.9:1 — passes AA for text at ≥14px, so rubric may carry small apparatus text (errata numerals, "corrected" tags) but never body copy. Never set rubric on rubric; never use as a background behind text. |
| `--taupe` | `#9A8F7D` | Quiet apparatus: folio numbers at rest, hairline rules at rest, skeleton bars, secondary notes, disabled states | ~2% as ink, but structurally everywhere (rules/folios) | On `--vellum` 3.2:1 — fails text contrast by design: taupe is *furniture, not reading matter*. Anything the visitor must read (including folio numbers once the page is being read — see §6.2 state rule) must step up to `--ink` or `--rubric`. Taupe text is permitted only for text that is also conveyed another way (e.g. a date repeated in the body). |

**Ink-density scale.** The theme's motion lives on a fifth, virtual token: ink opacity. Text and rules are rendered in `--ink` at graded densities — 55% (first impression), 70%, 85%, 100% (full impression) — implemented as `color-mix(in srgb, var(--ink) X%, var(--vellum))` so the *colour itself* pales rather than the element going transparent (transparency would let the ground texture ghost through unevenly; colour-mixing keeps the impression flat, like under-inked type). All reveal states are specified in these density steps, never in raw opacity, except where an element is genuinely a plate (images), which use opacity because a plate sits *on* the page.

**Dark-mode behaviour.** There is no dark mode, and that is a deliberate, stated position: a colophon leaf is printed on the paper it is printed on. The theme instead ships a *night-reading* variant only if the host product already forces one: ground becomes `#171410` (warm black, the ink's own hue deepened), ink becomes `#EDE6D6` (vellum pulled into text), rubric stays `#A62B1F` but is lightened to `#C0452F` for the dark ground to hold 6.5:1, taupe becomes `#7A7060`. Density steps are preserved exactly (55/70/85/100) so every motion spec in §5–§6 survives the inversion unchanged. If the product has no system dark mode, do not invent a toggle — a book does not have one either.

**Pairing rules (hard)**

- One rubric element per leaf, maximum two if one of them is the fleuron ornament. Rubric is a hand annotation; two hands arguing on one page looks like a markup fight.
- Taupe never touches rubric directly (rule in taupe, fleuron in rubric is the one allowed adjacency — the ornament sits *on* the rule by design, §6.7).
- `--ink` plates (full-bleed black sections) are forbidden. The darkest thing on the page is a line of type.

## 3. Typography

Two faces, no third, no exceptions — a colophon names its types, and this one names two.

**Cormorant Garamond** (display and text serif) — a Garamond revival with high stroke contrast and long ascenders; at large sizes it looks engraved, at text sizes it stays bookish rather than fragile. Weights used: 500 (text), 600 (display and headings). Italic (500) exists for exactly three jobs: the imprint line, errata entries, and foreign/book terms in body copy. Small caps are *synthesised by letterspacing + uppercase at reduced size*, not a font feature, so the apparatus look survives any subsetting.

**IBM Plex Mono** (apparatus) — folios, print-run data, dates, leaf numbers, form labels, footer facts. Weight 400 only; 500 for the folio numeral at its "current leaf" state. Tabular figures are native to the face — counters (§6.8) must use it so digits never reflow as they count.

**Type scale** (root 16px; the column is narrow, so the scale is tight and literary):

| Role | Face / weight | Size | Line-height | Tracking | Notes |
|---|---|---|---|---|---|
| Display (title-page title) | Cormorant 600 | 56px desktop / 40px mobile | 1.04 | -0.01em | Sentence case, never all-caps; the rubricated initial (§6.5) lives here. |
| Part-title (leaf headings) | Cormorant 600 | 34px / 28px | 1.12 | 0 | Always preceded by its leaf numeral in mono taupe ("Leaf IV —"). |
| Section heading | Cormorant 600 | 24px | 1.2 | 0 | Rarely needed inside a leaf; most leaves are one movement. |
| Body | Cormorant 500 | 19px | 1.62 | 0 | 19px is deliberate: book text, not web text. Measure is capped by the column (§4), landing at 58–66 characters. |
| Body small (notes, errata) | Cormorant 500 italic | 17px | 1.55 | 0 | Errata entries and marginal notes only. |
| Apparatus caps (running head, imprint) | Cormorant 500, uppercase | 12.5px | 1.4 | 0.18em | The "letterspaced small caps" apparatus voice. |
| Apparatus mono (folios, data) | Plex Mono 400 | 12px | 1.5 | 0.02em | Print-run figures, dates, leaf counts, form labels. |
| Caption (plate captions) | Cormorant 500 italic | 15px | 1.45 | 0 | Under every plate, preceded by "Plate I." in mono taupe. |

**Per-role rules**

- Display: one per page (the title). If a page has no title-page hero, its part-title takes display's *role* at 34px — never promote a second 56px headline mid-page; a book has one title page.
- Headings never use rubric. Rubric is for the initial, the ornament, underlines, and errata markers — if a heading is red, the page reads as alarmed.
- Body: first paragraph of each leaf may open with a 2-line drop initial in `--ink` (not rubric — rubric initials are reserved for the title page, §6.5). Drop initials are set as a floated `::first-letter` at 2.9em, line-height 0.82, padding-right 0.12em — and are removed entirely below 480px viewport, where the narrow measure makes them crowd the line.
- Apparatus mono never exceeds 12px and never appears in `--ink` at full density for more than a line or two — it is the voice of the margin, and a shouting margin breaks the spell. The one exception is the print-run counter mid-count (§6.8), which may use `--ink` while moving and settles to taupe when done.
- Numerals in body text: old-style (proportional) figures from Cormorant. Numerals as *data* (editions, dates, counts): Plex Mono. The distinction is the theme in miniature — story in serif, facts in mono.

## 4. Layout language

**The column.** One centered column, max-width 640px, on a vellum field that extends to the viewport edges. No sidebar, no multi-column grid, no card rows. The page is a leaf, and a leaf has one text block. Horizontal centering is exact: the column's optical centre (accounting for the margin furniture, §6.2/§6.14) sits on the viewport centre at ≥1024px; below that, furniture collapses into the column flow (§6.2 mobile variant) and the column centres plainly.

**Grid inside the column.** An 8px baseline grid governs vertical rhythm; body text sits on a 30.78px line (19px × 1.62), and all spacing tokens are multiples that return text to the baseline: `--space-leaf: 96px` (between leaves), `--space-part: 56px`, `--space-note: 24px`, `--space-line: 8px`. Rules (hairlines) are 1px, drawn as real borders or SVG lines — never `box-shadow`, which prints fuzzy at some zooms; a rule that is not crisp at 200% zoom fails the gate (§10).

**Leaves, not sections.** Content is divided into numbered leaves. Each leaf opens with its apparatus header: leaf numeral (mono, taupe), a hairline rule, and — for part-leaves — the fleuron ornament (§6.7). Leaves are separated by 96px of vellum and nothing else: no background change, no container, no shadow. Whitespace *is* the section break, the way a blank verso page is.

**Section choreography.** A standard page reads: title leaf (hero, §6.14) → contents leaf (the site's own list of leaves, set as a book's contents with dotted leaders in taupe) → body leaves in order → errata or notes leaf (if any) → colophon footer (§6.17). The contents leaf is mandatory on any page with 4+ leaves; it is the theme's substitute for a card index or tab bar.

**Density rules.** One idea per leaf. A leaf that needs a second heading is two leaves. Apparatus density is capped: per leaf, at most one ornament, one folio reference, and one mono data line beyond the text itself. The margin (at ≥1024px) holds exactly two things across the whole page — the printer's mark (§6.14, page-family) and the folio (§6.2) — pinned, quiet, and never joined by badges, share buttons, or sticky CTAs. Anything a normal theme would put in a sticky bar must here become a leaf of its own or not exist.

**Whitespace as material.** The vellum field is not empty; it is the paper. Margins are wide because the book is well-made: at 1440px viewport, the column occupies 44% of the width and the paper the rest. Do not "use" the margins for related links or promos — that is the exact moment the theme becomes a blog template wearing a costume.

## 5. Full motion system

The complete motion vocabulary of the theme, each term in the theme's own language. The governing law: **motion is density, not displacement.** No element in this theme translates more than 0px in any reveal. (Two sanctioned exceptions, both inherited from print: the frontispiece clip widening, §6.4, which is a mask, not a movement of the image; and the underline draw, §6.9, which is a line being ruled.) Easings are named from the press room: `press` = `cubic-bezier(0.22, 0.61, 0.21, 1)` (the press settling — fast contact, long settle), `impression` = `cubic-bezier(0.37, 0, 0.2, 1)` (ink soaking in — slow start, decisive middle), `leaf-fade` = `cubic-bezier(0.45, 0, 0.55, 1)` (symmetric, for crossfades between two printed states).

| Motion term | The Colophon's version | Duration / easing | Trigger |
|---|---|---|---|
| Scroll-triggered reveals | Ink-density leaf reveals (§6.3): content gains ink 55%→100%, zero movement, registration sub-pixel | 600ms, `impression` | Leaf crosses 18% into viewport (IntersectionObserver, threshold 0.18, rootMargin bottom −8%) |
| Parallax layers | Rules and ornaments drift a hair slower than the column — implemented as density, not position: hairlines enter at 70% density and reach 100% 40px of scroll later than the text they rule, so the eye reads a fractional lag without anything moving | density lag over 40px scroll, rAF-lerped (factor 0.12) | Scroll (scrubbed) |
| Pinned scenes | The printer's mark pins in the margin through the apparatus leaves (§6.14); the folio pins in the corner (§6.2). Pinning is the only "scene" device — nothing else pins, ever | pin is instant (CSS `position: sticky`); density of the mark settles 300ms `press` when the pin engages | Scroll position |
| Masked line reveals | The frontispiece's centred clip widening (§6.4) is the theme's one mask; text never masks — masked text is a stage trick, and this is a page | 900ms, `impression` | Scroll entry |
| Blur-to-sharp reveals | Not used. Blur is photographic; print is either inked or not. The density ramp *is* this theme's blur-to-sharp, stated plainly so no builder substitutes a blur filter | — | — |
| Animated counters | Mono print-run counters (§6.8): tabular digits count in `press` steps | 900ms, `press`, 60fps rAF | Scroll entry of the data line |
| Progress indicators | The folio itself (§6.2) + the hairline under the running head filling leaf by leaf (§6.13) | folio tick 200ms `leaf-fade`; hairline fill scrubbed, rAF-lerped 0.12 | Scroll (scrubbed) |
| Marquees | Not used. A marquee is a fairground. The theme's horizontal motion budget is spent entirely on the underline draw and the contents leaders' density | — | — |
| Ambient loops | Exactly one: the candle-steady 2% flicker in the rubric ornament (§6.6). Stillness is the ambience; a second loop anywhere fails the gate | 7–11s irregular, opacity 0.98↔1.00 | Time |
| Micro-interactions | Ink-darkening click (§6.10): ink deepens 10% for 150ms; link hover draws the rubric underline (§6.9) | 150ms `press` / 240ms `press` | Click / hover |
| Hover physics | No tilt, no lift, no shadow — by design. Cards gain a hairline plate border (§6.15); links gain the ruled underline. The physics is a pen, not a spring | border fades in 200ms `press` | Hover / focus-visible (identical) |
| Page transitions | Leaf-turn (§6.12): page fades to vellum, next leaf assembles in title order | 300ms out `leaf-fade`, assembly per §6.1 | Route change |
| Image treatments | Plates sit in hairline borders; on entry they scale-in-frame — the *frame* is fixed, the plate settles from 102% to 100% scale inside an overflow-hidden plate border (the one place a transform is allowed, because a plate being slipped into its frame is a print gesture) | 700ms `impression` | Scroll entry |

**Global motion safety.** Every animated property animates *from a visible value to a visible value* (55% density is the floor — nothing ever starts at 0). A global end-state timer (900ms after first paint, and 900ms after any route change) forces every element to its final state regardless of observer or rAF state. With JavaScript disabled, the server/static render is the final state — animations are applied by JS adding a `data-impression="pre"` attribute *before* first paint via an inline script in `<head>`; no-JS means the attribute never appears and the page is simply printed. `prefers-reduced-motion` collapses the whole system to the static page (§6 passim; the deltas are listed per element).

## 6. Signature elements

Each element below carries the full build spec: what it is, structure, motion, states, content-merge, fallback, reduced-motion variant, performance budget, and mobile variant.

### 6.1 Title-page assembly (hero signature)

- **What & why.** The hero assembles in bibliographic order — imprint line, rule, title, rule, place of publication — each gaining ink in reading order, like a title page being printed line by line. It belongs to this theme because the title page is the one page every book has, and its order *is* the information hierarchy: who made it, what it is, where it comes from.
- **Structure.** A `<header class="title-leaf">` containing, in DOM order: `<p class="imprint">` (apparatus caps), `<hr class="rule">`, `<h1>`, `<hr class="rule">`, `<p class="imprint-place">`. Real `<hr>` elements styled to 1px — they are semantic dividers here, not decoration. The rubricated initial (§6.5) is the `<h1>`'s first letter, wrapped in a `<span class="rubric-initial">` by the build, never by hand in content.
- **Motion spec.** Load-triggered, staggered 160ms apart, each line 55%→100% density over 400ms `impression`. Total assembly 400 + 4×160 = 1,040ms. Zero translation, zero opacity (density via `color-mix` on text; rules via border-color mix). The sequence starts on `DOMContentLoaded` + 50ms, not on full `load`, so a slow plate image can never delay the title.
- **States.** *Rest (pre-JS):* fully inked. *Assembling:* lines at graded densities. *Settled:* all 100%; the final beat hands off to §6.5. *Revisit (SPA back-navigation):* assembly does not replay — a printed page does not reprint; state is held in a session flag.
- **Content-merge.** The assembly order is the reading order of the actual hero content — imprint (the maker/brand line), title (the page's real H1), place (the real location or edition line). Nothing assembles that is not content.
- **Failure fallback.** If the inline pre-paint script or the observer fails, no `data-impression` attributes are set and the hero is simply fully inked. The global 900ms end-state timer (§5) forces final density even if the stagger chain breaks mid-sequence.
- **Reduced-motion variant.** No assembly. The title leaf is static at 100% density from first paint.
- **Performance budget.** Zero network cost (no assets), one rAF-free CSS transition chain (density transitions are compositor-cheap colour interpolations); must not delay LCP — the H1 is in the first paint at 55% minimum density, which is fully legible (55% ink on vellum ≈ 5.9:1 effective contrast, AA for large text). **Mobile variant:** identical, with the stagger tightened to 120ms and title at 40px — same order, same law.

### 6.2 Folio-advance progress

- **What & why.** A folio number in the page corner that advances — I, II, III — exactly at each leaf boundary, with a hairline under the running head filling leaf by leaf beside it. Progress *is* pagination: the book's own numbering does the job a progress bar does elsewhere, in the page's own apparatus.
- **Structure.** `<div class="folio" aria-hidden="true">` fixed at the corner (top-right at ≥1024px, within the running head below that), containing a Plex Mono numeral; the current-leaf state is mirrored for assistive tech by a visually hidden `<span aria-live="off">` in each leaf header ("Leaf III of VII") — the folio itself is decorative because the leaf headers carry the same information semantically. The running-head hairline is a 1px `<div>` whose inner fill is a second 1px line in `--ink`, width scrubbed.
- **Motion spec.** Scroll-scrubbed via rAF with lerp factor 0.12 on the hairline fill. The numeral tick is discrete: when the boundary leaf's header crosses 50% viewport height, the numeral crossfades to the next (200ms `leaf-fade`, both numerals stacked in a grid cell, density crossfade only). Numerals are Roman, set in Plex Mono tabular — Roman numerals vary in width (VIII vs IX), so the folio box is fixed-width (3.5ch) and right-aligned to prevent layout shift.
- **States.** *Rest (leaf 1):* folio shows I, hairline fill = 1/N of its track. *Advancing:* crossfade. *Current leaf:* numeral in `--ink` at 100%. *Past leaves' numerals:* never shown — a book shows the folio of the page you are on. *End of page:* final numeral + hairline full; the folio then rests (no "100%" flourish).
- **Content-merge.** The folio numbers the actual leaves of the actual page — it is the page's table of contents made ambient. The leaf count N is derived from the DOM (`querySelectorAll('[data-leaf]')`), never hard-coded, so the apparatus can never lie about the page it numbers.
- **Failure fallback.** No JS → no folio element is rendered at all (it is JS-injected); leaf headers still carry their numerals in the static HTML, so pagination survives intact.
- **Reduced-motion variant.** The folio still updates (it is information, not ornament) but the crossfade is removed — the numeral swaps instantly at the boundary; the hairline fill jumps leaf-to-leaf instead of scrubbing.
- **Performance budget.** One rAF loop shared with §6.13 (single scroll listener for the whole theme; see §6.13 budget), no layout reads per frame beyond a cached boundary table recalculated on resize only. **Mobile variant:** the folio moves into the running head (§6.13), right-aligned beside the running title, 11px mono; the hairline fill spans the full head width under it.

### 6.3 Ink-density leaf reveals

- **What & why.** Each leaf's content gains ink from 55% to 100% density as it enters — with registration held to sub-pixel precision, nothing moves; it simply becomes printed. This is the theme's core reveal and its whole argument: attention through deepening, not motion.
- **Structure.** Leaves are `<section data-leaf>` blocks. The reveal is a CSS transition on a custom property `--density` registered via `@property` (with a `color-mix` fallback chain for engines without `@property`: the class-based fallback sets explicit density-step classes `d55/d70/d85/d100` and steps them on a 150ms interval — degraded but identical in outcome). Text elements transition `color`; rules transition `border-color`; plates transition `opacity` (they are objects on the page, §2).
- **Motion spec.** Trigger: IntersectionObserver, threshold 0.18, `rootMargin: 0px 0px -8% 0px`. Duration 600ms `impression`, from 55% to 100% in one continuous ramp (the `@property` path) — perceived as ink soaking in. Stagger inside a leaf: the leaf's apparatus header leads by 80ms, body follows; images (plates) lag the text by 120ms so the page prints words first, pictures second, as a press sheet would be read.
- **States.** *Pre-entry:* 55% density — fully legible, deliberately. *Entering:* ramping. *Printed:* 100%, observer unobserves the leaf (reveals never reverse; scrolling back up does not un-print a page). *Scrolled-past:* unchanged at 100%.
- **Content-merge.** The reveal is in the content's own ink — there is no overlay, wrapper animation, or separate animated object. Remove the animation and the leaf is byte-identical.
- **Failure fallback.** Default state in CSS is 100%. JS adds the 55% starting state only to leaves below the fold at setup time (leaves already in view at load are never de-inked — the first screen must never flash pale). Observer failure or the 900ms global timer leaves everything at 100%.
- **Reduced-motion variant.** No ramp: leaves are 100% at all times. The observer is never created.
- **Performance budget.** Colour transitions on text are paint-only; cap concurrent ramping leaves at 3 (observer queue) to bound paint cost on fast scrolls — leaves beyond the cap jump straight to 100% (a fast scroller is skimming, and a printed page serves skimming better than a lagging one). **Mobile variant:** identical, threshold lowered to 0.12 (shorter viewports, longer leaves) and the cap is 2 concurrent ramps.

### 6.4 Book-opening frontispiece

- **What & why.** The frontispiece — the plate facing the title page — reveals through a centred clip-path that widens symmetrically like a book opening flat. It is the theme's single piece of theatre, rationed to one image per page, and it is the plate's own gesture: a book opening.
- **Structure.** `<figure class="frontispiece">` with the `<img>` inside a wrapper carrying `clip-path: inset(0 50% 0 50%)` in its pre-state. The hairline plate border lives on the *wrapper's* parent frame (a separate absolutely-positioned 1px border box) so the border is visible before, during, and after the opening — the frame waits, the plate opens inside it. Caption below in italic with its "Plate I." mono prefix (§3).
- **Motion spec.** Scroll entry (same observer settings as §6.3, but threshold 0.35 — the opening must be *seen*, so it waits until a third of the plate is in view). `clip-path` animates inset 50%→0 horizontally over 900ms `impression`; simultaneously the image settles from 102% to 100% scale (§5 image treatment) over 700ms `impression`, so the plate is still for the last 200ms of the opening — the book finishes opening after the picture settles, in that order.
- **States.** *Pre-entry:* centre slit visible — a 0-width vertical glimpse between the frame's halves; the frame and caption are already at 100% density (the caption never waits for the picture). *Opening:* clip widening symmetrically — both edges move at identical rates; an asymmetric opening reads as a curtain and fails review. *Opened:* clip removed entirely (`clip-path: none` in the end state, so no clipping cost persists). *Scrolled-past:* stays open.
- **Content-merge.** The image is the page's actual frontispiece — the portrait, the artefact, the work — chosen as a book's frontispiece is chosen: one image that faces the title and earns it. A page with no such image does not get a frontispiece element; a stock photo in this frame is the theme's most expensive mistake (§9).
- **Failure fallback.** Pre-state clip is applied by JS only, at setup, and only if the plate is below the fold. No JS, no clip — the plate is simply there, framed. If the image itself fails to load, the frame collapses to a caption-only plate with the alt text set as a caption line in italic — an honest missing plate, noted like a binder's note, never a broken-image icon.
- **Reduced-motion variant.** No clip, no settle: the plate fades its last density step (85%→100%, 200ms) or is simply static. The frame and caption are unchanged.
- **Performance budget.** `clip-path` animation on one element per page, ≤900ms, on the compositor where supported; the image must be `fetchpriority="high"` only if it is the LCP candidate (title-leaf frontispieces), otherwise lazy. Decode must complete before the observer arms the trigger (gate on `img.decode()`) so the opening never reveals a half-decoded plate. **Mobile variant:** the opening narrows in ambition, not in kind: inset starts at 42% (a shorter travel), duration 750ms, and the scale settle is dropped — small screens get the gesture without the cost.

### 6.5 Rubricated initial swell

- **What & why.** One initial letter of the title, in rubric red, swells in saturation from 70% to 100% as the hero settles — the page's single flourish, the scribe's red initial that makes a manuscript leaf recognisable across a room. One flourish per page; its power is that it is the only one.
- **Structure.** `<span class="rubric-initial">` wrapping the H1's first letter (build-time wrap, §6.1). Saturation is animated on the colour itself: `color-mix(in srgb, var(--rubric) S%, var(--taupe))` with S from 70→100 — mixing toward taupe desaturates toward the page's quiet register, so the letter *warms* rather than fades in.
- **Motion spec.** Trigger: the final beat of the title-page assembly (§6.1) — it starts when the place-of-publication line reaches 100%, i.e. at ~1,040ms after load. Duration 500ms `press`. No size change, no weight change — "swell" is colour only; a letter that grows is a cartoon.
- **States.** *Assembling:* initial sits at 70% rubric (present, muted — it is printed with the title's first pass). *Swelling:* 70→100%. *Settled:* 100% rubric, static forever — the flicker (§6.6) belongs to the ornament, never to the initial; two living red things on one leaf is a quarrel. *Hover:* none. The initial does not respond to the pointer.
- **Content-merge.** The flourish is a letter of the actual title — rubricated as a scribe rubricates the text in front of him, not an icon placed beside it.
- **Failure fallback.** The span's static colour is 100% rubric; the 70% start state is JS-applied with the rest of the assembly pre-states. Any failure leaves a fully rubricated initial.
- **Reduced-motion variant.** Static 100% rubric from first paint.
- **Performance budget.** One colour transition on one glyph; negligible. **Mobile variant:** identical — the flourish survives small screens at full strength, since it costs nothing and carries the theme's signature at a glance.

### 6.6 Candle-steady ornament flicker

- **What & why.** The rubric fleuron at the title leaf carries a barely perceptible 2% opacity flicker on a slow, irregular loop — candlelight on a page. It is the theme's only ambient loop, and its job is to make the stillness feel *attended* rather than dead: the page is being read by candlelight, by someone.
- **Structure.** The flicker applies to the title leaf's fleuron instance only (§6.7 defines the ornament; only this one instance flickers). Implemented as a CSS keyframe animation on `opacity` with an irregular keyframe set (0%: 1.00, 18%: 0.99, 41%: 1.00, 63%: 0.98, 82%: 0.99, 100%: 1.00) over an 11s duration, `animation-iteration-count: infinite`, with a second instance offset by using `animation-delay: -4.3s` — no, there is no second instance; the single loop's irregularity comes from the keyframes alone. JavaScript is not involved.
- **Motion spec.** Opacity range 0.98–1.00 — a 2% band, deliberately below the threshold of conscious notice for most visitors; it registers as warmth, not movement. Period 11s nominal; the keyframe irregularity (18/41/63/82%) breaks any metronome feel. No easing keyword — keyframe segments use `ease-in-out` individually so the drift is breath-like.
- **States.** *Rest:* flickering (it has no rest state — that is its point, and why it is rationed to one element). *Document hidden:* the browser pauses CSS animations automatically; nothing to do. *Reduced-motion:* off (below). *Print:* `@media print` kills all animation; the ornament prints at 100%.
- **Content-merge.** The flicker lives inside the printed ornament — it is the ink of the fleuron breathing, not a lighting overlay, glow, or shadow cast over the page. There is no halo, no blur, no drop-shadow at any point.
- **Failure fallback.** If CSS animations are unsupported or stripped, the ornament is static at 100% — indistinguishable in any screenshot, which is the test: the flicker must be *felt*, never *pointed at*.
- **Reduced-motion variant.** Animation removed entirely; static ornament. This is the one element where reduced-motion changes nothing perceptible — by design.
- **Performance budget.** One opacity animation on one small SVG; the browser may composite it; it must never be applied to a parent of text (opacity on a text ancestor forces expensive repaints — the ornament is always a standalone inline SVG sibling, never a wrapper). **Mobile variant:** identical — at 2% there is nothing to cheapen. If the device reports `prefers-reduced-data` or the page is in a battery-saver profile exposed by the browser, drop it anyway: ambience is the first thing a lean page gives up.

### 6.7 Self-drawing fleuron rules

- **What & why.** At each part-title, the rule-and-fleuron ornament — a hairline, a small printed fleuron (❦-class ornament, drawn as vector), a hairline — draws itself as the part enters. It is the divider furniture of the book, and its drawing is the sound of the press making the divider before the text below it is read.
- **Structure.** Inline SVG, one per part-title, `viewBox="0 0 320 24"`: left rule line (x 0–132), fleuron path centred (144–176), right rule line (188–320), all stroke `--taupe` at rest with the fleuron stroke in `--rubric`. Total path lengths are measured at build time and written as `pathLength="100"` on each sub-path so dash math is uniform: `stroke-dasharray: 100; stroke-dashoffset: 100` pre-state. The SVG is `aria-hidden` and the part-title carries its own text — the ornament is furniture, and furniture is not announced.
- **Motion spec.** Trigger: scroll entry, observer threshold 0.5 (the ornament must be half-seen before it draws, or the drawing is wasted). Sequence: left rule draws 0→100 over 260ms `press`; fleuron draws over 240ms `press` starting at 200ms; right rule draws over 260ms starting at 420ms — total 680ms, overlapping like a hand ruling left to right and stamping the fleuron mid-pass. The fleuron's stroke settles from `--taupe` to `--rubric` as it completes (colour transition 200ms at its draw end) — it is drawn in pencil and inked in red.
- **States.** *Pre-entry:* dashoffset 100 (invisible lines, but the SVG box occupies its layout space — no shift when drawn). *Drawing:* per sequence. *Drawn:* dashoffset 0; stroke colours final. *Scrolled-past:* stays drawn. *Title-leaf instance:* after drawing, this instance (and only this one) acquires the §6.6 flicker.
- **Content-merge.** The ornament *is* the part's divider — it separates the actual part-title from the actual text above it. It is never floated decoratively into margins or repeated as a texture.
- **Failure fallback.** Pre-states are JS-applied; no JS → the SVG renders fully drawn (its natural state). If SVG is blocked, the part-title still has its CSS hairline fallback (a `border-top` on the header block, hidden when the SVG is present via a `.has-svg` class) — a plainer rule, but a rule.
- **Reduced-motion variant.** The ornament appears fully drawn, with a 200ms density fade of the whole SVG (85%→100%) as its only concession to arrival.
- **Performance budget.** Stroke-dashoffset animation on 3 short paths per ornament, ≤6 ornaments per page, never simultaneous (observer queue serialises them 100ms apart on fast scroll). **Mobile variant:** the ornament scales to column width (SVG is fluid by construction); the sequence compresses to a single 400ms draw of all three sub-paths together — small screens get the gesture in one breath.

### 6.8 Mono print-run counters

- **What & why.** Where the colophon cites print data — edition size, copies bound, leaves in the volume, glyphs in the font — the numbers count up in IBM Plex Mono tabular figures. Counting belongs here because these are the book's *production facts*: the number arriving digit by digit is the print run being tallied.
- **Structure.** `<span class="print-data" data-count="1250" data-format="en-GB">1,250</span>` — the final, formatted value is the element's text content in the static HTML (the count is an enhancement of a printed number, never its source). Counting is a single rAF loop per counter writing `textContent` with `Intl.NumberFormat` grouping; `font-variant-numeric: tabular-nums` is set even though Plex Mono is inherently tabular, as a belt-and-braces for fallback fonts.
- **Motion spec.** Trigger: scroll entry of the data line, threshold 0.4. Duration 900ms, `press` easing applied to progress; the count starts at 62% of the value (not zero — a colophon tally starts from the sheets already printed, and starting at 0 makes small numbers like "8 leaves" absurd) and eases to the exact value, landing with no overshoot and no bounce. Frame updates are throttled to whole-number changes only.
- **States.** *Static:* final value, taupe. *Counting:* value rising, colour steps up to `--ink` while moving (the one sanctioned mono-in-ink moment, §3). *Landed:* colour returns to taupe over 300ms; the number is thereafter inert. *Re-entry:* never recounts.
- **Content-merge.** The counters count the page's own cited facts — the edition size of the book being sold, the leaf count of the volume being described. A counter on a marketing statistic ("10,000 happy readers") is forbidden: unverifiable numbers are exactly what a colophon's honesty exists to refuse.
- **Failure fallback.** Static HTML already shows the final value; JS only rewinds it to 62% at setup if the element is below the fold. Any failure leaves true numbers printed.
- **Reduced-motion variant.** No count. The number is simply there, in taupe, as printed.
- **Performance budget.** At most 4 counters per page, one shared rAF loop, text writes only on integer change; cost is negligible and capped. **Mobile variant:** identical, duration 750ms — shorter attention, same tally.

### 6.9 Rubric underline hover

- **What & why.** Hovering a link draws a rubric-red underline left to right beneath it — an editor's rubrication on the line being read. It is the theme's primary interaction signal, and its restraint (one line, one colour, no background change) is the interaction language of the whole theme.
- **Structure.** Links carry `background-image: linear-gradient(var(--rubric), var(--rubric))` sized `0% 1px`, positioned bottom-left, no-repeat — a background, not a border or text-decoration, so it never disturbs line-height or the baseline grid. Transition on `background-size`. Links that already carry a permanent taupe underline (contents leaders, §4) invert the scheme: the rubric line draws *over* the taupe at the same 1px position.
- **Motion spec.** Draw: `background-size: 0% 1px → 100% 1px` over 240ms `press`. Retreat (pointer leaves): 180ms `press`, right-to-left collapse (background-position flips to bottom-right during retreat so the line exits the way a pen lifts — a detail costing one CSS rule and worth more than most hover states on the web). `:focus-visible` produces the identical draw, held for as long as focus remains.
- **States.** *Rest:* no line (body links) or taupe line (apparatus links). *Hover/focus:* rubric line full. *Active (pressed):* the line thickens to 2px for the press duration — the pen pressing harder — paired with §6.10's ink darkening. *Visited:* the rest state gains a taupe underline permanently (a line already ruled in the margin of a read book); the rubric draw still works over it.
- **Content-merge.** The underline is drawn on the link text itself — the annotation lands on the words being chosen. It is never applied to buttons (buttons here are text links with apparatus styling; §6.16), never to the folio, never to the printer's mark.
- **Failure fallback.** It is pure CSS on the element's final state — there is no hidden content and no failure mode beyond "no animation," which still leaves a functional, focus-visible link (focus also gets a 1px taupe outline offset 2px, so keyboard users are never dependent on the draw alone).
- **Reduced-motion variant.** The underline appears instantly at full width on hover/focus (state change without transition).
- **Performance budget.** `background-size` transitions repaint the link's line box only; dozens of links per page are fine because transitions run one at a time under one pointer. **Mobile variant:** no hover exists; tap gives the 2px active state for 150ms before navigation, and all links in body copy carry the permanent taupe underline so they are identifiable without hover.

### 6.10 Ink-darkening click

- **What & why.** Clicking an entry quietly darkens its ink by 10% for 150ms — acknowledgement without movement. In a theme where nothing moves, feedback must live in the ink itself: the press of a finger on the page, the type taking a deeper impression for a moment.
- **Structure.** Applies to entries (contents rows, catalogue entries, errata items) via a `.entry` class: `transition: color 150ms` on the entry's text colour, driven by an `.is-pressed` class toggled on `pointerdown`/`pointerup` (and on Enter/Space keydown/keyup for keyboard parity). Darkening is implemented as a density overshoot: colour steps from 100% to a `color-mix` of `--ink` 100% + 10% black — specified as the pre-mixed token `--ink-pressed: #14110D` so no runtime mixing is needed on the hot path.
- **Motion spec.** Down: 60ms to `--ink-pressed` (a press is fast). Release: 150ms `press` back to `--ink`. If the click navigates, the darkened state holds through the leaf-turn fade (§6.12) — the pressed entry is the last thing seen darkening as the page turns.
- **States.** *Rest:* `--ink`. *Pressed:* `--ink-pressed`. *Disabled entry:* taupe, no darkening, `aria-disabled` — a faded entry that does not respond, like a line struck from the run. *Selected/current entry* (e.g. the contents row for the leaf being read): carries a permanent rubric tick in its left margin (a 6px rule), not a colour change — selection is apparatus, not ink.
- **Content-merge.** The feedback is in the entry's own print. There is no ripple, no highlight box, no shadow — the thing you touched is the thing that answers.
- **Failure fallback.** Pure class toggle on real elements; if JS is absent, entries that are links still navigate (the darkening is an enhancement layered on native behaviour, never a gate on it).
- **Reduced-motion variant.** The state change is a colour swap, already effectively instant at 60/150ms; it is kept, with durations halved (30/75ms). Colour-change feedback is not vestibular motion and removing it would remove the only confirmation the theme offers.
- **Performance budget.** One colour transition per press; zero layout. **Mobile variant:** identical — tap *is* the press, and this element is why the theme feels responsive on touch despite having no other touch theatre.

### 6.11 Skeleton leaves

- **What & why.** While a leaf's content loads, the page shows a skeleton leaf: hairline rules and grey bars at final positions — the leaf's own rule structure awaiting its text, like a page of ruled lines before the scribe begins. Loading states in this theme are not spinners; a book does not spin.
- **Structure.** `<div class="skeleton-leaf" aria-busy="true">` mirroring the target leaf's structure: one apparatus rule (1px, taupe at 60%), a title bar (Cormorant-height block, 34px tall, taupe at 22% density), and body bars at 19px height with the leaf's line-height (30.78px pitch), widths following the expected measure (100%, 96%, 100%, 61% for a paragraph's last line). Bars are flat `--taupe` mixes — no shimmer gradient, no pulse; a skeleton that moves would break the theme's one law.
- **Motion spec.** Appearance: the skeleton is simply present (it renders with the page shell; no entrance animation). Resolution: when content arrives, the skeleton's bars gain density 22%→0 over 200ms `leaf-fade` *while* the real content gains 55%→100% over 400ms `impression`, crossfading in place — total handover 400ms, no layout shift because every bar occupies its final box (the shell reserves exact heights from the leaf's known structure).
- **States.** *Loading:* bars at rest densities. *Resolving:* crossfade as above. *Error:* the skeleton is replaced by an errata-style note (§6.16's error language): an italic line — "This leaf could not be printed. [Retry]" — set as an errata entry, because in this world a failure is a correction waiting to be pasted in. *Timeout:* any leaf unresolved after 4s resolves to the error note automatically; skeletons never persist indefinitely.
- **Content-merge.** The skeleton is the leaf's own structure — its rules, its measure, its line pitch. It teaches the page's rhythm before the words arrive, which is precisely what a ruled blank page does.
- **Failure fallback.** If the shell itself fails, the server-rendered page (no skeletons, content inline) is the fallback — skeletons exist only in the client-hydrated path. `aria-busy` and a visually hidden "Loading" label keep the state honest for assistive tech; the bars themselves are `aria-hidden`.
- **Reduced-motion variant.** No crossfade: skeleton swaps to content in one step when ready.
- **Performance budget.** Static DOM, zero animation loops (the absence of a shimmer is also a performance position). Shell markup ≤1.5KB per skeleton leaf. **Mobile variant:** identical structure; body bars reduce to 3 lines + last-line stub, since mobile leaves are re-flowed excerpts of the same structure — the skeleton mirrors the *rendered* leaf, not the desktop one.

### 6.12 Leaf-turn transition

- **What & why.** Navigation turns the leaf: the page fades to vellum, and the next leaf assembles in title order (§6.1). It is the only page transition the theme permits, and it is the book's own gesture — you do not slide to the next page of a book; you turn to it, and the new page is simply there, printed.
- **Structure.** A full-viewport vellum veil (`<div class="leaf-veil">`, `background: var(--vellum)`, opacity 0, pointer-events none) owned by the router layer. On navigation: veil fades in over the old page, the route swaps beneath it, veil fades out onto the new leaf whose title assembly begins as the veil lifts.
- **Motion spec.** Out: veil 0→1 over 300ms `leaf-fade`. Swap: instantaneous beneath the veil (the veil must be fully opaque for at least one frame — a visible mid-swap flash fails the gate). In: veil 1→0 over 300ms `leaf-fade`, with the new title leaf's assembly (§6.1) starting at veil 40% so the imprint line is already gaining ink as the page is revealed. Total perceived transition ~750ms. Same-page anchor navigation never triggers the veil — anchors scroll (instantly, or with the density-lag of §5 — never with a smooth-scroll glide; gliding is movement, and movement is not this theme's language. Anchor jumps are instant, and the target leaf is already printed).
- **States.** *Idle:* veil transparent, inert. *Turning:* as sequenced. *Interrupted (user navigates again mid-turn):* the veil completes its fade-in, swaps to the newest route, fades out — the queue is length 1, latest wins, no stacked veils. *Back/forward:* identical treatment; a turned leaf is a turned leaf in either direction.
- **Content-merge.** The transition is between the book's own leaves, using the book's own paper (the veil is vellum, not a branded colour or a logo splash).
- **Failure fallback.** If the router/JS fails, navigation is a normal full-page load — the veil never appears and every page is server-rendered complete. The veil element is JS-injected; static HTML contains no veil.
- **Reduced-motion variant.** No veil: instant route change. The new page's title assembly is also suppressed (§6.1), so the reduced-motion experience is simply *pages, arriving printed*.
- **Performance budget.** One opacity transition on one fixed element; the route swap must complete within the 300ms fade-in on target hardware, or the veil holds (it waits for a router `ready` signal with a 1,200ms cap, after which it fades onto whatever has rendered — a veil that traps the visitor is worse than a plain load). **Mobile variant:** identical timings; the veil also covers the running head so the whole screen turns as one leaf.


### Page-family elements

The six page-family elements every build needs, in this theme's language. (Hero = §6.1, the title-page assembly; loader/transition = §6.11 and §6.12. What follows covers navigation, the margin mark, cards, forms, the contents leaf, and the footer.)

### 6.13 Running-head navigation

- **What & why.** The navigation is a running head — the line at the top of every printed page that repeats the book's title and the current part. It does not look like a navbar because it is not one: it is the page's own header furniture, stating where in the volume the reader stands.
- **Structure.** A `<header class="running-head">` spanning the column width: left, the work's title in apparatus caps (Cormorant 500, 12.5px, 0.18em tracking, uppercase); right, the current part name in the same voice, taupe; beneath both, the 1px hairline whose `--ink` fill is §6.2's progress line. Nav links (Contents, Errata, Colophon, and the host site's 2–4 primary destinations) live not in the head but in the contents leaf (§6.18) and the footer (§6.17) — a running head carries no menu, and this theme has no hamburger: with ≤6 destinations, the contents leaf *is* the navigation, one tap from the top via the head's "Contents" apparatus link, which is a plain anchor to that leaf.
- **Motion spec.** The head is sticky (`position: sticky; top: 0`) with a vellum background at 100% — it never blurs, never shadows; when it sticks, a second hairline appears beneath the progress line over 200ms `press` (the head "lifts" by ruling itself off from the page — the only separation device the theme owns). The progress fill scrubs per §6.2 (shared rAF loop, lerp 0.12). Part-name changes crossfade 200ms `leaf-fade` in step with the folio tick — head and folio always agree.
- **States.** *At top:* single hairline, part name = the title leaf's part. *Stuck:* double hairline. *Current destination* (when the head's apparatus link matches the page): rubric tick (6px rule) before the title. *Mobile:* see below.
- **Content-merge.** The running head names the actual book and the actual part the reader is in — it is the page's own furniture, generated from the page's real structure (part names come from the leaf headers, never from a separate nav config that could drift).
- **Failure fallback.** Static HTML renders the head unstuck with the correct part name for the page's first leaf; stickiness and progress are enhancements. All destinations remain reachable via the contents leaf and footer without any JS.
- **Reduced-motion variant.** Head sticks identically; the second hairline appears instantly; progress fill jumps leaf-to-leaf (with §6.2).
- **Performance budget.** Sticky header with background fill — no backdrop filters, no scroll listeners beyond the theme's single shared rAF loop. The head's height is fixed (57px including rules) and reserved in layout, so stickiness causes zero shift. **Mobile variant:** the head compresses to one line — title left, folio right (§6.2's mobile home), part name dropped (the leaf headers carry it), progress hairline full-width beneath; height 49px.

### 6.14 The printer's mark (margin device)

- **What & why.** The printer's mark — a small device (monogram, fleuron-in-frame, or the house's mark) — sits pinned in the left margin through the apparatus leaves, the way a printer's device recurs on title and colophon leaves. It is the brand's presence in the theme: not a logo in a navbar, but a mark in the margin, where printers have always put it.
- **Structure.** An inline SVG device, 44×44px, drawn in `--ink` strokes (never filled colour, never rubric — the mark is the printer's, and rubric is the scribe's; the two hands do not share ink). Positioned in the left margin at ≥1280px viewport (where the margin is ≥180px wide), `position: sticky` within the apparatus region (contents leaf through the leaf before the footer), aligned to the first leaf's header baseline.
- **Motion spec.** The mark does not animate. Its pin engages with a 300ms density settle (70%→100%, `press`) when the apparatus region enters — it *arrives in ink* like everything else, then never moves again. When the region ends, it un-pins and scrolls away with the page; no fade-out theatre.
- **States.** *Before apparatus:* absent (the title leaf has no margin mark — the title page carries the imprint line instead). *Pinned:* 100% ink, static. *Footer approach:* unpinned, scrolls off naturally. *Hover:* none — the mark is not a link and must not pretend to be; if the host brand insists the mark link home, it gets §6.9's underline treatment on a caption beneath it ("The House" in apparatus mono), never a hover effect on the device itself.
- **Content-merge.** The mark is the maker's own device, recurring where a printer's device recurs. It is content (identity), not decoration; a generic ornament in this slot fails §9.
- **Failure fallback.** Pure CSS sticky on an inline SVG; any failure leaves the mark sitting statically at the apparatus region's start — still correct, merely unpinned.
- **Reduced-motion variant.** Identical (a 300ms density settle is within the theme's reduced-motion allowance; if the builder's reduced-motion implementation is strict, the settle is the first thing cut and nothing is lost).
- **Performance budget.** One small SVG, zero JS. **Mobile variant:** below 1280px the margin cannot hold it, so the mark moves to the one place it also belongs in a book: centred above the footer colophon (§6.17), at 36px, as the footer's headpiece. It is never hidden outright — identity furniture relocates, it does not vanish.

### 6.15 Plate cards (entries)

- **What & why.** Where the site must list things — books, works, exhibitions, fonts — each item is a plate entry: a block that on hover gains a hairline plate border, as if the entry were being framed as a plate in the volume. Cards here do not float, shadow, or lift; they are *entered in the catalogue*, and the border is the catalogue's ruling around the chosen entry.
- **Structure.** `<article class="plate-entry">`: optional plate image (hairline-bordered, §5 image treatment) at column width or a 120px left plate on ≥640px; title (Cormorant 600, 24px); one-line description (body 19px, max 2 lines); apparatus line (Plex Mono 12px, taupe: date · edition · count — the entry's colophon facts). The whole entry is one link (stretched-link pattern with the title as the anchor) — one entry, one destination, as a catalogue dictates.
- **Motion spec.** Hover/focus-visible: a 1px border in `--taupe` fades in around the entry over 200ms `press` (border drawn via an inset `box-shadow: inset 0 0 0 1px` — used here, exceptionally, because animating four border sides costs layout; the shadow is a hard 1px ring, not a blur, so the §4 crispness rule holds — verify at 200% zoom per §10). Simultaneously the entry's plate image settles 102%→100% (§5). Press: §6.10 ink-darkening on the title. Entry reveal on scroll: §6.3 density, with entries staggering 90ms apart within a leaf (catalogue entries print one after another, not in a chord).
- **States.** *Rest:* borderless, on the vellum, separated from siblings by 40px of paper and a hairline rule at 40% density between entries (the catalogue's faint ruling). *Hover/focus:* full plate border at taupe 100%. *Current/featured entry:* permanent border in `--ink` + rubric tick in the margin (§6.10's selection language) — at most one per leaf. *Unavailable entry* (out of print, past exhibition): all ink at taupe, no border response, apparatus line gains "Out of print" / "Closed" — stated, never hidden.
- **Content-merge.** The card is the catalogue entry itself; its apparatus line carries the item's real production facts. There is no separate "card design" applied over content — remove the border behaviour and the entry is still a complete, well-set catalogue record.
- **Failure fallback.** Entries are static HTML; hover behaviour is CSS-only. No JS is involved at any point in this element's life.
- **Reduced-motion variant.** Border appears instantly on hover/focus; image settle removed; density reveals per §6.3's variant.
- **Performance budget.** CSS only; image settle is one transform on one image per hover. **Mobile variant:** no hover — the plate border is permanently on at taupe 60% (entries must be distinguishable as units on touch), the left plate stacks above the title, and the apparatus line wraps to two lines rather than truncating (facts are never truncated in this theme; §9).

### 6.16 The correspondence form (forms)

- **What & why.** Forms — contact, subscription, order-of-edition — are set as the book's correspondence leaf: a letter the visitor writes to the house, on ruled lines. A form in this theme succeeds by feeling like writing in a well-made book's guest leaf, not by resembling a SaaS signup. This element also owns the theme's error language (referenced by §6.11): in this world, errors are *errata* — corrections, stated plainly and pasted in.
- **Structure.** `<form class="correspondence">`: each field is a label in apparatus mono (12px, taupe, uppercase via letterspacing) above a single hairline-ruled input — no boxes, no filled backgrounds; the input is a line to write on (Cormorant 500, 19px, `--ink`), with the rule as its `border-bottom`. Fields stack at 32px gaps. The submit control is a text button in apparatus caps with §6.9's rubric underline permanently drawn at 100% — the one place the underline rests *drawn*, because signing is the act. A short imprint line under the form states, in italic, what happens to the letter ("Answered within two working days. Kept on paper, not sold.").
- **Motion spec.** Focus: the field's rule thickens from 1px taupe to 1px `--ink` over 200ms `press` and a rubric caret-line (2px, left 12px of the rule) draws in over 240ms — the editor's mark at the line being written. Label steps taupe→`--ink` with focus. Validation on submit: an erroneous field's rule turns rubric (the editor's red line) over 200ms, and its errata note (below) gains ink per §6.3 at 400ms. Successful submit: the whole form gains density to 100% (it is often already there), fades to 70% over 300ms, and is replaced by the acknowledgement leaf (§6.17's language: "Received and entered as leaf…" — no, precisely: a short leaf stating receipt with a mono reference line, e.g. "No. 214 — answered within two working days").
- **States.** *Rest:* taupe labels, hairline rules. *Focus:* per above. *Filled:* rule stays `--ink` at 70% (a written line stays darker than a blank one). *Error:* rubric rule + errata note in italic 17px beneath the field, worded as a correction: "For 'email' read: an address with an @ and a domain." — the errata voice states what the line should say, never "Invalid input." *Disabled/submitting:* all ink to 70%, submit underline undraws to 40%, no spinner (a book does not spin; the state is stated in the imprint line, which changes to "Being entered…"). *Success:* acknowledgement leaf replaces the form in place, same column, with the reference number in mono.
- **Content-merge.** The form's fields, imprint line, and acknowledgement are the correspondence itself — the imprint line carries the house's real policy (response time, data handling) in the place a colophon carries production facts. Error text is content written in the errata voice, not system strings.
- **Failure fallback.** The form is a real `<form>` with native validation attributes; without JS it submits natively and errors render server-side in the same errata format on reload. No field's meaning depends on JS-driven widgets — selects are native selects set in the same ruled style.
- **Reduced-motion variant.** All transitions instant; state changes (focus rule, error rule) still occur — they are information, not motion.
- **Performance budget.** CSS transitions only; the JS (progressive validation) is ≤2KB and deferrable. **Mobile variant:** identical structure — the ruled-line field is inherently touch-friendly at 19px type with 48px tap rows (label + line + gap); the submit underline stays drawn; date/number inputs use native controls.

### 6.17 The colophon footer

- **What & why.** The footer is an honest colophon — the theme's signature ending, quoted in the original theme's anti-slop line: *"Set in Cormorant Garamond. Built in one sitting. No cookies were consulted."* Every build's footer states, in the colophon voice, what the site was made with, where, and what it does not do. It is the most-remembered element of the theme precisely because footers are where sites usually stop telling the truth.
- **Structure.** A `<footer class="colophon">` opened by the printer's mark (mobile position, §6.14; on desktop the mark is in the margin and the footer opens with the fleuron rule, §6.7, drawn on entry), then three short apparatus blocks in the single column: (1) the colophon paragraph (italic 17px): types used, place, year, and the house's one honest sentence; (2) the facts line (Plex Mono 12px, taupe): edition data of the site itself — "Second edition · MMXXVI · Set in Cormorant Garamond & IBM Plex Mono" — updated when the site changes, like a real edition statement; (3) the necessary links (privacy, terms, contact) as plain apparatus links with §6.9 underlines, plus any legally required notices set in body small. No columns of links, no newsletter box (a newsletter is a form leaf of its own, §6.16, placed as a leaf — never smuggled into the footer).
- **Motion spec.** The footer's fleuron draws per §6.7 on entry. The colophon paragraph reveals per §6.3. Nothing else moves, ever — the footer is where the book ends, and books end quietly. One sanctioned delight: the year in the facts line is set from the actual date; when a returning visitor's stored last-visit year differs, the facts line gains the errata-style suffix "· corrected MMXXVI" — a joke only a colophon can make, and rationed to once.
- **States.** *Rest:* as structured. *Print:* the footer is the one element that must print perfectly — `@media print` sets it at 100% ink, mark included (a printed page of this site ends with its colophon, as it should).
- **Content-merge.** The footer *is* content — the site's own production statement. Every claim in it must be true of the actual build (types actually loaded, year actually current, the "no cookies" line only if it is literally true — §9 makes a false colophon the theme's capital offence).
- **Failure fallback.** Static HTML, no JS involved except the optional year suffix, whose absence changes nothing.
- **Reduced-motion variant.** Fleuron appears drawn (per §6.7); otherwise identical.
- **Performance budget.** Zero. **Mobile variant:** identical, mark centred above (per §6.14), facts line wraps — never truncates.

### 6.18 The contents leaf (navigation by list)

- **What & why.** The site's table of contents, set as a book's contents page: each entry a title, a dotted leader in taupe, and a folio numeral at the right. It is the theme's primary navigation device (§6.13 defers to it) and its listing pattern for anything that is genuinely a list of leaves — sections of the page, parts of the catalogue, chapters of the work.
- **Structure.** `<nav class="contents">` or `<ol class="contents">` of `<li class="entry">` rows: title (Cormorant 500, 19px), leader (a flexible dotted rule — implemented as a `border-bottom: 1px dotted var(--taupe)` on a flex-growing spacer span, baseline-aligned), folio/leaf numeral (Plex Mono 12px). Row height 44px; the whole row is one link. Leaders align: numerals form a right-hand column, titles a left — the two columns of a contents page.
- **Motion spec.** Rows reveal per §6.3 with a 70ms stagger (the contents prints line by line). Hover: §6.9's rubric underline draws under the *title only* (never under the leader — underlining dots is noise), and the row's numeral steps taupe→`--ink`. Press: §6.10. The current leaf's row (when the contents lists the page's own leaves) carries the rubric margin tick (§6.10) and its numeral in rubric.
- **States.** *Rest:* titles in `--ink`, leaders taupe 60%, numerals taupe. *Hover/focus:* as above. *Current:* tick + rubric numeral. *External entries* (leaving the volume): the numeral is replaced by "→" in mono taupe — stated plainly, not disguised.
- **Content-merge.** The contents lists the actual leaves/destinations with their actual numbering. It is generated from the same structure the folio counts (§6.2), so contents, folio, and running head can never disagree.
- **Failure fallback.** Plain list of links in static HTML; leaders are CSS-only decoration over a fully functional list.
- **Reduced-motion variant.** Rows appear printed; hover states instant.
- **Performance budget.** CSS only. **Mobile variant:** leaders shorten naturally (flex); below 400px the numeral moves *before* the title ("IV · Title") and the leader is dropped — a narrow contents page sets its numbers first, as some books do, rather than crushing the dots.

## 7. Page application map

**Home (the volume).** Title leaf (§6.1) with frontispiece (§6.4) if the house has one true image; contents leaf (§6.18) listing the site's parts; two or three body leaves at most — a home page in this theme is a title page and a promise, not a scroll of everything. The print-run counter (§6.8) appears if, and only if, the house has a true number worth tallying (copies bound, titles in print). Footer colophon (§6.17) closes. Folio counts the leaves honestly — if the home page has four leaves, the folio ends at IV.

**Listing / catalogue (the catalogue leaves).** Opens with a part-title leaf (numeral + fleuron, §6.7) stating what is catalogued and in what order ("Arranged by year of publication"). Entries are plate cards (§6.15) in one column, ruled apart. Ordering and filtering, if truly needed, are apparatus links in a single mono line above the entries ("All · In print · Out of print") — text filters, never chips, never a sidebar. Pagination is folio language: "Leaves I–III of the catalogue" with contents-style rows (§6.18) for further ranges, never numbered page buttons in boxes.

**Detail (the leaf itself).** One work, given a full leaf sequence: part-title with the work's title; its plate (frontispiece treatment is reserved for the home page — detail plates use the standard plate border and settle, §5, so the opening gesture stays rare); body leaves for description; an apparatus leaf carrying the work's full colophon facts in mono (edition, date, place, count, types) — on a detail page this facts leaf is mandatory, it is what the theme is *for*. Ends with a contents row (§6.18) returning to the catalogue, leader and all.

**About (the house).** Set as the house's own colophon, expanded: the story in body leaves, the people as catalogue entries (§6.15, without plates if there are no portraits worth printing — initial-only entries are permitted and often better), the printer's mark (§6.14) pinned through it. The about page is where the footer's honest sentence is earned; builders should draft the colophon paragraph (§6.17) from this page's facts.

**Contact / order (the correspondence leaf).** The form (§6.16) as the page's single leaf, preceded by one short leaf stating the house's terms of correspondence (response time, what is kept, what is never done with letters) in italic body — the imprint line of §6.16 writ large. Checkout equivalents (buying an edition) keep the same ruled fields, add an order summary set as an apparatus block (mono lines, leaders, total ruled double — a double rule under a total is the oldest total-marker in print), and end with an acknowledgement leaf bearing the order's number in mono. No progress-stepper UI: the steps are named in the running head's part slot ("Order — the second leaf").

**404 / error (the errata slip).** The error page is an errata slip: "Errata. For 'the page requested' read: 'not in this volume'." — followed by the contents leaf (§6.18) as the way back. It is the theme's best joke and it only works because the errata voice has been used seriously everywhere else (§6.16).

## 8. Worked example — the title leaf of a small press, end to end

The build: home page title leaf for a fictional-but-typical client, a two-person poetry press. Source content (all real, supplied by the client): house name "Heron & Quill Press"; title line "Poems, printed slowly."; place line "Stroud · MMXXVI"; frontispiece: a photograph of the press's Vandercook proof press, shot straight-on, available at 1600×1200.

1. **Shell.** Server-rendered HTML, no veil (§6.12 is client-side only). An inline `<script>` in `<head>` (≤0.4KB) checks `matchMedia('(prefers-reduced-motion: no-preference)')`; only if it passes does it add `data-impression="pre"` to `<html>`, arming the pre-states. Without JS or with reduced motion, the page is born printed.
2. **Running head (§6.13).** "HERON & QUILL PRESS" left, "The Title Leaf" right (taupe), hairline beneath with the progress fill at leaf 1 of 5 (the page has five leaves: title, contents, the new season, the print room, colophon footer — footer counts as a leaf for the folio, stated in the build notes so the apparatus agrees everywhere).
3. **Title leaf (§6.1).** DOM order: imprint line — "HERON & QUILL PRESS · EST. MMXIX" in apparatus caps; rule; H1 "Poems, printed slowly." at 56px Cormorant 600, first letter "P" wrapped in `.rubric-initial`; rule; place line "Stroud · MMXXVI". On load (motion allowed): lines gain ink at 160ms stagger, 400ms each, `impression`; at ~1,040ms the "P" begins its 500ms saturation swell (§6.5). LCP is the H1, painted in the first frame at 55% density — legible immediately, deepening as the press settles.
4. **Frontispiece (§6.4).** Directly beneath the place line, inside its waiting hairline frame: the Vandercook photograph, `alt="The Vandercook proof press in the Heron & Quill print room"`, caption "Plate I. The proof press, Stroud." The observer arms only after `img.decode()` resolves; at 35% visibility the clip opens 50%→0 over 900ms while the plate settles 102%→100% over 700ms. On the press's phone (375px), the opening runs 42%→0 over 750ms with no settle.
5. **Folio (§6.2).** Top-right corner: "I" in Plex Mono, box 3.5ch, right-aligned. Scrolling into the contents leaf, at its header crossing mid-viewport, "I" crossfades to "II" (200ms) and the head's hairline fill lerps to 2/5.
6. **The mark (§6.14).** The press's device — a heron over a quill, line-drawn SVG, 44px — pins in the left margin from the contents leaf to the print-room leaf, having settled 70%→100% as the contents leaf entered. On the client's 1280px laptop it is present; on a 1024px tablet it is already relocated to the footer (breakpoint 1280px, §6.14) — checked in the build, not discovered by the client.
7. **Print-run counter (§6.8).** In the print-room leaf, the apparatus line "Copies of the spring pamphlet, bound by hand: 340" — the 340 counts from 211 (62%) over 900ms when the line enters, in Plex Mono, stepping to `--ink` while counting, settling back to taupe.
8. **The check.** Before sign-off, the builder disables JS: the page is complete, every number final, the plate open, the folio absent but every leaf header numbered. Then reduced-motion: identical page, static. Then 200% zoom: every rule still crisp. The leaf passes §10 or it does not ship.

## 9. Anti-slop — how this theme goes cheap, and the cure

- **A false colophon.** Footer claims ("No cookies were consulted", "Set in…") that are not literally true of the build. This is the capital offence: the theme's entire value is that its apparatus tells the truth. *Cure:* every footer claim is verified against the build at the §10 gate; an unverifiable claim is deleted, not softened.
- **Costume serif.** Using Cormorant for headlines over an otherwise ordinary SaaS layout (hero + three cards + logo strip). The theme is a layout language (§4), not a font swap. *Cure:* if the page has a card row, a sidebar, or a sticky CTA bar, it is not this theme — rebuild the layout or choose another theme.
- **Rubric everywhere.** Red headings, red buttons, red links, red badges. Rubric past ~3% stops being annotation and becomes branding. *Cure:* the one-flourish rule (§2, §6.5); audit per leaf — one rubric element, two if one is the fleuron.
- **Taupe body text.** Quiet-grey body copy in the name of elegance — unreadable and dishonest about it. *Cure:* body is `--ink`, always; taupe is furniture (§2) and any taupe text must be redundantly conveyed.
- **Movement creep.** A builder adds a fade-up "just for polish", a hover lift "just for feedback". Each is small; together they dissolve the theme's one idea. *Cure:* the motion table (§5) is exhaustive — a motion not in the table does not ship, and "blur-to-sharp: not used" and "marquee: not used" are decisions, not gaps.
- **Stock frontispiece.** A generic letterpress photo from a stock library in the §6.4 frame. The opening gesture spends the page's whole theatre budget on the image; a borrowed image makes it a trailer for someone else's book. *Cure:* the frontispiece must be the client's own artefact, or the page ships without one.
- **Invented apparatus.** Print-run counters on numbers nobody verified, edition statements for a site that has no editions, "MMXXVI" used as decoration. *Cure:* apparatus is generated from real structure (§6.2's DOM-derived count) or real facts (§6.8); where no fact exists, the apparatus line is omitted — a shorter colophon, honestly.
- **Ornament spam.** Fleurons as bullet points, section icons, loading spinners. *Cure:* the fleuron exists in exactly two roles — part-title divider (§6.7) and the one flickering title instance (§6.6). Anywhere else, it is clip-art.
- **Skeleton shimmer.** Adding a shimmer sweep to §6.11 "so it looks like loading". *Cure:* the skeleton is ruled paper; stillness is the loading language. If stakeholders demand motion, the answer is a faster server, not a shinier skeleton.

## 10. Quality gate — minimum bar before this theme may be used in a build

Every item must pass; one failure returns the build.

1. **No-JS test.** JavaScript disabled: the page is complete and fully readable; every number shows its final value; the frontispiece is open; every leaf header carries its numeral. Nothing is missing, pale, or clipped.
2. **Reduced-motion test.** `prefers-reduced-motion` emulated: no assembly, no draws, no counts, no veil — and the page loses nothing it needs. State changes (focus rules, error rules, folio swaps) still occur instantly.
3. **Density floor test.** No element's resting or starting state is below 55% ink density; a screenshot at any moment of any animation shows a legible page.
4. **End-state timer test.** With the observer and rAF artificially broken (devtools throttling + a thrown error in the reveal script), the 900ms global timer still lands every element at its final state.
5. **Contrast audit.** `--ink` on `--vellum` ≥ 15:1 measured; rubric text used only at ≥14px; no body text in taupe anywhere in the DOM (grep the built CSS/classes, not just the design file).
6. **Rubric census.** Per leaf: ≤1 rubric element (≤2 counting the fleuron). Counted in review, per leaf, on the real page.
7. **Motion census.** Every animation on the page appears in §5's table. Zero translate-based reveals; the only transforms are plate settles inside frames.
8. **Apparatus agreement.** Folio count, contents list, and running-head part names are generated from one structure and agree exactly — change a leaf, and all three update without hand-editing.
9. **Colophon truth check.** Every claim in the footer is verified against the shipped build (fonts actually loaded, year current, privacy claims literally true). One false claim fails the build outright.
10. **Rule crispness.** At 200% zoom, every hairline is a clean 1px — no shadow-drawn rules, no half-pixel greys.
11. **Performance budget.** No animation library is loaded for this theme (the entire motion system is CSS transitions + one shared rAF loop + one observer); total theme JS ≤ 6KB gzipped excluding the router; the §6.6 flicker is the only infinite animation in the page's CSS (grep `infinite` — exactly one hit).
12. **Mobile pass.** At 375px: mark relocated to footer, folio in the running head, drop initials off, plate cards bordered and untruncated, contents numerals leading. Checked on a real narrow viewport, not a resized desktop guess.

## Part II — Deepening (50x standard)

Part I is the build spec: what each element is and how it moves. Part II is the deepening pass ordered for the 50x standard — it takes every element in §6 and adds the layers a second builder would otherwise have to invent (and would invent differently): the millisecond choreography, the full state matrix on desktop and touch, the behaviour at three breakpoint bands, the edge cases and failure modes, the accessibility spec, and the exact tokens consumed. It then adds the theme-level layers Part I did not carry: a complete component inventory, the copywriting voice, three further worked examples with scroll timelines, the full-page scroll choreography map, the whole-page performance budget, and the build order. Nothing in Part II redesigns anything in Part I; where a number in Part II refines a number in Part I (a start density raised for small text, a breakpoint band mapped onto Part I's device points), Part II states the refinement and the reason.

**Shared deepening tokens.** Defined once here; every element entry in §II.1 lists the subset it consumes, plus its own element-scoped tokens.

- Easings (from §5): `--ease-press: cubic-bezier(0.22, 0.61, 0.21, 1)`; `--ease-impression: cubic-bezier(0.37, 0, 0.2, 1)`; `--ease-leaf-fade: cubic-bezier(0.45, 0, 0.55, 1)`.
- Density steps (colour-mixes in `--vellum`, per §2): `--ink-55`, `--ink-70`, `--ink-85` (ink at 55/70/85%); `--rubric-70` (rubric mixed 70% toward `--taupe`, the swell's start); `--taupe-60`, `--taupe-40` (taupe mixed toward vellum, for rest-state furniture). Measured effective contrast on `--vellum`: `--ink-55` ≈ 5.9:1, `--ink-70` ≈ 8.6:1, `--ink-85` ≈ 11.8:1, `--ink` 15.4:1, `--rubric` 6.9:1, `--rubric-70` ≈ 4.1:1, `--taupe` 3.2:1.
- Rhythm (from §4): `--column: 640px`; `--space-leaf: 96px`; `--space-part: 56px`; `--space-note: 24px`; `--space-line: 8px`; `--head-h: 57px` (49px in the <768 band); `--rule: 1px`.
- Global: `--timer-endstate: 900ms` (the §5 end-state timer); `--lerp-scroll: 0.12` (the shared rAF loop's smoothing factor); one shared scroll listener and one IntersectionObserver serve the whole page — no element in Part II may create its own.

## II.1 Per-element deepening

Each entry follows the same six layers, in order: **Timeline** (millisecond choreography from the trigger), **States** (desktop and touch), **Breakpoints** (≥1200px / 768–1199px / <768px), **Edge cases**, **Accessibility**, **Tokens**. A state that does not exist for an element is stated as not existing, with the reason — an absent state is a designed state, not a gap.

### II.1.1 Title-page assembly (§6.1)

**Timeline.** Trigger: `DOMContentLoaded` + 50ms (= t0), gated on `document.fonts.ready` with a hard cap — if the fonts have not settled by t0 + 850ms, the assembly starts anyway in the fallback serif and the end-state timer (§5) governs; a title page that waits for a font is a page that arrives late to its own opening. All five lines begin at their start density (title and rules at `--ink-55`; the two apparatus lines — imprint and place — begin at `--ink-70`, a Part II refinement: at 12.5px, 55% density is ≈5.9:1, below AA for small text even transiently, so small lines start at 70% ≈ 8.6:1; the §10 density floor is a floor, not a target).

| Beat | Time | What happens |
|---|---|---|
| 1 | t0 → t0+400ms | Imprint line gains ink 70%→100%, `--ease-impression` |
| 2 | t0+160 → t0+560ms | First rule: border-colour `--taupe-40` → `--ink` |
| 3 | t0+320 → t0+720ms | Title gains ink 55%→100% |
| 4 | t0+480 → t0+880ms | Second rule, as beat 2 |
| 5 | t0+640 → t0+1040ms | Place line gains ink 70%→100% |
| 6 | t0+1040ms | Assembly-complete: the §6.5 swell is triggered; the session flag is set (no replay on revisit) |
| 7 | t0+1040 → t0+1540ms | Rubric swell (§6.5) runs; at t0+1540ms the hero is fully settled |

If focus lands anywhere inside the title leaf before beat 6 (a keyboard visitor tabbing immediately), the remaining beats are cancelled and every line jumps to 100% in one frame — nobody waits at a door for the printing to finish.

**States.**

| State | Desktop | Touch |
|---|---|---|
| Rest (pre-JS / no-JS) | Fully inked at 100%; this is the server-rendered state | Identical |
| Assembling | Beats 1–7 as above | Identical, stagger compressed (see Breakpoints) |
| Settled | All lines 100%; initial at full rubric | Identical |
| Hover / focus | No element of the assembly is interactive; no hover state exists. Focus entering the leaf cancels to settled (above) | No hover; a tap on the title does nothing — it is a title, not a control |
| Active | Does not exist — nothing here is pressable | Does not exist |
| Scrolled-past | Unchanged at 100%; the assembly never reverses or replays | Identical |
| Disabled | Does not exist — the hero cannot be disabled; if the page's hero content is missing, the leaf is omitted from the DOM entirely rather than rendered empty | Identical |

**Breakpoints.** *≥1200px:* title 56px, stagger 160ms, total settle 1,540ms. *768–1199px:* title 44px, stagger 140ms, each line 380ms — total settle ≈1,420ms; the column is unchanged (640px max) so only the type and tempo narrow. *<768px:* title 40px, stagger 120ms (per §6.1's mobile variant), each line 400ms — total settle 1,380ms including the swell; the imprint line may wrap to two lines, and if it does, both wrapped lines are one beat (the line is the unit, never the row).

**Edge cases.** *Slow network:* the title leaf's CSS (≤2KB) is inlined in `<head>` with the pre-paint script, so the assembly never waits on the main stylesheet; if the stylesheet is delayed past 900ms, the end-state timer fires on the inline styles alone and the leaf sits printed in fallback serif until the sheet lands, then re-renders in Cormorant with no re-assembly. *No canvas/WebGL:* irrelevant by construction — the assembly is colour transitions on text; there is no canvas anywhere in this theme. *Low-power device:* if `prefers-reduced-motion` or a battery-saver profile is detected, the assembly is skipped wholesale (static leaf) — it is the page's most expendable ceremony. *Content longer than designed:* a title wrapping to 3 lines assembles as one beat (beat 3 covers the whole H1); beyond 3 lines the content is wrong for a title page and §9's costume rule applies — shorten the title, do not shrink the type below 40px to fit it. *Content shorter:* a title leaf with no place line omits beat 5 and the swell triggers at t0+880ms — beats are skipped, never padded with pauses. *Scrolling back up:* nothing; a printed page does not unprint, and the session flag survives in-page navigation.

**Accessibility.** The H1 is the page's only `<h1>` and is present in the accessibility tree at full text from t0 — density is a paint property, never `aria-hidden`, never `visibility`. Focus order through the leaf: skip link → running-head Contents anchor → any link inside the title leaf (rare; the imprint is not a link) → contents leaf. No focusable element exists inside the assembly itself, so no visible-focus styling is needed within it; focus entering the leaf triggers the cancel-to-settled rule above, which is also the visible guarantee that a keyboard visitor never reads a half-printed title. Contrast during assembly: title at its palest (55%) is ≈5.9:1 at 40–56px — passes AA for large text (≥24px) at every frame; apparatus lines never drop below 70% (≈8.6:1, AA at 12.5px). Touch targets: none in this element.

**Tokens.** `--ink-55`, `--ink-70`, `--ease-impression`, `--dur-assembly-line: 400ms`, `--dur-assembly-stagger: 160ms` (140/120 per band), `--fs-display: 56px` (44/40 per band), `--lh-display: 1.04`, `--space-part` (title leaf's internal gaps ride the part rhythm).

### II.1.2 Folio-advance progress (§6.2)

**Timeline.** The folio is scrubbed, so its timeline is written against scroll events, not a start trigger. The shared rAF loop runs at the display's refresh rate; each frame, the hairline fill's current value moves toward its target by `--lerp-scroll` (0.12) of the remaining distance.

| Beat | When | What happens |
|---|---|---|
| 1 | Page load | Folio renders at I (or is absent, no-JS); fill target = 1/N of track; fill starts at target — there is no load animation on the folio |
| 2 | Continuous scroll | Fill lerps toward the true fraction; after scroll stops, the fill settles within ~150ms (8 frames at 60fps closes ~63% of the remaining gap per 8 frames at lerp 0.12 — full settle ≈150–200ms) |
| 3 | Leaf *k*'s header crosses 50% viewport height | Numeral tick armed |
| 4 | Tick +0 → +200ms | Numeral crossfade: outgoing numeral 100%→55% density, incoming 55%→100%, stacked in the fixed box, `--ease-leaf-fade`; the running head's part name crossfades in the same 200ms (§6.13) — head and folio change in one beat, never two |
| 5 | Final leaf reached | Numeral shows N; fill target = 100%; folio then rests — no completion flourish, no colour change |
| 6 | Scroll back above a boundary | The reverse tick fires with the identical 200ms crossfade — the folio is the one element in the theme that *does* reverse, because it reports position, and a position report that only moves forward is a lie |

**States.**

| State | Desktop | Touch |
|---|---|---|
| Rest (leaf 1) | Numeral I in `--ink`; fill at 1/N | Same, folio inside the running head |
| Advancing | 200ms crossfade per beat 4 | Identical |
| Hover | None — the folio is not interactive and takes no hover state; a pointer over it changes nothing | No hover exists |
| Focus | Never focusable (`aria-hidden` furniture; the information is carried semantically by leaf headers) | Never focusable |
| Active | Does not exist | Does not exist |
| Scrolled-past | Shows the *current* leaf's numeral at all times — "scrolled-past" for the folio means the numerals it has left behind, which are simply not shown (§6.2) | Identical |
| Disabled | Does not exist; if the page has one leaf, the folio and fill are omitted entirely — a one-leaf page has no pagination to report | Identical |

**Breakpoints.** *≥1200px:* folio fixed at the top-right corner, Plex Mono 12px, box min-width 3.5ch right-aligned; fill is the running-head hairline (§6.13). *768–1199px:* the corner margin is too narrow to hold the folio clear of the column, so the folio moves into the running head, right-aligned beside the running title (Part I's below-1024 rule, mapped onto this band), 12px; fill spans the full head width. *<768px:* folio in the running head at 11px; the part name is dropped from the head (§6.13 mobile), so the head reads title — folio — fill; numeral box stays 3.5ch so ticks never shift the title.

**Edge cases.** *Many leaves:* a 14-leaf page reaches XIV (4ch) and a hypothetical 38-leaf page XXXVIII (7ch) — the box is a *minimum* width; it grows leftward into the margin (corner) or into the head's flexible space (in-head bands) and never pushes the column or the title, because both placements are out of flow or flex-absorbing. A page with more than 20 leaves is a design smell in this theme (§4: one idea per leaf) — the folio tolerates it, the quality gate questions it. *Very short page (no scroll):* fill sits at 100% with numeral I of I — correct, and the folio may be omitted if the single leaf is the whole page. *Slow network / no JS:* no folio element exists (JS-injected); leaf headers carry the numerals in static HTML, so pagination survives (§6.2 fallback). *Low-power:* the crossfade is the first cut — numeral swaps instantly, fill jumps leaf-to-leaf (the reduced-motion treatment, applied early). *Scroll back up:* beat 6 — reverse ticks, fill lerps back; the loop's boundary table is cached and recalculated only on resize, so reverse scrolling costs no layout reads. *Orientation change / resize:* boundary table recalculated once on `resize` (debounced 150ms); the folio never shows a stale leaf for longer than one recalculation.

**Accessibility.** `aria-hidden="true"` on the folio element itself — it is furniture duplicating information. The information is available semantically: every leaf header contains visually-hidden text "Leaf III of VII" (§6.2), so a screen-reader user traversing by headings receives the same position report a sighted user gets from the corner. The folio never receives focus and is skipped in tab order. Contrast: current numeral is `--ink` (15.4:1); the outgoing numeral during the 200ms crossfade dips to 55% (≈5.9:1) at 12px — below AA for small text *transiently*; this is accepted because the folio is decorative (aria-hidden) and the semantic equivalent is static text at full contrast — stated here so no builder "fixes" it by making the folio live region, which would announce every leaf change and badger the reader. Touch targets: none — the folio is not a control at any band.

**Tokens.** `--ink`, `--ink-55`, `--ease-leaf-fade`, `--dur-folio-tick: 200ms`, `--folio-box: 3.5ch`, `--fs-apparatus-mono: 12px` (11px <768), `--lerp-scroll`, `--head-h`.

### II.1.3 Ink-density leaf reveals (§6.3)

**Timeline.** Trigger: the leaf's IntersectionObserver callback (threshold 0.18 desktop / 0.12 in the <768 band, rootMargin bottom −8%). t0 = the frame the callback fires.

| Beat | Time | What happens |
|---|---|---|
| 1 | t0 | Leaf's apparatus header begins its density ramp 55%→100% |
| 2 | t0+80ms | Body text begins the same ramp |
| 3 | t0+120ms | Plates (if any) begin: opacity ramp on the same 600ms curve, so picture follows words as a press sheet is read |
| 4 | t0+600ms | Header reaches 100% |
| 5 | t0+680ms | Body reaches 100% |
| 6 | t0+720ms | Plates reach 100%; the leaf is *printed*; the observer unobserves it in the same frame |
| 7 | Any time | If three leaves are already ramping when a fourth triggers, the fourth (and any beyond) jump straight to 100% at their t0 — the concurrency cap (§6.3) is a timeline rule, not a queue: nothing waits |

On a fast scroll that carries a leaf from below the fold to above the viewport between two observer callbacks, the leaf may never intersect at threshold — the observer's `isIntersecting` check on the *next* leaf's callback sweeps all earlier unprinted leaves to 100% instantly. A leaf the visitor has already passed is printed, never left pale above them.

**States.**

| State | Desktop | Touch |
|---|---|---|
| Pre-entry | 55% density — fully legible by design (§10 gate 3) | Identical |
| Entering | Beats 1–6 | Identical, threshold 0.12 |
| Printed | 100%, terminal state; observer detached | Identical |
| Hover / focus | The reveal has no hover or focus state of its own; interactive children keep their own (§6.9, §6.10). Focus entering an unprinted leaf (keyboard jump via anchor or find-in-page) prints it instantly — focus never lands on a half-printed leaf | Focus-equivalent (switch control / VoiceOver swipe landing) prints instantly, same rule |
| Active | Does not exist at leaf level | Does not exist |
| Scrolled-past | 100%, unchanged; reveals never reverse (§6.3) | Identical |
| Disabled | Does not exist; a leaf whose content failed to load is not "disabled" — it resolves to §6.11's errata error state | Identical |

**Breakpoints.** *≥1200px:* threshold 0.18, stagger 80/120ms, concurrency cap 3. *768–1199px:* threshold 0.15 (leaves are the same 640px column but viewports are shorter relative to leaf height), stagger unchanged, cap 3. *<768px:* threshold 0.12 (per §6.3), stagger tightened to 60/100ms, cap 2 — a phone ramping three leaves of 19px text is painting more than it can hold at 60fps, and the cap is where the theme chooses the reader over the effect.

**Edge cases.** *Slow network:* leaves are server-rendered; a leaf whose plate image is still loading reveals its text on schedule and the plate joins at beat 3 of *its own* readiness (gated on `img.decode()`, §6.4's rule applied to all plates) — text never waits for pictures. *No JS:* no pre-states are ever applied; every leaf is born at 100% (§6.3 fallback). *No `@property` support:* the class-step fallback (d55/d70/d85/d100 on a 150ms interval) reproduces the ramp in four steps — visibly steppier, identical in outcome and timing (4 × 150ms = 600ms). *Low-power device:* if the shared rAF loop detects sustained frame times >24ms, remaining unprinted leaves are set to 100% and the observer is disconnected — the page degrades to a printed book, which is its natural state anyway. *Content longer than designed:* a leaf taller than 2× viewport height triggers on its header alone (threshold is met by the header entering); its lower half is already at 100% when reached, because the ramp is per-leaf, not per-paragraph — a long leaf never leaves its own foot pale. *Content shorter:* a two-line leaf still gets its 600ms ramp; brevity is not a reason to skip the press. *Scrolling back up:* nothing reverses, nothing replays (§6.3 states). *Find-in-page / anchor jump:* the target leaf prints instantly (States, above) — a visitor who teleports is not made to watch the journey's animations.

**Accessibility.** Density is paint-only: the DOM and accessibility tree hold full text from server render, so a screen reader reads a leaf identically whether it is at 55% or 100% — there is no `aria-hidden` phase and no live announcement of reveals. Contrast floor: body text at its palest is `--ink-55` ≈ 5.9:1 at 19px — passes AA for normal text (≥4.5:1) at *every frame* of the ramp, which is the entire point of the 55% floor; apparatus text inside a leaf starts at 70% (≈8.6:1) per the §II.1.1 refinement. Focus visibility is unaffected by density (focus outlines are taupe→ink state changes on the focused element, §6.9/§6.16, rendered at full contrast independent of the leaf's ramp). Touch targets inside leaves are unaffected — density never changes geometry. Reduced-motion: no ramp at all (§6.3 variant) — leaves are 100% at all times and the observer is never created.

**Tokens.** `--ink-55`, `--ink-70`, `--ink-85`, `--ink`, `--ease-impression`, `--dur-reveal: 600ms`, `--dur-reveal-stagger-head: 80ms`, `--dur-reveal-stagger-plate: 120ms` (60/100 <768), `--reveal-threshold: 0.18` (0.15 / 0.12 per band), `--reveal-cap: 3` (2 <768).

### II.1.4 Book-opening frontispiece (§6.4)

**Timeline.** Two gates precede the trigger: the plate's `img.decode()` must have resolved, and the plate must cross 35% visibility. t0 = the later of the two. The frame and caption are at 100% density from server render — they are not in this timeline at all; only the plate moves.

| Beat | Time | What happens |
|---|---|---|
| 1 | t0 → t0+700ms | Plate settles 102%→100% scale inside its fixed frame, `--ease-impression` |
| 2 | t0 → t0+900ms | Clip widens symmetrically: `inset(0 50% 0 50%)` → `inset(0 0 0 0)`; both edges travel at identical rates |
| 3 | t0+700ms | Plate reaches final scale and is still — the picture settles 200ms before the book finishes opening (§6.4's order is law) |
| 4 | t0+900ms | `clip-path` is removed entirely (`none`) so no clipping cost or edge artefacts persist; element marked opened, observer detached |

**States.**

| State | Desktop | Touch |
|---|---|---|
| Pre-entry | Centre slit inside a complete frame; caption fully inked below | Identical |
| Opening | Beats 1–4 | Identical, compressed (Breakpoints) |
| Opened | Clip removed; plate at rest in its frame | Identical |
| Hover | None — the plate is not a control and takes no hover state (if a host insists the frontispiece link to its detail leaf, the *caption* becomes the link and takes §6.9's underline; the image itself still does not respond) | No hover; a tap on a linked plate follows the caption's link target — the whole figure is the anchor's hit area in that case only |
| Focus | The figure is not focusable; a linked caption shows §6.9's held underline on `:focus-visible` | Same via keyboard/switch focus |
| Active | Does not exist for the plate itself | Does not exist |
| Scrolled-past | Stays open; never re-closes | Identical |
| Disabled | Does not exist; a plate whose image failed is not disabled but *absent* — see Edge cases | Identical |

**Breakpoints.** *≥1200px:* clip travel from 50% inset, 900ms; scale settle on. *768–1199px:* clip from 46% inset, 825ms; settle on — the gesture shortens with the plate. *<768px:* clip from 42%, 750ms, scale settle dropped entirely (§6.4 mobile variant): one motion, not two, on the band least able to composite both.

**Edge cases.** *Slow network:* the decode gate means the opening simply waits, frame and caption already printed; if the plate is scrolled past before decoding finishes, the opened state is applied instantly when decode resolves — no animation performed for an audience that has left. *Image fails to load:* the frame collapses to a caption-only plate, the alt text set as an italic caption line (§6.4) — an honest missing plate; the collapse is a layout event, so the frame's reserved aspect-ratio box (set from the image's declared dimensions) collapses only on the `error` event, never speculatively. *No canvas/WebGL:* nothing in this element uses either; clip-path and transform are core CSS. *Low-power device:* the opening is replaced by §6.4's reduced-motion treatment (85%→100% density fade, 200ms) under battery-saver, even if the user has not requested reduced motion — theatre is cut before information, always (§II.6 cut order). *Unusual aspect ratios:* the clip is a horizontal inset and is aspect-agnostic; a portrait plate taller than the viewport reveals on the same 35% threshold measured against the *frame*, and the opening still completes within one screen of scrolling because the threshold is on visibility fraction, not on the plate's foot reaching the fold. *Scrolling back up:* the plate stays open; the book does not close behind the reader.

**Accessibility.** The `<figure>`/`<figcaption>` semantics are native; the clip is a paint effect and the image is in the accessibility tree with its full alt text from server render — a screen reader encounters the frontispiece as a complete image regardless of the opening's progress. The alt text must describe the artefact as a frontispiece deserves (subject, place, what matters in it — §8's worked alt is the model), never "image" or a filename. Contrast: the caption is `--ink` italic 15px at 15.4:1. Focus order: the figure is skipped unless its caption is a link, in which case the caption link sits in normal flow order after the title leaf's text. Touch targets: none, unless linked — then the figure-plus-caption block is the target, hundreds of pixels in both dimensions, far above the 44px floor.

**Tokens.** `--dur-open: 900ms` (825 / 750 per band), `--open-inset: 50%` (46% / 42% per band), `--dur-plate-settle: 700ms`, `--ease-impression`, `--rule`, `--taupe` (frame), `--open-threshold: 0.35`.

### II.1.5 Rubricated initial swell (§6.5)

**Timeline.** Trigger: §6.1's beat 6 — assembly complete. On the ≥1200 band that is load + 1,040ms; the swell is specified relative to that trigger (t0), not to page load, so it inherits whatever the assembly's band timings were.

| Beat | Time | What happens |
|---|---|---|
| 1 | t0 | Initial sits at `--rubric-70` — present, muted, already printed with the title's first pass |
| 2 | t0 → t0+500ms | Saturation mix 70%→100% toward full `--rubric`, `--ease-press` — the letter warms; no size, weight, or position change at any frame |
| 3 | t0+500ms | Settled at 100% rubric, static forever; the swell never repeats, including on SPA revisit (the §6.1 session flag covers it) |

If the assembly was cancelled early (focus entry, §II.1.1), the swell is cancelled with it — the initial renders at 100% immediately. A swell performed for a reader who has already started reading is a interruption, not a flourish.

**States.**

| State | Desktop | Touch |
|---|---|---|
| Assembling | At `--rubric-70` from the title's own beat (§6.1 beat 3) | Identical |
| Swelling | Beat 2 | Identical |
| Settled | 100% `--rubric`, permanent | Identical |
| Hover | Explicitly none — the initial does not respond to the pointer (§6.5); a hover effect here would make the page's one flourish into a toy | No hover exists |
| Focus | Not focusable — it is a glyph inside the H1 | Not focusable |
| Active | Does not exist | Does not exist |
| Scrolled-past | Unchanged | Identical |
| Disabled | Does not exist — if the title has no first letter worth rubricating (see Edge cases), the span is simply not emitted | Identical |

**Breakpoints.** Identical in all three bands — the swell is 500ms of colour at every size. Only its trigger time moves with the assembly's band timings: ≈load+1,040ms (≥1200), ≈load+940ms (768–1199: 5 beats at 140ms stagger, last line ends 380ms after its start at +560 → assembly completes ≈940ms), ≈load+880ms (<768, per §6.1's mobile stagger).

**Edge cases.** *Title begins with punctuation or a numeral:* the build wraps the first *alphabetic* character; a leading quote or figure stays in `--ink`. A title that is purely numeric has no initial and gets no swell — the flourish is a letter's, and forcing it onto a digit breaks the fiction. *Font failure:* the swell is a colour transition and runs identically in the fallback serif; nothing about it depends on Cormorant loading. *Very long titles:* the initial stays on the first line at display size; if the title wraps past three lines the content is at fault (§II.1.1), not the swell. *Low-power:* the swell survives battery-saver cuts that kill the §6.6 flicker — it is a single 500ms one-shot, and the cut order (§II.6) spends ambient loops before one-shot ceremonies. *Scrolling back up / revisit:* settled state persists; the session flag prevents replay. *Forced-colours mode (Windows High Contrast):* `color-mix` is overridden by the OS; the initial renders in the system highlight colour — accepted and correct: the reader's contrast needs outrank the scribe's red, and the letter remains distinguishable by the OS's own scheme.

**Accessibility.** The `<span class="rubric-initial">` splits the H1's first glyph into an inline element; screen readers read the heading as continuous text — the span carries no `aria-hidden`, no separate label, and the letter is never duplicated in a visually-hidden string (a heading that reads "P P oems" is the classic failure here; the build must not add one). Contrast: at its palest (`--rubric-70`, ≈4.1:1) the glyph is 40–56px display text — AA large-text requires 3:1, so every frame passes; settled at 6.9:1 it passes AA for normal text as well. The swell is colour-only and conveys no information — nothing is communicated by the saturation that is not present in the letter itself. Reduced-motion: static 100% from first paint (§6.5).

**Tokens.** `--rubric`, `--rubric-70`, `--dur-swell: 500ms`, `--ease-press`.

### II.1.6 Candle-steady ornament flicker (§6.6)

**Timeline.** A loop has no trigger beat; its choreography is the cycle itself. The flicker starts when the title leaf's fleuron finishes its §6.7 draw (the animation class is applied in the draw's completion frame, and because the cycle's 0% keyframe is opacity 1.00, the handover is invisible).

| Beat | Cycle time | Opacity | Note |
|---|---|---|---|
| 1 | 0.0s (0%) | 1.00 | Rest — the cycle starts and ends at full ink |
| 2 | ≈2.0s (18%) | 0.99 | First dip — a breath, not a blink |
| 3 | ≈4.5s (41%) | 1.00 | Recovery |
| 4 | ≈6.9s (63%) | 0.98 | The cycle's deepest point — still a 2% band |
| 5 | ≈9.0s (82%) | 0.99 | Rising |
| 6 | 11.0s (100%) | 1.00 | Loop restarts seamlessly |

Between keyframes, segments ease `ease-in-out` individually (§6.6) — the fastest change anywhere in the cycle is ≈1% opacity per 900ms. An IntersectionObserver pauses the animation (`animation-play-state: paused`) whenever the title leaf is more than one viewport away and resumes it on return: the candle is not tended in rooms nobody is in. This pause is a Part II addition for battery; it changes nothing a visitor can see, because a visitor who cannot see the ornament cannot see it pause.

**States.**

| State | Desktop | Touch |
|---|---|---|
| Rest | There is none — flickering *is* its rest state (§6.6), rationed to this one instance for exactly that reason | Identical |
| Hover / focus / active | None — the ornament is `aria-hidden` furniture, never focusable, never pointer-responsive; the SVG has `pointer-events: none` so it cannot even intercept a click meant for the rule beneath | Identical |
| Scrolled-past | Loop continues if the leaf returns to view; paused while away (Timeline) | Identical |
| Disabled | Does not exist as a state; the flicker is *removed* (not disabled) under reduced-motion, print, battery-saver, or `prefers-reduced-data` — in all four cases the ornament is simply static at 100% | Identical |
| Document hidden | The browser pauses CSS animations on hidden tabs automatically; on return, the cycle resumes mid-phase — no catch-up, no jump | Identical |

**Breakpoints.** Identical in all three bands — at a 2% band there is nothing to simplify (§6.6). The ornament itself scales with the column (§6.7), and the flicker rides it unchanged at 375px and at 1440px.

**Edge cases.** *No title leaf on the page:* no flicker. Part I rations the flicker to the title leaf's instance; a detail or catalogue page does not promote its first part-title fleuron to flicker instead — the ration is one per *book*, and pages without a title leaf are simply pages where the candle is not lit. *CSS animations stripped/unsupported:* the ornament is static at 100% — indistinguishable in any screenshot, which is §6.6's stated test. *Low-power / battery-saver / reduced-data:* animation removed; this is the first cut in the §II.6 order, before every other motion in the theme. *Print:* `@media print` removes all animation; the ornament prints at full ink. *The builder's temptation — a second flicker* (footer fleuron, mark): refused in §9's ornament-spam rule; two breathing things on one page is a séance, not a reading room. *Scrolling back up:* the loop neither restarts nor syncs to scroll; it is time-based and indifferent to the reader's position, which is what makes it feel like candlelight rather than a scroll effect.

**Accessibility.** The ornament is `aria-hidden` and the flicker conveys no information — nothing is announced, nothing needs announcing. Photosensitivity: the cycle's maximum luminance change is 2% of one small red ornament, gradual over seconds — orders of magnitude below WCAG 2.3.1 flash thresholds (no flash, no red flash, no luminance step); it is safe by construction, not by testing luck. Contrast: the ornament is furniture (its carrier rule is `--taupe`, 3.2:1, permitted for non-textual decoration that duplicates no information — the part-title it ornaments is full-ink text). Focus: never in the tab order. Touch targets: none — `pointer-events: none` throughout.

**Tokens.** `--dur-flicker: 11s`, `--flicker-floor: 0.98`, `--rubric` (fleuron stroke at rest), keyframes `candle-steady` (defined once, theme-wide).

### II.1.7 Self-drawing fleuron rules (§6.7)

**Timeline.** Trigger: the ornament crosses 50% visibility. t0 = observer callback. All dash math uses `pathLength="100"` (§6.7), so offsets below are percentages of each sub-path.

| Beat | Time | What happens |
|---|---|---|
| 1 | t0 → t0+260ms | Left rule draws: dashoffset 100→0, `--ease-press` |
| 2 | t0+200 → t0+440ms | Fleuron draws over 240ms, starting while the left rule still has 60ms to run — the hand does not lift between rule and stamp |
| 3 | t0+420 → t0+680ms | Right rule draws over 260ms, starting 20ms before the fleuron finishes |
| 4 | t0+440 → t0+640ms | Fleuron stroke settles `--taupe` → `--rubric` (200ms colour transition overlapping beat 3) — drawn in pencil, inked in red |
| 5 | t0+680ms | Draw complete. If this is the title leaf's instance, the §6.6 flicker class is applied in this frame |

On a fast scroll, queued ornaments serialise 100ms apart (§6.7); if more than three are queued, the rest render already drawn — the queue serves the reader's eye, and an eye that has passed an ornament does not need it drawn retroactively.

**States.**

| State | Desktop | Touch |
|---|---|---|
| Pre-entry | Dashoffset 100 on all three sub-paths; the SVG box occupies its full layout space — zero shift when drawn | Identical |
| Drawing | Beats 1–5 | Single-breath variant (Breakpoints) |
| Drawn | Final strokes and colours; terminal state | Identical |
| Hover / focus / active | None — `aria-hidden` furniture, `pointer-events: none`, never focusable | None |
| Scrolled-past | Stays drawn | Identical |
| Disabled | Does not exist; if SVG is blocked, the element is *replaced* by its CSS hairline fallback (§6.7), which has no states at all | Identical |

**Breakpoints.** *≥1200px:* the full 680ms sequence. *768–1199px:* the full sequence — the ornament is fluid SVG and the column is unchanged, so nothing about the draw needs the wide band. *<768px:* the sequence compresses to one simultaneous 400ms draw of all three sub-paths (§6.7 mobile variant); the fleuron's colour settle still lands at the draw's end (t0+400 → t0+550ms, 150ms transition).

**Edge cases.** *No JS:* the SVG renders in its natural, fully drawn state — the pre-state is JS-applied (§6.7), so the fallback is the finished ornament, not an absence. *SVG blocked or stripped (some email/webview pipelines):* the part-title keeps its CSS `border-top` fallback, suppressed only when the `.has-svg` class is present — a plainer rule, but the part is never left undivided. *Slow network:* the SVG is inline in the HTML; there is no asset to wait for. *Low-power:* the draw is replaced by §6.7's reduced-motion treatment (whole-SVG density fade 85%→100%, 200ms) under battery-saver. *Many part-titles (a long catalogue page):* the 100ms serialisation plus the three-queue cap (Timeline) bounds the cost; a page with 12 part-titles draws at most the three nearest the reader's position and prints the rest. *Scrolling back up:* drawn is terminal; nothing undraws. *Print:* the SVG prints in its natural state — a printed page of this site shows its fleurons ruled, as it must.

**Accessibility.** `aria-hidden="true"` on the SVG; the part-title it divides is a real heading with real text, so the ornament duplicates no information and announces nothing. Contrast: the rules are `--taupe` furniture (3.2:1, decorative); the fleuron at completion is `--rubric` (6.9:1) — it is the theme's mark, not text, and exceeds the 3:1 non-text threshold regardless. Focus: never in the tab order. Touch targets: none — the ornament cannot be tapped, swiped, or triggered; it is ruled paper.

**Tokens.** `--dur-draw-rule: 260ms`, `--dur-draw-fleuron: 240ms`, `--draw-offset-fleuron: 200ms`, `--draw-offset-right: 420ms`, `--dur-draw-mobile: 400ms`, `--ease-press`, `--taupe`, `--rubric`, `--ornament-w: 320px` (viewBox units; rendered fluid to column width).

### II.1.8 Mono print-run counters (§6.8)

**Timeline.** Setup (before any trigger): JS rewinds a counter's displayed value to its 62% start *only if* the element is below the fold at setup time; an element already visible is never rewound — a number the visitor has read does not un-print (§6.8's rule, made a timeline law here). Trigger: the data line crosses 40% visibility. t0 = callback.

| Beat | Time | What happens |
|---|---|---|
| 1 | t0 | Colour steps `--taupe` → `--ink` (the sanctioned mono-in-ink moment, §3); counting begins from the 62% start value (rounded to the nearest integer) |
| 2 | t0 → t0+900ms | Value rises with `--ease-press` applied to progress; `textContent` written only on whole-number change; grouping via `Intl.NumberFormat` at every write |
| 3 | t0+900ms | Lands on the exact value — no overshoot, no bounce, no terminal flourish |
| 4 | t0+900 → t0+1200ms | Colour settles back over 300ms — to `--taupe` if the same figure is printed in ink elsewhere on the leaf (the detail leaf's facts block, §7); to `--ink` if this counter is the figure's only appearance, per §2's rule that taupe may not carry unique reading matter. Part II states this landing rule explicitly because §6.8 alone leaves it ambiguous |

**States.**

| State | Desktop | Touch |
|---|---|---|
| Static (pre-trigger / no-JS) | Final formatted value, in the landing colour of beat 4 | Identical |
| Counting | Value rising, `--ink` | Identical, 750ms duration |
| Landed | Final value; inert forever | Identical |
| Hover / focus / active | None — the counter is a text span, not a control; it takes no pointer or focus state | None |
| Scrolled-past | Final value; never recounts on re-entry (§6.8) | Identical |
| Disabled | Does not exist. A figure that is no longer true (the edition sold out mid-session) is *corrected*, not disabled: the host updates the text in place, in the errata voice if the change is material ("340 — corrected: out of print") | Identical |

**Breakpoints.** *≥1200px:* 900ms count. *768–1199px:* 900ms — the tally's tempo is not a layout property. *<768px:* 750ms (§6.8 mobile variant). At every band, a counter whose value is <10 counts in single steps from its rounded 62% start (8 counts 5→6→7→8): three steps in 900ms reads as a tally clerk's ticks, which is correct; a counter to a value of 0 or 1 is forbidden — a nought is printed statically or stated as words ("Out of print"), never tallied.

**Edge cases.** *Large values:* 1,250,000 counts in the same 900ms — the tally is ceremonial, not proportional; grouping separators appear and shift as digits grow, but `tabular-nums` plus right-alignment of the data line's figure column (apparatus lines right-align their figures where a column of them exists) prevents horizontal jitter of surrounding text. *Slow network / late JS:* if the script arrives after the visitor has scrolled past a counter, the setup check finds it above the fold and never rewinds it — late enhancement must not rewrite history the visitor already read. *No JS:* final values in static HTML (§6.8). *Low-power / battery-saver:* counters print statically — the tally is ceremony, and ceremony is cut before information (§II.6). *Content longer than designed:* more than 4 counters on a page is refused at review (§6.8's cap); the fifth figure is printed statically — a page that tallies everything tallies nothing. *Scrolling back up:* landed counters are inert text. *Locale:* `data-format` drives grouping (en-GB in §6.8's example); a builder who hard-codes commas for a de-DE build has printed a false number in the theme whose capital offence is false apparatus (§9).

**Accessibility.** The counting span is `aria-hidden="true"` at all times, paired with a visually-hidden sibling span carrying the final formatted value — assistive technology always receives the true figure, never a mid-count fragment (a screen reader passing the line at t0+450ms must hear "1,250", not "943"). On landing, nothing changes for AT: the hidden sibling was always the source of truth. Contrast: while counting, `--ink` (15.4:1); landed, per beat 4's rule — 15.4:1 if unique, or taupe (3.2:1) only when the identical figure appears in ink within the same leaf, satisfying §2's redundancy condition. Focus: never focusable. Touch targets: none.

**Tokens.** `--dur-count: 900ms` (750ms <768), `--count-start: 0.62`, `--dur-count-settle: 300ms`, `--ease-press`, `--ink`, `--taupe`, `--fs-apparatus-mono: 12px`, `font-variant-numeric: tabular-nums` (set on the counter class, §6.8).

### II.1.9 Rubric underline hover (§6.9)

**Timeline.** Trigger: pointerenter or `:focus-visible` on the link. t0 = trigger frame.

| Beat | Time | What happens |
|---|---|---|
| 1 | t0 → t0+240ms | Draw: `background-size` 0%→100% at 1px height, from the reading-start edge, `--ease-press` |
| 2 | While held | Line rests at full width for as long as hover or focus lasts — focus holds it indefinitely (§6.9) |
| 3 | Pointer leaves / blur, t1 → t1+180ms | Retreat: background-position flips to the reading-end edge in the same frame the retreat starts, size 100%→0% over 180ms — the line exits the way a pen lifts |
| 4 | Press (pointerdown on the link) | Line thickens 1px→2px for the press, paired with §6.10's darkening; on release it returns to 1px if still hovered, or retreats per beat 3 |

**States.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Body links: no line. Apparatus links (contents, head, footer): permanent `--taupe` line at 60% | Body links carry the permanent taupe underline (identification without hover, §6.9 mobile variant); apparatus links as desktop |
| Hover | Beat 1 → full rubric line | No hover on coarse pointers; where a tablet reports hover capability, desktop behaviour applies — the switch is the `(hover: hover)` media query, not the breakpoint band |
| Focus (`:focus-visible`) | Beat 1, held; *plus* a 1px `--taupe` outline at 2px offset (§6.9) — two signals, because the draw alone is a colour change | Same for keyboard/switch focus |
| Active | 2px line (beat 4) | Tap: 2px line for 150ms before navigation (§6.9) |
| Visited | Permanent taupe underline at rest; the rubric draw still works over it (§6.9) | Identical |
| Scrolled-past | Not a link state — links inside a printed leaf are simply at rest; the leaf's §6.3 reveal never alters link states | Identical |
| Disabled | Designed out: this theme has no disabled links. An unavailable destination is rendered as non-link text (§6.15's unavailable entry), so nothing pretends to be a link that is not. If a host framework forces a disabled link, it takes `--taupe`, no draw, `tabindex="-1"`, and `aria-disabled="true"` — stated here so the forced case is still specified | Identical |

**Breakpoints.** *≥1200px:* as specified. *768–1199px:* as specified for fine pointers; coarse-pointer tablets take the touch column. *<768px:* the touch column — permanent taupe underlines in body copy, no draw animation (there is no hover to draw for), tap gives the 150ms 2px active state.

**Edge cases.** *Multi-line links:* the background gradient applies per line fragment, so a two-line link draws on both lines simultaneously — correct and rather beautiful (the editor rules both lines at once). A body link wrapping past two lines is a copy fault, not a styling case: shorten the link text. *RTL content:* the draw starts from the reading-start edge — in RTL that is the right; implement with logical background positioning (`background-position-x` set per `dir`), never a hard-coded left, or the pen draws backwards. *Forced-colours mode:* background images may be stripped by the OS; a `@media (forced-colors: active)` rule restores a native `text-decoration: underline` on all theme links — the reader's system wins, and the link remains a link. *Slow network / no JS:* the underline is pure CSS on final-state elements; there is no JS in this element at all. *Low-power:* kept in every mode — a 240ms paint on one line box is beneath notice; under reduced-motion the line appears instantly at full width (§6.9 variant). *Scrolling back up:* no interaction with scroll; a link hovered while the page scrolls under a stationary pointer retreats and redraws as the browser re-fires pointer events — standard behaviour, unmodified.

**Accessibility.** *Visible focus:* dual signal — the held rubric draw (`--rubric` on `--vellum`, 6.9:1) plus the 1px taupe outline at 2px offset (3.2:1 against the ground, above the 3:1 non-text contrast floor for focus indicators); either alone is visible, together they are unmistakable. *Link identification:* on touch bands, the permanent taupe underline; on fine-pointer bands, apparatus links carry the permanent taupe line and body links are identified by the draw on hover/focus and the permanent line once visited — colour is never the sole carrier of *focus*, which is the state that must never be missed. *Labelling:* link text is the label — the theme forbids "click here" by voice rule (§II.3), and a link whose text does not state its destination fails review, not just politeness. *Contrast at every state:* rest apparatus line taupe 3.2:1 (non-text, ≥3:1 ✓); hover/focus rubric 6.9:1 ✓; active 2px rubric 6.9:1 ✓; visited taupe line 3.2:1 ✓. *Touch targets:* inline text links are exempt from the 44px rule as in-sentence links, but apparatus links in the contents leaf and footer sit in rows of ≥44px height (§6.18, §6.17) — the theme's navigation links are always full-row targets.

**Tokens.** `--rubric`, `--taupe-60` (rest apparatus line), `--dur-underline-draw: 240ms`, `--dur-underline-retreat: 180ms`, `--underline-h: 1px`, `--underline-h-active: 2px`, `--ease-press`, `--focus-offset: 2px`.

### II.1.10 Ink-darkening click (§6.10)

**Timeline.** Trigger: `pointerdown` on an entry (or Enter/Space `keydown` for keyboard parity). t0 = press.

| Beat | Time | What happens |
|---|---|---|
| 1 | t0 → t0+60ms | Entry's ink text transitions `--ink` → `--ink-pressed` — a press is fast; the darkening must feel simultaneous with the finger |
| 2 | Release (pointerup / keyup) at t1 → t1+150ms | Colour returns `--ink-pressed` → `--ink`, `--ease-press` |
| 3 | If the press navigates | Beat 2 is replaced: the darkened state *holds* through §6.12's veil fade-in (≤300ms) — the pressed entry is the last thing seen darkening as the leaf turns (§6.10) |
| 4 | `pointercancel` (a touch press that becomes a scroll) | Treated exactly as a release: beat 2 runs from the cancel frame. An entry left dark after the page has scrolled is a stuck state and a build fault — this beat exists because touch scrolling makes it the element's most likely real-world failure |

Only the entry's ink text darkens. Its apparatus line stays `--taupe`, its rubric tick stays `--rubric` — the press lands on the words, not on the furniture around them.

**States.**

| State | Desktop | Touch |
|---|---|---|
| Rest | `--ink` text | Identical |
| Hover | No state of its own — hover feedback on an entry belongs to §6.9 (links) or §6.15 (plate border); the darkening answers presses, not proximity | No hover |
| Focus | If the entry is a link, §6.9's held draw + outline; the darkening itself has no focus state | Same for keyboard/switch focus |
| Active / pressed | Beats 1–3 | Identical — tap *is* the press (§6.10) |
| Selected / current | Permanent rubric margin tick (6px rule); no colour change (§6.10) | Identical |
| Scrolled-past | Not an entry state; entries rest at `--ink` regardless of scroll position | Identical |
| Disabled | `--taupe` text, no darkening, `aria-disabled` — a line struck from the run (§6.10); if the entry is a link it is also removed from the tab order | Identical |

**Breakpoints.** Identical in all three bands — a colour swap has no layout to adapt. What changes by band is the *size of the pressable surface*: contents rows are 44px at every band (§6.18); plate entries are full blocks (§6.15); on <768 both are at their largest relative to the screen, which is as it should be — the press is the theme's primary touch feedback and its targets are generous by structure, not by padding hacks.

**Edge cases.** *No JS:* the class toggle is absent and links still navigate (§6.10) — the darkening never gates behaviour. *Rapid repeated presses:* the colour transition interrupts and reverses from its current interpolated value (native CSS transition behaviour); there is no queue and no stuck state — a tenth press is identical to the first. *Long press (touch context-menu):* the darkening holds while the finger holds (correct — the press is still happening); when the OS context menu opens, `pointercancel` fires and beat 4 releases the state. *Low-power:* kept in full — at one colour transition per press this is the cheapest feedback in the theme; under reduced-motion the durations halve to 30/75ms (§6.10), because colour-change feedback is not vestibular motion and removing it would remove the theme's only press confirmation. *Scrolling back up:* no interaction — entries neither remember nor replay presses. *Forced-colours mode:* `color` is overridden by the OS palette; the darkening may be invisible — acceptable, because the press's real confirmation is the action that follows it, and the OS scheme provides its own active-state rendering.

**Accessibility.** The darkening is *supplementary* feedback for an action the visitor themselves initiated; it is never the sole signal of any state (selection is the rubric tick, navigation is the leaf-turn, errors are §6.16's errata notes). Contrast: `--ink-pressed` (`#14110D`) on `--vellum` ≈ 17:1 — the pressed state is the highest-contrast state on the page, so the feedback is visible to low-vision readers, not just felt. Focus order and visibility are governed by the entry's link (§6.9's dual signal). Touch targets: contents rows 44px, plate entries full-block, form submit per §6.16 — all ≥44px in the pressing dimension.

**Tokens.** `--ink`, `--ink-pressed: #14110D`, `--dur-press-down: 60ms`, `--dur-press-up: 150ms` (30/75ms reduced-motion), `--ease-press`.

### II.1.11 Skeleton leaves (§6.11)

**Timeline.** The skeleton has no entrance — it renders with the page shell. Its choreography is the handover. t0 = shell render; tR = the moment the leaf's real content is ready.

| Beat | Time | What happens |
|---|---|---|
| 1 | t0 | Skeleton present at rest densities: apparatus rule `--taupe-60`, title bar at 22% taupe density, body bars at 18% — the title bar is denser than the body bars because a leaf's hierarchy should be legible even in its ruled blank |
| 2 | tR → tR+200ms | Bars fade 22%/18%→0%, `--ease-leaf-fade` |
| 3 | tR → tR+400ms | Real content gains ink 55%→100%, `--ease-impression`, concurrently — the crossfade is in place, in the same boxes, so the handover has zero layout shift for everything the skeleton correctly predicted |
| 4 | tR+400ms | Skeleton DOM removed; `aria-busy` lifted in the same frame |
| 5 | t0+4000ms, if tR has not occurred | Timeout: the skeleton is replaced by the errata error note (§6.11's error state) with the same 200ms crossfade — a leaf that cannot be printed says so, in the errata voice, with a retry |

If the leaf is outside the viewport when tR occurs, beats 2–3 are skipped and the swap is instant — crossfades are performed for readers, not for empty rooms. If several leaves resolve in the same frame, each runs its own handover independently; there is no cross-leaf choreography.

**States.**

| State | Desktop | Touch |
|---|---|---|
| Loading | Bars at rest densities; `aria-busy="true"`; a visually-hidden "Loading" label | Identical |
| Resolving | Beats 2–4 | Identical |
| Error | Errata note in place of the leaf: italic line + retry link (§6.11) | Identical |
| Loaded | The skeleton no longer exists — its terminal state is replacement by the real leaf | Identical |
| Hover / focus / active | None — the skeleton contains no interactive elements, and a focusable placeholder is forbidden. If a refetch turns an already-read leaf back into a skeleton (rare; only on explicit refresh), focus is moved to the leaf's header (`tabindex="-1"`) rather than being dropped to `<body>` when the focused node is replaced | Identical |
| Scrolled-past | Resolves on data arrival regardless of position (instant swap, Timeline) | Identical |
| Disabled | Does not exist; the retry link in the error state is the only control this element ever grows, and it is never disabled — a retry that cannot be pressed is a second failure | Identical |

**Breakpoints.** *≥1200px:* the skeleton mirrors the leaf's full structure — rule, title bar at the part-title height (34px), body bars at the 30.78px pitch. *768–1199px:* identical structure; title bar 34px (the part-title is 34px until the small band). *<768px:* body bars reduce to 3 lines + the 61% last-line stub (§6.11 mobile variant), title bar 28px to match the band's part-title — the skeleton mirrors the *rendered* leaf in its band, never the desktop leaf.

**Edge cases.** *Slow network* is this element's home: the skeleton holds without animating (a moving skeleton would break §5's law and §9's shimmer ban) until the 4s timeout converts silence into an honest error. *Retry:* pressing retry restores the skeleton with a fresh 4s budget; focus stays on the note's position (the skeleton that replaces the note takes the note's place in the flow, and focus moves to the leaf header per the States rule). *No JS:* skeletons never exist — the server-rendered page is the only path (§6.11). *Low-power:* nothing to cut; the skeleton is static DOM and is itself the lean path. *Content taller than predicted:* the skeleton reserves the leaf's known structure; a catalogue leaf that returns 8 entries against a 3-entry skeleton grows at the swap — the growth is a single layout shift at a moment the reader is watching that leaf, bounded by the §II.6 CLS budget; where a previous visit established the entry count, the skeleton uses it. *Content shorter than predicted:* the leaf contracts at the swap by the same single shift; a skeleton may over-reserve but may never under-reserve silently — the shell uses the largest known structure for that leaf type. *Scrolling back up* to a leaf still loading: it is simply still ruled paper; its handover runs when ready, watched or not.

**Accessibility.** The container carries `aria-busy="true"` while loading and a visually-hidden "Loading" text alternative; the bars themselves are `aria-hidden` (they are pictures of text, and a screen reader reading a picture of a paragraph is a bug). No live-region announcement is made for routine handovers — the content arrives in flow and is found by normal reading; the one exception is the error state: if the timed-out leaf is the page's main leaf, the errata note is given `role="alert"` so the failure is announced once, without moving focus. Contrast: the bars are decorative placeholders (non-text, aria-hidden) and are exempt from text contrast; the error note is real text — italic `--ink` at 15.4:1 with its rubric errata marker at 6.9:1. Touch targets: the retry link sits in a ≥44px row.

**Tokens.** `--taupe-60` (apparatus rule bar), `--skel-title-density: 22%`, `--skel-body-density: 18%`, `--lh-body-px: 30.78px` (bar pitch), `--dur-skel-out: 200ms`, `--dur-skel-in: 400ms`, `--skel-timeout: 4000ms`, `--ease-leaf-fade`, `--ease-impression`.

### II.1.12 Leaf-turn transition (§6.12)

**Timeline.** Trigger: a navigation intent (link activation, router push). t0 = intent. The veil's tempo is fixed — readiness never shortens it (a 100ms veil flash is worse than the full turn).

| Beat | Time | What happens |
|---|---|---|
| 1 | t0 | Focus is surrendered from the old leaf (reset to `<body>`); the veil gains `pointer-events: auto` so the turning page cannot be double-navigated |
| 2 | t0 → t0+300ms | Veil opacity 0→1, `--ease-leaf-fade` |
| 3 | t0+300ms → ready, capped t0+1200ms | Veil holds at full vellum. The route swap may only occur while the veil has been fully opaque for at least one frame; earliest swap is therefore t0+300ms. If the router's `ready` signal has not fired by t0+1200ms, the veil fades onto whatever has rendered (§6.12's cap — a veil that traps the visitor is worse than a plain load) |
| 4 | Swap frame (tS) | DOM swaps beneath the opaque veil; scroll position set (top for a new leaf; the remembered position for back/forward, applied instantly — never glided); focus moves to the new leaf's H1 (`tabindex="-1"`) |
| 5 | tS → tS+300ms | Veil fades 1→0, `--ease-leaf-fade` |
| 6 | tS+180ms (veil at ≈40% opacity during beat 5) | The new title leaf's §6.1 assembly begins — the imprint line is already gaining ink as the page is revealed (§6.12) |
| 7 | tS+300ms | Veil returns to `pointer-events: none`; the turn is complete. Typical total: ≈750ms + assembly |

**States.**

| State | Desktop | Touch |
|---|---|---|
| Idle | Veil at opacity 0, `pointer-events: none`, present in the DOM only when JS injected it | Identical |
| Turning out (beats 1–2) | Veil rising; old leaf still readable beneath until ≈50% opacity | Identical; touches are intercepted from beat 1 |
| Holding (beat 3) | Full vellum; nothing readable; capped at 1200ms | Identical |
| Turning in (beats 5–7) | New leaf emerging; its assembly already running from beat 6 | Identical |
| Interrupted | A second navigation during any beat: the veil completes its fade-in from its *current* opacity at the standard rate, swaps to the newest route only, fades out — queue length 1, latest wins, no stacked veils (§6.12) | Identical |
| Hover / focus / active | The veil has no interactive states and no focusable children, ever. Focus lives where beats 1 and 4 put it: `<body>`, then the new H1 | Identical |
| Disabled | Does not exist; a navigation the router rejects never starts a turn — the veil is not raised for a journey that will not happen | Identical |

**Breakpoints.** Timings are identical in all three bands (§6.12) — the turn is the book's gesture and does not hurry on small paper. The one band difference: *<768px* the veil covers the running head as well, so the whole screen turns as one leaf (§6.12 mobile variant); at ≥768 the head is covered too (the veil is full-viewport) but is re-ruled on arrival per §6.13 rather than being treated as part of the turned leaf — in practice the visitor sees no difference, and the distinction exists only so builders do not animate the head separately.

**Edge cases.** *Router failure mid-turn:* if the swap errors, the veil fades back out onto the *old* leaf (the turn is rolled back, not completed onto a void) and the host's error handling takes over — for a missing route, the destination is §7's errata-slip 404, reached by a normal turn once the router resolves it. *Hard (non-SPA) navigation:* no veil exists; the browser loads the next page whole (§6.12 fallback) — the theme accepts the browser's own turn rather than faking one. *Prefetched route:* swap still waits for beat 3's first frame — the tempo is the design. *Very slow route:* the 1200ms cap fires; the veil lifts onto a page that may still be skeleton leaves (§6.11), which is the honest outcome — paper first, print after. *Low-power:* the veil is a single opacity transition on one fixed element and is kept in every mode; it is cheaper than the page it covers. *Reduced-motion:* no veil at all — instant route change, no assembly (§6.12 variant); the reduced-motion reader's pages simply arrive printed. *Scrolling back (back button):* identical treatment in both directions (§6.12), with scroll restoration applied at beat 4.

**Accessibility.** The veil is `aria-hidden` and contains nothing focusable; during beats 2–3 the old leaf remains in the accessibility tree (it is what is still, partially, on screen), and at the swap the tree changes with the DOM. Focus management is the announcement: moving focus to the new H1 at beat 4 makes a screen reader begin the new leaf at its title — no live region is used, because a route change the user initiated needs no announcement beyond landing where they asked to go. The holding state shows a blank vellum screen for at most 1200ms; a visitor who cannot see it is unaffected (their tree still holds the old leaf until the swap), and a low-vision visitor sees paper, not a spinner or a dark overlay. Contrast: the veil is `--vellum` itself — there is no state in which text sits on a dimmed or darkened ground. Touch: the veil's beat-1 pointer interception prevents the double-tap double-navigation that would otherwise fire two turns.

**Tokens.** `--vellum` (veil ground), `--dur-veil: 300ms`, `--veil-hold-cap: 1200ms`, `--veil-assembly-at: 0.4` (veil opacity fraction at which the new assembly starts), `--ease-leaf-fade`.

### II.1.13 Running-head navigation (§6.13)

**Timeline.** The head's choreography is scroll-position events on the shared rAF loop; there is no load animation — the head is printed with the page.

| Beat | When | What happens |
|---|---|---|
| 1 | Page load | Head rendered in its at-top state: single hairline, part name = the first leaf's part, progress fill at its §6.2 value |
| 2 | The head's natural top reaches the viewport top (sticky engages) | The second hairline fades in beneath the progress line over 200ms, `--ease-press` — the head rules itself off from the page (§6.13) |
| 3 | Each leaf boundary crossing | Part name crossfades 200ms `--ease-leaf-fade`, in the same beat as the §6.2 folio tick — head and folio always agree, never a frame apart |
| 4 | Scroll returns to the very top (sticky disengages) | The second hairline fades out over 200ms; the head is a page-top running head again |
| 5 | Continuous | Progress fill scrubs per §II.1.2 (lerp 0.12, settle ≈150ms after scroll stops) |

**States.**

| State | Desktop | Touch |
|---|---|---|
| At top | Single hairline; part name shown | Single hairline; part name dropped (<768 layout) |
| Stuck | Double hairline; otherwise identical | Identical |
| Current destination | Rubric tick (6px rule) before the running title, when the head's Contents anchor names this page (§6.13) | Identical |
| Hover | Only the Contents anchor is interactive: §6.9's underline draw | No hover; the anchor is a plain tap target |
| Focus | Contents anchor: §6.9's held draw + outline. The running title and part name are never focusable | Same for keyboard/switch |
| Active | Contents anchor takes §6.10's press darkening on its text | Identical on tap |
| Scrolled-past | Not applicable as a state — the head is persistent furniture; its at-top/stuck pair replaces the notion | Identical |
| Disabled | Does not exist; the head has no disableable control | Identical |

**Breakpoints.** *≥1200px:* full head — running title left, part name right (taupe), folio in its corner (§II.1.2), height 57px reserved. *768–1199px:* this band straddles Part I's 1024px device point and is specified in two sub-ranges rather than pretending otherwise: at 1024–1199px the layout is the ≥1200 layout (corner folio, part name present); at 768–1023px the folio moves into the head right (§II.1.2) and the part name is dropped — the leaf headers carry it. *<768px:* one line — title left, folio right, progress hairline full-width beneath, height 49px (§6.13 mobile variant).

**Edge cases.** *Long work titles:* the head never truncates with an ellipsis — a truncated title is a false title. Books solved this centuries ago: the running head uses the work's declared *short title* (a content requirement: every work in this theme supplies one, as real books do). If no short title is supplied, the build fails review rather than letting CSS cut the name. *Long part names:* the same short-form rule applies to parts. *No JS:* the head renders statically with the first leaf's part name; stickiness is pure CSS and still works; the progress fill is absent (it is JS-scrubbed) and the hairline is simply a hairline — the head loses nothing it needs. *Slow network:* the head is in the server-rendered shell and in the inlined critical CSS; it is never the thing a slow connection delays. *Low-power:* the head's only recurring cost is its share of the single rAF loop; the second-hairline fade is a 200ms paint. Nothing here is cut before §II.6's order reaches it, and the order never reaches it. *Resize/orientation change:* the head's height is fixed and reserved in both layouts, so band changes cause no layout shift; the part name and folio swap layouts at the band boundary in one frame. *Scrolling back up:* beats 3 and 4 reverse faithfully — the part name crossfades back, the second hairline lifts at the top. A head that disagrees with the leaf beneath it, in either direction, is a §10 apparatus-agreement failure.

**Accessibility.** The head is the page's `<header>` (banner landmark, one per page). The running title is *plain text, not a heading* — the page's H1 lives in the title leaf, and a second heading inside the furniture would corrupt the document outline. The part name is `aria-hidden` (it duplicates the leaf headers' semantic text, exactly as the folio does, §II.1.2). The Contents anchor is a real link in normal focus order — skip link → Contents → title leaf — with §6.9's dual focus signal. Contrast: running title `--ink` 15.4:1; part name `--taupe` 3.2:1, justified as furniture whose information is duplicated at full ink in every leaf header (the same redundancy condition as §2's taupe rule); the Contents link is `--ink` with its underline states per §II.1.9. Touch targets: the Contents anchor's hit area is the full head height (57px / 49px) via the head's padding — ≥44px in both bands.

**Tokens.** `--head-h: 57px` (49px <768), `--fs-apparatus-caps: 12.5px`, `--ink`, `--taupe`, `--rubric` (current-destination tick), `--dur-head-rule: 200ms`, `--ease-press`, `--ease-leaf-fade`, `--lerp-scroll`.

### II.1.14 The printer's mark (§6.14)

**Timeline.** Trigger: the apparatus region (contents leaf → the leaf before the footer) reaches the mark's sticky position. t0 = pin engagement.

| Beat | Time | What happens |
|---|---|---|
| 1 | Before t0 | The mark is absent — the title leaf carries no margin mark (§6.14); in bands where it lives in the footer, it is simply waiting there, printed, from page load |
| 2 | t0 → t0+300ms | Density settle 70%→100%, `--ease-press`, as the pin engages — the mark arrives in ink, then never moves again |
| 3 | The whole apparatus region (potentially thousands of pixels of scroll) | No beats. The mark is static at 100% — its stillness across a long scroll is the effect |
| 4 | Region end | The mark un-pins and scrolls away with the page; no fade-out, no ceremony |
| 5 | Scroll back into the region | The mark re-pins — but the settle does **not** replay: after its first settle it is at 100% for the rest of the page's life. A mark that re-arrives on every pass is a mascot, not a device |

**States.**

| State | Desktop | Touch |
|---|---|---|
| Absent (title-leaf region) | Not rendered in the margin | In footer bands, present in the footer from load — "absent" applies only to the margin placement |
| Pinned | 100% `--ink`, static, left margin aligned to the first leaf's header baseline | Not applicable — touch bands use the footer placement |
| Relocated (footer headpiece) | Applies at <1280px: centred above the colophon, 36px (§6.14) | The standard touch state |
| Hover | Explicitly none — the mark is not a link and must not pretend (§6.14). If the host insists it link home, a caption beneath it ("The House", apparatus mono) takes §6.9's underline; the device itself still takes no hover | Identical |
| Focus | The mark is never focusable; the optional caption link is, in footer flow order | Identical |
| Active | Does not exist | Does not exist |
| Scrolled-past | Un-pinned and gone with the region (beat 4) | In the footer, it is simply the footer's headpiece — reached, not passed |
| Disabled | Does not exist | Does not exist |

**Breakpoints.** *≥1200px:* this band straddles the mark's 1280px device point: at ≥1280px, pinned in the left margin at 44×44px (margin ≥180px); at 1200–1279px the margin cannot hold it, so the footer placement applies — stated plainly so no builder squeezes it into a 150px margin and crowds the column. *768–1199px:* footer headpiece, centred above the colophon, 36px. *<768px:* footer headpiece, 36px, identical — identity furniture relocates; it does not shrink further or vanish (§6.14).

**Edge cases.** *Sticky unsupported (legacy webview):* the mark sits statically at the apparatus region's start — still correct, merely unpinned (§6.14 fallback); in footer bands nothing changes at all. *No JS:* the mark is inline SVG in the HTML at 100% ink; the density settle is an observer-driven enhancement, and without JS the mark is simply printed — pinned by CSS where the band allows. *The brand has no device:* the sanctioned substitute is a type-only mark — the house's monogram in Cormorant caps inside a hairline frame, set at build time. A generic ornament in this slot is §9's failure, and a stock logo squeezed into it is worse. *Fine-detailed device:* at 44px, hairline detail in a full-size logo disappears; the device must be redrawn bold for the slot, as printers cut devices per size. If the brand cannot supply a legible 44px device, the monogram substitute is used — legibility at the slot size is a requirement, not a preference. *Low-power:* the mark is the theme's cheapest element (one SVG, one 300ms settle, once); nothing is ever cut from it. *Very long apparatus region:* the pin holds for the whole region (§6.14 sticky range); the mark does not follow into the footer leaf — its region ends where the colophon begins, because the colophon has its own claim on the mark in footer bands and its own fleuron on desktop. *Scrolling back up:* beat 5 — re-pin without replay.

**Accessibility.** The running head already names the house in text on every page, so the mark is a duplicate identity statement and is `aria-hidden` — announcing the brand twice per page is noise. (If a build ever removes the running title, the mark must instead take `role="img"` and an `aria-label` of the house name; the rule is: the name is available as text exactly once.) Contrast: the device is drawn in `--ink` strokes — 15.4:1 against the vellum margin. Focus: never focusable in its own right. Touch targets: none — it is not a control; the optional caption link, where it exists, is a standard ≥44px footer row link.

**Tokens.** `--ink`, `--mark-size: 44px` (36px footer placement), `--mark-settle-from: 70%`, `--dur-mark-settle: 300ms`, `--ease-press`, `--mark-margin-min: 1280px` (the band breakpoint, named so builders stop hard-coding it).

### II.1.15 Plate cards (§6.15)

**Timeline.** Two choreographies: the scroll reveal (inherited from §6.3 with an entry stagger) and the hover/focus border.

| Beat | Time | What happens |
|---|---|---|
| 1 | Leaf reveal t0 + k×90ms (k = the entry's index within the leaf) | Entry k begins its §6.3 density ramp (600ms, `--ease-impression`). The stagger applies to the first six entries of a leaf; entries beyond the sixth start at t0 with no offset — a long catalogue prints in a run, not in a queue the reader waits on |
| 2 | Hover/focus t1 → t1+200ms | Plate border fades in (inset 1px ring, `--ease-press`): `--taupe` on hover, `--ink` on `:focus-visible` — focus is distinguishable from hover by ink, a Part II refinement so a keyboard reader's position is never mistaken for a mouse passing through. Simultaneously the entry's apparatus line steps `--taupe` → `--ink` (§2's rule: apparatus being read steps up to ink, as the folio does) |
| 3 | Hover t1 → t1+700ms | The entry's plate image settles 102%→100% inside its frame (§5 image treatment) |
| 4 | Press | §6.10's darkening on the title (60ms down / 150ms up) |
| 5 | Pointer leaves / blur | Border fades out over 200ms; apparatus line returns to `--taupe` over the same 200ms |

**States.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Borderless; entries separated by 40px of paper and a `--taupe-40` hairline | Border permanently on at `--taupe-60` (units must be distinguishable without hover, §6.15) |
| Hover | Beats 2–3 (taupe border) | No hover on coarse pointers |
| Focus (`:focus-visible`) | Beats 2–3 with the border in `--ink` | Same for keyboard/switch focus |
| Active / pressed | Beat 4 | Tap: beat 4 |
| Current / featured | Permanent `--ink` border + rubric margin tick; at most one per leaf (§6.15) | Identical |
| Unavailable | All ink at `--taupe`, no border response, apparatus line gains its status word — and the status word itself ("Out of print") is set in `--ink` within the taupe line: the one fact in the line that must be readable at rest is readable | Identical; not a link, so no tap state |
| Scrolled-past | Entries stay printed; states above are unaffected by scroll history | Identical |
| Disabled | Does not exist as a separate state — the unavailable state *is* the theme's answer, rendered as non-link text rather than a greyed link | Identical |

**Breakpoints.** *≥1200px:* 120px plate at the entry's left, text beside it; apparatus line one line where it fits. *768–1199px:* the same side-plate layout (Part I's ≥640px condition holds across this band); the apparatus line wraps to two lines rather than truncating — facts are never truncated in this theme (§6.15). *<768px:* the plate stacks above the title at column width; border permanently on (touch column); apparatus wraps to two lines.

**Edge cases.** *Entry with no image:* a text-only entry (permitted and often better, §7) — and no empty frame is reserved for it: an empty hairline frame reads as a *missing* plate, and §6.4's honesty about missing plates applies — absence is stated by the layout, never faked by a placeholder box. *Very long titles:* an entry's title may wrap to three lines; the one-column catalogue absorbs it (entries are separated by space, not aligned in a grid, so nothing else moves) — this is precisely why the theme lists in one column. *Slow image:* the entry's text reveals on the leaf's schedule; the plate joins when decoded, per §6.3's plate beat — the catalogue never waits for its pictures. *No JS:* entries are static HTML; hover/focus borders are CSS and still work; the touch permanent border is a `(hover: none)` media rule, not a script. *Low-power:* the plate settle (beat 3) is dropped first; the border fade stays (a 200ms paint on one entry). *A catalogue of 100+ entries:* pagination is §7's folio language, not infinite scroll — a catalogue that never ends cannot be folio'd, and the folio is the theme's contract with the reader. *Scrolling back up:* printed entries stay printed; the featured entry's border and tick are state, not animation, and persist.

**Accessibility.** The whole entry is one link via the stretched-link pattern, with the entry's title as the anchor text — the accessible name is the work's title, and the apparatus facts are readable text in the same link, so a screen reader encounters title + description + facts as one coherent unit. Focus is the ink border (15.4:1 against the ground, unmistakable) plus the apparatus step-up; hover's taupe border (3.2:1) is a non-text indicator above the 3:1 floor. Contrast at rest: title and description in `--ink` (15.4:1); apparatus line in `--taupe` (3.2:1) at rest, stepping to `--ink` whenever the entry is hovered, focused, or featured — and its one always-ink word is the unavailable status (States). Touch targets: the entry block itself is the target — full column width and never shorter than its content, with a 44px minimum height enforced for short entries.

**Tokens.** `--taupe`, `--taupe-40` (separator), `--taupe-60` (touch border), `--ink` (focus/featured border, apparatus step-up), `--rubric` (featured tick), `--dur-entry-border: 200ms`, `--dur-plate-settle: 700ms`, `--entry-stagger: 90ms`, `--space-entry: 40px`, `--ease-press`, `--ease-impression`.

### II.1.16 The correspondence form (§6.16)

**Timeline.** Focus, validation, and submission are three separate choreographies.

*Focus (per field):*

| Beat | Time | What happens |
|---|---|---|
| 1 | t0 → t0+200ms | The field's rule thickens in colour: `--taupe` → `--ink` (still 1px — the thickening is of ink, not of geometry), `--ease-press`; the label steps `--taupe` → `--ink` in the same 200ms |
| 2 | t0 → t0+240ms | The rubric caret-line — the leftmost 12px of the rule, at 2px — draws in, `--ease-press`: the editor's mark at the line being written |
| 3 | Blur | If the field is empty, rule and label return to `--taupe` over 200ms and the caret-line undraws; if the field has content, the rule settles to `--ink` at 70% (a written line stays darker than a blank one) and the caret-line undraws |

*Validation (on submit, tS):* erroneous fields' rules turn `--rubric` over 200ms; at tS+100ms each errata note begins gaining ink (400ms, `--ease-impression`) — the red line lands first, then the correction, in the order an editor's hand moves. At tS+200ms focus moves to the first erroneous field, landing on a line already marked. *Submission:* at tS the form's ink drops to 70% over 300ms and the imprint line's text changes to "Being entered…". *Success (server confirms, tR):* the form fades to 70% over 300ms `--ease-leaf-fade` if it is not there already, is replaced in place by the acknowledgement leaf at tR+300ms, and the acknowledgement prints per §6.3 (600ms ramp, no stagger) with its reference number in mono — "No. 214 — answered within two working days."

**States.**

| State | Desktop | Touch |
|---|---|---|
| Rest | `--taupe` labels, hairline rules, submit underline drawn at 100% | Identical; field rows ≥48px |
| Focus | Beats 1–2 above | Identical on tap-focus |
| Filled | Rule at `--ink` 70%; label returns to `--taupe` (the field is done being written; its label quiets) | Identical |
| Hover | Fields take no hover state (a line does not respond to a hovering pen). The submit control does: its text steps to `--ink-pressed` — the pen poised over the signature line | No hover |
| Active | Submit press: §6.10 timing on its text | Identical |
| Error | Rubric rule + errata note beneath the field in italic 17px, worded as a correction (§II.3) | Identical |
| Disabled / submitting | All ink at 70%; the submit's underline undraws to 40%; the submit is genuinely `disabled` (the theme's one disabled control — a second submission must be impossible, not merely unlikely); imprint line reads "Being entered…". No spinner exists in this theme | Identical |
| Success | The form no longer exists; the acknowledgement leaf stands in its place (terminal) | Identical |
| Scrolled-past | Not a form state — and stated because it matters: errors and filled values persist through any amount of scrolling. An error that vanishes when scrolled past is an error the house hoped the visitor would forget | Identical |

**Breakpoints.** The structure is identical in all three bands (§6.16: the ruled-line field is inherently touch-friendly). *≥1200px and 768–1199px:* the form occupies the standard 640px column; fields at 32px gaps. *<768px:* fields span the column (viewport minus margins); labels stay 12px mono, input text stays 19px — the type does not shrink to fit the phone, the line simply gets shorter; each field's tap row (label + line + gap) is ≥48px; native date/number controls are used unstyled-beyond-the-rule.

**Edge cases.** *No JS:* the form submits natively; validation is the server's; errors return on reload rendered in the same errata format in the same positions (§6.16 fallback) — the no-JS error and the JS error are the same object, so the visitor's experience of being corrected does not depend on their client. *Slow network on submit:* the submitting state holds indefinitely and honestly (the imprint line says what is happening); if the request fails, a *form-level* errata note appears above the form — "The letter could not be sent. Nothing was kept." with a send-again control — set as an errata entry, and focus moves to it (`tabindex="-1"`): a whole-letter failure is a different object from a field correction and is never reported as one. *Double submission:* the disabled submit (States) plus a submitted-flag in the handler; a double-click in the same frame is absorbed by the flag, not by hope. *Browser autofill:* fields carry correct `autocomplete` attributes (`name`, `email`, `street-address`…); the autofill background is neutralised with the long-transition background trick so the vellum is not vandalised by a yellow wash, and an autofilled field takes the Filled state (rule at 70% ink) — the browser has written on the line, and the line shows it. *Very long input:* text inputs are single ruled lines; an over-long value scrolls within the line as in any input — the theme does not grow the line; long-form answers belong in the textarea, which is a ruled *block* (hairlines at the 30.78px pitch, so writing sits on the rules like a letter on lined paper). *Content shorter than designed:* a one-field form (the newsletter leaf) keeps the full structure — label, line, imprint line, submit — because the correspondence fiction is carried by the imprint line, not by field count. *Scrolling back up* to a submitted form: the acknowledgement leaf is what is there; the form does not resurrect.

**Accessibility.** Every label is a real `<label>` programmatically associated with its input — the apparatus-mono styling is presentation only. Each field's errata note is wired with `aria-describedby`, and an erroneous field carries `aria-invalid="true"`; on a multi-error submit, focus moves to the first error (Timeline) so the correction path is walked in order. *Visible focus* is triple: rule to `--ink` (15.4:1), label to `--ink`, and the rubric caret segment (6.9:1) — any one suffices, all three agree. *Contrast:* field text `--ink` 15.4:1; errata notes `--ink` italic 15.4:1 with a rubric marker at 6.9:1; the filled rule at 70% ink ≈8.6:1. Resting labels are `--taupe` (3.2:1) — recorded here as the theme's single deliberate contrast debt, not hidden: the label is the input's programmatic name (available to assistive technology at full fidelity regardless of its colour), it steps to `--ink` on focus, and a build under a strict WCAG AA contract sets resting labels to `--ink-70` (≈8.6:1) — the one substitution the theme permits, changing nothing else. *Touch targets:* field rows ≥48px; the submit's hit area is at least 48px tall and, below 768px, the full column width — signing a letter is the page's most important tap and it is sized like it.

**Tokens.** `--taupe` (resting labels/rules), `--ink`, `--ink-70` (filled rule; AA-contract labels), `--rubric` (error rule, caret-line), `--ink-pressed` (submit hover), `--dur-field-rule: 200ms`, `--dur-caret-draw: 240ms`, `--dur-form-fade: 300ms`, `--caret-w: 12px`, `--field-gap: 32px`, `--ease-press`, `--ease-impression`, `--ease-leaf-fade`.

### II.1.17 The colophon footer (§6.17)

**Timeline.** The footer is where the book ends, and its entire motion budget is two events, once each.

| Beat | When | What happens |
|---|---|---|
| 1 | Footer crosses 50% visibility | Its fleuron rule draws per §II.1.7's timeline (680ms sequence; 400ms single-breath <768) — on desktop, where the mark is in the margin, the fleuron is the footer's opening; in footer-mark bands the mark is already there and the fleuron still draws beneath it |
| 2 | Same trigger | The colophon paragraph reveals per §II.1.3 (600ms ramp from 55%) |
| 3 | Never | Nothing else. No link animates beyond §6.9's own states, the facts line does not count, the mark does not flicker — the §6.6 candle belongs to the title leaf, and a footer that breathes is a book that will not end |

The "corrected year" suffix (§6.17) is computed at render from the stored last-visit year — it has no timeline; it is either in the facts line's text or it is not.

**States.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Printed: mark (margin bands) or fleuron, colophon paragraph, facts line, links | Mark centred above at 36px; otherwise identical |
| Hover / focus | Footer links take §6.9's draw (hover) and held draw + outline (focus) | Tap: §6.9's 150ms 2px active state |
| Active | §6.10 darkening on link text | Identical |
| Print | `@media print`: everything at 100% ink, mark included — a printed page of this site ends with its colophon (§6.17) | n/a |
| Scrolled-past | The footer is the page's end; "past" it there is only the folio at rest on its final numeral (§II.1.2, beat 5) | Identical |
| Disabled | Does not exist — a footer has no controls to disable | Identical |

**Breakpoints.** *≥1200px:* at ≥1280px the mark is in the margin and the footer opens with the fleuron rule; the facts line sets on one line. At 1200–1279px the mark takes the footer placement (per §II.1.14's band rule). *768–1199px:* mark centred above the colophon at 36px; the facts line wraps to two lines rather than truncating — an edition statement is never cut. *<768px:* identical structure; the necessary links stack as apparatus rows of ≥44px; the colophon paragraph stays 17px italic — the last words on the page do not shrink.

**Edge cases.** *The stale colophon* is this element's characteristic failure: the site changes and the facts line still claims the previous edition. The cure is structural — the facts line is *generated* from build metadata (build date, edition counter, the actual font files loaded) at build time, never hand-typed into a template, so it cannot silently go stale; §10's truth check then verifies generation against the shipped build. *False claims* are §9's capital offence and §10 gate 9's outright failure — the element's edge case is a content case, and it is handled by process, not styling. *No JS:* the footer is complete static HTML; the year is server-rendered; the corrected-year suffix (which needs storage) is simply absent — a joke that requires localStorage does not get to break the colophon for anyone else. *Storage unavailable (private mode):* same absence, no error. *Slow network:* the footer is the last thing in the document and arrives when it arrives; there is no footer skeleton — a book's final page is never announced by a placeholder. *Low-power:* zero recurring cost; nothing exists here to cut. *Very long legal notices:* set in body small, in `--ink`, in full — legal text is reading matter (§2), never taupe, never truncated, never accordioned away in the footer (the §II.2 accordion exists for the *terms leaf*, not for hiding the footer's obligations).

**Accessibility.** The footer is the `contentinfo` landmark, once per page. The colophon paragraph is `--ink` italic 17px (15.4:1). The facts line is `--taupe` mono — permitted under §2's redundancy rule *by construction*: every fact in it (types used, place, year, edition) is stated in ink in the colophon paragraph directly above it, so the mono line is the apparatus echo, not the sole carrier. The mark, in footer bands, is `aria-hidden` (the house is named in the running head and in the colophon paragraph — §II.1.14's exactly-once rule). Footer links carry §II.1.9's full contrast table; touch rows ≥44px in the small band. Focus order: the footer's links are the last stops on the page, in reading order — necessary links first as listed, and no element of the footer is focusable that is not a link.

**Tokens.** `--ink`, `--taupe`, `--fs-body-small: 17px` (colophon paragraph, italic), `--fs-apparatus-mono: 12px` (facts line), `--space-leaf: 96px` (the footer's separation from the last leaf), plus the fleuron tokens of §II.1.7 and, in footer bands, the mark tokens of §II.1.14.

### II.1.18 The contents leaf (§6.18)

**Timeline.** Trigger: the contents leaf's §6.3 reveal. Row k (0-indexed) begins its ramp at leaf-t0 + k×70ms; each row's ramp is the standard 600ms `--ease-impression`.

| Beat | Time | What happens |
|---|---|---|
| 1 | Leaf t0 + k×70ms → +600ms | Row k prints (title, leader, numeral together — the row is the unit) |
| 2 | After the last row (t0 + (n−1)×70 + 600ms) | The contents is fully printed. For n > 12, rows beyond the twelfth start at t0+840ms with no further offset — the stagger caps at 12 so a long contents never makes the reader wait out a queue |
| 3 | Hover/focus on a row | §6.9's rubric underline draws under the *title only* (240ms) and the row's numeral steps `--taupe` → `--ink` over 200ms, concurrently |
| 4 | Press | §6.10's darkening on the title (60/150ms) |
| 5 | In-page contents: a §6.2 boundary crossing | The current-row marker (rubric tick + rubric numeral) moves to the newly current row *instantly* — no crossfade, no draw. A bookmark is picked up and put down; it does not glide. Stated here because every other apparatus change in the theme is eased, and this one must not be |

**States.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Titles `--ink`; leaders `--taupe-60`; numerals `--taupe` | Identical |
| Hover | Beat 3 | No hover |
| Focus (`:focus-visible`) | Beat 3, held, plus §6.9's outline on the row link | Same for keyboard/switch |
| Active | Beat 4 | Tap: beat 4, then navigation |
| Current | Rubric margin tick + numeral in `--rubric`; `aria-current` set (States, Accessibility) | Identical |
| External | The numeral is replaced by "→" in mono `--taupe` — leaving the volume is stated, never disguised (§6.18) | Identical |
| Scrolled-past | Rows stay printed; in-page, the current marker tracks per beat 5 | Identical |
| Disabled | Does not exist — an entry for a leaf that does not exist yet is not disabled; it is omitted, because a contents page that lists unprinted leaves is false apparatus (§9) | Identical |

**Breakpoints.** *≥1200px:* full form — title left, dotted leader, numeral in a right-hand column whose width is set at build time to the list's widest numeral, so every leader ends at the same x. *768–1199px:* identical; leaders shorten naturally with the column. *<768px:* leaders continue down to 400px viewport; below 400px the numeral moves before the title ("IV · Title") and the leader is dropped (§6.18 mobile variant) — a narrow contents page sets its numbers first rather than crushing its dots. Row height is 44px in all bands.

**Edge cases.** *A long contents (20+ rows):* the contents leaf splits into two leaves — "Contents" and "Contents, continued" — as real books do; §4's one-idea-per-leaf rule governs furniture too. The folio counts both leaves honestly. *Long titles:* a title may wrap to two lines; the leader then sits on the title's *last* line, baseline-aligned with the numeral (the row is a flex line whose leader and numeral align to the final text line) — a leader floating beside the first line of a two-line title points at the wrong line and fails review. *Slow network:* the contents is server-rendered in the page's first HTML — it is the wayfinding, and wayfinding is never lazy-loaded, deferred, or skeletoned. *No JS:* a plain list of links; leaders are CSS-only; the current marker for site navigation is server-rendered from the route. *Low-power:* the reveal stagger is the only cost; under battery-saver the rows print statically (§II.1.3's degradation). *Generated disagreement:* the contents, the folio count, and the running head's part names derive from one structure (§6.18, §10 gate 8) — a hand-edited contents row is the edge case, and the build's apparatus-agreement check is its cure. *Scrolling back up:* beat 5's marker walks back with the reader, instantly, in both directions.

**Accessibility.** The contents is a `<nav>` (site contents) or `<ol>` (the page's own leaves) of real links — one per row, the whole row being the link. The visible numeral is `aria-hidden`, and each link carries a visually-hidden prefix — "Leaf III:" — before its title, so the accessible name is "Leaf III: The Print Room" while the visual numeral is not read twice. The current row carries `aria-current="page"` (site contents) or `aria-current="true"` (in-page contents). Contrast: titles `--ink` 15.4:1; leaders are non-text decoration; numerals `--taupe` 3.2:1 at rest — justified as apparatus whose value is duplicated by the sr-only prefix and by the leaf headers themselves (§2's redundancy rule), stepping to `--ink` on hover/focus and to `--rubric` (6.9:1) when current. Focus is visible per §II.1.9's dual signal, applied to the row. Touch targets: every row is a full-width 44px target — the contents is the theme's primary navigation and its rows are sized as such.

**Tokens.** `--ink`, `--taupe-60` (leaders), `--taupe` (resting numerals), `--rubric` (current numeral + tick; underline draw), `--contents-row-h: 44px`, `--contents-stagger: 70ms`, `--dur-reveal: 600ms`, `--fs-apparatus-mono: 12px`, `--ease-impression`, `--ease-press`.

## II.2 Component inventory — every component a real site needs, in this theme

Part I specified the theme's signature and page-family elements. A real site needs more furniture than that, and every piece of it must speak the theme's language or the costume slips. Each entry below is the complete themed treatment: form, behaviour, and the rule that keeps it honest. Components the theme *refuses* are listed as refusals, with the themed replacement — a builder who reaches for the refused component is told what to build instead.

- **Primary action (the signature).** There are no filled buttons in this theme. The primary action is a text signature: apparatus caps (12.5px, 0.18em tracking) with §6.9's rubric underline *permanently drawn* — the one resting-drawn underline (§6.16). It reads as a signature on the letter, not a control on a screen. Hit area ≥48px tall. One per leaf, maximum — a page with three signatures has signed nothing.
- **Secondary action.** The same text treatment with a permanent `--taupe` underline, stepping to `--ink` with the rubric draw on hover/focus (§6.9). Used for the lesser path ("Read the errata" beside "Order the edition").
- **Text input.** §6.16's ruled line, in full. No boxed variant exists; a builder who boxes an input has left the theme.
- **Textarea.** A ruled block: hairlines at the body pitch (30.78px) so handwriting-height text sits on the rules like a letter on lined paper; the block's rules are `--taupe-40`, the text `--ink` at 19px. Minimum 4 lines tall.
- **Select.** A native `<select>` wearing the ruled line (label above, 1px rule below, apparatus caps for its closed value's label). The dropdown itself is the OS's — the theme does not fake a listbox; a custom listbox in a printed book is a pop-up book, and this is not one.
- **Checkbox.** A small square hairline box (14px) that takes an editor's tick — a hand-drawn ✓ path in `--ink`, drawn over 150ms `--ease-press` when checked; focus shows the §6.9 outline logic (1px taupe outline, 2px offset) around the box. The label is body text, never apparatus — what is being agreed to is reading matter.
- **Radio.** A hairline circle with a rubric centre dot when chosen — the one place rubric marks a *selection* rather than an annotation, because a chosen radio is the reader's own rubrication of the list. Dot fades in over 150ms.
- **Switch / toggle.** *Refused.* A sliding switch is machinery. Binary settings are set as a two-row apparatus choice (two contents-style rows, §6.18; the current state carries the rubric tick and numeral) or as a checkbox where the choice is a single assent. If a host product demands a switch, the setting does not belong in this theme's pages.
- **Search.** "Search the index": a ruled line (§6.16) labelled in apparatus mono, whose results are a contents leaf (§6.18) generated from matches — titles, leaders, leaf numerals. No search dropdown, no live suggestion chips; results are a list of leaves, printed per §6.3 as they arrive, with the query's matches carrying the rubric underline permanently (the editor has marked every occurrence the reader asked for).
- **Data table (the collation table).** Hairline rules only: a `--ink` rule above and below the header row, `--taupe-40` rules between body rows, no vertical rules, no zebra striping (zebra is spreadsheet language; a collation table is a list that happens to have columns). Header in apparatus caps; text columns in Cormorant 17px; figure columns right-aligned in Plex Mono tabular. Row hover: the row's ink steps up per §6.10's logic at 70%→100% for taupe-set cells — no background change, ever; there are no backgrounds to change.
- **Badge (the edition tag).** A mono line, never a pill: "Second edition" in apparatus mono `--taupe`, preceded by a 6px rubric rule — the §6.10 selection tick doing badge duty. Status tags ("Corrected", "Out of print") follow the same form, with "Corrected" taking the rubric tick because a correction is the house speaking in red.
- **Alert (the pasted slip).** Alerts are errata slips: an italic entry in a hairline-ruled block, opened by a rubric errata marker ("Errata —" for corrections of fact; "Note —" for information), pasted into the flow at the point it concerns. There is no red background, no icon, no dismiss × for factual alerts (a correction is not dismissed; it stands). Dismissible *notices* (a reading-room closure) may carry a plain "Filed" text control that removes the slip with a 200ms density fade — filed, not swatted.
- **Pagination.** §7's folio language, as a component: "Leaves I–III of the catalogue" in apparatus mono, with further ranges as contents rows (§6.18) — leader, numeral, and all. Numbered page buttons in boxes do not exist.
- **Modal (the tipped-in slip).** A modal in this theme is a slip tipped into the book: the §6.12 vellum veil at full opacity behind, a single column leaf centred on it, opening by density (55%→100%, 400ms `--ease-impression`) — no scale, no slide, no drop shadow (a hairline rule frames the slip). Focus is trapped inside the slip for its life; `Esc` and a plain "Return" apparatus link close it, returning focus to the invoking control. A modal is rationed to irreversible or legally-required moments (confirming an order, a rights notice) — anything else is a leaf the visitor should navigate to.
- **Toast (the entered note).** Confirmations are entry slips: a mono line at the foot of the viewport — "Entered as No. 214" — that gains ink over 300ms, rests for 6s, and fades to 70% (not away) until the next interaction dismisses it. One at a time; a second entry replaces the first. It is never coloured, never iconned, and it always carries its number — an unnumbered confirmation is a rumour.
- **Tabs.** *Refused as tabs.* Grouped views (Description / Collation / Provenance on a detail leaf) are set as a contents row of apparatus links (§6.18's row, horizontal): the current view carries the rubric tick above its word and its §6.9 underline drawn; switching views turns to that view's leaf per §6.12's logic in miniature (the block fades to vellum-white 150ms and the new view prints per §6.3). No pill backgrounds, no sliding indicator — the indicator is a tick, and ticks do not slide.
- **Accordion (the notes disclosure).** Used for errata lists and long notes: a part-title row carrying a mono "[+]" marker; opening sets the marker to "[−]", rules the §6.7 hairline beneath the row, and prints the content per §6.3's density ramp. The space opens in one frame (the theme does not animate layout height — displacement is banned, §5); the eye is given the density ramp instead of the motion. Closing reverses: content returns to 55% over 200ms and is then removed. `aria-expanded` is wired correctly or the component does not ship.
- **Breadcrumb (the volume trail).** An apparatus-caps line at the head of detail leaves: "The Catalogue · Spring · Leaf III" — each ancestor a §6.9 link, separators are the middot of the imprint line. It duplicates the running head's job at leaf level and is therefore used only where the running head's part name cannot carry the full path (deep catalogues).
- **Tooltip (the marginal gloss).** A gloss is marginalia: on hover/focus of a marked term, the gloss appears in italic `--taupe`→`--ink` (it steps up when read, per §2) in the margin at ≥1280px, or as a footnote line directly beneath the paragraph in narrower bands. It is triggered by focus as reliably as by hover, it is never the sole carrier of essential information, and it never appears in a floating box with an arrow — books do not point; they annotate.
- **Skip link.** "To the text" — an apparatus link that is the first focusable element, invisible until focused, then printed at the head's top-left in `--ink` with its underline drawn. It skips to the title leaf, not to a `<main>` landmark label the visitor cannot see.
- **Progress bar (generic).** *Refused as a component.* Progress in this theme is the folio and its hairline (§6.2) for reading, and the imprint line's own words ("Being entered…") for processes. A generic striped or filling bar is fairground equipment.
- **Spinner.** *Refused.* Loading is skeleton leaves (§6.11) for content and stated text for processes. Nothing in a book spins.
- **Chips / tags.** *Refused.* Categorisation is apparatus mono words separated by middots in the entry's apparatus line (§6.15). A chip is a badge pretending to be a button; this theme's badges are lines and its buttons are signatures.
- **Empty state.** An errata-voice leaf (§II.3): the fact stated ("No copies remain of the spring pamphlet"), the reason if known, and the way onward as a contents row. It is a leaf in the volume, set with the same care as a full one — an empty shelf in a well-kept library is still part of the library.
- **Consent notice.** If the law requires one, it is a correspondence slip at the foot of the page in the §6.16 voice, stating exactly what is kept and offering the choice as two apparatus links. And the build's colophon (§6.17) must then be *corrected* — a site that shows a consent slip may not print "No cookies were consulted" (§9). The inventory and the footer are audited against each other.

## II.3 Content & copywriting voice

The voice is the colophon's voice: the maker, after the performance, stating what was made. Every string on the page — including the ones developers usually write last and worst — is set in it.

**Principles.**

- **Facts or silence.** Every claim carries its evidence or is cut. "Printed slowly" is a claim the house can show; "crafted with passion" is neither fact nor information. (§9 makes the false version a capital offence; the voice rule is its daily practice.)
- **The house speaks as "we", sparingly.** First person plural, used for acts ("We bind the spring pamphlet by hand"), never for feelings ("We are thrilled to announce" — the house is never thrilled in print).
- **No exclamation marks.** A colophon has never contained one. Emphasis is rubrication and position, not punctuation.
- **Sentence case everywhere.** Apparatus caps are a *type treatment* (§3), not shouting in the copy; the underlying text is written in sentence case and the caps are applied by CSS.
- **Numbers are exact or absent.** Apparatus figures follow §3's numeral law (facts in mono, story in serif). "Many readers" is banned where a count exists; where no count exists, the sentence is restructured to not need one.
- **Years in apparatus are Roman** (MMXXVI); years in body text are figures in Cormorant old-style. Dates are never written "11/23/26" — the volume writes "23 November 2026".

**Headline style.** Declarative, specific, quiet; the headline states what the thing *is*, in the present tense, with the house's fact inside it.

- ✓ "Poems, printed slowly." — the product and the method in four words.
- ✓ "The spring list: six pamphlets, bound by hand."
- ✗ "Discover the magic of slow poetry!" — three offences: a command to feel, an abstraction ("magic"), an exclamation.
- ✗ "Welcome to Heron & Quill Press" — a headline that spends itself on greeting has nothing left for information; the running head already names the house.

**Label style.** Labels are nouns of the trade, naming the thing itself: "Edition", "Leaves", "Set in", "Your name", "The address for the reply". A label never contains an instruction ("Please enter your…") — the ruled line is the instruction. Field labels in forms are the correspondence's own: "Your name", "Where the reply should go", "How many copies".

**Error voice (the errata format).** Every error is a correction, in the form: **"For 'X' read: Y."** — the errata slip's own grammar, used seriously everywhere so the 404 joke (§7) can exist.

- Email: "For 'email' read: an address with an @ and a domain, as in reader@press.example."
- Required field left blank: "For the blank line read: your name — the letter cannot be answered without it."
- Copies field: "For 'copies' read: a whole number, one or more."
- Form-level failure: "The letter could not be sent. Nothing was kept." — the failure, the consequence for the visitor's data, and (in the control beside it) the remedy: "Send it again."
- Never: "Invalid input", "Oops", "Something went wrong", a field name in developer English ("email_address is required"), or an apology in the plural ("We're sorry!!") — the house corrects; it does not grovel.

**Empty-state voice.** The fact, the reason if there is one, and the way onward — in that order, in at most three lines.

- "No copies remain of the spring pamphlet. The run of 340 was bound in March. The autumn list is entered in the catalogue." (+ a contents row to the catalogue)
- "Nothing in the index answers to 'vellum'. The index covers the house's own terms; the correspondence leaf reaches a person." (+ rows to the contents and the correspondence leaf)
- Never: "Nothing here yet", "No results found 😕", or a bare zero — a zero with no sentence around it is a shrug in mono.

**Success voice.** An acknowledgement with its number (§II.2's entered note, §6.16's acknowledgement leaf): "Received and entered as No. 214. Answered within two working days." The number, the commitment, full stop. Never "Success!", never a tick icon in a circle — the number *is* the tick: it can be quoted back.

**Action voice (buttons and links).** Verbs of the house, destinations named: "Order the edition", "Write to the house", "Read the errata", "Return to the catalogue". Banned: "Get started" (started on what?), "Learn more" without its object, "Click here" (the link's text is its destination — §II.1.9's labelling rule is a voice rule too), "Submit" (letters are *sent*: the form's signature reads "Send the letter").

**The banned list (grep the build for these).** "Oops", "Invalid", "Welcome to", "Get started", "Learn more" (bare), "Click here", "Submit", "delve", "passionate", any exclamation mark in interface copy, any emoji. **The owned list:** leaf, folio, apparatus, errata, impression, set in, bound, corrected, entered as, out of print. A string that could appear on any SaaS site unchanged fails the voice exactly as a sentence that could appear in any other theme fails §9's anti-filler law — the voice is the theme, set in words.

## II.4 Three worked examples, end to end

§8 built the title leaf as a set of construction steps. These three examples are the same press's pages *as experienced* — timed, scrolled, and pressed — because the deepening standard measures a theme by what the visitor lives through, not by what the builder assembled. All three use Heron & Quill Press (§8) and its real content.

### II.4.1 The hero — the title leaf, as a timeline

*Content (§8): imprint "Heron & Quill Press · Est. MMXIX"; H1 "Poems, printed slowly."; place line "Stroud · MMXXVI"; frontispiece: the Vandercook proof-press photograph, 1600×1200, served as AVIF ≈150KB. Visitor: desktop, 1440×900, fast 4G. The page has five leaves; the folio starts at I.*

| Time | Beat | What the visitor sees and feels |
|---|---|---|
| t≈0–350ms | Shell paints | Vellum, running head printed, title leaf present at start densities — the page never shows a blank or a spinner; it shows a page being printed |
| t=450ms | Assembly t0 (`DOMContentLoaded` + 50ms, fonts settled inside the cap) | — |
| 450–850ms | Imprint line gains ink 70%→100% | The maker's name arrives first — the book states who made it before what it is |
| 610–1010ms | First rule inks | The press settling, line by line |
| 770–1170ms | Title gains ink 55%→100% | "Poems, printed slowly." deepens into legibility that was never absent |
| 930–1330ms / 1090–1490ms | Second rule; place line | The title page completes its bibliographic order |
| 1490–1990ms | The "P" swells 70%→100% rubric (§II.1.5) | The page's one flourish, half a second of warmth; then stillness |
| ≈1100–2000ms | Frontispiece, in parallel: decode resolved at ≈1100ms with the plate already 55% visible, so the opening runs 1100–2000ms — settle done at 1800ms, clip fully open at 2000ms | The book opens flat beneath its title; the caption was readable the whole time |
| ≈2s onward | Rest | Nothing moves except the fleuron's 2% candle (§II.1.6). The visitor reads. The folio sits at I; the head's fill at 1/5 |
| ≈6s | The visitor scrolls into the contents leaf | The printer's mark settles 70%→100% over 300ms as its pin engages (§II.1.14); the contents rows begin printing at 70ms staggers; when the contents header crosses mid-viewport, the folio ticks I→II in a 200ms crossfade and the head's part name changes in the same beat |

*Checks:* with JS disabled, every beat above is absent and nothing is missing — the leaf is born printed, the plate open, the folio replaced by the leaf headers' own numerals. With reduced motion, the same: the visitor's first second is identical to the settled state. The hero's entire theatre costs the LCP nothing — the H1 is text, painted in the first frame at 55% density (≈5.9:1, legible), and the largest *asset* on the leaf (the plate) is not the LCP element.

### II.4.2 The mid-page section — the spring list (catalogue leaf)

*Content: the catalogue page's first leaf. Part-title "Leaf I — The Spring List" with its fleuron rule (§6.7). Six plate entries (§6.15), each: a plate photograph of the pamphlet, title, one-line description, apparatus line ("March MMXXVI · Edition of 340 · 12 leaves"). Entry 1 is the season's new pamphlet — the featured entry (permanent `--ink` border, rubric tick). Entry 5 is out of print. Below the entries, one apparatus line carries a counter: "Pamphlets bound by hand this season: 1,150."*

| Scroll / time | Beat | What the visitor sees and feels |
|---|---|---|
| Leaf header crosses 50% visibility | Fleuron draws: left rule 260ms, fleuron at +200ms, right rule at +420ms, fleuron inked rubric by +640ms, done +680ms (§II.1.7) | The divider is ruled before the list is read — the press prepares the page |
| Leaf trigger t0 (threshold 0.18) | Entries print: entry k starts at t0 + k×90ms, 600ms density ramp; all six printed by t0+1050ms | The catalogue arrives entry by entry, like a list being read aloud at reading pace — not a grid dumping itself at once |
| Counter line crosses 40% visibility | The count: colour steps to `--ink`, 713 → 1,150 over 900ms with `press` easing, digits tabular, landing exactly; settles over 300ms and *stays in ink* — the figure appears nowhere else on the leaf, so §II.1.8's landing rule keeps it readable | A production fact, tallied in front of the visitor; the number was true before it moved (the static HTML always held 1,150) |
| Hover on entry 3 | Border fades in (`--taupe`, 200ms); its apparatus line steps up to `--ink`; its plate settles 102%→100% over 700ms | The entry is *framed as a plate* — the catalogue acknowledges the reader's attention without lifting, shadowing, or scaling anything |
| Entry 3 loses hover | Border and apparatus step back over 200ms | The frame returns to the shelf |
| Entry 5, any pointer | Nothing responds. Its apparatus line reads "Out of print" — the status word in `--ink` inside the taupe line | The catalogue's honesty is tactile: the unavailable entry is visibly, pressably *not there to be chosen*, and says why |
| Scroll back up | Everything stays printed; the featured entry keeps its border and tick; the counter is inert text | A read catalogue stays read |

*Checks:* the featured entry is the leaf's only permanent border — a second featured entry would fail §II.1.15's one-per-leaf rule at review. On touch (<768 or coarse pointer), all six entries carry the `--taupe-60` border permanently, plates stack above titles, and the counter still tallies (750ms in the small band).

### II.4.3 The conversion section — ordering the spring pamphlet

*Content: the order leaf for pamphlet No. 6, "Field Notes". An order summary set as an apparatus block — "Field Notes, the spring pamphlet · One copy · £9" / "Posted flat, second class · £2" / total under a double rule: "£11". Then the correspondence form (§6.16): "Your name", "Where the reply should go" (email), "How many copies" (set to 1), "The address for the parcel" (textarea on ruled lines). Imprint line: "Answered within two working days. Kept on paper, not sold." Signature: "Send the letter".*

| Time | Beat | What the visitor sees and feels |
|---|---|---|
| Leaf entry | The summary block and form print per §6.3 (600ms ramp); the total's double rule is the heaviest mark on the leaf — the oldest total-marker in print doing its work | The price is apparatus, not marketing: itemised, ruled, totalled |
| t0 (visitor focuses "Your name") | Rule → `--ink` 200ms; rubric caret-line draws at the line's left over 240ms; label steps to ink | Writing on a ruled line, with the editor's mark where the pen is |
| Blur with the name written | Rule settles to `--ink` 70% — a written line stays darker | The form remembers being written on |
| Email field: visitor types "reader@press" | Nothing happens per keystroke. The theme validates on submission, once — correction is an editorial act performed on the whole letter, not a drip of rebukes | The visitor finishes their letter in peace |
| tS (signature pressed) | Submit text darkens (§6.10 timing); the email rule turns `--rubric` over 200ms; at tS+100ms the errata note gains ink over 400ms: *"For 'email' read: an address with an @ and a domain, as in reader@press.example."*; at tS+200ms focus moves to the email field, landing on a line already marked in red | Being corrected by an editor, not rejected by a machine — the note says what the line *should* say |
| Visitor corrects the address, presses the signature again | Form ink drops to 70% over 300ms; imprint line now reads "Being entered…"; the signature disables, its underline undrawn to 40% | The letter is being handled; nothing spins |
| tR (≈900ms later, server confirms) → tR+300ms | The form is replaced in place by the acknowledgement leaf, which prints over 600ms: *"Received and entered as No. 214. One copy of 'Field Notes' will be posted flat to the address given. Payment is taken when the parcel is posted."* — reference in mono | A receipt with a number that can be quoted back — the conversion ends in the theme's native currency: a fact |

*Checks:* the no-JS path is the same story told by full-page loads — submit, server-rendered errata leaf, resubmit, acknowledgement leaf — with identical wording, because the errata note is one object rendered by either path (§II.1.16). The form-level failure (server unreachable) produces the pasted slip above the form — "The letter could not be sent. Nothing was kept." — never a field error, and the visitor's typed lines survive it: a letter that failed to post is still on the desk, not in the bin.

## II.5 Full-page scroll choreography map

The standard home page (the §8 volume: five leaves — title, contents, the new season, the print room, the colophon footer). Every motion beat from the top of the page to the footer, in order. Read bottom-up, the map is the return journey: everything stays printed except the position-reporting apparatus (folio, part name, the mark's pin), which tracks the reader faithfully in both directions.

| # | Scroll position | Beat | Element(s) | What the visitor sees and feels |
|---|---|---|---|---|
| 1 | Arrival (no scroll) | Title assembly, 450→1490ms (§II.4.1) | §6.1, §6.5 | The title page prints itself in bibliographic order — ceremony: *this was made, by someone, in an order* |
| 2 | Arrival, parallel | Frontispiece opens, ≈1100→2000ms | §6.4 | The book opens flat under its title — the one piece of theatre, spent early and never repeated |
| 3 | Arrival, continuous | The candle settles into its 11s cycle | §6.6 | Stillness with a pulse — the room is attended |
| 4 | First scroll: contents leaf enters | Mark settles 70%→100% (300ms) and pins; contents rows print at 70ms staggers | §6.14, §6.18 | Orientation: the volume shows its shape, and the maker's mark takes its place in the margin for the journey |
| 5 | Contents header crosses mid-viewport | Folio ticks I→II (200ms crossfade); head's part name changes in the same beat; fill lerps to 2/5 | §6.2, §6.13 | Pagination as progress — the reader always knows where in the volume they stand |
| 6 | The new season leaf enters | Part-title fleuron draws (680ms); the leaf's text ramps (600ms); its plate settles in-frame (700ms) | §6.7, §6.3, §5 | The work itself, introduced by its divider — each part is *ruled in* before it is read |
| 7 | Mid-leaf | Links take the rubric draw on hover; nothing else moves | §6.9 | The reader's attention is answered in red ink, at the line being read |
| 8 | Print room leaf enters | Fleuron draws; the counter line crosses 40%: 211 → 340 tallies over 900ms in mono, in ink while counting, settling to taupe (the figure is repeated in the leaf's apparatus) | §6.7, §6.8 | The facts leaf: production numbers, tallied like a print run being counted off the press |
| 9 | Print room → footer approach | The mark un-pins and scrolls away with the page — no farewell animation | §6.14 | The apparatus withdraws; the book is ending |
| 10 | Footer enters | Footer fleuron draws (680ms); the colophon paragraph ramps; folio reaches V and its fill completes — and rests, with no flourish | §6.17, §6.2 | The honest ending: what it was set in, where, and what it does not do — then quiet |
| 11 | Any point, any direction | Reveals never reverse; the folio, part name, and pin always report true position | §6.3, §6.2, §6.13 | The page has a memory and a conscience: print is permanent, position is honest |

The arc the map is built to produce: **ceremony → orientation → the work → the facts → the truth, quietly.** A build whose map produces a different arc — excitement in the middle, a climax at the footer — has choreographed some other theme inside this one's clothes.

## II.6 Whole-page performance budget

Budgets are ceilings measured on the shipped build (4× CPU throttle, Moto-class device, fast 4G), not aspirations. Where a budget and a §10 gate overlap, the stricter number governs.

**Asset weight.**

| Asset | Budget | Notes |
|---|---|---|
| Fonts (total, woff2) | ≤60KB | Cormorant Garamond 500/600 + 500 italic, IBM Plex Mono 400/500 — subset to latin + latin-ext, `font-display: swap` with metric-matched fallbacks so the swap never reflows the column |
| Theme CSS | ≤14KB gzipped | The whole visual system; the title leaf's critical slice (≤2KB) is inlined in `<head>` |
| Theme JS | ≤6KB gzipped, excluding the host router | §10 gate 11: one observer, one shared rAF loop, class toggles. No animation library — loading one fails the build outright |
| Frontispiece image | ≤180KB | AVIF (WebP fallback), 1600w maximum — the frame is column-width; shipping a 4K plate to a 640px column is waste wearing quality's clothes |
| Plate images | ≤60KB each | Lazy below the second leaf; decode-gated (§II.1.4) |
| Total initial page (home) | ≤450KB | Everything above the fold's needs, counted honestly — fonts included |

**Frame and task budget.** The shared rAF loop's own work is ≤2ms per frame (cached boundary table, lerped values, style writes on at most the fill and one scrubbed element). Density ramps are CSS colour transitions — paint-only, no layout, no per-frame JS. Concurrent ramps are capped at 3 (§II.1.3), bounding worst-case paint to three leaves' text areas. No long task (>50ms) may occur after `DOMContentLoaded`: the counter writes `textContent` only on integer change; observer callbacks are batched into the frame loop. **Targets: LCP ≤2.0s** (the H1 is text in the first paint — an image is never the LCP on a title leaf), **CLS ≤0.02** (reserved everywhere: head height, folio box, plate aspect boxes, skeleton min-heights, footer facts generated not typed), **INP ≤200ms** (the press answer is a 60ms colour change; nothing on the interaction path parses, fetches, or measures layout).

**The cut order.** When a measured build exceeds its budget, cuts are taken in this order and no other — the order is the theme's values, written down so a deadline cannot improvise them:

1. The §6.6 flicker — ambience is always the first sacrifice.
2. Counters print statically (§II.1.8's battery treatment, applied to everyone).
3. The frontispiece opening becomes its 200ms density fade (§II.1.4's low-power treatment).
4. Reveal staggers collapse — leaves ramp uniformly, then (5) ramps become instant print.
6. The leaf-turn veil becomes an instant route change.

**Never cut, at any budget:** content completeness; the no-JS final state; focus visibility (§II.1.9's dual signal); error states and the errata voice; contrast floors; and the folio's *information* — under pressure it degrades to instant swaps (§II.1.2), never to absence. A build that meets its budget by cutting from the never-cut list has not met its budget; it has changed the subject.

## II.7 Build-order checklist

The sequence in which the theme is implemented. Each step is gated by the one before it; the order exists because the theme's deepest rule — *the printed page is the foundation, motion is an enhancement laid on it* — is a build order before it is a philosophy.

1. **Tokens first.** Palette, density mixes (`--ink-55/70/85`, `--rubric-70`, `--taupe-40/60`), the three easings, the type scale, the rhythm tokens (§II preamble). Nothing visual is built before the tokens exist — two builders with the same tokens produce the same element; two builders with the same *description* do not.
2. **Fonts.** Subsets cut and weighed (§II.6), fallbacks metric-checked. The assembly must look correct in the fallback serif, because on a slow connection it will be seen in it.
3. **The static leaves.** Server-render the complete page: every leaf, every number final, every plate open, footer generated. **Gate: §10 items 1, 3, 5, 9 pass now, with no JavaScript in the build at all.** If the page is not finished here, it will not be finished later — it will only be decorated.
4. **Apparatus generation.** Leaves carry `data-leaf`; folio count, contents rows, and running-head part names derive from that one structure (§10 gate 8 is wired up at this step, not audited into existence at the end).
5. **Running head + folio.** CSS sticky first (works without JS), then the JS boundary table and the scrubbed fill.
6. **Title assembly + swell**, including the focus-cancel rule (§II.1.1) — accessibility behaviours are built with their elements, not retrofitted.
7. **The reveal system.** Observer, thresholds per band, concurrency caps, the 900ms end-state timer, and the instant-print rules (focused, anchored-to, already-passed leaves).
8. **Fleuron draws + the single flicker** (grep `infinite` — exactly one hit, §10 gate 11).
9. **The frontispiece** — decode gate, clip, missing-plate honesty.
10. **Counters** — the `aria-hidden` counting span paired with its visually-hidden final value (§II.1.8), landing-colour rule implemented.
11. **Interactions.** §6.9 underlines, §6.10 press (including `pointercancel`), plate entries, contents current-tracking.
12. **Forms and loading.** Ruled fields, errata errors as single objects rendered by both server and client, the acknowledgement leaf, skeleton leaves with their 4s timeout and error conversion.
13. **The leaf-turn**, last of the motion — veil, focus handoff, scroll restoration — because it wraps every other system and must be fitted around finished parts.
14. **Footer generation** from build metadata; the colophon truth check (§10 gate 9) re-run against the final build.
15. **The reduced-motion pass.** Every §II.1 entry's variant verified element by element; the §II.6 cut order implemented as the battery-saver path.
16. **The full gate.** §10's twelve items, plus Part II spot-checks: one element per §II.1 entry re-read against the build; breakpoint passes at 1440 / 1280 / 1024 / 800 / 390 / 360px; a forced-colours pass; a print pass (the footer must print perfectly); a 200%-zoom rule-crispness pass. The theme ships when the gate passes, and not on the strength of having been built in this order.
