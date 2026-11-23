# Theme 9 — The Sunday Supplement (Expanded)

## 1. Concept & world

The Sunday Supplement is the colour section of a 1930s Sunday newspaper — the part of the paper that arrived smelling of ink, printed in four process colours on cream stock, full of comic strips, illustrated features, and pictures that were never quite in register. The theme takes that material seriously: halftone dot screens, Ben-Day colour plates, panel borders, speech balloons, a Playfair masthead — but art-directed with gallery restraint instead of cartoon noise. Nothing shouts. The cream is warm, the panels are bordered like frames in a print room, and the colour is rationed the way a 1930s press rationed it: four inks, laid down in passes, each one visible as a physical layer.

The world is a broadsheet spread flat on a breakfast table in morning light. The emotional register is *leisure and ceremony* — Sunday, not a weekday. The weekday paper informs; the supplement is *kept*. That feeling of a printed object worth keeping is the theme's persuasion engine: content presented as panels in a supplement feels collected rather than consumed, and a visitor slows down for it the way a reader slows down over the Sunday paper. The theme's signature promise is printed into its hero mechanic: **pictures are literally printed sharper as you attend to them** — the halftone screen resolves from coarse dots to fine dots as the image receives scroll attention, so looking closely is rewarded with a sharper picture, exactly as leaning toward a printed page rewards the eye.

Motion is print behaviour, never screen behaviour. Things do not fade in like slides; they are *printed*: borders draw like a press laying a frame, art fills inside its border in a hard wipe, colour plates sit 2px off-register and snap into register when touched, progress is measured in plate passes. The supplement never dissolves — it turns, wipes, and sets. Every animation in this document can be answered with "what does the press do?" and if it cannot, it does not belong here.

**Best-fit sites and audiences**

- Children's brands with illustrated worlds: picture-book publishers, toy makers with story-led ranges, children's museums and theatre. The panel grammar is native to how children already read.
- Illustration studios and illustrators' collectives: the portfolio *is* a supplement — each commission a panel, each case study a strip, with the halftone screen as the house print finish.
- Weekend and leisure magazines: food, gardening, slow travel, puzzles, craft — editorial products whose natural rhythm is the weekly issue, not the daily feed.
- Family leisure venues: zoos, aquariums, science centres, heritage railways — anywhere the visit is a Sunday ritual and the site sells anticipation of a day out.
- Comic and graphic-novel publishers, festival programmes, and reading schemes: the theme is their own material, formalised.
- Any brand whose content arrives in *issues* — a numbered, dated, collectable rhythm — and whose audience is trusted to read in order.

**When NOT to use it**

- Anything urgent, transactional, or high-frequency: news tickers, trading, live scores, flash commerce. The supplement's ceremony reads as slowness where speed is the product.
- Data-dense tools and dashboards: panel borders, dot screens, and plate colour fight tables, filters, and dense controls at every turn.
- Photography-led luxury: the halftone screen deliberately degrades photographic fidelity into print. A brand whose promise is the unmediated photograph (high fashion, automotive beauty shots) should not screen its pictures into dots.
- Brands with no illustrated or panel-shaped content. The theme runs on panels, strips, plates, and captions. If the content is a wall of prose or a grid of identical product shots, the supplement becomes a costume and §9 will fail it.
- Dark, sombre, or memorial subjects: four-colour Sunday cheer is the wrong register for grief, crisis, or clinical gravity, and no palette discipline fixes that.

## 2. Palette

Five inks, all flat. There are no gradients in this theme except the two places the press itself produces them: the halftone screen (dots, not blends) and the paper-edge shadow of the page-turn (§6.12), which is a printed drop shadow rendered as offset flat plates, never a blur. Colour is laid in *plates* — a colour area is a separate layer from the ink line-work, offset by exactly 2px at rest (§6.4), and that physical separation is visible everywhere colour appears.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--paper` | `#F6ECD4` | Supplement cream; the page ground, panel interiors at rest | ~62% of any viewport | Ground for all text. Against `--ink` the contrast is 13.1:1. Never used as a text colour except reversed out of full `--ink` panels (rare, §6.14 cards only). |
| `--ink` | `#20242A` | Line-work ink: panel borders, body text, masthead lettering, balloon outlines | ~18% as drawn area, structurally everywhere | On `--paper` 13.1:1 — passes AAA at every size. The only colour body text may use. All borders are ink; there is no grey border anywhere in the theme. |
| `--red` | `#D43D2A` | Process red plate: first progress pass, rubric moments, the funniest page's extra misregistration, error ink | ~7% | On `--paper` 4.6:1 — passes AA for text ≥14px and for all non-text marks; body copy in red is forbidden. On `--ink` 3.4:1 — graphic use only, never text. Red is the first plate laid and the loudest voice; ration it like one. |
| `--teal` | `#1F6E6A` | Teal plate: second progress pass, links, secondary headings, calm features | ~7% | On `--paper` 5.6:1 — passes AA for normal text, so teal is the only plate colour permitted for short text runs (links, kickers, captions' speakers). On `--ink` 2.9:1 — never text. |
| `--mustard` | `#E0A51E` | Mustard plate: third progress pass, highlights, the sun in any illustrated plate, badges | ~6% | On `--paper` 2.1:1 — fails text contrast by design: mustard is a *plate*, never a letter. Mustard text is permitted only reversed on `--ink` (7.3:1) at ≥16px, e.g. the footer imprint (§6.16). Any mustard word on cream is a §9 failure. |

**Derived tokens** (computed from the five inks, never new hues):

| Token | Derivation | Used for |
|---|---|---|
| `--paper-deep` | `#EFE0BC` (paper darkened one press pass) | Panel interior shading, the strip beneath the pinned masthead, skeleton plate ground |
| `--ink-60` | ink at 60% via `color-mix` | Halftone dot colour at coarse pitch, caption speaker rules, disabled borders |
| `--red-wash` | red at 10% on paper | Error field ground (§6.15), the funniest page's plate bed |
| `--teal-wash` | teal at 12% on paper | Link hover bed, selected panel fill |
| `--mustard-wash` | mustard at 16% on paper | Badge beds, the registration bar's unfilled track |
| `--plate-shadow` | ink at 22%, offset flat (4px 4px 0) | The printed drop shadow under lifted panels and the page-turn edge — always hard-edged, never blurred |

**Plate discipline (hard rules)**

- Colour always sits on its own layer, offset **2px** (one channel only — red plate shifts +2px x, 0 y at rest; the full rule is §6.4) behind the ink line-work. Flat colour directly under its lines, perfectly registered at rest, reads as a vector illustration, not a print — that is the theme's most common failure (§9.1).
- Exactly one plate colour may dominate a panel. A panel is "the red panel" or "the teal panel"; panels that use all four plates at full strength are reserved for the hero plate and the finale.
- Mustard never touches red directly (they vibrate at 1930s print contrast); separate them with ink line-work or a paper gap of ≥8px.
- The four progress colours always appear in press order — red, teal, mustard, ink — in the registration bar (§6.5), in loading skeletons, and anywhere else sequence is shown. Any other order is wrong in a way print-literate visitors feel without naming.

**Dark-mode behaviour.** A Sunday supplement is read in daylight; the theme ships **no dark mode** and says so. If the host product forces a dark scheme, the ruling is a *lamplight* variant, not an inversion: `--paper` becomes `#EAD9AE` (the same cream under tungsten light — hue held, lightness dropped ~8%), `--ink` deepens to `#17191D`, plates hold their hexes (print inks do not change under lamplight; paper does). All motion specs survive unchanged because every spec is written against tokens, not raw hexes. Do not ship a black-background version: a black supplement is a different object (a cinema programme) and belongs to another theme.

## 3. Typography

Two faces. Playfair Display carries the paper's public voice — masthead, headlines, numerals — and Lora carries the reading voice — features, captions, body. A third face appearing anywhere is a §9 failure.

**Playfair Display** — high-contrast Didone serif; its thin horizontals and ball terminals are the letterforms of a newspaper nameplate. Weights: 700 (masthead, headlines), 900 (masthead "Sunday" flourish and the registration numerals), 500 italic (standfirsts and plate credits only). Playfair is never set below 20px: its hairlines vanish at text sizes, which is precisely why Lora exists here.

**Lora** — a sturdy serif with calligraphic roots that survives small sizes and halftone company. Weights: 400 (body, captions), 500 (panel headings at small sizes, form labels), 600 (card titles), italic 400 (captions — the hand-lettered voice, see below). Lora italic is the theme's hand: captions are set in Lora italic with +0.01em letterspacing to imitate lettering laid in after the art, and they *arrive* lettered (§6.2), never typed.

**Type scale** (root 16px; the broadsheet column is wide, so the scale is generous at the top and disciplined at the bottom):

| Role | Face / weight | Size | Line-height | Tracking | Notes |
|---|---|---|---|---|---|
| Masthead | Playfair 900 | 84px desktop / 52px mobile | 0.95 | -0.01em | The paper's name. "Sunday" carries the bounce-settle flourish (§6.6); the rest of the nameplate is set, not flourished. |
| Plate headline (hero) | Playfair 700 | 54px / 36px | 1.02 | -0.005em | Sentence case with a capitalised first word in the newspaper manner; never all-caps. |
| Feature headline | Playfair 700 | 38px / 30px | 1.08 | 0 | One per panel maximum; a panel with two headlines is two panels. |
| Panel heading | Lora 600 | 22px / 20px | 1.2 | 0 | For card and strip panels where Playfair would shout. |
| Standfirst | Playfair 500 italic | 20px / 18px | 1.45 | 0 | The italic summary under a headline; the only italic Playfair on the page. |
| Body | Lora 400 | 17px | 1.62 | 0 | Measure 58–66ch inside panels; justified text is forbidden (ragged right, like the columns). |
| Caption | Lora 400 italic | 14.5px | 1.5 | +0.01em | The lettered voice. Always under or inside its panel, always after the art (§6.2). |
| Apparatus (folios, dates, plate numbers) | Lora 500, uppercase | 11.5px | 1.3 | +0.14em | The small print of the paper: "No. 214 · Sunday · Price: one smile" energy — real data only. |
| Data & counters | Playfair 700, tabular | 34px | 1.1 | 0 | Circulation and panel counts (§5); Playfair numerals are old-style by default — enable `font-variant-numeric: tabular-nums lining-nums` so counters never reflow. |
| Form label | Lora 500, uppercase | 12px | 1.3 | +0.1em | Set like a coupon's small print (§6.15). |
| Error text | Lora 400 italic | 14px | 1.45 | 0 | In `--red`, in the caption voice — the paper corrects you like a caption, not an alarm (§12). |

**Typographic laws**

- Headlines are never underlined, never linked-looking; links live in body text in `--teal` with a 1px ink underline offset 3px.
- The word "Sunday" in the masthead is the only lettering allowed an overshoot flourish. Flourish anywhere else is clip-art (§9.6).
- Numerals in running text are old-style (Lora default); numerals that *count* (counters, prices, dates in apparatus) are lining tabular via Playfair or the apparatus style — the distinction is print-correct: the paper sets its stories in old-style and its facts in lining figures.
- Drop caps: the first feature on a page may open with a 3-line Playfair drop cap in the panel's plate colour. One per page. It is a plate, so it sits 2px off-register like all plates (§6.4) until hovered.


## 4. Layout language

The page is a **broadsheet of bordered panels in reading order**. Every content unit lives inside a panel: a rectangle with a 2.5px `--ink` border, a paper or wash interior, and — for illustrated panels — a colour plate offset behind the line-work. There is no borderless content on the page except the masthead furniture and the footer imprint; a section without a panel border is a layout error, not a minimal choice.

**Grid.** A 12-column broadsheet grid, max width 1240px, gutters of 20px that read as the white column-gaps between printed panels. Panels span in print fractions only: full-width *strips* (12), half panels (6+6), thirds (4+4+4), and the classic supplement arrangement — one tall half panel (6) beside two stacked quarters (6 split vertically). Mixed spans within one row are encouraged; uniform card grids of identical panels are the weekday web leaking in (§9.4). Panel padding is 28px desktop, 18px mobile; the border is always 2.5px ink, corners square — a 1930s press has no radius. (Interactive states may not round corners either; the register snap is this theme's "hover lift".)

**Spacing rhythm.** The base unit is the **column inch**: 8px. Vertical rhythm between panels is 3 units (24px) within a strip, 6 units (48px) between strips, and a full 12 units (96px) of paper before the finale/finishing panel — the supplement breathes more as it ends, like the last page of the colour section. Inside panels, caption sits 12px below its art, headline 16px above its standfirst, apparatus lines hug panel corners at 12px insets.

**Section choreography.** A page reads as one issue, top to bottom: (1) masthead panel with the registration bar at its foot; (2) the hero plate panel — the issue's cover picture; (3) the first comic strip, scrolling beneath the pinned masthead (§6.7); (4) feature panels in reading order, alternating plate colours; (5) a full-width strip panel (the panorama — listings, a timeline, a wide illustration); (6) the conversion panel (subscription coupon, §6.15) set as the supplement's own back-page offer; (7) the imprint footer. No page type reorders the masthead or the imprint; features may vary freely between them.

**Density rules.** Maximum five panels in any viewport height at 1200px wide; the supplement is a *spread*, not a feed. Imagery ratio: at least one illustrated panel in every three. Text-only panels carry a self-drawn balloon-tail flourish or a fleuron rule so the print furniture never fully disappears. Whitespace is paper, and paper is a material here: the cream ground showing between panels is the table the broadsheet lies on — never fill it with background patterns, tints, or floating shapes. The only permitted ground texture is the cream-grain drift of §6.11 at ±4% — felt, not seen.

**The register grid.** Plates offset +2px x / 0 y from their ink layer at rest (red channel only — see §6.4 for the full channel rule). Every illustrated element on the page obeys the same offset, so the whole page feels printed by one press in one pass. Elements that cannot carry a plate (body text, form fields) are pure ink and never offset — type was printed last and sits true.

## 5. Full motion system

One scroll engine drives everything scrubbed: a single `requestAnimationFrame` loop lerping a virtual scroll position toward the real one at **0.12** per frame, from which dot pitch, register drift, progress quarters, and strip parallax are all derived — one press, one drive shaft. Triggered (non-scrubbed) animations run on the named easings below and nowhere else.

**Named easings (the press's four movements)**

| Name | Curve | Used for |
|---|---|---|
| `press` | `cubic-bezier(.6,0,.3,1)` | Border draws, plate fills — the press coming down: slow contact, firm set |
| `turn` | `cubic-bezier(.77,0,.18,1)` | Hard wipes and the page-turn — paper moving at constant will |
| `snap` | `cubic-bezier(.3,1.35,.35,1)` | Register snap and balloon pop — a mechanical settle with one overshoot tooth |
| `settle` | `cubic-bezier(.34,1.4,.64,1)` | Masthead bounce-settle — hand-lettered ink relaxing onto the page |

**Every motion term, in this theme's language**

| Motion term | The Supplement's version | Duration / trigger |
|---|---|---|
| Scroll-triggered reveals | Panels reveal as press passes: border draws (450ms `press`), art wipes in, caption letters in last (§6.2) | On panel entering the lower 75% of the viewport, reading-order stagger 120ms between panels in the same strip |
| Parallax | Colour plates drift against their ink layer: register offset breathes 2px → 3.5px → 2px across a panel's viewport transit (§6.4) | Scrubbed to scroll via the shared loop |
| Pinned scenes | The masthead pins for the length of the first strip (~150vh) while panels scroll beneath (§6.7) | Scroll-scrubbed pin |
| Masked line reveals | Headlines are unmasked by a hard clip wipe in reading direction — the line is *set* left to right, never faded | 380ms `turn`, on panel reveal, after the border completes |
| Blur-to-sharp reveals | Print-sharp, not optical: the halftone resolve (§6.1) — coarse dots (14px pitch) refine to fine (3px) as attention lands | Scrubbed across the hero's viewport transit; triggered 900ms `press` variant for in-strip images |
| Animated counters | Circulation and "panels in this issue" count up in Playfair lining numerals, digit rolls settling like a press counter | 1200ms `press`, once, when the apparatus panel enters |
| Progress indicators | The four-colour registration bar (§6.5): red, teal, mustard, ink quarters fill in press order, each scrubbed to its quarter of total scroll | Continuous scrub |
| Marquees | Exactly one: the contents ticker under the masthead on listing pages — a slow column-rule crawl of section names separated by fleurons, 40s per loop, pausable on hover | Ambient; never on the home page, never more than one |
| Ambient loops | Living-print shimmer: dot screens breathe ±4% opacity on a 5s loop, offset per image, over the cream-grain drift (§6.11) | Continuous, paused off-screen |
| Micro-interactions | Register snap on hover (§6.4), caption-balloon pop on click (§6.10), panel corner-lift tilt (max 1.2°, §6.14) | 200–220ms |
| Hover physics | The corner-lift: a panel lifts its bottom-right corner 6px with the flat `--plate-shadow` growing 4px→7px, `snap` ease — paper, not glass: no gloss, no blur shadow | 180ms in, 240ms out |
| Page transitions | The page-turn: hard wipe with a visible paper edge and flat shadow plate, 350ms `turn` (§6.12) | Route change |
| Image treatments | All imagery is halftone-screened (SVG filter or pre-rendered dot plate), scale-in-frame 1.07→1 with rescreening (§6.9); no unscreened photograph may appear anywhere | Scrubbed / on reveal |
| Loading states | Coarse-dot skeleton plates that resolve as content arrives (§6.12) | Until content lands, 1.2s maximum before the fallback strips the screen entirely |
| Reduced motion | Halftones pre-resolved to fine pitch, panels stacked plainly with borders pre-drawn, plates pre-snapped to register on the hero only, no pin, no shimmer, counters at final values | `prefers-reduced-motion` — a still, fully printed page |

**Motion budget per viewport:** at most one scrubbed hero effect, one pinned scene, and one ambient shimmer family active at once; triggered animations queue behind the panel stagger so no more than three panels animate simultaneously. If a fourth panel enters mid-stagger, it appears pre-printed (borders drawn, art in) rather than joining the queue late — the press never rushes.


## 6. Signature elements

Each element below carries its full build spec, then its v2 deepening layers: a millisecond choreography timeline, a complete state matrix, breakpoint behaviour, edge cases, an accessibility spec, and the exact tokens it consumes. Token names are normative — two builders using these names produce the same element.

### 6.1 Coarse-to-fine halftone resolve (the hero picture)

**What & why.** The hero image enters the page as a coarse halftone — dot pitch ~14px, the picture barely legible, pure print texture — and resolves continuously to a fine 3px screen as it scrolls into full view. The picture is *printed sharper by attention*: the longer and more fully the visitor looks, the finer the print. It is the theme's thesis in one mechanic, and it belongs to this theme because the halftone screen is not an effect applied to the photograph — in a 1930s supplement the dots *are* the photograph, the only form it ever had.

**Structure.** The hero panel contains three stacked layers inside its ink border: (1) the image itself, pre-rendered or SVG-filtered into a halftone plate at fine pitch — this is the base layer and the no-JS final state; (2) a coarse-screen overlay plate (same image, 14px pitch, rendered as an SVG `<pattern>` of ink dots over a duotone of the image, or a second filtered copy) whose opacity and dot scale are scrubbed; (3) the caption plate (§6.2's caption, lettered last). Implementation: one `<figure class="plate-hero">` with two absolutely-positioned screened copies and a `<figcaption>`; the scrub variable `--resolve` (0→1) is written by the shared scroll loop onto the figure, and CSS derives overlay opacity (`1 - var(--resolve)`) and overlay dot scale from it. No canvas required; a canvas variant is permitted only if it degrades to the same two-layer DOM.

**Motion spec.** Scrubbed, not triggered: `--resolve` maps the hero's transit from "top enters at 85% viewport height" (0) to "hero centre reaches viewport centre" (1), lerped at 0.12 by the shared loop. Dot pitch interpolates 14px → 3px across the same range; overlay opacity 1 → 0 across the final 30% so the fine plate lands cleanly. If the visitor loads mid-page with the hero already past centre, `--resolve` starts at 1 — the picture is simply printed.

**States.** Rest (unresolved, coarse) → resolving (scrubbed) → resolved (fine, final). Hover does nothing here — the hero's interaction is attention, not touch; its plate still obeys the global register rule (§6.4) at 2px.

**Content-merge.** The dots are the photograph's own screen. There is no separate decoration: remove the effect and the image remains, sharper. The headline and standfirst sit in the same panel, in ink, unscreened — type was printed after the plate and stays true.

**Failure fallback.** The base layer is the fully resolved fine image, present in the DOM from first paint. The coarse overlay is added by JS only after the scroll loop is running. If JS fails, is blocked, or the loop errors, the visitor sees the finished picture. A 1.2s watchdog: if `--resolve` has not been written within 1.2s of load, the overlay is removed by class, permanently for that page view.

**Reduced-motion variant.** Overlay never added; hero ships pre-resolved at 3px pitch. The theme's own standing rule: *halftones shown pre-resolved*.

**Performance budget & mobile variant.** Two screened copies of one image: combined image payload ≤ 260KB (AVIF/WebP, hero width ≤ 1600px). The scrub writes one CSS variable per frame on one element — no layout, no paint beyond the figure. On <768px the coarse start pitch drops to 11px (dots must stay legible as dots on a small screen, not become mud) and the overlay copy is served at 800px width; total ≤ 150KB.

**Choreography timeline** (relative to hero top crossing 85% viewport height = t₀ of the scrub; values are scroll positions, since the beat is scrubbed — the timeline is spatial):

| Beat | Scroll position | What happens |
|---|---|---|
| 1 | Hero top at 85% vh | Coarse plate fully present (14px pitch); border already drawn by §6.2's pass if the hero is a revealed panel, or pre-drawn if above the fold |
| 2 | Hero top at 60% vh | `--resolve` ≈ 0.35: pitch ≈ 10px; faces and large shapes legible; caption not yet lettered |
| 3 | Hero top at 35% vh | `--resolve` ≈ 0.7: pitch ≈ 6px; overlay opacity begins its fade (from `--resolve` 0.7) |
| 4 | Hero centre at 50% vh | `--resolve` = 1: pitch 3px, overlay opacity 0 and `visibility:hidden` after a 120ms settle; caption lettering triggers (§6.2 beat 3) |
| 5 | Any time after | Resolved state is sticky scrolling down; scrolling back above beat 2 does NOT re-coarsen (a printed page does not unprint) — `--resolve` is a ratchet, max-so-far |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (below fold) | Coarse plate shown if in DOM; no work done until near viewport (loop skips off-screen figures) | Same; overlay copy is the 800px asset |
| Resolving | Pitch/opacity scrubbed per frame from lerped scroll | Identical — scrub is scroll-driven, not pointer-driven |
| Resolved | Fine plate only; overlay hidden; caption lettered | Same |
| Hover | No change (attention mechanic, not hover) | n/a |
| Focus (figure focusable only if it is a link) | Register snap applies to the plate (§6.4); resolve state unchanged | n/a |
| Scrolled-past | Stays resolved (ratchet) | Same |
| Disabled / no-JS | Fine plate only — the base layer is the final state | Same |

**Breakpoint behaviour.** ≥1200px: full spec, 14→3px. 768–1199px: start pitch 12px, hero width ≤ 1200px asset. <768px: start pitch 11px, end pitch 3.5px (a 3px dot on a 360px screen is below the print illusion's floor), overlay asset 800px, and the scrub range compresses — resolve completes by hero top at 45% vh, because a phone viewport gives the picture less travel.

**Edge cases.** *Slow network:* the fine base layer loads first (it is the `<img>`); the coarse overlay is a progressive enhancement requested after `load` — on a slow connection the visitor simply sees the sharp picture arrive, never a stuck abstraction. *Huge hero / short hero:* pitch is a function of `--resolve`, not of pixel height, so any aspect ratio resolves identically. *User scrolls back up:* ratchet holds (see beat 5). *Print stylesheet:* overlay suppressed, fine plate prints. *Image fails to load:* the panel shows its `--paper-deep` interior with the caption and a fleuron — the panel grammar survives a missing plate.

**Accessibility spec.** The figure's `alt` carries the picture's real description — the screen effect never alters the accessible name. The resolve is decorative motion: it is not announced, has no ARIA live behaviour, and conveys no information (the resolved image is identical in content). Under `prefers-reduced-motion` it never runs. Contrast: caption text sits on `--paper`, never on the screened image, so dot density can never degrade text contrast. The hero is not focusable unless it is a genuine link, in which case the panel border takes the focus treatment of §11 (buttons/links row).

**Tokens consumed.** `--paper`, `--paper-deep`, `--ink`, `--ink-60`, `--resolve` (element-local, 0→1), `--dot-coarse` (14px), `--dot-fine` (3px), `--loop-lerp` (0.12), `--fallback-strip` (1.2s).

### 6.2 Border-draw panel reveals

**What & why.** Every panel arrives the way a press lays it down: first the border draws itself, then the art fills inside, then the caption is lettered in. Three beats, in print order. It belongs here because the panel is the theme's atom, and a panel that simply fades in has skipped its own manufacture — the draw *is* the panel being made in front of the reader.

**Structure.** Each panel is a `<section class="panel">` containing an SVG rectangle (or four `<span class="rule">` edges where SVG is impractical) traced at the panel's inset, the content wrapper, and the caption as a separate `<figcaption>`-equivalent block. The border path length is normalised (`pathLength="100"`) so one dash animation serves every panel size. Content starts in its final layout — the reveal masks and draws, it never reflows.

**Motion spec.** Trigger: panel's top crosses 75% viewport height; panels in the same strip stagger 120ms apart in reading order. Beat 1 — border: stroke-dashoffset 100→0 over **450ms `press`**, drawn clockwise from the top-left corner (the press starts at the corner the reader starts at). Beat 2 — art fill: the panel's interior (image or wash) wipes in via `clip-path: inset()` from left, **300ms `turn`**, starting 120ms before the border completes (the press overlaps its passes). Beat 3 — caption: lettered in word by word, Lora italic fading/sliding 4px per word at **45ms per word**, starting **150ms** after the art lands. Headline unmask (§5) runs with beat 2.

**States.** Unprinted (border undrawn, art masked, caption unlettered — but all present in layout) → printing (beats 1–3) → printed. Scrolled-past: printed, permanently. Hover/focus: no reveal change; §6.4/§6.14 interactions layer on top of the printed state.

**Content-merge.** The three beats are the panel's own three parts — frame, picture, caption — in manufacturing order. Nothing decorative is added; the reveal is the panel's biography.

**Failure fallback.** All three beats are JS-added start states. Without JS, or if the observer fails, panels render fully printed (borders as ordinary CSS borders — the SVG trace is an overlay on a real border, never a replacement for it). A per-panel 900ms watchdog forces the printed class if its trigger never fires.

**Reduced-motion variant.** Panels appear printed: border solid, art in place, caption fully lettered. The reading-order stagger is dropped entirely.

**Performance budget & mobile variant.** One shared IntersectionObserver; the draw is a stroke animation on compositor-friendly properties only. Max three panels printing concurrently (§5 budget); a fourth appears printed. Mobile: border draw shortens to 320ms and caption lettering becomes a single 200ms fade — small screens get the same order of events at a brisker press speed.

**Choreography timeline** (per panel, t₀ = trigger):

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Border draw begins, top-left corner, clockwise |
| 2 | t₀ + 330ms | Art wipe begins (border at ~73%) |
| 3 | t₀ + 450ms | Border completes; headline unmask finishes with the wipe |
| 4 | t₀ + 630ms | Art fully filled |
| 5 | t₀ + 780ms | Caption lettering begins (150ms after art lands) |
| 6 | t₀ + 780ms + 45ms × word count | Caption complete; panel marked printed; balloon tails (§6.8) draw if present |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Unprinted | In layout, masked by JS-added classes only | Same |
| Printing | Beats run in order; stagger 120ms within a strip | Beats run; border 320ms, caption single fade |
| Printed | Final state; hover interactions (§6.4) live | Final state; tap = hover equivalent where applicable |
| Hover | No reveal change | n/a |
| Focus within | Panel is printed before focus can land inside it (focus scroll triggers the reveal at 85% vh, earlier than the 75% trigger) | Same |
| Scrolled-past | Printed, never re-runs | Same |
| Disabled / no-JS | Printed by default | Same |

**Breakpoint behaviour.** ≥1200px: full spec. 768–1199px: stagger 100ms, border 400ms. <768px: border 320ms, caption lettering replaced by one fade, stagger 80ms, and panels reveal at 80% vh (a phone shows fewer panels; each deserves its full manufacture).

**Edge cases.** *Very tall panel (>150vh):* trigger fires on top entry as usual; the art wipe applies to the first viewport-height of the panel and the rest is pre-printed — a panel must never be half-masked while its lower half is being read. *Content shorter than expected (empty panel):* an empty panel is a build error, but if one ships, it prints as a bordered empty frame with its caption — the grammar holds. *User scrolls fast:* panels passed entirely between frames are set printed by the observer's initial check, never left masked. *User scrolls back up:* printed is terminal. *Slow network with late images:* the border and caption keep their beats; the art wipe runs when the image lands or after 600ms, whichever first — the frame never waits empty for a late plate.

**Accessibility spec.** Reveal state is purely presentational: content is in the accessibility tree in reading order from first paint, never `display:none` or `visibility:hidden` for the unprinted state (masking is by clip and stroke only). Focus order follows the DOM, not the stagger. Focus landing inside an unprinted panel forces its immediate print (no animation) so a keyboard user never tabs into a masked region. Caption lettering animates opacity per word — screen readers read the whole caption at once, unaffected.

**Tokens consumed.** `--ink`, `--paper`, `--ease-press`, `--ease-turn`, `--draw-border` (450ms), `--wipe-art` (300ms), `--letter-word` (45ms), `--stagger-panel` (120ms), `--watchdog-panel` (900ms).


### 6.3 Hard panel wipes

**What & why.** Moving between feature panels — within a strip carousel, a tabbed feature, or a panel-to-panel "next in the strip" step — uses a hard border-sweep wipe: the panel's own border edge sweeps across its frame and the next panel is behind it. No crossfade, ever. It belongs here because the supplement *turns*; a dissolve is film grammar, and this is a paper object. The wipe is the physical act of the printed sheet being pulled across.

**Structure.** A `.panel-stage` clips its children (`overflow:hidden`, ink border on the stage, not the children). Two panel layers stack; the incoming layer is revealed by animating a `clip-path: inset(0 0 0 X%)` — or, in the preferred build, the outgoing layer is covered by an ink-edged "sheet" div whose leading edge is a 2.5px ink rule with a flat `--plate-shadow` plate behind it, sweeping left→right for forward navigation, right→left for back. Direction follows reading direction, always.

**Motion spec.** **300ms `turn`**, one sweep, no bounce, no fade at either end. The leading edge's ink rule is visible for the whole sweep; the trailing 24px carries the flat shadow plate so the eye reads a sheet edge, not a mask. Trigger: explicit visitor action (next/previous control, tab switch, strip pagination) — never autoplay. During the sweep, both panels are inert.

**States.** Idle (one panel shown) → sweeping (300ms, controls locked) → idle (new panel). Rapid repeat clicks queue at most one pending step; further clicks are ignored, not stacked.

**Content-merge.** The sweeping edge is the panel border itself — the frame does the work. The incoming content is a real sibling panel in the same strip, not a modal or overlay.

**Failure fallback.** If clip-path or the animation is unavailable, the swap is instant (panels exchange with no motion). Content is never left half-covered: a `transitionend` watchdog at 380ms forces the end state.

**Reduced-motion variant.** Instant swap. A 1px ink outline pulse (120ms, opacity only) may mark the change for orientation; nothing sweeps.

**Performance budget & mobile variant.** One clip-path animation on one element — negligible. Mobile: duration 260ms; swipe gestures (touch drag following the finger, release past 35% completes the wipe at the same `turn` ease) are permitted because the finger *is* pulling the sheet — the only gesture-driven motion in the theme.

**Choreography timeline** (t₀ = activation):

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Controls lock; sheet edge enters at the reading-start side, ink rule + shadow plate visible |
| 2 | t₀ + 150ms | Sweep at 50%; outgoing and incoming panels each half-visible, divided by the moving rule |
| 3 | t₀ + 300ms | Sweep complete; incoming panel full; its caption re-letters only if it has never been printed — otherwise it arrives printed |
| 4 | t₀ + 380ms | Watchdog deadline: any unfinished state is forced to beat 3 |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Current panel shown; next/prev controls at apparatus size | Same; swipe also available |
| Hover (on controls) | Control's ink darkens; the stage border thickens 2.5→3.5px on the entry side, previewing direction | n/a |
| Focus | Control takes the theme focus ring (§11); Enter/Space fires the wipe | n/a |
| Active (sweeping) | 300ms sweep; controls locked | Gesture drag tracks finger; release <35% springs back 160ms `snap` |
| Scrolled-past | Stage shows its last-selected panel; no reset on scroll | Same |
| Disabled | If the strip has one panel, controls are absent (not greyed) — a one-panel strip has nothing to turn to | Same |

**Breakpoint behaviour.** ≥1200px and 768–1199px: identical spec. <768px: 260ms, gesture enabled, and the shadow plate narrows to 16px (a phone screen cannot spare 24px of theatre).

**Edge cases.** *Panels of unequal height:* the stage height animates with the sweep (height is the one layout property permitted to animate here, 300ms same ease) — or, where content allows, the stage is fixed to the tallest panel and shorter panels letterbox on paper; choose per build, never mix. *Images not yet loaded in the incoming panel:* the panel arrives with its coarse skeleton (§6.12) behind the wipe — the turn is never delayed for a plate. *Backwards navigation:* sweep reverses direction; the press order of the strip is spatial, not temporal. *Rapid keyboard repeats:* the one-pending-step queue applies identically.

**Accessibility spec.** The stage is a `region` with an `aria-label` naming the strip ("The Millers' Garden strip, panel 2 of 4"); panel changes update a visually-hidden live region politely. Focus never moves on a wipe unless the visitor activated a control that disappears (it never does — controls persist). The incoming panel's heading is not auto-focused. Keyboard: Left/Right arrows operate the stage when it has focus-within. Touch targets for next/prev ≥ 44px.

**Tokens consumed.** `--ink`, `--plate-shadow`, `--ease-turn`, `--wipe-panel` (300ms), `--watchdog-wipe` (380ms), `--shadow-plate-w` (24px).

### 6.4 Register-snap hover

**What & why.** Every colour plate on the page rests exactly **2px off-register** — the red plate shifted +2px on x behind its ink line-work — the honest misregistration of a real press run. Hovering a panel animates its colour channels into perfect register over 200ms: *hover fixes the print*. Leaving restores the honest 2px. It belongs here because misregistration is the supplement's most recognisable physical truth, and making the visitor the one who corrects it turns a print flaw into the theme's central micro-interaction. On the funniest page (the humour feature, designated per build), plates rest at **3px** off and snap further — the joke is printed worst and corrected most, and §9 protects this from becoming a bug report.

**Structure.** Each illustrated element is two layers: `.plate` (colour, a duotone/plate rendering or the colour image) translated by the register offset, and `.linework` (ink layer: borders, line art, the image's ink pass) unshifted above it. In practice for photographic content: one image rendered twice — a colour copy (plate, translated) and a high-contrast ink-screened copy at 88% opacity above it — or a single image with an SVG filter splitting channels; the two-layer DOM is the reference build. The offset lives in one variable, `--reg` (default 2px), written per panel.

**Motion spec.** Hover/focus: `--reg` animates 2px → 0 over **200ms `snap`** (the overshoot tooth is ±0.4px — the plate kisses register and settles). Leave: 0 → 2px over 260ms `press` (the press drifts back slower than it was corrected — entropy is unhurried). Scrubbed companion behaviour: as a panel transits the viewport, `--reg` breathes 2px → 3.5px → 2px via the shared loop (§5 parallax) — hover/focus overrides the breath to 0 for as long as it lasts.

**States.** Rest 2px (3px on the funniest page) → breathing (scroll transit, 2–3.5px) → snapped (hover/focus, 0) → returning (260ms) → rest. Touch: first tap snaps (and the panel's tap target still fires on the same tap — the snap is visual only, never a click tax).

**Content-merge.** The misregistration is a property of the very image being read; the visitor corrects the printing of the picture in front of them. Text is never offset (type sits true, §4), so readability is never the price of the effect.

**Failure fallback.** If transforms are unavailable or JS is off, plates render at `--reg: 0` — perfectly registered, fully legible. Misregistration is an enhancement layered onto a correct page, never the default state of the raw markup: the DOM ships registered, JS applies the offset.

**Reduced-motion variant.** Plates rest registered (0px) throughout; hover produces no motion — a 120ms opacity pulse on the plate (to 92%) marks the hover instead. The print is pre-corrected for readers who ask for stillness.

**Performance budget & mobile variant.** Transform on one layer per panel — compositor-only. The breath writes `--reg` only for panels within one viewport of travel. Mobile: no hover, so the snap fires on tap and on scroll-centring — when a panel crosses viewport centre, its plate snaps to 0 for the duration of its centre transit (±15% vh), giving touch visitors the correction without a pointer. Breath amplitude on mobile: 2→3px.

**Choreography timeline** (hover, t₀ = pointer enter):

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Breath (if running) yields; `--reg` begins 2→0, `snap` |
| 2 | t₀ + 140ms | `--reg` ≈ 0.3px; overshoot tooth approaches |
| 3 | t₀ + 200ms | `--reg` = 0 (after a ±0.4px settle at ~170ms); panel fully registered |
| 4 | Pointer leave + 0ms | Return begins, `press` |
| 5 | Leave + 260ms | `--reg` back to rest (2px / 3px funniest page); breath resumes if panel is in transit |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | 2px off (3px funniest page) | 2px off |
| Scrolled transit | Breath 2→3.5→2px scrubbed | Breath 2→3px; centre-transit snap to 0 within ±15% vh of centre |
| Hover | Snap to 0 in 200ms | n/a (tap instead) |
| Focus | Snap to 0 in 200ms — keyboard visitors get the correction too | External keyboard: same |
| Active (tap/click) | Snap holds while pressed | Tap snaps instantly to 0 and holds 600ms after release if no navigation follows |
| Scrolled-past | Rest offset; breath stops off-screen | Same |
| Disabled / no-JS | 0px — registered by default | Same |

**Breakpoint behaviour.** ≥1200px: full spec. 768–1199px: breath amplitude 2→3px. <768px: no breath (a small screen's plates are small; drift reads as blur, not print) — rest 2px, centre-snap only.

**Edge cases.** *The funniest page designation:* exactly one page/section per site carries 3px rest offset; if a build cannot decide which is funniest, none does — 3px everywhere is a defect, not a style (§9.1). *Plates inside the pinned strip (§6.7):* breath continues under the pin; hover snap works identically. *Very small plates (<80px wide):* offset caps at 1.5px — below that the misregistration exceeds the plate's own line weight and reads as damage. *User prefers contrast:* `prefers-contrast: more` forces `--reg: 0` at all times (misregistration is a contrast hazard for some readers). *Print:* plates print registered.

**Accessibility spec.** The offset never applies to text, borders carrying meaning, or form elements. Focus triggers the snap so the focused panel is always the sharpest-registered object on screen — the correction is an orientation aid, not a reward for pointer users only. Contrast is computed at the *rest* offset (worst case): plate colours against paper must pass §2 ratios with the 2px fringe present, which they do because text never sits on plates. The effect is decorative and unannounced.

**Tokens consumed.** `--reg` (2px), `--reg-funny` (3px), `--reg-breathe-max` (3.5px), `--ease-snap`, `--ease-press`, `--snap-in` (200ms), `--snap-out` (260ms), plus the plate colours of §2.


### 6.5 Four-colour registration progress bar

**What & why.** Reading progress is shown as the press's registration strip: a slim bar at the foot of the masthead (and repeated at the imprint) that fills in **four sequential plate passes** — process red fills its quarter of the bar, then teal, then mustard, then ink — each pass scrubbed to its quarter of the total scroll. It belongs here because it makes progress *manufacturing*: the page is finished being printed when the reader finishes reading it, and the last pass is always ink, the pass that makes it a page.

**Structure.** A `.regbar` track (height 6px, `--mustard-wash` ground — the unprinted strip) containing four segment fills, each 25% wide, in press order: `.pass-red`, `.pass-teal`, `.pass-mustard`, `.pass-ink`. Each segment's fill is a scaleX (or width) driven by the shared scroll loop: segment *n* fills across scroll fraction [(n−1)/4, n/4]. Fine registration ticks (1px ink, every 10% of the bar) are printed on the track as background — the strip is a ruler as well as a progress meter. Above the bar, at its right end, the apparatus line reads the current pass in words: "First pass · Red" → "Second pass · Teal" → "Third pass · Mustard" → "Final pass · Ink" → "Printed." — real state, set in the apparatus style (§3).

**Motion spec.** Fully scrubbed via the shared loop (lerp 0.12): each segment fills linearly within its quarter; at a quarter boundary the next segment begins the same frame — no gap, no overlap, the passes are contiguous like press runs. The apparatus label crossfades (120ms) at each boundary. No easing on the fills themselves — progress is a measurement, and measurements do not ease.

**States.** Passes 1–4 in progress → complete ("Printed."). At scroll 0 the bar is empty track. Scrolling back up un-fills in reverse press order (ink drains first) — unlike §6.1's ratchet, the registration strip honestly reports position both ways, because it is an instrument, not an achievement.

**Content-merge.** The bar is the supplement's own registration strip, printed in its own four inks in their working order, sitting where a printer's strip sits: at the edge of the sheet. It measures the page it is printed on.

**Failure fallback.** Without JS the bar renders as the empty printed track with its ticks and the label "The Sunday Supplement" — a decorative rule, no false progress claimed. The bar is never the only way to know where you are: section apparatus (§6.13) carries folio numbers independently.

**Reduced-motion variant.** The bar still fills (it is scroll position, not animation), but the lerp is removed — fill maps 1:1 to scroll with no smoothing lag, and label changes are instant, no crossfade.

**Performance budget & mobile variant.** Four scaleX writes per frame maximum, transform-only. Mobile: bar height 5px, label shortens to "Pass 2 · Teal" form, ticks every 12.5% (eight ticks) to stay legible at small width.

**Choreography timeline** (spatial — scrubbed to total page scroll):

| Beat | Scroll fraction | What happens |
|---|---|---|
| 1 | 0.00–0.25 | Red segment fills 0→100%; label "First pass · Red" |
| 2 | 0.25 | Red complete; teal begins same frame; label crossfades (120ms) to "Second pass · Teal" |
| 3 | 0.50 | Teal complete; mustard begins; label "Third pass · Mustard" |
| 4 | 0.75 | Mustard complete; ink begins; label "Final pass · Ink" |
| 5 | 1.00 | Ink complete; label settles on "Printed." and the bar's end tick thickens to 2.5px — the sheet is off the press |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (top) | Empty track, ticks visible, label "First pass · Red" at 0% | Same |
| Scrolling | Segments fill per quarter, lerped | Same, label in short form |
| Hover | Bar thickens 6→9px and each completed pass's boundary shows its plate name in a caption balloon (§6.10 grammar) | n/a |
| Focus | Bar is not focusable (it is an instrument, not a control) | n/a |
| Scrolled-past (bottom) | "Printed." state | Same |
| Disabled / no-JS | Empty printed track + paper name label | Same |

**Breakpoint behaviour.** ≥1200px: full spec with word labels. 768–1199px: labels shorten ("Pass 3 · Mustard"). <768px: height 5px, ticks ×8, label "Pass n" only, plate name moves into the bar's `aria-label` and the masthead apparatus line.

**Edge cases.** *Very short page (<150vh total):* quarters compress but the four-pass order holds; below 120vh of scrollable length the bar is omitted entirely — a single-sheet page needs no progress instrument, and a bar that fills in one flick is noise. *Dynamic content loading (listing pages):* total scroll is recomputed on resize/content change; the bar may jump — acceptable for an instrument, and it animates the correction over 200ms `press` rather than snapping. *Anchor jumps:* the lerp catches up within ~400ms; the bar never eases for longer than the loop's natural lag. *Multiple bars (masthead + imprint):* both are driven by the same loop values — two strips, one press.

**Accessibility spec.** `role="progressbar"` with `aria-valuenow` as a percentage and `aria-valuetext` in press language ("Second pass, teal — halfway printed"). Updates are throttled: `aria-valuenow` writes at most every 250ms and only on whole-percent change, so screen readers are not flooded by the scrub. The bar is not focusable and conveys nothing the folio apparatus doesn't also convey. Contrast: each filled segment against the track passes 3:1 non-text contrast at its quarter (red 3.9:1 vs the wash track, teal 4.7:1, mustard 1.9:1 — mustard's segment is therefore always flanked by its ink boundary ticks, and its pass is *also* announced by the label text, never by colour alone; ink 11:1).

**Tokens consumed.** `--red`, `--teal`, `--mustard`, `--ink`, `--mustard-wash`, `--regbar-h` (6px), `--loop-lerp` (0.12), `--label-fade` (120ms).

### 6.6 Masthead bounce-settle

**What & why.** On load, the masthead's "Sunday" — the nameplate's flourished word — swells once with a hand-lettered bounce-settle: scale 1.12 → 1 with the `settle` overshoot, 600ms, then rests forever. It belongs here because a Sunday paper announces itself once, at the doorstep, and then is simply the paper. The flourish lives in the lettering of the paper's own name — it is the one moment of showmanship the theme permits itself, spent entirely on the word "Sunday".

**Structure.** The masthead is a panel (border per §4) containing the nameplate line: "Sunday" as a `<span class="masthead-word">` in Playfair 900, the rest of the paper's name in Playfair 700 on the same baseline, flanked by apparatus lines (date, issue number, price line — real data). The animated span has `transform-origin` at its baseline centre-left (the point a letterer's brush would anchor). The rest of the masthead never moves.

**Motion spec.** Trigger: first load, once, after fonts are ready (`document.fonts.ready`, so the flourish is never performed in a fallback face). Scale 1.12 → 1, **600ms `settle`**, with the overshoot dipping to 0.995 at ~70% before resting — the letterform presses into the paper. A flat `--plate-shadow` under the word grows 0→4px in the first 200ms and holds, as if the nameplate were a plate laid on the sheet. Subsequent page views in the same session: no repeat (sessionStorage flag) — the paper does not re-announce itself to a reader already holding it.

**States.** Pre-load (static, full size — the no-JS state) → flourishing (600ms, once) → rested (permanent). No hover, no replay control. If the tab is backgrounded during the flourish, it completes silently or not at all; the rested state is identical either way.

**Content-merge.** The animation is performed by the paper's own name, in its own lettering, inside its own panel. There is no logo animation bolted on; the nameplate *is* the brand mark and the motion.

**Failure fallback.** The rested state is the DOM default. JS adds the pre-flourish scale only at the moment it can also animate it back. Font failure: if Playfair fails to load, the flourish is skipped (a bounce in a fallback serif looks like a different, cheaper paper).

**Reduced-motion variant.** No flourish. The nameplate is simply present — which, in this theme, is the dignified default anyway.

**Performance budget & mobile variant.** One transform on one span — free. Mobile: swell reduces to 1.07 → 1 over 480ms (a 52px nameplate cannot throw 12% without crowding its panel), shadow plate to 3px.

**Choreography timeline** (t₀ = fonts ready + first paint):

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | "Sunday" at scale 1.12, shadow plate at 0 |
| 2 | t₀ + 200ms | Scale ≈ 1.05; shadow plate reaches 4px and holds |
| 3 | t₀ + 420ms | Scale crosses 1.0 into the 0.995 press-in |
| 4 | t₀ + 600ms | Scale rests at exactly 1; transform removed from the span (clean final state); session flag written |
| 5 | t₀ + 600ms → | The registration bar (§6.5) is live; the masthead is furniture from here on |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (pre/post) | Nameplate static at full size | Same |
| Flourishing | 600ms `settle` swell, once per session | 480ms, 1.07 amplitude |
| Hover | Nothing — the nameplate is not a toy; if it is a home link, §6.13 nav hover applies to its link state only | n/a |
| Focus (if home link) | Theme focus ring on the masthead panel; no flourish replay | Same |
| Scrolled-past | The masthead unpins after the strip (§6.7) and scrolls away like any panel | Same |
| Disabled / no-JS | Static nameplate | Same |

**Breakpoint behaviour.** ≥1200px: 84px nameplate, 1.12 swell. 768–1199px: nameplate 64px, swell 1.09. <768px: 52px, swell 1.07, apparatus lines stack under the nameplate (date left, issue right, price line dropped — a small paper carries less furniture).

**Edge cases.** *Return visit within session:* no flourish (flag). *New session:* the flourish performs again — a new Sunday, a new paper; that is the point of the session boundary. *Slow font load:* flourish waits for `fonts.ready` up to 800ms, then performs in whatever face arrived or not at all; it never performs half in one face and half in another (the span swaps atomically with the font). *Masthead is the home link:* the flourish span is inside the link; the animation never changes the link's hit area (transform-origin anchored, layout size constant — scale is visual only, and the panel clips nothing).

**Accessibility spec.** The flourish is decorative and unannounced; the nameplate's accessible name is the paper's name as plain text regardless of the span split (use `aria-label` on the link/heading with the full name, spans `aria-hidden` if split for styling). No information is conveyed by the motion. Under reduced motion it does not run. The nameplate meets contrast at 13.1:1 (ink on paper) at all sizes.

**Tokens consumed.** `--ink`, `--paper`, `--plate-shadow`, `--ease-settle`, `--flourish` (600ms), `--flourish-scale` (1.12), `--masthead-size` (84px).


### 6.7 Pinned masthead, scrolling strip

**What & why.** The masthead panel pins at the top of the viewport for the length of the first comic strip (~150vh of scroll) while the strip's panels scroll beneath it in reading order, passing under the nameplate like the first page sliding under the folded front of the paper. It belongs here because it stages the supplement's founding relationship — the paper's name presiding over its first story — and because it gives the visitor one anchored orientation point during the longest single read on the page. After the strip ends, the masthead unpins and scrolls away with the page; the ceremony is for the opening only.

**Structure.** A `.strip-zone` wrapper of height = masthead height + 150vh of travel contains: the masthead panel as `position: sticky; top: 12px` (the preferred build — no JS pinning, no layout jank), and the strip: 3–5 panels in reading order flowing beneath, their top edges passing under the masthead's panel (z-order: masthead above, with its `--paper` ground fully opaque and its flat bottom shadow plate visible as panels slide under). The registration bar (§6.5) lives in the pinned masthead, so progress stays visible through the whole strip. Strip panels reveal per §6.2 as they emerge from beneath the masthead.

**Motion spec.** The pin is pure sticky positioning — no scrubbed transform on the masthead itself. The motion is the strip's: panels scroll at natural speed (no parallax inside the strip — the reading must be honest), and each panel's §6.2 reveal triggers as its top clears the masthead's bottom edge + 40px (not the viewport top — the masthead occludes the viewport top, and triggers must respect the real reading line). Pin length: exactly the strip's height, capped at 150vh of travel; a longer strip ends the pin at 150vh and the masthead releases mid-strip (the paper lets go rather than presides forever).

**States.** Approaching (masthead in normal flow) → pinned (strip passing beneath) → released (masthead scrolls away with the page, now ordinary furniture). The pinned masthead is fully live: its nav (§6.13) and registration bar work throughout.

**Content-merge.** The masthead is the supplement's cover and the strip is its first page; the pin is the physical fold between them. No artificial header is introduced — the pinned object is a real content panel doing double duty, which is why it may pin and a generic site header may not.

**Failure fallback.** Without sticky support or JS, the masthead is simply the first panel and the strip follows it — the page reads identically, minus the fold. Sticky is CSS-only; there is no JS pin to fail.

**Reduced-motion variant.** No pin. Masthead in flow, strip beneath it, all panels pre-printed. (Pinning is motion-adjacent — a fixed object against moving content — and reduced-motion readers get the flat broadsheet.)

**Performance budget & mobile variant.** Sticky compositing is free; the cost rule is occlusion: strip panels under the masthead must still be painted (they emerge mid-panel), so the strip's panels keep their §6.2 budget. Mobile: pin length shortens to 100vh of travel and the masthead compresses (apparatus lines drop per §6.6 mobile rule, nameplate 44px) so the pinned cover never occupies more than 22% of a phone viewport.

**Choreography timeline** (spatial, scrubbed by scroll):

| Beat | Scroll position | What happens |
|---|---|---|
| 1 | Masthead top reaches 12px from viewport top | Pin engages; masthead's flat bottom shadow plate fades in over 150ms (it now casts onto moving paper) |
| 2 | Strip panel 1 top clears masthead bottom + 40px | Panel 1's §6.2 reveal begins (border draw from its visible portion) |
| 3 | Each subsequent panel | Same reveal at the same reading line; registration bar filling throughout (pass 1 completes inside the strip on most pages) |
| 4 | Strip travel reaches 150vh (or strip ends) | Pin releases; shadow plate fades out 150ms; masthead scrolls away with the page |
| 5 | After release | Masthead never re-pins on the same page, in either scroll direction |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (above strip) | Masthead in flow | Same, compressed masthead |
| Pinned | Sticky at top 12px; nav + regbar live; strip scrolls beneath | Sticky; ≤22% viewport height; travel capped 100vh |
| Hover (on masthead) | Per §6.13 nav states; the pin itself has no hover | n/a |
| Focus | Focusable elements inside the pinned masthead stay reachable; focus scroll never fights the pin (browser scrolls the strip, masthead is sticky not fixed) | Same |
| Scrolled-past (released) | Ordinary panel in the scrollback | Same |
| Disabled / reduced motion | No pin; static order | Same |

**Breakpoint behaviour.** ≥1200px: travel 150vh, full masthead. 768–1199px: travel 130vh, nameplate 64px. <768px: travel 100vh, compressed masthead (44px nameplate, date + issue only), shadow plate 3px.

**Edge cases.** *Strip shorter than expected (2 panels):* pin travel shrinks to the strip's real height — never pad a strip to justify the pin; a short strip gets a short fold. *Strip taller than 150vh:* release at cap (beat 4) — the masthead exits mid-strip and the remaining panels reveal against the plain viewport top with triggers at 75% vh as usual. *Anchor link into the strip:* scroll-margin on strip panels accounts for the pinned masthead height + 12px so anchored panels land below the fold, not under it. *Keyboard user tabbing through the strip:* focus follows the DOM (masthead first, then strip) — a focused strip panel under the masthead is scrolled into the clear by the browser's scroll-into-view, which the sticky layout tolerates without a JS handler. *Resize mid-pin:* sticky recomputes natively; no state to repair.

**Accessibility spec.** Sticky (not fixed) keeps the browser's scroll and find-in-page behaviour honest. The masthead's content is in the DOM once, in reading position — no duplicated hidden header for the pinned state. Focus order: masthead controls, then strip panels, matching visual order while pinned. The occlusion is visual only; screen readers read straight through. Scroll margins (§edge cases) are also the keyboard-focus guarantee: a focused panel is never left hidden beneath the pinned masthead — `scroll-margin-top` equal to pinned height + 16px is mandatory on all strip panels.

**Tokens consumed.** `--paper`, `--ink`, `--plate-shadow`, `--pin-travel` (150vh), `--pin-top` (12px), `--masthead-h` (per breakpoint), `--shadow-in` (150ms).

### 6.8 Self-drawing balloon tails

**What & why.** Speech-balloon tails and panel border flourishes — the little line-work ornaments of the comic page: a tail pointing from a balloon to its speaker, a fleuron corner on a feature panel, the wavy rule under a joke — draw themselves in SVG as their panels arrive. It belongs here because line-work is the supplement's handwriting; watching the tail draw is watching the cartoonist's pen finish the panel. The tails belong to the balloons in the art — they are never floating decoration; every drawn line terminates at a real balloon, border, or caption.

**Structure.** Each flourish is an inline SVG path inside its panel, with `pathLength="100"` normalisation and a dash array applied by the reveal system. Balloons themselves are DOM elements (a bordered, paper-filled rounded rect — the one permitted radius in the theme, 50% ellipses for balloons only) containing real caption text; the tail is a two-segment path from the balloon's edge to its speaker/panel anchor point. Flourish corners are four short paths at a panel's corners, drawn after the main border (§6.2 beat 1) completes.

**Motion spec.** Trigger: the parent panel's §6.2 beat 2 (art fill) start. Duration: **300–450ms `press`**, scaled by path length class (short tail 300ms, long flourish 450ms), drawing from the balloon outward to the anchor — the pen starts at the words and finds the speaker, as a reader's eye does. Multiple flourishes in one panel stagger 60ms apart in reading order. Draws run once, on first print.

**States.** Undrawn (dash offset full — but see fallback: this state exists only as a JS-added class) → drawing → drawn (terminal). Hover: no redraw, ever — a tail that redraws on hover becomes a nervous tic (§9.5). The §6.10 caption pop may *re-point* a tail (that is a geometry change, §6.10, not a redraw).

**Content-merge.** The tail connects a real caption to the real panel element it comments on — a price, a face in the art, a headline. If a caption has nothing to point at, it gets no tail; the absence is the discipline.

**Failure fallback.** Paths render fully drawn by default; JS adds the dash state only when it can animate it. A flourish whose panel prints via the watchdog (§6.2) is set drawn instantly. No-JS: all line-work present.

**Reduced-motion variant.** All line-work pre-drawn. Balloons are static paper shapes with their tails attached — the finished comic page.

**Performance budget & mobile variant.** Stroke animations on small paths are cheap; cap: ≤ 6 drawing paths per viewport at once (panels print in stagger, so this is natural). Mobile: durations compress ×0.8; flourish corners are dropped below 768px (panel corners at phone width cannot spare the ornament — the tails, which carry meaning, are kept).

**Choreography timeline** (t₀ = parent panel's art-fill start):

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | First flourish begins drawing (balloon tail of the panel's primary caption) |
| 2 | t₀ + 60ms × n | Subsequent tails/flourishes begin, reading order |
| 3 | t₀ + 300–450ms | Each path completes at its own length class; dash removed, path rests as plain line-work |
| 4 | With §6.2 beat 3 | Caption lettering runs concurrently — words arrive as their tail finishes, binding text to pointer |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (undrawn) | Only as JS-added pre-print state | Same |
| Drawing | 300–450ms `press`, once | ×0.8 durations |
| Drawn | Terminal; plain SVG line-work | Same |
| Hover | No change | n/a |
| Focus (balloon is a button, §6.10) | Tail thickens 1.5→2.5px to show the connection is live | Same on focus-visible |
| Scrolled-past | Drawn | Drawn |
| Disabled / no-JS | Drawn by default | Same |

**Breakpoint behaviour.** ≥1200px: full spec including corner flourishes. 768–1199px: flourishes kept, stagger 50ms. <768px: tails only (no corner flourishes), durations ×0.8, tail stroke 1.5px (from 2px) to match smaller panels.

**Edge cases.** *Caption re-pointed by §6.10:* the tail path's `d` is recomputed to the new anchor and swapped instantly (no draw) — re-pointing is editing, not performing. *Balloon near panel edge:* tails clamp to a minimum length of 18px and a maximum bend; if the anchor is closer, the balloon carries no tail (the caption sits adjacent instead) — never draw a tail that crosses text. *Panel re-flowed by resize:* tails are SVG in the panel's own coordinate space (viewBox per panel), so they scale with the panel; below 768px the corner flourishes are removed from the DOM, not merely hidden. *Long panels with many captions:* the 6-path concurrency cap queues extra tails to draw with their own caption's lettering beat instead of the panel's first pass.

**Accessibility spec.** Tails and flourishes are `aria-hidden` decoration; the caption text they serve is ordinary DOM text with its reading order intact. A tail never carries meaning that the caption doesn't state in words (if a caption says "the miller, left," the tail is redundant confirmation, which is the correct relationship). Focus thickening (state matrix) is a supplement to, never a replacement for, the balloon's own focus ring.

**Tokens consumed.** `--ink`, `--ease-press`, `--draw-tail` (300ms), `--draw-flourish` (450ms), `--stagger-flourish` (60ms), `--tail-w` (2px).


### 6.9 Rescreening scale-in-frame

**What & why.** Images inside panels scale gently in-frame as they scroll through the viewport — 1.07 → 1.0 — and their halftone dot pitch *rescreens* as they settle, the dots re-spacing in step with the scale, so the picture arrives slightly large and slightly coarse and then is *set* into its frame at final size and final screen. It belongs here because scale and dot screen are one print property in this theme: a plate enlarged is a plate rescreened, and animating them together on the image itself keeps the mechanic honest — the visitor watches the picture being fitted to its panel the way a compositor fits a block to the page.

**Structure.** Each in-panel image is wrapped in its panel's frame element (`overflow:hidden`, ink border). The image carries the screened rendering (§6.1's plate technique at panel scale: standard pitch 10px coarse → 4px fine) and a transform scale driven by the shared scroll loop: scale maps the image's viewport transit (entering at 90% vh → centred) from 1.07 → 1.0; dot pitch maps the same transit 10px → 4px. One CSS variable `--settle` (0→1) per image drives both, written by the loop only while the image is within one viewport of travel.

**Motion spec.** Scrubbed, lerp 0.12 (shared loop). No trigger, no easing curve — the scroll is the timeline. The rescreen is implemented as an SVG filter scale or a background-size step on the dot pattern layer; pitch changes in 0.5px increments (quantised) so the screen never shimmers from sub-pixel dot swimming — the dots step like a press re-screening in passes, four to six visible steps across the transit.

**States.** Approaching (scale 1.07, pitch 10px) → settling (scrubbed) → set (scale 1.0, pitch 4px, terminal for that pass). Scrolling back up reverses the effect symmetrically (unlike §6.1's ratchet — in-panel images are many and small, and the set/unset breath as they pass is the strip's living texture; the hero alone earns permanence).

**Content-merge.** The scale happens inside the panel's own frame and the dots are the image's own screen. The frame never moves; the picture is fitted to it. Nothing outside the panel is affected.

**Failure fallback.** Images render at scale 1, fine pitch, by default in markup; the loop adds the unset state only for images below the fold that it will actually drive. No-JS: all images set. If the loop fails mid-page, a 1.2s watchdog per image forces `--settle: 1`.

**Reduced-motion variant.** All images set (scale 1, 4px pitch) at all times. No exceptions — a rescreening picture is exactly the kind of ambient motion reduced-motion exists to still.

**Performance budget & mobile variant.** The loop tracks only images within ±1 viewport; transform + pattern-size writes on those only. Cap: 6 actively settling images per frame budget. Mobile: scale range narrows to 1.04 → 1 and pitch 9px → 4.5px (smaller frames, smaller drama), quantisation steps of 0.75px.

**Choreography timeline** (spatial, per image):

| Beat | Image position | What happens |
|---|---|---|
| 1 | Frame top at 90% vh | `--settle` = 0: scale 1.07, pitch 10px |
| 2 | Frame top at 65% vh | `--settle` ≈ 0.4: scale ≈ 1.04, pitch ≈ 7.5px (two quantised steps passed) |
| 3 | Frame centre at 55% vh | `--settle` ≈ 0.75: scale ≈ 1.02, pitch ≈ 5.5px |
| 4 | Frame centre at 50% vh | `--settle` = 1: scale 1.0, pitch 4px; loop stops writing this image until it re-enters the transit band |
| 5 | Scrolling up | Symmetric reversal through the same beats |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (below band) | Unset state pre-applied by JS (1.07 / 10px) or set if JS off | 1.04 / 9px pre-applied |
| Settling | Scrubbed per frame | Scrubbed per frame |
| Set | Scale 1, pitch 4px | Scale 1, pitch 4.5px |
| Hover | §6.4 register snap governs the plate; scale holds wherever the scrub left it (hover never fights the loop) | n/a |
| Focus (if image is a link) | Settles instantly to 1 / 4px — a focused picture is a read picture | Same |
| Scrolled-past | Returns toward unset as it exits upward (symmetric) | Same |
| Disabled / no-JS | Set | Set |

**Breakpoint behaviour.** ≥1200px: full ranges. 768–1199px: scale 1.05→1, pitch 10→4px. <768px: scale 1.04→1, pitch 9→4.5px, active-image cap 4.

**Edge cases.** *Image taller than its frame (cropped plates):* scale origin is the frame's centre; the crop must be composed so the 1.07 state never reveals an unprinted edge — images are sized to the frame at scale 1.1 in the asset itself (10% bleed baked in), so the unset state crops *into* the bleed. *Tiny images (<120px):* exempt — below that size rescreening is invisible labour; they ship set. *Images inside the pinned strip:* the loop's band math uses viewport position, which sticky does not disturb; they settle normally as they emerge from under the masthead. *Layout shift:* the frame's aspect ratio is reserved in markup (`aspect-ratio` from the plate's real dimensions) — the settle never changes layout, only the picture inside the frame.

**Accessibility spec.** Decorative motion, unannounced; `alt` text unaffected. The scale never crops content the alt describes as essential — plates are decorative-contextual by theme law (§1: the theme is not for content where the photograph itself is the evidence). Focus forcing the set state (state matrix) guarantees a keyboard visitor never reads a deliberately blurred-by-coarseness image.

**Tokens consumed.** `--settle` (element-local), `--scale-unset` (1.07), `--dot-panel-coarse` (10px), `--dot-panel-fine` (4px), `--loop-lerp` (0.12), `--watchdog-img` (1.2s).

### 6.10 Caption-balloon click pop

**What & why.** Clicking a panel pops its caption balloon — the balloon scales 0.9 → 1.05 → 1 in 220ms on the `snap` ease, and its tail (§6.8) re-points to the panel just clicked. The balloon *speaks up*. It belongs here because the caption balloon is the supplement's voice — the lettered comment in the margin of the art — and clicking the art to hear its caption is the theme's native equivalent of a tooltip, except the tooltip was always printed on the page, waiting to be asked.

**Structure.** Each illustrated panel may carry one `.balloon`: an ellipse-bordered (the theme's only radius), paper-filled element positioned at a panel corner or margin, containing the caption text (Lora italic, §3) and an SVG tail path (§6.8) whose anchor end is recomputed on re-point. Balloons are `<button>`s when they carry an action (expand, credit, "read the strip"), and plain `<div>`s when they are pure caption — the pop serves both; only buttons are focusable/clickable, while pure captions pop when their *panel* is clicked.

**Motion spec.** Trigger: click/tap on the panel (for caption balloons) or on the balloon itself (for button balloons). Pop: scale 0.9 → 1.05 (110ms, `snap` rising) → 1.0 (110ms, `snap` settling), transform-origin at the tail's root so the balloon grows *from its pointer*. Tail re-point: the path `d` swaps instantly at pop start (no draw — §6.8's rule), with the tail's stroke thickening 2px → 2.5px for 300ms to show the new connection. A balloon may be popped once per click; re-clicking the same panel re-pops (the reader asked again).

**States.** Resting (printed, small, in its corner) → popping (220ms) → spoken (resting at full presence, tail pointing at the last-clicked panel — for shared balloons serving a strip) → resting. Only one balloon in a strip may be in the spoken state; popping another returns the first instantly (no reverse animation — the conversation moved on).

**Content-merge.** The balloon's words are the panel's own caption — credit, joke, explanation — typeset in the theme's caption voice (§12). The pop adds no new UI chrome; it amplifies an element already printed on the page.

**Failure fallback.** Balloons are fully visible and legible at rest without any pop; the pop is emphasis, not disclosure. No content is ever *only* available after a pop (that would be a tooltip trap and a §9 failure). No-JS: static balloons, tails drawn to their default anchors.

**Reduced-motion variant.** No scale. The tail re-points instantly and the balloon's border thickens 2.5px for 600ms — emphasis by line weight, the print-native way.

**Performance budget & mobile variant.** One transform on one small element — free. Mobile: balloons are sized ≥ 44px in their tap dimension when they are buttons; caption balloons on <768px sit *below* their panel's art instead of overlaying a corner (a phone panel has no spare corner), and the pop scale reduces to 0.94 → 1.03 → 1.

**Choreography timeline** (t₀ = click):

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Tail path swaps to the clicked panel's anchor; stroke thickens to 2.5px; previous spoken balloon (if any) resets instantly |
| 2 | t₀ + 110ms | Balloon at scale 1.05 (overshoot peak), origin at tail root |
| 3 | t₀ + 220ms | Balloon settles at 1.0; spoken state marked |
| 4 | t₀ + 300ms | Tail stroke relaxes to 2px; the connection is simply true now |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Balloon printed at corner, tail to default anchor | Balloon below art; tail to panel |
| Hover (button balloons) | Border thickens 2.5→3px; tail pre-thickens 2.5px — the balloon leans in | n/a |
| Focus | Theme focus ring; tail thickens; Space/Enter pops | Same |
| Active (pop) | 220ms scale pop + re-point | 220ms reduced-amplitude pop |
| Spoken | Tail anchored to last-clicked panel; border at rest weight | Same |
| Scrolled-past | Spoken state persists (the reader's conversation is not reset by scrolling) | Same |
| Disabled | A button balloon that is disabled loses its tail (an unanchored balloon) and its border greys to `--ink-60` | Same |

**Breakpoint behaviour.** ≥1200px: corner balloons, full pop. 768–1199px: corner balloons, pop 0.92→1.04→1. <768px: balloons below art, reduced pop, button balloons full-width of their panel's caption zone.

**Edge cases.** *Panel inside a §6.3 stage:* clicking the stage's panel pops its balloon; the stage's next/prev controls are separate targets — a click on a control never pops (event targets are distinct by build rule). *Balloon text longer than its ellipse:* balloons size to content up to 34ch; longer captions are edited, not shrunk — caption voice law (§12) caps balloons at 14 words, so overflow is a copy bug, caught at the quality gate. *Rapid clicking:* the pop restarts from current scale (no queue); tails re-point per click, last click wins. *Shared balloon across a strip:* default anchor is the strip's first panel; the spoken state survives strip wipes (§6.3) and re-points to the wiped-to panel automatically.

**Accessibility spec.** Button balloons are real `<button>`s with descriptive labels ("About this picture: the miller's joke — show caption emphasis" is wrong; the label is the caption's own first words plus the panel name). Pure-caption balloons are text, always readable, never interactive, never `aria-hidden`. The pop is decorative emphasis and is not announced; the re-point is visual only. Focus-visible state is the border + ring, never the pop alone. Touch targets ≥ 44px for button balloons at all breakpoints.

**Tokens consumed.** `--paper`, `--ink`, `--ink-60`, `--ease-snap`, `--pop` (220ms), `--pop-scale` (0.9→1.05→1), `--tail-w` (2px), `--tail-w-live` (2.5px).


### 6.11 Living-print shimmer

**What & why.** The halftone dot screens across the page's imagery shimmer very faintly — dot opacity breathing ±4% on a slow 5s loop, each image offset from its neighbours — over a barely-there cream-grain drift in the paper ground. The print is *alive but restrained*: the page feels freshly inked, still settling, rather than laminated. It belongs here because stillness is this theme's luxury and total stillness is death; the shimmer is the smallest possible motion that keeps the supplement a physical object instead of a screenshot of one. Its restraint is the spec: a visitor should feel it before they can see it, and should have to look twice to confirm it moves at all.

**Structure.** The dot layer of each screened image (§6.1/§6.9 plates) gets a CSS animation on opacity only, driven by a per-image `--shimmer-phase` (set inline as `animation-delay` from a hash of the image's index, so phases never sync). The grain drift is a single fixed, pointer-events-none overlay of the paper texture (SVG feTurbulence noise at 3% opacity) translating 0→14px over 26s, alternate-direction. Both layers are enhancement-only: the DOM's base state has dots at full opacity and no overlay.

**Motion spec.** Dots: opacity 0.96 → 1.0 → 0.96, **5s ease-in-out infinite**, phase-offset per image across a 5s spread. Grain: 26s linear alternate drift, 14px range, opacity constant 3%. Both pause when off-screen (IntersectionObserver toggling `animation-play-state`) and when the tab is hidden (native behaviour). The shimmer never applies to: text, borders, plates under 120px, the hero during its resolve (the resolve owns the hero's dots until `--resolve` = 1, then shimmer fades in over 1s), or any image currently being hovered (the register snap's stillness is the point of hover).

**States.** Resting (base state, also the no-JS state) → shimmering (in viewport, page visible, motion allowed) → paused (off-screen / hovered / hero resolving) → resting. There is no user control; the shimmer is weather, not a feature.

**Content-merge.** The shimmer lives *in* the dot screens of the images themselves and in the paper's own grain. Remove it and every picture and page remains, complete — it is the theme's pulse, not its content.

**Failure fallback.** Base state is the finished page. If animations are unsupported or the overlay fails, nothing is missing. The overlay is created by CSS only (a `body::after` with the noise background) so a JS failure cannot even remove the grain's *possibility* — and its absence is equally invisible.

**Reduced-motion variant.** None. No shimmer, no drift — a still printed page. This element has the strictest reduced-motion ruling in the theme because it is the only purely ambient one.

**Performance budget & mobile variant.** Opacity-only animations on composited layers; the grain overlay is one fixed layer repainted on transform only. Hard cap: shimmer applies to at most 8 images per page (the 8 nearest the reading position, rotated by the observer) — a page of 40 screened images shimmering at once is a screensaver, not a supplement. Mobile: grain drift disabled (a phone's paper doesn't need to crawl), dot shimmer kept at ±3% on the 4 nearest images.

**Choreography timeline** (continuous loop; t₀ = image enters viewport):

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Shimmer starts at the image's phase point (never all images at phase 0 together) |
| 2 | t₀ + 2.5s | First opacity peak/trough completes (±4%) |
| 3 | Continuous | 5s cycle repeats; grain drifts independently at 26s |
| 4 | Image exits viewport | Animation pauses at its current value; resumes on re-entry — no phase reset |
| 5 | Hero only | Shimmer held at 0 until `--resolve` = 1, then fades in across 1s |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Dots at full opacity (base) | Same |
| Shimmering | ±4%, 5s loop, phase-offset | ±3%, 4 nearest images |
| Hover (on the image) | Shimmer pauses — the snapped print holds still | n/a |
| Focus (image is a link) | Shimmer pauses while focused | Same |
| Scrolled-past | Paused off-screen | Paused |
| Disabled / no-JS | Resting — fully printed page | Same |
| Reduced motion | Never runs | Never runs |

**Breakpoint behaviour.** ≥1200px: 8-image cap, ±4%. 768–1199px: 6-image cap, ±4%, grain drift on. <768px: 4-image cap, ±3%, grain drift off.

**Edge cases.** *Photosensitivity:* ±4% opacity at 0.2Hz is far below any flash threshold (no luminance alternation near 3 flashes/second, no high-contrast strobing) — the spec's slowness is a safety property, not just taste; do not " enliven" it. *Battery saver / low-power:* `navigator.getBattery` is not consulted (unreliable); instead the loop honours the observer caps strictly and the grain is the first thing cut by the §14 performance ladder. *Many images entering at once (fast scroll):* phases are index-hashed, so a wall of panels arriving together still never pulses in sync. *Print:* animations do not print; dots print at full opacity.

**Accessibility spec.** Purely decorative; `aria-hidden` where the layers are separate elements, and the grain overlay is a CSS pseudo-element (invisible to AT). No information, state, or affordance rides on the shimmer. It is fully disabled under `prefers-reduced-motion` and paused for focused/hovered content so it never competes with reading.

**Tokens consumed.** `--shimmer-amp` (4%), `--shimmer-cycle` (5s), `--grain-opacity` (3%), `--grain-drift` (26s), `--shimmer-cap` (8).

### 6.12 Coarse-dot skeleton + page-turn transition

**What & why.** The theme's two state-change rituals, sharing one material logic. **Loading** shows coarse halftone skeleton blocks — panels with their borders drawn and their interiors filled with a coarse dot plate (14px) and caption bars as unlettered rules — which resolve into real content as it arrives: the page is *on the press*, mid-printing. **Navigation** is a comics page-turn: a hard wipe across the viewport with a visible paper edge — a flat ink rule fronting a `--plate-shadow` plate — 350ms, after which the new page stands printed. Both belong here because they are the supplement's own substances (dots and paper) doing the two jobs every site must do; a spinner or a fade would be foreign objects.

**Structure.** Skeleton: the real panel markup rendered server-side (or by the app shell) with `.is-loading` — borders real, image areas as dot-plate divs with the panel's aspect ratio, text areas as 60%-width `--ink-60` rules at caption height. Content swap replaces the plate children in place; the panel itself never moves or resizes. Page-turn: a fixed full-viewport `.page-edge` element (paper-coloured, leading ink rule 3px, trailing shadow plate 28px) parked off-canvas at the reading-start side; on navigation it sweeps across (`transform: translateX`), the route swaps at the sweep's midpoint coverage, and the edge exits the far side.

**Motion spec.** Skeleton resolve: as each panel's content lands, its dot plate crossfades to the real art over 240ms `press` while its pitch tightens 14px → the panel's resting screen — a miniature of §6.1. Hard cap: any panel still loading at **1.2s** has its screen stripped entirely (plate becomes plain `--paper-deep`) — the standing rule that no picture may stay abstract if the machinery fails; the panel then receives content plainly when it comes. Page-turn: **350ms `turn`** total — 175ms cover, swap at full coverage, 175ms reveal. The incoming page arrives *printed* (its panels do not re-run §6.2 reveals after a turn; a turned page is a finished page — reveals are for first manufacture only).

**States.** Skeleton: loading → resolving (240ms) → loaded; loading → stripped (1.2s watchdog) → loaded-plain. Page-turn: idle → covering → covered (route swap, scroll to top of new page) → revealing → idle. Browser back/forward: no turn (the browser's own history gesture rules; the theme does not intercept it).

**Content-merge.** The skeleton is the panel's own unfilled self, same borders, same geometry — layout shift is zero by construction. The page-turn's edge is the sheet of the page being left, sweeping over to become the sheet of the page arrived at.

**Failure fallback.** Skeleton without JS: the shell must not render `.is-loading` states it cannot resolve — server-rendered pages ship loaded; skeletons exist only inside client-side fetches that own their watchdog. Page-turn without JS or in a plain multi-page build: ordinary navigation, no sweep; the turn decorates links it can intercept and never breaks one it can't (it enhances `<a>` clicks, it does not replace href behaviour — middle-click, new-tab, and modified clicks bypass it entirely).

**Reduced-motion variant.** Skeleton: plates are plain `--paper-deep` blocks (no dots, no resolve animation — content fades in at 120ms opacity or appears). Page-turn: no sweep; instant navigation with a 120ms ink-outline flash on the masthead to mark the change of sheet.

**Performance budget & mobile variant.** Skeleton plates are CSS patterns — no image payload. The page-turn is one transform on one fixed element. Mobile: turn shortens to 300ms and the shadow plate narrows to 18px; skeleton caption rules reduce to two per panel.

**Choreography timeline** (page-turn, t₀ = link activation):

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Edge enters from reading-start side; ink rule leading |
| 2 | t₀ + 175ms | Full coverage; route swaps underneath; new page at scroll top, printed |
| 3 | t₀ + 350ms | Edge exits far side; new page fully revealed; focus moves to the new page's masthead heading (see a11y) |
| 4 | t₀ + 430ms | Watchdog: any turn not completed is torn down and the destination shown plainly |

Skeleton resolve (per panel, t₀ = content landed): plate pitch 14px → resting over 240ms with the art fading in beneath; caption rules replaced by lettered caption (§6.2 beat 3 runs in miniature, 45ms/word).

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Loading (skeleton) | Dotted plates inside real borders | Same, fewer caption rules |
| Resolving | 240ms pitch-tighten + fade | Same |
| Loaded | Normal panel behaviour | Same |
| Turning | 350ms sweep, pointer locked out | 300ms sweep |
| Hover | Links show §11 link hover; the turn itself has no hover state | n/a |
| Focus | Keyboard activation of a link fires the same turn; focus lands on destination masthead at beat 3 | Same |
| Disabled / no-JS | No skeletons rendered unresolved; plain navigation | Same |

**Breakpoint behaviour.** ≥1200px: full spec. 768–1199px: turn 330ms, shadow plate 22px. <768px: turn 300ms, plate 18px, skeleton rules ×2.

**Edge cases.** *Navigation to a slow page:* the edge holds at full coverage with the registration bar's first pass pulsing on the edge itself (the press is working) — up to 3s, after which the turn aborts, the edge retreats (200ms), and the browser's native load proceeds; the theme never traps a visitor inside a transition. *Same-page anchor links:* no turn — anchors scroll (§6.3 grammar does not apply either; a plain smooth-or-instant jump per reduced-motion). *External links:* no turn. *Content that never arrives (fetch error):* the skeleton panel resolves into the theme's error panel (§11 alerts) with its caption in the error voice (§12) — a panel apologises in character rather than spinning forever. *Prefetch:* hovered internal links may prefetch; the turn then runs its full 350ms anyway — the ritual is the point, not the wait.

**Accessibility spec.** During a turn, the outgoing page is `inert` from beat 1 and the destination is made live at beat 3 with focus moved to its `<h1>` (tabindex=-1) and a polite announcement "Turned to: [page name]" — SPA navigation focus law, executed in the theme's grammar. Skeletons: loading panels carry `aria-busy="true"` until resolved; the strip region announces "This issue is still printing" once, not per panel. The turn is skipped entirely for reduced-motion and for screen-reader-driven navigation where focus is already managed by the router.

**Tokens consumed.** `--ink`, `--ink-60`, `--paper-deep`, `--plate-shadow`, `--ease-turn`, `--ease-press`, `--turn-page` (350ms), `--resolve-skeleton` (240ms), `--fallback-strip` (1.2s), `--edge-plate-w` (28px).


### Page-family elements

### 6.13 Masthead navigation (the contents rail)

**What & why.** Navigation in this theme is the supplement's own contents line: a rail inside (or directly beneath) the masthead panel listing the issue's sections as a printed contents column — section name in Lora 500, its folio (page anchor) in apparatus numerals, joined by a dotted leader rule, exactly as a contents page joins title to page number. It belongs here because a supplement is not navigated by a hamburger; it is *consulted* like a contents page, and the leader dots are the oldest wayfinding line in print.

**Structure.** A `<nav class="contents">` inside the masthead panel: a horizontal rail on desktop (sections in reading order, leader dots filling the gaps between name and folio), collapsing to a two-column contents list inside a toggled "Contents" panel on mobile. Each item: `<a>` with `.sec-name`, `.leader` (a dotted bottom border on a flexible span), `.folio` (Playfair lining numeral). The current section's item is printed in the section's plate colour with its leader dots in ink at full weight — currentness is shown by ink, never by a pill or a filled chip.

**Motion spec.** Hover: the item's leader dots draw in from the name toward the folio (background-position sweep, 180ms `press`) and the folio numeral snaps its plate into register (§6.4 grammar at item scale). Current-section tracking: as the visitor scrolls, the contents item for the section in view gains its plate colour over 200ms — a scrollspy printed as ink change, not a sliding indicator. The mobile contents panel opens with the §6.3 hard wipe (300ms) downward — the sheet pulls down; it never fades or springs.

**States.** Items: rest (ink, dotted leader at 40% ink) → hover/focus (leader draws, folio registers) → current (plate colour, full leader). The nav as a whole inherits the masthead's states: in flow, pinned (§6.7 — fully live while pinned), released.

**Content-merge.** The items are the page's real sections with their real folio positions (anchor order = reading order). The contents rail is generated from the page's actual panel headings — if a section is added, the contents gains a line, because it *is* the page's table of contents, not a marketing menu.

**Failure fallback.** Plain anchor list in the masthead; leader dots are CSS borders and survive without JS; scrollspy is the only JS behaviour and its absence leaves all items at rest weight with the first marked current by the server where known.

**Reduced-motion variant.** No leader draw (dots appear at full), no wipe for the mobile panel (instant open), scrollspy colour changes instant.

**Performance budget & mobile variant.** Scrollspy runs on the shared IntersectionObserver — free. Mobile: the rail becomes the Contents toggle + wiped panel; the toggle is a full apparatus-style button ("Contents — this issue") with a 44px target; folio numbers remain visible in the panel (a phone contents page still lists pages).

**Choreography timeline** (hover, t₀ = pointer enter an item):

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Leader sweep begins at the section name |
| 2 | t₀ + 180ms | Leader fully drawn to the folio; folio plate registered (2px → 0) |
| 3 | Pointer leave | Leader relaxes to 40% dots over 240ms; folio drifts back off-register |

Scrollspy change: outgoing item's colour drains to ink over 200ms as the incoming item inks into its plate colour — the two overlap for one beat, like passes on the press.

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Ink items, 40% leaders | Behind the Contents toggle |
| Hover | Leader draws, folio registers | n/a |
| Focus | Same as hover (keyboard gets the full treatment) | Same |
| Active / current | Plate colour, full-weight leader | Marked in the contents panel |
| Scrolled-past | Masthead released; nav scrolls away with it — no separate sticky nav ever appears | Same |
| Disabled | A section with no content is absent from the contents — never a greyed item | Same |

**Breakpoint behaviour.** ≥1200px: horizontal rail inside masthead, leaders flexible. 768–1199px: rail wraps to two rows, leaders shorten (min 24px) — if a row cannot fit name + 24px leader + folio, it wraps rather than squeezing dots below legibility. <768px: Contents toggle + wipe panel, two-column list inside, leaders full-width per row.

**Edge cases.** *More sections than the rail holds (>7):* the rail shows the first-level sections only; sub-sections live in the strip panels' own apparatus lines. A contents line with 15 items is a directory, not a supplement. *Very long section names:* names truncate with an ellipsis at 22ch on the rail but are full in the mobile panel and in `aria-label`. *Single-section page:* the contents rail is omitted — a one-story issue has no contents page. *Pinned + anchor click:* anchors carry the §6.7 scroll-margin so targets land below the pinned masthead.

**Accessibility spec.** A real `<nav>` with `aria-label="Contents of this issue"`; current item carries `aria-current="true"` (updated by the scrollspy, throttled to section changes only). Leader dots are CSS, invisible to AT. Focus order = reading order. The mobile toggle is a `<button aria-expanded>` controlling the panel; Esc closes it and returns focus to the toggle. All items are links with ≥24px height on desktop and ≥44px rows on mobile.

**Tokens consumed.** `--ink`, `--ink-60`, the four plate tokens, `--ease-press`, `--leader-draw` (180ms), `--spy-fade` (200ms), `--wipe-panel` (300ms).

### 6.14 Feature panel cards (the plate card)

**What & why.** The card in this theme is a small panel that behaves like a plate clipped from the supplement: ink border, one plate colour, a screened thumbnail fitted per §6.9, a Lora 600 title, a caption-voice standfirst, and an apparatus footer line (date, reading time as "a two-minute strip", plate number). Cards are the listing and related-content unit — "more from this issue" — and they belong in panel form because in this world there are no floating cards; there are only smaller panels, printed by the same press at a smaller size.

**Structure.** `<article class="plate-card">`: figure (screened image, §6.9 settle behaviour), plate layer (the card's one colour, offset per §6.4), body (kicker in apparatus style, title, standfirst max 2 lines), footer apparatus row. The whole card is one link (stretched-link pattern over the title) except when it carries a second action (a balloon button, §6.10), in which case the card is a group with two explicit targets.

**Motion spec.** Entry: §6.2 panel reveal at card scale (border 380ms, caption rules apply to the standfirst's fade). Hover: the corner-lift — bottom-right corner rises 6px, flat `--plate-shadow` grows 4px → 7px offset, 180ms `snap` in / 240ms `press` out — plus the plate's register snap (§6.4, the card's thumbnail corrects itself) and the thumbnail's shimmer pausing (§6.11). The lift is a *corner*, pivoting from the top-left: paper lifts from the corner a reader would thumb.

**States.** Rest → printing (entry) → printed → hover (lifted, registered, still) → focus (same as hover, plus ring) → active (corner presses back down 2px, shadow 5px — the thumb presses the page flat to turn it). Scrolled-past: printed, shimmer paused.

**Content-merge.** Every part of the card is the content it lists: its picture (screened), its title, its caption. The lift and snap act on the card's own paper and plate. A card for content with no image uses a fleuron plate (a printed ornament block in its colour) — the grammar holds without inventing imagery.

**Failure fallback.** Static bordered card, image at final screen, plate registered — the no-JS card is the finished card. The lift and snap are JS/CSS enhancements on a complete object.

**Reduced-motion variant.** No lift, no snap: hover/focus changes the border weight 2.5px → 3.5px and the kicker inks into the plate colour. Entry is instant-printed.

**Performance budget & mobile variant.** Cards inherit §6.9's loop caps (settling images) and §6.11's shimmer caps. Mobile: no hover lift — a card at viewport centre gets the register snap (per §6.4 mobile rule) and that is its whole performance; tap goes straight through (no first-tap tax).

**Choreography timeline** (hover, t₀ = pointer enter):

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Corner lift begins (`snap`); shadow plate starts growing |
| 2 | t₀ + 120ms | Plate register at ~0.5px, correcting |
| 3 | t₀ + 180ms | Lift complete (6px, shadow 7px); register at 0; shimmer paused |
| 4 | Pointer leave | 240ms `press` return: corner settles, plate drifts back to 2px, shimmer resumes |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Flat, 2px misregistered thumbnail | Flat |
| Hover | Corner lift + snap + still shimmer | n/a |
| Focus | Lift + snap + focus ring on the title link | Same (external keyboard) |
| Active | Corner pressed to 2px lift, shadow 5px | Tap: straight to navigation (§6.12 turn) |
| Scrolled-past | Printed, shimmer paused off-screen | Same |
| Disabled | A card for unavailable content is not rendered as a card — it becomes an apparatus note in the listing ("This plate is at the binder's") | Same |

**Breakpoint behaviour.** ≥1200px: cards in mixed spans per §4 (never a uniform grid of 12 identical cards — vary span or plate colour rhythm). 768–1199px: two-up, lift 5px. <768px: one-up stacked, no lift, centre-snap only, standfirst allowed 3 lines (narrow measure).

**Edge cases.** *Missing image:* fleuron plate (see content-merge) — never a grey box, never a stock photo substituted silently. *Very long title:* clamps at 2 lines with ellipsis; the full title lives in the link's accessible name. *Card inside the pinned strip:* entry reveals respect the §6.7 reading line. *A whole grid entering at once (listing page):* §5's three-panel concurrency cap applies — the rest appear printed.

**Accessibility spec.** One link per card (title), with the card's full title as its name; the thumbnail is decorative (`alt=""`) when the title names the content, or carries real alt when the image is the content (illustration portfolios) — choose per build, consistently. Focus ring: 2px ink outline offset 3px plus the lift, so focus is visible even in the lifted state. The apparatus footer is real text, readable by AT in order. Colour: kicker in plate colour must meet §2's text rules (teal/red only, never mustard on paper).

**Tokens consumed.** `--ink`, `--paper`, `--plate-shadow`, plate tokens, `--ease-snap`, `--ease-press`, `--lift` (6px), `--lift-in` (180ms), `--lift-out` (240ms).

### 6.15 The subscription coupon (conversion form)

**What & why.** Every 1930s supplement carried a coupon: a dashed-border form at the foot of a page that the reader clipped and posted. The theme's conversion form is that coupon — a panel with a **scissors rule** (a dashed ink border with a small scissors fleuron at its corner), fields set as ruled lines to write on, and a submit button printed as a rubber stamp. It belongs here because conversion in a print world is not a funnel; it is an act of reader commitment performed with scissors and a pen, and the form's honesty (name, address, one checkbox, one stamp) is the theme's answer to dark-pattern checkout.

**Structure.** `<form class="coupon">` inside its panel: dashed 2px ink border (`border: 2px dashed`), scissors fleuron (SVG, drawn per §6.8 on entry), a coupon headline in Playfair ("Take the Supplement every Sunday"), fields as bottom-ruled inputs (transparent ground, 2px ink bottom rule, Lora 17px input text, apparatus-style labels above), one consent checkbox drawn as an empty panel square that fills with its plate colour and an ink tick when checked, and the submit as a `.stamp-button`: ink-bordered, uppercase apparatus text, which on press performs the stamp (§6.10's pop grammar at form scale — scale 1 → 0.94 → 1 with the flat shadow shifting, 160ms).

**Motion spec.** Entry: the coupon panel prints per §6.2, then the scissors fleuron draws (300ms) last — the coupon is finished when it can be clipped. Field focus: the field's bottom rule thickens 2px → 3px and a plate-colour plate slides in beneath the rule from the left (200ms `press`) — the line you are writing on is underlined by the press. Error: the field's rule turns `--red`, the field ground washes `--red-wash`, and the error caption letters in beneath (§6.2 caption grammar, 45ms/word) in the error voice (§12). Submit press: stamp animation 160ms `snap`; on success the whole coupon is *franked*: a "Posted · Thank you" stamp (rotated −6°, in teal, apparatus style) fades/scales in over the panel corner (300ms `snap`) and the form is replaced by its confirmation caption.

**States.** Fields: empty → focused (rule + plate) → filled (rule stays 2.5px, a small ink tick appears at the rule's right end — the pen has been here) → error (red rule, wash, lettered message) → corrected (error clears on input, rule returns to ink over 200ms). Form: idle → submitting (stamp pressed, fields inert, the coupon's border dashes march 8px over 600ms — the coupon is moving through the post) → franked (success) or returned (error summary at top, in caption voice, focus moved to it).

**Content-merge.** The form's print furniture is its function: the dashed border is the clipping line, the ruled fields are the writing lines, the stamp is the submission. Nothing is decorative; remove the theme and the form is still legible as a form — that is the test.

**Failure fallback.** A plain, fully working form with solid borders if CSS/JS is limited; validation is server-truth — the lettered error captions are renderings of real validation results, never client-only theatre. No-JS: standard form post, errors returned as printed captions in the re-rendered page.

**Reduced-motion variant.** No dash marching, no stamp scale (the stamp's shadow shifts instead), error captions appear whole. Focus plate slide becomes an instant underline colour change.

**Performance budget & mobile variant.** Negligible motion cost. Mobile: fields full-width, input font-size 17px (also prevents iOS zoom), the stamp button is full-width of the coupon and ≥ 52px tall, scissors fleuron moves to the top-right corner clear of the headline.

**Choreography timeline** (submit, t₀ = press):

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Stamp presses (scale 0.94, shadow collapses to 1px) |
| 2 | t₀ + 160ms | Stamp releases; fields go inert; dashes begin marching if the request is pending |
| 3 | Response lands | Success: frank stamp lands at the panel corner (300ms `snap`, −6°); confirmation caption letters in |
| 3′ | Response lands (error) | Error summary prints at the coupon head; focus moves to it; first field error letters in beneath its rule |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest (field) | Ruled line, apparatus label | Same, 17px input text |
| Hover (field) | Rule warms to full ink (from 85%) | n/a |
| Focus | Rule 3px + plate slide beneath (200ms) | Same; the on-screen keyboard never shifts the coupon's panel (it scrolls the page, border intact) |
| Filled | Rule 2.5px + end tick | Same |
| Error | Red rule, red wash, lettered caption | Same |
| Disabled (submitting) | Fields inert at 70% ink density; dashes marching | Same |
| Success | Franked stamp + confirmation caption; form inert | Same |

**Breakpoint behaviour.** ≥1200px: coupon panel spans 8 columns centred, fields in two columns where pairs are natural (name/city). 768–1199px: span 10, fields mostly single-column. <768px: full-width panel, single column, stamp full-width.

**Edge cases.** *Long error text:* error captions wrap to two lines maximum by copy law (§12); the coupon grows — it never clips a correction. *Autofill:* filled-state ticks appear for autofilled fields on first paint check, so the coupon honestly shows what the browser wrote on its lines. *Double submit:* the stamp is disabled after first press; the marching dashes are the pending state, and a second press is impossible, not merely ignored. *Success without navigation (SPA):* the franked coupon remains in place as the receipt; a "clip another" reset link (apparatus style) restores an empty coupon with the §6.2 print beats skipped (it arrives printed). *Honeypot/anti-spam fields:* visually hidden in the ordinary way — the theme's print honesty does not extend to helping bots read the form.

**Accessibility spec.** Labels are real `<label>`s (the apparatus small print above each rule), errors are `aria-describedby`-linked and announced via a polite live region when they letter in (the full message at once for AT; the lettering is visual only). The error summary on submit takes focus (`tabindex="-1"`). The checkbox is a real checkbox — the panel-square is its styled presentation, 24px box with a 44px hit area. Contrast: labels in ink (13.1:1); error text in red at 14px italic meets 4.6:1 (AA at that size on paper) and is always accompanied by the red rule + wash (never colour alone). The stamp button's text is uppercase apparatus at 12px with 0.1em tracking — legible, and its hit area is ≥ 48px tall.

**Tokens consumed.** `--ink`, `--ink-60`, `--red`, `--red-wash`, `--teal`, plate tokens, `--ease-press`, `--ease-snap`, `--stamp` (160ms), `--dash-march` (600ms), `--rule-field` (2px).


### 6.16 The imprint footer

**What & why.** A newspaper ends with its imprint: who printed this, where, in what inks, and the small print of the edition. The footer is that imprint block — a full-width panel-less zone (the one place borders relax) ruled off by a double ink rule (3px over 1px, the classic newspaper foot rule), containing the paper's name in Playfair, the colophon line naming the theme's own materials ("Set in Playfair Display & Lora · Printed in four colours on cream · No pixels were harmed"), real contact apparatus, section links as a compact contents (§6.13 grammar, no leaders), and the second registration bar (§6.5) standing complete at "Printed." It belongs here because the supplement's last act is to sign its work; a generic footer with social icons in circles is a different century's object.

**Structure.** `<footer class="imprint">`: double rule, then a three-column broadsheet row (name + colophon line / contents list / apparatus column: address, email set as text, "printed by" line), then the completed registration bar with its "Printed." label, then the legal line in apparatus style. Social/contact links, if any, are text links in the apparatus column with §6.13 leader-less grammar — never icon buttons; if an icon is unavoidable it is a printed fleuron, not a brand glyph in a circle.

**Motion spec.** The footer prints like any panel (§6.2 border-less variant: the double rule draws left-to-right 500ms `press`, columns fade in reading order at 120ms stagger — the one place a fade is permitted, because the imprint is small print arriving, not a picture printing). The registration bar in the footer is rendered complete and static (it is the *record* of the printing, not the live instrument — the live one is in the masthead; two live instruments would disagree at the margins of the lerp and instruments must never disagree).

**States.** Unprinted → printing (on first entry) → printed (terminal). The footer's regbar is always at "Printed." — if the visitor jumps straight to the footer via anchor, the imprint still claims the edition complete, because the *edition* (the page as published) is complete even if this reader hasn't read it; the masthead instrument reports the reader, the imprint reports the paper. That distinction is deliberate and documented here so builders don't "fix" it.

**Content-merge.** Every line is real apparatus: the actual organisation, the actual sections, the actual typefaces and colours of the build. The colophon line is generated from the build's true tokens — a footer that lies about its materials fails §10.

**Failure fallback.** Static footer, complete bar, all links live. Nothing in the footer depends on JS except the rule draw, whose absence is invisible.

**Reduced-motion variant.** Rule pre-drawn, columns present, no stagger.

**Performance budget & mobile variant.** One draw + three fades, once. Mobile: columns stack (name, contents, apparatus), the double rule stays full-width, regbar keeps its four passes at mobile spec (§6.5).

**Choreography timeline** (t₀ = footer top crosses 80% vh):

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Double rule draws left → right |
| 2 | t₀ + 500ms | Rule complete; first column fades in |
| 3 | t₀ + 620ms / 740ms | Second and third columns follow |
| 4 | t₀ + 860ms | Imprint printed; the completed regbar was present from beat 1 (it is a record, not a reveal) |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Static imprint (post-print or no-JS) | Stacked static imprint |
| Printing | Rule draw + column stagger, once | Same, stagger 90ms |
| Hover | Links per §6.13 (leader-less: ink → plate colour) | n/a |
| Focus | Theme focus ring on links | Same |
| Scrolled-past | Printed | Printed |
| Disabled | No disabled states in an imprint | Same |

**Breakpoint behaviour.** ≥1200px: three columns. 768–1199px: two columns (contents wraps under the name). <768px: single stack, apparatus column last, legal line wraps freely.

**Edge cases.** *Very long legal lines:* apparatus style at 11.5px wraps without truncation — legal text is never ellipsised in this theme. *Missing apparatus (no address):* the column carries what exists; an imprint with one honest line beats three invented ones (Real Content Rule). *Footer reached without scrolling (short page):* the print beats run on load if the footer is in the initial viewport.

**Accessibility spec.** `<footer>` with the contents list as a second `<nav aria-label="Contents — footer">`. The completed regbar in the footer is `aria-hidden` (the live instrument in the masthead owns the progressbar role — one role, one owner). Legal and contact text is ordinary readable text at §2 contrasts.

**Tokens consumed.** `--ink`, `--paper`, the plate tokens, `--ease-press`, `--draw-rule` (500ms), `--stagger-col` (120ms).

### 6.17 The front-page hero (hero composition)

**What & why.** The hero is the supplement's front page: one wide panel — the issue's cover plate — composed as masthead-adjacent theatre: a Playfair plate headline, an italic standfirst, the resolving halftone picture (§6.1) as the panel's plate, a caption balloon (§6.10) carrying the picture's credit-and-joke, and an apparatus strip along the panel's foot (issue number, the feature's plate colour chip, "continued inside →" as a real anchor to the first strip). It belongs as its own element because the hero is where all the theme's systems meet at full strength, and a builder needs the composition specified as one object, not assembled from vibes.

**Structure.** `<section class="panel hero-plate">`: top apparatus row (issue/date left, plate chip + "The Colour Supplement" right), headline block (headline + standfirst, max 26ch headline measure), the §6.1 figure (full panel width, aspect 16/9 desktop, 4/3 mobile), caption row (balloon left, credit apparatus right), foot apparatus strip with the continued-inside anchor. The hero panel's border is 3.5px ink — the cover is printed heavier than interior panels, the one sanctioned border-weight variation.

**Motion spec.** On load (hero is above the fold): the panel arrives *mid-manufacture* — border pre-drawn (a cover does not wait to be scrolled to), headline unmask 380ms `turn` at load + 100ms, standfirst fades 200ms after, the §6.1 resolve owns the picture, the balloon's tail draws at resolve beat 4 (§6.1 timeline), the foot apparatus fades in last (load + 500ms). If the hero is somehow below the fold (custom landing), it runs §6.2's standard panel beats instead — one grammar, two doors.

**States.** Composing (load beats) → printed (all systems live: resolve scrubbing, balloon poppable, anchor live) → scrolled-past (resolve ratcheted complete, panel ordinary). Hover on the figure: §6.4 snap. The continued-inside anchor: hover draws a leader (§6.13 grammar) toward its folio — the word "inside" with the strip's panel number.

**Content-merge.** The hero contains nothing that is not the issue's real lead feature: its headline, its picture, its caption, its continuation. A hero that advertises the *site* instead of leading with a *story* is a landing page wearing the supplement (§9.7).

**Failure fallback.** The composed static hero: border solid, picture resolved, all text present — the no-JS hero is indistinguishable from the finished animated one at rest. That is the standard for the whole theme, stated here at its most visible point.

**Reduced-motion variant.** Fully composed at first paint: picture pre-resolved, headline unmasked, balloon static with tail drawn.

**Performance budget & mobile variant.** The hero owns the page's LCP: its image is the §6.1 budget (≤260KB desktop). No other panel may animate until the hero's load beats complete (the §5 concurrency budget is spent here first). Mobile: aspect 4/3, headline 36px, apparatus strip wraps to two rows, plate chip drops (colour is in the picture already).

**Choreography timeline** (t₀ = first paint with fonts ready):

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 100ms | Headline unmask begins (380ms `turn`) |
| 2 | t₀ + 300ms | Standfirst fades in (200ms) as the unmask completes |
| 3 | t₀ + 0ms → scroll | Picture resolving per §6.1's spatial timeline |
| 4 | §6.1 beat 4 | Balloon tail draws (300ms); caption letters in |
| 5 | t₀ + 500ms | Foot apparatus fades in; hero marked printed; page's other panels may now spend the motion budget |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Composing | Load beats run | Same, compressed timings ×0.9 |
| Printed | All systems live | Same |
| Hover | Figure plate snaps (§6.4); anchor leader draws | n/a |
| Focus | Anchor/balloon focus per their elements; hero itself not focusable | Same |
| Scrolled-past | Resolved, ordinary panel | Same |
| Disabled / no-JS | Composed static hero | Same |

**Breakpoint behaviour.** ≥1200px: 16/9 plate, 54px headline, 3.5px border. 768–1199px: 3/2 plate, 44px headline. <768px: 4/3 plate, 36px headline, apparatus wraps, border 3px.

**Edge cases.** *No lead image (text-led issue):* the plate area becomes a typographic plate — the headline set huge across the full width with a fleuron rule and the standfirst as the picture's caption; the resolve applies to a fleuron dot-plate behind the type at 20% strength. The composition survives without photography because the supplement's first material is type. *Extremely long headline (>9 words):* Playfair steps down one scale notch per build rule (54 → 44) rather than wrapping past two lines — a cover headline is two lines maximum, enforced at the §10 gate. *Hero video:* forbidden. A supplement cover does not move; video pitches belong to another theme.

**Accessibility spec.** The hero's `<h1>` is the headline (the masthead's paper name is a `<p>`-styled brand line, not a competing heading — one h1 per page, and it is the story's). Reading order: apparatus, headline, standfirst, figure (with alt), caption, foot strip — DOM order matches. The figure's alt is editorial, not decorative, here: the cover picture is content. Contrast: headline ink on paper 13.1:1; the plate chip is never text-bearing.

**Tokens consumed.** `--ink`, `--paper`, plate tokens, `--ease-turn`, `--ease-press`, `--border-hero` (3.5px), `--unmask` (380ms), plus all of §6.1's tokens.

### 6.18 Classified listing rows (the small ads)

**What & why.** Listing pages in a newspaper are the classifieds: dense little ruled rows, each a small ad — a bold lead word, a run of descriptive text, a price or date in lining figures, separated by hairline rules and grouped under plate-coloured section heads ("Situations Vacant", "Bicycles", "Lost & Found" — or their modern equivalents). The theme's listing unit is that row. It belongs here because it solves the theme's hardest page type — the long list — in native grammar: where other themes reach for card grids, the supplement reaches for the classified column, and density becomes charm instead of clutter.

**Structure.** A `.classifieds` panel containing a section head (apparatus style, plate-colour rule) and `<ul>` of `.ad-row`s: lead word(s) in Lora 600 (the ad's first words are its headline, classified-style), body run in Lora 400 at 15.5px, a right-aligned apparatus datum (price/date/count) in Playfair lining numerals, hairline 1px `--ink-60` rules between rows, full 2.5px ink rules between groups. Rows are whole-row links when they lead somewhere (with the datum inside the link), or plain rows when they are pure information (a timetable, a results list).

**Motion spec.** Entry: rows print in reading order with the §6.2 caption grammar at row scale — each row's lead word inks in (density 55% → 100%, 160ms) staggered 40ms per row, capped: rows beyond the first 12 in a group arrive printed (a classified column is long; its printing must not become a ceremony the reader waits through). Hover (link rows): the row's ground washes to its group's plate wash (`--teal-wash` etc. at 8%) over 150ms and the lead word's plate snaps into register if the lead carries a plate chip. Group heads: their plate rule draws (§6.8 flourish grammar, 300ms) on first entry.

**States.** Unprinted → printing (first 12 rows) → printed. Link rows: rest → hover (wash + snap) → focus (wash + ring inset) → active (wash deepens one step). Plain rows have no interactive states and must not fake them (no hover wash on a non-link row — a row that reacts must lead somewhere).

**Content-merge.** The row *is* the listing: lead, description, datum. The classified grammar adds nothing but its rules and heads — the two print objects that make a list into a column.

**Failure fallback.** A plain ruled list. The density-ink entry is JS-added; without JS all rows print at full density. The list is fully usable with every enhancement dead — it is a list.

**Reduced-motion variant.** All rows printed at full density on entry; hover wash becomes instant.

**Performance budget & mobile variant.** Density animations on text colour only (`color-mix` steps), capped at 12 rows; lists paginate or "continue" at 40 rows per panel (a broadsheet column ends; the next begins in a new panel). Mobile: the datum drops below the lead word (apparatus line) instead of right-aligning — a 360px column cannot hold the classified three-part line — and row padding grows to keep link rows ≥ 44px tall.

**Choreography timeline** (group entry, t₀ = group head crosses 75% vh):

| Beat | Time | What happens |
|---|---|---|
| 1 | t₀ + 0ms | Group head's plate rule draws (300ms) |
| 2 | t₀ + 100ms | Row 1 lead inks in (160ms) |
| 3 | t₀ + 100ms + 40ms × n | Rows stagger in, reading order |
| 4 | t₀ + ~660ms | Row 12 inked; rows 13+ were printed from the start |
| 5 | Hover thereafter | Wash + snap per row, 150ms |

**State matrix.**

| State | Desktop | Touch |
|---|---|---|
| Rest | Full-density rows, hairline rules | Same, datum stacked |
| Printing | First 12 rows ink in, staggered | Same, stagger 30ms |
| Hover (link row) | Plate wash + lead snap | n/a |
| Focus | Wash + inset ring | Same |
| Active | Wash deepens; navigation follows (§6.12) | Tap: wash flash 120ms, then turn |
| Scrolled-past | Printed | Printed |
| Disabled | Non-link rows have no states; a sold/expired item keeps its row but its datum is replaced by the apparatus word "Gone" — classifieds honesty | Same |

**Breakpoint behaviour.** ≥1200px: two classified panels side by side (two columns of the broadsheet) with independent group heads. 768–1199px: single panel, rows full width. <768px: single panel, stacked datum, group heads sticky within the panel at top 0 of the panel's scroll context only on very long lists (>25 rows) — and never sticky on the page itself (the masthead owns page stickiness, §6.7).

**Edge cases.** *Empty group:* the group head prints with one row — the empty-state line in the classified voice (§12): "Nothing advertised under this head today." — never a blank panel. *Huge datum variance (prices, dates, "Free"):* the datum column is fixed-width per group (the widest datum sets it, max 12ch) so rules align like a printed column; overflow data wraps under the lead instead of breaking the column. *Duplicate leads:* classifieds allow them (two "Bicycle" ads are two ads); no dedup theatre. *Sorting/filtering (where the product needs it):* controls live in the panel's head as apparatus-style text toggles; a re-sort re-prints the group with beats capped at 6 rows — the reader asked for a new column, they get a brisk one.

**Accessibility spec.** A real list (`<ul>`) with list semantics intact; link rows have one link each whose name is lead + datum ("Bicycle, lady's frame — £40" pattern) so a screen-reader user hears the ad as its reader would scan it. The ink-in entry never hides rows from AT (density is colour, not visibility). Focus ring is inset (rows are full-bleed within the panel; an outset ring would cross the hairlines). Group heads are `<h3>` under the page's listing `<h2>` — the classifieds keep the document outline honest.

**Tokens consumed.** `--ink`, `--ink-60`, plate wash tokens, `--ease-press`, `--ink-in` (160ms), `--stagger-row` (40ms), `--wash-row` (150ms), `--rule-hair` (1px).


## 7. Page application map

**Home (the issue front).** Masthead + registration bar → §6.17 hero plate (the lead story) → §6.7 pinned strip (the first comic/feature strip, 3–5 panels) → feature panels alternating plates (§6.2/§6.14) → a full-width classifieds strip (§6.18) as the "inside this issue" index → §6.15 coupon → §6.16 imprint. The home page is one issue, read top to bottom; it never becomes a portal of equal boxes.

**Listing (the classified pages).** Masthead (compact — nameplate at 44px, no flourish) → contents rail as section index → classified panels (§6.18) grouped under plate heads, two-up on desktop → plate-card rows (§6.14) only for the *featured* group at the top (one row of 3, marked as plates, not ads) → coupon (the issue's standing offer) → imprint. Pagination is printed as folios: "More small ads → page 2" as a §6.12 turn, never an infinite scroll — a newspaper does not infinitely scroll, it *continues on page 2*, and the visitor is told so.

**Detail / article (the feature page).** Masthead compact → the feature as a sequence of panels in reading order: headline panel (Playfair headline, standfirst, apparatus byline — author and date as real data), plates at the points the text earns them (§6.9 settle, §6.1's resolve reserved for the opening plate only), pull-quotes as caption balloons at panel scale (§6.10 grammar without the pop — a pull-quote is already speaking), a mid-feature strip panel if the story has a sequence (steps, a day, a journey), the ending panel carrying the author's imprint line → related plate cards ("More from this issue") → coupon → imprint. Drop cap per §3 law on the first text panel.

**About (the paper introduces itself).** Masthead → a "letter from the editor" panel (the theme's warmest page: Lora body, one plate — red — used sparingly) → the masthead's own history as a strip of dated panels (real dates or none) → the people as plate cards with fleuron plates where no portrait exists (never invented portraits) → circulation counters (§5) in an apparatus panel → coupon or contact panel → imprint. The about page is where the counters and the colophon line earn their keep.

**Contact / checkout equivalent (the coupon page).** Masthead compact → the §6.15 coupon at full width (span 8 centred) with its scissors rule → beside/below it, the "small print" panel: what happens next, in caption voice, as three numbered apparatus lines → imprint (no second coupon; one ask per issue). For commerce: the product is a plate card enlarged to feature panel; purchase happens through the coupon grammar (details → stamp button) and payment itself is handed to the processor's own page from the franked state — the supplement takes the order; it does not pretend to be a bank.

**404 / not found (the missing page).** A single panel: a fleuron plate, the headline "This page was not in today's issue." in Playfair, a caption-voice line, and the contents rail (§6.13) as the way back — the supplement treats a missing page as a printing apology, not a system error, and the registration bar stands at "Printed." (the rest of the issue exists).

**Search results (the index).** Classified grammar throughout: the query as the group head ("Advertised under: 'bicycle'"), results as §6.18 rows with the matched term's lead word in the group plate colour. No results: the classified empty line (§12) plus two suggested heads. Search is an index, and the theme already owns a perfect index form.

## 8. Worked examples

### 8.1 The hero — "The Millers' Garden" (a seed company's Sunday lead)

A heritage seed company leads its spring issue with a feature on a community garden. The hero panel (§6.17): apparatus row reads "No. 214 · Sunday, 6 April" and "The Colour Supplement". Headline, Playfair 700 at 54px: "The Millers' Garden Wakes Up." Standfirst, Playfair italic: "Twelve plots, one borrowed mower, and the first peas of the year — our spring visit to the allotments behind Mill Lane." The plate: a photograph of the garden at dawn, halftone-screened, 16/9. Caption balloon at the plate's lower-left: "Mr. Okafor inspects the peas. He always inspects the peas." — credit apparatus right: "Plate I · Photograph: R. Sethi".

**Scroll/load timeline.** t₀ (first paint, fonts ready): border pre-drawn (3.5px). t₀+100ms: headline unmasks left→right, 380ms `turn`. t₀+300ms: standfirst fades (200ms). The picture begins at 14px pitch; as the visitor scrolls the hero through centre-frame, `--resolve` scrubs 0→1 (pitch 14→3px, overlay gone by hero-centre at viewport centre). At that beat the balloon's tail draws (300ms) from balloon to the figure of Mr. Okafor in the plate, and the caption letters in at 45ms/word (9 words ≈ 400ms). The foot apparatus ("Continued inside → Panel 2") fades in at t₀+500ms. The registration bar overhead sits in pass 1, red filling. A keyboard visitor tabbing to the balloon button gets the §6.4 snap on the plate and the §6.10 focus states — the same hero, at reading speed.

### 8.2 Mid-page section — "A Strip in Four Panels: Sowing, Week by Week"

Midway down the same issue, a how-to strip runs under the pinned masthead (§6.7). Four panels, each a week: a small screened plate (a hand sowing, a first shoot, a row of green, a trug of peas), a Lora 600 panel heading ("Week One — The Drill"), two lines of body, and a caption. The strip's plates rest 2px off-register (teal — this is a calm, instructional strip).

**Scroll timeline.** The masthead pins as the strip zone enters (beat 1 of §6.7; its bottom shadow plate fades in over 150ms). Panel 1's top clears the masthead's foot + 40px: border draws (450ms `press`), art wipes (300ms), heading unmasks, caption letters in — total ≈ 1.1s, during which the visitor has scrolled perhaps 15% of the panel. Panels 2–4 repeat the beats at the same reading line, staggered naturally by scroll. The teal pass of the registration bar completes somewhere inside panel 3 — the reader is halfway through the issue while learning to sow. Hovering panel 3 snaps its shoot photograph into register (200ms); on a phone, panel 3 snaps as it crosses centre-frame. Panel 4's caption is a balloon shared with panel 3's strip balloon: clicking panel 4 pops it and re-points its tail (§6.10) — the joke about the peas lands wherever the reader asks for it. As the strip ends, the masthead's shadow fades (150ms) and it scrolls away; the next feature's headline panel arrives in ordinary flow.

### 8.3 Conversion section — "Take the Garden Every Sunday" (the seed catalogue coupon)

The issue closes with the coupon (§6.15): a dashed-border panel, scissors fleuron at its top-right, headline "Take the Garden Every Sunday", standfirst in caption voice: "The spring catalogue and a packet of Mr. Okafor's peas, posted monthly. Clip, fill, stamp." Fields: Name (ruled line), Address (two ruled lines), Email (one line), one panel-square checkbox — "May we write to you about the autumn issue?" — and the stamp button: "POST THE COUPON".

**Scroll/interaction timeline.** The coupon panel enters at 75% vh: border prints (§6.2 — dashed from the start; the dash is its nature, not a loading state), scissors draw last (300ms). The visitor tabs in: Name's rule thickens and a red plate slides beneath it (this coupon's plate is red — the offer is the issue's one loud moment) over 200ms. They mistype the email: on blur, the rule reddens, the ground washes red at 10%, and beneath the line the caption letters in: "That address looks short a letter — the postman will lose it." (45ms/word.) They fix it; the error clears on input, rule back to ink over 200ms, the end-tick appears. They press the stamp: it presses (160ms), dashes march while the request flies, and on success the teal frank lands at −6° across the panel's corner — "Posted · Thank you" — while the confirmation caption letters in below the headline: "Your first catalogue leaves with Friday's post." Focus has moved to that confirmation (live region), the form is inert, and the registration bar in the masthead — if the visitor scrolls up to look — stands complete: the issue, and the order, are printed.


## 9. Anti-slop — how this theme goes cheap, and the cure

**9.1 Misregistration as mess.** Plates offset by random amounts per element, in random directions, or at 4px+, reads as a broken page, not a printed one — and 3px (the funniest page's privilege) leaking everywhere is the same failure. *Cure:* one offset, one direction, one token (`--reg: 2px`, +x, red channel), everywhere; 3px on exactly one designated page/section per build, recorded in the build notes.

**9.2 Halftone as wallpaper.** Dot screens tiled over backgrounds, section dividers, and buttons — dots where no picture is — turns the screen from a print property into a texture pack. *Cure:* dots exist only as the screen of an actual image (or its skeleton). If there is no picture, there are no dots. Backgrounds are paper.

**9.3 Cartoon noise.** Speech balloons on every heading, starbursts, "POW!" colours at full saturation, borders on everything including buttons and inputs — the theme performed as a costume. *Cure:* gallery restraint is the brief (§1): one balloon per panel maximum, plates rationed per §2, interactive elements in ink with print behaviours (§11), and the anti-test — if a children's party invitation would look at home, remove elements until it wouldn't.

**9.4 The uniform card grid.** Twelve identical plate cards in a 4×3 grid is a template wearing the theme. *Cure:* §4's mixed spans and plate-colour rhythm; on listing pages prefer §6.18 classified rows and reserve cards for featured plates. A grid may exist (the classified panels two-up) but its units must differ in span, plate, or content weight.

**9.5 Nervous line-work.** Tails redrawing on hover, borders re-drawing on every scroll pass, flourishes looping — line-work that won't sit still reads as anxiety, and print is calm. *Cure:* every draw in this theme runs once, on first print (§6.2, §6.8); states after that are weight and colour changes only.

**9.6 Flourish inflation.** Bounce-settles on sub-headings, drop caps in every panel, scissors on every form, stamps on every button. Each ritual is rationed in its element spec; spending them everywhere bankrupts all of them. *Cure:* the ration table is the spec — masthead flourish once (§6.6), drop cap once per page (§3), scissors only on the coupon (§6.15), stamp only on submit (§6.15).

**9.7 The hero that advertises the site.** A hero panel whose headline is the company's slogan and whose plate is a smiling team photo breaks the fiction that this is an issue with a lead story. *Cure:* the hero leads with a story, a feature, an offer with a date on it (§6.17) — something with apparatus (issue, plate number, continuation). If the client has no lead story, the theme is wrong for the page (§1).

**9.8 Fade-itis.** Panels fading in, images crossfading, modals fading — film grammar smuggled back in. The supplement wipes, draws, and sets; it fades in exactly two places (the imprint's small print, §6.16, and the skeleton resolve, §6.12) for stated reasons. *Cure:* audit every transition: if it is an opacity ramp and not one of the two exceptions, replace it with the print behaviour for that element.

**9.9 Mustard text and plate soup.** Mustard words on cream (2.1:1 — illegible), panels using all four plates at full strength outside the hero/finale, red body copy. *Cure:* §2's pairing rules are hard; the §10 gate includes a contrast sweep and a one-plate-per-panel count.

**9.10 The screen that never resolves.** Coarse halftones that stay coarse because the scrub was wired to the wrong element or the fallback was skipped — the theme's signature failure, and the one the original standing rules were written against. *Cure:* the base layer is always the finished picture (§6.1), the 1.2s watchdog is not optional, and the §10 gate includes a JS-disabled pass and a loop-killed pass on every build.

## 10. Quality gate — minimum bar before this theme may be used in a build

A build in this theme may not ship unless every item passes. Items marked ◆ are blocking: one failure fails the build.

- ◆ **Registered by default:** with JavaScript disabled, every page is complete — pictures resolved, borders solid, captions lettered, plates at 0px offset. (Test: JS off, full pass.)
- ◆ **No stranded abstraction:** kill the scroll loop mid-page (devtools) — within 1.2s every image is at final sharpness and every panel is printed. (§6.1/§6.2/§6.9 watchdogs.)
- ◆ **One press:** every plate on every page rests at exactly `--reg` (2px, +x, red channel); the 3px funniest-page exception, if used, appears on exactly one page/section and is noted in the build record.
- ◆ **Contrast sweep:** no mustard text on paper; no red body copy; all text meets §2 ratios at rest offset; the regbar's mustard pass is never the sole carrier of its state (label text present).
- ◆ **Reduced motion:** with `prefers-reduced-motion`, a full pass shows: pre-resolved halftones, no pin, no shimmer, no wipes/draws/pops, counters at final values, regbar mapping 1:1. Nothing moves that a still page wouldn't.
- **Motion vocabulary audit:** every animation on the page is one of §5's named behaviours with its specified duration/easing; no unlisted transition exists (search the CSS for `transition`/`animation` and account for each).
- **Concurrency:** no viewport ever shows more than 3 panels printing, 1 pinned scene, 1 scrubbed hero, and the capped shimmer family (§5/§6.11 caps verified on the longest page).
- **Panel grammar:** every content section is panelled; mixed spans present on home; no uniform 12-card grid; one balloon per panel maximum; drop cap ≤ 1 per page.
- **Apparatus honesty:** issue numbers, dates, counters, and colophon lines show real data or are absent; the footer's colophon line names the build's actual fonts and colours.
- **Performance:** §14's budget holds on the heaviest page (hero image ≤ 260KB, page total ≤ 900KB initial, no long task > 50ms from theme code, 60fps scroll on a mid-range phone with the loop running).
- **Keyboard pass:** full page reachable and operable by keyboard; focus is never under the pinned masthead (scroll-margins set); focus states snap plates and show rings per §6.
- **Copy pass:** headlines, captions, errors, and empty states obey §12's voice rules; balloon captions ≤ 14 words; no lorem, no "Welcome to our website", no exclamation marks outside a designated funniest page.


## 11. Component inventory — every component, in this theme's treatment

Each component below is specified once, here, so any page built in the theme draws from the same printed stock. All components obey §2 colour law, §3 type law, and the standing rules (normal cursor, focus always visible, nothing conveyed by colour alone).

- **Buttons (primary).** The stamp button (§6.15 grammar, general use): ink 2.5px border, paper ground, apparatus uppercase label, flat `--plate-shadow` 4px. Press: scale 0.97 with shadow collapsing to 1px, 160ms `snap`. Hover: shadow grows to 6px, ground warms to the action's plate wash at 8%. One primary per panel.
- **Buttons (secondary).** The contents item (§6.13 grammar): text with a dotted leader or a 1px ink underline offset 3px, plate-colour ink on hover. No border, no fill — the supplement's second actions are printed lines, not boxes.
- **Text inputs.** Ruled-line fields (§6.15): transparent ground, 2px ink bottom rule, apparatus label above, Lora 17px input. Focus: rule 3px + plate slide. Error: red rule + wash + lettered caption. Disabled: rule in `--ink-60`, text at 70% density.
- **Textarea.** A ruled *block*: the coupon's address treatment extended — a panel-bordered area with faint ruled lines every 29px (the line-height) so writing sits on lines like a letter. Same focus/error grammar as inputs, applied to the block's border.
- **Selects.** A ruled-line field with a printed chevron (a small ink fleuron, not a system arrow) at the rule's right end; the open list is a mini-panel (ink border, paper ground) whose options highlight in the field's plate wash. Native `<select>` styled is preferred over a custom listbox wherever the platform allows.
- **Checkboxes & radios.** Panel squares (checkbox, 20px, fills with its plate colour + ink tick when checked, §6.15) and plate circles (radio, fills with a centred ink dot — the one other sanctioned circle besides balloons). Hit areas 44px. Indeterminate checkbox: half-plate fill, a state the print metaphor handles honestly (part-printed).
- **Toggles.** Forbidden as sliding switches (a switch is a machine part). A binary choice is a checkbox, or a two-option *plate pair*: two small panels side by side, the chosen one printed in its plate wash with a 3px border, the other at rest — selection shown by ink weight, change is a 150ms wash fade (one of the theme's rare fades, justified: it is a plate being laid, §9.8's spirit preserved by keeping it out of content panels).
- **Tabs.** A strip's contents line: tab labels as §6.13 items on a shared rule; switching panels is a §6.3 hard wipe. The active tab's label carries its plate colour and a 3px rule beneath. Tabs never scroll horizontally on mobile — they wrap to two rows of the contents grid.
- **Accordions.** "Further panels in this strip": the summary row is a panel head (Lora 600 + a fleuron that rotates 90° on open, 200ms `press`); opening wipes the body in downward (§6.3 grammar rotated: the sheet pulls down, 300ms), closing reverses instantly to printed-hidden (no ceremony for putting things away). One open per strip by default.
- **Tables.** The results table / fixture list treatment: no outer border; a 2.5px ink head rule and foot rule, 1px `--ink-60` row rules, Playfair lining numerals right-aligned, Lora text left, plate-colour head labels in apparatus style. Row hover: paper-deep wash. Tables never carry halftone, plates, or shadows — tabular matter is the supplement's driest page and proud of it.
- **Badges & tags.** Small plates: a rectangle (square corners) of plate wash with an ink border 1.5px and apparatus text in ink — the colour is a *wash*, the text is always ink (contrast law). A badge in mustard wash with ink text is the theme's standard "new this week" marker.
- **Alerts & notices.** Panels at small scale with the scissors-less dashed border reserved for coupons replaced by a solid 2.5px border in the alert's ink: information = ink with a fleuron; success = teal border + frank-stamp tick; warning = mustard border + ink text (never mustard text); error = red border + `--red-wash` ground + caption-voice text (§12). Alerts print in (§6.2 beats at 0.8× durations) and are dismissible only when they are not errors of record.
- **Modals.** A panel torn from the supplement: full ink border 3.5px, paper ground, flat shadow plate 8px, over a `--ink` scrim at 55% (flat, no blur — print has no blur). Entry: the page-turn's edge grammar at modal scale — a 260ms wipe from the reading-start side. Focus trapped inside; Esc closes; the modal's own headline is its `<h2>` in Playfair. One modal at a time; a modal never opens from a modal (the supplement is flat).
- **Toasts.** Imprint slips: small paper slips that slide (translateY 8px + the §6.16 fade, 200ms) into the foot of the viewport above the imprint zone, apparatus text + one line of caption voice, auto-retiring in 5s (errors never auto-retire). Max two visible; they stack like slips on a spike file.
- **Pagination.** Folios (§7 listing law): "← Earlier in the issue · Page 2 of 5 · Later in the issue →" as apparatus text links with leader dots (§6.13), navigation by §6.12 turn. Numbered folios up to 7; beyond that, first/current/last with an ellipsis *printed as three dots in ink*, not a disabled button.
- **Breadcrumbs.** A contents line fragment: "This issue › The Garden › Sowing" in apparatus style with › as a printed separator (a fleuron arrow), each ancestor a §6.13 link. One line, never wrapped into a panel.
- **Progress (task).** For multi-step flows (checkout, signup): the registration bar grammar (§6.5) with steps as passes — but a 3-step flow uses three passes (red, teal, ink; mustard is skipped rather than subdividing — passes are plates, and a plate is never half a plate). Step labels in apparatus style beneath.
- **Search field.** A ruled-line input (§6.15) with a printed magnifier fleuron as its submit stamp-button at small size; results per §7's index grammar. Recent searches, if offered, are classified rows (§6.18), not chips.
- **Avatars / portraits.** Halftone plates, circular-cropped *only* inside balloon-adjacent contexts (a speaker's portrait beside their balloon); otherwise square plates in panel frames. No portrait exists for a person who hasn't supplied one — a fleuron plate stands in (§6.14).
- **Dividers.** Three sanctioned rules: the hairline (1px `--ink-60`, inside panels), the panel rule (2.5px ink, structural), and the double foot rule (3px over 1px, footer and section finales only). A divider with a centred ornament is the fleuron rule (§6.8 draws it); no other divider styles exist.
- **Loaders (inline).** The coarse-dot plate (§6.12) at component scale; a button in flight shows the stamp pressed + its label replaced by three marching dots in apparatus style (the coupon dash grammar at 600ms).

## 12. Content & copywriting voice

The supplement's voice is a **cheerful sub-editor**: precise about facts, warm about people, funny exactly once per page, and never breathless. Copy is written as print — it will be *read*, in order, by someone with a cup of tea — not scanned by someone fleeing the page.

**Headline style.** Sentence case, concrete nouns, a verb doing real work, ≤ 9 words for features, ≤ 6 for panels. The headline names the story's subject, not the company's virtue. *Yes:* "The Millers' Garden Wakes Up." / "Twelve Plots, One Borrowed Mower." *No:* "Welcome to GreenGrow — Your Gardening Journey Starts Here!" (slogan + journey + exclamation: three failures in one line). Numbers in headlines are lining figures and always real ("Twelve plots" was counted).

**Label & apparatus style.** Uppercase, terse, factual: "No. 214 · Sunday, 6 April", "Plate II", "Continued in Panel 3", "Price: one smile" is the ceiling of whimsy for apparatus — one joke in the furniture per page, and it must be *in* the furniture (a price line, a folio), never in a headline doing information's job.

**Caption voice (balloons & captions).** First person plural or gentle third person, ≤ 14 words, one observation or one joke, always about *this* picture. *Yes:* "Mr. Okafor inspects the peas. He always inspects the peas." *No:* "Check out this amazing garden pic!" — "check out", "amazing", and the exclamation are all banned words/forms in captions.

**Error voice.** The paper corrects you like a caption, never alarms you like a system. State what happened, what to do, in one sentence, with the reader cast as competent. *Yes:* "That address looks short a letter — the postman will lose it." / "The coupon needs a name before it can be posted." *No:* "Error 422: Invalid input detected." / "Oops!! Something went wrong." Errors never use "oops", never use exclamation marks, never blame ("you failed to…"), and always name the field in the field's own label words.

**Empty-state voice.** Classified honesty (§6.18): "Nothing advertised under this head today." + one helpful direction ("Try the Garden head — it is full this week."). An empty state is a small ad for the rest of the issue, written in the same voice; it never says "No data found" and never shows an illustration of a sad mascot.

**Button & action labels.** Verb + object, from the theme's world where honest: "Post the coupon", "Turn the page", "Read the strip", "See this week's plates". Generic labels ("Submit", "Click here", "Learn more") are banned; "Continue" is permitted only as "Continued inside →" with a real destination panel named in the apparatus.

**Microcopy laws.** Exclamation marks: maximum one per page, and only on the designated funniest page/section (§6.4's page earns the punctuation too). "Amazing", "incredible", "revolutionary", and "journey" are banned outright. Prices, dates, counts, and issue numbers are always real or absent (Real Content Rule). Every page's colophon line (§6.16) is generated from the build's true materials.

## 13. Full-page scroll choreography map

One page (the home issue), every motion beat from masthead to imprint, in order. Times are for a reader scrolling at a natural reading pace; scrubbed beats are positional.

| # | Scroll position | Beat | What the visitor sees & feels |
|---|---|---|---|
| 1 | Load | Masthead flourish (§6.6) | "Sunday" swells and settles once — the paper announces itself, then is calm |
| 2 | Load + 100ms | Hero headline unmask (§6.17) | The lead story's headline sets itself left to right |
| 3 | Load → hero centre | Halftone resolve (§6.1) | The cover picture sharpens as it is attended to; caption letters in at full resolve; the bar's red pass begins |
| 4 | Hero exits up | Strip zone approaches | The masthead readies to pin; nothing moves yet — anticipation is stillness |
| 5 | Strip zone top | Pin engages (§6.7) | The nameplate folds over the first page; its shadow plate appears — the paper is now *held* |
| 6 | Strip panels 1–5 | Panel prints at the reading line (§6.2), tails draw (§6.8), plates breathe (§6.4) | Each panel is manufactured as it is met: border, picture, caption — the press works at reading speed |
| 7 | Inside the strip | Registration bar: red completes, teal fills | Progress is felt as printing, not as a percentage |
| 8 | Strip ends | Pin releases (§6.7) | The nameplate lets go and scrolls away — the ceremony of the opening is over |
| 9 | Feature panels | §6.2 prints, §6.9 images settle, §6.4 hover snaps, §6.11 shimmer in the margins of attention | The issue's middle: varied plates, each panel a small press run; hover corrects the print under the reader's hand |
| 10 | Classified strip | Group rules draw, rows ink in (§6.18) | The tempo changes — denser, quicker, the classifieds' bustle after the features' calm |
| 11 | Counters panel | Circulation & panel counts roll (§5) | The paper states its facts in Playfair numerals — a moment of pride, printed plainly |
| 12 | Coupon zone | Coupon prints; scissors draw last (§6.15) | The ask arrives as a physical object to clip — commitment feels tactile, not funnelled |
| 13 | Imprint | Double rule draws; columns settle (§6.16) | The paper signs its work; the footer's bar stands at "Printed." |
| 14 | Bottom | Nothing | The issue ends. No infinite scroll, no autoplay, no parting gimmick — the last feeling is of a finished, kept thing |

**Rhythm law the map enforces:** ceremony (beats 1–8) → variety (9–11) → commitment (12) → signature (13–14). Any page type reorders the middle but never the opening ceremony or the closing signature (§7).

## 14. Whole-page performance budget

The theme's effects are cheap by construction (transforms, opacity, one scroll loop); this budget keeps them that way on the heaviest page type (home).

| Budget line | Limit | Notes |
|---|---|---|
| Initial payload (HTML+CSS+JS+fonts+hero) | ≤ 900KB | Fonts subset to Latin + punctuation, two faces, three weights total across both |
| Hero image (§6.1, both copies) | ≤ 260KB desktop / ≤ 150KB mobile | AVIF first, WebP fallback |
| All other images per page | ≤ 400KB total | Screened plates compress well — halftone is mostly pattern; if a plate exceeds 60KB, re-screen at a coarser resting pitch before shipping |
| Theme JS (loop, observers, interactions) | ≤ 38KB gzipped | One shared rAF loop; no per-element listeners beyond delegation; no animation library — the easings are CSS |
| Scroll frame cost | ≤ 4ms JS per frame on a mid-range phone | The loop writes CSS variables for in-band elements only; layout is never read inside the loop (positions cached on resize/intersection) |
| Long tasks | None > 50ms attributable to theme code | Panel prints are stroke/opacity work; image rescreening is pre-rendered plates, never runtime filtering of full-size photos |
| Animation concurrency | §5 caps: ≤ 3 panels printing, ≤ 6 paths drawing, ≤ 8 shimmering images, 1 pinned scene | Enforced by the loop's scheduler, not by hope |
| CLS | 0.00 from theme elements | Panel geometry is final from first paint (§6.2); aspect ratios reserved on all plates (§6.9) |

**Cut ladder (when the budget is exceeded, cut in this order, silently):** 1) grain drift (§6.11 overlay), 2) shimmer beyond the 4 nearest images, 3) register breathing (rest offset stays; the breath is the luxury), 4) §6.9 rescreen quantisation steps (settle becomes a plain scale), 5) the masthead flourish. **Never cut:** reveal fallbacks and watchdogs, the resolve's base layer, reduced-motion behaviour, focus states, or any element's content. The ladder cuts theatre before it ever touches legibility — that ordering is the theme's performance ethics, and reversing it fails §10.

## 15. Build-order checklist

Implement the theme in this order; each step leaves the page shippable.

1. **Tokens & type.** §2 tokens (including derived), §3 faces and scale, apparatus/body/caption styles. Page reads correctly with zero motion.
2. **Panel grammar.** Borders, spans, spacing rhythm (§4); masthead and imprint as static panels. The broadsheet stands.
3. **Static content pass.** All panels with real content; plates registered (0px); halftones at final pitch. *This is the no-JS ship state — verify it now, before any motion exists.*
4. **The scroll loop.** The single rAF engine with lerp, band tracking, and the scheduler enforcing §5/§14 caps — empty of effects, instrumented for frame cost.
5. **Reveals.** §6.2 panel prints + §6.8 tail draws + watchdogs. Verify the JS-kill test (§10) at this step, not at the end.
6. **The hero systems.** §6.1 resolve + §6.17 composition + §6.6 flourish.
7. **The strip.** §6.7 pin (sticky only) + reading-line triggers + scroll margins.
8. **Instruments.** §6.5 registration bar (both instances, one live), §5 counters, §6.13 scrollspy.
9. **Interactions.** §6.4 register snap + breath, §6.10 balloon pop, §6.14 card lift, §6.3 wipes, §6.12 page-turn, §6.15 form behaviours + franking.
10. **Ambient.** §6.11 shimmer + grain, with caps; §6.9 rescreening settle.
11. **Reduced-motion & fallback pass.** Every element's reduced-motion variant switched and walked; JS-off pass; loop-killed pass; print stylesheet (plates registered, screens at final pitch).
12. **Gate.** §10 in full, on the heaviest page, on a mid-range phone and a desktop. Record the funniest-page designation (or its absence) in the build notes.
