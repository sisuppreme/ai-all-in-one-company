# 79. Vent Field Survey — Expanded (50x)

An ROV dive log to a hydrothermal vent field, built as a working vehicle's
survey rather than a brochure about one. This expansion preserves the
original entry exactly — same concept, same five palette anchors, same two
type families, all ten original signature elements deepened, not redesigned —
and adds the page-family elements, choreography timelines, state matrices,
breakpoint behaviour, edge cases, accessibility specs and token lists the
50x standard requires.

---

## 1. Concept & world

**The world.** Two and a half kilometres below the surface there is no
sunlight, no weather and no colour that the water has not filtered out.
What exists down there exists because a vehicle brought light with it. Vent
Field Survey is a website built inside that fact: the page is the dive.
The visitor does not scroll through a document about a hydrothermal vent
field — they pilot the ROV *Meridian* down to the Acheron Field, station by
station, and the page only shows them what the vehicle's own light, at the
vehicle's own depth, would actually reach. Darkness here is not a theme
colour. It is the medium. The light cone is not decoration. It is the only
reason anything is visible at all, and the theme never lets the visitor
forget it.

The dive has a shape, and the page keeps it: **descend, survey, surface
with samples.** Six survey stations lie along the bottom traverse. Each
station is a section; each section reports through its own instrument panel
before it says anything else; each completed station earns one labelled jar
in the sample basket fixed in the page corner. The last section is not a
call to action. It is titled "Surface with Samples," and it shows the full
basket, the manifest, and the dive's totals — because surfacing with
something is what a survey dive is *for*.

**The theme's one law: *the instruments report the place, and nothing is
lit that the vehicle has not reached.*** Every number on the page — depth,
temperature, pressure, dissolved oxygen, jar weights, bottom time — traces
to the single declared dive record in §5.1, and every figure can be
re-derived by the visitor from values printed beside it (pressure is
depth ÷ 10 + 1 bar, and the page says so). Every dark or dim state is a
JS-armed enhancement over a complete, fully lit, fully printed page: the
DOM ships as the dive with the lights on, and the darkness is applied only
after the vehicle has demonstrably arrived. If any trigger, sensor or
script fails, the page's failure mode is *more light*, never less content.

**The dive, as the page tells it.** ROV *Meridian*, operated by Meridian
Subsea from the support ship RV *Northlight*. Dive № 214, launched
14 March, 03:40 UTC. Target: the Acheron Vent Field, seabed at 2,512 m.
Six stations: the Smoker Garden, the Crab Fields, the Plume Traverse, the
Mussel Beds, the Old Chimney, the Shimmer Flats. Bottom time 400 minutes
of a 500-minute dive (55 down, 400 on the bottom, 45 up — the arithmetic
is printed in the manifest and must reconcile everywhere it appears).

**Best-fit sites and audiences.** Marine research institutes publishing
cruise and dive reports; subsea robotics and ROV manufacturers whose
product pages are really capability surveys; ocean-documentary and
expedition projects that need the audience inside the dive, not watching a
trailer for it; deep-sea mining *assessment* and environmental baseline
surveys (the theme's sample-and-record discipline suits evidence-led
publishing); aquarium and museum deep-ocean exhibition microsites.

**When NOT to use it.** Not for anything that must be scanned in under
thirty seconds — a dive is a commitment, and this theme refuses to hurry.
Not for e-commerce checkout: the theme routes payment out entirely (§7),
because a basket you fill by scrolling must never be confused with a cart
you fill by buying. Not for surface-world subjects with no depth, pressure
or darkness in them — a bakery in this theme is not charming, it is a lie
about where the reader is. Not for audiences on very low-end devices as
the *only* version: the reduced and lit variants are complete, but if the
client cannot ship those honestly, choose another theme. And never for
content that needs to feel warm, sunlit or safe — the vent field is
magnificent and it is not safe, and the theme's honesty about that is the
product.

**The custodian rule.** The vehicle is a presence, not a mascot. The
manipulator arm crosses the beam exactly once (§6.6); the panels report in
checklist order, never in chorus; the theme permits itself precisely two
ambient loops (marine snow, plume shimmer) and no more. Restraint is how
the visitor knows something real is piloting this view.

---

## 2. Palette

Five anchors from the original entry, unchanged. Seven derived tokens,
each measured against the ground it will actually sit on. Contrast ratios
below are computed from the hex values for this expansion.

| Token | Hex | Role | Usage ratio | Pairing / contrast ruling |
|---|---|---|---|---|
| `--vent-black` | `#0B0D0E` | The water. Page ground, cone exterior, frame stock. | ~62% of pixels | Ground for every other token. Never a text colour on anything but sulphur or sonar fills. |
| `--shell` | `#E8E4DA` | Crab-shell white. Body text, headline text inside the cone, jar labels. | ~14% | On vent black **15.34:1** — the page's reading colour. On plume grey 5.28:1 (panel heads only, ≥14px). |
| `--sulphur` | `#D9A62E` | Sulphur yellow. Heat, caution, the sample action, station markers, focus rings. | ~6% | On vent black **8.76:1** — licensed for text and the primary action. Vent black on sulphur 8.76:1 (button label pairing). On plume grey 3.02:1 — **forbidden pairing**, never set sulphur on grey. |
| `--sonar` | `#6FA287` | Sonar green. Live-data colour: instrument values in range, all-clear states, the bathymetry dot, links. | ~8% | On vent black **6.67:1** — licensed for data text and links. On panel 6.28:1. Vent black on sonar 6.67:1 (badge pairing). |
| `--plume-grey` | `#565D60` | Smoker plume grey. Panel stock, frame brackets, hairlines, jar glass, disabled fills. | ~10% | On vent black only **2.90:1** — **never text, never an only indicator**; it is a material, not a voice. Shell on plume grey is the panel pairing (5.28:1). |

**Derived tokens.**

| Token | Hex | Derivation / role | Ruling |
|---|---|---|---|
| `--panel` | `#121517` | Vent black lifted one step. Instrument-panel and card stock. | Shell on panel 14.44:1; sonar on panel 6.28:1. Plume grey on panel 2.73:1 — frames and rules only. |
| `--cone-warm` | `#F2EDDC` | The light itself — shell warmed by the lamp. Cone gradient core, headline text at full illumination. | On vent black 16.62:1. Used as a *light value*, never as a flat background fill. |
| `--plume-text` | `#A8AEAF` | Plume grey lightened to speech. Captions, timestamps, secondary instrument labels. | On vent black **8.66:1**. This is the only grey allowed to talk. |
| `--sulphur-deep` | `#A67C1F` | Sulphur in shadow. Jar-seal wax, visited station markers, pressed states. | On vent black 5.12:1 — large labels and fills only, never body text. |
| `--sonar-deep` | `#4E7A63` | Sonar in shadow. Bathymetry line at rest, basket grid lines, footer rules. | On vent black 3.98:1 — lines and large data only, never small text. |
| `--snow` | `#E8E4DA` at 50% | Marine snow particles (§6.2). A value, not a surface. | Alpha token; never composited into text areas at >30% local density. |
| `--glass` | `#565D60` at 22% | Jar glass and cone-edge falloff tint. | Alpha token over `--panel` or `--vent-black` only. |

**Dark-mode behaviour.** There is no light scheme and no inversion: the
subject is a place where light does not reach, and a "light mode" would be
a photograph of the surface, not a variant of the dive. The theme's answer
to brightness needs is the **lights-on fallback** (§6.1): a declared,
fully-designed state in which the cone is lifted, the ground rises to
`--panel`, and every reading is printed statically. `prefers-contrast:
more` engages the same state. This is a ruling, not an omission, and §10
tests it.

**The sulphur census.** Sulphur is the colour of heat and of the one
action that matters (taking a sample). It is rationed: per viewport, at
most one primary action, one station marker, and heat data in a single
instrument panel may carry it. If everything is sulphur, nothing is hot.

---

## 3. Typography

Two families, from the original entry, unchanged. **Archivo** — the
expedition grotesque — carries everything a human says: headlines, body,
the dive log's voice. **JetBrains Mono** carries everything the vehicle
says: instrument values, depths, temperatures, jar labels, timestamps.
The division is absolute and is the theme's typographic law: **if a number
has a unit, it is mono; if a sentence has a feeling, it is Archivo.**

**Type laws.**

1. **Numerals are mono, always.** Every depth, temperature, pressure,
   weight, time and count on the page — including numerals inside prose —
   is JetBrains Mono with tabular figures. A depth set in Archivo is a
   defect on the §10 gate.
2. **Archivo never shouts in the dark.** Display sizes are large but
   weights stay 500–700; there is no Archivo black (900) in this theme —
   at 2,512 m nothing is that certain. Headlines are sentence case; the
   only uppercase Archivo on the page is the station name on a panel head,
   letterspaced as a label.
3. **Mono labels are uppercase, tracked, and small — and they never carry
   a sentence.** Instrument labels (`DEPTH`, `TEMP`, `PRESS`, `O₂ DISS`)
   are 11px, +0.14em tracking. The moment a label needs a verb, it moves
   to Archivo.
4. **The log speaks in past tense, the instruments in present.** Body copy
   (the Log register, §12) narrates completed action; panel values are
   always *now*. Type keeps the two tenses visually separate — Archivo
   italic is reserved for the log's asides and is never used for data.
5. **Nothing moves type.** The cone, the shimmer and the snow animate
   light and matter; letterforms never translate, scale or blur. Layout
   shift from animation is zero by construction (CLS contribution 0).

**Scale** (1.25 ratio, rem base 16px):

| Role | Family | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Display (hero depth statement) | Archivo 600 | 3.815rem / 1.04 | −0.01em | Set in `--cone-warm`; the depth numeral inside it is mono 600. |
| H1 (page / final section) | Archivo 600 | 3.052rem / 1.08 | −0.01em | "Surface with Samples" is the largest H1 after the hero. |
| H2 (station names) | Archivo 600 | 2.441rem / 1.12 | 0 | Always preceded by its instrument panel, never by an eyebrow. |
| H3 (sub-features) | Archivo 500 | 1.563rem / 1.25 | 0 | |
| Body (Log register) | Archivo 400 | 1rem / 1.65 | 0 | Measure 58–66ch; the cone, not the column, sets the reading width (§4). |
| Body large (station ledes) | Archivo 400 | 1.25rem / 1.55 | 0 | First paragraph of each station only. |
| Instrument value | JetBrains Mono 500 | 1.25rem / 1.2 | 0 | Tabular; unit follows in `--plume-text` at 0.75em. |
| Instrument label | JetBrains Mono 500 | 0.6875rem / 1.3 | +0.14em | Uppercase; `--plume-text`. |
| Jar label | JetBrains Mono 500 | 0.75rem / 1.35 | +0.02em | Specimen name in Archivo 500 0.875rem above the mono depth line. |
| Caption / timestamp | Archivo 400 italic or Mono 400 | 0.875rem / 1.5 | 0 | Italic = log aside; mono = recorded fact. Never both. |

**Font loading.** Archivo (400/500/600, latin) and JetBrains Mono
(400/500) subset and self-hosted, `font-display: swap`, total ≤118KB.
Fallbacks: Archivo → `system-ui, sans-serif`; JetBrains Mono →
`ui-monospace, "SF Mono", monospace`. Fallback metrics are close enough
that swap moves nothing the visitor is reading (law 5).

---

## 4. Layout language

**The cone is the grid.** The page is a single centred column, max 1120px,
but the *reading* width is set by the viewport-fixed light cone (§6.1):
at ≥1200px the cone's full-illumination core is ~640px across, and body
copy is set at 58–66ch to live inside it. Text that leaves the core is
still printed and still legible — the cone dims, it never hides (§6.1's
floor rule) — but the choreography assumes the visitor reads in the beam
and treats the margins as water.

**Fixed furniture.** Three things do not scroll, and the layout reserves
space for them before any content is placed:

- **The bathymetry rail** — a 72px margin column on the left (≥1200px)
  carrying the dive-profile line (§6.7). Below 1200px the profile moves
  into the header as a horizontal depth strip (§6.7 breakpoints).
- **The sample basket** — a fixed corner grid, bottom-right, 3 × 2 jar
  slots at desktop (§6.4). Content's right margin at ≥1200px is widened
  by 148px in the lower viewport zone so prose never passes *under* the
  basket; the basket never overlays text (§6.4 state matrix).
- **The depth gauge** — a mono readout docked to the basket's top edge:
  current depth, always current, always derived from §5.1's function.

**Station rhythm.** Each station section follows the same survey order —
instrument panel, station name, lede, body, camera frames, specimen card —
because a survey is a procedure and procedures repeat. Vertical rhythm is
a 8px base unit; stations are separated by 18–24rem of open water (dark,
snow only) so the descent *between* stations is felt as travel time. The
final section breaks the rhythm deliberately: full width, manifest table,
basket enlarged — the surface is a different kind of place.

**Density rules.** One developing idea per viewport: at any scroll
position, at most one station's panel is "live" (§6.8), at most one
camera frame is inside a plume zone's shimmer (§6.9), and the snow never
exceeds its density budget (§6.2). Whitespace in this theme is black
water, and it is a material: it is where the depth lives. Sections are
never compressed to fit a fold; the page is as long as the dive is deep,
and the bathymetry line says exactly where you are in it.

**Alignment.** Instrument panels align to a strict left mono column
(labels at fixed 11ch stops) — a checklist reads down, not across.
Specimen cards and camera frames hang on the body column's right edge at
desktop, like equipment on the vehicle's skid; on mobile they stack into
the column in DOM order.

---

## 5. Full motion system

### 5.1 The dive record — the one source of every figure

Declared once, here, and referenced by every element, worked example and
the §10 figure audit. A build that needs a number takes it from this
table or derives it by a formula printed on the page.

| Fact | Value |
|---|---|
| Vehicle / operator / ship | ROV *Meridian* / Meridian Subsea / RV *Northlight* |
| Dive | № 214 — launched 14 March, 03:40 UTC |
| Field / seabed depth | The Acheron Vent Field / **2,512 m** |
| Dive time budget | 55 min descent + 400 min bottom + 45 min ascent = **500 min (8 h 20)** |
| Ambient bottom temperature | 2 °C |
| Pressure law | P(d) = 1 + d ÷ 10 bar → at 2,512 m, **252.2 bar** (printed on the page) |
| Dissolved O₂ | Ambient 3.4 mg/L; vent-adjacent low 1.1 mg/L |
| Stations (6) | 1 Smoker Garden · 2 Crab Fields · 3 Plume Traverse · 4 Mussel Beds · 5 Old Chimney · 6 Shimmer Flats |
| Station depths | 2,512 · 2,495 · 2,470 · 2,489 · 2,501 · 2,480 m (terrain varies; the profile in §6.7 draws exactly these) |
| Thermal peaks (zone centres) | Smoker Garden **352 °C** · Crab Fields 18 °C · Plume Traverse 120 °C · Mussel Beds 9 °C · Old Chimney 2 °C (dead) · Shimmer Flats 24 °C |
| Thermal law | Within a zone, T(p) = 2 + (peak − 2) × sin²(π × p), p = progress through the zone (printed beside the panel) |
| Samples (6 jars) | №1 Chimney fragment, Smoker Garden, 2,512 m, 4.2 kg · №2 Crab carapace (moult), Crab Fields, 2,495 m, 0.3 kg · №3 Plume particulate filter, Plume Traverse, 2,470 m, 0.8 kg · №4 Mussel shell pair, Mussel Beds, 2,489 m, 1.6 kg · №5 Basalt glass, Old Chimney, 2,501 m, 2.9 kg · №6 Tube-worm tubes (empty), Shimmer Flats, 2,480 m, 0.5 kg |
| Sample totals | **6 jars · 10.3 kg · deepest 2,512 m** (4.2+0.3+0.8+1.6+2.9+0.5 = 10.3 — reconciles in §6.4, §6.14, §6.18, §8) |
| Sampling ethic (printed) | "We take moult, shell and stone. Nothing living comes up." |
| Next dive | № 215 — 8 berths, **5 taken** (printed in §6.16 and §8.3; a request confirms as Berth 6 of 8) |

### 5.2 The shared loop and the named easings

All scroll-scrubbed values — depth, temperature, cone pressure response,
bathymetry draw, profile dot — are driven by **one** `requestAnimationFrame`
loop. Raw scroll position is never applied directly: a smoothed progress
value chases the true value at **lerp 0.085**, which is the dive's ballast
— scrolling in this theme *sinks*, with weight, and a fast flick of the
wheel takes a visible moment to arrive. The loop sleeps when the tab is
hidden or when nothing is within 0.1% of target.

| Easing | Curve | Used by |
|---|---|---|
| `ballast` | cubic-bezier(0.22, 0.9, 0.28, 1) | Scroll smoothing feel, cone widening, section entries — everything that descends. |
| `sonar` | cubic-bezier(0.16, 1, 0.3, 1) | Reveals and pings: panel wake, bathymetry dot settle, nav state. Fast out, long listen. |
| `drift` | cubic-bezier(0.37, 0, 0.63, 1) | Ambient loops: snow sway, shimmer phase, lantern-like cone breathing (±1.5% diameter, 9s). |
| `settle` | cubic-bezier(0.34, 1.4, 0.44, 1) | The one licensed overshoot: a jar dropping into the basket (§6.4, §6.5). Matter landing in a rack. |
| `checklist` | steps, hand-timed | Instrument panels waking in order (§6.8) — flicker is scheduled, not eased. |

### 5.3 Every motion term, in this theme's language

- **Scroll-triggered reveals** — stations surface into the cone: content
  is fully printed at all times; entering the beam raises local
  illumination from the 55% floor to 100% over 600ms `ballast`. A reveal
  here is a *lighting* event, never an existence event.
- **Scroll-driven / scrub animation** — depth, temperature, pressure and
  O₂ readouts; the bathymetry profile's draw and dot; the temperature
  spike (§6.3). All read from the smoothed progress value, all reversible
  — scroll up and the vehicle rises, readings fall, exactly by the same
  functions.
- **Parallax** — marine snow at three rates (§6.2); camera frames drift
  6px against scroll inside their brackets; the cone itself does not
  parallax — it is bolted to the vehicle, which is bolted to the visitor.
- **Pinned sections** — one only: the Plume Traverse pins its camera frame
  for a 160vh range while the temperature completes its spike (§6.3,
  §6.9). Pinning is rationed because a pinned page is a vehicle holding
  station, and holding station costs power the narrative should feel.
- **Smooth scrolling** — the lerp loop (§5.2) plus `ballast` anchor
  travel (900ms) for in-page navigation.
- **Progress indicator** — two, both diegetic: the depth gauge (metres,
  now) and the basket (jars, kept). No progress bar exists in this theme;
  §11 refuses it with its replacement.
- **Staggered + masked reveals** — instrument panels wake in checklist
  order with 90ms staggers (§6.8); station headlines are uncovered by the
  cone's edge, not by masks — the mask *is* the water.
- **Kinetic typography** — refused as motion; practised as behaviour: the
  depth numeral counts, the temperature spikes, values flicker and settle.
  Digits change; letterforms never move (law 5, §3).
- **Marquee** — refused. Nothing at 2,512 m scrolls sideways to get
  attention. The dive log is a list, read downward like the water column.
- **Counters** — depth (scrubbed, exact), temperature (scrubbed, exact),
  jar count and manifest totals (counted from the DOM, §6.14). No counter
  in this theme ever animates *from zero for show* — the depth gauge
  starts at the surface (0 m) because the dive starts there, which is a
  fact, not an effect.
- **SVG line-draw** — the bathymetry profile (§6.7), drawn by the same
  smoothed progress that moves its dot.
- **Image scale-in-frame** — camera frames hold their photographs at
  scale 1.06 → 1.0 across their traverse of the cone (§6.9); the frame,
  not the photograph, is what the visitor is meant to notice.
- **Hover / micro-interactions** — hover leans light: the cone brightens
  +6% locally toward a hovered specimen card (§6.5 arms the sample);
  buttons pressurise (fill rises 180ms `sonar`); the one magnetic
  behaviour in the theme is the basket's open slot, which brightens as a
  flying jar approaches (§6.5).
- **Custom cursor** — refused, explicitly and permanently. The system
  cursor is the surface world's tool; the theme does not dress it up.
- **Skeleton loading** — unlit frames: panel-shaped blocks in `--panel`
  with mono labels printed ("PANEL WARMING") and a hard 1500ms ceiling
  (§6.17).
- **Page transitions** — the surface transition (§6.10): dim to black,
  one beat, descend into the next page's cone.
- **Reduced motion** — the dive fully lit (§6.1 fallback state), snow
  printed as a static starfield-density texture at 8% alpha, shimmer off,
  all readings printed at their station values. A complete page, not a
  lesser one.

---

## 6. Signature elements

Eighteen elements: the ten originals (§6.1–§6.10), deepened, plus eight
page-family elements (§6.11–§6.18) the original entry implied but did not
specify. Every element carries the full v1 field set and every v2 layer.

### 6.1 The ROV light cone

- **What / why:** A radial light pool fixed to the viewport for the entire
  dive — the vehicle's headlamps, and the reason anything is visible. It
  belongs to this theme absolutely: remove it and the site is a black page
  with opinions. The cone teaches the visitor the theme's law in the first
  second — you are somewhere light has to be carried.
- **Structure:** A `position: fixed; inset: 0` overlay div above the
  ground and below the content's interactive layer, painted with two
  stacked radial gradients (core `--cone-warm` at 14% alpha → transparent
  at 62% radius; a wider, cooler falloff `--glass` to 88%). Content sits
  *above* the gradient in z-order but is dimmed by a second, inverted
  vignette layer above it (multiply blend) so text genuinely passes
  through light and shade. `pointer-events: none` throughout. Cone centre
  is viewport centre, offset +4vh downward (lamps aim slightly down, at
  the seabed ahead).
- **Motion spec:** On load the cone widens from 40vmin to 92vmin diameter
  over 1500ms `ballast`. At rest it breathes ±1.5% diameter on a 9s
  `drift` cycle (generator load, not decoration). Scroll velocity adds a
  pressure response: fast descent narrows the cone by up to 4% (water
  resistance), recovering over 800ms. Illumination floor: content outside
  the cone renders at 55% brightness minimum — dimmed, never hidden.
- **Choreography timeline (ms):** t=0 page paints fully lit (fallback
  state). t=120 JS arms the cone at 40vmin over the lit page. t=120–1620
  cone widens to 92vmin `ballast` while the vignette deepens to full —
  the visitor watches the lamps warm up, not a fade from black. t=900 the
  hero panel begins its wake (§6.8). t=1620 cone at full; breathing loop
  starts. Any scroll before t=1620 completes the widening instantly to
  the visitor's position state — the dive never waits for its own intro.
- **State matrix:** *Rest:* cone at 92vmin, breathing. *Hover (any
  interactive element):* cone unchanged; the element's own local brighten
  (§6.5) handles focus. *Focus:* identical — light follows scroll, not
  pointers. *Active:* n/a. *Scrolled-past:* cone is viewport-fixed; there
  is no past. *Disabled (JS off / reduced motion / watchdog):* lights-on
  state — cone layers removed, ground `--panel`, all content at 100%.
  *Touch:* identical to desktop; no hover dependency anywhere.
- **Content-merge:** The cone is not over the content, it is the content's
  lighting rig: station text is set to live in the core (§4), instrument
  values brighten as their panel crosses centre, and the hero headline
  "surfaces inside it" because the headline's position is the first thing
  the widening cone reaches. Remove the copy and the cone lights an empty
  seabed — which is why the copy's placement is specified in §4, not left
  to taste.
- **Breakpoints:** ≥1200px: 92vmin cone, centre +4vh. 768–1199px: 108vmin
  (a smaller screen needs a relatively wider lamp), centre +2vh.
  <768px: 130vmin, breathing disabled (battery), pressure response
  disabled, illumination floor raised to 65% — small screens get more
  light, not less, because their content fills more of the beam.
- **Edge cases & failure modes:** Very tall viewports: cone diameter is
  vmin-based so it never outgrows the short axis. Ultrawide: falloff
  layer caps at 1600px radius, corners stay `--vent-black`. If the
  browser lacks `mix-blend-mode`, the vignette layer is dropped and the
  gradient alone carries the effect (checked once at arm time). If the
  tab was backgrounded during load, the widening is skipped to final
  state on first visibility.
- **Failure fallback & watchdog:** The DOM ships lit. JS arms darkness
  only after first paint, and a 2000ms watchdog checks the cone reached
  its target diameter; if the rAF loop has stalled (hidden tab, throttled
  timers), the watchdog removes both cone layers and leaves the page in
  the lights-on state. A missed trigger can therefore only ever produce
  *more* light.
- **Reduced motion:** No cone. Lights-on state from the start: ground
  `--panel`, snow off, all readings printed. The §10 gate tests this as a
  first-class design, not an error path.
- **Accessibility:** The cone layers are `aria-hidden`, presentational,
  and never the sole carrier of information — dimming is brightness only,
  text contrast at the 55% floor still measures ≥4.5:1 for body text
  because `--shell` on `--vent-black` starts at 15.34:1. Focus outlines
  (2px `--sulphur`, 2px offset) render above the vignette layer. The
  lights-on state is also exposed as a visible "Lights on" toggle in the
  masthead (§6.11) for visitors who find the dark tiring.
- **Tokens:** `--vent-black`, `--cone-warm`, `--glass`, `--panel`,
  `--ease-ballast`, `--ease-drift`, `--loop-lerp` (0.085), `--cone-size`
  (92vmin), `--cone-floor` (0.55).
- **Performance & mobile:** Two gradient layers, compositor-only
  (transform/opacity on the breathing via scale of a pre-rendered layer);
  ≤0.3ms/frame. Mobile variant: single gradient layer, no breathing, no
  pressure response — the cone still widens on load, because that widening
  *is* the theme's first sentence.

### 6.2 Marine snow particulate

- **What / why:** ~60 motes of marine snow — the endless fall of organic
  debris that is the deep ocean's only weather — drifting down through
  the beam at three parallax rates. It belongs because it is the water
  made visible: without it the cone lights a void; with it, the visitor
  can *see* the 2,512 metres between themselves and the surface.
- **Structure:** One `<canvas>` fixed behind the content, sized to the
  viewport, `aria-hidden`. Particles are 1–2.5px soft dots in `--snow`,
  each assigned to one of three depth planes (rate 0.3 / 0.6 / 1.0) with
  its own size and alpha (0.18 / 0.32 / 0.5). No DOM nodes per particle;
  no images.
- **Motion spec:** Base fall speed 6–14 px/s by plane. A slow lateral
  sway (sin, period 7–13s per particle, `drift`) of ±6px. Scroll
  turbulence: the shared loop's scroll velocity adds drift — up to
  ±14px/s vertical and ±5px/s lateral, decaying over 1200ms after scroll
  stops, so a hard scroll visibly stirs the water and then the water
  settles. Particles recycle at the viewport edges with new random
  x-positions (seeded per session, never per frame).
- **Choreography timeline (ms):** t=0 (JS armed): canvas fades in over
  800ms *after* the cone begins widening — snow is only visible once
  there is light to catch it. Continuous thereafter. On station entry,
  no change (snow does not perform for sections). On the surface
  transition (§6.10), snow density thins to zero over the 400ms dim —
  you leave the water before you leave the page.
- **State matrix:** *Rest:* full drift. *Hover / focus / active:* no
  change — snow ignores the visitor; it is weather, not interface.
  *Scrolled-past:* n/a (fixed layer). *Disabled:* canvas hidden; reduced
  motion prints a static 8%-alpha speckle texture on the ground instead.
  *Touch:* identical; turbulence reads touch scroll velocity the same way.
- **Content-merge:** Snow density is zoned by the layout: the generator
  thins particles by 40% over body-text blocks (checked against section
  bounding boxes each second) so the water never snows *on* the reading.
  Inside the cone's core the motes brighten (they are lit); outside it
  they fall to 30% alpha — the same particle, lit or unlit by the same
  lamp as everything else.
- **Breakpoints:** ≥1200px: 60 particles, 3 planes. 768–1199px: 44
  particles, 3 planes. <768px: 28 particles, 2 planes (0.4 / 1.0),
  sway halved. Canvas resolution capped at devicePixelRatio 1.5.
- **Edge cases & failure modes:** No canvas support → the static texture
  fallback (same as reduced motion). Low-power device (hardware
  concurrency ≤2 or `save-data`): particle count halves and turbulence
  is disabled. Long pages: canvas is viewport-sized, cost is constant.
  Resize: canvas re-seeds on a 300ms debounce, particles keep their
  plane assignments.
- **Failure fallback & watchdog:** Snow is pure enhancement — its total
  failure is an empty canvas and a still-complete page. A frame-time
  watchdog monitors the shared loop: if average frame cost exceeds
  2.5ms over 120 rolling frames, snow is the first thing cut (§14 cut
  order) and the canvas hides itself.
- **Reduced motion:** Canvas off. The printed speckle texture (CSS
  gradient noise, 8% alpha) stands in so the ground does not go flat —
  the water is still *there*, it is simply not falling.
- **Accessibility:** `aria-hidden="true"`, no information content,
  excluded from contrast calculations. It never overlays focus outlines
  (z-order below content). The static fallback respects
  `prefers-reduced-motion` identically.
- **Tokens:** `--snow`, `--vent-black`, `--ease-drift`, `--snow-count`
  (60), `--snow-turbulence` (14px/s max).
- **Performance & mobile:** ≤0.5ms/frame at 60 particles; one canvas, no
  per-particle DOM. Mobile variant: 28 particles, 2 planes, no sway —
  specified above; if the frame watchdog trips, mobile drops to the
  static texture first.

### 6.3 Temperature spikes at plume zones

- **What / why:** Near a vent, water that was 2°C is suddenly 352°C, and
  the vehicle's thermometer is the first thing to know. As the visitor
  scrolls into a plume zone, the station panel's temperature readout
  climbs — scrubbed, by the printed thermal law — while an SVG turbulence
  filter warps the edges of the camera frames inside the zone. The
  instrument reacts to the place the text describes; data and narrative
  arrive together or not at all.
- **Structure:** The temperature value lives in the station's instrument
  panel (§6.8) as a mono readout; the spike is a pure function of the
  shared loop's smoothed progress through the zone's declared scroll
  range, evaluated per frame: T(p) = 2 + (peak − 2) × sin²(πp), peak from
  the dive record (§5.1). The shimmer is an SVG `<filter>` with
  `<feTurbulence>` + `<feDisplacementMap>`, applied to a wrapper on
  in-zone camera frames (§6.9), its displacement scale driven by the same
  p (0 → 6px at zone centre → 0).
- **Motion spec:** Fully scrubbed — no autonomous animation. Scrolling
  down into the Smoker Garden zone raises TEMP from 2°C through the
  printed law to 352°C at zone centre and back down as the zone exits;
  scrolling up reverses it exactly. The readout updates at most every
  frame, displays one decimal below 20°C and whole degrees above (real
  instruments shed precision as they approach their limit — and the panel
  says so). Shimmer displacement follows p with the loop's lerp, so the
  warp lags the scroll by the ballast feel, never snaps.
- **Choreography timeline (ms):** Zone entry (p=0): TEMP begins rising
  from ambient; shimmer scale 0. p=0.25: TEMP ≈ 2 + 0.146 × (peak − 2)
  (Smoker Garden ≈ 53°C); first visible frame-edge warp. p=0.5 (zone
  centre): TEMP = peak (352°C); the panel's TEMP label gains its one
  licensed sulphur treatment; shimmer at full 6px. p=0.75: symmetric
  fall. p=1: TEMP back to the next zone's ambient behaviour; shimmer 0.
  All values are functions of scroll position — the timeline is the
  scroll itself.
- **State matrix:** *Rest (outside zones):* TEMP reads the local ambient
  (2°C open water, or the low diffuse value printed for the station).
  *Hover / focus:* no effect — you cannot hover water hotter. *Active:*
  n/a. *Scrolled-past:* value settles to the zone's exit ambient and
  holds; scrolling back re-enters the function. *Disabled:* each panel
  prints its station's peak and ambient as static text ("AMBIENT 2°C ·
  PEAK 352°C AT ORIFICE"). *Touch:* identical; scrub follows touch
  scroll through the same loop.
- **Content-merge:** The spike is not a widget beside the article — the
  article's station *is* the zone. The Smoker Garden's text describes
  352°C fluid while the panel above it reads 352°C and the photographs
  beside it warp. The thermal law is printed in the panel's footer in
  mono, so a sceptical visitor can check the curve against the scroll —
  the theme would rather be audited than admired.
- **Breakpoints:** ≥1200px: full behaviour, shimmer on all in-zone
  frames. 768–1199px: shimmer displacement capped at 4px. <768px:
  shimmer applies to the single pinned frame only (§6.9), temperature
  scrub unchanged (it is data, and data is never cut).
- **Edge cases & failure modes:** SVG filters unsupported → shimmer is
  skipped; the temperature readout (the information) is unaffected. Very
  fast scrolling through a zone: the lerp means the spike may peak late
  and lower — physically true to a real thermometer's lag, and the panel
  never displays a value the function didn't produce. Zone ranges are
  measured from live DOM positions on resize, never hard-coded pixels.
  Content longer than expected stretches the zone; the law is in p
  (proportion), so the curve survives.
- **Failure fallback & watchdog:** If the shared loop stalls, a 1200ms
  watchdog freezes readouts at their last true values and adds the
  panel's printed static line (ambient · peak) beneath — the visitor
  still learns the temperature story, told plainly. No state exists in
  which the panel shows a blank or a zero.
- **Reduced motion:** No scrub, no shimmer. Panels print ambient and peak
  statically (above), and zone photographs sit still in their frames.
  The information content is identical; only the *experience of
  approaching* is removed.
- **Accessibility:** The temperature readout is `aria-live="off"` during
  scroll (a live region would shout hundreds of values); instead each
  panel carries a visually-hidden static summary ("Smoker Garden:
  ambient 2 degrees, vent fluid peaks at 352 degrees") that assistive
  tech reads once, in order. The sulphur treatment at peak is never the
  only signal — the numeral itself is the signal. Shimmer never applies
  to text, only to photographic frames.
- **Tokens:** `--sulphur`, `--plume-text`, `--sonar`, `--loop-lerp`,
  `--thermal-peak` (per zone, from §5.1), `--shimmer-max` (6px).
- **Performance & mobile:** The temperature evaluation is one sin² per
  frame — negligible. The turbulence filter is the expensive part:
  applied to at most two frame wrappers at once, static regions cached
  by the browser, and it is cut second in the §14 order. Mobile variant:
  one frame, 4px cap, filter region clipped to the frame's edge band
  (the warp lives at edges; the centre is never displaced).

### 6.4 The sample basket

- **What / why:** A fixed corner grid of six jar slots — the ROV's sample
  basket, riding on the vehicle for the whole dive. Completing each
  station drops a labelled jar into its slot. It belongs because it makes
  progress *holdable*: not a bar that fills, but specimens you surface
  with. It is also the theme's anti-slop signature (the original entry's
  own detail): the final section is "Surface with Samples," and the
  basket the visitor has watched fill for six stations is shown full,
  enlarged, as the dive's result.
- **Structure:** A `position: fixed` aside, bottom-right, containing a
  3 × 2 CSS grid of jar slots (glass jar silhouettes in `--glass` over
  `--panel`, hairline `--sonar-deep` rules). Each slot carries its jar's
  label in mono (specimen short name + depth) once filled; empty slots
  show their station number and the word `EMPTY`. The depth gauge
  (§4) docks to the basket's top edge. The whole basket is a `<aside
  aria-label="Sample basket">` with a list of jars — it is content, not
  chrome.
- **Motion spec:** A jar arrives either from its section's completion
  (the slot fills in place: jar fades/rises 8px and settles, 450ms
  `settle`, with a 60ms glass glint) or by click-to-sample flight (§6.5).
  Section completion is measured by the shared loop: a station counts
  complete when its specimen card has passed the viewport's 55% reading
  line. Jars never leave. The basket's count line ("3 / 6 JARS · 6.6 KG")
  updates from the DOM's filled slots, weights summed from the dive
  record values printed on each jar.
- **Choreography timeline (ms):** Station complete (t=0): the slot's
  target jar brightens at its card (§6.5 rest state) — t=0–450 the
  in-place jar settles into the slot with `settle`; t=300 the count line
  ticks to the new totals; t=450 a single sonar ping ring (6.12's
  language) fades from the slot, 600ms, the basket's only flourish.
  Final section entry: the basket's fixed instance fades to 40% over
  300ms as its enlarged twin in the final section takes over — the same
  basket, surfaced, never two baskets at once at full strength.
- **State matrix:** *Rest (dive in progress):* slots filled per stations
  completed. *Hover (a filled jar):* jar label expands to full specimen
  name + station + depth + weight (a tooltip card in `--panel`, shell
  text). *Focus:* same expansion, keyboard reachable — the basket list
  is in tab order once, as a group. *Active:* clicking a filled jar
  scrolls (`ballast`, 900ms) to its station — the basket is also the
  dive's index. *Scrolled-past:* jars persist; state survives scroll
  direction changes absolutely. *Disabled:* the basket renders as a
  static manifest summary in the final section only (§6.14), and the
  fixed aside is not shown — no JS, no pretend collecting. *Touch:*
  tap = focus behaviour (label expands); tap again = travel to station.
- **Content-merge:** The basket is the dive's table of contents, its
  progress record and its cargo in one object. Its jars are the same
  jars listed in the manifest (§6.14) and weighed in the footer totals
  (§6.18) — one record, three printings. A station the visitor skipped
  shows an empty slot all the way to the surface, which is the theme's
  quiet honesty: the final section shows what *you* collected, and the
  manifest shows what the *dive* collected, and §8.1 keeps the two
  distinct on purpose.
- **Breakpoints:** ≥1200px: full 3 × 2 basket, 132px wide, labels
  visible. 768–1199px: basket collapses to a 6-segment jar strip (slots
  as 18px cells, count line only) docked bottom-right; tap expands to
  the full grid as an overlay panel. <768px: a single docked chip —
  "BASKET 3/6" in mono with the depth gauge — tap opens the full basket
  as a bottom sheet; the fixed grid never covers text on small screens.
- **Edge cases & failure modes:** Short viewports (<560px tall): the
  basket auto-collapses to the strip at any width. If a station section
  is removed by the CMS, its slot renders `STATION NOT FLOWN` and the
  totals recompute from the DOM — the basket counts what exists, never
  what the design expected. Session persistence: basket state is
  per-page only; a reload restarts the dive at the surface, which is
  correct behaviour for a dive.
- **Failure fallback & watchdog:** The fixed basket is JS-armed over a
  hidden-until-armed attribute; if the shared loop or the arm script
  fails, the aside never appears and the final section's static manifest
  (§6.14) carries the full record. A 2500ms watchdog after load verifies
  at least the basket shell is present if armed; failure removes it
  cleanly rather than leaving a dead box in the corner.
- **Reduced motion:** Jars appear in slots without flight or settle
  (instant, with the count line updating). The final-section handover
  is a cut, not a fade. Everything else — labels, travel, totals — is
  identical.
- **Accessibility:** The basket is a labelled landmark with a real list;
  each jar addition is announced once via a polite live region ("Jar 3
  collected: plume particulate filter, 2,470 metres. Basket: 3 of 6.").
  Jar targets are ≥44px. The count line is text, never colour-only.
  Keyboard: the basket group is one tab stop; arrow keys move between
  jars; Enter travels to the station.
- **Tokens:** `--panel`, `--glass`, `--plume-grey`, `--sonar-deep`,
  `--sonar`, `--shell`, `--sulphur-deep` (jar seals), `--ease-settle`,
  `--basket-slots` (6).
- **Performance & mobile:** One fixed aside, transform/opacity only;
  negligible frame cost. Mobile variant: the chip + bottom-sheet form
  above — the full grid is never fixed-position on <768px, by rule.

### 6.5 Click-to-sample

- **What / why:** Each station's specimen card carries one sulphur
  action: **Take sample**. Clicking it flies the specimen's jar in an
  arc into the basket, ahead of the scroll schedule — the visitor does
  the manipulator arm's job. It belongs because collecting is the dive's
  work, and a survey site where the visitor only *reads* about sampling
  has missed its own subject. It is also the theme's single conversion
  gesture, rehearsed six times before the berth form (§6.16) asks for
  anything real.
- **Structure:** The specimen card (DOM: figure + name + depth + the
  sampling note) holds a jar ghost — a clone of the basket's jar node —
  created on click, `position: fixed`, animated along a quadratic arc
  from the card to the target slot via WAAPI (`element.animate`) with
  offsets computed from live `getBoundingClientRect()`s. The card itself
  stays put; only the jar travels. Protected specimens (the living crab
  colony's residents, §12) render the action disabled with the printed
  reason — the moult is taken, the animal is not (§5.1 ethic).
- **Motion spec:** Flight 600ms `settle` along the arc (apex +12% of
  distance above the straight line), jar scaling 1 → 0.42 to match slot
  size, rotating ≤4° — a jar in a manipulator's grip, not a cartoon.
  Landing triggers §6.4's settle and count update. If the station was
  already collected by scroll, the button reads `IN BASKET` and the
  flight does not repeat. The basket slot brightens (+10% `--glass`
  alpha) as the jar passes the viewport's midpoint — the theme's one
  magnetic-adjacent behaviour, and it is the *slot* that responds, not
  the pointer.
- **Choreography timeline (ms):** t=0 click; button label switches to
  `SAMPLING…` and disables. t=0–80 jar ghost materialises at the card
  (fade + rise 4px). t=80–680 arc flight. t=560 slot brightens. t=680
  landing: ghost removed, real jar settles in slot (§6.4 timeline takes
  over), live-region announcement fires. t=680–900 button label resolves
  to `IN BASKET ✓` (the check is a drawn pencil-equivalent stroke in
  sonar, 200ms — the theme's one drawn mark of completion).
- **State matrix:** *Rest:* `TAKE SAMPLE` in sulphur, enabled, if the
  specimen is takeable and not yet collected. *Hover:* cone brightens
  +6% locally over the card; button fill rises. *Focus:* 2px sulphur
  outline; same local brighten (keyboard visitors get the light too).
  *Active:* the flight sequence above; button inert until landing.
  *Scrolled-past:* if the station completed by scroll first, the button
  is already `IN BASKET`. *Disabled:* two kinds — already-collected
  (`IN BASKET`, still focusable, explains itself) and protected
  (`LOOK ONLY — LIVING`, not focusable as a button; the reason is
  printed as text beside it). *Touch:* tap = click; the arc is identical;
  no hover brighten precedes it.
- **Content-merge:** The button is on the specimen card, the jar carries
  the specimen's real label, and the flight path crosses the page the
  visitor is reading — the collection visibly *comes from* the station's
  content and lands in the record they've been watching. It is the
  opposite of a floating action button: it exists six times, each time
  about one named thing.
- **Breakpoints:** ≥1200px: full arc flight. 768–1199px: arc flattened
  (apex +6%), duration 520ms. <768px: no flight — the basket chip (§6.4)
  pulses once and the jar is simply there when the sheet opens; small
  screens get the fact without the journey, because the journey would
  cross the entire reading column.
- **Edge cases & failure modes:** Basket collapsed to chip/strip: the
  flight targets the chip's position and the jar count increments
  there. Rapid double-click: the button disables at t=0; a second jar
  can never exist. Clicking during the surface transition: the action
  queues until the new page arms, or is dropped with the button state
  intact — never a jar lost between pages. If WAAPI is unavailable, the
  jar fades at the card and settles in the slot (two-step fallback,
  300ms).
- **Failure fallback & watchdog:** A 1200ms watchdog on the flight: if
  the animation hasn't completed (tab throttled, WAAPI error), the ghost
  is removed and the slot fills directly — the sample is never lost to
  its own animation. If JS is off, the button is a plain anchor to the
  manifest section, labelled `SEE IN MANIFEST` — the record is reachable
  without the performance.
- **Reduced motion:** No flight. Click → jar appears in the slot, count
  updates, announcement fires. The button states and the protected-
  specimen ruling are unchanged.
- **Accessibility:** Real `<button>` elements with descriptive labels
  ("Take sample: chimney fragment, Smoker Garden, 2,512 metres").
  Flight is decorative — the state change is announced by the basket's
  live region (§6.4), not by the animation. Focus returns to the button
  after landing. Touch target ≥44 × 44px. The `LOOK ONLY` ruling is
  text, never a greyed button alone.
- **Tokens:** `--sulphur`, `--vent-black` (button label), `--glass`,
  `--sonar`, `--ease-settle`, `--ease-sonar`, `--flight-time` (600ms).
- **Performance & mobile:** One cloned node + WAAPI per flight; no
  layout thrash (rects read once at t=0). Mobile variant: the chip-pulse
  form above; zero animation cost.

### 6.6 Manipulator arm crossing

- **What / why:** Once, shortly after load, a jointed manipulator-arm
  silhouette crosses the cone's lower edge, slowly, and leaves. It never
  repeats. It belongs because it is the theme's whole argument in four
  seconds: this view is being *piloted* — something with a grip is down
  here with you, and it is restrained enough to only show itself once.
  Repetition would make it a screensaver; once makes it a sighting.
- **Structure:** An inline SVG (three-segment arm: shoulder, elbow,
  wrist + two-prong gripper, drawn in `--vent-black` at 82% alpha with a
  1px `--plume-grey` rim light on the upper edges), `position: fixed`,
  entering from the bottom-left edge of the cone, `aria-hidden`,
  `pointer-events: none`. Path and joint angles are keyframed in CSS;
  the gripper opens 6° at the crossing's midpoint — it is travelling,
  not grabbing.
- **Motion spec:** Total crossing 4000ms `drift`-based easing (slow in,
  slower out). The arm traverses the cone's lower third on a shallow
  arc, dipping 12px at midpoint as if clearing the seabed. Trigger:
  time — it fires once at t≈2600ms after load (after the cone has
  widened and the hero panel has woken), and a session flag
  (`sessionStorage`) prevents any repeat within the visit, across pages.
- **Choreography timeline (ms):** t=2600 arm's shoulder enters frame
  left-bottom, 12% visible. t=2600–3400 first segment crosses the cone
  edge into light — the rim light catches. t=3400–4600 full crossing of
  the lower third; gripper opens at t≈4000. t=4600–6600 exit right,
  decelerating. t=6600 arm gone; the flag is written. Total on-screen
  ≈4s of the 6.6s window including partial entry/exit.
- **State matrix:** *Rest:* absent — its rest state is not existing.
  *Hover / focus / active:* no interaction, ever. *Scrolled-past:* if
  the visitor has already scrolled beyond the hero when t=2600 arrives,
  the crossing is **cancelled**, not relocated — the moment was the
  hero's, and a missed moment stays missed (the flag still writes, so it
  doesn't ambush them later). *Disabled:* reduced motion, JS off, or
  `save-data` → never rendered. *Touch:* identical rule.
- **Content-merge:** The arm crosses *the cone's* lower edge — the
  vehicle's own workspace, in front of the hero's seabed content, at the
  depth where a real arm would be working relative to the camera. It
  never crosses text (its band is the hero's lower visual field, over
  the seabed photograph), and it carries nothing: it is not delivering a
  message, selling a sample, or pointing at a button. Its uselessness is
  its truthfulness.
- **Breakpoints:** ≥1200px: full crossing as specced. 768–1199px:
  crossing shortened to the cone's lower-left quadrant (path scaled
  0.7). <768px: **cut entirely** — on a small screen the arm would cross
  the reading column, and the theme does not interrupt reading for
  atmosphere.
- **Edge cases & failure modes:** If the hero is not in the viewport at
  trigger time (deep link to #station-4), cancelled per the state
  matrix. If the tab is hidden at t=2600, the crossing waits for
  visibility and then checks the scroll rule again. If SVG is somehow
  unavailable, nothing renders and nothing is missed — the element is
  pure presence.
- **Failure fallback & watchdog:** No fallback content exists because no
  content depends on it. A watchdog is unnecessary; the failure mode is
  absence, which is also its rest state. This asymmetry is deliberate
  and is the model for all ambient elements in the theme: anything the
  visitor *needs* gets a watchdog; anything merely *witnessed* gets a
  shrug.
- **Reduced motion:** Never rendered. The hero's printed caption gains
  nothing and loses nothing — the arm is not referenced by any text, so
  its absence leaves no dangling reference.
- **Accessibility:** `aria-hidden="true"`, unfocusable, no text, no
  meaning. It moves slowly (≤0.15 viewport-widths/sec) and crosses no
  text, staying well inside photosensitivity comfort; it is also cut
  entirely under reduced motion.
- **Tokens:** `--vent-black`, `--plume-grey`, `--ease-drift`,
  `--arm-once` (session flag key).
- **Performance & mobile:** One SVG, CSS keyframes on transform only,
  runs once for 4s. Mobile variant: cut (above). Frame cost after its
  single pass: zero, forever.

### 6.7 Bathymetry margin line

- **What / why:** An SVG dive profile — descent, the six-station bottom
  traverse at its true depths, ascent — drawn down the page's left margin,
  scrubbed to scroll, with a dot marking current depth on the profile.
  It belongs because it is the dive plan and the reader's position on it,
  in one line: the margin stops being decoration and becomes the chart
  the whole expedition is following.
- **Structure:** An SVG in the 72px left rail (§4), viewBox stretched to
  the page's full height. The path is generated from the dive record's
  station depths (§5.1): surface (0 m) → descent slope → station plateaus
  at 2,512 / 2,495 / 2,470 / 2,489 / 2,501 / 2,480 m in page order →
  ascent. Drawn with `stroke-dasharray` driven by the shared loop; the
  position dot is a 7px `--sonar` circle with a mono depth label. Station
  ticks cross the line at each plateau, labelled with the station number
  in mono.
- **Motion spec:** Draw progress = smoothed page progress, mapped so the
  line completes exactly at the final section's start (the surface is
  the profile's end, drawn as the visitor arrives). The dot rides the
  drawn portion's head; its depth label reads the same depth function as
  the gauge (§6.4 dock) — two instruments, one value, always agreeing.
  On station entry the dot pulses once (scale 1 → 1.5 → 1, 500ms
  `sonar`) as it passes the station's tick.
- **Choreography timeline (ms):** Continuous with scroll. At load the
  line is drawn to the hero's depth (~120 m of the descent — the dive
  has begun, the profile admits it). Each station: dot crosses tick →
  pulse (500ms) → panel wake begins (§6.8) 150ms later — the chart
  arrives a breath before the instruments, as it should. Final section:
  the ascent segment draws over the last 120vh of scroll, dot rising to
  0 m exactly as "Surface with Samples" reaches the reading line.
- **State matrix:** *Rest:* drawn to current depth. *Hover (a station
  tick):* tick label expands to station name + depth; the line segment
  for that station brightens to full `--sonar`. *Focus:* ticks are
  links — the profile is a navigation (§6.11 shares its targets);
  keyboard focus shows the same expansion plus outline. *Active:* click
  travels (`ballast` 900ms) to the station. *Scrolled-past:* the drawn
  line stays drawn — the profile is a record of where you've been, and
  scrolling up does *not* un-draw it; the dot alone moves back. (This
  ratchet is deliberate and is tested in §10: history doesn't erase.)
  *Disabled:* the full profile prints statically with all stations
  labelled — in reduced motion it is simply a chart in the margin.
  *Touch:* tap a tick = travel; no hover expansion.
- **Content-merge:** The profile's plateaus are at the stations' real
  depths and in the page's real order, so the margin chart is a true map
  of the document — a visitor who reads only the rail has still read the
  dive's shape. Its ascent segment is the only part of the page that
  goes *up*, and it is timed to the one section where the narrative
  surfaces.
- **Breakpoints:** ≥1200px: full rail form. 768–1199px: rail narrows to
  44px; station labels become numbers only; hover expansion retained.
  <768px: the rail leaves the margin and becomes a horizontal depth
  strip under the masthead — profile rotated to a left-to-right
  sparkline with the depth readout at its head; ticks remain tappable
  links in a horizontally scrollable row.
- **Edge cases & failure modes:** Page height changes (late images,
  CMS content): the path regenerates on a debounced resize/observer;
  station proportions are computed from live section offsets, so the
  map stays true. If a station is missing, its plateau is skipped and
  the profile draws through — the chart reflects the dive that exists.
  Extremely long pages: SVG scales; stroke stays 1.5px via
  `vector-effect: non-scaling-stroke`.
- **Failure fallback & watchdog:** The full path is printed in the DOM
  as a complete `d` attribute; JS only *reveals* it progressively via
  dash offset. If the loop fails, a 1500ms watchdog sets the offset to
  fully drawn — the chart appears whole rather than half-surveyed.
- **Reduced motion:** Fully drawn, static, all stations labelled; the
  dot is replaced by a printed "YOU ARE AT" marker only in the
  lights-on state — under reduced motion with the cone active, the
  depth gauge (§6.4) carries position and the rail is a reference chart.
- **Accessibility:** The rail is a `<nav>` with a list of station links
  (the SVG is `aria-hidden`; the list is the accessible truth). Depth
  position is available as text in the gauge. Ticks/links ≥44px target
  height in the rail (the rail is 72px wide; hit areas extend into the
  margin). Focus order follows the dive order.
- **Tokens:** `--sonar`, `--sonar-deep`, `--plume-text`, `--shell`,
  `--ease-sonar`, `--ease-ballast`, `--rail-width` (72px).
- **Performance & mobile:** One path redraw per frame at most (dash
  offset is a compositor-cheap attribute); negligible. Mobile variant:
  the horizontal strip above — same data, one sparkline, no per-frame
  work beyond the readout text.

### 6.8 Instrument panels coming online

- **What / why:** Every station is headed by a mono instrument panel —
  DEPTH / TEMP / PRESS / O₂ DISS — that wakes in checklist order as the
  station enters the cone: values flicker, settle, then hold. It belongs
  because a survey section should *report* before it describes; the
  panel is how the visitor knows the vehicle has arrived somewhere real,
  with conditions, before a single sentence of prose asks for their
  trust.
- **Structure:** A `<section>`-heading `<div role="group" aria-label=
  "Station instruments">` per station: a panel bar in `--panel` with a
  `--plume-grey` hairline, four readout cells in a fixed mono grid
  (label 11ch stop, value, unit), and a footer line carrying the
  station's printed laws (thermal law at vent stations, pressure law on
  the hero panel). Values are real DOM text updated by the shared loop —
  DEPTH and TEMP scrub with position (§6.3); PRESS derives from DEPTH by
  the printed formula; O₂ DISS steps between its two declared values by
  zone.
- **Motion spec:** Wake sequence on station entry (panel's top crosses
  the 70% viewport line): cells light in checklist order — DEPTH, TEMP,
  PRESS, O₂ — 90ms apart; each value flickers through 3–5 seeded
  near-values over 240ms (`checklist` timing, steps not easing) then
  locks. After lock, DEPTH/TEMP/PRESS scrub live with scroll. Only one
  panel is *live* (scrubbing) at a time — the one whose station occupies
  the cone; panels above hold their exit values, panels below sleep at
  their printed static line until woken.
- **Choreography timeline (ms):** t=0 panel crosses trigger. t=0–90
  DEPTH flickers → locks to true depth at panel position. t=90–180 TEMP
  wakes (begins at ambient, spike function takes over if in a zone).
  t=180–270 PRESS computes in (the flicker is the formula's digits
  resolving: 25 → 252 → 252.2). t=270–360 O₂ settles. t=360 panel fully
  live; station headline's illumination begins (§5.3). Wake happens
  once per station per page-load; scrolling back up never re-wakes —
  systems stay online once started.
- **State matrix:** *Rest (unwoken):* panel shows its printed static
  line (station depth · ambient · peak) in `--plume-text` — informative
  before it is alive. *Rest (woken, station in cone):* live scrubbing.
  *Rest (woken, station passed):* values hold at exit readings, panel
  dims to 80% (it is history now). *Hover:* the hovered cell's label
  expands its gloss ("O₂ DISS — DISSOLVED OXYGEN, MG/L") in place.
  *Focus:* cells are not focusable; the panel's group label is read as
  the section's introduction. *Active:* n/a. *Disabled:* static line
  only, at full contrast — the printed dive. *Touch:* identical; glosses
  expand on tap of the label.
- **Content-merge:** The panel is the station's first content, not a
  widget above it: its DEPTH is the depth the following text claims to
  be written at; its TEMP is the temperature the photographs are
  shimmering in; its footer prints the laws the values obey. A station
  whose panel disagrees with its prose fails §10 — the merge is enforced
  by audit, not by hope.
- **Breakpoints:** ≥1200px: four cells in a row, full glosses.
  768–1199px: four cells in a row, values 1.125rem, glosses shortened
  ("O₂ DISSOLVED"). <768px: 2 × 2 grid; the footer law line wraps to two
  lines; wake stagger tightens to 60ms (smaller ceremony, same order).
- **Edge cases & failure modes:** Rapid scrolling past several stations:
  wakes queue and complete in dive order, capped — if three panels are
  pending, the two older ones snap to live without flicker (the vehicle
  doesn't perform checklists for an audience that has left). Values
  never display outside their function's range; a NaN from any sensor
  function renders as the printed static line, never as "NaN" — §10
  greps for it. O₂ near vents steps down over the zone (3.4 → 1.1 mg/L)
  by the same sin² law as temperature, inverted.
- **Failure fallback & watchdog:** Each panel carries its static line in
  the DOM beneath the live cells. A 3000ms watchdog per panel: if the
  wake hasn't completed (loop stalled, IO never fired), the panel snaps
  to its static line at full contrast and is marked printed. The dive
  reads perfectly with every panel in fallback — that is the test §10
  runs with JS disabled entirely.
- **Reduced motion:** No wake, no flicker. Panels show the static line
  plus the station's key live-equivalent values printed as a fixed row
  (depth · ambient · peak · pressure at depth). Nothing scrubs.
- **Accessibility:** The live values are `aria-live="off"` (see §6.3 —
  scrubbing values must not be announced continuously). Each panel has a
  visually-hidden summary sentence with the station's conditions in
  prose. Visible text contrast: values in `--sonar` on `--panel` 6.28:1,
  labels `--plume-text` on `--panel` ≈7.8:1. The flicker phase never
  drops a value's contrast — flicker changes digits, not opacity.
- **Tokens:** `--panel`, `--plume-grey`, `--plume-text`, `--sonar`,
  `--sulphur` (TEMP at peak only), `--shell`, `--ease-sonar`,
  `--wake-stagger` (90ms).
- **Performance & mobile:** Text updates only, throttled to when the
  displayed value actually changes (depth changes per metre, not per
  pixel). One live panel at a time caps the cost at four text writes per
  frame worst case. Mobile variant: same, with the 2 × 2 grid; no cost
  difference that matters.

### 6.9 Heat-shimmer camera frames

- **What / why:** Photographs sit in ROV camera frames — corner brackets,
  a mono caption with timestamp and depth — and inside plume zones their
  edges warp with animated turbulence, stilling outside them. It belongs
  because the camera should suffer the environment it films: a vent
  photograph that looks like a studio shot is a lie, and the frame —
  brackets, caption, warp — is how the page keeps its images honest.
- **Structure:** A `<figure>` with a bracket overlay (four corner
  strokes, SVG or border segments in `--plume-grey`), the `<img>` inside
  an SVG-filter wrapper (§6.3's turbulence), and a `<figcaption>` in
  mono: `CAM 2 · 14 MAR 05:12 UTC · 2,508 M · SMOKER GARDEN, NORTH
  CHIMNEY`. The caption's depth is the *camera's* depth at that station
  (printed, static — captions are records, and records don't scrub).
  Images scale 1.06 → 1.0 across their cone traverse (§5.3).
- **Motion spec:** Shimmer displacement 0 → 6px scrubbed by zone
  progress p (§6.3), applied to the wrapper's edge band only (filter
  region inset so the centre of the photograph is never displaced — you
  can always see what the photograph is *of*). Outside zones: scale 0,
  photograph still. The scale-in-frame runs on the shared loop's
  smoothed progress as the frame crosses the cone.
- **Choreography timeline (ms):** Frame enters cone: brackets brighten
  `--plume-grey` → `--plume-text` over 400ms. Frame crosses into a plume
  zone (p rising): warp fades in with p, no separate timeline — the
  scroll is the timeline (§6.3). Zone centre: full 6px edge warp; the
  caption's TEMP-adjacent note (`WATER AT FRAME EDGE ≈ 340°C`) becomes
  legible as the cone passes it — it was always printed. Frame exits
  zone: warp returns to 0 by the same function.
- **State matrix:** *Rest (outside zone):* still photograph, brackets
  dim. *Rest (in zone):* edge warp at current p. *Hover:* warp pauses
  its *phase* (the turbulence pattern holds still while displacement
  stays) and the photograph scales +1% — inspection steadies the camera.
  *Focus:* same steadying; the caption is the focus's text alternative
  companion. *Active:* click opens the frame's full-resolution view in
  the lights-on state (§6.1 fallback design) — examining a photograph
  happens with the lights up, as it would on the ship. *Scrolled-past:*
  warp settles to the exit value (0 unless the frame remains in-zone).
  *Disabled:* no filter, no scale; brackets and caption print statically.
  *Touch:* no hover steadying; tap = the full-view behaviour.
- **Content-merge:** The frames are the dive's evidence, captioned like
  evidence, warped by the same law that drives the thermometer. A
  photograph's caption depth, its station's panel depth and its jar's
  label depth are three printings of the record — §10 samples them for
  agreement. The images are never decorative stock: each is *of* its
  station, named in its caption, and the warp is the environment signing
  the photograph.
- **Breakpoints:** ≥1200px: frames hang at the body column's right edge,
  46% column width. 768–1199px: full column width, in flow. <768px:
  full width; shimmer only on the single pinned Plume Traverse frame
  (§6.3); other frames print still — mobile keeps the story, drops the
  shimmer count.
- **Edge cases & failure modes:** Missing/failed image: the frame
  renders with its caption and a `--panel` plate reading `FRAME NOT
  RECOVERED — CAM 2` — a lost camera frame is a known event on a dive,
  and the page treats it as record, not error. Slow image load: the
  frame and caption are laid out first (aspect-ratio reserved), the
  photograph fades in inside its brackets — never a reflow (§3, law 5).
  Filters unsupported: §6.3's ruling applies — warp skipped, story
  intact.
- **Failure fallback & watchdog:** The filter is applied by JS adding a
  class; if the filter reference breaks (SVG not parsed), the class is
  inert and the photograph shows plain — failure looks like a calm day,
  not a broken page. No watchdog needed beyond §6.3's; the element's
  information (photograph + caption) is never behind the effect.
- **Reduced motion:** No warp, no scale. Photographs print still in
  their frames with full captions. In-zone status is carried by the
  caption's printed temperature note alone.
- **Accessibility:** Every photograph has real alt text describing the
  vent subject (the caption is *additional* record data, not a
  substitute). The bracket overlay is `aria-hidden`. Contrast: caption
  `--plume-text` on `--vent-black` 8.66:1. The full-view state is a
  dialog with proper focus trap and Esc, in lights-on design.
- **Tokens:** `--plume-grey`, `--plume-text`, `--panel`, `--shell`,
  `--shimmer-max` (6px), `--ease-ballast`.
- **Performance & mobile:** The turbulence filter is the theme's most
  expensive effect — capped at two live wrappers (§6.3), filter region
  clipped to edges. Mobile variant: one wrapper, 4px cap, or none
  (above). Images: responsive `srcset`, lazy below the hero, ≤520KB
  total for the home page (§14).

### 6.10 Surface transition

- **What / why:** Page transitions briefly surface through black: the
  current page's cone dims to nothing, one beat of true dark, then the
  next page descends — its cone widening over its own hero. It belongs
  because moving between dives should feel like the vehicle moving:
  black water between worlds, never a white flash or a slide. It is the
  theme's only full-screen effect, and it earns that by being the
  literal journey between pages.
- **Structure:** A fixed black overlay (`--vent-black`, opacity 0) plus
  the cone layers (§6.11's ownership: the cone belongs to the page
  shell, not the route). On navigation click (same-origin links only),
  JS intercepts, dims cone + content to black over 400ms, swaps the
  route (or performs the native navigation with a stored "descending"
  flag for MPA builds), then runs §6.1's widening on arrival. Snow
  thins to zero during the dim (§6.2).
- **Motion spec:** Out: 400ms `ballast` — cone diameter shrinks 92 →
  30vmin while the vignette closes to full black (the lamps don't switch
  off; the vehicle turns away). Beat: 120ms of held black. In: the new
  page's §6.1 load sequence (cone widens 40 → 92vmin, 1500ms; a
  returning visitor's subsequent transitions shorten the widen to 900ms
  — the vehicle is warmed up). Total perceived transition ≈1.4–2s,
  skippable by any scroll or keypress, which snaps to the arrived state.
- **Choreography timeline (ms):** t=0 click. t=0–400 dim/shrink.
  t=400–520 held black (route swap happens here, invisibly).
  t=520 new page painted (it painted lit, per §6.1's rule). t=640 cone
  arms at 40vmin. t=640–1540 (returning) or t=640–2140 (first) widening.
  Panel wake follows §6.8. Any input after t=520 fast-forwards the
  widening to complete.
- **State matrix:** *Rest:* overlay at opacity 0, inert. *Hover /
  focus:* no pre-transition teasing — a link hover never starts the
  water moving. *Active:* the sequence above. *Scrolled-past:* n/a.
  *Disabled:* JS off or reduced motion → ordinary navigation, no
  overlay, no flag; the link simply goes where links go. *Touch:*
  identical; tap targets unchanged.
- **Content-merge:** The transition is not a loading screen with
  branding — it is water. It carries no logo, no message, no progress
  bar; its content is the *absence* between two lit places, which is
  exactly what the vehicle experiences between stations on different
  dives. The basket (§6.4) and its state cross the transition untouched:
  what you collected stays collected within the session's dive pages.
- **Breakpoints:** ≥1200px and 768–1199px: full sequence. <768px: dim
  shortens to 280ms, beat to 80ms, widening to 700ms — small screens
  and their networks get a brisker vehicle.
- **Edge cases & failure modes:** Slow route (>1200ms to first paint):
  the held black extends, but at 1200ms the overlay fades back up to
  reveal the *old* page with a mono line in the panel register:
  `SURFACE DELAYED — HOLDING POSITION` and navigation falls back to
  native. The visitor is never trapped in black water by a slow server.
  External links, downloads, and modified clicks (ctrl/cmd) bypass the
  transition entirely. Back/forward: the transition does not run —
  history navigation is instant, with the cone arriving already wide.
- **Failure fallback & watchdog:** A 2500ms hard watchdog on the whole
  sequence: any state older than 2500ms forces the overlay to opacity 0
  and removes the descending flag. The catastrophic failure of this
  element would be a black page; the watchdog exists so that failure is
  impossible by construction.
- **Reduced motion:** No transition. Links navigate natively; pages
  arrive lit (§6.1 fallback). Nothing about the information architecture
  changes.
- **Accessibility:** The overlay is `aria-hidden`; during the ≤2s
  sequence, focus moves to the new page's H1 on arrival (standard route
  behaviour), never into the overlay. The `SURFACE DELAYED` line is a
  polite live announcement if it ever appears. No content is ever
  *only* reachable through a transitioned link.
- **Tokens:** `--vent-black`, `--cone-warm`, `--ease-ballast`,
  `--transition-dim` (400ms), `--transition-beat` (120ms).
- **Performance & mobile:** One overlay div + the existing cone layers;
  no assets. Mobile variant: the shortened timings above; the sequence
  is disabled entirely on `save-data`.

### 6.11 Sonar masthead & station navigation

- **What / why:** The site's header is the vehicle's control frame: the
  operator wordmark set like a hull plate, the dive number ticking
  beside it, station navigation rendered as a sonar sweep list — each
  station a contact that brightens as the visitor's depth approaches
  it. It belongs because navigation on a survey is not a menu; it is
  the list of places the vehicle can go, in the order the ocean puts
  them.
- **Structure:** A fixed top bar (height 64px) in `--vent-black` at 88%
  alpha with a `--plume-grey` keel line. Left: wordmark (Archivo 600,
  "MERIDIAN SUBSEA") + mono dive tag (`DIVE 214 · ACHERON FIELD`).
  Centre/right: station nav — six mono links with station number, name
  (Archivo on ≥1200px, number-only below), and a sonar ping indicator
  (a 6px ring that expands from the active station's dot). Right: the
  "Lights on" toggle (§6.1) and the berth link (§6.16) in sulphur text.
  The bathymetry rail (§6.7) is this nav's in-page twin; both share
  targets and active state.
- **Motion spec:** On station change (from the shared loop's station
  detection), the new active link's ping ring expands 6 → 18px and
  fades over 900ms `sonar`, once; the previous station's dot dims to
  `--sonar-deep`. The bar itself never moves, resizes or hides on
  scroll — a control frame you can't find is a safety issue, and the
  theme treats it as one. Wordmark and dive tag are static.
- **Choreography timeline (ms):** Page load: bar paints with the lit
  page; when JS arms, the current station (from scroll position) pings
  once at t=1800 (after cone widening). Station change: t=0 dot swap;
  t=0–900 ping ring; t=150 the rail's tick (§6.7) pulses in answer —
  the two navs acknowledge each other, briefly, like crew.
- **State matrix:** *Rest:* current station's dot full `--sonar`,
  others `--sonar-deep`. *Hover (a station link):* name brightens to
  `--shell`; a depth readout for that station appears in mono beneath
  the bar's keel line (e.g. `STN 3 · 2,470 M`). *Focus:* same readout +
  2px sulphur outline. *Active (the station you're in):* dot full,
  name in `--shell`, `aria-current="true"`. *Scrolled-past:* stations
  above the current one show a small sonar check-stroke (visited —
  the log remembers). *Disabled:* bar renders fully, links are anchors,
  active state is set server-side by page. *Touch:* tap = navigate
  (`ballast` anchor travel or page link); the depth readout appears on
  the station page's panel instead.
- **Content-merge:** The nav's stations are the page's stations, in dive
  order, at their true depths — the header is a compressed copy of the
  bathymetry profile, and the two can be checked against each other.
  The dive tag is not decoration: it is the same Dive № 214 that the
  manifest (§6.14) and footer (§6.18) print.
- **Breakpoints:** ≥1200px: full names + dive tag + toggle + berth link.
  768–1199px: station numbers + names abbreviated to two words; dive
  tag hides its field name. <768px: the station nav leaves the bar and
  becomes the horizontal depth strip (§6.7's mobile form) pinned under
  it; the bar keeps wordmark, lights toggle, and berth link only.
- **Edge cases & failure modes:** More stations than fit (a 9-station
  dive): the nav scrolls horizontally within the bar, active station
  scrolled into view — the bar never wraps to two lines. Long station
  names truncate with ellipsis at 22ch, full name in the depth readout.
  If JS never arms, the bar is a complete static header (its default
  state) — nothing about it is JS-dependent except the ping.
- **Failure fallback & watchdog:** None required beyond default-state
  design: the bar ships complete and static; JS only adds the ping and
  the live active-state tracking. If station detection fails, the
  server-rendered active state (by page/section) stands.
- **Reduced motion:** No ping ring. Active station changes are instant
  state swaps. The bar is otherwise identical.
- **Accessibility:** A real `<header>` + `<nav aria-label="Survey
  stations">`; `aria-current` on the active station; the ping is
  `aria-hidden`. Lights toggle is a real `<button aria-pressed>`.
  Contrast: station names `--plume-text` on black 8.66:1 at rest,
  `--shell` 15.34:1 active/hover. All targets ≥44px tall.
- **Tokens:** `--vent-black`, `--plume-grey`, `--sonar`, `--sonar-deep`,
  `--shell`, `--plume-text`, `--sulphur`, `--ease-sonar`,
  `--masthead-h` (64px).
- **Performance & mobile:** Static bar, one small ring animation on
  station change only. Mobile variant: the two-tier form above; the
  ping is cut on <768px (the strip's readout carries position instead).

### 6.12 Specimen catalogue cards

- **What / why:** The listing element: a grid of specimen cards — one
  per sample in the catalogue (this dive's six, and on the samples index
  page, previous dives' jars) — each card a small evidence plate:
  photograph or jar rendering, specimen name, station, depth, weight,
  and its takeable status. It belongs because a survey's output is a
  catalogue, and the catalogue is where the dive becomes citable.
- **Structure:** Cards in a responsive grid (`--panel` stock, hairline
  `--plume-grey`). Anatomy, top to bottom: camera-frame image area
  (§6.9's brackets, still form), specimen name (Archivo 500 1.125rem),
  mono data row (`STN 1 · 2,512 M · 4.2 KG`), the sampling note (one
  line, Log register), and the card's action — on this dive's stations,
  the Take sample button (§6.5); on index pages, `VIEW RECORD`, a link
  to the specimen's detail. The whole card is not a link; actions are
  explicit (a card that is secretly one big link is a trap, not a
  card).
- **Motion spec:** Cards surface with the cone like everything else
  (illumination, §5.3). On grid entry, cards settle in a 60ms stagger
  (translateY 6px → 0, `sonar`) — a tray being set down, once. Hover
  lifts the card's local cone brighten (+6%, §6.5's language) and the
  jar seal (`--sulphur-deep` disc) rotates 8° — wax catching light.
  No idle animation exists on cards; a catalogue at rest is still.
- **Choreography timeline (ms):** Grid crosses the reading line: t=0
  first card settles; t=60/120/180… subsequent cards in DOM order
  (which is dive order — the stagger reads as the traverse). Settle
  completes by t≈600 for a full row. On filter change (§7 listing
  behaviour): outgoing cards dim to the floor over 200ms, incoming
  settle without stagger — filtering is work, not ceremony.
- **State matrix:** *Rest:* printed, lit by cone position. *Hover:*
  brighten + seal rotation (above). *Focus:* the card's action takes
  focus with the sulphur outline; the card brightens identically to
  hover. *Active:* the action's own states (§6.5). *Scrolled-past:*
  cards hold; a collected specimen's card gains its `IN BASKET` tag
  permanently. *Disabled:* the grid is a static catalogue — fully
  readable, actions become manifest anchors (§6.5's fallback).
  *Touch:* no hover effects; the brighten happens on the action's tap
  press state only.
- **Content-merge:** Each card *is* its specimen's record in miniature —
  the same name, station, depth and weight as the jar label (§6.4), the
  manifest row (§6.14) and the detail page. The catalogue is not a
  marketing grid for the samples; it is the samples, indexed. §10's
  figure audit samples cards against the dive record directly.
- **Breakpoints:** ≥1200px: 3 columns in the body measure, cards ~340px.
  768–1199px: 2 columns. <768px: 1 column; the data row wraps to two
  lines rather than shrinking below 0.75rem; image area aspect holds
  4:3.
- **Edge cases & failure modes:** A specimen with no photograph: the
  card shows its jar rendering (SVG jar + label) instead — the
  catalogue never shows a broken-image icon. Very long specimen names
  wrap to two lines; the grid row stretches, cards in the row equalise
  height (grid, not masonry — a catalogue is shelved, not scattered).
  Empty catalogue (a dive with no samples yet): the §12 empty state,
  printed as a log line, not an illustration.
- **Failure fallback & watchdog:** Cards ship fully rendered; the settle
  is JS-added. If images fail, §6.9's `FRAME NOT RECOVERED` plate
  applies inside the card's frame. No watchdog — nothing here can
  strand content.
- **Reduced motion:** No settle, no stagger, no seal rotation. Cards
  print in place. Hover brighten becomes an instant state (it is a
  lighting change, not a motion).
- **Accessibility:** Cards are `<article>`s with headed names; the data
  row is text, not an image of text. Action labels are specimen-specific
  (§6.5). Grid navigation is natural tab order (dive order). Contrast:
  name `--shell` on `--panel` 14.44:1; data row `--plume-text` ≈7.8:1.
- **Tokens:** `--panel`, `--plume-grey`, `--plume-text`, `--shell`,
  `--sulphur-deep`, `--sonar`, `--ease-sonar`.
- **Performance & mobile:** Grid of static cards; images lazy-loaded
  with reserved aspect (CLS 0). Mobile variant: single column, seal
  rotation cut, settle cut — the catalogue is data first at every size.

### 6.13 Dive-log entries

- **What / why:** The expedition's written log — timestamped entries in
  the Log register ("05:12 — First smoker in the lights. Column thirty
  metres, fluid shimmering at the orifice.") — presented as a vertical
  list that reads downward like the water column. It belongs because
  every real survey produces a log before it produces a paper, and the
  log is where the dive's voice lives: terse, past tense, unimpressed
  by wonders it has work to do during.
- **Structure:** An ordered list; each entry is a mono timestamp chip
  (`05:12 UTC`) + Archivo entry text (1–3 lines) + an optional linked
  reference (station, jar, or camera frame — the log cites the record).
  Entries group under dive-day headings on archive pages. On the home
  page, a short log (6–8 entries) runs between the last station and the
  final section — the traverse's own account of itself.
- **Motion spec:** Entries do not animate in — a log is written, not
  performed. The one behaviour: as the visitor scrolls the log, the
  timestamp chip of the entry at the reading line brightens from
  `--plume-text` to `--sonar` (the entry currently being *read aboard*),
  a 300ms crossfade driven by the shared loop. That is all. The
  restraint is the spec: if the log danced, nobody would believe it.
- **Choreography timeline (ms):** Continuous: reading-line entry's chip
  transitions over 300ms as lines change. On page load, the chip of the
  first entry starts lit. Nothing else moves, ever, in this element.
- **State matrix:** *Rest:* entries printed; current-reading chip lit.
  *Hover (a reference link):* standard link treatment; the referenced
  station's tick in the rail (§6.7) brightens in answer — the log and
  the chart acknowledge each other. *Focus:* same rail answer + outline.
  *Active:* reference links travel (`ballast`) to their target.
  *Scrolled-past:* chips dim back as entries pass. *Disabled:* a plain
  list; identical text. *Touch:* references tap normally; no rail
  answer (the rail is a strip on mobile, §6.7).
- **Content-merge:** Log entries cite jars, frames and stations by their
  record names, and the citations resolve to the actual elements — the
  entry "Jar 3 away — plume filter, sealed 06:03" links to the manifest
  row for Jar №3. The log is the narrative index of the same record
  everything else prints; an entry that mentions a number must match
  the record (§10 samples the timestamps against the dive timeline:
  launch 03:40 + descent 55 = bottom 04:35; entries run 04:35–11:15;
  ascent complete 12:00 — printed in §6.18).
- **Breakpoints:** ≥1200px: timestamp chip in a fixed 12ch left column,
  text in the measure. 768–1199px: chip column 10ch. <768px: chip moves
  above the entry text (stacked); the list's left rule (a `--sonar-deep`
  hairline, the water column) persists at 12px inset.
- **Edge cases & failure modes:** Very long archives paginate by dive
  (§11 pagination in log dress: `EARLIER DIVES` / `LATER DIVES` — never
  numbered page pills; dives are the unit). An entry with no references
  is normal and common. Entries longer than 3 lines are an editorial
  defect, not a layout problem — §12 caps them.
- **Failure fallback & watchdog:** None needed: the element is text in a
  list; its fallback is itself. The chip-brightening is JS garnish on a
  complete element.
- **Reduced motion:** The chip crossfade becomes instant. Nothing else
  changes — this element is the theme's proof that reduced motion, done
  honestly, often changes almost nothing.
- **Accessibility:** A semantic `<ol>` (the order is chronological and
  meaningful); timestamps are `<time datetime>` with UTC offsets. The
  brightened chip is never the only indicator of position — it indicates
  nothing the visitor needs. Link text is descriptive ("Jar 3 in the
  manifest"), never "click here".
- **Tokens:** `--plume-text`, `--sonar`, `--sonar-deep`, `--shell`,
  `--ease-sonar`.
- **Performance & mobile:** Text only. The reading-line check runs
  inside the shared loop at negligible cost. Mobile variant: the
  stacked chip form above.

### 6.14 Sample manifest table

- **What / why:** The dive's official output: a data table of every
  sample — jar №, specimen, station, depth, weight, disposition — with
  totals computed from its own rows. It belongs because a survey is
  judged by its manifest, and the manifest is where this theme's
  figure discipline becomes visible as a designed object: the table
  that cannot disagree with itself.
- **Structure:** A semantic `<table>` on the final section (and the
  samples index page). Columns: JAR № (mono) · SPECIMEN (Archivo) ·
  STATION · DEPTH (mono, m) · MASS (mono, kg) · DISPOSITION (mono short:
  `LAB — NORTHLIGHT FREEZER 2` etc.). Footer row: totals — jar count,
  total mass, deepest sample — computed by JS from the rendered rows
  and *also* printed statically in the HTML (the static printing is the
  fallback and the audit target; JS recomputation must match it or the
  build fails §10). Zebra striping is refused; rows separate by
  hairlines (`--plume-grey` at 40%) — a manifest is ruled, not shaded.
- **Motion spec:** None on the table itself, with one exception: when
  the visitor collects a jar (§6.5) after having already seen the final
  section (scrolled back up and down), the corresponding manifest row
  pulses its № cell once (`--sonar` fade, 800ms) on next view — the
  record acknowledging its own update. Rows never animate on first
  view. A manifest that performs has misunderstood its job.
- **Choreography timeline (ms):** First view: nothing. Post-collection
  re-view: t=0 row enters cone; t=200 № cell brightens; t=200–1000
  fade to rest. Totals never animate — they are recomputed silently
  and printed; a counting total on a manifest would be a slot machine.
- **State matrix:** *Rest:* printed table, static totals correct.
  *Hover (a row):* row's hairlines brighten one step; the row's jar in
  the enlarged basket (§6.4's final-section twin) highlights in answer.
  *Focus:* rows are not focusable; specimen names may link to detail
  pages with standard link states. *Active:* n/a. *Scrolled-past:*
  holds. *Disabled:* identical table; static totals stand (they were
  always the truth; JS was only checking). *Touch:* no hover answer;
  tap on a specimen link behaves as a link.
- **Content-merge:** The manifest is the third printing of the dive
  record (§5.1) — basket (§6.4) first, cards (§6.12) second, manifest
  third, footer (§6.18) fourth — and its totals row is the exact
  sentence the final section's headline stands on: "6 jars · 10.3 kg ·
  deepest 2,512 m." If the CMS adds a seventh sample, the table, the
  totals, the basket's slot count (`--basket-slots` is a build-time
  value, §10 checks it) and the final headline all change together or
  the gate fails.
- **Breakpoints:** ≥1200px: full six columns. 768–1199px: DISPOSITION
  column hides (available on the specimen detail page); five columns.
  <768px: the table becomes a stacked record list — each row a block:
  specimen name, then mono data lines (STN / DEPTH / MASS) — *never* a
  horizontally scrolling table; a manifest you must pan is a manifest
  you can't audit.
- **Edge cases & failure modes:** Zero samples (a survey that came up
  empty): the table renders its header and one row spanning all
  columns: `NO SAMPLES — THE DIVE IS LOGGED, THE BASKET IS EMPTY.`
  (§12's empty voice) with totals 0 / 0.0 kg / —. Mass values always
  print one decimal (0.3, never .3). Depths always carry thousands
  separators as printed in the record (2,512).
- **Failure fallback & watchdog:** The static totals are the fallback;
  the JS recomputation is the watchdog — on DOMContentLoaded it sums
  the rows and, on any mismatch with the printed totals, replaces the
  printed totals with the computed ones and flags the discrepancy in
  the console and in a data attribute for the build pipeline. The
  visitor always sees a self-consistent table.
- **Reduced motion:** The №-cell pulse is cut. Everything else is
  identical, because everything else was already still.
- **Accessibility:** Real `<table>` with `<th scope="col">`, a
  `<caption>` ("Samples collected on Dive 214, ROV Meridian — 6 jars"),
  and totals in `<tfoot>`. Screen readers get the table as a table.
  Contrast: body `--shell` on `--vent-black` 15.34:1; mono data
  `--plume-text` 8.66:1; hairlines are decorative.
- **Tokens:** `--shell`, `--plume-text`, `--plume-grey`, `--sonar`,
  `--panel`, `--vent-black`.
- **Performance & mobile:** One table; the recomputation is O(rows) once.
  Mobile variant: the stacked record list above — a transformation of
  presentation, never of data.

### 6.15 Station briefs accordion

- **What / why:** Collapsible briefs for the six stations — objectives,
  planned bottom time, hazards, sampling protocol — the dive plan's
  detail, available without leaving the page. It belongs because a real
  survey publishes its plan, and because some visitors (collaborators,
  reviewers, the curious) want the procedure, not just the story. The
  accordion is the plan drawer in the vehicle's console: closed by
  default, opened deliberately.
- **Structure:** Six `<details>`-equivalent rows (built as button +
  region for animation control, with the semantics of disclosure).
  Each header: station number + name (Archivo), mono summary line
  (`OBJ: MAP CHIMNEY FIELD · BOTTOM 70 MIN · HAZARD: 352°C FLUID`).
  Each region: the brief in Log-register prose + a mono protocol list.
  Bottom times sum to the record's 400 minutes (70+80+45+75+60+70 =
  400 — printed in the last brief's footer and audited in §10).
- **Motion spec:** Open/close animates region height over 320ms
  `ballast`, with the header's chevron — a small sonar triangle —
  rotating 90° over the same duration. Only one brief open at a time
  *on the home page's plan section* (opening one closes the previous,
  320ms, sequenced close-then-open); on the dedicated plan page,
  multiple may open (a drawer policy difference, stated in §7).
  Height animation uses the grid-template-rows technique; content never
  fades — it is uncovered, like everything in this theme.
- **Choreography timeline (ms):** t=0 click. If another brief is open:
  t=0–320 it closes. t=320–640 the new brief opens. If none open:
  t=0–320 opens. The header's summary line stays visible throughout —
  the visitor never loses the station's vital facts to the animation.
- **State matrix:** *Rest (closed):* header + summary line. *Rest
  (open):* full brief. *Hover:* header brightens to `--shell`.
  *Focus:* sulphur outline on the header button; the region is reached
  by natural tab order after the header. *Active:* the sequence above.
  *Scrolled-past:* open state persists (scrolling away doesn't tidy the
  console). *Disabled:* without JS, all briefs render open — a plan you
  can't open is worse than a long page. *Touch:* tap targets ≥48px
  header height; identical timing.
- **Content-merge:** The briefs are not FAQs wearing a costume — their
  content is the actual dive plan whose execution the rest of the page
  narrates, and their numbers (bottom times, hazard temperatures) are
  the record's numbers. The hazard line for the Smoker Garden says
  352°C because §6.3's thermometer will read 352°C; the accordion is
  where the theme's promises are made, in writing, before the dive
  keeps them.
- **Breakpoints:** ≥1200px: briefs in the body measure, protocol list
  in two mono columns. 768–1199px: single column protocol list.
  <768px: header wraps (name line, then summary line); open/close
  duration 260ms.
- **Edge cases & failure modes:** Deep-linking to a brief (`#brief-3`)
  opens it on load, instantly, no animation. If JS fails mid-animation,
  the region's height is set to auto by the watchdog pattern (a 700ms
  timer clears any inline height) — a brief can never be stuck
  half-open. Content much longer than expected: the region scrolls
  internally only beyond 70vh; briefs are capped editorially by §12.
- **Failure fallback & watchdog:** The no-JS state (all open) is the
  fallback, shipped as the default DOM and closed by JS on arm — the
  standard pattern, with the 700ms height watchdog above.
- **Reduced motion:** Open/close is instant (height swaps, no
  transition). The one-open policy still applies on the home page.
- **Accessibility:** Real disclosure semantics: `<button
  aria-expanded aria-controls>` + `role="region" aria-labelledby`.
  Header is a heading (`<h3>`) containing the button, so the plan is
  navigable by heading. Focus never moves on open/close. Contrast as
  per §6.12's card values.
- **Tokens:** `--panel`, `--plume-grey`, `--plume-text`, `--shell`,
  `--sonar`, `--sulphur` (hazard values only), `--ease-ballast`.
- **Performance & mobile:** Height animation on at most one region at a
  time; no layout cost when closed. Mobile variant: the wrapped header
  and 260ms timing above.

### 6.16 Berth-request form — "Request a berth on Dive 215"

- **What / why:** The theme's one conversion: a request to join the next
  dive as an observer/scientist berth aboard RV *Northlight*. It belongs
  because a survey programme's real output is the next survey — and
  because the form is where the theme proves its discipline under
  pressure: even asking for something is done by the record. The printed
  facts frame it: Dive № 215, 8 berths, **5 taken** — printed above the
  form, in the dive record (§5.1) and in §8.3. A successful request
  confirms as **Berth 6 of 8**, a number the visitor can derive before
  they ever submit.
- **Structure:** A form panel in `--panel` styled as the ship's berth
  manifest sheet: fields — full name (text), organisation (text), role
  (select: OBSERVER / SCIENTIST / MEDIA / CREW — WAITLIST), dive choice
  (radio: DIVE 215 · ACHERON / DIVE 216 · TBC), email, and one checkbox:
  the ballast check — "I understand a berth is a request, not a booking,
  and that the dive plan is set by the chief scientist." Submit:
  `FILE REQUEST` in sulphur. Confirmation replaces the form in place
  with a stamped manifest entry (§6.16 states).
- **Motion spec:** Field focus: the field's label brightens to `--shell`
  and a 2px `--sonar` keel line draws under the field over 240ms
  `sonar` — the form's only animation while filling. On submit: the
  panel dims to 70% for the request's duration with the mono line
  `TRANSMITTING TO NORTHLIGHT…` (a status, not a spinner — §11 refuses
  spinners). On success: the confirmation entry stamps in — scale 1.04
  → 1 + opacity, 300ms `settle`, with a sulphur-deep stamp border
  ("LOGGED · BERTH 6 OF 8 · DIVE 215"). No confetti has ever existed at
  2,512 m.
- **Choreography timeline (ms):** t=0 submit; button disables, label →
  `FILING…`. t=0–240 panel dims; status line prints. Response (target
  <900ms): t=R confirmation stamp sequence 300ms; the berth count above
  the form updates 5 → 6 taken (silently — it is a record correcting
  itself, and §6.14's totals discipline applies). t=R+300 focus moves
  to the confirmation heading. If response exceeds 2500ms, the status
  line extends: `…STILL TRANSMITTING — THE SHIP IS OVER THE SIDE, NOT
  OUT OF RANGE.` (the §12 error voice warming up, honestly).
- **State matrix:** *Rest:* printed form, berth count visible (5 OF 8
  TAKEN). *Hover:* submit button fill rises (180ms). *Focus:* per-field
  treatment above; visible at all times, never outline-none. *Active
  (submitting):* fields inert, status line live. *Error:* the failing
  field's keel line turns `--sulphur` (the theme has no red; sulphur is
  its caution colour) and an error line in the Log register prints
  beneath it (§12 examples) — errors never clear the visitor's other
  entries. *Success:* confirmation state, permanent for the session,
  with a `FILE ANOTHER REQUEST` ghost action (which re-opens the form
  with the count now at 6 taken — the next confirmation would be Berth
  7, and the form's arithmetic stays true). *Scrolled-past:* n/a (form
  state persists). *Disabled (no JS):* the form posts natively to its
  endpoint; the confirmation is a server-rendered page in the same
  manifest dress. *Touch:* identical; inputs ≥48px tall, 16px font
  (no iOS zoom).
- **Content-merge:** The form is a manifest sheet, its confirmation is a
  manifest entry, and its numbers come from the same record as the
  manifest table's (§6.14) — including the discipline that the count it
  shows (5 taken) and the number it issues (6) are derivable from each
  other. The ballast-check checkbox is the theme's ethic as a form
  field: what this dive is, stated before anyone signs.
- **Breakpoints:** ≥1200px: two-column sheet (name/organisation side by
  side; role/dive choice side by side). 768–1199px: single column,
  panel in the body measure. <768px: single column, full-bleed panel,
  submit button full width ≥52px tall.
- **Edge cases & failure modes:** Validation: email format and required
  fields only — the form asks for nothing it doesn't need (no phone, no
  address; a berth request is not an interrogation). Server failure:
  the panel restores, entries intact, error line in §12 voice:
  `THE REQUEST DID NOT REACH THE SHIP. YOUR ENTRIES ARE AS YOU LEFT
  THEM — FILE AGAIN.` Double-submit is blocked at t=0. If all 8 berths
  fill (count reaches 8 in the record), the form's state changes
  entirely: `DIVE 215 IS FULLY BERTHED` with the waitlist radio
  pre-selected — the form never sells what the record says is gone.
- **Failure fallback & watchdog:** Native form submission is the
  fallback (the form works with JS disabled, endpoint-rendered
  confirmation). A 4000ms watchdog on the JS submit path: if no
  response and no error, the form restores with the §12 failure line
  rather than transmitting forever.
- **Reduced motion:** No stamp animation (confirmation appears), no
  keel-line draw (instant state), dim becomes an instant opacity swap.
  The status and error text behaviour is unchanged.
- **Accessibility:** Real `<label>`s (visible, mono, above fields —
  never placeholder-as-label); errors linked via `aria-describedby`
  and announced via a polite live region; the confirmation heading
  receives focus on success (the one deliberate focus move in the
  theme, because the page's content genuinely changed). Contrast:
  labels `--plume-text` on `--panel` ≈7.8:1; input text `--shell`;
  sulphur error lines on `--panel` ≈7.4:1. Required fields are marked
  in text (`REQUIRED`), not by colour or asterisk alone.
- **Tokens:** `--panel`, `--plume-grey`, `--plume-text`, `--shell`,
  `--sonar`, `--sulphur`, `--sulphur-deep`, `--ease-sonar`,
  `--ease-settle`.
- **Performance & mobile:** The form ships no library; validation is
  ~2KB of the page's JS budget. Mobile variant: the full-bleed single
  column above; the stamp animation is the first thing cut under the
  §14 order (the confirmation text is the content).

### 6.17 Descent loader & unlit skeleton

- **What / why:** Between navigation and arrival, and wherever content
  loads late, the theme shows *unlit frames*: panel-shaped blocks in
  `--panel` with their instrument labels printed and the mono status
  `PANEL WARMING` — the vehicle descending toward content that isn't in
  the lights yet. It belongs because loading states in this theme must
  obey the same law as everything else: absence is described honestly,
  in the vehicle's own register, and never for long.
- **Structure:** Skeleton blocks mirror the real layout they precede
  (panel bars, card frames, manifest rows) at exact final dimensions —
  the skeleton is a reservation, not an approximation, so arrival never
  shifts layout (§3, law 5). Each block carries its real label text
  (e.g. `STN 3 — PLUME TRAVERSE`) in `--plume-text`; only the *values*
  are withheld. A thin `--sonar-deep` sweep line crosses each block
  once per 1400ms — a sonar ping looking for the content.
- **Motion spec:** The sweep is the only motion: a 1px gradient line
  travelling the block's width over 1400ms `drift`, fading at both
  ends. Hard ceiling: **1500ms**. At 1500ms, whatever content exists
  renders; the skeleton never outlives its welcome, and partial content
  (three of six cards) renders as three cards and three honest
  `FRAME NOT RECOVERED` plates (§6.9) rather than six skeletons.
- **Choreography timeline (ms):** t=0 skeleton paints (it is in the
  server HTML for route arrivals). t=0–1400 first sweep. Content ready
  before 1500: skeleton swaps to content with a 200ms illumination
  (the cone arriving, §5.3's language). t=1500: ceiling — remaining
  blocks convert to their failure plates or static lines. No second
  sweep ever starts after t=1500.
- **State matrix:** *Rest (loading):* sweeping blocks. *Rest (loaded):*
  gone, replaced. *Hover / focus:* skeletons are inert and unfocusable;
  focus skips them to the page's first real element. *Active:* n/a.
  *Scrolled-past:* n/a. *Disabled:* with JS off, server rendering means
  skeletons appear only if the server itself streams them — the
  no-JS document is the complete one (§6.1's rule) and contains no
  skeletons at all. *Touch:* identical.
- **Content-merge:** The skeleton is shaped like the content, labelled
  like the content, and capped like a dive procedure. It is the theme's
  refusal of the generic shimmer-bar: a visitor who sees `PANEL
  WARMING` for 900ms has learned where they are and what is coming —
  the loading state is already the log's voice at work.
- **Breakpoints:** All breakpoints: skeletons mirror the target layout
  at that breakpoint (the 2 × 2 panel grid on mobile, the stacked
  manifest on mobile). No variant behaviour beyond mirroring.
- **Edge cases & failure modes:** Content that never arrives (API
  down): at 1500ms the blocks become static plates reading `NOT
  RECOVERED ON THIS DIVE — THE LOG CONTINUES BELOW.` with a link to
  the section's static content where one exists. Slow images inside
  arrived content use §6.9's frame behaviour, not skeletons. Repeat
  visits (cached): skeletons may never appear; that is success, not
  inconsistency.
- **Failure fallback & watchdog:** The 1500ms ceiling *is* the
  watchdog, implemented as a timer independent of the content's own
  promises — a hung fetch cannot extend it. If the timer itself fails
  (JS dead), the server-rendered document contains no skeletons to be
  stuck in (above).
- **Reduced motion:** No sweep. Blocks sit printed and still with their
  labels; the 1500ms ceiling is unchanged.
- **Accessibility:** Skeleton regions carry `aria-busy="true"` on their
  container and are removed from the accessibility tree's content flow
  until real content lands (announced once, politely: "Station three
  loaded."). The printed labels are decorative duplicates of the coming
  headings — hidden from AT to avoid double announcement.
- **Tokens:** `--panel`, `--plume-text`, `--sonar-deep`, `--glass`,
  `--ease-drift`, `--skeleton-ceiling` (1500ms).
- **Performance & mobile:** Pure CSS blocks + one keyframe; zero assets.
  Mobile variant: identical, mirroring mobile layouts. This element is
  exempt from the §14 cut order — it is what the page looks like while
  the cuts are loading.

### 6.18 Ascent footer & the off-chart 404

- **What / why:** The footer is the ascent: the dive's totals printed a
  fourth and final time, the log's closing entries, and the colophon of
  the expedition — the place where the vehicle surfaces and the record
  is signed off. Below it, specified in the same element because it is
  the same gesture, the 404: a page off the dive plan entirely, treated
  as water the vehicle has no chart for. Both belong because endings in
  this theme are procedures, and a footer that is just links has
  surfaced without checking its basket.
- **Structure:** Footer (in-flow, full width, `--panel` ground — the
  surface is lit differently, §2's ruling in action): (1) the totals
  block — `DIVE 214 · 6 JARS · 10.3 KG · DEEPEST 2,512 M · BOTTOM 400
  MIN` in mono, DOM-computed like §6.14's; (2) closing log lines
  ("11:15 — Ascent begun. 12:00 — On deck. Samples to Freezer 2.");
  (3) columns: STATIONS (the six, linking), RECORD (Manifest, Dive log,
  Plan), OPERATOR (About the vehicle, Berths — §6.16, Contact);
  (4) the sign-off line: operator, ship, and the printed ethic (§5.1).
  The 404 page: cone at its narrowest (40vmin, unlit centre), a single
  panel reading `NO CHART FOR THIS WATER`, the requested path in mono,
  and three links — Surface (home), Manifest, Dive log — the places a
  lost vehicle can actually get to.
- **Motion spec:** Footer: the ascent segment of the bathymetry line
  (§6.7) completes as the footer enters; the totals block illuminates
  like a panel waking (§6.8's checklist, but at half ceremony: two
  beats, totals then log). Nothing else moves — the surface is calm.
  404: **choreography: none.** The cone stays narrow and still; a lost
  page does not perform. The only motion available is the visitor
  leaving, via a link, through §6.10.
- **Choreography timeline (ms):** Footer entry: t=0 totals block wakes
  (values print in checklist order, 90ms staggers, no flicker — the
  dive is over, the numbers are history and history doesn't flicker).
  t=360 log lines illuminate. t=720 footer fully lit; the depth gauge
  (§6.4) reads 0 M and the basket shows its final state — the only
  moment in the theme where every instrument reads *finished*.
- **State matrix:** *Rest:* printed totals and links. *Hover / focus:*
  standard link treatments; the totals block is text, not a link.
  *Active:* links navigate via §6.10. *Scrolled-past:* n/a (page end).
  *Disabled:* identical footer; totals are the static printing (the
  audit target). *Touch:* identical. *404 rest:* static, narrow cone
  or lights-on under reduced motion; links fully functional.
- **Content-merge:** The footer's totals are the manifest's totals are
  the basket's count are the record's numbers — the fourth printing
  closes the audit loop §10 walks. The closing log lines reconcile with
  §6.13's timeline (ascent 11:15–12:00, dive total 500 min from the
  03:40 launch: 03:40 + 8:20 = 12:00 ✓). The 404 merges by refusal: it
  admits, in the theme's own language, that this water was never
  surveyed — and offers the charted places instead of a search box
  dressed as a sonar.
- **Breakpoints:** ≥1200px: four footer zones in a row (totals, log,
  link columns, sign-off). 768–1199px: two rows. <768px: stacked;
  totals block first (it is the point), link columns as two mono
  lists; the 404's panel is full-width with its three links stacked
  ≥48px tall.
- **Edge cases & failure modes:** A dive with zero samples: totals read
  `0 JARS · 0.0 KG` and the log's closing line changes to the §12 empty
  form ("Basket empty. The dive is logged all the same."). Footer
  totals are computed from the same DOM source as §6.14 — if the
  manifest is absent from a page, the footer falls back to the printed
  dive record values for that page's dive. 404s for asset paths
  (missing images) never render this page — §6.9's plate handles those.
- **Failure fallback & watchdog:** The footer ships static and complete;
  its wake is garnish. The totals' watchdog is §6.14's recomputation,
  shared. The 404 requires no fallback — it is one.
- **Reduced motion:** Footer prints fully lit, no wake. 404 in
  lights-on state. Identical text throughout.
- **Accessibility:** Footer is a `<footer>` landmark with labelled nav
  groups; totals are a text block (also the page's summary for AT
  users who jump to the end). The 404 has a proper H1 (`No chart for
  this water`), the requested path in text, and links with descriptive
  names. Contrast: footer text `--shell` on `--panel` 14.44:1; mono
  `--plume-text` ≈7.8:1.
- **Tokens:** `--panel`, `--shell`, `--plume-text`, `--sonar`,
  `--sonar-deep`, `--plume-grey`, `--vent-black` (404 cone field),
  `--ease-sonar`.
- **Performance & mobile:** Static content; the wake reuses §6.8's code
  path. Mobile variant: the stacked form above. Nothing here is ever
  cut by §14 — a page may lose its shimmer, never its sign-off.

---

## 7. Page application map

**Home — the dive itself.** The full descent as specced: hero (§8.1),
six stations in dive order, the log (§6.13), the plan briefs (§6.15),
and "Surface with Samples" (manifest §6.14 + enlarged basket §6.4 +
footer §6.18). This is the only page that runs the complete choreography
(§13); every other page is a partial dive and says so.

**Stations index — the chart room.** A listing page: the six stations as
catalogue cards (§6.12's grid form, station variant: name, depth,
bottom time, hazard line) over a static bathymetry chart (§6.7's
reduced-motion form — on an index, the chart is a reference, not a
ride). No cone scrub; the page is lit at a steady survey light (cone
fixed wide, no breathing) because an index is a tool for choosing, and
choosing needs even light. Each card links to its station detail.

**Station detail — one station, full depth.** The cone, panel (§6.8),
frames (§6.9) and specimen card (§6.5) for a single station, plus its
brief (§6.15, open by default here — the drawer policy difference) and
its log entries filtered to that station. Depth scrub covers the
station's own range only: the panel's DEPTH walks the station's
±40 m working range as the visitor reads, so the vehicle is visibly
holding station, finessing its buoyancy, while they study one place.

**Samples index / specimen detail.** The catalogue (§6.12) across dives,
filterable by field, station type and disposition — filters are mono
checkbox rows styled as the manifest's own column heads, and filtering
is instant with §6.12's no-ceremony rule. Specimen detail: the jar at
large, its full record (every printing reconciled on one page), its
camera frames, its log citations (§6.13), and its chain of custody as a
mono timeline. This is the page researchers cite; it is deliberately
the plainest page in the theme.

**Expedition / about — the vehicle and the crew.** RV *Northlight* and
ROV *Meridian* as instrument-panelled profiles: specifications in mono
tables (the vehicle's depth rating — 6,000 m — printed beside the
field's 2,512 m so the margin is visible and checkable), crew as log-
register biographies with role labels in mono. The cone is present but
the page's subject is the surface world, so it runs in the lights-on
state with the cone as a framed viewport graphic — the one page where
the theme shows its vehicle from outside, honestly lit.

**Berth request — the conversion page.** §6.16's form with its record
framing, plus the dive-215 plan summary (stations, dates, the 5-of-8
count) drawn from the same record pattern as §5.1. Checkout and payment
are **routed out of the theme entirely**: a confirmed berth is settled
by the operator's ordinary booking system, linked plainly. The theme
never styles a payment form — money is surface business.

**Contact — surface radio.** A short form in the berth form's dress,
addressed to the ship: the conceit is a radio message (fields labelled
`FROM / SUBJECT / MESSAGE`), with the printed note that the ship
answers within two working days. No map. The ship is at sea; a map pin
would be a lie about where help is.

**404 — off-chart water.** §6.18's specification: narrow cone, one
panel, three links, no search, no choreography.

---

## 8. Worked examples

### 8.1 The hero — "Dive 214 begins" (home, top)

**What the visitor gets.** A black page that is already complete: the
hero panel printed (DIVE 214 · ACHERON FIELD · TARGET 2,512 M), the
headline set in `--cone-warm` Archivo — "Two and a half kilometres down,
the smokers are still burning." — with the depth numeral in mono, the
lede in Log register, and the descent's first log line beneath. Then
the lamps warm: the cone arms at 40vmin and widens to 92vmin over
1500ms (§6.1), the snow fades in behind it (§6.2), the hero panel wakes
in checklist order (§6.8), and at t≈2600 — if the visitor is still
here, and only then — the manipulator arm crosses the cone's lower edge
once (§6.6) and is gone for the session.

**Scroll timeline.** 0–15% of the hero's scroll range: the depth gauge
leaves 0 M; the bathymetry line (§6.7) begins its descent slope;
headline illumination holds (the hero is leaving the light as the dive
deepens — the surface gets darker behind you, which is true). 15–100%:
the hero's content dims toward the 55% floor as Station 1's panel
approaches the reading line; the temperature readout is still 2°C. The
hero never pins — a dive does not pause at the surface.

**Numbers on this section, and their sources.** Target depth 2,512 m
(§5.1). Launch 03:40 UTC (§5.1). Descent budget 55 min (printed in the
hero panel's footer: `DESCENT 55 MIN · BOTTOM 400 · ASCENT 45`). First
log line: "03:40 — Away from the ship. Lights on." — consistent with
§6.13's timeline.

### 8.2 Mid-page — Station 2, the Crab Fields, with a sample taken

**What the visitor gets.** The station arrives as procedure: panel first
(§6.8) — DEPTH settling at 2,495 M, TEMP at its diffuse behaviour,
PRESS resolving to 250.5 BAR by the printed law (1 + 249.5 = 250.5 ✓),
O₂ at 2.1 MG/L (diffuse flow, between the record's ambient 3.4 and vent
low 1.1 — an interpolated working value the panel's footer declares:
`O₂ INTERPOLATED BETWEEN STATION READINGS`). The headline: "A field of
white crabs, waving at the current." The lede explains the waving —
they farm bacteria on their claws in the shimmering outflow. Two camera
frames (§6.9) hang at the column's right: the colony at frame edge
shimmer-light (this is a diffuse zone — displacement peaks at 2px, not
6; the §6.3 law with this station's 18°C peak produces exactly that,
and the caption's printed note says `DIFFUSE FLOW — EDGE SHIMMER ONLY`).

**The sample.** The specimen card offers the moulted carapace — shed,
empty, left on the rock — with the ethic printed on the card: "We take
moult, shell and stone. Nothing living comes up." The living crabs
beside it carry `LOOK ONLY — LIVING` (§6.5). The visitor clicks **Take
sample**: the jar arcs 600ms into the basket's slot №2, the count line
moves to "2 / 6 JARS · 4.5 KG" (4.2 + 0.3 ✓), the live region announces
it, and the manifest row for Jar №2 is armed for its pulse when the
visitor reaches the surface (§6.14).

**Scroll timeline.** Station entry: bathymetry dot crosses the 2,495 m
tick and pulses; 150ms later the panel wakes (360ms). Mid-station: TEMP
scrubs 2 → 18 → 2 by the sin² law across the zone; the frames' shimmer
follows at its 2px cap. Station exit: the specimen card crosses the 55%
reading line — if the visitor hasn't clicked, the jar settles into the
basket by scroll (§6.4), because the dive collects its samples whether
or not the visitor does the arm's work. The two routes to the same jar
are the theme's whole interaction philosophy in one station.

### 8.3 Conversion — the berth request, filed

**What the visitor gets.** After surfacing — the berth section sits
after "Surface with Samples," because you ask to join the next dive
after you've completed this one — a manifest-sheet panel (§6.16):
`DIVE 215 · ACHERON FIELD · 8 BERTHS · 5 TAKEN`, the fields in ship's
order, the ballast check, and `FILE REQUEST`. The copy above the form
is two Log-register lines: the next dive's dates and what a berth is.
Nothing on the panel says "don't miss out." The record says 5 of 8;
the visitor can do arithmetic; urgency is left to the ocean.

**Submit timeline.** t=0 click: `FILING…`, panel dims, `TRANSMITTING
TO NORTHLIGHT…`. t≈700 (typical response): the stamp lands —
`LOGGED · BERTH 6 OF 8 · DIVE 215` — focus moves to the confirmation
heading, the count above the form corrects itself to 6 TAKEN, and the
confirmation prints the one operational fact that matters: "The chief
scientist's office writes within two working days. Your request is in
the manifest for Dive 215." A `FILE ANOTHER REQUEST` ghost action
re-opens the form; the next confirmation would stamp BERTH 7 OF 8, and
at 8 the form becomes the fully-berth state (§6.16) — the arithmetic
never breaks because the count and the stamp are one value, printed
twice.

**Failure rehearsal.** Submit with a malformed email: the field's keel
turns sulphur, and the line beneath reads, in full: `THAT ADDRESS
WON'T RECEIVE THE SHIP'S REPLY. CHECK IT AND FILE AGAIN.` — the error
says what is wrong, why it matters, and what to do, in the voice of
someone who has filed paperwork in weather. The rest of the form is
untouched.

---

## 9. Anti-slop — how this theme goes cheap, and the cure

1. **The aquarium screensaver.** Snow everywhere, shimmer on everything,
   the arm crossing every minute, bubbles rising for no reason. *Cure:*
   the two-ambient-loop law (§1) and the arm's once-per-session rule
   (§6.6). The deep is mostly still; motion is rationed like oxygen.
2. **Horror-movie darkness.** Content lurking at 10% brightness,
   jump-scare reveals, text the visitor must hunt. *Cure:* the 55%
   illumination floor (§6.1) and the law that darkness is applied over a
   lit page — the theme is a workplace at night, not a haunted house.
3. **Sci-fi cosplay.** Neon cyan, holographic grids, a HUD with rotating
   rings and fake telemetry graphs. *Cure:* the palette is sulphur,
   shell and sonar green on black water; instruments are mono text in
   ruled panels. If it looks like a starship, it has left the ocean.
4. **Invented numbers.** A depth of "2,500 m" in the hero, 2,512 in the
   manifest, "about 350 degrees" in the copy. *Cure:* the dive record
   (§5.1) and the §10 figure audit. Every number traces or the build
   fails; approximations are printed as approximations, with their law.
5. **The progress bar.** A thin web bar wearing a depth costume.
   *Cure:* progress here is a gauge (metres, now) and a basket (jars,
   kept) — §11 refuses the bar outright.
6. **Stock-photo vent cosplay.** Generic deep-sea imagery captioned with
   the wrong species at the wrong depth. *Cure:* §6.9's evidence rule —
   every frame is captioned with camera, time, depth and subject, and
   the caption is auditable against the station it illustrates.
7. **The gamified dive.** Points, badges, "Achievement: reached the
   smokers!", a leaderboard of readers. *Cure:* the basket fills because
   the *dive* collects, not because the visitor is winning. §6.4 keeps
   the visitor's basket and the dive's manifest distinct on purpose.
8. **Sulphur confetti.** The heat colour sprayed over buttons, links,
   headings and badges until nothing reads as hot. *Cure:* the sulphur
   census (§2) — one action, one marker, one panel's data per viewport.
9. **The cursor with a flashlight.** A pointer-tracked light blob
   trailing the mouse. *Cure:* refused in the original entry and here —
   the cone is the vehicle's, fixed and autonomous; the visitor pilots
   by scrolling, and the system cursor stays the system cursor.
10. **Brochure voice in a working vehicle.** "Discover the magical
    wonders of the deep!" *Cure:* §12's two registers. The log is terse
    and past-tense; the instruments are present-tense numbers. Wonder is
    permitted only as a consequence of accurate reporting.
11. **The white flash.** Any transition, modal or load that flashes a
    light background into a dark-adapted visitor's eyes. *Cure:* every
    state change in the theme travels through black or through panel
    grey; §6.10's watchdog makes a stuck black impossible and a white
    flash unthinkable.
12. **Fake live data.** Panels whose values are random, or a "LIVE"
    badge on a static page. *Cure:* every value is a function of scroll
    or a printed static — the page never claims to be live; it claims
    to be a *log*, which is why its timestamps are in the past.

---

## 10. Quality gate

Blocking checks — the theme may not ship in a build until all pass.

1. **Figure-truth audit.** Every depth, temperature, pressure, O₂ value,
   weight, time and count on every page is traced to §5.1 or derived by
   a printed formula. Spot-checks must include: pressure at three
   depths by P = 1 + d/10; the manifest total (10.3 kg) by re-adding
   the rows; the briefs' bottom times summing to 400; the log timeline
   (03:40 + 55 + 400 + 45 = 12:00).
2. **Lights-on test.** With JS disabled, the entire site is readable,
   navigable and complete; the cone, snow, flights and wakes are absent
   and nothing is missing where they were.
3. **Watchdog drill.** With the shared loop deliberately stalled: the
   cone lifts by 2000ms, panels print their static lines by 3000ms,
   the transition overlay clears by 2500ms, a jar flight resolves by
   1200ms. No drill may leave darkness, a blank panel or a lost sample.
4. **Floor test.** At every scroll position, body text outside the cone
   measures at or above the 55% illumination floor and ≥4.5:1 effective
   contrast.
5. **Ratchet test.** Scroll up after passing three stations: the
   bathymetry line stays drawn, collected jars stay collected, woken
   panels stay online. History does not erase.
6. **One-record grep.** The strings for the record's key figures
   (2,512 · 352 · 10.3 · 400 MIN · BERTH) appear only in their licensed
   printings; any fourth, unlicensed value (e.g. a stray "2,500 m")
   fails the build.
7. **Sulphur census.** Per viewport at load and at three scroll stops:
   ≤1 primary action, ≤1 station marker, ≤1 panel's data in sulphur.
8. **Arm discipline.** The manipulator arm renders at most once per
   session, never under reduced motion, never on <768px, and is
   cancelled — not relocated — if the hero is off-screen at trigger.
9. **No-NaN sweep.** Automated pass over every panel value at 50 scroll
   stops: no `NaN`, no blank, no value outside its function's range.
10. **Reduced-motion completeness.** The reduced variant is reviewed as
    a design in its own right: lit, static, fully informed — including
    static ambient/peak printings in every panel.
11. **Performance budget (§14) verified** on a mid-tier Android over
    4G: LCP, frame cost, and the cut order rehearsed by disabling
    features in sequence.
12. **Gate sign-off by a non-builder.** The person who signs did not
    write the code; the figure audit is re-run by hand, from the
    printed page, with a calculator — the theme's values must survive
    being checked the way a manifest is checked: slowly, and against
    the source.

---

## 11. Component inventory

Every component a real site in this theme needs, with its treatment.
Components the theme refuses are listed with their in-world replacement
— a refusal without a replacement is a gap, not a stance.

| Component | Treatment in this theme |
|---|---|
| Primary button | Sulphur fill, vent-black label, fill rises 180ms `sonar` on hover. One per viewport (§2 census). Reserved for the dive's real actions: Take sample, File request. |
| Secondary / ghost button | Transparent, `--plume-grey` hairline, `--shell` label; hover brightens the hairline to `--plume-text`. |
| Text link | `--sonar`, underlined by a `--sonar-deep` rule that deepens on hover. Visited links shift to `--sonar-deep` with a small check-stroke (the log remembers). |
| Station nav | §6.11 — sonar contact list with ping on change. |
| Bathymetry rail | §6.7 — the in-page navigation twin. |
| Instrument panel | §6.8 — the theme's signature container; all data lives in panels or tables, never in loose divs. |
| Depth gauge | Mono readout docked to the basket (§6.4): `DEPTH 1,204 M`, tabular, always current. |
| Sample basket | §6.4. |
| Specimen card | §6.12. |
| Camera frame | §6.9. |
| Data table (manifest) | §6.14 — ruled, not shaded; DOM-audited totals. |
| Accordion (station briefs) | §6.15 — the plan drawer. |
| Form inputs | `--panel` fill, `--plume-grey` hairline, mono labels above; focus draws the `--sonar` keel (§6.16). 16px minimum text. |
| Select | Native `<select>` in panel dress — the ship uses standard parts; no custom dropdown theatre. |
| Radio / checkbox | Square, sonar-checked (a drawn stroke, §6.5's completion mark). The ballast check (§6.16) is a checkbox with a paragraph's worth of honesty beside it. |
| Badge / tag | Station tags: mono, `--panel` fill, `--sonar-deep` rule. Heat tags (hazard): sulphur text on panel, never a sulphur fill at badge size. |
| Alert — notice | Sonar-ruled panel line: `NOTE —` + Log-register sentence. |
| Alert — caution | Sulphur-ruled panel line: `CAUTION —` + the fact + the action. (No red exists in this theme; sulphur is its caution, §6.16.) |
| Pagination | Dive-unit pagination (§6.13): `EARLIER DIVES` / `LATER DIVES` ghost actions with dive numbers in mono. Numbered pills refused — dives are the unit of archive. |
| Progress bar | **Refused.** Replaced by the depth gauge (position) + the basket (kept results) — §5.3. |
| Spinner | **Refused.** Replaced by status lines in the panel register (`TRANSMITTING TO NORTHLIGHT…`, `PANEL WARMING`) — a vehicle reports; it does not spin. |
| Toast | **Refused.** Replaced by the basket's live-region announcement (§6.4) and, where visible confirmation is needed, a line added to the page's log (§6.13) — messages join the record instead of floating over it. |
| Modal | **Refused for content; one exception:** the camera frame's full view (§6.9) opens as a lights-on dialog — examining evidence is a surface activity. Focus-trapped, Esc closes, returns focus. |
| Tabs | **Refused.** Stations are a traverse, not tabs; the briefs (§6.15) handle selectable depth of detail. |
| Tooltip | Instrument glosses (§6.8) expand in place on hover/focus/tap — never floating bubbles that the cone would have to light. |
| Skeleton | §6.17 — unlit frames, labelled, 1500ms ceiling. |
| Breadcrumbs | On detail pages only, in mono: `FIELD / STN 2 / SPECIMEN` — a position fix, styled as coordinates, not a trail of pages. |
| Footer | §6.18 — the ascent. |
| 404 | §6.18 — off-chart water. |
| Search | A log-index search on archive pages: a single mono input over the dive-log corpus; results are log entries with their citations (§6.13), never a generic results grid. Labelled `SEARCH THE LOG`. |

---

## 12. Copywriting voice

Two registers, and the page never mixes them inside one element.

**The Instrument register** (JetBrains Mono, present tense, no voice at
all): labels, values, statuses. Uppercase labels; numbers with units,
always (`2,512 M`, never "deep"); statuses as verb phrases in progress
(`PANEL WARMING`, `TRANSMITTING TO NORTHLIGHT…`). The instrument never
says "you", never apologises, never exclaims.

**The Log register** (Archivo, past tense, first person plural, terse):
the expedition speaking after the fact. Short sentences. Numbers welcome
(in mono). Wonder is allowed exactly once per station, and only after
the facts. The log's "we" is the crew; the visitor is never "we" until
the berth form (§6.16), where the invitation is precisely to join it.

**Headline style.** A concrete image from the station, stated plainly:
✓ "A field of white crabs, waving at the current." ✓ "The chimney has
been venting since before the ship was built." ✗ "Discover the magical
hidden wonders of the deep!" ✗ "Dive into an unforgettable underwater
adventure." Headlines never use the words *magical, amazing, stunning,
unforgettable* or *adventure* — §10's grep list.

**Label style.** Labels name the thing and its state, not the feeling:
✓ `TAKE SAMPLE` ✓ `FILE REQUEST` ✓ `LOOK ONLY — LIVING` ✗ `Grab your
treasure!` ✗ `Claim your spot now!`

**Error voice.** What is wrong, why it matters, what to do — in Log
register, on the panel: ✓ "THAT ADDRESS WON'T RECEIVE THE SHIP'S REPLY.
CHECK IT AND FILE AGAIN." ✓ "THE REQUEST DID NOT REACH THE SHIP. YOUR
ENTRIES ARE AS YOU LEFT THEM — FILE AGAIN." ✗ "Oops! Something went
wrong 😞" ✗ "Invalid input."

**Empty-state voice.** The fact, stated with dignity: basket — "BASKET
EMPTY — THE DIVE IS YOUNG." Manifest — "NO SAMPLES — THE DIVE IS
LOGGED, THE BASKET IS EMPTY." Search — "THE LOG HAS NO ENTRY FOR THAT.
THE DIVE ITSELF IS ABOVE." Emptiness is a survey result, not a failure.

**Fixed strings (verbatim, do not paraphrase):**
- "We take moult, shell and stone. Nothing living comes up."
- "Surface with Samples" (final section title)
- "NO CHART FOR THIS WATER" (404 headline)
- "PANEL WARMING" (skeleton status)
- "BASKET EMPTY — THE DIVE IS YOUNG."

**Numbers in copy.** Always the record's numbers, always with units,
always mono — including inside headlines and log sentences. If a number
isn't in the record or derivable by a printed law, it doesn't appear;
"thousands of crabs" is acceptable (a count nobody took is written as a
word, not a digit).

---

## 13. Scroll choreography map

The home page, top to bottom. Every beat names what the visitor sees and
what the instruments say. All scrubbed beats run on the shared loop
(lerp 0.085); all triggered beats fire once.

1. **Arrival (0%, lit page).** The complete page, lights on. Depth 0 M.
2. **The lamps warm (t=120–1620ms).** Cone widens 40 → 92vmin; snow
   fades in; hero panel wakes in checklist order. The visitor
   understands: *I am in a vehicle, and it has just switched on.*
3. **The sighting (t≈2600ms).** The manipulator arm crosses once, low,
   and is gone (§6.6). Nothing refers to it. The dive feels piloted
   from here on.
4. **Descent (hero scroll).** Depth gauge climbs through the hundreds;
   the bathymetry line draws its slope; the hero dims behind. TEMP
   holds 2°C. The water column is the page's first long read — mostly
   darkness, snow, and falling numbers.
5. **Station 1 — Smoker Garden.** Dot crosses the 2,512 m tick; panel
   wakes; TEMP begins its sin² climb as the plume zone scrubs: 2 →
   352 → falling. Frames warp at their edges (6px at centre). Jar №1
   settles at the reading line. *Feeling: arrival at the fire.*
6. **Station 2 — Crab Fields.** Depth 2,495 M; TEMP's small 18°C swell;
   frames shimmer at 2px only. The visitor may take the moult
   themselves (§8.2). *Feeling: the garden around the fire.*
7. **Station 3 — Plume Traverse.** The page's one pin (160vh): the
   frame holds while TEMP crosses 120°C at the plume's core and the
   water column itself seems to rise past. Jar №3 is a filter of that
   plume — the sample is the medium. *Feeling: crossing the smoke.*
8. **Station 4 — Mussel Beds.** Calm water, 9°C. The brief (§6.15) for
   the remaining stations sits after this station — the plan, reviewed
   mid-dive, where a crew would review it.
9. **Station 5 — Old Chimney.** TEMP never rises (2°C, dead). The
   panel's peak line prints `PEAK 2°C — THIS CHIMNEY IS COLD.` The
   basalt glass jar is the dive's heaviest science per kilo of story:
   the vent that stopped. *Feeling: the ruin.*
10. **Station 6 — Shimmer Flats.** Diffuse warmth (24°C), tube worms,
    the last jar. The log (§6.13) follows — the traverse told back.
11. **Surface with Samples.** The ascent segment draws; depth falls to
    0 M; the fixed basket hands over to its enlarged twin; the
    manifest (§6.14) prints the dive; totals illuminate. *Feeling:
    surfacing with something.*
12. **The next dive.** The berth panel (§6.16 / §8.3) — the only ask on
    the page, placed after the evidence.
13. **Ascent footer (§6.18).** Totals a fourth time, closing log lines,
    sign-off. The gauge reads 0 M. Every instrument reads *finished*.

**Reverse pass.** Scrolling up reverses every scrubbed value by the
same functions (the vehicle rises; temperatures fall) — but the
ratchets hold (§10, check 5): drawn line, collected jars, woken panels
and read log entries stay done. Up is a revisit, not a rewind.

**Jump scroll.** Anchor travel and scrollbar drags land the loop's
smoothed value within ~600ms; panels woken out of order snap live
without ceremony (§6.8's queue rule); the arm never fires on a jump
(§6.6's cancellation). A visitor who teleports to the bottom gets the
full final state — manifest, totals, footer — with nothing pending.

---

## 14. Whole-page performance budget

Home page (the dive), mid-tier Android on 4G as the reference device:

| Budget | Limit |
|---|---|
| Total page weight | ≤880KB (images ≤520KB, fonts ≤118KB, JS ≤140KB gz, CSS ≤60KB, HTML+SVG ≤42KB) |
| Animation frame cost | ≤1.6ms/frame total across all systems (cone ≤0.3, snow ≤0.5, filters ≤0.5 when live, readouts ≤0.3) |
| Long tasks | None >50ms after load; the wake/flicker scheduling is chunked across frames |
| LCP | ≤2.5s on the reference device; the hero is text + gradients, so LCP is the headline, not an image |
| CLS | 0 from animation and loading (reserved aspect ratios, skeleton mirroring, law 5) |
| Interaction latency | Click-to-sample flight starts within 1 frame of the click; form feedback within 100ms |

**Cut order** (when the budget is exceeded, cut in this order, and the
page must remain complete after every cut):
1. Marine snow turbulence (keep base drift).
2. Marine snow entirely → static texture (§6.2's fallback).
3. Heat-shimmer on all but the pinned traverse frame.
4. Heat-shimmer entirely (temperature readouts carry the story).
5. Cone breathing and pressure response (cone still widens on load).
6. The manipulator arm (already once-only; cutting it costs a mood,
   not a fact).
**Never cut:** the lights-on fallback, any watchdog, the figure record,
the basket/manifest content, the reduced-motion variants, focus
visibility. A page that loses its honesty to keep its shimmer has the
budget exactly backwards.

---

## 15. Build-order checklist

1. **The record first.** Encode §5.1's dive record as the single data
   source; every component reads from it. No number is typed twice.
2. **The static lit page.** Full HTML, lights-on design, all content,
   all static printings (panel static lines, manifest totals, footer
   totals). This page must pass §10 checks 1, 2 and 10 before any
   animation exists.
3. **Panels and tables.** §6.8 static → §6.14 with its recomputation
   watchdog → §6.15 briefs (DOM-open by default).
4. **Navigation shell.** Masthead (§6.11), rail (§6.7) fully drawn,
   footer (§6.18).
5. **The cone.** Arm the darkness over the lit page (§6.1) with its
   2000ms watchdog; add the lights-on toggle and rehearse the drill.
6. **The shared loop.** Lerp plumbing; wire depth/temperature/pressure
   functions; verify against the record at 50 scroll stops (check 9).
7. **Snow** (§6.2) with its density zoning and frame watchdog.
8. **Basket + sampling.** §6.4 slots, §6.5 flights with the 1200ms
   watchdog, live-region announcements, the two collection routes.
9. **Shimmer** (§6.3 + §6.9) last among the scrub systems — it is the
   most expensive and the most cuttable.
10. **The arm** (§6.6) — one SVG, session flag, cancellation rules.
11. **Transitions + skeletons** (§6.10, §6.17) with their watchdogs.
12. **The form** (§6.16) — native-first, JS enhancement, the berth
    arithmetic tested at 5, 6, 7 and 8 taken.
13. **Reduced-motion pass.** Build the variants as designs; review
    them with fresh eyes (check 10).
14. **Breakpoint pass.** ≥1200 / 768–1199 / <768 for every element's
    specced behaviour — especially the basket's three forms and the
    rail-to-strip transformation.
15. **The gate.** §10 in full, signed by a non-builder, figure audit
    by hand. Then — and only then — the theme may be used in a build.
