# 60. Meteorite Iron — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** A site forged from a fallen star: Widmanstätten
crystal patterns — kamacite and taenite lamellae that only form
when iron-nickel cools at a few degrees per million years inside
an asteroid's core — become the page's signature texture, and
everything feels hammered, heavy and singular. Palette anchors:
iron dark `#17181C`, etched steel `#3A3D46`, crystal band
`#8A8F9C`, polished edge `#C8CBD4`, forge ember `#C96A2B`. Type:
Archivo (display, black weights, condensed) + IBM Plex Mono
(body/data). The page opens with one forge strike and then does
only one thing for its whole length: it cools — ember accents
dulling from forge orange to cold steel as the reader descends —
until the footer, which is cold, still and mirror-bright: the
cooled end of the process the hero begins.

## 1. Concept & world

Meteorite Iron is the website of a material that arrived. Its
iron did not come out of a mine; it fell out of the sky already
older than the Earth, carrying a crystal structure no furnace on
this planet can reproduce — the Widmanstätten pattern, broad and
fine bands of two nickel-iron alloys intergrown at ±60°, which
appears only when metal cools so slowly that a human lifetime is
not a measurable unit of its formation. A terrestrial forge can
shape this iron, etch it, polish its edge. It cannot make more
of it, and it cannot make the pattern twice: cut the same
meteorite at a different angle and the bands run differently.
Every object in this theme's world is therefore singular in a
way that is not marketing. It is crystallography.

The page performs the material's biography in order. It begins
hot: one forge strike (§6.1) dents the maker's name into the
hero plate, sparks fly once and die, and from that moment the
page is a cooling body. Section markers carry embers that dull
as the reader descends (§6.3); the margin holds a cooling bar
(§6.5) that begins as a glowing strip and ends as mirror steel,
etching one cross-hatch segment per section completed; a single
margin ember breathes beside the current section and slows as
the story cools (§6.6). Mid-page, the hero product pins and the
Widmanstätten pattern etches itself across the blade's own
photograph at the true lamellae angles (§6.4) — the crystal
forming, in seconds, at the speed the reader scrolls. The
footer (§6.10) is the end of the thermal story: polished,
mirror-bright, no embers, no loops, still. The visitor has not
just read about cooling. Their scroll *was* the cooling, and
the page keeps the receipt: dents they struck stay struck
(§6.9), the pattern stays etched, and nothing reheats behind
them.

**The theme's one law: cooling is one-way, and every figure is
a formation fact.** Two clauses, both audited by the gate.
(1) *One-way cooling.* Page temperature is a declared function
of the **deepest point the visitor has reached**, never of
their current position: `p = maxScrollDepth / pageHeight`, and
every ember, marker, bar segment and printed temperature on the
page is a function of that `p` alone. Scrolling back up does
not reheat anything — the crystal, once formed, does not melt
because the reader changed their mind. The single licensed
exception is touch: a hover or focus rekindles one marker's
ember briefly (§6.8), the way a thumb warms the spot it rests
on, and even that decays back to the temperature `p` dictates.
A build in which any element's heat is a function of live
scroll position — reheating on scroll-up — has broken the
material's physics and fails the gate. (2) *Formation facts.*
Every number the page prints — cooling time, nickel content,
lamellae width, mass, fall or find year — traces to the
specimen record (§6.17): the declared data object naming each
piece's meteorite, class, composition and provenance. A
counter that counts to a number nobody assayed, a "4.5 billion
years" sprinkled into copy for awe, a lamellae width that
disagrees with the pattern drawn beside it — each is a gate
failure, because in this world a figure is a measurement or it
is a lie, and the page does not lie about the iron.

**Best-fit sites and audiences.** Bladesmiths and knife makers
working meteoritic iron (the theme's native citizen: damascus
and monosteel blades forged from Gibeon, Muonionalusta, Canyon
Diablo); jewellers setting meteorite inlay and wedding bands;
watchmakers using meteorite dials; meteorite dealers and
collectors selling classified specimens with provenance;
museums and planetarium shops presenting a single famous fall;
a sculptor or furniture maker whose signature material fell
from the sky; any single-object luxury house whose entire
argument is *this exists once*. The audience it suits is
patient, technical and willing to pay for provenance: people
who read an assay line, who care that the pattern is drawn at
the true angles, who understand that a cooling bar is a
formation timeline and not a progress widget. Conversion in
this world is a commission, a reservation, or an enquiry about
one named piece — never a cart of forty SKUs.

**When NOT to use it.** Not for anything plentiful, fast or
cheap: mass retail, marketplaces, deal surfaces — the theme's
whole grammar is scarcity that happens to be true, and over a
catalogue of ten thousand interchangeable products it becomes
scarcity theatre, the exact slop §9 exists to refuse. Not for
dashboards or tools: etched panels and dented type are enemies
of rapid scanning, and §11 refuses the data grid outright. Not
for children's or playful products (the register is impact,
fire and deep time). Not for any client who wants "space"
decoration — stars, nebulae, rockets: the theme contains no
sky at all, only the iron after it landed; a starfield
background is failure 1 in §9. Not where the maker cannot
supply real specimen data: every figure must trace to a record
(§6.17), and a forge that will not name its meteorite, class
and nickel content has no business wearing this theme. If the
iron's origin is a secret, choose another theme.

## 2. Palette

Five anchors, inherited exactly. Derived tokens form a closed
list: a token not in this table does not exist in the theme,
and the gate greps built CSS for undeclared hex values.

| Token | Hex | Role | Usage ratio | Pairing & contrast (measured) |
|---|---|---|---|---|
| `--iron` | `#17181C` | Iron dark — the plate ground; page ground, panel faces | ~55% of viewport area | Carries `--edge` text at **10.88:1**, `--band` at **5.47:1**. The default reading ground; every other colour is a state of this iron. |
| `--steel` | `#3A3D46` | Etched steel — etched panel fills, recessed fields, the pattern's shadow alloy | ~20% | On `--iron` **1.64:1** — a surface distinction, never text. Carries `--edge` at 6.65:1, `--band` at 3.34:1 (large/graphical only). |
| `--band` | `#8A8F9C` | Crystal band — kamacite lamellae, captions, apparatus, secondary text | ~12% | On `--iron` **5.47:1** — the workhorse text grey. On `--steel` 3.34:1: apparatus and large text only. |
| `--edge` | `#C8CBD4` | Polished edge — primary text on dark, polished highlights, the mirror's approach | ~10% | On `--iron` **10.88:1**; on `--steel` 6.65:1. The brightest text the page allows itself until the footer. |
| `--ember` | `#C96A2B` | Forge ember — heat itself: markers, the cooling bar's hot end, sparks' parent colour | ≤3%, falling to 0% at the footer (§5 ration) | On `--iron` **4.70:1** — data and large text only, never body. On `--steel` 2.88:1 — graphical only. Ember is a *temperature*, not an accent: it appears only where the page is hot (§5). |
| `--iron-deep` (derived) | `#101116` | Unetched iron — the loading ground, the space behind plates, the 404's unfallen dark | — | Carries `--band` at 4.92:1 (apparatus only). One step below the plate: what the iron looks like before the forge touches it. |
| `--steel-pale` (derived) | `#565B68` | The etch's mid-line — pattern construction lines, hairlines on iron, disabled states | — | On `--iron` 2.62:1 — graphical only; never text, never a disabled *label* (disabled labels stay `--band` at reduced size, §11). |
| `--band-deep` (derived) | `#6E7482` | Taenite shadow — the pattern's second alloy line, cooled-marker mid-state | — | On `--iron` 3.42:1 — graphical and large text only. The colour an ember marker passes through as it dies (§6.3). |
| `--ember-deep` (derived) | `#9A4E1E` | Dull red heat — the cooling curve's middle third; ember at rest below the fold | — | On `--iron` 3.24:1 — graphical/data only. Heat that is leaving, printed honestly. |
| `--ember-pale` (derived) | `#E89B57` | Strike heat — the ember's peak during the strike and rekindle flare | — | On `--iron` 6.83:1. Exists for ≤1200ms at a time (§6.1, §6.8); a page found resting at this colour is overheated and fails §9. |
| `--spark` (derived) | `#F5C88F` | Spark — the strike's ejecta and struck letters' micro-bursts only | <0.1% | Momentary by law: no spark-coloured pixel may persist past its 600ms life (§6.1). Never a text or UI colour. |
| `--mirror` (derived) | `#E4E7EE` | The cold mirror — footer ground, the cooling bar's final state | footer only | Carries `--iron` text at 13.9:1. The only light surface in the theme, and it is earned by reaching the bottom. |
| `--smoke` (derived) | `rgba(200,203,212,.07)` | Polished veil — hover sheens, card light-catch | — | A tint over `--iron`/`--steel` only; never a text colour. |

**Usage discipline.** The page is mostly iron and steel —
three quarters of any viewport is the metal itself. Band and
edge are the reading voices. Ember obeys a **thermal budget**:
at the hero it may occupy up to 3% of the viewport (the strike,
the hot markers, the bar's glowing head); the budget falls with
`p` (§1) and reaches exactly 0% in the footer, where the gate
greps the rendered footer for ember-family hexes and expects
none. A build whose checkout button is ember-orange "for
conversion" has spent the heat budget on furniture and fails.

**Dark behaviour — the theme is the dark; there is no light
mode to invert to.** Meteorite Iron is a single-scheme theme:
the iron is dark at noon and at midnight. Under
`prefers-color-scheme: light` the page does **not** brighten —
a light-grey "iron" page is a photograph of iron, not iron.
The only scheme response is at the footer: under dark scheme
preference the mirror (§6.10) drops one step to `--edge` as its
ground (the mirror at night reflects less), text pairings
unchanged. A build that adds a light theme has misunderstood
the material and fails §9.

## 3. Typography

**Faces.** Archivo for display — headlines, section titles,
the struck maker's mark — in its Black (900) weight, condensed
(Archivo Expanded's opposite: `font-stretch: 78%` where the
variable font is served, else Archivo Narrow Black as the
declared fallback face). IBM Plex Mono for everything else:
body, data, apparatus, form labels, errors. The pairing is the
theme's two voices made visible: the Smith speaks in Archivo —
struck, condensed, heavy — and the Assay speaks in Plex Mono —
measured, tabular, unimpressed. No third face exists in the
theme; numerals in counters and assay lines are Plex Mono's
tabular figures, never a display font's proportional ones.

**Scale** (root 16px; the scale is in plate increments — the
forge measures type the way it measures stock, in coarse
steps):

| Role | Face | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Display (hero headline) | Archivo 900, condensed | 64px / 1.02 (≥1200px); 48px tablet; 36px mobile | −0.01em | Struck in, §6.2. Uppercase only — a maker's mark is stamped, not written. |
| Section title | Archivo 900, condensed | 34px / 1.1 | 0 | Follows its cooling marker (§6.3); never ember-coloured (§5 ration). |
| Plate heading | Archivo 800, condensed | 22px / 1.2 | 0.01em | Sub-heads inside a plate; the only Archivo below 900 weight. |
| Lead | IBM Plex Mono 400 | 18px / 1.7 | 0 | First paragraph under a headline; the Assay introducing the Smith's work. |
| Body | IBM Plex Mono 400 | 15.5px / 1.75 | 0 | Mono body is the theme's wager: the whole page reads like a lab record. Below 15.5px mono becomes a rumour — floor is law. |
| Caption / apparatus | IBM Plex Mono 500 | 12.5px / 1.6 | 0.06em, uppercase | `--band` on iron; the voice of §6.17's record. |
| Data / assay figure | IBM Plex Mono 600 | 15px, tabular | 0 | Cooling years, Ni %, lamellae widths. Figures are set, never struck (§3 law 2). |
| Maker's mark | Archivo 900, condensed | 20px | 0.04em, uppercase | In masthead and footer; dented (§6.1's treatment) wherever it appears. |

**Type laws.**
1. **The Smith strikes, the Assay measures.** Anything the
   maker is imagined to have made — the name, headlines, the
   mark — is Archivo Black, uppercase, condensed. Anything
   recorded about the work — composition, prices, dates,
   errors — is Plex Mono. A price in Archivo is a costume; a
   headline in mono is a spreadsheet.
2. **Figures are never display type.** A cooling time of
   4,000,000 years set in 64px Archivo is awe theatre (§9).
   Figures live at data size in mono, where they can be
   checked; the drama is in the number, not its point size.
3. **Uppercase is struck, sentence case is spoken.** Archivo
   headlines and the mark are uppercase (stamps are). Mono
   body and errors are sentence case — the Assay does not
   shout its records. Apparatus labels are uppercase at
   12.5px with tracking, the one licensed exception, because
   they are plate inscriptions.
4. **The dent is typographic, not decorative.** Struck type
   carries its inset shadow and per-letter depth offsets
   (§6.2) as part of its rendering, in the DOM's finished
   state — with JS off, the headline is still dented. A
   headline that is only dented while animating is a sticker.
5. **Line-height is the cooling of type.** Display 1.02 —
   letters packed like lamellae. Body 1.75 — the record
   breathes. Nothing in the theme sets below 1.6 or above
   1.8; density is a material property here, not a style.

## 4. Layout language

**Plates, not sections.** The page is a stack of iron plates.
Each plate is a full-width band of `--iron` (hero, footer
excepted per §2/§6.10) separated from the next by an etched
seam: a 1px `--steel-pale` hairline above a 24px gap in which
the Widmanstätten band pattern (§6.7) completes itself as the
plate is reached. Plates never float as cards on a background;
the page *is* the metal, edge to edge. The one exception is
the blade card (§6.13), which is a smaller plate laid on the
big one — same iron, raised 1px, polished edge catching light.

**Grid and measure.** A 12-column grid at ≥1200px with a
**132px left margin rail** carved out of it: the rail holds
the cooling bar (§6.5), the breathing ember (§6.6) and the
section markers (§6.3) — the page's instruments live in the
margin the way a smith's tools hang at the bench's edge, and
content never enters it. Body measure is 62ch of mono
(≈640px) — mono runs wide, and the measure admits it.
Tablet: rail narrows to 88px, grid 8 columns. Mobile: the
rail folds into a 44px top strip (§6.5's mobile variant) and
the grid is 4 columns; plates remain full-bleed.

**The pattern field.** The Widmanstätten texture is generated
per plate from the specimen seed (§6.17): an SVG of intergrown
bands at +60°/−60°/0° in `--steel` and `--band-deep` lines,
drawn at the lamellae width the record declares for that
plate's subject (fine octahedrite 0.2–0.5mm bands render at
6–10px pitch on screen; the drawing is a declared scale, and
§6.4's showcase states it). **The pattern never tiles.** A
repeating background tile is failure 3 in §9: real crystal
does not repeat, so each plate's field is one continuous
generated drawing, seeded, non-repeating across its area, and
different on every plate — cut from the same meteorite at a
different angle.

**Density and descent.** Density falls as the page cools:
the hero plate is dense (mark, headline, standfirst, specimen
line, tally), mid plates alternate dense etched panels with
single-object stillness (one blade, one figure, one assay
line), and the final plate before the footer holds the least
content per viewport of the page — the cold end of the process
is quiet. Whitespace in this theme is *unetched iron*: dark,
material, load-bearing. It is never "minimal"; it is the part
of the plate the acid has not touched yet.

**The descent contract.** Every page in the theme is built to
be read as a cooling: hot furniture at the top (strike, hot
markers, glowing bar head), working plates in the middle
(showcase, cards, record), one conversion plate (§6.15), and
the mirror. A page type that cannot honour the descent (a
settings screen, a dense account page) does not belong to
this theme (§1, §7).

## 5. Full motion system

Five named easings. No other easing exists in the theme; the
gate greps built CSS for them by name.

| Easing | Curve | Character | Used by |
|---|---|---|---|
| `--ease-strike` | `cubic-bezier(.2,2.0,.3,.85)` | The hammer: fast in, one overshoot as the dent rebounds 1px, hard stop | §6.1 strike, §6.2 letter landings, §6.9 dent |
| `--ease-etch` | `cubic-bezier(.65,0,.25,1)` | The acid: slow start, steady eat, no bounce — chemistry does not overshoot | §6.4 pattern draw, §6.7 etch masks, §6.16 transition |
| `--ease-drop` | `cubic-bezier(.16,1,.3,1)` | Forge weight: a heavy settle, long tail, no spring | Card entrances, plate reveals' content drop |
| `--ease-cool` | `cubic-bezier(.4,0,.2,1)` | Cooling itself: unhurried, asymptotic, the curve of a body losing heat | All temperature scrubs (§6.3, §6.5, §6.6) |
| `--ease-flare` | `cubic-bezier(.2,.9,.3,1)` | Rekindle: quick to glow, and its pair on release is `--ease-cool` at 1200ms — warming is fast, cooling is slow, always | §6.8 hover, focus warmth |

Duration tokens: `--dur-strike` 300ms; `--dur-shake` 280ms;
`--dur-spark` 600ms; `--dur-letter` 90ms (per struck letter);
`--dur-etch-band` 600ms; `--dur-drop` 650ms; `--dur-flare`
300ms; `--dur-cool-long` 1200ms; `--dur-turn` 700ms (page
transition).

**Every motion term, in this theme's language:**
- **Scroll-triggered reveals** are etchings (§6.7): the
  pattern eats in from a plate's edges over 600ms
  `--ease-etch` while content drops 8px into place on
  `--ease-drop`. Trigger: plate's top crosses 78% of viewport.
- **Scroll-scrubbed animation** is cooling (§6.3, §6.5, §6.6):
  all scrubbed values derive from `p`, the max-depth function
  (§1), driven by the one shared rAF loop at lerp **0.085** —
  the heaviest smoothing in the library, because iron does
  not hurry. Scrubbing to live position instead of max-depth
  is the law broken (§1).
- **Parallax** is the etched panel against its polished edge:
  pattern field translates at 0.92× scroll, the polished-edge
  highlight line at 1.06×, re-converging at each plate seam —
  a ±14px maximum differential, so the plate reads as one
  object with depth, never as layers sliding apart.
- **Pinned scenes:** exactly one per page — the etching
  showcase (§6.4), 140vh of pin. A second pin is a second
  forge, and the theme has one forge.
- **Masked reveals** are the etch mask itself (§6.7) and the
  struck headline's dent mask (§6.2). No clip-path wipes, no
  curtain lifts: masks in this theme are chemical or physical.
- **Blur-to-sharp is refused.** Hot iron glows; it does not
  blur. Images arrive by scale-in-frame (§6.13) and the
  pattern by line-draw. A blurred reveal reads as camera
  trickery in a theme whose camera is a workbench.
- **Kinetic typography is refused** beyond the struck letters
  (§6.2): type that dances is type that was not hammered.
  The headline is *made*, once, at load; it does not perform
  again.
- **Animated counters** are formation counters (§6.14):
  they count once, upward, to figures from the record, and
  stop. A counter that re-runs on scroll-back is reheating
  (§1).
- **Progress** is the cooling bar (§6.5) and nothing else:
  no bars, no percentages of reading, no step dots. The bar
  *is* a temperature history.
- **Marquees are refused.** Nothing in a forge scrolls
  sideways forever. The footer's light crawl (§6.10) happens
  once and rests.
- **Ambient loops:** exactly one — the breathing ember
  (§6.6), and it is designed to die. Any second loop (a
  pulsing badge, a shimmering button) is a second fire in a
  page whose story is the fire going out.
- **Micro-interactions:** rekindle (§6.8), strike click
  (§6.9), card tilt-to-light (§6.13), the stamp-press on
  buttons (§11). Each leaves the surface changed or warmed —
  no interaction in this theme is weightless.
- **Hover physics:** tilt is capped at 3° and pivots like a
  blade turned on a bench, not a card floating in space;
  shadows are hard offsets (the plate's edge shadow), never
  soft glows.
- **Page transitions** are the strike transition (§6.16): a
  white spark flash ≤120ms and the new page lands already
  dented and still — transitions arrive *cold*, because the
  strike belongs to the first page of a session only.
- **Smooth scrolling** is the shared loop's lerp on scrubbed
  values only; native scroll is never hijacked. Anchor jumps
  are instant (a smith does not glide across the bench), and
  landing deep in a page sets `p` honestly to the depth
  reached — the page arrives at the temperature of where you
  are in it (§6.5's jump rule).

**The strike census.** Per session: one forge strike (§6.1),
one letters ceremony (§6.2), sparks only from those two and
from deliberate clicks (§6.9). The gate counts spark emitters
in the built page. Confetti physics, hover sparkles and
scroll-triggered bursts are failures, however pretty: in this
theme a spark is struck metal leaving the work, and metal is
not spent on decoration.

## 6. Signature elements

### 6.1 The forge strike

- **What & why.** On first load, after 300ms of complete
  stillness, the page is struck once: the viewport shakes 3px
  for ≤280ms with a hard decay, a ring of ~16 ember sparks
  flies from the headline's centre and dies within 600ms, and
  the headline (§6.2) is revealed already dented into the
  plate. It belongs because the page's first event should be
  its manufacturing process: this site was not loaded, it was
  forged, and the strike is the only loud moment the theme
  permits itself — everything after it is cooling.
- **Structure.** The hero plate ships complete in the DOM:
  headline dented (inset shadow + per-letter offsets are CSS,
  §6.2), sparks absent. JS arms the strike by adding a
  `.pre-strike` class that *un-dents* nothing — the shake and
  sparks are an overlay performance on an already-finished
  plate. Sparks are one `<canvas>` (fixed, hero-sized,
  `pointer-events:none`, `aria-hidden`) or 16 absolutely
  positioned 2px divs where canvas is unavailable; the shake
  is a transform on the hero plate only, never on `<body>`
  (layout must not move under the reader's other content).
- **Motion spec.** Trigger: load, once per session
  (`sessionStorage` flag `mi-struck`), at t=300ms after first
  paint or `document.fonts.ready`, whichever is later, capped
  at t=900ms. Shake: 280ms, keyframes 3px → −2px → 1px → 0,
  `--ease-strike` segments, transform only. Sparks: 16 ± 3,
  radial from the headline's optical centre, velocities
  60–260px/s with gravity 480px/s², colour `--spark` cooling
  to `--ember` across their 600ms life, size 2px → 0. At
  t=600ms the canvas is cleared and removed from the DOM.
- **States.** Unstruck (first paint, plate complete and
  readable) → striking (280ms) → struck (rest state for the
  session). Hover/focus: none — the strike is not a control.
  Returning visitor: no strike; the page opens struck, cold
  and still (its §6.16 arrival state).
- **Content merge.** The strike lands on the headline, which
  is the maker's name — the brand is the workpiece. Nothing
  else on the page shakes, flashes or performs; the violence
  is precisely located, like a real hammer blow.
- **Failure fallback.** Watchdog at 1200ms from arming: if
  the strike has not run (rAF starved, tab backgrounded), the
  arming class is removed and the session flag set — the
  plate simply stands struck, which it always was in the
  DOM. No JS: no strike, no loss; the hero reads complete.
- **Reduced-motion variant.** No shake, no sparks, ever. The
  page opens struck and still. The information (this was
  made by impact) survives in the dented type (§6.2); only
  the blow rests.
- **Performance budget & mobile variant.** Canvas ≤ 20KB of
  code+draw, one 600ms burst, zero ongoing cost; sparks are
  the only canvas on the page. Mobile (<768px): shake
  amplitude 2px, sparks 10, same timings — a phone is struck
  more gently because it is held in the hand that feels it.
- **Choreography timeline (v2).** t=0 first paint (plate
  complete) → fonts ready, ≤900ms → t=300ms stillness ends →
  shake 280ms (3px peak at t≈360ms) → sparks emit t=300–380ms
  → sparks die by t=980ms → canvas removed t=1000ms →
  §6.2's letters settle completes underneath the shake (its
  own timeline) → t=1200ms watchdog deadline passes unused.
- **State matrix (v2).** *Rest:* struck plate, no motion.
  *Hover:* none. *Focus:* focus landing in the hero before
  t=300ms cancels the shake (a keyboard visitor is never
  shaken) but sparks still fire, dimmed 50%. *Active:* n/a.
  *Scrolled-past:* strike already spent; never replays on
  return. *Disabled / no-JS:* plate stands complete. *Touch:*
  identical; the first touch before t=300ms cancels the shake
  (the hand holding the phone has already felt enough).
- **Breakpoints (v2).** ≥1200px: 3px shake, 16 sparks.
  768–1199px: 3px, 14 sparks. <768px: 2px, 10 sparks, canvas
  height = hero height only.
- **Edge cases & failure modes (v2).** *Slow network:* the
  strike waits for fonts (masks and letterforms must be
  true) but the 900ms cap ships it in a fallback face rather
  than hold the page hostage. *Tab hidden at load:* rAF
  never fires; on first visibility the watchdog has already
  settled the plate — no strike erupts belatedly at the
  returning visitor. *Canvas blocked:* div-spark fallback;
  if that fails, shake alone; if transforms fail, nothing —
  each layer degrades independently. *Repeat visits within
  session:* flag suppresses entirely.
- **Accessibility spec (v2).** The shake is a transform on a
  decorative-timed overlay of already-readable content; the
  headline is in the accessibility tree, complete, from
  first paint. Nothing is announced. `prefers-reduced-motion`
  and `prefers-reduced-transparency` both suppress the whole
  ceremony. Vestibular safety: 3px/280ms is under common
  thresholds, and the reduced-motion variant removes it
  outright.
- **Tokens consumed (v2).** `--iron`, `--spark`, `--ember`,
  `--ease-strike`, `--dur-strike` (300ms), `--dur-shake`
  (280ms), `--dur-spark` (600ms).

### 6.2 Struck-in letters

- **What & why.** The hero headline's letters land one at a
  time, 70ms apart, each with its own micro-burst of 3–5
  sparks and a 2px dent settle — hammer blows spelling the
  name. It belongs because in this theme typography is not
  typeset but *made*: the visitor watches the mark being
  struck into the plate letter by letter, and a name that was
  forged in front of you carries its provenance in its
  letterforms for the rest of the page.
- **Structure.** A real `<h1>` in Archivo 900 condensed,
  full text in the DOM at full contrast from first paint.
  JS wraps each glyph in a `<span class="ltr">` (aria-hidden
  duplicates avoided by keeping the original text in an
  sr-only node and marking the wrapped copy `aria-hidden`),
  each span carrying its authored dent: `text-shadow: 0 1px 0
  rgba(200,203,212,.14), inset…` rendered as a two-layer
  effect — a `--steel` offset copy 1px down-left beneath the
  `--edge` face, giving the letter a struck depth of exactly
  1px. Per-letter depth offsets vary ±0.5px by an authored
  table (a hand struck them; no two blows are identical).
  The dent is present in the finished CSS state — JS only
  animates the *arrival*, never the dent itself (§3 law 4).
- **Motion spec.** Trigger: sequenced with §6.1 — first
  letter lands with the strike at t=300ms. Each letter:
  translateY −6px → 0 with a 2px overshoot dent over 90ms
  `--ease-strike`, staggered 70ms; micro-sparks 3–5 per
  letter from the letter's baseline, 300ms life, `--spark`
  cooling to transparent. An 8-letter name completes at
  300 + 7×70 + 90 = 880ms. Headlines longer than 14 glyphs
  compress the stagger to fit a 1400ms cap; longer than 22
  glyphs is refused at build time (§12 — a mark is a name,
  not a sentence).
- **States.** Unlanded (JS-armed only: letters at −6px,
  opacity 1 — letters are never invisible, only *unstruck*,
  held 1px proud of the plate) → landing (per-letter) →
  struck (rest; dented, still). Hover: none. Scrolled-past
  mid-ceremony: the sequence completes on its own clock.
- **Content merge.** The ceremony is the headline's own
  manufacture, not an intro screen: the standfirst, specimen
  line and tally (§6.12) are already readable beneath it
  while the name is being struck above them.
- **Failure fallback.** Watchdog at 1600ms: any letter not
  yet landed snaps to its struck state and remaining sparks
  are cancelled. No JS: the `<h1>` stands dented and
  complete — the dent is CSS, the ceremony is the only JS.
- **Reduced-motion variant.** No landings, no sparks. The
  headline stands struck at first paint, dent and all.
- **Performance budget & mobile variant.** Spans and shadows
  only; spark bursts share §6.1's single canvas. Total
  added DOM ≤ 22 spans. Mobile: stagger 55ms, micro-sparks
  2–3 per letter, same cap.
- **Choreography timeline (v2).** t=300ms strike (§6.1) +
  letter 1 lands → +70ms per letter → last letter lands ≤
  t=1400ms → its sparks die +300ms → t=+200ms after last
  letter, §6.12's specimen line etches in (§6.7's border
  band, 600ms) → ceremony closed; the hero is at rest and
  already cooling (§6.3 begins from p=0 heat).
- **State matrix (v2).** *Rest:* struck, dented, still.
  *Hover:* none (the headline is not a control). *Focus:*
  focus entering the hero completes the sequence instantly.
  *Active:* n/a. *Scrolled-past:* completed; returning shows
  the finished mark. *Disabled / no-JS:* printed struck.
  *Touch:* identical; first touch completes a running
  sequence.
- **Breakpoints (v2).** ≥1200px: 64px, 70ms stagger.
  768–1199px: 48px, 62ms. <768px: 36px, 55ms, sparks 2–3.
- **Edge cases & failure modes (v2).** *Font swap after
  arming:* letters arm only after `document.fonts.ready`;
  a late swap disarms to the printed headline rather than
  land letters in two faces. *Edited headline in a CMS:*
  dent offsets are keyed by index with a seeded default —
  an edited name still strikes plausibly, never misaligns.
  *RTL text:* landing order follows reading order (the
  hammer works the way the language reads). *Very long
  word:* stagger compresses per the cap formula; the cap
  wins over the stagger, always.
- **Accessibility spec (v2).** Screen readers receive the
  plain `<h1>` text once, from first paint; the wrapped
  copy is `aria-hidden`. The ceremony is never announced
  and never delays content availability — the sr-only text
  and the visible base are the same words at the same time.
  Contrast is `--edge` on `--iron` 10.88:1 at every frame;
  letters are never rendered below full opacity.
- **Tokens consumed (v2).** `--edge`, `--steel`, `--spark`,
  `--ember`, `--ease-strike`, `--dur-letter` (90ms).

### 6.3 Cooling section markers

- **What & why.** Every section marker — the numbered
  inscription at each plate's head, which is also the
  navigation's current-position furniture — carries an ember
  dot that begins forge-orange at the hero and cools to cold
  steel grey by the footer, interpolated across the page's
  descent. It belongs because the navigation furniture should
  undergo the meteorite's own story: millions of years of
  cooling, compressed into one read, told by the page's most
  ordinary element.
- **Structure.** Each plate head carries
  `<div class="marker">` with a mono apparatus label
  (`PLATE 03 — THE ASSAY`), a 10px ember dot (div, border-
  radius 50%), and the section title (§3). The dot's colour
  is a single CSS custom property `--temp` written by the
  shared rAF loop: colour = the declared cooling curve
  (§6.5's function) evaluated at `p`, mapped through three
  stops — `--ember` (p<0.3) → `--ember-deep` (0.3–0.65) →
  `--band-deep` → `--steel-pale` (p>0.85). All markers share
  the one `--temp`; markers never have individual
  temperatures (one body, one temperature — §1).
- **Motion spec.** Trigger: the shared loop, continuous.
  Colour transitions are scrubbed by the loop at lerp 0.085
  on `--ease-cool`'s curve; a full-page descent cools a
  marker over the whole read — there is no per-marker
  duration, only the page's. A marker entering view for the
  first time etches its plate in (§6.7) but its dot is
  already at page temperature: it does not flare on arrival
  (arrival is not heat; §5 census).
- **States.** Hot (hero plates) → cooling (mid) → cold
  (final plates, dot `--steel-pale`, glow 0). The current
  plate's marker additionally carries the breathing ember's
  relay (§6.6 passes its pulse to the current marker at
  ≥1200px). Hover/focus: §6.8's rekindle. Scrolled-past:
  markers keep page temperature — scrolling up does not
  reheat them (§1 law).
- **Content merge.** The marker *is* the plate's head and
  the nav's anchor; its cooling is not a widget beside the
  content but the title block itself changing state, the way
  the metal at the top of a cooling ingot is the same metal
  as at the bottom, at a different hour of its life.
- **Failure fallback.** No JS: markers render at a fixed
  mid-cool state (`--ember-deep` dots, printed statically) —
  the page reads as a photograph of the cooling at its
  middle hour, complete and honest. Loop failure: the
  watchdog (§6.5) freezes `--temp` at its last value; dots
  remain visible at *a* temperature, never invisible.
- **Reduced-motion variant.** Markers step through four
  discrete temperatures at plate boundaries (no continuous
  scrub): hot / dull / grey / cold, applied instantly as
  each plate is passed. The information — descent is
  cooling — survives intact.
- **Performance budget & mobile variant.** One custom
  property write per frame, shared by all markers; colour
  interpolation in CSS via `color-mix` steps precomputed at
  32 stops (no per-frame JS colour maths). Mobile: dots
  shrink to 8px and move inline before the apparatus label
  (the rail is folded, §4); the curve is unchanged.
- **Choreography timeline (v2).** Continuous from t=0:
  p=0, dots `--ember` with 6px glow → p=0.3, glow 0,
  `--ember-deep` → p=0.65, `--band-deep` → p=0.85,
  `--steel-pale` → p=1 (footer), dots match the bar's
  mirror end (§6.5) exactly — marker and bar are two
  printings of one temperature and the gate samples both.
- **State matrix (v2).** *Rest:* at page temperature.
  *Hover:* rekindle (§6.8): +1 stop hotter for 300ms,
  decay 1200ms back to page temperature. *Focus:* same as
  hover, plus the marker's plate link gets the focus ring
  (§11). *Active:* n/a. *Scrolled-past:* holds temperature
  (max-depth law). *Disabled:* markers are not controls;
  the nav links within them disable per §11. *Touch:* no
  hover rekindle; a tap on the marker's link is navigation,
  not warmth.
- **Breakpoints (v2).** ≥1200px: 10px dot in the rail,
  label beside it. 768–1199px: 9px dot, label wraps under
  the title. <768px: 8px dot inline in the plate head; the
  rail copy is hidden (the top-strip bar, §6.5, carries
  temperature alone).
- **Edge cases & failure modes (v2).** *Short page*
  (fewer than 3 plates): the curve compresses — p still
  spans the page, so a two-plate page cools fully by its
  footer; the law is about the page's own length, not an
  absolute metre count. *Anchor jump to the footer:* p
  jumps honestly; markers land cold instantly (the loop's
  lerp is bypassed for jumps >40% of page height — you
  teleported the ingot, it arrives at destination
  temperature). *Print:* markers print at mid-cool state.
- **Accessibility spec (v2).** Dots are decorative
  (`aria-hidden`); temperature is never the only carrier of
  position — the apparatus label names the plate in text
  and the nav (§6.11) carries `aria-current`. Dot colour is
  never used to convey a state a screen reader needs. The
  marker link targets are ≥44px tall including the label.
- **Tokens consumed (v2).** `--ember`, `--ember-deep`,
  `--band-deep`, `--steel-pale`, `--band`, `--ease-cool`.

### 6.4 The etching showcase

- **What & why.** The hero product's plate pins for ~140vh
  while the Widmanstätten cross-hatch etches itself, line by
  line, across the blade photograph's own panel — band angles
  alternating +60°/−60° as real kamacite and taenite lamellae
  intergrow. It belongs because the pattern is the product's
  entire claim to singularity, and the theme refuses to state
  that claim in copy alone: the visitor watches the crystal
  form *on the blade itself*, at the speed of their own
  scroll, the way it formed at the speed of an asteroid's
  cooling — the page's central argument performed, not
  described.
- **Structure.** A pinned plate (§4's one licensed pin)
  containing the product photograph (real `<img>`, the blade
  on iron, §6.13's frame treatment) with an SVG overlay the
  exact size of the photo's panel: generated lamellae paths
  from the specimen seed (§6.17), band pitch = the record's
  declared lamellae width at the panel's stated scale
  (printed in the apparatus line: "PATTERN AT 12:1 — BANDS
  0.3 MM"). Each path carries `pathLength=1` and is drawn by
  `stroke-dashoffset` scrubbed to pin progress. Beside the
  panel, the assay column (§6.17's lines for this piece)
  stands static — the record does not perform; only the
  crystal does.
- **Motion spec.** Trigger: pin progress q ∈ [0,1] across
  140vh of scroll (240vh of travel at ≥1200px total plate
  height). Bands draw in formation order — the pattern grows
  from the panel's top-left nucleus outward, kamacite bands
  (+60°) in q 0→0.55, taenite (−60°) interleaving q
  0.3→0.85, cross-bands (0°) q 0.7→1 — because a crystal
  grows, it does not fade in. All values from the shared
  loop (lerp 0.085). The photograph beneath scales
  1.04→1.0 across the same q (scale-in-frame, §5). At q=1
  the pin releases; the completed pattern stays, printed on
  the blade for the rest of the page's life.
- **States.** Unetched (JS-armed only: overlay paths at
  dashoffset 1; photo fully visible beneath — the blade is
  never hidden by its unformed pattern) → etching (scrubbed,
  fully reversible *within* the pin: scrolling back up
  inside the pin un-draws, the one licensed reversal in the
  theme, because formation here is being *demonstrated*,
  and a demonstration may rewind; once the pin is exited
  downward, the pattern is formed and §1's law locks it) →
  etched (rest). Hover: none (the panel is not a control).
- **Content merge.** The pattern forms over the actual
  product photograph, aligned to the blade's geometry in
  the photo (the overlay is authored per product image,
  bands following the blade's flat) — not a texture behind
  text, but the object's own surface developing. The assay
  column beside it names what is forming while it forms.
- **Failure fallback.** Watchdog: if the loop stalls >900ms
  mid-pin, all paths snap to their q-complete state for the
  current scroll position. No JS / no pin support: the
  overlay ships fully drawn in the DOM (dashoffset 0) — the
  blade arrives already etched, the argument made
  statically. Reduced-motion: no pin; pattern printed
  complete; the scale statement remains.
- **Reduced-motion variant.** As fallback: static etched
  panel, no pin, no scrub. The photograph at scale 1.0.
- **Performance budget & mobile variant.** Overlay ≤ 90
  paths, dashoffset writes batched per frame from the loop;
  the pin uses `position: sticky`, never JS scroll-jacking.
  Mobile (<768px): pin shortens to 100vh, band count halves
  (every second lamella — the pitch doubles and the
  apparatus line states the mobile scale honestly), assay
  column moves beneath the panel.
- **Choreography timeline (v2).** Pin engages (plate top
  hits viewport top) → q=0.0–0.15 photo settles 1.04→1.02,
  first kamacite nucleus strokes → q=0.3 taenite begins
  interleaving → q=0.55 kamacite complete → q=0.7 cross-
  bands begin → q=0.85 taenite complete → q=1.0 pattern
  complete, apparatus line "ETCHED" state inks (§6.17) →
  pin releases; from here the pattern is locked by §1.
- **State matrix (v2).** *Rest (pre-pin):* photo visible,
  pattern unetched overlay armed. *Hover:* none. *Focus:*
  focus entering the plate skips the pin (scroll anchoring
  yields; pattern completes instantly) — a keyboard visitor
  is never trapped in 140vh of scrub. *Active:* n/a.
  *Scrolled-past:* etched, locked. *Disabled / no-JS:*
  printed etched. *Touch:* identical scrub; fling scroll
  catches up via the loop's jump rule (§6.3).
- **Breakpoints (v2).** ≥1200px: 140vh pin, full band count,
  assay column right. 768–1199px: 120vh pin, full bands,
  assay column right at narrower measure. <768px: 100vh
  pin, half bands, doubled pitch stated, assay below.
- **Edge cases & failure modes (v2).** *Image fails to
  load:* the panel shows the etched pattern over `--steel`
  with the photo's alt as a printed apparatus line — the
  pattern argument survives the photograph. *Pattern seed
  missing from the record:* build fails (§15) — the
  showcase may not invent a crystal. *User resizes mid-pin:*
  q recomputes from geometry; paths hold their drawn
  fraction. *Browser without sticky:* plate renders unpinned
  with the pattern at the visitor's plate-progress fraction
  — degraded, never broken.
- **Accessibility spec (v2).** The overlay SVG is
  `aria-hidden`; the photograph's alt names the blade and
  states "its Widmanstätten pattern etched across the flat".
  The apparatus scale line is real text. Pin behaviour is
  announced nowhere and traps nothing: scroll and focus
  both pass through freely, and the focus-skip rule above
  guarantees keyboard parity.
- **Tokens consumed (v2).** `--steel`, `--band-deep`,
  `--band`, `--edge`, `--ease-etch`, `--dur-etch-band`.

### 6.5 The cooling bar

- **What & why.** In the margin rail, a vertical strip that
  begins as a glowing ember bar and cools section by
  section — orange → dull red → steel → mirror — etching
  one cross-hatch segment per section completed. It is the
  theme's only progress indicator, and it belongs because
  progress in this world is not a percentage of tasks but a
  temperature history: the reader's journey *is* the
  crystal's formation time, and the bar is the ingot they
  are cooling by reading.
- **Structure.** A 6px-wide, rail-height strip (fixed
  within the rail, §4) divided into one segment per plate
  (DOM-counted from the plates themselves — a page with 7
  plates has 7 segments; the bar cannot disagree with the
  page). Each segment is a div with a cross-hatch background
  (two repeating-linear-gradients at ±60° in `--steel-pale`)
  revealed as its plate completes. The strip's fill colour
  is the same `--temp` property §6.3's markers consume —
  one temperature, two instruments. Beneath the strip, the
  Assay prints the current temperature as a figure:
  `T(p) = 18 + 1132·(1−p)^2.2` °C, rounded to whole degrees
  — 1,150°C at the hero, 18°C at the footer — the declared
  curve, printed where it is used (§1 law 2).
- **Motion spec.** Trigger: shared loop. Segment etches
  when its plate's foot crosses 55% of viewport: hatch
  opacity 0→1 over 600ms `--ease-etch`, and the segment's
  colour locks at the temperature of that moment (segments
  are a *record*: a segment etched early stays warmer in
  the bar's history than one etched late — the bar is a
  core sample of the read). The live head (current segment)
  follows `--temp` continuously. Temperature figure updates
  at most 4×/second, tabular mono, crossfading digits (no
  rolling counters — §5).
- **States.** Hot (head glowing, 0 segments) → cooling
  (segments etching, head dulling) → cold (all segments
  etched, head `--mirror`-bright steel, figure 18°C).
  Hover on the bar: the figure expands to show the curve's
  name ("COOLING CURVE — DECLARED, §6.17") — information,
  not warmth; the bar does not rekindle (§6.8 is for
  markers and cards only). Scrolled-past: the record
  stands; scrolling up changes nothing (§1).
- **Content merge.** The bar's segments *are* the page's
  plates, counted from the DOM; its temperature is the same
  value the markers wear and the footer prints. Remove the
  content and the bar has nothing to say — it is an
  instrument of the page, not a widget on it.
- **Failure fallback.** No JS: the bar renders fully etched
  in `--steel` with the figure line reading "TEMPERATURE —
  PRINTED AT REST" and no number (a number without the
  measurement would break §1 law 2). Loop failure: watchdog
  freezes the bar at its last true state.
- **Reduced-motion variant.** Segments etch instantly at
  their triggers; the figure steps discretely. The bar's
  record-keeping is unchanged.
- **Performance budget & mobile variant.** One property
  write + ≤7 segment class toggles per page; figure updates
  throttled. Mobile: the bar becomes the 44px top strip
  (§4) — horizontal, 4px tall, segments left→right, figure
  at the strip's right end at 11px; same curve, same law.
- **Choreography timeline (v2).** p=0: head `--ember`,
  figure 1150° → each plate foot at 55%: segment etches
  600ms, locks its colour → p≈0.5: head `--ember-deep`,
  figure ≈210° → final plate: last segment etches → p=1:
  head cools to mirror steel over 1200ms `--ease-cool`,
  figure settles 18° → the footer's own line (§6.10) prints
  the same 18° — two instruments, one reading, gate-checked.
- **State matrix (v2).** *Rest:* recording. *Hover:*
  curve-name expansion (desktop only). *Focus:* the bar is
  not focusable; its figure is reachable as text in the
  rail's reading order. *Active:* n/a. *Scrolled-past:*
  record stands. *Disabled / no-JS:* printed at rest (see
  fallback). *Touch:* no hover expansion; the curve name is
  printed permanently under the mobile strip at 10px.
- **Breakpoints (v2).** ≥1200px: vertical rail bar, 6px,
  figure beneath. 768–1199px: vertical, 5px, figure rotated
  out (apparatus label carries "COOLING" only; figure moves
  to the footer record). <768px: horizontal top strip as
  above.
- **Edge cases & failure modes (v2).** *Plate added in a
  CMS:* segments recount from the DOM on load — the bar
  self-corrects; a hard-coded segment count is a build
  failure (§15). *Anchor jump:* segments for all plates
  above the landing point etch instantly, locked at the
  landing temperature (the record notes the jump honestly:
  they were not read hot, they were arrived at cold).
  *Very long page (>14 plates):* segments thin to 3px
  minimum height; beyond 20 plates the bar groups plates
  in pairs and the apparatus says so.
- **Accessibility spec (v2).** The bar is `role="img"` with
  an aria-label updated at plate boundaries only: "Cooling:
  plate 3 of 7 passed, 412 degrees" — throttled, polite,
  never per-frame. The figure is real text. Colour is never
  the sole carrier: segment count and the printed figure
  carry the same information in countable form.
- **Tokens consumed (v2).** `--ember`, `--ember-deep`,
  `--band-deep`, `--steel-pale`, `--mirror`, `--ease-cool`,
  `--ease-etch`, `--dur-etch-band` (600ms).

### 6.6 The breathing ember

- **What & why.** One margin ember pulses slowly — a 4s
  opacity/glow cycle — beside the current section, and it is
  the theme's only ambient loop. As sections pass, its pulse
  slows and its colour dulls; at the footer it is dead cold
  and still. It belongs because a forge page needs exactly
  one living coal to prove the fire was real, and its slow
  death is the page's emotional plot told in a single dot:
  everything the visitor reads is read by the light of a
  fire that is going out on schedule.
- **Structure.** One 12px div in the rail (§4), positioned
  beside the current plate's marker (§6.3) by the shared
  loop (transform translateY to the active marker's offset,
  lerped at 0.085 — the ember *travels* the rail as the read
  descends, settling beside each new current plate over
  ~800ms). Pulse: a CSS keyframe on opacity/glow whose
  `animation-duration` and colour are set from `--temp`:
  cycle = 4s at p=0 lengthening to 9s at p=0.8; colour from
  the §6.3 curve. At p≥0.92 the animation is removed
  entirely and the ember renders `--steel-pale`, still — a
  stopped loop, not a paused one.
- **Motion spec.** Trigger: time loop + scroll state,
  continuous. Pulse amplitude also decays: glow radius 10px
  at p=0 → 0 at p≥0.85. The ember never brightens beyond
  page temperature (it is the page's coal, not a beacon):
  its peak colour each cycle is exactly `--temp`.
- **States.** Breathing (hot plates) → slowing (mid) →
  still (p≥0.92) → absent (footer: the rail ends, and the
  ember's final position is beside the last marker, cold).
  Hover: the ember does not respond — it is not a control
  and does not perform for attention (§5 census).
  Scrolled-past: its history is its position; it never
  travels back up the rail (§1: max-depth governs).
- **Content merge.** The ember sits beside the *current
  section's* marker — it is the reading position made
  thermal. It marks where in the cooling the visitor
  currently stands, the way a smith's last coal marks where
  the work stopped.
- **Failure fallback.** No JS: no ember (a breathing dot
  printed statically would be a lie about a loop that is
  not running; the markers' printed mid-cool state, §6.3,
  carries the story instead). Loop failure: the watchdog
  stops the pulse at its current frame — a still ember at a
  true temperature.
- **Reduced-motion variant.** No pulse, no travel: the
  ember is a static dot at the current plate's marker,
  stepping discretely between plates at page temperature.
  At the footer plates it is already cold.
- **Performance budget & mobile variant.** One element, one
  keyframe, two property writes per frame from the loop —
  the cheapest ambient loop in the library, by design.
  Mobile: the ember is cut (the top strip, §6.5, has no
  room for a coal, and a pulsing dot in a 44px strip would
  be a notification badge — §9). Its information (current
  plate) survives in the strip's figure.
- **Choreography timeline (v2).** t=0: ember beside marker
  1, 4s cycle, full glow → each plate change: travel 800ms
  to the new marker, cycle lengthens per the curve → p=0.8:
  9s cycle, glow 2px → p=0.92: pulse stops mid-fade
  wherever it stands (a coal does not finish its breath
  politely) → footer: cold, still, beside the last marker.
- **State matrix (v2).** *Rest:* breathing at page
  temperature. *Hover:* none. *Focus:* when focus enters a
  plate (keyboard navigation), the ember steps to that
  plate's marker instantly — focus is a position, and the
  ember marks position. *Active:* n/a. *Scrolled-past:*
  holds its deepest position. *Disabled / no-JS:* absent.
  *Touch:* absent on mobile; on touch tablets ≥768px it
  behaves as desktop but never pulses while a finger is
  down (the hand is on the page; the coal waits).
- **Breakpoints (v2).** ≥1200px: full treatment in the
  rail. 768–1199px: ember present, travel steps discretely
  (the narrower rail makes gliding read as drift).
  <768px: cut (see mobile variant).
- **Edge cases & failure modes (v2).** *Hidden tab:* the
  keyframe pauses (browser-native); on return it resumes
  at page temperature — the coal did not burn while nobody
  watched, and the fiction allows it because temperature
  is scroll-governed, not clock-governed (§1). *Plate
  heights change (late images):* the ember's target offset
  recomputes; it glides to the corrected marker without a
  pulse reset. *Reduced data / low power:* the pulse is
  the first thing §14 cuts — the ember becomes §6.3's
  static relay.
- **Accessibility spec (v2).** `aria-hidden`, no live
  region, no role. It conveys nothing that the marker
  labels and bar figure (§6.5) do not convey in text. Its
  pulse respects `prefers-reduced-motion` absolutely, and
  at 4–9s per cycle it is far outside photosensitivity
  ranges in any case.
- **Tokens consumed (v2).** `--ember`, `--ember-deep`,
  `--band-deep`, `--steel-pale`, `--ease-cool`.

### 6.7 Etch-mask section reveals

- **What & why.** Each plate is revealed by its own
  cross-hatch pattern eating in from the plate's edges —
  stroke-drawn border bands completing over ~600ms — while
  the plate's content settles with a forge-weight drop. It
  belongs because the reveal process should be the
  pattern-forming process: a chapter is not *shown*, it is
  etched into the plate as the reader reaches it, and what
  the acid has not yet eaten stays honestly unetched rather
  than theatrically hidden.
- **Structure.** Each plate carries an SVG border frame
  (four band strips, top/bottom/left/right, generated from
  the plate's pattern seed at a coarse pitch — the reveal
  bands are the pattern at 3× scale, so the frame and the
  plate's field (§4) are visibly the same crystal). Paths
  ship at dashoffset 0 (drawn) in the DOM; JS arms them to
  dashoffset 1 only for plates below the fold at load.
  Content drop: the plate's inner wrapper ships at
  translateY(0); JS arms it to −8px only when arming its
  frame, so content is never displaced without its frame.
- **Motion spec.** Trigger: plate top crosses 78% of
  viewport (IntersectionObserver, rootMargin pre-arms at
  120%). Frame: bands draw from the corners inward over
  600ms `--ease-etch`, staggered 60ms per side (top, right,
  bottom, left — the acid works around the plate). Content:
  8px drop over 650ms `--ease-drop`, starting at t=150ms
  (the frame leads, the content settles into it). Etching
  is permanent: a plate, once etched, never un-etches
  (§1's law applied to formation).
- **States.** Unetched (below-fold, JS-armed only) →
  etching (600ms) → etched (rest, permanent). Hover/focus:
  none. Scrolled-past quickly: plates flung past etch
  instantly at their trigger (the observer fires; durations
  compress to 0 for plates already above the viewport — the
  acid caught up while you weren't looking, and the record
  does not pretend otherwise).
- **Content merge.** The frame is the plate's own pattern,
  and the content it reveals is the plate's own text and
  objects — the reveal is the plate manufacturing its
  border, not a curtain over a stage. Nothing outside the
  plate is involved.
- **Failure fallback.** Watchdog per plate: 1000ms after
  its trigger, any incomplete band snaps to drawn. No JS:
  every frame ships drawn; the page is a finished etching,
  complete at first paint. Observer unsupported: all plates
  etch at load in document order over one 600ms pass.
- **Reduced-motion variant.** Frames printed drawn; content
  at rest. No plate ever waits for a reveal ceremony.
- **Performance budget & mobile variant.** ≤ 16 paths per
  plate frame, dashoffset only. Mobile: the side bands are
  cut (frame = top and bottom bands only — a phone-width
  plate has no room for etched margins, and the pattern
  field, §4, carries the texture alone); duration 450ms.
- **Choreography timeline (v2).** Plate top at 120%
  viewport: armed → at 78%: t=0 top band draws → t=60ms
  right → t=120ms bottom → t=150ms content drop begins →
  t=180ms left band → t=600ms frame complete → t=800ms
  content settled → plate's marker (§6.3) is already at
  page temperature throughout — etching is formation, not
  heating.
- **State matrix (v2).** *Rest:* etched. *Hover:* none.
  *Focus:* focus entering an unetched plate etches it
  instantly (a keyboard visitor never reads inside an
  unfinished frame). *Active:* n/a. *Scrolled-past:*
  etched, permanently. *Disabled / no-JS:* drawn at first
  paint. *Touch:* identical; fling-scroll uses the
  instant-etch catch-up rule.
- **Breakpoints (v2).** ≥1200px: four bands, 600ms.
  768–1199px: four bands at 80% pitch, 550ms. <768px: two
  bands, 450ms.
- **Edge cases & failure modes (v2).** *Plate taller than
  200vh:* the frame etches on entry as normal — the frame
  is the plate's head, not its whole perimeter at that
  scale; side bands cap at 160vh length and the apparatus
  does not claim otherwise. *Content loaded late into a
  plate (CMS):* new plates arm on insertion via the same
  observer. *Print:* all frames print drawn.
- **Accessibility spec (v2).** Frames are `aria-hidden`
  decoration around real content that is never hidden,
  dimmed or delayed for assistive technology: the DOM
  order and readability are identical armed or unarmed.
  The drop is 8px of transform on a wrapper — no focusable
  element changes position by more than its own height,
  and focus-skip (above) prevents focus ever landing in a
  moving plate.
- **Tokens consumed (v2).** `--steel`, `--band-deep`,
  `--steel-pale`, `--ease-etch`, `--ease-drop`,
  `--dur-etch-band` (600ms), `--dur-drop` (650ms).

### 6.8 Ember-rekindle hover

- **What & why.** Hovering or focusing a section marker or
  a blade card briefly rekindles its ember: a glow flare
  over 300ms, decaying over 1.2s, and the card's polished
  edge brightens. It belongs because attention is heat —
  touching steel warms the spot you touch — and because
  §1's one-way law needs its single licensed exception to
  be *physical*: warmth that comes from a hand, peaks
  modestly, and is already leaving.
- **Structure.** Markers (§6.3) and cards (§6.13) carry a
  `--warm` custom property (0 at rest). Hover/focus sets a
  JS-driven tween: `--warm` 0→1 over 300ms `--ease-flare`;
  on leave, 1→0 over 1200ms `--ease-cool`. `--warm` drives
  exactly two things: the dot's colour (mixed one stop
  hotter than page temperature, capped at `--ember` — a
  rekindle can never exceed the forge's original heat) and
  a box-shadow glow (0→8px, `--ember` at 35%). Cards: the
  polished-edge highlight (§6.13) brightens by `--warm` ×
  20% lightness. No transform, no lift — heat, not levitation.
- **Motion spec.** Trigger: pointerenter / focusin.
  Flare 300ms; hold while hovered (the hand is still
  there); decay 1200ms from pointerleave / focusout.
  Re-entry during decay resumes from the current `--warm`
  (no snap). One element rekindles at a time per pointer;
  keyboard focus rekindles independently.
- **States.** Cold-at-page-temperature (rest) → flaring
  (300ms) → warm-held (hover persists) → cooling (1200ms)
  → rest. Scrolled-past: an element left behind mid-decay
  finishes cooling off-screen; its state is never stored
  warm. Disabled controls: no rekindle (a disabled action
  is cold iron; §11).
- **Content merge.** The warmth lands on the marker of the
  section you are considering and the edge of the blade you
  are touching — the feedback is located *in* the object,
  not in a tooltip, cursor trail or page-wide glow.
- **Failure fallback.** No JS: no rekindle; markers and
  cards rest at page temperature with their printed states
  complete. CSS-only degradation: a `:hover` rule applies
  the static one-stop-hotter colour without the tween —
  warmth without choreography, still honest.
- **Reduced-motion variant.** The colour change applies
  instantly on hover/focus and removes instantly on leave
  (a state, not an animation). Glow shadow is omitted
  (shadows are motion-adjacent shimmer in this variant);
  the edge brightening remains, instant.
- **Performance budget & mobile variant.** One tween per
  hovered element, property writes only while `--warm` is
  changing. Touch: no hover rekindle — a tap is either
  navigation or §6.9's strike, never a warm-up; focus
  rekindle remains for switch/keyboard users on touch
  devices.
- **Choreography timeline (v2).** t=0 pointerenter →
  `--warm` 0→0.6 by t=180ms → 1.0 at t=300ms (dot one stop
  hotter, glow 8px) → held while hovered → pointerleave:
  decay begins → t=+600ms `--warm` 0.4 → t=+1200ms 0, dot
  back at page temperature exactly (the curve lands on
  `--temp`, not near it — the gate samples the end state).
- **State matrix (v2).** *Rest:* `--warm` 0. *Hover:* as
  above. *Focus:* as hover, plus §11's focus ring on the
  control itself (the ring is `--edge`, never ember — focus
  is information, not heat). *Active:* press interrupts
  rekindle into §6.9/§11's press behaviour. *Scrolled-past:*
  decay completes regardless of visibility. *Disabled:*
  no rekindle, dot printed cold. *Touch:* tap = action;
  long-press does nothing (no hidden gestures in this theme).
- **Breakpoints (v2).** Identical at all sizes where a
  pointer exists; ≥1200px glow 8px, 768–1199px glow 6px
  (narrower rail, tighter light), <768px pointer-fine only.
- **Edge cases & failure modes (v2).** *Pointer sweeping
  across many markers:* each flare is capped and decays
  independently; the page may show several cooling dots —
  true to a hand brushing a rail of cooling iron. *Hover
  during the strike (§6.1):* rekindle is suppressed until
  t=1200ms — the forge's first blow outranks a visitor's
  warmth. *`--warm` left high by a killed tween:* the
  loop's watchdog resets any `--warm` with no active
  pointer/focus owner to decay within 1200ms.
- **Accessibility spec (v2).** Rekindle is never the only
  hover/focus feedback: focus always carries §11's ring,
  and hovered links/cards keep their underline/edge states
  independent of `--warm`. Colour change is ≤ one stop and
  never reduces text contrast (dots and edges only; text
  colours do not warm).
- **Tokens consumed (v2).** `--ember`, `--ember-pale`,
  `--ember-deep`, `--edge`, `--ease-flare`, `--dur-flare`
  (300ms), `--dur-cool-long` (1200ms).

### 6.9 Strike click & the dent ledger

- **What & why.** Clicking a blade card dents it: a 1px
  inset shadow blooms at the exact click point with 4–6
  sparks, and a tiny dent mark stays on the card's surface
  for the session. It belongs because in a forge, handling
  leaves marks — the card accumulates its own forged
  history, and a visitor who has struck three blades can
  see which three. Interaction here is not feedback *about*
  the object; it is a change *to* the object.
- **Structure.** Each card (§6.13) carries a dent layer
  (absolutely positioned, `pointer-events:none`) holding up
  to 12 dent marks: 10px radial dents (radial-gradient,
  `--iron-deep` centre, `--steel-pale` rim at 40%, hard
  stop) placed at click coordinates. Click handling: the
  card's primary action (navigation to the piece, §7) still
  fires — the dent is struck *on the way*, at pointerdown,
  so the mark exists even though the page is leaving; dents
  persist in `sessionStorage` as (card-id, x%, y%) and are
  re-applied on return within the session. Sparks share
  §6.1's canvas system, spawned at the click point.
- **Motion spec.** Trigger: pointerdown on a card. Dent
  bloom: scale 0.4→1 + shadow deepen over 180ms
  `--ease-strike`; sparks 4–6, 300ms life, velocities
  40–140px/s (a click is a tap of the hammer, not the
  forge blow — §6.1's energies are reserved). The dent
  itself is permanent for the session from t=0 — the bloom
  is the striking, the mark is the result.
- **States.** Undented → struck (bloom 180ms) → dented
  (rest; dent visible at rest contrast, slightly deepened
  by §6.8's warmth under hover). 13th click on one card:
  the oldest dent is *re-forged* — it fades to a faint
  ghost (the smith planished it out) and the apparatus line
  under the card notes "RE-WORKED" once (§6.17's voice).
  Scrolled-past: dents persist.
- **Content merge.** The dents land on the product's own
  card, at the spot the visitor actually touched — often
  on the blade's photograph itself, where a real buyer's
  thumb-and-hammer curiosity would mark a handled piece.
  The ledger is the card's surface, not a sidebar of
  achievements.
- **Failure fallback.** No JS: cards are plain links,
  undented, complete. Storage blocked: dents last for the
  page view only (in-memory), and the card's apparatus
  says nothing about persistence it cannot keep.
- **Reduced-motion variant.** No sparks, no bloom: the
  dent appears instantly at pointerdown (the mark matters,
  the blow rests). Session persistence unchanged.
- **Performance budget & mobile variant.** Dent layer ≤ 12
  nodes per card; sparks reuse the shared canvas (≤6 per
  click, and clicks are rate-limited by the pointer
  itself). Mobile: identical — a tap is a strike on touch
  too, at 3–4 sparks; dents are *more* valuable on mobile,
  where hover feedback does not exist.
- **Choreography timeline (v2).** t=0 pointerdown → dent
  node placed at (x,y), bloom begins → sparks emit
  t=0–60ms → t=180ms bloom complete, dent at rest contrast
  → navigation (if the click was on the card's link)
  proceeds in parallel from t=0 — the dent is written to
  session storage synchronously at pointerdown, before any
  navigation can unload the page.
- **State matrix (v2).** *Rest:* dents as struck. *Hover:*
  §6.8 warmth; dents deepen 10% (light catches damage).
  *Focus:* keyboard activation (Enter on the card link)
  strikes a dent at the card's optical centre — keyboard
  visitors leave marks too, at the one honest coordinate
  available to them. *Active:* the press itself (above).
  *Scrolled-past:* dents persist. *Disabled:* a sold
  piece's card (§6.13) takes no new dents — its surface is
  finished; clicks route to its record instead. *Touch:*
  tap = strike + action, as desktop.
- **Breakpoints (v2).** Identical behaviour; dent size
  10px ≥768px, 12px <768px (a thumb strikes wider than a
  cursor).
- **Edge cases & failure modes (v2).** *Click on the
  card's inner button (reserve/enquiry):* the button's own
  press (§11) fires; no dent — striking the paperwork is
  not striking the blade. The dent zone is the card's
  image and body, declared in markup. *Session storage
  full/blocked:* in-memory fallback (above). *Card
  re-rendered by filtering (§7):* dents re-apply by
  card-id on render.
- **Accessibility spec (v2).** Dents are `aria-hidden`
  decoration on a link whose accessible name never changes
  ("Gibeon blade № 3 — view the piece"); the dent count is
  not announced (it is a surface, not a score). The click
  target remains the whole card ≥ 44px in every dimension
  of its link area. Sparks respect §6.1's reduced-motion
  and transparency rules.
- **Tokens consumed (v2).** `--iron-deep`, `--steel-pale`,
  `--spark`, `--ember`, `--ease-strike`.

### 6.10 The cold mirror footer

- **What & why.** The footer is polished mirror-bright —
  the page's only light surface — where a slow, cold light
  crawl crosses its etched bands once as it centres, and
  then everything rests still: no loops, no embers, no
  warmth. It belongs because the page must end the way the
  meteorite ends: cold, finished and singular. Stillness
  itself is the final state the whole design has been
  cooling toward, and a footer that keeps animating would
  be a fire that refuses to go out — a lie about the
  material (§1).
- **Structure.** A `--mirror` ground plate (the theme's
  only inversion) carrying: the maker's mark (§6.11's
  treatment, in `--iron` on mirror), the cooling record —
  the session's thermal summary printed by the Assay:
  plates passed (DOM-counted), final temperature (18°C,
  §6.5's figure, gate-checked to agree), deepest pattern
  etched (§6.4's state) — the navigation repeated in
  `--iron`, the legal line, and the fixed closing line
  (§12): "Cooled. Finished. Singular." Etched bands: three
  hairline Widmanstätten strips in `--band-deep` cross the
  footer's head; the light crawl is a `--smoke`-white
  gradient translating across them once.
- **Motion spec.** Trigger: footer centre crosses 60% of
  viewport, once. Crawl: gradient translateX −20%→120%
  over 2400ms `--ease-cool`, opacity peaking 0.5 — cold
  light on a mirror, not a shimmer loop. After the crawl:
  nothing on the footer ever moves again, including on
  scroll-back (a mirror does not re-polish itself for a
  second look).
- **States.** Approaching (bands matte) → crawling (once,
  2400ms) → still (permanent rest). Hover on footer links:
  underline inks (§11) — the only footer interaction, and
  it is typographic, not thermal: no rekindle exists here
  (§6.8 is refused below the last plate; the gate greps
  the footer for ember-family values and expects none, §2).
- **Content merge.** The footer is not a sitemap bolted
  under the artwork: it is the process's end-state, and its
  record lines are the page's own data (plates, temperature,
  etch state) printed by the Assay as a foundry stamp. The
  legal and navigation furniture ride on the mirror because
  the mirror is where the page's story deposits them.
- **Failure fallback.** No JS: the footer renders complete
  with the crawl pre-applied as a static gradient resting
  at 60% across the bands (a photograph of the light
  mid-crossing), record lines printed at their full-page
  values ("PLATES — ALL", temperature line omitted rather
  than faked, per §6.5's no-JS ruling).
- **Reduced-motion variant.** No crawl. The bands rest
  matte; the record prints identically. Stillness is the
  variant *and* the original's destination.
- **Performance budget & mobile variant.** One gradient
  animation, once, then zero ongoing cost — the cheapest
  footer in the library after the crawl, by design.
  Mobile: crawl shortens to 1600ms (less mirror to cross);
  the record stacks in one column.
- **Choreography timeline (v2).** Footer top enters →
  centre at 60%: t=0 crawl begins → t=2400ms crawl ends,
  gradient removed from the DOM → t=+0 the cooling bar's
  head (§6.5) reaches mirror state in the rail above —
  the two events are sequenced by the same p=1 condition,
  so instrument and destination agree → rest, permanently.
- **State matrix (v2).** *Rest:* still mirror. *Hover:*
  link underlines only. *Focus:* §11 ring in `--iron`
  (visible on mirror at 13.9:1 pairing). *Active:* link
  press, §11. *Scrolled-past:* still — there is nothing
  past the footer, and scrolling back up finds it exactly
  as cold. *Disabled / no-JS:* complete, static gradient.
  *Touch:* identical; no tap effects exist here.
- **Breakpoints (v2).** ≥1200px: three record columns.
  768–1199px: two columns, record first. <768px: one
  column; the mark centres; bands remain full-width.
- **Edge cases & failure modes (v2).** *Short page* (footer
  visible at load): the crawl fires once at t=1200ms after
  load instead of on scroll — the mirror still gets its
  one crossing. *Footer reached by anchor jump:* crawl
  plays on arrival (it is positional, not earned by
  scrolling) but the record prints only plates actually
  passed — a jumper's record honestly shows the jump
  (§6.5's rule). *Print:* footer prints as a light plate
  with the record — the one page of the printout that
  looks like paper.
- **Accessibility spec (v2).** Text on `--mirror` is
  `--iron` at 13.9:1; apparatus `--band-deep` on mirror is
  3.9:1, apparatus-size only per §3. The crawl is
  `aria-hidden` and unannounced. Focus order is document
  order; nothing in the footer is positionally trapped.
- **Tokens consumed (v2).** `--mirror`, `--iron`,
  `--band-deep`, `--smoke`, `--ease-cool`.

### 6.11 The plate masthead — navigation

- **What & why.** The site's navigation is a narrow iron
  plate riveted across the top: the maker's mark at left,
  struck and dented (§6.2's treatment at small scale), and
  the section links set as apparatus inscriptions in mono,
  the current one underlined by a polished-edge rule. It
  belongs because a forge's nameboard is a plate, not a
  bar; and because the masthead is the one piece of
  furniture that must read *hot* — it is forged first and
  carries the strike's dent for the whole session.
- **Structure.** A 56px `--iron` plate, bottom hairline
  `--steel-pale`, sticky at the viewport top. Mark: Archivo
  900 20px with the §6.2 dent shadow (static CSS — the
  masthead never re-strikes). Links: mono 12.5px uppercase
  apparatus, `--band`, current link `--edge` with a 2px
  `--edge` rule beneath (the polished edge is the underline
  of record). Right side: the session's one utility — the
  enquiry link (§6.15) — set as a struck chip (§11 button).
  The rail's instruments (§6.5, §6.6) begin below the
  masthead; the masthead itself carries no temperature (it
  is above the story, like the forge's sign).
- **Motion spec.** The masthead does not animate on scroll:
  no shrink, no hide-on-scroll-down (a nameboard does not
  duck). Its single motion is the current-link rule sliding
  between links on in-page navigation: 240ms `--ease-etch`.
  On page change (§6.16) it arrives already in place.
- **States.** Rest (all pages). Current-link state migrates
  with scroll position on single-page sites (scrollspy at
  the 45% line) and with route on multi-page. Hover:
  §6.8's warmth is refused here — links ink to `--edge`
  instead (the masthead is signage, not workpiece).
  Scrolled-past: unchanged, by design.
- **Content merge.** The mark in the masthead is the same
  struck mark as the hero's headline in miniature — one
  name, struck once, carried everywhere. Links name the
  plates in the Assay's voice (§12 labels).
- **Failure fallback.** No JS: all links plain, current
  link marked by route at build time. Sticky unsupported:
  the plate sits at the document head, static — the page
  loses a convenience, nothing else.
- **Reduced-motion variant.** The current-rule applies
  instantly on change. Nothing else exists to reduce.
- **Performance budget & mobile variant.** Static plate;
  scrollspy shares the §6.5 loop's plate registry (no
  second observer). Mobile: mark + enquiry chip + a
  "PLATES" disclosure that opens the link list as a second
  plate row beneath (in-flow, pushing nothing sideways);
  targets ≥48px.
- **Choreography timeline (v2).** On load: masthead
  present from first paint (never slides in) → on section
  change: rule slides 240ms → on §6.16 arrival: masthead
  is present in the landed page's first frame.
- **State matrix (v2).** *Rest:* as built. *Hover:* link
  inks to `--edge` over 150ms. *Focus:* §11 ring, `--edge`
  on iron. *Active:* link press — none (links navigate,
  they do not dent; §6.9 is for workpieces). *Scrolled-
  past:* n/a. *Disabled:* a link to the current page is
  `aria-current`, never disabled-styled into illegibility.
  *Touch:* identical, disclosure pattern as above.
- **Breakpoints (v2).** ≥1200px: full link row. 768–1199px:
  links compress (apparatus shortens to plate names only).
  <768px: disclosure pattern.
- **Edge cases & failure modes (v2).** *Many sections
  (>7 links):* the row refuses to shrink type below 12.5px
  — overflow links move into the disclosure at every size
  (a nameboard with nine names is a directory; the theme
  caps the board). *Long mark:* the mark truncates never;
  links yield first.
- **Accessibility spec (v2).** `<nav>` with aria-label
  "Plates"; `aria-current="page"` (or `"location"` for
  scrollspy) on exactly one link; disclosure button
  `aria-expanded` wired; skip-link lands on the first
  plate head, styled as an apparatus line on focus.
- **Tokens consumed (v2).** `--iron`, `--steel-pale`,
  `--band`, `--edge`, `--ease-etch`.

### 6.12 Hero composition — the maker's plate

- **What & why.** The hero plate's exact composition: the
  struck headline (§6.2) at the plate's optical centre-left,
  beneath it the standfirst in mono lead, beneath that the
  specimen line — one line of assay naming the hero piece's
  meteorite, class and cooling time (§6.17) — and at the
  plate's foot the tally row: formation counters (§6.14)
  in miniature, already counting. It belongs because the
  hero must state the whole theme in one screen: a name
  being forged, a material being assayed, a timescale being
  counted — Smith, Assay and deep time, stacked in that
  order.
- **Structure.** One 100vh plate (min 640px, max 920px —
  the hero never sprawls). Vertical rhythm: mark zone
  (headline + §6.1's strike point), standfirst ≤ 3 lines at
  62ch, specimen line as an apparatus inscription with
  hairline rules above and below (an inscription is *set
  into* the plate), tally row at the foot separated by the
  first etched seam (§6.7). The pattern field (§4) occupies
  the plate's right third as a generated panel behind
  nothing — it is beside the text, never behind it (text
  over crystal is failure 6 in §9).
- **Motion spec.** Sequence: strike + letters (§6.1, §6.2,
  t=300–1400ms) → specimen line's rules draw 600ms
  `--ease-etch` from t=+200ms after the last letter → tally
  counters begin on first scroll or at t=2500ms, whichever
  is earlier (§6.14). The standfirst never animates: it is
  readable from first paint (the Assay does not wait for
  the Smith to finish before speaking).
- **States.** Composing (first 1400ms) → at rest (the
  hero's permanent state: struck name, printed record,
  counting tally) → scrolled-past (the hero cools with the
  page; its marker, §6.3, is the page's first ember).
  Hover: the pattern panel does not respond. Focus: §6.2's
  completion rule applies.
- **Content merge.** Every element of the composition is
  the page's actual first content — headline, introduction,
  the hero product's record, the site's figures. There is
  no decorative layer to remove; delete the motion and the
  hero is unchanged, only quieter.
- **Failure fallback.** No JS: the complete composition at
  rest — struck headline, printed specimen line, counters
  at full value (§6.14). Fonts late: §6.2's rule ships the
  headline printed rather than hold the composition.
- **Reduced-motion variant.** The full composition printed:
  no strike, no letter ceremony, rules drawn, counters at
  value. Identical information, identical order.
- **Performance budget & mobile variant.** Hero payload
  budget: pattern SVG ≤ 30KB, no hero video, no image
  (the hero product's photograph lives in §6.4's plate,
  not here — the hero is type and crystal, the product
  gets its own plate). Mobile: pattern panel moves below
  the tally as a 96px band; headline 36px; plate height
  auto (min 100svh − masthead).
- **Choreography timeline (v2).** t=0 composition readable
  → t=300ms strike → letters land to t≤1400ms → t=+200ms
  specimen rules draw (600ms) → t=2500ms or first scroll:
  tally counts (§6.14) → hero at rest; page temperature
  p=0, all instruments hot (§6.3, §6.5, §6.6).
- **State matrix (v2).** *Rest:* as composed. *Hover:*
  none on the composition; the tally's figures are not
  controls. *Focus:* ceremony-completion rule (§6.2).
  *Active:* n/a. *Scrolled-past:* cooled with the page.
  *Disabled / no-JS:* printed complete. *Touch:* identical;
  the strike's shake is the 2px variant (§6.1).
- **Breakpoints (v2).** ≥1200px: side pattern panel, 64px
  headline. 768–1199px: pattern panel narrows to a quarter,
  48px. <768px: stacked, pattern as a band, 36px.
- **Edge cases & failure modes (v2).** *Headline at the
  22-glyph cap + long standfirst:* the plate grows (max
  height yields) rather than shrink type below law sizes —
  a plate can be taller; type cannot be smaller than §3.
  *No hero specimen (a dealer with no featured piece):*
  the specimen line names the house meteorite stock line
  from the record, or the line is omitted entirely — an
  inscription is never filler (§12).
- **Accessibility spec (v2).** Reading order = visual
  order: h1, standfirst, specimen line, tally. The pattern
  panel is `aria-hidden`. Tally figures carry sr-only full
  text ("cooling time, four million years") beside their
  tabular renderings (§6.14).
- **Tokens consumed (v2).** `--iron`, `--steel`,
  `--band-deep`, `--edge`, `--band`, `--ease-etch`.

### 6.13 Blade cards — tilt to the light

- **What & why.** Product cards are small iron plates laid
  on the page's big plate: the piece's photograph in a
  hammered frame, its name in Archivo, its assay line in
  mono (§6.17), and its status as a printed line. Hover
  turns the card ≤3° like a blade turned on a bench to
  catch light on its edge — the polished edge brightens as
  it centres. It belongs because a blade is examined by
  tilting it; the card's one physical behaviour is the
  object's own.
- **Structure.** `<article>` plate: `--steel` face, 1px
  `--steel-pale` rim, hard offset shadow (0 2px 0
  `--iron-deep` — a plate's shadow is a line, §11). Image
  zone: the photograph (never the same angle twice across a
  listing — §9, from the original entry) inside a frame
  whose inner edge is a 2px `--edge`-at-20% line (the
  polished edge). Below: name (Archivo 800 20px), assay
  line (mono apparatus: meteorite · class · one figure),
  status line ("ON THE BENCH" / "SOLD — IN THE VAULT" /
  "WITH THE SMITH"), and the whole card is one link to the
  piece's plate (§7) with §6.9's dent layer above the image.
- **Motion spec.** Entrance: forge-weight drop — 10px
  translateY + settle over 650ms `--ease-drop`, staggered
  70ms per card in a row, triggered with the plate's etch
  (§6.7, t=+150ms). Tilt: pointer-tracked rotateX/rotateY
  ≤3°, driven by the shared loop at lerp 0.14 (cards are
  lighter than the page's cooling values — a blade in the
  hand responds faster than an ingot cools), pivot at the
  pointer's quadrant. Edge brightening: the frame's
  polished line lightens toward `--edge` full as the
  card's centre crosses the viewport's middle third on
  scroll (scrubbed, same loop). Image: scale-in-frame
  1.06→1 across the card's viewport pass.
- **States.** Rest (flat, edge at 20%) → entering (drop) →
  held/tilted (hover) → centred (edge at full polish,
  scrub state) → sold (status line printed, tilt refused —
  a sold blade is in the vault, not on the bench; its card
  still links to its record). Focus: tilt 1.5° toward the
  top edge + §11 ring (keyboard gets a courteous half-tilt,
  never the full performance). Scrolled-past: flat, dents
  (§6.9) persisting.
- **Content merge.** The card is the product's listing
  itself — photograph, name, assay, status. The tilt is
  how the object is examined; the edge-light is the
  object's own polished bevel catching the room. Nothing
  decorative is added; remove the motion and the listing
  is complete.
- **Failure fallback.** No JS: cards flat, edges at a
  printed 55% polish (a middle state, honestly static),
  all links live. Images missing: the frame holds the
  etched pattern field (§4) with the piece's name as an
  apparatus inscription — a card without a photograph is a
  plate awaiting its blade, and says so.
- **Reduced-motion variant.** No tilt, no drop: cards
  printed in place as their plate etches (§6.7's frame
  only). Edge polish printed at 55%.
- **Performance budget & mobile variant.** Tilt writes are
  transform-only, one card at a time (the hovered one);
  images lazy-load below the fold with declared dimensions
  (no layout shift — a plate does not jump on the bench).
  Mobile: no tilt (no pointer); edge polish printed at
  55%; entrance drop 6px/500ms; cards stack one per row —
  a blade is examined alone.
- **Choreography timeline (v2).** Plate etch begins →
  t=+150ms cards drop, 70ms stagger → each card's edge
  scrubs with viewport pass → hover: tilt engages ≤120ms
  to full angle (loop-lerped), §6.8 warmth flares on the
  card's marker-line → pointerdown: §6.9 dent + sparks →
  pointerleave: tilt returns over 400ms `--ease-cool`
  (a blade is laid down gently).
- **State matrix (v2).** *Rest:* flat, dents as struck.
  *Hover:* tilt ≤3°, edge brightens, §6.8 warmth. *Focus:*
  1.5° courtesy tilt + ring. *Active:* §6.9 strike at the
  press point; the link navigates on release (click).
  *Scrolled-past:* flat, edge at its scrub value.
  *Disabled:* sold cards — tilt and dents refused, link to
  record live. *Touch:* tap = §6.9 strike + navigation;
  no tilt, no hover warmth.
- **Breakpoints (v2).** ≥1200px: 3 cards per row, tilt 3°.
  768–1199px: 2 per row, tilt 2.5°. <768px: 1 per row, no
  tilt, drop 6px.
- **Edge cases & failure modes (v2).** *Long names:* card
  names cap at 2 lines (Archivo 800) with the assay line
  always visible — a card that hides its assay to fit its
  name has failed the theme's priorities (§3 law 2).
  *Mixed sold/available rows:* sold cards keep their grid
  place (the bench shows its gaps honestly) and sort last
  only when the visitor filters (§7). *Image aspect
  variance:* frames are fixed-ratio (4:3); photographs are
  cropped by the frame, never stretched — iron does not
  stretch.
- **Accessibility spec (v2).** The card link's accessible
  name: piece name + status ("Muonionalusta blade № 2 —
  on the bench"). Tilt is `aria-hidden` motion on a link
  whose geometry for AT never changes. Focus ring is
  §11's `--edge` 2px offset 3px, visible at every tilt
  angle (the ring does not tilt — it belongs to the page,
  not the blade).
- **Tokens consumed (v2).** `--steel`, `--steel-pale`,
  `--iron-deep`, `--edge`, `--band`, `--ease-drop`,
  `--ease-cool`, `--dur-drop` (650ms).

### 6.14 Formation counters

- **What & why.** The site's figures — cooling time in
  millions of years, blades forged from one fall, nickel
  percentage of the house iron — count up once, in mono, to
  values taken from the specimen record (§6.17). It belongs
  because deep time is this theme's awe, and awe here is
  arithmetic: a number that took four million years to
  become true deserves to be *counted to*, once, at data
  size (§3 law 2), and then to stand still like everything
  else that has finished forming.
- **Structure.** Counter figures are real text in the DOM
  at their **full final value** from first paint. JS arms a
  count by *masking* the figure with a counting copy
  (`aria-hidden`) that runs 0→value; the accessible, printed
  value never changes. Each counter carries its source in
  an apparatus line beneath ("FROM THE ASSAY — GIBEON,
  IVA") — a figure without its source printed beside it
  may not count (§1 law 2). Counting duration is banded by
  magnitude: <100 → 900ms; <10,000 → 1400ms; ≥1,000,000 →
  2200ms (millions take time; the count is the theme's one
  licensed piece of theatre, and it is rationed to it).
- **Motion spec.** Trigger: the counter's plate etches
  (§6.7) or, in the hero tally (§6.12), t=2500ms/first
  scroll. Easing `--ease-cool` (counts decelerate like
  cooling — fast when hot, asymptotic at the true value).
  Digits are tabular; thousands separators are the record's
  own format. A counter runs **once per session**; its end
  state is the printed value, indistinguishable from no-JS.
- **States.** Printed (DOM default) → counting (masked
  copy running) → counted (mask removed; the printed value
  stands). Hover/focus: none. Scrolled-past mid-count: the
  count completes on its own clock (formation does not
  wait to be watched). Re-entry: never re-runs (§1 —
  reheating).
- **Content merge.** The counters *are* the site's claims —
  the hero tally and the record plate's figures. Their
  apparatus source lines tie each to §6.17's record, so the
  performance and the provenance are the same element.
- **Failure fallback.** No JS: full values printed — the
  fallback is the design's own rest state. Watchdog at
  duration+400ms: mask removed regardless.
- **Reduced-motion variant.** No counting. Figures stand
  printed. (The mask is never armed.)
- **Performance budget & mobile variant.** Text writes at
  most every frame for ≤3 concurrent counters; trivial.
  Mobile: identical, durations shortened 20% (a smaller
  screen holds less deep time comfortably — stated here so
  two builders do the same thing).
- **Choreography timeline (v2).** Plate etch t=0 → t=+300ms
  count begins → magnitude-banded duration → final 15% of
  the count covers the last 2% of value (the asymptote —
  the number *arrives* the way cooling ends: gradually,
  then certainly) → mask removed → apparatus source line
  etches its underline (§6.7 band, 300ms).
- **State matrix (v2).** *Rest:* printed value. *Hover:*
  none. *Focus:* a focused counter completes instantly.
  *Active:* n/a. *Scrolled-past:* completed or completing
  on its clock; end state identical. *Disabled / no-JS:*
  printed. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: figures at 28px in the
  tally row. 768–1199px: 24px, tally wraps 2×2. <768px:
  22px, tally stacks; apparatus source lines remain
  (they are not optional decoration).
- **Edge cases & failure modes (v2).** *Record value
  changes (a blade sells; the count of blades from one
  fall rises):* the printed value is the record's at build
  time; the counter counts to the printed value, never to
  a live-fetched different one — figure and count cannot
  disagree because they are the same string. *Value 0:*
  a counter never counts to zero for theatre; a true zero
  prints as a line of prose ("NO BLADE FROM THIS FALL IS
  ON THE BENCH") per §12's empty voice.
- **Accessibility spec (v2).** The counting copy is
  `aria-hidden`; screen readers meet only the true value,
  once, in reading order. No live regions — a number
  arriving is not an announcement. Tabular figures prevent
  layout shift during the count.
- **Tokens consumed (v2).** `--edge`, `--band`,
  `--ease-cool`.

### 6.15 The commission forge — conversion form

- **What & why.** The theme's conversion is a commission:
  a visitor asks the smith to forge one piece — from a
  named meteorite, to a named form — and the form is a
  bench record, not a checkout: fields for the piece, the
  iron, the hand it is for, and the words to etch. Its
  success state is a struck confirmation plate carrying a
  commission number derived from the bench's real book
  (§6.17). It belongs because in this world nothing is
  bought off a shelf; everything is *ordered into
  existence*, and the form should feel like the first
  strike of that making.
- **Structure.** One plate, one column of etched fields
  (§11's input treatment: `--steel` recessed fields,
  hairline `--steel-pale`, mono labels above in apparatus).
  Order of fields (the bench's order, never rearranged by
  a platform): the piece (radio rows of forms — blade /
  band / dial / other, §11's struck-chip radios), the iron
  (radio rows generated from the record's available
  meteorites — a meteorite with no stock does not appear;
  the form cannot offer iron the forge does not hold),
  the hand (name), the direction (email), the etching
  (optional text, ≤ 40 characters — an inscription is
  short, §12), the note (textarea, grows by lines). The
  summary line above the submit recomputes from the live
  selections: "ONE BLADE — GIBEON IRON — ETCHED WITH 6
  CHARACTERS" in apparatus mono. Submit: the struck plate
  button (§11).
- **Motion spec.** Field focus: the field's hairline inks
  to `--edge` over 200ms `--ease-etch` and a small ember
  dot at the label's left warms one stop (§6.8's curve —
  the bench warms where you work). Radio selection: the
  chip takes a 1px dent press, 150ms `--ease-strike`.
  Submit: the button strikes (dent + 4 sparks, §6.9's
  energies), the form's plate holds a "STRIKING…" apparatus
  state for the real submission duration, then the whole
  plate turns (§6.16's transition grammar at plate scale,
  700ms) into the confirmation: a struck plate bearing the
  visitor's own selections as assay lines and the
  commission number (derived: the bench book's next number,
  printed by the server/record — never a random string;
  where the demo is static, the number is labelled
  "BENCH BOOK — NEXT NUMBER AT TIME OF PRINTING" per §12's
  honesty rule).
- **States.** Rest (fields printed, summary live) →
  working (per-field warmth) → striking (submit in flight;
  fields disabled but *kept* — values never clear on
  error) → confirmed (the struck plate; the form is gone,
  replaced, not hidden). Error state: the field's rule
  turns `--ember-deep` (dried heat — an error is a cooling
  problem, stated in the Assay's voice beneath the field,
  §12), focus moves to the first error on submit, and
  nothing the visitor typed is lost.
- **Content merge.** The form's choices are generated from
  the same record (§6.17) that powers the cards and
  counters — the forge cannot be asked for iron it does
  not list, and the confirmation's assay lines are the
  record's own words. The form is the bench's order book
  made fillable.
- **Failure fallback.** No JS: a plain working form (native
  radios, native submit) posting to the same endpoint; the
  summary line prints its default ("ONE PIECE — IRON TO BE
  AGREED AT THE BENCH") rather than a fake live value.
  Submission failure: the plate holds its state, error
  stated at the plate head in the Assay's voice, all
  values intact, submit re-enabled.
- **Reduced-motion variant.** No strike, no turn: the
  confirmation replaces the form with a 200ms crossfade.
  Field warmth applies instantly. Everything else identical.
- **Performance budget & mobile variant.** The form plate
  is one observer target; no per-keystroke layout (the
  summary updates on change events only, text-only writes).
  Mobile: fields stack full-width; radio chips become
  full-width rows ≥52px; the summary sticks above the
  submit at the plate's foot (the bench keeps the order in
  sight while the hand signs it).
- **Choreography timeline (v2).** Field focus: rule inks
  200ms, label ember warms → selection: chip dents 150ms,
  summary line updates (text swap, no animation) → submit
  pointerdown: button dent + sparks t=0 → t=+150ms plate
  state "STRIKING…" → response: success → plate turn 700ms
  → confirmation plate lands dented (§6.16 grammar) with
  its commission number struck last (90ms `--ease-strike`,
  the number is the final blow) → error → plate head note
  etches in 300ms, first errored field's rule turns, focus
  moves.
- **State matrix (v2).** *Rest:* printed, live summary.
  *Hover:* chips and button take §6.8 warmth. *Focus:*
  rule ink + label warmth + §11 ring. *Active:* dent
  presses (chip 150ms, button strike). *Scrolled-past:*
  the form keeps its state (a half-filled commission
  survives scrolling — the bench does not clear itself).
  *Disabled:* submit is never pre-disabled (§11 — the
  bench accepts the strike and answers honestly); fields
  disable only during the striking state. *Touch:*
  identical; chips ≥52px rows.
- **Breakpoints (v2).** ≥1200px: form plate at 62ch with
  the record's iron list as a two-column chip grid.
  768–1199px: one-column chips. <768px: full-width rows,
  sticky summary (above).
- **Edge cases & failure modes (v2).** *A meteorite sells
  out between page load and submit:* the confirmation is
  refused in the Assay's voice ("THE GIBEON WAS CLAIMED
  WHILE YOU WROTE. THE BENCH OFFERS MUONIONALUSTA, OR
  WAITS.") with the visitor's other fields intact — the
  form keeps faith and stock simultaneously. *Etching
  text with glyphs the forge cannot cut:* the field states
  its alphabet plainly under the label ("LETTERS, FIGURES,
  AND THE MAKER'S MARK") before the error, not after.
  *Duplicate submit:* the strike is idempotent — a second
  press during striking is ignored, and the confirmation
  number is the book's, struck once.
- **Accessibility spec (v2).** Native form semantics
  throughout: real `<fieldset>`/`<legend>` for the radio
  groups ("The piece", "The iron"), labels bound to
  inputs, errors linked by `aria-describedby` and
  summarised at the plate head with `role="alert"` on
  submit only. Focus is never moved except to the first
  error, and the confirmation takes focus at its heading
  (`tabindex="-1"`) so the number is the next thing read.
  All targets ≥48px.
- **Tokens consumed (v2).** `--steel`, `--steel-pale`,
  `--edge`, `--band`, `--ember`, `--ember-deep`,
  `--ease-etch`, `--ease-strike`, `--dur-turn` (700ms).

### 6.16 Unetched skeleton & the strike transition

- **What & why.** Loading in this theme is dark, unetched
  iron: plates arrive as `--iron-deep` fields carrying the
  layout's anatomy in `--steel` blocks — the shape of the
  plate before the acid touches it. Page transitions are
  the strike's echo: a white spark flash ≤120ms, and the
  new page lands already dented and still. It belongs
  because both states are the material at its two honest
  extremes — before formation, and after impact — and
  because the theme's law forbids the transition from
  re-striking (§6.1 is once per session): later pages
  arrive *cold*, dented by a blow the visitor is trusted
  to remember.
- **Structure.** Skeleton: per-plate blocks mirroring the
  real plate's anatomy (headline bar at true measure, text
  bars at true line count ±1, image block at the frame's
  true ratio), built from the same layout tokens as the
  content — a skeleton that lies about anatomy is a
  different plate (§9). No shimmer sweep: unetched iron
  does not glitter; a single `--steel-pale` hairline etches
  across the skeleton's head over 1200ms to signal *work
  is happening* — the acid arriving, slowly. Transition:
  an overlay flash div (`--spark` at 85% → transparent,
  120ms) fired on navigation commit, with the incoming
  page rendered beneath it already complete.
- **Motion spec.** Skeleton etch-line: 1200ms
  `--ease-etch`, loops only while content is genuinely
  loading, hard-capped at 6s — past 6s the skeleton is
  replaced by the plate's error state in the Assay's voice
  (§12), because iron that never arrives should say so.
  Transition flash: 120ms, on internal navigation only;
  modified clicks (new tab etc.) bypass it entirely — the
  browser's gestures outrank the theme's.
- **States.** Skeleton → etching-in (real content replaces
  block-for-block as it arrives; a plate never pops from
  skeleton to a *different* layout) → loaded. Transition:
  flash → landed (new page at rest, its own §6.7 etches
  arming normally below its fold).
- **Content merge.** The skeleton is the plate's own
  anatomy and the flash is the session's founding event
  remembered — both are the site's material states, not
  chrome borrowed from a UI kit.
- **Failure fallback.** Content that fails: the plate
  renders its error as an apparatus inscription on
  `--iron-deep` ("THIS PLATE DID NOT ARRIVE FROM THE
  BENCH — RETRY"), retry as a §11 chip. The flash failing
  (JS off) leaves plain navigation — the theme degrades to
  the web's default without a scar.
- **Reduced-motion variant.** No flash. Skeleton static
  (the etch-line printed at 60%). Navigation is instant
  and silent.
- **Performance budget & mobile variant.** Skeleton is
  pure CSS blocks (no images); flash is one div. Mobile:
  identical, flash 100ms.
- **Choreography timeline (v2).** Navigation click → t=0
  flash begins (only after the browser commits to the
  navigation — a flash over a page that never leaves is a
  lie) → new document's first paint beneath the flash's
  tail → t=120ms flash gone; new page stands dented, its
  masthead (§6.11) already in place → its below-fold
  plates arm their etches (§6.7).
- **State matrix (v2).** *Rest:* content. *Hover:* n/a.
  *Focus:* focus is never held by the skeleton; on landing,
  focus moves to the new page's masthead skip target per
  the router's contract. *Active:* n/a. *Scrolled-past:*
  n/a. *Disabled / no-JS:* no skeleton performance (server
  renders content), no flash. *Touch:* identical.
- **Breakpoints (v2).** Skeleton anatomy follows each
  size's real layout (the blocks are generated from the
  same grid tokens, §4).
- **Edge cases & failure modes (v2).** *Back/forward
  cache:* a bfcache restore shows the page exactly as left
  — dents, temperatures, etched plates intact (§1: history
  is thermal, the browser's cache agrees). *Slow plate on
  a fast page:* plates resolve independently; the page is
  never held by its slowest plate.
- **Accessibility spec (v2).** Skeleton containers carry
  `aria-busy="true"` and resolve to real content in place;
  the flash is `aria-hidden` and is suppressed under
  `prefers-reduced-transparency` as well as reduced motion
  (a white flash is a photosensitivity consideration even
  at 120ms — the gate requires the suppression, not a
  debate about it).
- **Tokens consumed (v2).** `--iron-deep`, `--steel`,
  `--steel-pale`, `--spark`, `--ease-etch`.

### 6.17 The specimen record — assay lines

- **What & why.** Every piece on the site carries its
  record: a ruled list of assay lines — METEORITE, CLASS,
  NICKEL, LAMELLAE, MASS, FELL / FOUND, PATTERN SEED — set
  in mono, label left, value right, hairlines between. It
  is the theme's data soul: §1 law 2's single source, from
  which the showcase's pattern (§6.4), the counters'
  figures (§6.14), the cards' assay lines (§6.13) and the
  form's iron list (§6.15) are all generated. It belongs
  because a theme whose law is *figures are facts* needs
  the fact-sheet itself as a designed element, not a
  database afterthought.
- **Structure.** A `<dl>` of assay rows on the piece's
  plate (and, in summary form, inside §6.4's assay column).
  Row: label apparatus 11px `--band-deep` (graphical
  register — the *values* carry the reading), value mono
  15px `--edge`, hairline `--steel-pale` beneath. The
  PATTERN SEED row prints the seed as a short hex string —
  the crystal's fingerprint, shown openly: any visitor can
  check that two pieces' patterns differ because their
  seeds do. Cooling time prints in words in the record's
  prose line ("COOLED AT ABOUT THREE DEGREES PER MILLION
  YEARS") and as a figure in §6.14 — two printings, one
  value, gate-checked.
- **Motion spec.** The record does not animate, with one
  exception: when §6.4's showcase completes (q=1), the
  record's LAMELLAE row's hairline inks from `--steel-pale`
  to `--band` over 600ms `--ease-etch` — the assay
  acknowledging the pattern it predicted. Otherwise the
  record is the stillest element on the page: the Assay
  does not perform.
- **States.** Printed (always). The LAMELLAE acknowledgment
  state (post-showcase) persists for the session.
  Hover/focus: rows are not interactive; a row that is a
  link (METEORITE → the fall's own page, §7) inks its
  value on hover per §11.
- **Content merge.** The record is not *about* the content;
  in this theme it *is* the content's warrant. Cards,
  counters, patterns and forms are its printings — the
  merge is total, and §10's three-printings audit exists
  to prove it on every build.
- **Failure fallback.** No JS: the record prints complete
  (it is server-rendered text; there is nothing to fall
  back *from*). A missing field in the data: the row is
  omitted and the record's foot prints "ASSAY INCOMPLETE —
  THE BENCH DOES NOT GUESS" (§12's fixed string) — an
  absent fact is stated, never interpolated.
- **Reduced-motion variant.** Identical, minus the LAMELLAE
  ink (applied instantly at showcase completion, which
  itself is static in this variant).
- **Performance budget & mobile variant.** Text only.
  Mobile: rows stack label-above-value at <400px widths
  (a two-column assay on a narrow plate would crush the
  values — the figures outrank the grid).
- **Choreography timeline (v2).** Static, except: showcase
  q=1 → t=0 LAMELLAE hairline inks 600ms → record at rest.
- **State matrix (v2).** *Rest:* printed. *Hover:* linked
  values ink. *Focus:* linked values take §11's ring.
  *Active:* n/a. *Scrolled-past:* printed. *Disabled:*
  n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥768px: two-column rows. <768px:
  two-column until 400px, then stacked (above).
- **Edge cases & failure modes (v2).** *Two pieces from
  one fall:* records share METEORITE/CLASS/NICKEL and
  differ in MASS, LAMELLAE (cut angle changes apparent
  width — the record prints the *measured* width per
  piece, and §8.2's example shows the two printings
  agreeing with their photographs) and SEED. *A piece
  whose provenance is contested:* the record prints the
  contest ("FOUND — ATTRIBUTED") — the Assay records
  uncertainty in the same type as certainty, labelled.
- **Accessibility spec (v2).** `<dl>` semantics with
  `<dt>`/`<dd>` pairs; values are never conveyed by colour
  or position alone; the seed string is selectable text
  (a fingerprint you cannot copy is a picture of one).
- **Tokens consumed (v2).** `--band-deep`, `--band`,
  `--edge`, `--steel-pale`, `--ease-etch`.

### 6.18 The unfallen page — 404

- **What & why.** The 404 is an unetched plate of
  `--iron-deep`: no pattern, no ember, one apparatus line
  and the fixed heading (§12): "This iron has not fallen."
  Beneath it, two plain lines in the Assay's voice and the
  two nearest real destinations as struck chips (the bench,
  the record index). It belongs because a missing page in
  this world is not an error cartoon — it is a piece of sky
  that never arrived, and the honest response is a dark
  plate and directions, not a performance.
- **Structure.** The masthead (§6.11), one centred plate:
  heading in Archivo 900 `--band` (not `--edge` — the
  unfallen page is dimmer than any real page), the
  requested path printed in mono as an apparatus line
  ("SOUGHT: /gibeon-no-9"), two lines of prose, two chips.
  No pattern field is generated — generating a crystal for
  a page that does not exist would break §1 law 2 in its
  purest form.
- **Motion spec.** None, by specification. The page's
  choreography is *absence*: no strike (the session's
  strike is not spent on a void), no etch, no ember. The
  cooling bar (§6.5) renders its segments for the site's
  real plates with the figure line reading the path's
  honest state: no temperature is printed for a page that
  is not a plate.
- **States.** Rest only. Hover/focus on the chips: §11's
  standard press and ring — the furniture works even where
  nothing else does.
- **Content merge.** The sought path is the page's
  content; the chips are the site's real nearest plates.
  Nothing is decorated.
- **Failure fallback.** The 404 *is* a fallback; its own
  fallback is that it must render with every system down —
  no JS, no fonts (system stack, still dim, still legible),
  no pattern. It is the most robust page on the site, by
  design.
- **Reduced-motion variant.** Identical (there is no
  motion to reduce).
- **Performance budget & mobile variant.** The lightest
  page on the site; mobile identical, chips stack.
- **Choreography timeline (v2).** None — t=0 is the whole
  timeline, and the spec says so rather than inventing one.
- **State matrix (v2).** *Rest:* still, dim, complete.
  *Hover/focus/active:* chips per §11. *Scrolled-past:*
  n/a (the page fits one screen by construction; if a
  long path wraps it taller, it scrolls as plain iron).
  *Disabled / no-JS:* identical. *Touch:* identical.
- **Breakpoints (v2).** One composition at all sizes;
  heading 40px ≥768px, 32px below.
- **Edge cases & failure modes (v2).** *A sought path that
  once existed (a sold piece's retired URL):* the plate
  adds one line — "IT FELL, AND WAS CLAIMED." — with the
  record's link: the Assay distinguishes *never existed*
  from *no longer here*, because provenance is its whole
  job.
- **Accessibility spec (v2).** Heading is the `<h1>`;
  status is conveyed in text, never by the dimness alone;
  contrast `--band` on `--iron-deep` 4.92:1 at display
  size (large-text licensed, §2) with prose in `--edge`
  at 10.4:1.
- **Tokens consumed (v2).** `--iron-deep`, `--band`,
  `--edge`, `--steel-pale`.

## 7. Page application map

- **Home.** The full descent as designed: hero plate
  (§6.12) → etching showcase (§6.4) for the featured piece
  → blade cards (§6.13) → formation counters plate (§6.14)
  → the record of the house iron (§6.17, summary) →
  commission plate (§6.15) → cold mirror footer (§6.10).
  The home page is the theme's reference build; every other
  page type is a subset that keeps the descent contract
  (§4): hot head, working plates, mirror foot.
- **Listing (the bench).** Cards (§6.13) in a single grid
  plate, filter slips (§11) that re-lay the grid — the
  bench is re-arranged, never re-paginated mid-read.
  Markers and bar treat the listing as one plate (its
  segments count pages of *plates*, not of products).
  Sold pieces keep their places (§6.13). The listing's
  apparatus head prints its own count from the DOM ("ON
  THE BENCH — 9 PIECES, COUNTED FROM THE BENCH ITSELF").
- **Detail (the piece).** The showcase grammar at full
  size: photograph + etching overlay (§6.4, unpinned on
  detail pages — the pin belongs to the home page's
  demonstration; here the pattern is printed complete and
  the visitor's own scroll etches nothing, because this
  piece's formation is not a demo) → the full specimen
  record (§6.17) → its dents (§6.9 applies to the detail
  hero image too — handled pieces show handling) → the
  commission plate pre-set to this piece (§6.15) → footer.
  Provenance prose sits between record and commission:
  the fall's story, in the Assay's prose register (§12).
- **About (the forge).** The maker's plate: portrait
  photograph in a hammered frame (§6.13's frame treatment,
  untilted — a person is not a blade), the bench's book in
  figures (§6.14 counting commissions completed, falls
  worked, years at the bench — all from the record), and
  the fixed materials line (§12). No showcase pin: a
  biography is not a product demonstration.
- **The fall (collection story).** One meteorite's own
  page: its find story, its class record (§6.17 for the
  parent body), and every piece cut from it as cards —
  the one page where several records legitimately share
  lines (§6.17's two-pieces rule), and where the pattern
  fields of sibling pieces are generated side by side so
  the visitor can *see* one crystal cut at different
  angles: the theme's quietest and strongest page.
- **Contact / commission.** §6.15's plate alone with the
  masthead and footer — a single-purpose descent: the
  form plate is warm (its fields take §6.8 warmth) and the
  footer still arrives cold. No cross-sell plates may be
  inserted between form and footer (§9, failure 11).
- **404.** §6.18. **Search / archive.** A record index:
  assay-line rows (§6.17's grammar) as results, counted
  from the DOM, empty state in §12's voice ("NO IRON IS
  RECORDED UNDER THAT NAME."). No cards, no pattern —
  an index is the Assay's purest page.

## 8. Worked examples

### 8.1 The hero, end to end — a bladesmith's home page

The smith is **Auerbach & Fall**, working Gibeon iron. The
hero plate (§6.12): headline "IRON THAT FELL" (13 glyphs —
stagger compresses to fit the 1400ms cap: 300 + 12×78 +
90 ≈ 1326ms). t=0: the composition stands readable —
standfirst in mono: "Blades forged from the Gibeon fall,
Namibia. Each pattern exists once. The bench book is open
below." The strike lands at t=300ms (§6.1): 3px shake,
16 sparks from the headline's centre, letters denting in
sequence beneath the shake — I-R-O-N struck by t≈610ms,
the space, T-H-A-T by ≈890ms, FELL complete at 1326ms,
its final L's micro-sparks dying at ≈1620ms. At last
letter +200ms, the specimen line's rules draw (§6.7
grammar, 600ms): "GIBEON — FINE OCTAHEDRITE (IVA) —
COOLED AT ABOUT THREE DEGREES PER MILLION YEARS" — every
word of it from the record (§6.17). The tally at the
plate's foot (§6.14): "4,000,000 YEARS TO COOL" (counts
2200ms, magnitude band), "7.9% NICKEL" (a decimal counter —
counts to one decimal place, tabular, 1400ms), "31 BLADES
FROM ONE FALL" (900ms) — each with its assay source line.
First scroll: the markers (§6.3) begin at full ember; the
bar's head (§6.5) reads 1150°; the ember (§6.6) breathes
at 4s beside PLATE 01. A returning visitor sees none of
the ceremony: the plate stands struck, counters printed,
temperature at their deepest p. A reduced-motion visitor
sees the same plate, printed, and loses no fact.

### 8.2 Mid-page — the etching showcase on the same page

Below the hero, the featured piece: "GIBEON BLADE № 3".
The plate pins at 140vh (§6.4). The photograph: the blade
flat on iron, shot from directly above (the listing's
angle rule, §9, is satisfied — № 3's card shot was from
the edge; this plate's is from above; never the same angle
twice). The apparatus states the scale: "PATTERN AT 12:1 —
BANDS 0.3 MM". Scrolling the pin: q 0→0.55 kamacite bands
draw at +60° from the blade's tip nucleus; taenite
interleaves from q=0.3; cross-bands close the field by
q=1. Beside the panel, the assay column stands still:
METEORITE — GIBEON · CLASS — IVA FINE OCTAHEDRITE ·
NICKEL — 7.9% · LAMELLAE — 0.3 MM · MASS — 412 G · FOUND
— 1836, NAMAQUALAND · SEED — 9F3A·C41B. At q=1 the
record's LAMELLAE hairline inks (§6.17) — prediction,
confirmed. The visitor scrolls back *inside* the pin: the
bands un-draw, the demonstration rewinding honestly; the
moment they pass the pin's foot, the pattern locks
(§1) — further down, № 3's card (§6.13) shows the same
blade, edge-shot, pattern printed, with two dents where a
previous visitor struck it in an earlier session of the
same sitting (§6.9's session rule). The counters plate
below repeats "0.3 MM" as a counted figure — the third
printing of one measurement (§6.17's audit).

### 8.3 Conversion — commissioning a blade

The visitor reaches the commission plate (§6.15) at
p≈0.8: the page is cool now, markers at `--band-deep`,
the bar's figure near 60°, and the form's warmth (§6.8
field flares) reads *stronger* against the cold page —
the bench is the last warm place on the site, by thermal
design. They choose: piece — BLADE (chip dents, 150ms);
iron — the record offers GIBEON and MUONIONALUSTA (CANYON
DIABLO is listed in the record as a fall the forge has
worked but holds no stock of, so it does not appear as a
choice — §6.15's rule; its absence is explained in one
apparatus line, not hidden); etching — "FOR M." (6
characters, inside the 40 cap); the summary line updates:
"ONE BLADE — GIBEON IRON — ETCHED WITH 6 CHARACTERS".
Email mistyped without "@": submit strikes, the plate
answers in the Assay's voice — "THAT DIRECTION WILL NOT
REACH ANYONE — THE @ IS MISSING FROM IT." — the direction
field's rule turns `--ember-deep`, every other field keeps
its value. Corrected; submit again: the button dents,
four sparks, "STRIKING…" for the true submission beat,
then the plate turns (700ms) and lands as the confirmation:
the visitor's selections as assay lines, and last, struck
at 90ms `--ease-strike`, the commission number from the
bench book. Below it, the footer is already visible —
mirror-bright, 18°, the record printing "PLATES — ALL ·
FINAL TEMPERATURE — 18°C". The commission was made at the
cold end of a cooling page: considered, finished, singular.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The starfield.** A starry-sky background, nebula
   gradient or planet clip-art anywhere. The theme's sky
   has already happened; the page is the iron *after* it
   landed. Cure: the ground is `--iron`, full stop. Space
   is provenance (the record, §6.17), never wallpaper.
2. **Spark confetti.** Sparks on scroll, on hover, on
   every click, twinkling UI stars. Cure: the §5 census —
   sparks exist only at the strike, the struck letters and
   deliberate card strikes, with stated counts and 600ms
   lives. A spark is struck metal; metal is not spent on
   decoration.
3. **The tiling crystal.** The Widmanstätten pattern as a
   repeating background tile, or — worse — a stock "metal
   texture" PNG. Real crystal never repeats and never came
   from a texture pack. Cure: per-plate generated fields
   from specimen seeds (§4), non-repeating, different on
   every plate, angles locked to +60°/−60°/0°.
4. **Wrong angles.** Lamellae drawn at 45°/90° (a tartan)
   or random angles (a scribble). Kamacite/taenite
   intergrow on octahedral planes; the drawing's discipline
   *is* the theme's credibility. Cure: the angle law in
   §6.4; the gate measures two bands in the built showcase.
5. **Ember as accent colour.** Orange CTA buttons, orange
   links, orange sale badges. Ember is a temperature with
   a budget (§2) and a curve (§6.5); the moment it
   decorates furniture it stops meaning heat. Cure:
   actions are struck chips in `--edge`/`--steel` (§11);
   ember appears only where the page is hot.
6. **Text over crystal.** Headlines or body copy set across
   the pattern field "for texture". The pattern is a
   specimen, not a backdrop; text over it is a museum label
   glued to the artefact. Cure: §6.12's composition —
   pattern beside text, in its own panel, always.
7. **The weightless hover.** Cards that lift, float and
   cast soft shadows like paper in a breeze. Ironware does
   not hover. Cure: §6.13's 3° bench tilt, hard offset
   shadows, and §6.8's warmth — the card is *turned*, never
   lifted.
8. **Shake abuse.** The impact shake on buttons, errors or
   section entries. One blow per session (§6.1) is a
   founding event; a second shake anywhere is a cartoon.
   Cure: presses dent (§11, 1px, no shake); errors state
   themselves in type.
9. **Invented awe.** "BILLIONS OF YEARS OLD!" in display
   type, cooling times that vary between pages, a nickel
   percentage that disagrees with the record. Cure: §1
   law 2 + §6.17's single source + §3 law 2 (figures at
   data size). Awe is the assay's job.
10. **Chrome cosplay.** Mirror gradients, rainbow
    iridescence, liquid-metal blobs — the theme's polish
    is one flat mirror in one footer, earned by descent.
    Cure: `--mirror` exists in exactly one plate (§6.10);
    gradients are refused except the footer's crawl and
    the dents' radial marks, both specified to the pixel.
11. **The reheated page.** Elements that glow again when
    scrolled back into view, counters that re-run, etches
    that redraw on every pass. Cure: §1 law 1 — formation
    is permanent; the gate's scroll-back test (§10) walks
    the page up and expects *nothing* to happen.
12. **Cross-sold cold.** Upsell plates, "pairs well with"
    carousels or countdown offers inserted between the
    commission plate and the footer. The descent ends in a
    decision and a mirror; commerce shouting at the cold
    end breaks the thermal contract. Cure: §7's map —
    nothing stands between §6.15 and §6.10.

## 10. Quality gate

Blocking unless marked (A = advisory):

- [ ] **One-way audit:** scripted scroll down then up:
  every marker, the bar head and the printed temperature
  are functions of max-depth only; nothing reheats,
  re-counts or re-etches on the upward pass (the §6.4 pin
  is the sole licensed reversal, and only inside the pin).
- [ ] **Three-printings agreement:** for the featured
  piece, lamellae width, nickel and cooling figure agree
  across §6.4's apparatus, §6.17's record and §6.14's
  counters — sampled from the rendered page, not the
  source.
- [ ] **Pattern audit:** every plate's field is generated
  from its record seed; no field repeats within itself;
  two bands in the showcase measure +60°/−60° ±2°; no
  background image files exist in the build.
- [ ] **Spark census:** emitters in the built page =
  strike (1) + letters (≤ glyph count) + card strikes
  (pointer-only). Total spark lifetime ≤ 600ms each; no
  scroll- or hover-triggered spark exists.
- [ ] **Thermal budget:** ember-family pixel share sampled
  at hero ≤3%, mid-page ≤1.5%, footer = 0% (grep the
  rendered footer for ember hexes).
- [ ] **Printed-state test:** JS disabled — headline
  struck and dented, pattern printed on the showcase
  panel, counters at full value, form submittable, footer
  complete with its static gradient.
- [ ] **Watchdog test:** rAF frozen — strike settles by
  1200ms, letters by 1600ms, etch frames by their 1000ms
  rule, counters by duration+400ms; nothing is left armed,
  masked or unetched.
- [ ] **Contrast audit:** text pairings measured against
  §2's table; no body text in `--ember` or `--band-deep`;
  no text set over the pattern field anywhere.
- [ ] **Motion audit:** easing grep — only the five named
  easings; pins per page ≤1; marquee, blur reveals and
  kinetic type absent; shake occurs exactly once per
  session and is suppressed for focus-first visitors.
- [ ] **Reduced-motion pass:** full walk — page opens
  struck and cold-ready, pattern printed, counters
  printed, markers stepping discretely, footer still.
- [ ] (A) **Five-second test:** a first-time viewer, shown
  the hero for five seconds, says "a smith" and "the name
  was struck into metal" unprompted.
- [ ] (A) **Cold-end test:** a viewer who reaches the
  footer describes the page as "finished" or "quiet"
  without being offered either word.

## 11. Component inventory

Every component a real site in this theme needs, with its
themed treatment. Global rules: radius **0** everywhere
except dent marks (§6.9) and ember dots — plates are cut,
not rounded; shadows are hard offsets in `--iron-deep`
(0 2px 0), never soft glows; focus ring is a 2px `--edge`
outline offset 3px on iron and steel alike (the mirror
footer uses `--iron`, §6.10).

- **Buttons.** *Primary:* a struck chip — `--steel` fill,
  1px `--steel-pale` rim, Archivo 800 14px uppercase label,
  48px tall. Press: 1px translate down + a dent bloom at
  the press point (150ms `--ease-strike`, no sparks — a
  button is furniture, §9 failure 8) and the label's colour
  steps `--band` → `--edge`. *Secondary:* mono text link,
  hairline underline that inks on hover. *Refused:* pill
  buttons, gradient buttons, ember buttons (§9 failure 5),
  icon-only buttons without labels.
- **Inputs & textarea.** Etched fields (§6.15): `--steel`
  recessed fill, 1px `--steel-pale` hairline, label above
  in apparatus mono (always visible; no floating labels,
  no placeholder-as-label). Focus: hairline inks to
  `--edge` 200ms `--ease-etch`, label ember warms one stop
  (§6.8). Textarea grows by lines. Error: rule turns
  `--ember-deep`, message beneath in the Assay's voice.
- **Selects.** Refused as native dropdowns: choices are
  struck-chip radio rows (§6.15). Where a platform forces
  a native select (a payment country's name), it is styled
  as an etched field and accepted as a foreign object at
  ≥48px — the theme admits the compromise in writing
  rather than pretend the object is forged.
- **Radios & checkboxes.** Radio = a struck chip row: the
  chosen chip carries a 1px dent and its label in `--edge`;
  unchosen chips rest in `--band`. Checkbox = a small
  square plate that takes a miniature etched cross (two
  hairlines, ±60° — the pattern at check-box scale) when
  checked. Never the platform's rounded tick.
- **Tables.** **Refused** as data grids. Tabular truth is
  set as assay record lists (§6.17) — label left, value
  right, hairline between. A genuine many-column dataset
  does not belong to this theme (§1); the one sortable
  surface, the archive index (§7), sorts its record rows,
  not a grid.
- **Badges & tags.** Refused as coloured pills. A status
  is a printed line in the record ("ON THE BENCH", "SOLD —
  IN THE VAULT") or, on a card, §6.13's status line. No
  count bubbles; tallies live in §6.14's counters, at data
  size, with sources.
- **Alerts.** A plate-level note: an apparatus inscription
  at the plate's head on `--iron-deep`, message in the
  Assay's voice, `--ember-deep` rule at its left for
  errors. It does not push content mid-read (it is placed
  at the head of the plate it concerns) and never appears
  as a toast (below).
- **Modals.** Refused. A piece's enlargement is its detail
  page (§7) reached by the strike transition (§6.16); a
  confirmation is §6.15's struck plate. The one overlay in
  the theme is the mobile nav plate (§6.11), which is
  furniture, not a dialog.
- **Toasts.** Refused outright. Feedback is written where
  it belongs: dents on cards, lines in records, the struck
  confirmation. A message that vanishes in four seconds is
  heat without mass; the bench writes things down.
- **Tabs.** Refused. Plates are sequential (§4); alternate
  views (pieces by fall) are filter slips that re-lay the
  grid — the visitor watches the bench rearranged, not a
  panel swapped behind a tab strip.
- **Accordions.** One licensed form: the care-and-provenance
  plate's clauses open as *seams* — a clause's body etches
  in under its hairline (400ms `--ease-etch`), one open at
  a time. Used for care instructions and terms only; never
  for primary content or the record.
- **Pagination.** The plate system itself: "PLATE 2 OF 3"
  apparatus line + named next/previous chips (§6.16's
  transition between them). Numbered pills are refused.
- **Breadcrumbs.** Refused. The site is a bench, not a
  warehouse: masthead (§6.11) + the detail page's "next
  plate" line carry orientation.
- **Search.** Lives on the archive plate (§7) as an etched
  field whose results re-lay the record rows; the query is
  a line etched on the plate, never an expanding icon.
- **Loader.** The unetched skeleton (§6.16). Spinners are
  refused in all forms — iron does not spin while it waits.
- **Progress.** The cooling bar (§6.5) is the only progress
  component. No bars, percentages or step indicators
  elsewhere; a multi-field commission is one plate (§6.15),
  not a wizard.
- **Cards.** §6.13's blade plates. No other card exists.
- **Tooltip.** Refused. Anything worth saying is printed
  on the plate — apparatus lines exist for exactly this.
- **Avatar / byline.** The maker is represented by the
  struck mark (§6.11) and the bench book's figures
  (§6.14), never a circular headshot. A portrait belongs
  on the forge page (§7), framed and untilted.

## 12. Content & copywriting voice

Two registers, kept apart as strictly as the two typefaces
(§3 law 1).

**The Smith** (Archivo contexts — the mark, headlines, the
closing line): brief, concrete, declarative; names the
material or the act, never a benefit. ✓ "Iron that fell" /
✓ "One blade, one sky" / ✓ "The bench book is open" /
✗ "Unleash the power of the cosmos" / ✗ "Own a piece of
the universe!!" — and note: the Smith uses no exclamation
marks either; a hammer does not shout, it lands. One clause
is a headline; two is a sentence asking to be the standfirst.

**The Assay** (mono contexts — labels, records, errors,
apparatus): plain, exact, sourced. It states measurements
and keeps receipts. ✓ "Gibeon. Fine octahedrite, IVA.
Nickel 7.9%. Cooled at about three degrees per million
years." / ✗ "Forged from an ancient star that fell from
the heavens in a blaze of cosmic fire!" The Assay's awe is
in its figures; adjectives are uncalibrated instruments
and it does not use them.

- **Labels.** Verbs of the bench: "Strike the commission"
  (submit — the one licensed use of the strike word outside
  §6.1, because submitting *is* the visitor's blow),
  "View the piece", "The bench", "The falls", "The record",
  "The forge". ✗ "Add to cart", ✗ "Buy now", ✗ "Submit".
- **Error voice.** The Assay, naming the defect and the
  remedy, never the visitor's competence: ✓ "That direction
  will not reach anyone — the @ is missing from it." /
  ✓ "The Gibeon was claimed while you wrote. The bench
  offers Muonionalusta, or waits." / ✗ "Invalid input!"
  An error is a property of the letter, not of the writer.
- **Empty states.** Stated as unworked iron, never as
  apology: ✓ (archive search) "No iron is recorded under
  that name." / ✓ (bench filter) "Nothing from that fall
  is on the bench." / ✗ "Oops, nothing here 😢".
- **Figures.** Every number traces to the record (§6.17).
  Cooling times print in millions of years as figures in
  counters ("4,000,000 YEARS") and in words in prose ("about
  four million years") — the two printings must agree (§10).
  Nickel to one decimal, always ("7.9%", never "8%" — a
  rounded assay is a wrong assay). Percentages are licensed
  for composition only (the Assay's percentages), never for
  progress, discounts or urgency — the cooling bar (§6.5)
  prints degrees, not percent.
- **Provenance honesty.** A find is not a fall: copy says
  FELL only where the record says the fall was witnessed,
  FOUND everywhere else (§6.17). "Ancient" is banned as a
  bare adjective — the record's figures carry the age or
  the copy stays silent.
- **Fixed strings (verbatim).** 404 heading: "This iron
  has not fallen." Retired-piece line: "It fell, and was
  claimed." Pattern line: "The pattern in this blade exists
  once." Footer closing: "Cooled. Finished. Singular."
  Incomplete-assay line: "Assay incomplete — the bench does
  not guess." These strings are the theme's furniture;
  translations translate them as units.

## 13. Full-page scroll choreography map

The home page, top to footer. (Reverse pass: by §1's law,
scrolling up triggers *nothing* — no reheat, no re-etch,
no re-count; the only scrub that follows the visitor back
up is §6.4's pattern inside its pin, and §6.13's edge
polish, which is a light state, not a formation state.)

1. **t=0, load.** The composition stands readable (§6.12);
   masthead in place (§6.11); markers hot; bar at 1150°.
2. **t=300ms.** The strike (§6.1) and the letters (§6.2):
   the page's only loud moment.
3. **t≈1600ms.** Specimen rules drawn; hero at rest; the
   ember breathes at 4s beside PLATE 01 (§6.6).
4. **First scroll.** Tally counters fire (§6.14); the
   cooling begins — every instrument leaves its maximum
   together, because there is one temperature (§6.5).
5. **Showcase plate.** Etch frame (§6.7), then the pin:
   140vh in which the crystal forms on the blade (§6.4)
   while the assay column stands still — the page's
   centre of gravity, deliberately the slowest beat.
6. **Pin exit.** The pattern locks (§1). The record's
   LAMELLAE line inks (§6.17). From here, nothing on the
   page is unformed again.
7. **Bench plate.** Cards drop in with forge weight
   (§6.13), edges scrubbing to polish as they centre;
   the visitor's first card strike (§6.9) usually lands
   here — the page's second, smaller sound.
8. **Counters plate.** Deep-time figures count once
   (§6.14) under a plate whose markers are already at
   `--ember-deep`: the numbers are hot facts on a cooling
   page, and the contrast is the point.
9. **Record plate.** Stillness. The house assay (§6.17)
   with no motion at all — the choreography rests here so
   the conversion plate's warmth can register.
10. **Commission plate.** The last warm place (§8.3):
    field flares and chip dents against a cold page;
    markers at `--band-deep`; bar near double digits.
11. **Final approach.** The last plate is the sparsest
    (§4's density law); the ember (§6.6) stops breathing
    at p≥0.92 somewhere in this stretch — most visitors
    will not notice the exact moment, which is correct:
    fires go out that way.
12. **Footer.** p=1: bar head turns mirror as the footer's
    crawl crosses its bands (§6.10) — instrument and
    destination in the same 2400ms — then the page's
    permanent rest: cold, finished, singular.

## 14. Whole-page performance budget

- **Total page weight (home):** ≤ 820KB transferred —
  fonts (Archivo variable + Plex Mono, subset to Latin +
  figures) ≤ 120KB; pattern SVGs generated inline, ≤ 30KB
  per plate, ≤ 120KB per page (the seed generator is code,
  ≤ 6KB, not data); product photography ≤ 90KB per image,
  ≤ 4 above the fold's plates; JS ≤ 55KB (one loop, one
  observer set, the spark canvas, the dent store); CSS
  ≤ 45KB.
- **Frame budget:** the shared loop's per-frame work ≤
  1.6ms on a mid-tier phone: one `--temp` write, ≤ 90
  dashoffset writes (showcase frames only), one tilt
  transform, parallax transforms for the visible plate
  only. No layout reads inside the loop except the cached
  plate registry (recomputed on resize/insertion only).
- **Long tasks:** none > 50ms after load; pattern
  generation for below-fold plates is deferred to idle
  callbacks, one plate per task.
- **Cut order when the budget breaks:** (1) the breathing
  ember's pulse (it becomes §6.3's static relay); (2)
  showcase band count at tablet sizes; (3) card tilt
  (edges print at 55%); (4) hero pattern panel resolution.
  **Never cut:** the strike (it is the theme's founding
  event, and it is cheap), the cooling law's instruments,
  any fallback or watchdog, the record.
- **Measurement:** budget is checked on the built home page
  with a throttled mid-tier profile; the frame figure is
  the loop's own instrumented average over a full descent,
  printed in the build report beside §6.5's curve — the
  theme measures its performance the way it measures its
  iron: once, in writing.

## 15. Build-order checklist

1. **The record first.** Author the specimen data object
   (§6.17) — meteorites, classes, nickel, lamellae, seeds,
   stock. Nothing visual exists before the facts do; every
   later step consumes this object.
2. **The static cold page.** Build every plate complete at
   rest: struck headline (CSS dent), printed pattern on
   the showcase, counters at value, form working, mirror
   footer. This is the no-JS product; it must already be
   the theme, merely unperformed. Gate: §10's printed-state
   test passes on this build alone.
3. **Palette and type tokens** exactly as §2/§3, including
   the closed derived list; grep for undeclared hexes.
4. **The shared loop** with the max-depth function `p`,
   the declared cooling curve and lerp 0.085; wire §6.3's
   markers and §6.5's bar to the single `--temp`.
5. **The strike and letters** (§6.1, §6.2) with session
   flag, focus-cancellation and both watchdogs.
6. **Etch frames** (§6.7) with the observer and instant-
   etch catch-up rules.
7. **The showcase** (§6.4): pattern generator from the
   record seed, pin, formation order, focus-skip.
8. **Cards and dents** (§6.13, §6.9): tilt loop, dent
   layer, session persistence, sold-state refusals.
9. **Counters** (§6.14) with magnitude bands and source
   lines generated from the record.
10. **The commission plate** (§6.15): record-driven iron
    list, live summary, error-keeping, struck confirmation.
11. **The ember** (§6.6) and rekindle (§6.8) — the warmth
    layer last among motions, because it tunes against
    everything else's rest states.
12. **Skeleton and transition** (§6.16) from the real
    layout tokens.
13. **The 404** (§6.18) and archive index (§7).
14. **Reduced-motion pass:** every variant in §6 walked
    end to end; the printed page and the performed page
    compared fact by fact.
15. **The gate** (§10) run by someone who did not build
    the page — the Assay does not certify its own iron.
