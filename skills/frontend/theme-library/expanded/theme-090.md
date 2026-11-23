# Theme 090 — Cymatics Garden (50x Expansion)

*Sound made visible as a garden. Tones draw Chladni patterns in sand on a bronze plate; frequencies bloom into geometry; the site is a quiet conservatory where every section hums at its own pitch. The hero image is not an image — it is an equation, computed live.*

---

## 1. Concept & world

A cymatics plate is a brass or bronze sheet covered in fine sand, bowed or driven at a resonant frequency. The sand flees the vibrating regions and collects along the nodal lines — the still curves where the plate does not move — and a figure appears: a star, a lattice, a flower of geometry that nobody drew. Change the pitch and the figure dissolves, boils, and re-forms into a different, more complex figure. Cymatics Garden builds a whole website inside that one physical fact. The page is a conservatory: a bronze plate pinned centre-stage from the first viewport to the footer, and the content arranged around it in beds, the way planting beds arrange around a fountain. Every section of the page owns one rung of a single declared frequency ladder (§6.17): a pitch in hertz, a pair of Chladni indices (n, m), and a marginal waveform whose cycle count steps up as the visitor descends. Scrolling is retuning. The visitor never "navigates to a new page section" in this theme's felt experience; they walk deeper into the garden and the instrument changes key under their feet — the current figure dissolves into chaos mid-scroll, glides, and locks into the next section's figure with a resonant settle, the way a struck plate rings and then holds its tone.

The garden's mood is quiet, exact, and faintly ceremonial. This is not a music-visualiser skin and it is not a psychedelic audio toy. Nothing here pulses to a beat, nothing glows neon, nothing is decorative waveform clip-art. The beauty on offer is the beauty of a proof: every figure on the page is the output of the real Chladni equation for a square plate,

F(x, y) = cos(nπx/L)·cos(mπy/L) − cos(mπx/L)·cos(nπy/L) = 0,

evaluated with the very (n, m) indices printed beneath the figure, at the very frequency printed beside them. A scientifically literate visitor can check the maths, and the theme is designed to survive that check. That checkability is the brand.

**The theme's one law: the sand only ever shows what the equation says.** No curve, squiggle, star, or "sound-wave" decoration may appear anywhere on the page unless it is (a) the nodal set of F for a stated (n, m), (b) a true sine waveform at a stated frequency ratio, or (c) a labelled photograph or illustration of a physical object (a specimen under glass, §6.9), which is a picture *of* the garden, not a claim *by* the garden. Every printed frequency is the frequency the adjacent figure was computed at; every printed index pair is the pair in the function call; every counter that settles, settles on a number taken from the one ladder record (§6.17). If a figure cannot be computed — no canvas, no JavaScript, a failed worker — the page prints the figure's pre-rendered static plate and says nothing false about it. The garden never fakes a bloom.

**Best-fit sites and audiences.** Audio and loudspeaker brands whose product story is physical sound; music-education platforms that teach acoustics, harmonics, and the mathematics of vibration; sound-healing and resonance-therapy technology that needs calm credibility rather than incense clichés; science museums and exhibition microsites; instrument makers (bowed strings, handpans, singing bowls, plate reverb) whose craft is literally resonance; acoustics consultancies and anechoic-lab services; a record label or composer whose identity is built on one instrument's overtone series. The audience is patient and literate: people who read captions, who will notice that the indices under the figure are the indices in the figure, and who distrust decoration that pretends to be data.

**When NOT to use it.** Not for high-frequency trading, news, or anything that must feel urgent — the garden's fastest event is an 800ms glissando and its whole posture is unhurried. Not for dense transactional catalogues with hundreds of SKUs; the plate is a centre-stage instrument and a 400-row table fights it (the programme table, §6.12, caps at a sitting's worth of rows). Not for brands whose sound identity is loud, bass-heavy, or club-oriented — cymatics is the visible geometry of *pure tones*, and the theme will make a dubstep brand look like a liar. Not where the client will demand stock "audio waveform" graphics, equaliser bars, or neon glow: those are exactly the counterfeits the law forbids, and bolting them on collapses the theme's one claim. Not for content with no frequencies in it at all — if the site cannot honestly assign each section a rung of a ladder (a programme, a curriculum, a set of instruments, a scale of sessions), the garden has nothing to grow and another theme should be chosen.

**The world, concretely.** The conservatory has: one bronze plate (the instrument), sand (the medium), beds (sections), a margin where waveforms keep the score, water in the margins answering bronze with slow ripple rings, glass-green specimen frames (the exhibits), a programme table (the season's soundings), a booking form that lets the visitor choose the pitch of their own visit, and a resting state — the garden at rest, plate formed at the first rung, when nothing is being asked of it. Every element specified in §6 is one of these things. Nothing enters from outside the world: no generic toast, no spinner, no badge pill; §11 gives each ordinary component its conservatory treatment or refuses it outright.

---

## 2. Palette

Five anchors, taken unchanged from the theme's original entry. The ground of the page is sand plate — the pale, dry colour of the plate's sand bed and of conservatory paper. Bronze is the instrument's metal: structure, rules, the plate's rim, large display furniture — never body text on sand (3.6:1, measured below). Pattern ink is the text colour and the colour of the drawn figure's printed line. Bloom scarlet is the garden's one flower: spent only where something blooms — the click-to-sound flash (§6.7), the live rung marker, the form's confirmation seal — rationed to at most three appearances per viewport. Glass green is the specimen glass and the frames of exhibits: a graphic colour, never a text colour.

| Token | Hex | Role | Usage ratio | Pairing / contrast ruling |
|---|---|---|---|---|
| `--sand` | `#E4DCC8` | Page ground; the plate's sand bed; card paper | ~55% of surface | Ground for `--ink` text: **10.9:1** — the page's default text pairing |
| `--bronze` | `#8A6D3B` | The plate, rims, rules, display furniture, ladder rail | ~15% | On `--sand`: **3.6:1** — display ≥24px and graphics only, never body text; `--sand` on `--bronze` also 3.6:1, same ruling |
| `--ink` | `#2E2A24` | All body text; the printed figure line; inscriptions | ~18% | On `--sand` 10.9:1 (AAA); on `--bronze-lit` 4.6:1 — plate inscriptions only, ≥14px |
| `--bloom` | `#B3402A` | Blooms: click-to-sound flash, live-rung marker, confirmation seal | ≤3% | On `--sand`: **5.4:1** — text ≥14px permitted for the marker word only; primarily a graphic accent |
| `--glass` | `#5C7A5E` | Specimen frames, glass dividers, bed edging | ~9% | On `--sand`: **3.4:1** — graphics and frames only, never text |
| `--sand-lit` | `#EFE8D6` | Raised sand: card faces, the form leaf, tooltip paper | derived | With `--ink`: 12.4:1 |
| `--sand-deep` | `#CFC3A6` | Recessed sand: table row alternation, skeleton beds, footer soil line | derived | With `--ink`: 7.8:1 |
| `--bronze-deep` | `#6B5327` | The plate's shadowed rim, footer plate, pressed states | derived | With `--sand`: 5.1:1 — small inscriptions permitted on the footer plate |
| `--bronze-lit` | `#A5854E` | The plate's lit face where inscriptions sit; hover-lit rim | derived | With `--ink`: 4.6:1 (AA, ≥14px) |
| `--bloom-deep` | `#8E3120` | Pressed bloom, the seal's shadow edge, error underline | derived | On `--sand`: 7.3:1 — error text permitted |
| `--glass-deep` | `#425C46` | Specimen frame shadow side, bed edging in shade | derived | Graphic only |
| `--night-soil` | `#23211B` | Dark-scheme ground (see below) | scheme only | With `--sand` text: 13.6:1 |

**Contrast method.** Ratios above are computed from the hex values by the WCAG relative-luminance formula for this expansion, not estimated. The two forbidden pairings are load-bearing and are checked in the quality gate (§10): `--glass` text on `--sand` (3.4:1, fails) and `--bronze` body text on `--sand` (3.6:1, fails). Any builder who sets a paragraph in bronze has broken the theme even if the page "looks fine."

**Dark behaviour — "the garden at dusk," not an inversion.** Under `prefers-color-scheme: dark`, the conservatory glass darkens; the exhibits do not. The page ground becomes `--night-soil`; body text becomes `--sand` on it (13.6:1). The plate itself stays exactly as it is — sand bed, bronze rim, ink figure — because the plate is a lit object in the conservatory, the way a museum case stays lit after dark. Specimen frames keep `--glass`; bloom keeps its hex (a flower does not change colour at dusk). Cards become `--sand` leaves resting on the dark soil rather than dark cards: in this theme, content is always printed on sand. There is no fully-dark content surface anywhere in the theme, in either scheme.

**Colour discipline.** Scarlet is rationed like a flowering: the live-rung marker in the ladder readout (§6.3), the bloom of a sounded element (§6.7), and the seal on a booking confirmation (§6.13) are its only licensed appearances, and no viewport may show more than three. Bronze is a material, not a colour wash: it appears where metal would be — rims, rules, the rail — and a section background in flat bronze is forbidden. Glass green edges things; it never fills a panel. Sand is the default state of every surface the visitor reads.

---

## 3. Typography

Two families, exactly as the original entry specifies — no third family is added, and the "mono" voice the original asks for in its printed indices is achieved inside Space Grotesk (see the inscription register below), not by smuggling in a monospace font.

- **Fraunces** — display. The garden's serif: soft, organic, slightly old-style, with optical sizing that lets a headline feel grown rather than set. Used for headlines, bed titles, the plate's engraved title, and numerals in display contexts (Fraunces' old-style figures are the garden's figures — a frequency in Fraunces at display size is a carved number).
- **Space Grotesk** — body, labels, data. A grotesque with a technical spine; carries body text, captions, the programme table, form labels, and — with tabular figures engaged — every readout.

**The type scale** (root 16px; display in Fraunces, text in Space Grotesk):

| Role | Size / line-height | Family & settings | Used for |
|---|---|---|---|
| Display 1 | 64px / 1.02, −0.01em | Fraunces 72pt optical, weight 560 | Hero headline at the plate's calm centre |
| Display 2 | 44px / 1.08 | Fraunces, weight 540 | Bed titles |
| Display 3 | 30px / 1.14 | Fraunces, weight 520 | Card titles, the form's heading, footer plate title |
| Heading | 21px / 1.3 | Space Grotesk 600 | Sub-heads inside beds, table group heads |
| Body | 17px / 1.62 | Space Grotesk 400 | All reading text; measure capped at 62ch |
| Body small | 15px / 1.58 | Space Grotesk 400 | Secondary text, card bodies |
| Caption | 13px / 1.5 | Space Grotesk 400 | Specimen captions, figure notes |
| Inscription | 12.5px / 1.4, +0.14em, uppercase | Space Grotesk 500, `font-variant-numeric: tabular-nums` | The printed (n, m) indices, frequency readouts, ladder rail labels — the plate-inscription register |
| Data | 15px / 1.5, tabular-nums | Space Grotesk 500 | Programme table figures, counters |

**Type laws.**
1. **Numerals are data or they are carving.** A frequency, an index, a count: set in the inscription or data register with tabular figures, always with its unit (`110.00 Hz`, `(n, m) = (3, 2)`), never rounded silently — the ladder's frequencies print at two decimals because the record (§6.17) holds two decimals.
2. **Headlines name growing things and sounding things** — beds, tones, figures — in Fraunces, sentence case, no more than seven words; the garden does not shout, so Display 1 is the only size above 44px on the page and it appears once.
3. **No letterspaced lowercase, no uppercase body.** Uppercase exists only in the inscription register, where it behaves like lettering stamped under a plate.
4. **The word for a figure is "figure."** Captions and copy call the Chladni patterns *figures*, the sections *beds*, the pitches *rungs* — §12 fixes the vocabulary; type follows it (a bed title is a plant label, set like one).
5. **Type never trembles.** The resting-tone tremble (§6.5) moves sand only; no text element ever jitters, vibrates, or blurs — the garden's stillness is typographic even when its sand is alive.

---

## 4. Layout language

**The plate pins centre-stage.** The defining layout fact, from the original entry: one bronze plate — a square, rimmed, sand-covered — sits at the centre of the page's composition and remains the visual anchor from hero to footer. On desktop (≥1200px) the plate is a sticky element in the centre column of a three-column conservatory grid: a left margin (the score margin, 120px, where waveforms live, §6.4), the centre stage (the plate, 520–600px square), and the beds arranged in the right and lower field as the visitor scrolls. Each bed, as it becomes the active section, retunes the pinned plate (§6.2): the visitor reads the bed's text beside the very figure that bed sounds. On tablet the plate unsticks to the top of each bed in turn (a smaller plate, 380px, travelling with its section). On mobile the plate sits above each bed's text at 78vw, and the glissando happens in place. The plate is never a background, never dimmed behind text, never cropped: it is an instrument on a stand, and the layout is the room built around it.

**Grid and rhythm.** A 12-column grid at ≥1200px (max width 1440px, gutters 32px), 8 columns at 768–1199px, 4 below 768px. Vertical rhythm is the *bed rhythm*: each bed is separated from the next by a glass-green edging rule and a full measure of sand — 96px of empty ground on desktop, 64px tablet, 48px mobile — because a conservatory is mostly path and air. Whitespace here is soil and path: it is the ground things grow in, and it is never "filled" with decoration. The score margin is sacred: nothing enters the left 120px except the waveforms, the ladder rail (§6.10), and the ripple rings' outer edges (§6.8).

**Density rules.** One figure per bed. One bed per viewport-height, roughly — a bed's text is capped near 340 words so the plate's retune, not the scroll, marks the chapter change. Cards (§6.11) come in beds of three at most. The programme table (§6.12) caps at 12 rows per sitting. The page's total sounded rungs are the ladder's rungs (§6.17) — six — and no page may invent a seventh section with a seventh pitch; a longer page adds unsounded beds (text at rest against the resting figure) rather than new frequencies.

**Section choreography (summary; full map in §13).** Hero: the plate forms its first figure and the headline settles into the calm centre. Then beds in ladder order — pitch ascending, figures complexifying, marginal waveforms stepping 2 → 3 → 5 → 8 cycles. The programme table is the garden's middle: the one place the visitor reads rows instead of beds. The form is the last sounded bed: the visitor chooses a rung and the plate sounds *their* figure as the confirmation. The footer is the garden at rest: plate printed at rung 0, the whole ladder inscribed on the footer plate, and stillness.

---

## 5. Full motion system

All motion in the garden is one of five physical behaviours, each with a named easing. There is no generic "fade-up" anywhere in the theme: things form, glide, bloom, ripple, or tremble — the five things sand, tone, and water actually do.

**Named easings.**
- `--ease-resonate` — `cubic-bezier(0.22, 1.4, 0.36, 1)` with the overshoot damped by the choreography, not the curve: the settle of a figure locking in, a struck plate's ring decaying into stillness. Used for figure lock-in, counter settle, seal press.
- `--ease-gliss` — `cubic-bezier(0.45, 0, 0.55, 1)`: the glissando — an even, unhurried pitch glide with no accent at either end.
- `--ease-bloom` — `cubic-bezier(0.16, 1, 0.3, 1)`: a bloom opening — fast unfurl, long soft arrival. Click-to-sound, specimen focus.
- `--ease-ripple` — `cubic-bezier(0.25, 0.6, 0.35, 1)`: water leaving a centre — decelerating expansion.
- `--ease-drift` — `cubic-bezier(0.4, 0, 0.2, 1)`: sand and margin movement, hovers, the ladder rail's marker travel.

**The one loop.** Every scroll-scrubbed or continuous value — plate jitter amplitude, waveform draw progress, rail marker position, ripple phase, counter values during a settle — is driven by a single `requestAnimationFrame` loop that lerps each registered value toward its target at **0.12** per frame (0.08 for the plate's chaos amplitude, which must feel heavier). No scroll handler writes a style. The loop sleeps when the tab is hidden and when every registered value is within 0.001 of target and no ambient behaviour is armed; ambient behaviours (tremble, ripples) keep it awake only while their section is within one viewport of the reader.

**Motion terms, in the garden's language.**
- *Scroll-triggered reveals:* beds do not reveal — they **sound**. A bed entering arms its rung; the plate glissandos (§6.2) and the bed's own content is already fully printed beneath (reveals move sand and light, never text opacity from zero).
- *Scroll-driven / scrub animation:* the glissando's chaos amplitude is scrubbed to scroll position between bed thresholds (§6.2); the ladder rail marker travels scrubbed (§6.10).
- *Parallax:* three depths only — margin waveforms at 0.92×, beds at 1.0×, specimen glass glints at 1.06×. The plate never parallaxes; an instrument on a stand does not drift.
- *Pinned sections:* the plate stage pins on desktop for the page's whole sounded length (§4); the programme table's header row pins inside its bed.
- *Smooth scrolling:* native, with the loop's lerp supplying the felt smoothness; `scroll-behavior: smooth` for in-page ladder jumps (§6.10).
- *Progress indicator:* the marginal waveform's cycle count plus the ladder rail's rung marker (§6.3, §6.10) — progress is pitch, printed.
- *Staggered + masked reveals:* the hero headline settles line by line into the figure's calm centre (120ms stagger, §6.1); bed titles rise through a sand-mask (a `--sand` block that drifts down like settled sand, 500ms `--ease-drift`).
- *Kinetic typography:* refused, with one exception — the frequency readout's digits count (§6.18). Headlines do not move; a conservatory label is not a marquee.
- *Marquee:* **refused.** Nothing in a garden scrolls sideways forever. The programme table is a table.
- *Counters:* frequencies and counts settle with `--ease-resonate` (§6.18) — they ring, briefly, then hold the exact figure.
- *SVG line-draw:* marginal waveforms draw (§6.4); the footer ladder inscription underlines itself once on first view (§6.15).
- *Image scale-in-frame:* specimen photographs scale 1.06 → 1.0 inside their glass frames (§6.9) — focusing, not zooming.
- *Hover / micro-interactions:* fingertip-on-the-rim (§6.6) — hover is acoustic contact; links deepen to `--bloom-deep` underline drawn left-to-right 240ms; buttons press like a plate key (§11).
- *Custom cursor:* **refused** — normal system cursor only, per standing rule; the visitor's hand is on the rim (§6.6), not replaced by a gadget.
- *Skeleton loading:* re-sanding (§6.14) — beds print as raked, empty sand with their labels already set.
- *Page transitions:* the re-sanding veil (§6.14): sand sweeps flat, the new page's first figure forms.
- *Reduced motion:* §6 passim — the garden at rest: every figure printed as its static plate, every number at its final value, no tremble, no ripple, no glissando (figures change by cut between beds).

**Ambient loops — exactly two licensed.** The resting-tone tremble (§6.5) and the water-ripple rings (§6.8). Both pause off-screen, both die under reduced motion, and no third loop may be added: a garden with three things moving is a machine.

---

## 6. Signature elements

The nine original signature elements (§6.1–§6.9) are deepened, never redesigned. §6.10–§6.18 are the page-family elements the original layout implies — the pinned plate's navigation, the beds as cards, the programme table, the booking form, the transition, the footer, the silent bed, the ladder record itself, and the settling counters. All eighteen draw every figure from the one ladder record (§6.17) and the one equation. Where a number appears in an element's spec — a frequency, an index pair, a particle count — it is the number that element ships with.

### 6.1 Sand migrating into a Chladni star (hero formation)

**What & why.** On load, the bronze plate sits sanded flat and still. A tone "sounds" — visually only — and ~900 sand particles on the plate slide along the nodal lines of the real Chladni function for rung 0, (n, m) = (2, 1) at 110.00 Hz, settling over ~2.2s into a crisp four-pointed star. The headline then rests into the pattern's calm centre. This is the theme's thesis in one gesture: the hero image is physics, computed live on the visitor's machine, and it merges with content because the headline literally takes its place inside the figure — the calm centre of a (2, 1) figure is a real, quiet region of the plate, and the title sits in it.

**Structure.** A square `<canvas>` (plate face) inside the bronze rim (§6.10's stage), over a pre-rendered static SVG of the same (2, 1) nodal set (the no-JS / fallback layer). Particles are a Float32 array of positions; each frame, each particle samples |F| at its position and at four offsets, steps down the |F| gradient by a fixed stride, and adds Brownian jitter whose amplitude decays as the formation progresses. Settle test: a particle is *home* when |F| < 0.04 in normalised plate units; formation completes when ≥97% are home or the watchdog fires. The headline is DOM text in the plate's centre cell, printed from the start (see Fallback).

**Motion spec.** Total formation 2200ms. Phase 1 (0–300ms): the plate's rim catches light (a `--bronze-lit` sweep, `--ease-drift`). Phase 2 (200–1900ms): migration, stride easing from 2.2px/frame to 0.4px/frame as home-count rises. Phase 3 (1700–2200ms): the last jitter decays (amplitude 0.6px → 0), the figure "locks" with a 120ms `--ease-resonate` brightening of the settled sand. Headline lines settle at 1500ms, 1620ms, 1740ms (120ms stagger, translateY 10px → 0, `--ease-resonate`). Trigger: first paint + 150ms, once per session (a `sessionStorage` flag replays it only as the 600ms short form on repeat visits).

**Choreography timeline.** 0ms rim sweep begins · 200ms first particles move · 900ms star recognisable (home-count ≈55%) · 1500ms headline line 1 · 1620ms line 2 · 1700ms jitter decay begins · 1900ms migration ends · 2200ms lock brightening done; tremble (§6.5) arms.

**State matrix.** *Rest (pre-trigger):* flat sand, headline printed — the page is complete in this state. *Forming:* as above; pointer events on the plate disabled for the canvas only, text selectable throughout. *Formed:* tremble arms (§6.5); hover hands over to §6.6. *Scrolled-past:* formation never replays; the plate shows the current bed's figure. *Disabled (no canvas):* static SVG figure, identical composition. *Touch:* identical — formation is time-triggered, not pointer-triggered, on every device.

**Content-merge.** The figure is rung 0 of the ladder the whole page climbs; the headline sits in the figure's own calm centre; the inscription beneath the plate (§6.3) prints the figure's true indices. Remove the canvas and the hero still says everything — remove the headline and the figure is a screensaver, which is why they are one element.

**Breakpoints.** ≥1200px: plate 560px, 900 particles. 768–1199px: plate 380px, 420 particles, headline below the plate instead of centred in it (the centre cell is too small for 44px type). <768px: plate 78vw, 220 particles, formation shortened to 1600ms (stride scaled), headline below.

**Edge cases & failure modes.** Slow device: if the first 30 frames average >24ms, particle count halves and stride doubles (formation still lands ≈2200ms). Tab hidden mid-formation: the loop sleeps; on return, if elapsed >4000ms the figure snaps home (watchdog state) rather than resuming a stale glide. Content longer than expected: the headline is capped at 3 lines by the copy rules (§12); a 4th line overflows *below* the plate, never across the sand. Scrolling during formation: permitted; the glissando (§6.2) queues until lock or watchdog.

**Fallback & watchdog.** The static SVG figure is in the DOM beneath the canvas from first paint; the canvas starts transparent and only covers it once particles render. **Watchdog: 4000ms** — if home-count <97% at 4000ms, particles snap to their nearest precomputed nodal sample points (a 1,024-point sampling of the (2, 1) nodal set ships as data) and the lock proceeds. If canvas context creation fails, the canvas is removed and the SVG is the figure. With JS disabled, the SVG and headline are simply the hero.

**Reduced motion.** No migration: the static figure is printed, the headline rests in place, tremble never arms. The hero is a photograph of the garden at rest.

**Accessibility.** The canvas is `aria-hidden="true"`; the figure's meaning is carried by the inscription (§6.3) as real text: "Figure (n, m) = (2, 1) · 110.00 Hz". The headline is a normal `<h1>`; focus order is untouched by the plate (the plate is not focusable). Contrast: headline ink on the sand bed 10.9:1.

**Performance & mobile variant.** Canvas physics budget: ≤1.2ms/frame at 900 particles on a mid-tier laptop; gradient sampling is the only per-particle cost (no allocations in the loop). Mobile: 220 particles, ≤0.6ms/frame, DPR capped at 1.5 for the plate canvas. The static SVG is 6KB gzipped.

**Tokens.** `--sand`, `--bronze`, `--bronze-lit`, `--ink`, `--plate-size`, `--form-dur: 2200ms`, `--ease-resonate`, `--ease-drift`, `--particle-count` (set per breakpoint).

### 6.2 Glissando pattern changes (the retune)

**What & why.** Between beds, the plate retunes. As the visitor scrolls from one bed's territory into the next, the current figure dissolves into chaos — particles scatter with Brownian jitter — then re-forms into the next bed's more complex figure, scrubbed to scroll and timed like a pitch glide (~800ms of felt time). This is the theme's transition grammar: there are no page wipes, no fades between sections; the instrument changes key and the visitor hears it with their eyes. It merges with content because the retune *is* the chapter break — the bed you are entering is the figure now forming.

**Structure.** Same canvas and particle system as §6.1, plus a *chaos amplitude* value `c` ∈ [0, 1] registered in the shared loop. Between bed thresholds (the scroll interval where neither bed owns the plate), `c`'s target is a tent function of scroll progress: 0 at the outgoing bed's lock point, 1 at the interval's midpoint, 0 at the incoming bed's lock point. Particle behaviour blends by `c`: step direction = (1−c)·(gradient descent toward the *incoming* figure's nodal set) + c·(Brownian jitter at amplitude 2.4px). Because the incoming figure's gradient field is used throughout the second half, the chaos visibly *resolves toward* the new figure rather than teleporting.

**Motion spec.** Felt duration ≈800ms at reading scroll speed; the tent's width is 60vh of scroll. At the incoming lock point, a 140ms `--ease-resonate` settle brightens the sand (as §6.1's lock). The frequency readout (§6.3) counts through the glide (§6.18) and the marginal waveform (§6.4) cross-draws. If the visitor scrolls fast, the tent compresses — chaos peaks lower (max `c` scales with dwell time in the interval, capped at 1, floored at 0.35) so a fast reader sees a shiver, not a storm.

**Choreography timeline** (relative to entering the interval). 0% scroll: outgoing figure locked, tremble on. 25%: tremble amplitude doubles, first particles leave their lines. 50%: full chaos (c = dwell-scaled peak); readout mid-count; waveform half-drawn. 75%: new nodal lines visibly attracting sand. 100%: lock — settle brightening, tremble re-arms at the new rung, bed title's sand-mask completes.

**State matrix.** *Rest:* figure locked at the owning bed's rung. *Gliding:* as above; the plate is never blank and never shows a half-printed caption — the inscription (§6.3) updates only at lock, so the page never claims a figure it is not showing. *Scrolled-past (upward):* the same glide runs in reverse to the previous rung — the garden retunes down as faithfully as up; there is no "already visited" shortcut state. *Jump scroll (anchor / find-in-page / restoration):* if the scroll position teleports across ≥2 rungs, no glide: the target rung's figure is already formed when rendering resumes (the loop sets c = 0 and snaps particles to the target nodal sampling if the jump exceeds one interval). *Disabled:* static figures per bed (tablet/mobile in-place plates) change by cut. *Touch:* identical — scrub is scroll-driven, not gesture-driven.

**Content-merge.** The glide's endpoints are the beds' own figures; the inscription, waveform, and rail marker (§6.3, §6.4, §6.10) all retune together from the same ladder record, so the whole margin agrees with the plate at every scroll position. A bed whose figure fails to form shows the previous figure *with the previous inscription* — the page would rather be one bed behind than lie about a pitch.

**Breakpoints.** ≥1200px: pinned plate, tent width 60vh. 768–1199px: plate travels with the bed; the glide runs in place over the same tent relative to the bed's entry. <768px: tent width 40vh, chaos peak capped at 0.7 (a small screen of boiling sand reads as noise, not music), particle count per §6.1.

**Edge cases & failure modes.** Scrolling back up mid-glide: the tent is symmetric; c follows scroll position, not a timeline, so reversal is free and exact. Very long beds (text over cap): the bed owns the plate for its whole length; the glide only begins at the *next* bed's threshold — a long read never triggers a retune early. Low-power device: if frame time degrades, chaos jitter updates every 2nd frame (the figure still resolves on schedule). Content shorter than a viewport (tiny screens, huge text zoom): two beds may share the screen; the plate belongs to the bed whose title is nearest the viewport's upper third — a deterministic rule, stated here so two builders implement the same garden.

**Fallback & watchdog.** **Watchdog: 1200ms** after a lock point is crossed — if home-count for the incoming figure is <97%, particles snap to the incoming nodal sampling and the lock proceeds (the reader must never be left watching soup). If the loop dies entirely, the last formed figure stays and inscriptions stay matched to it.

**Reduced motion.** No glide, no chaos: crossing a bed threshold cuts the plate to the new bed's static figure. The inscription changes at the same moment. Nothing animates.

**Accessibility.** The retune is decorative physics over printed content; `aria-hidden` canvas, live text (inscription) updates are *not* in a live region (a screen reader must not be serenaded with hertz). Bed titles are real headings; the heading order is the document order regardless of which figure is showing.

**Performance & mobile variant.** Reuses §6.1's system — zero additional per-frame cost beyond the chaos blend. Mobile: peak chaos capped, jitter stride halved.

**Tokens.** `--ease-gliss`, `--gliss-tent: 60vh`, `--chaos-peak: 1`, `--chaos-amp: 2.4px`, `--lock-dur: 140ms`, `--lerp-heavy: 0.08`.

### 6.3 Printed (n, m) indices & the frequency readout

**What & why.** Beneath every figure, its actual Chladni indices and frequency are printed in the inscription register: `FIGURE (n, m) = (3, 2) · 164.81 Hz`. The readout is the theme's proof-of-work — the caption is a proof, not a caption — and it is also the page's progress indicator: pitch ascends bed by bed, so a reader who glances at the inscription always knows how deep in the garden they are. It merges with content because it is *about* the content at the level of mechanism: the numbers are the function arguments that drew the picture above them.

**Structure.** A `<p class="inscription">` under the plate (and under each in-place tablet/mobile plate), containing three spans: the figure's (n, m), the frequency, and the rung's name ("RUNG 3 OF 6 · THE EQUATION, HONESTLY"). All values are rendered server-side (or in the static HTML) from the ladder record (§6.17) for rung 0; JavaScript updates the spans at each lock (§6.2) — textContent swaps, never innerHTML. The frequency span's digits are the counters of §6.18 during a glide.

**Motion spec.** At lock: the (n, m) span cross-fades 120ms (opacity dip to 0.35 and back, `--ease-drift`) — a re-engraving, not a blink. During the glide, the frequency counts through the interval's pitch range (§6.18) and settles at the exact record value with the lock's `--ease-resonate` 140ms. The live-rung marker — a 6px bloom-scarlet dot before the rung name — appears only on the currently sounded rung (one of scarlet's three licensed appearances).

**Choreography timeline.** Glide 50%: frequency mid-count, dot still on the outgoing rung. Lock −140ms: count enters its settle. Lock: dot moves, (n, m) cross-fades. Lock +140ms: all values final and still.

**State matrix.** *Rest:* values of the owning bed, printed, still. *Gliding:* frequency counting; (n, m) still shows the outgoing figure (the page does not claim the new indices until the figure exists). *Scrolled-past:* values persist — scrolling back re-reads them. *Disabled (no JS):* each bed's in-place plate carries its own printed inscription; the pinned desktop plate's inscription shows rung 0 and the beds' own captions carry their indices (the static document is complete). *Touch:* identical.

**Content-merge.** The inscription is generated from the same record object the particle system reads (§6.17) — one source, so print and physics cannot drift apart. §10's gate includes a figure-truth audit: a script evaluates F at the printed (n, m) and compares the nodal sampling to the shipped static plates.

**Breakpoints.** ≥1200px: inscription centred under the pinned plate, 12.5px. 768–1199px: under each in-place plate. <768px: same, wrapping to two lines (indices line, frequency line) — never truncated, never smaller than 12.5px.

**Edge cases & failure modes.** A bed added without a ladder rung (unsounded bed, §4): its inscription reads `AT REST · THE GARDEN'S RESTING FIGURE (2, 1) · 110.00 Hz` — honest about showing the resting figure. If the record fails to load (it is inline; failure means a build error), the inscription prints the static HTML values and the particle system does not start — print first, physics second, always.

**Fallback & watchdog.** The inscription is plain text in the initial HTML for rung 0 and for every in-place plate; JS only updates it. No watchdog needed — text cannot strand. If a lock event is missed, §6.2's watchdog still fires the snap, and the inscription updates from the same handler.

**Reduced motion.** Values swap by cut at threshold crossing; no count, no cross-fade. The dot still marks the live rung (colour is not motion).

**Accessibility.** Real text, 12.5px minimum, ink on sand 10.9:1. The scarlet dot is decorative (`aria-hidden`); the rung name carries the information in words. Frequencies are written with a space and unit (`164.81 Hz`) so screen readers parse them cleanly.

**Performance & mobile variant.** Text swaps only; zero layout thrash (the inscription box has a fixed two-line height reserve on mobile so locks never shift the bed below).

**Tokens.** `--ink`, `--bloom`, `--inscription-size: 12.5px`, `--inscription-tracking: 0.14em`, `--ease-drift`, `--lock-dur: 140ms`.

### 6.4 Marginal waveforms stepping up

**What & why.** In the score margin, an SVG sine waveform draws in sync with the plate, its frequency visibly stepping up bed by bed — 2 cycles at the hero, then 3, 5, 8 — the Fibonacci climb the original entry specifies. The margin keeps the score: progress you can read as pitch. It merges with content because the waveform is not a generic squiggle — its cycle count is the rung's `cycles` field in the record (§6.17), drawn at the moment that rung sounds, and its phase is locked to the plate's glide.

**Structure.** One inline SVG per margin segment (desktop: a single tall SVG spanning the sounded length, redrawn per rung; the path is generated from the record's cycle count over a fixed 720° phase window). Path draw via `stroke-dasharray` driven by the shared loop's registered *draw* value (0 → 1 across the glide). A faint full path (12% ink) is always printed beneath — the undrawn state still shows the whole wave, pale, so the margin is never empty.

**Motion spec.** Draw duration = the glide's felt 800ms (`--ease-gliss`), synchronised with §6.2's tent: draw progress = 1 − c on the interval's second half. At lock, the wave is fully drawn in ink; the previous rung's wave fades to 18% over 300ms as the new one completes (the margin holds a fading memory of the last pitch, one rung deep only). Amplitude: 14px desktop, 9px mobile (where drawn at all — see Breakpoints).

**Choreography timeline.** Interval 50%: old wave at 18%, new wave at ~50% draw. 75%: new wave ~85%. Lock: new wave full ink; old wave removed from the DOM after its fade (never more than two wave paths alive).

**State matrix.** *Rest:* current rung's wave full ink; previous at 18% for one bed, then gone. *Gliding:* as above. *Scrolled-past (up):* the process reverses — the wave redraws downward in cycles as rungs descend. *Disabled:* all waves printed full ink at 40% (the static margin shows the whole climb at once — a fair printed score). *Touch:* same, where the margin exists.

**Content-merge.** Cycle counts come from the record; the wave's bed-side tick aligns exactly with the bed title it scores. A wave that disagreed with the plate's figure would be a lie in the margin — the gate (§10) checks cycle counts against the record.

**Breakpoints.** ≥1200px: full margin treatment. 768–1199px: the margin narrows to 64px; waves draw at 9px amplitude, ticks remain. <768px: **the margin is cut** — no waveforms; progress is carried by the inscription (§6.3) and the rail's rung name (§6.10). This is the theme's first mobile cut and it is specified here so no builder improvises a cramped margin.

**Edge cases & failure modes.** Long pages: the SVG is segmented per bed (one path group per rung) so no single path exceeds ~40 points per cycle × 8 cycles. If path generation fails for a rung, that segment prints its pale full path (the fallback layer) and the draw simply does not run.

**Fallback & watchdog.** The pale full path is the fallback and is always in the DOM; the draw is a mask over it. **Watchdog: 1200ms** (shared with §6.2's lock) — if draw progress has not reached 1 by lock + 1200ms, dash values snap to full.

**Reduced motion.** All waves printed full ink at 40%; no draw, no fade. The climb is still readable as a static score.

**Accessibility.** Decorative (`aria-hidden`); the information (which rung, what frequency) is text in §6.3. No focusable elements in the margin.

**Performance & mobile variant.** Path redraw only during glides; at rest the loop does not touch the margin. Mobile: cut entirely (above).

**Tokens.** `--ink`, `--wave-amp: 14px`, `--wave-draw-dur: 800ms`, `--ease-gliss`, `--margin-w: 120px`.

---

### 6.5 Resting-tone tremble

**What & why.** At rest, the formed figure's sand trembles faintly — sub-pixel jitter at the section's frequency character — because the plate is never fully silent. Stillness here still hums; the garden idles at pitch. This is one of the theme's two licensed ambient loops (§5), and its restraint is the point: a visitor should *sense* the tremble before they see it, the way you sense a fridge's hum. It merges with content because the tremble belongs to the figure the bed is about — each rung trembles at its own character: higher rungs jitter finer and faster.

**Structure.** A tremble amplitude value `t` (px) and a per-particle phase, applied inside §6.1's particle loop as a sinusoidal offset perpendicular to each particle's nodal line: offset = t · sin(time · ω + phase), with ω mapped from the rung's frequency (ω = Hz / 55 rad/s, so rung 0 ≈ 2.0 rad/s, rung 5 ≈ 4.8 rad/s — visible character, not literal audio rate). Amplitude: 0.35px desktop — deliberately below the threshold of conscious noticing at reading distance.

**Motion spec.** Continuous while the plate is formed and within one viewport of the reader. Ramp-in 600ms (`--ease-drift`) after each lock; ramp-out 300ms when a glide begins (the glide's chaos takes over). Fine sand also migrates almost imperceptibly toward the nearest nodal line during tremble (the figure slowly *sharpens* at rest — stride 0.02px/frame toward home), so a figure left alone for a minute is crisper than the moment it locked.

**Choreography timeline.** Lock +0ms: tremble at 0. Lock +600ms: full 0.35px. Glide start: tremble → 0 over 300ms as chaos amplitude rises. Tab hidden / plate off-screen by >1 viewport: tremble suspended (loop may sleep).

**State matrix.** *Rest:* trembling. *Hover (plate):* §6.6 takes over locally; global tremble continues. *Scrolled-past:* the plate always shows the current bed's figure, so tremble is always the current rung's. *Disabled:* no tremble — static figure. *Touch:* identical (time-triggered).

**Content-merge.** The tremble is a property of the sounded figure, not a page-wide effect: text never trembles (Type law 5), margins never tremble; only sand. When the garden is at rest in the footer (§6.15), the printed plate does not tremble — print is print.

**Breakpoints.** ≥1200px: 0.35px. 768–1199px: 0.3px. <768px: 0.25px and ω scaled ×0.8 — a small screen at arm's length shows jitter more readily, so the garden quiets itself.

**Edge cases & failure modes.** Vestibular sensitivity beyond the media query: an in-page "Still the garden" toggle (§11) sets a `data-still` attribute that kills tremble and ripples for the session. Battery saver / `prefers-reduced-data`: tremble is a candidate cut (§14) — the loop's idle wake is the first thing sacrificed. If frame rate drops, tremble updates every 2nd frame rather than degrading the glide.

**Fallback & watchdog.** None required — tremble is an offset on an already-formed figure; if the loop stops, the figure simply rests, which is a legal state of the garden. No watchdog: nothing can strand.

**Reduced motion.** **Off.** The formed figure is still. This is the single most important reduced-motion ruling in the theme: a trembling page is exactly what the preference exists to prevent.

**Accessibility.** Sub-pixel, sand-only, and off under reduced motion; the "Still the garden" toggle is a real button with a visible focus ring (§11), placed in the navigation (§6.10), labelled in words.

**Performance & mobile variant.** Tremble is the loop's only idle cost: ~0.3ms/frame at 900 particles. It suspends off-screen and on hidden tabs. Mobile: reduced amplitude and rate (above).

**Tokens.** `--tremble-amp: 0.35px`, `--tremble-ramp: 600ms`, `--ease-drift`, `--ink` (none — sand only).

### 6.6 Fingertip-on-the-rim hover

**What & why.** Hovering an element — a bed card, a programme row, a specimen frame — is a fingertip on the rim of the plate: the pattern near that element trembles and locally re-forms. A small region of sand around the element's corresponding figure stirs, re-settles along its nodal lines, and calms. Touch is acoustic here; the reader's hand is on the instrument. It merges with content because the region that stirs is the figure of the very rung the hovered element belongs to — hovering a programme row for the 196 Hz sitting stirs the (4, 2) figure, not a generic sparkle.

**Structure.** Each hoverable element carries `data-rung`. On the pinned plate (desktop), a *local disturbance* is registered in the loop: a centre point (the plate region mapped from the element's rung — each rung's disturbance centre is a fixed, pleasing point of its figure, stored in the record) and a radius (90px). Particles inside the radius get a temporary jitter amplitude of 1.2px and a re-settle stride; outside, the resting tremble continues. On tablet/mobile (in-place plates), the disturbance applies to that bed's own plate if visible; if the bed's plate is not on screen, the hover falls back to the element's own micro-response (frame glint, §6.9; row underline, §6.12) — the garden never animates something the visitor cannot see.

**Motion spec.** Stir-in 180ms (`--ease-drift`) to full local amplitude; sustain while hovered (re-settle continuously, so the local figure is perpetually *almost* formed — alive under the finger); release: 500ms decay back to resting tremble (`--ease-resonate` — the rim rings a little after the finger lifts). Keyboard focus triggers the identical stir (focus parity is mandatory, not a port).

**Choreography timeline.** Hover 0ms: amplitude ramps. 180ms: full local stir. Sustain: particles cycle stir → re-settle → stir. Leave +0ms: decay begins. +500ms: resting tremble only.

**State matrix.** *Rest:* resting tremble. *Hover:* local stir as above. *Focus:* identical to hover, plus the element's own focus ring (§11) — the ring is bronze on sand, never scarlet. *Active (press):* the stir sharpens for 120ms (amplitude 1.6px) — the fingertip presses — then §6.7 fires on click. *Scrolled-past:* disturbances are cancelled when the plate retunes; a hover during a glide adds nothing (the glide owns the sand). *Disabled (touch):* no hover exists; tap = §6.7 directly. Touch users lose nothing — the stir is a garnish on the click, never the only feedback. *Disabled (element):* no stir; disabled elements are silent in every sense (§11).

**Content-merge.** The disturbance centres live in the ladder record beside each rung's indices — data, not decoration. Hovering teaches the visitor the page's physics: everything here answers touch with resonance.

**Breakpoints.** ≥1200px: pinned-plate disturbance as specified. 768–1199px: in-place plate disturbance when visible. <768px: element-local micro-response only (glint/underline) — a phone's plate is usually above the text, and stirring an off-screen plate is waste.

**Edge cases & failure modes.** Rapid hover sweeping across many rows: disturbances are single-instance — a new hover moves the one disturbance (centre lerps at 0.12 between rung centres), so the sand shows one travelling stir, never a storm. Hover during formation (§6.1): formation wins; stir arms only after lock. Pointer leaves the window mid-stir: decay runs; no stuck state (the loop's target returns to rest unconditionally).

**Fallback & watchdog.** The stir is an amplitude target in the loop; if the loop is dead, hover still produces the element's CSS micro-responses (underline, glint) which are pure CSS. **Watchdog:** none needed — a stuck amplitude would require a stuck loop, and §6.2's snap governs the loop's health; additionally the disturbance target hard-resets to rest on any `pointerleave` of the document.

**Reduced motion.** No stir. Hover produces the static micro-responses only (underline drawn instantly, glint at full). The rim is touched and nothing moves — correct for the preference.

**Accessibility.** Focus parity (above); the stir is never the sole indicator of anything — hovered rows also underline, cards also lift their glint. Touch targets unaffected. The effect is `aria-hidden` canvas physics; nothing is announced.

**Performance & mobile variant.** Local radius limits cost: only particles within 90px of the centre update their jitter per frame (~120 particles worst case). Mobile: CSS micro-responses only (above) — zero canvas cost.

**Tokens.** `--stir-amp: 1.2px`, `--stir-radius: 90px`, `--stir-in: 180ms`, `--stir-out: 500ms`, `--ease-drift`, `--ease-resonate`.

### 6.7 Click-to-sound (the bloom)

**What & why.** Clicking a sounded element — a card, a row, a rung in the rail — sounds its tone visually: a Chladni figure flashes into form around it in a ~600ms bloom, at that element's own (n, m), in bloom scarlet's single licensed flash. Every element has a pitch; clicking is playing the page. It merges with content because the bloom is the element's own rung made momentarily visible at the element itself — a programme row blooms the (4, 2) figure of the sitting it names — and because scarlet is rationed (§2), a bloom is an event, not a habit.

**Structure.** A small inline SVG (120×120 desktop) generated from the same nodal function — the nodal set of the element's (n, m) extracted as contour segments at build time (or first use) and cached per rung (six SVGs maximum, one per rung). The SVG is positioned centred on the clicked element, clipped to a circle (the bloom is a flower, round), pointer-events none, z-index above the element but below the navigation. Its strokes draw in (dashoffset) while the whole bloom scales 0.82 → 1 and fades at the end of its life.

**Motion spec.** Total 600ms (`--ease-bloom`). 0–360ms: strokes draw, scale rises, scarlet at full strength. 360–600ms: the figure holds formed for a beat, then fades to 0 (opacity, 240ms) and the node is removed. The pinned plate simultaneously gives a sympathetic stir (§6.6's disturbance at the rung's centre, 400ms) — the instrument answers its miniature. A second click on any element within the bloom's life replaces it (blooms are single-instance, like disturbances).

**Choreography timeline.** Click 0ms: bloom node inserted, plate stir begins. 120ms: first nodal strokes visible. 360ms: figure complete, scale 1. 480ms: fade begins. 600ms: node removed; plate stir decayed.

**State matrix.** *Rest:* no bloom. *Active (the click itself):* bloom as above; the element's own pressed state (§11) runs concurrently. *Focus + Enter:* blooms identically — keyboard visitors play the page too. *Scrolled-past:* blooms are viewport-local; an element scrolled off mid-bloom has its node removed by the loop's housekeeping. *Disabled element:* no bloom — silence. *Touch:* tap blooms (and performs the element's action, if any — bloom never swallows the click; it is an overlay with pointer-events none).

**Content-merge.** The bloom's figure is computed from the record for the element's rung — clicking around the page is a way of *reading* the ladder with your hands. In the programme table (§6.12), blooming a row is how a visitor previews a sitting's pitch before booking it in the form (§6.13), whose rung options are the same six.

**Breakpoints.** ≥1200px: bloom 120px. 768–1199px: 104px. <768px: 88px, and the plate's sympathetic stir is skipped (the plate is usually off-screen).

**Edge cases & failure modes.** Clicking an unsounded element (an unsounded bed's card, a footer link): no bloom — instead the element's plain pressed state. The garden does not pretend everything has a pitch. Rapid clicking: single-instance replacement prevents pile-up; the SVG cache prevents regeneration cost. If SVG generation fails for a rung, that rung's elements simply do not bloom (their other feedback is intact) and the failure is silent — a missing flower is not an error state.

**Fallback & watchdog.** Blooms are pure enhancement; the click's real action (navigation, selection) never depends on them. **Watchdog: 900ms** — a housekeeping sweep removes any bloom node older than 900ms, so a interrupted animation can never leave a scarlet figure parked on the page.

**Reduced motion.** No bloom. The click's feedback is the element's pressed state and, in the rail, the marker's instant move. Scarlet still appears (it is a colour, not a motion) on the confirmation seal (§6.13).

**Accessibility.** The bloom is decorative and `aria-hidden`; it never carries state (a selected rung is indicated by the rail marker and `aria-current`, not by having bloomed). Enter/Space parity as above. Scarlet-on-sand at 5.4:1 applies to the marker word only — the bloom itself is a graphic.

**Performance & mobile variant.** Six cached SVGs, ≤9KB total; the bloom is one node, animated by the shared loop (scale/opacity only — compositor-friendly). Mobile: smaller, no plate stir.

**Tokens.** `--bloom`, `--bloom-dur: 600ms`, `--ease-bloom`, `--bloom-size: 120px`.

### 6.8 Water-ripple margin rings

**What & why.** Slow ripple rings breathe in the margins — expanding, fading, on a ~6s cycle, out of phase with each other. The conservatory's second instrument: water answering bronze, ambience with a source. The rings live in the margin soil beside the beds, rising from two fixed "basin points" per bed (the spots where, in the fiction, water stands in the conservatory), and they are the theme's second and last licensed ambient loop. They merge with content by placement and restraint: they are *in the margin*, keeping time beside the text, never under it, never competing with the plate.

**Structure.** Per bed, one SVG (margin-width, bed-height) with two `<circle>` ring pairs at the bed's basin points. Each ring: radius animates 4px → 54px while opacity falls 0.5 → 0, `--ease-ripple`, 6000ms per ring, the pair offset by 3000ms, the two basins offset by 1500ms from each other — four phases per bed, never synchronised. Rings are clipped to the margin; on beds where the margin is cut (§6.4 breakpoints), rings are cut too.

**Motion spec.** Continuous while the bed is within one viewport. A ring's stroke is `--glass` at 1.5px — water over soil, greenish, quiet. When a bed sounds (lock), its rings restart their phase from the lock moment — the water answers the tone, once, then resumes its own time.

**Choreography timeline.** Per ring: 0ms radius 4px, opacity 0.5 · 3000ms radius 30px, opacity 0.22 · 6000ms radius 54px, opacity 0, loop. Basin B offset +1500ms; second ring of each pair +3000ms.

**State matrix.** *Rest:* breathing. *Gliding (bed change):* rings continue — water does not retune; only the phase-reset at lock marks the event. *Scrolled-past:* rings suspend when their bed leaves the one-viewport band. *Disabled:* printed as two faint static circles per basin (the margin shows where the water stands). *Touch:* identical (time-driven).

**Content-merge.** Basin points are placed at the bed's two quietest margin spots — beside the caption block and beside the bed's final paragraph — recorded per bed in the build, not randomised. The rings' green ties the margin to the specimen frames' glass (§6.9): one material, two states (still glass, moving water).

**Breakpoints.** ≥1200px: full treatment. 768–1199px: one basin per bed, radius to 38px. <768px: **cut** (with the margin itself).

**Edge cases & failure modes.** If a bed is very short, rings overlap the next bed's basin — the per-bed SVG is clipped to its own bed box, so overlap is impossible by construction. Under `prefers-reduced-data` or battery saver, rings are the second cut (§14) after tremble.

**Fallback & watchdog.** Static circles are the fallback layer, printed in the SVG from the start; animation only modulates radius/opacity of additional ring nodes. No watchdog — a frozen ring is a printed circle, a legal state.

**Reduced motion.** **Off.** Static basin circles only, at 18% — the water is still, and the margin says so honestly.

**Accessibility.** Fully decorative, `aria-hidden`, no information carried. Motion off under the preference (above) and under the "Still the garden" toggle (§6.5).

**Performance & mobile variant.** Four animated circles per visible bed, transform/opacity only. Mobile: cut.

**Tokens.** `--glass`, `--ripple-cycle: 6000ms`, `--ripple-max: 54px`, `--ease-ripple`.

### 6.9 Glass-green specimen frames

**What & why.** Photographs — the conservatory's exhibits: a real plate in a real museum, a bowl, a hand on a rim — scale inside glass-green frames like specimens brought into focus, each captioned with the frequency at which its figure forms. Photographs are exhibits here, labelled by the same system as everything else: the caption is not "Figure 3" but "Forms at 196.00 Hz · (4, 2)". It merges with content because the caption ties the photograph into the ladder — the visitor learns which rung the pictured instrument sounds, and clicking the frame sounds it (§6.7).

**Structure.** A `<figure>` with a 10px `--glass` frame (outer), a 2px `--glass-deep` inner keyline (the glass's edge), and the image inside an overflow-hidden well. A glint — a linear-gradient sheen at 18% white — sits above the image, translating with parallax depth 1.06× (§5). The caption below carries the inscription-register line (frequency + indices) and a caption-register sentence. Frames are rectangular with square corners: conservatory glass is not rounded.

**Motion spec.** On scroll into view: the image scales 1.06 → 1.0 over 900ms (`--ease-bloom`) — a specimen focusing — while the glint sweeps once (translateX −30% → 130%, 900ms, same easing, delayed 120ms). The frame itself never moves. Re-entry does not replay (once per session per frame; the specimen stays in focus once focused).

**Choreography timeline.** Entry 0ms: scale begins. 120ms: glint sweep begins. 900ms: scale settles, glint gone. Caption is printed throughout (captions never animate).

**State matrix.** *Rest:* focused specimen, glint at rest position (off-frame). *Hover:* glint returns part-way (to 40%, 300ms) and §6.6's stir arms if the frame's rung has a visible plate — the glass answers the hand. *Focus:* same as hover (the frame is a link/button only when it sounds a rung; purely illustrative frames are not focusable). *Active:* §6.7 bloom at the frame's centre. *Scrolled-past:* stays focused. *Disabled:* n/a (frames are not controls unless they sound).

**Content-merge.** Every specimen must earn its caption: a photograph whose subject has no honest frequency (a portrait of the founder, a stock hallway) does not belong in a specimen frame — it belongs in a plain sand card (§6.11) or nowhere. The frame is a claim: *this thing sounds at this pitch.*

**Breakpoints.** ≥1200px: frames up to 520px wide, in the bed's field. 768–1199px: full bed width. <768px: full width, glint sweep shortened to 600ms, parallax off (glint static at rest).

**Edge cases & failure modes.** Missing image: the frame prints its caption and a raked-sand well with the inscription `SPECIMEN NOT YET PLATED` — an honest empty case, never a broken-image icon. Slow image: the frame and caption render at layout time (aspect-ratio reserved); the image fades in on load (opacity, 300ms) *before* its focus scale runs — the scale waits for the load event, with a 2500ms cap after which the frame is simply shown.

**Fallback & watchdog.** No JS: the image sits at scale 1.0, glint absent — a framed photograph, complete. **Watchdog: 2500ms** on the load-wait (above). The focus animation is an enhancement layered on a finished exhibit.

**Reduced motion.** No scale, no sweep: the specimen is in focus from the start, glint absent.

**Accessibility.** Real `alt` text describing the exhibit; the caption's frequency line is text. Focusable frames (sounding ones) get the bronze focus ring and a label like "Sound the specimen's tone, 196 hertz". Contrast: captions ink on sand 10.9:1.

**Performance & mobile variant.** Images are the page's heavy assets — §14 budgets them (≤120KB each, WebP/AVIF, `loading="lazy"` below the hero). The scale transform is compositor-only. Mobile: no parallax, shorter sweep.

**Tokens.** `--glass`, `--glass-deep`, `--sand`, `--focus-dur: 900ms`, `--ease-bloom`, `--frame-w: 10px`.

---

### 6.10 The pinned plate stage & ladder rail (navigation)

**What & why.** The navigation of a conservatory is a plan of the garden, and the garden's plan is its ladder. The header carries the site's name and three plain links (Programme, Visit, About — sand cards' worth of chrome, §11); the real navigation is the **ladder rail**: a vertical rail in the score margin listing the six rungs by name and frequency, with a marker that travels to the live rung as the visitor scrolls. Beside it, on desktop, the plate stage itself — the pinned bronze plate (§4) with its rim, stand shadow, and inscription (§6.3) — is specified here as one element, because stage and rail are one instrument: the rail says where you are on the ladder; the plate sounds it. It merges with content because the rail *is* the table of contents, written in the content's own units (rungs and hertz, not page numbers).

**Structure.** Header: a sand bar, Fraunces wordmark left, links right, the "Still the garden" toggle (§6.5) as a labelled button at the far right. Rail: a `<nav aria-label="The ladder">` — an ordered list of six rung links, each showing rung name (Space Grotesk 500, 13px) and frequency (inscription register). The marker is a 22px bronze rule with a scarlet dot (§6.3's licensed dot, shared with the inscription) that travels the rail's height via the shared loop (lerp 0.12, scrubbed to the sounded rung's position). The stage: a sticky container (top: 50% translate on desktop) holding rim (12px `--bronze` with a `--bronze-lit` top edge — one light source, from above), the canvas (§6.1), the static SVG fallback, and the inscription.

**Motion spec.** Marker travel: continuous lerp toward the live rung's offset; at a lock it arrives with the figure (same 140ms settle window). Rail link hover: the rung name deepens to ink and its frequency underlines (240ms draw). Clicking a rung: smooth scroll to its bed; on arrival the bed sounds (§6.2's glide runs if the jump crosses one interval; §6.2's jump rule applies beyond that). Header: no motion at all — the garden's roof does not move.

**Choreography timeline.** Scroll: marker lerps continuously. Lock: marker within 2px of the rung row by lock +140ms. Rung click: scroll (native smooth, ~700ms typical) → threshold crossings fire glides per §6.2 → arrival lock.

**State matrix.** *Rest:* marker on the live rung; that rung's link carries `aria-current="true"` and its name in ink (others in `--ink` at 72%). *Hover/focus:* as above; focus ring bronze, 2px, offset 2px. *Active:* pressed rung name shifts 1px down (a key press). *Scrolled-past:* the rail is sticky in the margin for the whole sounded length; after the last rung it rests on rung 5 until the footer, where the footer plate (§6.15) takes over the eye. *Disabled:* rung links are never disabled. *Touch:* the rail collapses (see Breakpoints) — no hover states exist; tap targets are the rung rows themselves.

**Content-merge.** The rail's entries are generated from the ladder record (§6.17) — names and frequencies cannot disagree with the plates they navigate to. A page with unsounded beds lists those beds below the ladder under a hairline, labelled `AT REST` — the plan shows the whole garden, sounded and resting.

**Breakpoints.** ≥1200px: rail in the 120px margin (rung names may wrap to two lines; frequencies never wrap). 768–1199px: rail becomes a horizontal strip above the first bed (six rung chips, marker = chip underline), and the plate travels in-place per bed. <768px: rail is a `<details>`-style "The ladder" disclosure at the top (native, no JS needed) listing the rungs as links; the marker concept survives as `aria-current` styling on the open list. The header compresses to wordmark + toggle + a menu disclosure with the three links.

**Edge cases & failure modes.** Long rung names: the record's names are capped at 24 characters by §12's copy rules, so the rail cannot overflow its margin; a name at cap wraps to two lines and the marker aligns to the row's first line. Scroll restoration mid-page: marker and figure both initialise to the restored rung (§6.2 jump rule) — the garden wakes up in tune. If the record is missing a rung (build error), the rail renders from the static HTML (all six rows are in the initial markup; JS only moves the marker).

**Fallback & watchdog.** No JS: rail is a list of anchor links; marker absent; every bed reachable. The stage shows rung 0's static figure. **Watchdog:** none for the rail (links cannot strand); the stage inherits §6.1/§6.2's watchdogs.

**Reduced motion.** Marker jumps by cut at locks; rung clicks scroll instantly (`scroll-behavior` overridden by the media query in CSS); no other change.

**Accessibility.** Landmarks: one `<header>`, one ladder `<nav>` with a real label, `aria-current` on the live rung. Toggle button labelled "Still the garden" with `aria-pressed`. All rail targets ≥44px tall on touch layouts. Contrast: rung names at 72% ink on sand = 6.1:1 (passes AA for 13px semibold); live rung 10.9:1.

**Performance & mobile variant.** The rail is six list items; the marker is one transformed element. Mobile replaces the sticky stage with in-place plates (§4), so no sticky cost on scroll.

**Tokens.** `--bronze`, `--bronze-lit`, `--bloom`, `--ink`, `--margin-w: 120px`, `--rail-marker-w: 22px`, `--ease-drift`.

### 6.11 Bed cards

**What & why.** Within a bed, sub-content — a workshop, a bowl in the collection, a lesson in the curriculum — is carried on bed cards: sand-paper cards edged in glass green, each with a title, a short body, and, if the item sounds, its rung's inscription line. Cards are how the garden holds more than one plant per bed without breaking the one-figure-per-bed rule: the bed sounds one figure; its cards are labelled specimens within it. The card merges with content because its footer line is data — the item's own frequency or an honest `AT REST` — never a decorative tag.

**Structure.** `<article class="bed-card">`: a `--sand-lit` face, 1px `--glass` edge with a 6px glass-green top rule (the bed's edging), Fraunces Display-3 title, body at 15px/1.58, and a footer row: inscription-register rung line left, and a text link ("Sound it", "Read the lesson") right. Cards sit in a grid of up to three (§4). A card that sounds carries `data-rung` and is hoverable/clickable per §6.6/§6.7; a resting card is inert paper.

**Motion spec.** Entry: cards rise through the bed's sand-mask with their bed (500ms `--ease-drift`, staggered 90ms across the row — the only stagger besides the hero's). Hover (sounding cards): the top rule brightens to `--glass-deep`→`--bloom`? No — scarlet is rationed; the top rule deepens to `--glass-deep` (300ms) and §6.6's stir arms. The card itself does not lift or tilt: paper in a bed does not float. The link underline draws 240ms.

**Choreography timeline.** Bed entry: card 1 mask at 0ms, card 2 at +90ms, card 3 at +180ms; all settled by +680ms. Hover: rule deepens over 300ms; stir per §6.6. Click: §6.7 bloom centred on the card.

**State matrix.** *Rest:* printed card. *Hover:* rule deepens; stir. *Focus:* bronze ring on the card's link (the card itself is not focusable; its link is). *Active:* link pressed state (§11). *Scrolled-past:* masks never replay within a session. *Disabled:* a card for an unavailable item (a sold-out workshop) prints its footer as `SOUNDED OUT — NO SEATS` in inscription register and its link is removed, not greyed into illegibility — the text stays ink, the *link* goes. *Touch:* no hover; tap on the link acts; tap on a sounding card blooms (§6.7) without navigating (the link is the navigation).

**Content-merge.** Card content is the site's real sub-content; the rung line is the item's true place in the ladder or an honest rest. A card may not carry a frequency its item does not have — §10's audit samples card inscriptions against the record and the items' data.

**Breakpoints.** ≥1200px: 3-across grid, 32px gaps. 768–1199px: 2-across. <768px: 1-across, top rule 5px, body 15px kept (reading size never shrinks).

**Edge cases & failure modes.** A bed with one card: the grid left-aligns at card width (no stretching to fill — a single plant is not a row). A bed with seven items: four become cards, three become programme rows (§6.12) — the density rule (§4) routes overflow to the table, it does not cram the bed. Long titles: capped by §12 (≤7 words); a title at cap wraps to two lines and the row's cards equalise height by grid, footers aligned.

**Fallback & watchdog.** Cards are printed content; the mask is a `--sand` overlay removed by the loop. **Watchdog: 2000ms** after bed entry — any mask still covering a card is removed outright. No JS: no masks exist (they are JS-inserted).

**Reduced motion.** No masks, no stagger: cards are simply present. Hover deepening still applies (colour change, instant).

**Accessibility.** Semantic `<article>`s with real headings (h3 under the bed's h2). Links are descriptive ("Sound the handpan workshop — 196 hertz" as the accessible name where the visible text is shorter). Footer inscription 12.5px ink on sand-lit 12.4:1.

**Performance & mobile variant.** Cards are DOM + CSS; masks are one overlay per card, removed after entry. Mobile: no masks (entry is instant below 768px — small screens get the garden without its theatre).

**Tokens.** `--sand-lit`, `--glass`, `--glass-deep`, `--ink`, `--mask-dur: 500ms`, `--card-stagger: 90ms`, `--ease-drift`.

### 6.12 The programme table (the season's soundings)

**What & why.** The garden's middle is a table: the season's programme — sittings, workshops, demonstrations — each row a date, a title, the rung it sounds (frequency + indices), and the seats remaining. This is where the theme proves it can do ordinary information work without breaking character: a table that is also a ladder. Rows merge with content doubly — their rung column is live (hovering stirs that rung's figure, §6.6; clicking sounds it, §6.7) and their seats figure is a true count that the booking form (§6.13) decrements in the record, so the table and the form can never disagree.

**Structure.** A semantic `<table>` on a `--sand-lit` leaf: caption ("The season's soundings"), header row (Date · Sitting · Sounds at · Seats), up to 12 rows per §4. The "Sounds at" cell carries the inscription-register frequency and (n, m). Rows are `data-rung`-carrying; the seats cell is data register. A totals footer row prints the season's sums (sittings count, total seats) computed from the rows — printed in the HTML, updated by JS only when a booking changes them (§6.13). The header row pins within the bed on scroll (`position: sticky` inside the bed's scroll context on desktop).

**Motion spec.** Row entry: rows print with the bed (no per-row animation — a table is read, not performed). Hover: row's sand deepens to `--sand-deep` at 40% (200ms) + §6.6 stir on the plate + the rung cell's frequency underlines. Seats counter, when changed by a booking, settles via §6.18 (count, 600ms, `--ease-resonate`). Nothing else in the table moves: tables are the garden's still water.

**Choreography timeline.** Bed entry: table present. Booking elsewhere on the page (§6.13 success): the affected row's seats count settles within the same second; if the row is off-screen, the number is simply correct when reached (no deferred theatrics).

**State matrix.** *Rest:* printed table. *Hover/focus:* as above; focus lands on the row's booking link (each row has one: "Book" in the final cell, or the row's title link — one focusable per row, never the row itself). *Active:* link press. *Scrolled-past:* header unpins at the bed's end. *Disabled:* a full sitting's row prints `FULL` in the seats cell (inscription register, ink) and its Book link is removed (as §6.11's rule). *Touch:* no hover; the rung cell is tappable to bloom (§6.7) — target ≥44px via cell padding.

**Content-merge.** Every row is a real sitting with a real rung from the record; the seats figures are the same numbers the form decrements (§6.17 is the single source for both). A programme with no rungs (a season of silent events) is not a programme for this theme — see §1's when-not-to-use.

**Breakpoints.** ≥1200px: full four-column table. 768–1199px: the (n, m) folds into the frequency cell (two-line cell). <768px: the table becomes a list of row-cards (each row a §6.11-style card with the same data, same order) — a *transformation of presentation, not of content*: every value present, identically worded. Builders must not hide the seats column on mobile; gardeners book from phones.

**Edge cases & failure modes.** More than 12 sittings: paginate by month with plain links (§11 pagination), each page a full table — never an infinite scroll (a season is finite and printed). Zero sittings: the empty state (§11) prints `THE GARDEN IS BETWEEN SEASONS` with the next season's first date if known. Seats reaching zero mid-session: the row updates to FULL and its link is removed on next render; a visitor mid-form for that sitting gets §6.13's honest error, not a silent failure.

**Fallback & watchdog.** The table is static HTML with true figures; JS only enhances hover/click and updates counts after bookings. No watchdog — nothing is hidden. If the booking update fails (network), the table keeps the pre-booking figure and the form says so (§6.13) — the page never prints a seat count it does not believe.

**Reduced motion.** All hover colour changes instant; seats swap by cut. The table is otherwise unchanged — it was already still.

**Accessibility.** Real `<table>` semantics with `<th scope>`, a caption, and no layout tables anywhere. The rung cell's frequency is text. Book links have unique accessible names ("Book the dawn sitting, 14 June"). Contrast: all cells ink on sand-lit 12.4:1; the FULL marker ink, not scarlet (rationing + colour-independence).

**Performance & mobile variant.** ≤12 rows; zero per-frame cost at rest. Mobile list transformation is CSS + the same DOM (no duplicated markup — `display` restructuring via grid on the table elements, or a build-time list rendering from the same data; either way one source).

**Tokens.** `--sand-lit`, `--sand-deep`, `--ink`, `--glass`, `--row-hover-dur: 200ms`, `--ease-resonate`.

### 6.13 Sound your visit (the booking form)

**What & why.** The conversion section is a bed, and its form is the garden's one act of hospitality: the visitor chooses a sitting from the programme, chooses **the pitch of their visit** — any rung of the ladder — and the plate sounds *their* figure as the confirmation. The form merges with content at the deepest level the theme allows: its confirmation is not a tick icon but a computed Chladni figure at the visitor's chosen (n, m), printed on a confirmation plate with the booking's real reference, and its success decrements the programme table's seats (§6.12) from the same record. A form that books you into a garden should hand you a flower; here the flower is geometry.

**Structure.** A `<form>` on a `--sand-lit` leaf in the final sounded bed: fields — sitting (a `<select>` generated from the programme's non-full sittings), your pitch (a radio group of the six rungs, each labelled with name + frequency + indices; default = the sitting's own rung), name, email, seats (number, 1–6). Submit button: bronze plate-key (§11) labelled "Sound my visit". On success the form is replaced (in place, same leaf) by the confirmation plate: a static SVG of the chosen rung's figure (generated exactly as §6.7's blooms, but printed, permanent), the inscription of that rung, the booking reference (format `CG-` + the sitting's date + a sequence number from the record), the sitting's details restated, and one line in the garden's voice (§12). The pinned plate simultaneously forms the chosen figure (§6.2's snap rule if the rung differs from the current bed's).

**Motion spec.** Field focus: the field's label warms to `--bronze-deep` and a 2px bronze underline draws under the field (240ms, `--ease-drift`) — a fingertip near the rim, not in it. Rung radio selection: §6.7's bloom fires at the radio's label (the visitor hears their choice with their eyes before committing). Submit: the button presses (120ms), then a 500ms "sounding" state — the button's label becomes "Sounding…" and the plate glissandos to the chosen rung if needed — then the confirmation plate settles in (opacity/translate, 400ms, `--ease-resonate`) with its figure already drawn (print first: the SVG fades in *drawn*, it does not draw itself — a confirmation is a document, not a performance). The seal: a scarlet wax-dot (§2's third licensed scarlet) presses onto the confirmation's corner at +200ms (scale 1.4 → 1, 180ms, `--ease-resonate`).

**Choreography timeline.** Submit 0ms: press. +120ms: sounding state; plate glide begins if rung differs. +500ms: form leaf cross-fades to confirmation. +700ms: seal presses. +900ms: programme table's seats settle (§6.18) if visible. Focus moves to the confirmation's heading (a real `<h2 tabindex="-1">`).

**State matrix.** *Rest:* printed form, all fields usable with JS disabled (the form posts to a real endpoint; the confirmation plate is the server-rendered result in the no-JS path). *Hover:* button rim lights (`--bronze-lit` top edge warms). *Focus:* per-field treatment above; focus ring bronze 2px offset 2px on every control. *Active/submitting:* button disabled *after* the press registers (never before — a disabled-looking button that swallows the first click is a defect), fields readonly during the 500ms sounding. *Error:* §11's error voice — the field's error text in `--bloom-deep`, the field marked with a bronze-deep left rule, focus sent to the first error on submit-fail, errors listed in a summary at the form's head (real links to fields). *Success:* confirmation plate as above; the form is gone (a "Book another sitting" link resets the bed). *Disabled (a sitting fills between page load and submit):* the error is specific and kind (§12): the sitting is named, the visitor's other choices are preserved, the nearest sitting with seats is offered as a one-click change. *Touch:* radios are 44px rows; the bloom on selection fires on tap.

**Content-merge.** Sittings come from the programme (§6.12), pitches from the ladder (§6.17), seats decrement the same record — three elements, one dataset, no possibility of the form selling a seat the table says is gone. The confirmation figure is computed from the chosen rung by the same function as every figure on the page.

**Breakpoints.** ≥1200px: form leaf 560px in the bed beside the pinned plate. 768–1199px: leaf full bed width under the in-place plate. <768px: single column; radio rows stack full-width; the confirmation plate's figure is 200px (from 260px).

**Edge cases & failure modes.** Network failure on submit: the form restores exactly as filled (no field is ever cleared by an error), with the summary "The garden gate didn't open — your details are still here. Try again." Double-submit: the sounding state disables re-entry; the booking reference's sequence makes duplicates detectable server-side. A rung radio group with a rung whose SVG generation failed: that rung's confirmation prints its inscription and a sand bed (figure omitted, honestly — the booking itself never depends on the picture). Long names/emails: fields are single-line with no maxlength below 254 (email) / 120 (name); the confirmation restates them wrapped, never truncated.

**Fallback & watchdog.** **Watchdog: 3000ms** on the sounding state — if no response, the form unlocks with the network-error summary above; a booking is never left "sounding" forever, and the visitor is never told a booking succeeded that did not. No-JS path: standard POST + server-rendered confirmation (same plate design, static figure).

**Reduced motion.** No glide, no bloom on radio selection (the radio's checked state is indication enough), confirmation appears by cut, seal printed already-pressed. The 500ms sounding state shortens to the request's real duration.

**Accessibility.** Native controls throughout (select, radios, inputs) — no custom widgets to break. Labels are real `<label>`s; the rung radios' labels include the frequency in words. Error summary uses `role="alert"` on submit-fail only (not on every keystroke). Confirmation heading receives focus. All text ink on sand-lit (12.4:1); error text `--bloom-deep` on sand-lit 7.0:1.

**Performance & mobile variant.** The form is one leaf of DOM; the confirmation SVG ≤3KB from the §6.7 cache. Mobile: no plate glide on submit (the in-place plate cuts to the chosen figure), bloom skipped.

**Tokens.** `--sand-lit`, `--bronze`, `--bronze-lit`, `--bronze-deep`, `--bloom`, `--bloom-deep`, `--ink`, `--sound-dur: 500ms`, `--seal-dur: 180ms`, `--ease-resonate`, `--ease-drift`.

### 6.14 Re-sanding (loader & page transition)

**What & why.** When the garden must wait — a page change, a heavy bed loading — the plate is **re-sanded**: sand sweeps flat across the plate and the beds print as raked, empty sand with their labels already set. Loading in this theme is the gardener raking the beds before planting; a skeleton here is not grey boxes but *prepared ground*. It merges with content because the skeleton carries the content's labels and true layout — the visitor reads the bed's title and inscription while its body is still being raked, and nothing shifts when the real content lands (the rake reserves exact space).

**Structure.** Two forms. *Page transition:* a full-plate overlay on the stage (desktop) or a sand veil over the viewport (mobile): the current figure's particles scatter to a flat, even sand field (chaos amplitude driven to a *level* state — uniform jitter, no figure), hold, then the new page's first figure forms (§6.1's short form, 900ms). *Skeleton beds:* a bed whose content is pending renders its title (real), its inscription (real), and body-shaped raked sand: `--sand-deep` blocks with a subtle rake-line gradient (repeating-linear-gradient at 3px pitch, 4% ink) at the exact heights of the incoming paragraphs/cards.

**Motion spec.** Transition: scatter 300ms (`--ease-gliss`), hold ≤ the load's duration (no artificial minimum beyond 300ms — the garden never makes a visitor wait for theatre), form 900ms. Skeleton: a single rake shimmer passes once (a `--sand-lit` band translating across, 1200ms, `--ease-drift`) then stillness — skeletons do not pulse forever; prepared ground is quiet. **Ceiling: 3000ms** — any bed still raked at 3000ms prints whatever content has arrived and marks the rest with the §11 empty-state line rather than raking indefinitely.

**Choreography timeline.** Navigation 0ms: scatter begins. +300ms: flat sand. Load complete: form begins. +900ms after form: new rung locked, inscription updated. Skeleton bed: shimmer 0–1200ms once; content swap by cut per block as it arrives (blocks never fade from 0 — they *replace* rake with print at full opacity).

**State matrix.** *Rest:* no overlay, beds printed. *Loading:* as above; the header and rail remain live and clickable (a visitor may change their mind mid-transition; the new target wins and the veil re-aims). *Scrolled-past:* skeletons below the fold resolve without shimmer (the shimmer only runs in view). *Disabled:* with JS off there are no transitions — pages load as pages, skeletons never appear (content is server-rendered). *Touch:* identical, veil form.

**Content-merge.** Skeleton labels are the real bed titles and inscriptions from the record — a screen-reader user hears the bed's true name during load, not "loading". The transition's flat-sand state is the plate's own material, not a branded curtain dropped over the garden.

**Breakpoints.** ≥1200px: stage overlay form. 768–1199px: veil over the bed area only. <768px: veil full-viewport (the plate is small; the whole garden re-sands). Skeleton rake pitch scales: 3px / 3px / 2.5px.

**Edge cases & failure modes.** Instant loads (cache): if content arrives <300ms, the scatter never starts — no flicker of theatre for a fast page. Failed load: the veil lifts at the 3000ms ceiling and the bed prints the §11 error state with a retry link; the plate re-forms the *previous* page's figure (the garden returns to where you were, in tune). Back-button during transition: the veil follows the newest navigation only (a token guards stale completions).

**Fallback & watchdog.** **Watchdog: 3000ms** ceiling (above) on both forms. The static fallback is the server-rendered page itself.

**Reduced motion.** No scatter, no shimmer: transitions are cuts; skeletons are static raked blocks with labels, replaced by cuts.

**Accessibility.** `aria-busy` on beds while raked, removed on print; the veil is `aria-hidden` and never traps focus; focus is never moved by a transition except the §6.13-style heading focus on a *completed* navigation in the app-shell case. Rake contrast: labels are ink text (10.9:1) — only the decorative rake blocks are low-contrast, and they carry no information.

**Performance & mobile variant.** The veil reuses the plate's particle system (no new assets). Skeleton blocks are CSS gradients — zero images. Mobile veil is one fixed div + the in-place plate's static figure swap.

**Tokens.** `--sand-deep`, `--sand-lit`, `--ink`, `--scatter-dur: 300ms`, `--form-short-dur: 900ms`, `--rake-ceiling: 3000ms`, `--ease-gliss`, `--ease-drift`.

### 6.15 The resting garden (footer)

**What & why.** The footer is the garden at rest: the day's soundings done, the plate printed at rung 0, the whole ladder inscribed on a bronze footer plate, and the conservatory's practical information — address, hours, contact — set in sand below it. It merges with content because the footer plate is the ladder's *third printing* (rail §6.10, inscriptions §6.3, footer): the visitor who scrolls to the bottom is handed the whole instrument, silently, as a colophon. And it is printed, not performed: the garden's last statement is stillness.

**Structure.** A `--bronze-deep` footer plate (the plate, laid flat) carrying: the full ladder as a six-row inscription table (rung · name · (n, m) · Hz — text, `--sand` on `--bronze-deep`, 5.1:1, ≥12.5px), generated from the record (§6.17). Below the plate, on `--sand`: three columns (Visit · The Garden · Write to us) of plain links and text, then a colophon line: "Cymatics Garden — every figure on this page is computed from the Chladni equation with the indices printed beside it." The footer's static figure: rung 0's SVG, small (120px), beside the ladder table.

**Motion spec.** One licensed motion: as the footer first enters, a bronze rule under the ladder table draws itself left-to-right (600ms, `--ease-drift`) — the inscription underlining itself, once. Nothing else moves; the printed plate does not tremble (§6.5's ruling), does not ripple, does not bloom.

**Choreography timeline.** Entry 0ms: rule draw begins. +600ms: complete. There is no second beat.

**State matrix.** *Rest:* printed footer. *Hover/focus:* links underline-draw (240ms) as everywhere; focus rings bronze on sand, sand on the bronze plate (a `--sand` ring on `--bronze-deep` — visible at 5.1:1 against the plate and offset onto the surrounding sand where possible). *Scrolled-past:* it is the bottom; nothing follows. *Disabled:* n/a. *Touch:* tap targets ≥44px in the link columns.

**Content-merge.** The ladder table is generated from the record — if a rung's frequency ever changed in the record, the footer's printing changes with it; the footer can never memorialise a wrong ladder. The colophon line states the theme's law in the garden's own voice — the footer is where the proof is signed.

**Breakpoints.** ≥1200px: plate with ladder table left, figure right; three link columns below. 768–1199px: ladder table full width, figure above it at 96px. <768px: ladder rows wrap to two lines (rung + name / indices + Hz); columns stack.

**Edge cases & failure modes.** A record with fewer rungs (a small site using four): the table prints the record's rungs — the footer never pads the ladder to six with invented pitches. Print stylesheet: the footer plate prints as its sand equivalent (bronze backgrounds dropped, ladder table in ink on white) — the ladder must survive paper.

**Fallback & watchdog.** Entirely static; no watchdog. The rule draw is CSS/loop enhancement over a printed rule (the rule exists at full width beneath the animation's mask).

**Reduced motion.** The rule is simply drawn. Everything else was already still.

**Accessibility.** Footer landmark (`<footer>` / contentinfo). The ladder table uses real table semantics with a caption ("The ladder, complete"). Link contrast: ink on sand 10.9:1; sand on bronze-deep 5.1:1 at ≥12.5px semibold (AA for large/semibold — the ladder's figures are data register, 500 weight).

**Performance & mobile variant.** One small SVG (shared cache with §6.7) + text. Zero per-frame cost.

**Tokens.** `--bronze-deep`, `--sand`, `--ink`, `--rule-draw-dur: 600ms`, `--ease-drift`.

---

### 6.16 The silent bed (404)

**What & why.** A missing page in a conservatory is a bed with nothing planted and no tone assigned: the silent bed. The 404 prints an empty, raked bed — a sand panel with rake lines, a plant label with nothing behind it — and says, in the garden's voice, that this bed has no frequency. It merges with content because its honesty is the theme's law applied to absence: the garden will not invent a figure for a page that does not exist, and the empty plate is the one place the plate is *supposed* to be bare.

**Structure.** A centred composition: the plant label (Fraunces, "This bed is silent."), a raked sand panel (as §6.14's rake, larger), the inscription line `NO FREQUENCY ASSIGNED · (n, m) = —`, and three ways back: the ladder's first rung (Home, sounded at 110.00 Hz), the Programme, and the Visit bed — plain links. The header (§6.10) and footer (§6.15) are the standard ones; the footer ladder still prints in full (the garden exists; this bed doesn't).

**Motion spec.** **None — choreography specified as none.** No formation, no tremble, no ripple. The rake is static. This is deliberate and is itself the spec: a 404 that performed would be a lie about the garden's state. The only animation on the page is the standard link underline on hover.

**Choreography timeline.** None. The page is printed.

**State matrix.** *Rest:* the silent bed, complete. *Hover/focus:* link treatments only. *Scrolled-past:* n/a (the page is one viewport by design; on short screens it scrolls plainly). *Disabled:* n/a. *Touch:* links ≥44px.

**Content-merge.** The three exit links are the site's real primary beds, named as they are named elsewhere. The inscription's em-dash indices are the honest notation for "no figure" — the same register that prints real indices everywhere else prints their absence here.

**Breakpoints.** ≥1200px: panel 560px. 768–1199px: 440px. <768px: full width minus margins; label 30px.

**Edge cases & failure modes.** A 404 reached with a rung fragment (`#bed-3` on a dead URL): the fragment is ignored; the silent bed does not pretend the bed exists. Server errors (500) use the same page with the label changed to "The garden gate is stuck." and the inscription unchanged — one absence page, two honest labels.

**Fallback & watchdog.** Static page; none.

**Reduced motion.** Identical (there was no motion).

**Accessibility.** The label is the `<h1>`. The em-dash inscription is supplemented for screen readers by visually-hidden text: "No frequency is assigned to this page." Status code is the server's real 404.

**Performance & mobile variant.** The lightest page on the site: no canvas, no loop, no images. It must load instantly — a slow 404 in this theme is a special disgrace, and §10 gates it.

**Tokens.** `--sand`, `--sand-deep`, `--ink`, `--glass`.

### 6.17 The ladder record (the one data object)

**What & why.** Every figure, inscription, waveform, rail entry, card line, programme row, bloom, and footer printing in this theme reads from **one declared data object: the ladder**. This element is that record, specified as an element because it is the theme's load-bearing content: if the ladder is wrong, every printing of it is wrong together, and if it is right, they are right together. The garden has exactly one tuning, and this is where it lives.

**Structure.** A JSON object, inlined in the page (or the build's data layer), one entry per rung:

```
{ "rung": 0, "bed": "first-sounding", "name": "The First Sounding",
  "hz": 110.00, "n": 2, "m": 1, "cycles": 2,
  "centre": [0.50, 0.50], "note": "A2" }
```

The canonical ladder for the reference build (a minor-pentatonic ascent A–C–E–G–C, so the page's key changes cohere musically):

| Rung | Bed | Hz | (n, m) | Wave cycles | Note |
|---|---|---|---|---|---|
| 0 | The First Sounding (hero) | 110.00 | (2, 1) | 2 | A2 |
| 1 | What Sound Looks Like | 130.81 | (3, 1) | 3 | C3 |
| 2 | The Equation, Honestly | 164.81 | (3, 2) | 5 | E3 |
| 3 | Specimens | 196.00 | (4, 2) | 8 | G3 |
| 4 | The Season's Soundings (programme) | 261.63 | (4, 3) | 8 | C4 |
| 5 | Sound Your Visit (form) | 220.00 | (5, 3) | 8 | A3 — the visitor's rung: the ladder's one descent, because the form answers the hero |

Rung 5's pitch (220.00, A3) sits below rung 4's by design: the form bed is the visitor's own sounding, an octave of the hero's A — the garden ends where it began, one octave up, in the visitor's hands. The `centre` field is §6.6's disturbance centre for that rung's figure. Waveform cycles follow the original entry's 2 → 3 → 5 → 8 climb and hold at 8 (the margin's resolution limit) for rungs 4–5, distinguished by phase.

**Motion spec.** The record does not move. It *is* moved *from*: every duration and target in §6.1–§6.16 that involves a pitch reads `hz`, `n`, `m`, `cycles` from here.

**Choreography timeline.** None — paper-level. Build time: the static plates, inscriptions, rail, and footer are generated from the record; runtime: the particle system, counters, and form read the same object (inlined identically — the build asserts the two copies match).

**State matrix.** *Rest:* the record, printed in six places. *Every other state:* unchanged — states belong to elements, not to the record. *Disabled (no JS):* the record's printings (static HTML) are the whole story, and they are complete.

**Content-merge.** Total: the record is the content's physics. The programme's sittings (§6.12) reference rungs by index; the form's pitches (§6.13) are the record's rows; a sitting may not reference a rung the record does not contain.

**Breakpoints.** Identical at all sizes (the mobile rail cut, §6.4/§6.10, drops presentations of the record, never entries).

**Edge cases & failure modes.** A build that adds a bed without a rung: the bed is unsounded (§4) and prints `AT REST` — the record is never stretched by the layout. A record edited in one place only (a frequency changed in the rail's HTML but not the object): the build's figure-truth audit (§10) compares all printings and fails the build. Frequencies must be plausible for the fiction (a garden of pure tones: 55–880 Hz) and index pairs must satisfy n ≠ m (n = m yields a degenerate figure — the equation's nodal set collapses — and the audit rejects it).

**Fallback & watchdog.** If the runtime object fails to parse, the page runs print-only: static figures, static inscriptions, no particle system — the garden at rest is always a legal fallback for the whole site. No watchdog; the record cannot strand content because its printings are the content.

**Reduced motion.** Paper-level ruling: the record is identical; the elements' reduced variants consume it as print.

**Accessibility.** Paper-level ruling: every printing of the record is real text or real table data (§6.3, §6.10, §6.15) — the record is never carried by canvas alone.

**Performance & mobile variant.** The object is <1KB. Its printings are the cost, budgeted in §14.

**Tokens.** Consumed by all elements; defines `--ladder-*` custom properties per rung at build time (`--rung-0-hz: 110.00` etc.) for CSS-side labels that must match.

### 6.18 Counters that settle (frequency & figure counts)

**What & why.** The original entry's ambient data rule: frequency and (n, m) indices *count and settle* as each figure forms. This element specifies the garden's counters as one system: the frequency readout during a glide (§6.3), the hero's settling counts (plates in the collection, sittings this season — the conservatory's true totals), and the programme's seats when a booking lands (§6.12). A counter in this theme never spins like a slot machine and never rounds: it travels like a pitch and stops dead on the true figure, ringing for one beat. It merges with content because every counted value is a record value or a true total of printed things — the seats counter counts seats that exist in the table; the frequency counter counts to the rung the plate is forming.

**Structure.** Counters are text spans with `data-count-to` (the true value, present in the HTML as the final text — JS animates a *display copy* and restores the true text at settle, so the DOM's resting state is always the truth). Frequency counters render at two decimals throughout the count (the count passes through the glide's intermediate pitches — 110.00 → 164.81 sweeps the real interval, formatted continuously). Seat and total counters are integers. During a glide, the frequency counter is driven by the loop's glide progress mapped over the interval's log-frequency ratio (pitch is logarithmic; a linear count would sound wrong to a musician's eye).

**Motion spec.** Frequency count: the glide's ≈800ms, log-mapped, `--ease-gliss`, with a 140ms `--ease-resonate` settle at the end (the last 0.4% of the interval takes the settle's curve — the ring). Standalone counters (hero totals, seats): 900ms from first view (hero) or from the booking event (seats), counting from the previous true value — **never from zero** (a seats counter that counts from 0 after a booking is a lie about the seats that were already sold; it counts from the old total to the new). Settle: final value held, with a 120ms inscription-brightening (the engraved digit catches light).

**Choreography timeline.** Glide counters: locked to §6.2's tent. Standalone: trigger +0ms count begins · +900ms settle · +1020ms brightening done. Seats: booking success +0ms · +600ms settle (shorter — a smaller interval, a quicker ring).

**State matrix.** *Rest:* the true value, printed. *Counting:* display copy animating; the true value is in the accessible text (below). *Scrolled-past:* counters that were never seen do not count when finally seen late — if a counter's element enters after its bed has sounded, it simply shows the true value (the garden does not perform for an empty room, retroactively). *Disabled:* true values, always. *Touch:* identical.

**Content-merge.** Every `data-count-to` is generated from the same source as the static text it replaces — build-asserted. The hero's totals (e.g. "214 plates in the collection") must be the true counts of things the site elsewhere enumerates or states; §10's audit samples them.

**Breakpoints.** Identical behaviour at all sizes; on <768px the frequency counter still counts (it is the inscription, §6.3, which survives the margin cut).

**Edge cases & failure modes.** A count interrupted by a new glide: the counter re-targets from its current displayed value — never snaps back to the interval's start. A seats value that would go negative: the form prevents the booking (§6.13); the counter's floor is the record's truth, and a mismatch fails loudly in the audit, never silently clamps. Very large totals: tabular figures, thin-space thousands separators (`34 127` style is *not* used here — the garden uses the plain comma of its other printings; consistency beats cleverness).

**Fallback & watchdog.** The static text is the true value; JS only animates a copy. **Watchdog: 1500ms** — any counter still animating at 1500ms snaps to its true value. Nothing can strand: the worst case is a number that is correct and still.

**Reduced motion.** No counts: values swap by cut. The settle brightening does not run.

**Accessibility.** During a count, the animating span is `aria-hidden` and a visually-hidden twin holds the final value, so assistive tech reads the truth once, not a stream of pitches. Counters are never in live regions.

**Performance & mobile variant.** Text writes at most once per frame per counter, ≤3 counters alive at once (frequency + one standalone + seats). Mobile identical.

**Tokens.** `--ink`, `--count-dur: 900ms`, `--seats-count-dur: 600ms`, `--ease-gliss`, `--ease-resonate`.

---

## 7. Page application map

**Home (the garden itself).** The full ladder, hero formation (§6.1), beds in rung order, programme (§6.12), form (§6.13), resting footer (§6.15). This is the reference build §8 walks through.

**Listing page (the collection / all sittings).** The plate rests at the listing's own rung (a listing page is assigned one rung from the record, or rests at rung 0 if it is a utility listing). Items are bed cards (§6.11) in beds of three; filters are the §11 select and tabs, styled as plant-label sorts; pagination is printed (§11). No glissando on a listing page — commerce-adjacent pages are kept calm; rung changes happen only when the visitor opens a detail page.

**Detail page (one sitting / one specimen / one instrument).** The detail's own rung sounds on arrival (formation short form, 900ms, §6.14's mechanism): the plate forms the item's figure while the item's text prints beside it. Specimen frames (§6.9) for its photographs; its programme row (§6.12) is reproduced as its booking card; the form (§6.13) arrives pre-set to this sitting. Related items are bed cards carrying their own rung lines.

**About (the conservatory / the makers).** An unsounded page by default — text beds at rest against the resting figure, specimen frames for the workshop photographs (captioned by the pictured instruments' true pitches where known; a portrait of a person is never put in a specimen frame, §6.9's rule). One sounded bed is permitted: the page's explanation of the equation itself, at rung 2 (the Equation bed's own rung), with the formula printed in Fraunces italic and a static plate.

**Contact / visit (the gatehouse).** The form system (§11 inputs) on a sand leaf; no plate heroics — the visit information (hours, address, directions) is the content, printed plainly, with the ladder rail still present for orientation. Booking conversion lives in §6.13, not here; this page answers letters.

**Checkout (tickets, shop).** **Routed out of the theme's theatre**, as the theatre theme routed its checkout out: payment is a plain sand-leaf surface (§11 buttons/inputs at their calmest), no plate, no blooms, no glissando — the garden does not perform while a visitor is paying. The order confirmation, however, returns to the garden: it prints the §6.13 confirmation plate (figure + seal + reference), because a confirmation is a document of the garden, and documents are where the theme is strongest.

**The silent bed (404/500).** §6.16, verbatim.

---

## 8. Worked examples

### 8.1 The hero — "The First Sounding" (rung 0)

**The bed.** A science-museum microsite, "Cymatics Garden — an exhibition of visible sound." The visitor arrives. The page ground is sand; in the centre stage, a bronze plate, sanded flat; in the left margin, a pale waveform of 2 cycles, undrawn; the rail lists six rungs, its marker at the top.

**Scroll timeline.** 0ms: first paint — the static (2, 1) SVG is already under the transparent canvas, the `<h1>` "Sound, made visible." printed at the plate's centre cell in Fraunces 64px, the inscription beneath reading `FIGURE (n, m) = (2, 1) · 110.00 Hz · RUNG 1 OF 6`. +150ms: the rim sweep begins. +350ms: particles start to move; the headline is already fully readable (it never waited). +900ms: the star is recognisable — four lobes of sand gathering. +1500/+1620/+1740ms: the headline's three lines settle their last 10px, a breath, not an entrance. +2200ms: lock — the sand brightens for 120ms, the tremble fades in over the next 600ms, the margin wave finishes its draw. The visitor scrolls: the bed "What Sound Looks Like" approaches; at the interval, chaos rises, the readout begins its log-count 110.00 → 130.81, and the garden changes key.

**Build notes.** Everything in this hero is §6.1 + §6.3 + §6.4 + §6.10 composed; the only hero-specific decisions are the headline's three-line cap and the centre-cell placement (desktop) — both already specified. If the canvas is unavailable, this hero is pixel-for-pixel the static composition: SVG figure, centred headline, printed inscription.

### 8.2 Mid-page — the Specimens bed (rung 3, 196.00 Hz, (4, 2))

**The bed.** The exhibition's specimen bed: three photographs — a Chladni plate in the museum's own collection (bow at its rim), a bronze singing bowl, a hand scattering sand — each in a glass-green frame (§6.9), captioned by its pitch. The bed's text (260 words) explains that the bowl and the plate are cousins: same physics, different geometry.

**Scroll timeline.** The visitor leaves rung 2's bed. Interval: the (3, 2) figure dissolves; chaos peaks at the midpoint; the (4, 2) lattice — visibly more woven — attracts the sand. Lock: inscription re-engraves to `(4, 2) · 196.00 Hz`, the rail marker arrives, the margin wave redraws at 8 cycles. The bed's title rises through its sand-mask (500ms). The three frames enter: each image focuses 1.06 → 1.0 (900ms, staggered by entry, not by index — they focus as the reader reaches them), glints sweep once. Hovering the bowl's frame: the pinned plate stirs locally at the (4, 2) centre (the record's `centre` for rung 3) — the visitor's finger is on the rim of the very figure the bowl's cousin-equation draws. Clicking the frame blooms a scarlet (4, 2) miniature over the photograph for 600ms, and the plate answers with its sympathetic stir.

**Build notes.** The bed's figure, the frames' captions, and the bloom all read rung 3 from the record — a builder who hard-codes "196" anywhere has failed the build (§10 audit greps for stray frequency literals outside the record and its printings).

### 8.3 Conversion — "Sound your visit" (the form bed)

**The bed.** The exhibition's booking bed. The programme table (§6.12) above the form lists Saturday's soundings; the visitor picks the 11:00 demonstration (rung 4, 261.63 Hz, 14 seats left), then — because the form offers it — chooses *their own pitch* for the confirmation: they pick rung 1, "What Sound Looks Like," 130.81 Hz, the figure they loved at the top of the page.

**Scroll/submit timeline.** Selecting rung 1's radio blooms a small scarlet (3, 1) figure at the label — they hear their choice with their eyes. Submit: the plate-key presses; "Sounding…" for 500ms while the pinned plate glissandos from the programme's (4, 3) down-then-up to the visitor's (3, 1) (the glide handles the descent by the same tent, direction-agnostic). The form leaf settles into the confirmation plate: the (3, 1) figure, printed; the inscription; reference `CG-0614-003`; the sitting restated ("The Season's Soundings — Saturday demonstration, 11:00, 2 seats"); the scarlet seal pressing at +700ms; and the garden's line: "Your figure is drawn. The plate will sound it on Saturday." In the programme table above — off-screen now — the 11:00 row's seats have settled 14 → 12, counting from the true old value, ready to be believed when the visitor scrolls back up.

**Build notes.** The no-JS path posts and returns this same confirmation as a server-rendered page. The error path (the sitting filled meanwhile) preserves every field and offers the 14:00 sitting in one click — §6.13's disabled-state rule, exercised here because it is the conversion section where honesty costs money and is therefore where it matters.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **A drawn figure.** The moment a "Chladni pattern" is an SVG somebody sketched, a stock star, or a mandala generator with random petals, the theme's one claim dies. *Cure:* every figure is evaluated from F at its printed (n, m) — §10's audit samples the nodal set mathematically. There is no asset folder of figures.
2. **Equaliser bars and audio waveforms as decoration.** Rainbow EQ bars, a "sound wave" divider squiggle, a pulsing play button — the clip-art of sound. *Cure:* the law (§1). The only waveforms are §6.4's, at the record's true cycle counts; the only pulse is a tone's physics.
3. **Neon on black "audio visualiser" styling.** This theme is sand and bronze in daylight. A dark-mode page with glowing cyan figures is a different, cheaper theme wearing this one's name. *Cure:* §2's dusk ruling — the plate stays lit and sand-coloured; nothing glows; bloom scarlet is a flower, not a laser.
4. **Indices that don't match the figure.** Printing (3, 2) under a (2, 1) star because the caption was copied from the bed above. *Cure:* inscriptions are generated from the record by the same code path as the physics; the audit compares them.
5. **Chaos that never resolves.** A glissando that leaves the plate muddy, or a lock that arrives late, reads as a broken page, not a retune. *Cure:* §6.2's 1200ms snap watchdog; the figure is always either formed, forming on schedule, or snapped — never soup.
6. **Tremble creep.** The resting tremble at 1px is charming; at 3px the page looks anxious and cheap, and text-adjacent jitter destroys the conservatory calm. *Cure:* 0.35px cap in tokens; type never trembles (Type law 5); §10 measures it.
7. **Scarlet everywhere.** Bloom used as the generic accent colour — links, buttons, badges — spends the flower until it means nothing. *Cure:* the three licensed appearances (§2) and a scarlet census in the gate: >3 per viewport fails.
8. **Rounded, soft, "wellness-app" styling.** Sound-healing clichés — lavender gradients, lotus icons, floating orbs. *Cure:* square corners on glass and plates, sand and bronze materials, Fraunces' carved serif; the garden is a conservatory, not a spa brochure.
9. **Counters from zero and rounded totals.** "200+ exhibits!" under a counter that spun up from 0. *Cure:* §6.18 — counters travel from the previous true value, land on exact figures with units, and totals are the true sums of printed things.
10. **A form that says "Submit".** Generic SaaS form furniture — floating labels, a spinner, a green tick toast — inside the garden. *Cure:* §6.13's plate-key, sounding state, and confirmation plate; §11's refusals (no spinner, no toast) with their in-theme replacements.
11. **Hover sparkles.** Particle bursts, cursor trails, magnetic buttons — nightclub physics. *Cure:* hover is a fingertip on a rim (§6.6): local, physical, quiet, and identical on focus.
12. **The plate as wallpaper.** The bronze plate dimmed behind hero text, cropped by the viewport edge, or repeated as a section background. *Cure:* §4 — the plate is an instrument on a stand, whole and lit, or (mobile) a plate above its bed; never a texture.

## 10. Quality gate

The build may not ship unless **every** blocking check passes. A non-builder signs the gate.

1. **Figure-truth audit.** For each rung, a script samples F at the printed (n, m) on a 64×64 grid and compares the nodal set against the shipped static plate's sampling: ≥98% agreement required. Any rung whose printed indices differ from its computed figure fails the build.
2. **One-record audit.** Grep the build for frequency literals (e.g. `130.81`, `196.00`) outside the ladder record and its generated printings: zero strays. Rail, inscriptions, footer ladder, programme rung cells, and form radios all print the record's values exactly.
3. **Lock test.** At three scroll speeds (slow read, fast flick, jump scroll), the plate is never observed in chaos for >1200ms after a lock point, and the inscription always matches the figure shown.
4. **No-JS pass.** With JavaScript disabled: every bed's content, figures (static), inscriptions, programme, and form are present and correct; the form submits to its server path.
5. **Reduced-motion pass.** With `prefers-reduced-motion`: no tremble, no ripple, no glide, no bloom, no counts; figures cut between beds; all content identical.
6. **Scarlet census.** No viewport, at any scroll position, shows scarlet in more than the three licensed roles, and never as body text or a button fill.
7. **Contrast audit.** Body text ink-on-sand ≥10:1 measured; no bronze or glass text below its §2 ruling; error text `--bloom-deep` ≥7:1 on its leaf.
8. **Tremble measurement.** Resting tremble amplitude ≤0.4px (measured from particle telemetry), sand only; zero text elements animated.
9. **Watchdog drill.** With the particle loop artificially stalled, formation and glissando snaps fire at 4000ms / 1200ms and inscriptions stay truthful throughout.
10. **Seats reconciliation.** After a test booking, the programme row, the confirmation reference sequence, and the record agree; a forced failure mid-booking leaves all three at the pre-booking truth with the honest error shown.
11. **Performance budget (§14) verified** on a mid-tier Android over throttled 4G: LCP ≤2.5s, per-frame physics ≤1.2ms desktop / ≤0.6ms mobile, no long task >50ms during a glide.
12. **404 speed & honesty.** The silent bed loads with no canvas and no loop, prints `NO FREQUENCY ASSIGNED`, and returns a real 404.

## 11. Component inventory

Every ordinary component, with its conservatory treatment — or its refusal and replacement.

| Component | Treatment in this theme |
|---|---|
| Primary button | The **plate-key**: a bronze key (`--bronze`, sand inscription-register label), lit top edge, presses 1px with a 120ms settle; used once per view (the form's "Sound my visit", a bed's main action) |
| Secondary button | Sand key: `--sand-lit` face, bronze 1px edge, ink label; hover warms the edge to `--bronze-deep` |
| Text link | Ink, underline draws left-to-right 240ms; visited links deepen to `--bronze-deep` (a read path in the garden is a walked path) |
| Inputs (text/email/number) | Sand-leaf fields, 1px `--glass` rule beneath, label above in Space Grotesk 500; focus: bronze underline draws + label warms (§6.13) |
| Select | Native `<select>` in a sand field with a bronze chevron (the programme's sitting picker) — never a custom listbox |
| Radios / checkboxes | **Rung radios** (§6.13): full-width rows, inscription-register pitch data, a sand-bed square indicator that fills with a miniature of the rung's nodal dot pattern when checked; checkboxes are small sand squares with an ink tick drawn 160ms |
| Tabs | **Bed tabs** (listing filters): plant-label tabs — sand labels on a glass rule, the active label's rule thickens to bronze; content swaps by cut with its bed's mask (§6.11) |
| Accordion | **Bed folds**: a bed section that opens like a rake passing — content prints downward behind a settling sand-mask (500ms); one open at a time in a group; headings are real buttons |
| Table | §6.12's programme table is the pattern for all tables: sand-lit leaf, inscription-register numeric columns, sticky header in-bed |
| Cards | §6.11 bed cards |
| Badge / tag | **Refused as pills.** A status is an inscription line (`FULL`, `AT REST`, `SOUNDED OUT`) in the register, printed in ink — never a coloured chip |
| Alert / banner | A **notice bed**: a sand-deep strip with a bronze left rule and the message in body text; errors use `--bloom-deep` text (never a scarlet fill) |
| Toast | **Refused.** Transient messages have no home in a garden; outcomes are documents (confirmation plate) or notice beds that persist until dismissed |
| Modal | The **glasshouse modal**: a centred sand leaf under a `--glass` scrim (the conservatory glass fogs — scrim is glass at 88% with the page visible, quiet, behind it); one modal maximum; Esc and scrim-click close; focus trapped and returned |
| Tooltip | A small sand label, inscription register, appearing above its element after 400ms hover/focus, gone on leave — tooltips carry data (a rung's note name), never instructions |
| Pagination | Printed pagination: `PREVIOUS BED · 2 OF 5 · NEXT BED` as text links with the record's rung names where the pages are beds |
| Progress bar | **Refused as a bar.** Progress is the ladder rail + inscription (§6.3, §6.10); a linear bar exists only inside the form's sounding state, as a sand-fill in the button (500ms, truthful to the request) |
| Spinner | **Refused.** Waiting is re-sanding (§6.14) |
| Skeleton | §6.14's raked beds |
| Breadcrumbs | The **path line**: `GARDEN / BEDS / SPECIMENS` in inscription register at a bed's head, links underlining as usual — a garden path, walked in order |
| Search | A sand field in the header's menu; results are bed cards + programme rows (the garden's two content shapes), each with rung lines where honest |
| Toggle ("Still the garden") | A labelled sand switch (§6.5): kills tremble + ripples for the session; state persists; `aria-pressed` |
| Empty state | §11 voice: `THE GARDEN IS BETWEEN SEASONS` pattern (§6.12) — a raked bed, a true sentence, the next true thing offered |
| 404 | §6.16, the silent bed |
| Footer | §6.15, the resting garden |

## 12. Copywriting voice

Two registers, one garden.

**The Keeper's register** (headlines, bed titles, empty states, the confirmation's closing line): the voice of the person who tends this conservatory — unhurried, exact, fond of the physics. Sentence case, short declaratives, numbers always with units and never rounded for drama. Headlines name the sounding thing: "Sound, made visible." / "The bowl and the plate are cousins." / "Choose the pitch of your visit." *Not:* "Experience the magic of sound!!" (exclamation marks are banned from the garden entirely — a conservatory does not shout), not "Unlock the power of frequencies" (nothing is locked; nothing is "powered").

**The Inscription register** (labels, readouts, table heads, errors' factual lines): uppercase, letterspaced, tabular — lettering under a plate. `FIGURE (n, m) = (3, 2) · 164.81 Hz` · `SEATS REMAINING: 12` · `NO FREQUENCY ASSIGNED`. Errors are written in the Keeper's voice for the sentence and the Inscription register for the fact: "That sitting has filled. — SEATS REMAINING: 0 · The 14:00 sounding still has room."

**Fixed strings (verbatim, do not paraphrase).**
- The colophon: "Every figure on this page is computed from the Chladni equation with the indices printed beside it."
- The confirmation's closing line: "Your figure is drawn. The plate will sound it on Saturday." (weekday varies with the sitting; the sentence's shape does not.)
- The network error: "The garden gate didn't open — your details are still here. Try again."
- The 404 label: "This bed is silent."
- The still-toggle: "Still the garden."

**Error voice.** Specific, kind, and preserving: name the field and the fact ("The email needs an @ — we could not read it as an address."), never blame, never clear the form. **Empty-state voice.** A true sentence about the garden's state plus the next true thing: between seasons → the next season's first date; a search with no results → "Nothing in the garden sounds at that pitch." plus the nearest rungs. **Label style.** Buttons are verbs from the world: "Sound my visit", "Book the sitting", "Walk the ladder" — never "Submit", "Click here", "Learn more" (say what will be learned: "Read the equation").

## 13. Scroll choreography map

The whole sounded page, top to footer, in order. (Pinned-plate build; in-place builds run the same beats per bed.)

1. **Arrival.** Static hero complete (SVG figure, headline, inscription). Rim sweep (300ms). Formation begins (+150ms).
2. **Lock of rung 0** (+2200ms): sand brightens 120ms; tremble fades in (600ms); margin wave completes its 2-cycle draw; rail marker at rung 0.
3. **Bed 1 interval.** Chaos tent rises; frequency counts 110.00 → 130.81 (log-mapped); wave cross-draws to 3 cycles.
4. **Lock of rung 1.** Inscription re-engraves to (3, 1); bed 1's title settles through its sand-mask; its cards stagger in (90ms).
5. **Bed 2 interval + lock.** (3, 2) forms — the first woven lattice; wave to 5 cycles. The equation bed prints the formula itself; no specimen frames here (the maths is the exhibit).
6. **Bed 3 interval + lock.** (4, 2); wave to 8 cycles. Specimen frames focus as reached (900ms each, glint sweep once). Hover stirs answer the reader's hand at rung 3's centre.
7. **Bed 4 — the programme.** The plate holds (4, 3) at 261.63 Hz. The table is read, not performed: rows stir the plate on hover, bloom on click; header pins inside the bed.
8. **Bed 5 — the form.** Plate at the visitor's rung (220.00, (5, 3)) — the ladder's descent home. Radios bloom on selection. On submit: the sounding, the chosen figure on the plate, the confirmation plate, the seal, the seats settling in the table above.
9. **The footer.** The garden rests: printed (2, 1) figure, the ladder inscribed in full, the rule drawing itself once beneath the table (600ms). Stillness.

**Reverse pass.** Every beat runs backwards faithfully: glides retune down the ladder, waves redraw to fewer cycles, masks never replay (content, once printed, stays printed — only the *instrument* retunes). **Jump scroll.** §6.2's rule: crossing ≥2 rungs snaps the target figure formed; the inscription and marker agree on arrival; no beat is owed to a reader who teleported.

## 14. Whole-page performance budget

| Budget | Limit | Notes |
|---|---|---|
| Total page weight (home) | ≤ 640KB | Fonts ≤ 120KB (Fraunces + Space Grotesk subsets, `font-display: swap`); static plates ≤ 8KB total; specimen images ≤ 120KB each, ≤ 3 above the fold |
| Plate physics | ≤ 1.2ms/frame desktop (900 particles), ≤ 0.6ms mobile (220) | Gradient sampling only; zero allocation in the loop; DPR cap 1.5 |
| Shared loop | One rAF; sleeps when settled & no ambient armed | Long tasks: none > 50ms during any glide |
| Ambient cost | Tremble ≈0.3ms/frame; ripples compositor-only | Both suspend off-screen / hidden tab |
| LCP | ≤ 2.5s on throttled 4G, mid-tier Android | The hero is DOM + SVG at first paint — the canvas never gates LCP |
| CLS | 0.00 target | Inscription reserves its box (§6.3); images reserve aspect ratios; counters never change width (tabular figures) |

**Cut order when the budget is exceeded** (in this order, never silently): 1) resting tremble (the loop's idle wake), 2) ripple rings, 3) specimen glint sweeps, 4) particle count 900 → 500 (formation time held by stride), 5) margin waveforms to static print, 6) hero formation to the short form. **Never cut:** the static figures, the inscriptions, the ladder record's printings, the form's honesty machinery (watchdog, preserved fields), any reduced-motion variant. A garden that must choose between its tremble and its truth keeps its truth.

## 15. Build-order checklist

1. **The record first.** Author §6.17's ladder; generate `--ladder-*` properties; write the figure-truth audit (§10.1) before any figure ships.
2. **Print the garden.** Static HTML/CSS: all beds, static SVG plates from the record, inscriptions, rail, programme, form (server path), footer ladder. Verify the no-JS pass (§10.4) — the garden at rest is the foundation, not a fallback afterthought.
3. **Typography & palette tokens** exactly as §2–§3; run the contrast audit (§10.7).
4. **The plate system.** Canvas + particle engine (§6.1) with the nodal sampling data; formation + watchdog; then the glissando (§6.2) and its snap.
5. **The shared loop** with the 0.12 / 0.08 lerps; register tremble (§6.5), waveforms (§6.4), rail marker (§6.10), counters (§6.18).
6. **Inscriptions & counters** wired to locks (§6.3, §6.18).
7. **Touch.** Rim hover/focus stir (§6.6), click-to-sound blooms (§6.7) with the SVG cache and housekeeping sweep.
8. **Ambient.** Ripple rings (§6.8); the "Still the garden" toggle.
9. **Beds' furniture.** Cards (§6.11), specimen frames (§6.9), programme table (§6.12) with seats reconciliation.
10. **The form.** §6.13 end-to-end including the disabled-sitting error, the sounding watchdog, and the confirmation plate; test the no-JS POST path.
11. **Transitions & skeletons** (§6.14); the silent bed (§6.16).
12. **Reduced-motion variants** for every element; run §10.5.
13. **Mobile transformations**: margin cut, in-place plates, table-to-list, rail disclosure.
14. **Performance pass** against §14 on real mid-tier hardware; apply the cut order if needed.
15. **The gate.** §10 signed by a non-builder — figure-truth, one-record, scarlet census, watchdog drill, seats reconciliation — before the theme may be used in a build.

---

*End of Theme 090 — Cymatics Garden (50x expansion). Identity preserved from the original entry: same concept, same five palette anchors, same two type families, all nine original signature elements deepened, and the theme's anti-slop heart kept intact — the patterns are computed from the real Chladni equation, with each figure's actual (n, m) indices printed beneath it, because the beauty is checkable maths.*
