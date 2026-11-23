# 84. The Tube Weather Bureau — Expanded (v1 + v2)

> A 1950s analog-computing weather bureau — vacuum tubes, patch
> cords, and forecasters in shirtsleeves solving the atmosphere by
> hand and valve. Warm, analog, quietly confident: the
> anti-dashboard. The page is not a screen of widgets. It is a
> bench in a working bureau at the start of a shift: panels bolted
> down, cords patched by hand, dials that read what the room has
> computed, and everything — *everything* — also written down on
> the chart paper, because a bureau that cannot show its workings
> has not made a forecast. It has made a guess.

**The theme's one law: print first, glow second — no reading lives
only in the light.** Every figure on the page is printed in full,
in ink, on chart paper or in mono type, before any tube warms,
any needle sweeps or any filament brightens. The glow is warmth
over a finished record, never the record itself. A dial whose
value exists only as a needle position has broken the law; a panel
whose content waits for an animation to exist has broken it twice.
Every number printed anywhere traces to one declared document —
the Observation Sheet (§6.17) — and the sheet is printed on the
page where a visitor can check the dials against it.

---

## 1. Concept & world

In 1950, at Aberdeen Proving Ground, the ENIAC ran the first
numerical weather forecast in history: twenty-four hours of
computing to predict twenty-four hours of weather, the arithmetic
carried on vacuum tubes and patch cords, the results read off
dials and transcribed by hand. The Tube Weather Bureau is that
room, kept. Not a museum of it — a working bureau that never
modernised: the forecasts are still solved on the bench, the
panels are still brushed aluminium with riveted corners, the
cords are still patched by a person who knows which jack takes
which plug, and the forecaster on shift still signs the sheet.

The emotional register is *quiet confidence under warm light*.
Nothing in the bureau hurries and nothing performs. A modern
weather dashboard shouts in saturated blues and animated radar
sweeps; the bureau murmurs in amber and paper, and its confidence
comes from the visible labour: you can see the connections, see
the dials settle, read the sheet. The site's argument — made by
its furniture, not its copy — is *this forecast was made by
someone, carefully, and here is the working*.

**The world, stated plainly.** The bureau has: a bench of
riveted panels (§4), each panel an instrument or a record;
patch cords (§6.2) that connect panels the way the computation
connects them; valves whose filaments warm when the room works
(§6.1, §6.6); a master dial at the centre panel (§6.8) that the
whole room is organised around; a chart-paper record of
everything (the Observation Sheet, §6.17); a requisition desk
where visitors ask the bureau for things (§6.13); and a
maintenance log in the footer where the room admits its own
failures (§6.15, §6.16). The forecaster is a presence, not a
mascot: a voice in the copy (§12), a signature on the sheet,
never a cartoon in shirtsleeves waving at the visitor.

**Best-fit sites and audiences.**

- **Weather and climate data services** whose differentiator is
  method — a service that shows its workings (observation-based
  forecasting, hyperlocal stations, marine or aviation weather)
  gains a room that embodies the method.
- **Broadcasters and programme pages** with a heritage of
  forecast craft — the shipping-forecast register, the evening
  bulletin — where the audience already trusts a human voice
  reading figures aloud.
- **Retro-tech and analog-computing brands** — synthesizer and
  valve-amp makers, film and analog-process studios, computing
  museums with working machines — where the room is the product's
  own ancestry.
- **Data products that must feel accountable**: environmental
  monitoring, energy-grid weather risk, agricultural forecasting
  — anywhere "a person checked this" is worth more than "an
  algorithm generated this."

**When NOT to use it.**

- **Severe-weather alerting.** When a tornado warning must land
  in 400ms with maximum alarm, a room that warms up over two
  seconds is a liability. The bureau issues forecasts; it does
  not shout warnings. (The storm card in §11 exists, but it is a
  printed card, not an alarm.)
- **High-frequency live data.** Tick-by-tick markets, live
  sports, dispatch boards: the bureau's fastest honest rhythm is
  the dial settle (~900ms). Data that changes ten times a second
  will make the valves look broken.
- **Clinical or scientific-instrument contexts** that need cold
  neutrality — a laboratory LIMS, a medical monitor. Warmth here
  is an argument; where no argument is wanted, do not build the
  room.
- **Children's products.** The bureau is adult, unhurried and
  text-dense; its charm is lost on, and its density hostile to, a
  seven-year-old.

**The room's honesty rules** (enforced by §10): stations that
have not reported are named as silent, never silently dropped
from the count (§6.17); a forecast figure is never printed that
the sheet does not carry; flicker is rationed to exactly two
licensed places (the warm-up's single settle flicker, §6.1, and
Valve 7, §6.16) because a room where everything flickers is a
room where nothing is maintained.

---

## 2. Palette

Five anchors from the original entry, unchanged, plus seven
derived tokens. The bureau is lit by its own valves: a dark warm
ground (bakelite and shadow), one warm light source (amber), one
paper surface where the record lives, one signal colour that is
a *physical object* in the room (the red patch cord) and one
quiet institutional green.

| Token | Hex | Role | Usage ratio |
|---|---|---|---|
| `--bakelite` | `#3A2C22` | Anchor. Panel faces, header bench, card stock on dark ground | ~34% |
| `--amber` | `#E8A33D` | Anchor. Tube glow, filament light, dial illumination, active states | ~7% (light, not surface) |
| `--paper` | `#EFE6D0` | Anchor. Chart paper: the record, tables, form slips, body text on light panels | ~30% |
| `--cord-red` | `#B3402A` | Anchor. Patch cords, the one signal colour: tendencies, warnings, the plug in hand | ~3% |
| `--panel-green` | `#44584A` | Anchor. Secondary panels, footer bench, "reporting" status, calm confirmations | ~12% |
| `--bakelite-deep` | `#271C14` | Derived. Page ground behind the bench, footer depth, shadow side of panels | ~10% |
| `--filament-cold` | `#7A2418` | Derived. A filament at rest: dark red, the warm-up's starting temperature | glow only |
| `--amber-hot` | `#F6C569` | Derived. Filament core at full working temperature; the progress frontier | glow only |
| `--paper-dim` | `#D9CCAC` | Derived. Aged paper edges, table rules, secondary print on paper | ~3% |
| `--ink` | `#2C241B` | Derived. Print ink on chart paper: body text, table figures, form handwriting lines | text on paper |
| `--aluminium` | `#B7B1A2` | Derived. Brushed panel frames, rivets, image windows (§6.9) | ~1% |
| `--aluminium-dark` | `#847D6E` | Derived. Brushed metal in shadow, rivet shading, disabled hardware | <1% |

**Measured contrast (computed from the hex values for this
expansion):**

- `--ink` on `--paper`: **12.0:1** — the record's text pairing;
  all body copy and table figures on paper use it.
- `--paper` on `--bakelite`: **10.4:1** — panel headings and
  light text on dark panels.
- `--amber` on `--bakelite`: **6.3:1** — licensed for panel
  labels, dial numerals and active states (large or mono text);
  never for long body copy, because glow is tiring to read at
  length even when the ratio passes.
- `--cord-red` on `--paper`: **4.6:1** — licensed for tendency
  figures, warning lines and short labels on paper.
- `--panel-green` on `--paper`: **6.1:1** — status text and the
  footer's print.
- `--paper` on `--panel-green`: **6.1:1** — footer headings.
- `--amber` on `--paper`: **1.7:1** — *forbidden pairing for
  text.* Amber is a light, and light does not print on paper; on
  paper panels the "lit" state is shown by `--cord-red` or a
  filled jack, never by amber text.
- `--filament-cold` on `--bakelite-deep`: **1.6:1** — a glow
  state, never text; a cold filament is seen, not read.

**Pairing rules.** (1) Every text pairing above is the *only*
licensed pairing for that surface — a builder who needs a new
one must measure it and add it to this table. (2) Amber appears
as light: gradients, glows, filament strokes, dial illumination.
It is never a flat background for a content block — a page that
is 30% flat amber has built a warning sign, not a bureau.
(3) Cord red is rationed to what is physically red in the room:
the cords themselves, and figures that behave like cords —
tendencies, connections, the one warning line per panel. A page
with red body text has spent the signal. (4) Panel green is the
room's calm: statuses that mean *reporting, filed, steady*.

**Dark-mode behaviour.** There is no inverted scheme and no
light mode. The bureau is a room lit by valves; at night the
same room is worked by lamplight, and the tokens do not change —
the visitor's OS preference does not redecorate the bureau.
What *does* change is §6.1: under `prefers-reduced-motion` the
room ships already warmed (§6.1's variant), which is the
theme's answer to "just show me the lit room." Paper-forward
pages (the sheet, §7) invert the *ratio*, not the palette: paper
becomes the ground at ~70% and bakelite the furniture — same
tokens, same pairings, the record brought to the front of the
bench.

---

## 3. Typography

Three families, each doing the job it did in the room. **Oswald**
is the panel lettering — the stencilled, letterspaced capitals
painted on the hardware. **Libre Caslon** is the forecaster's
prose — the written forecast, the explanation, the signature.
**IBM Plex Mono** is the data — every figure the bureau commits
to, set so digits align in columns like a teletype ledger.

| Role | Font | Size / line-height | Tracking | Case & notes |
|---|---|---|---|---|
| Panel title (hero) | Oswald 500 | 3.5rem / 1.05 (56px) | +0.14em | UPPERCASE, painted on the master panel |
| Panel title (section) | Oswald 500 | 1.75rem / 1.1 (28px) | +0.12em | UPPERCASE, one per panel, never two lines |
| Instrument label | Oswald 400 | 0.8125rem / 1.3 (13px) | +0.18em | UPPERCASE, the lettering beside dials and jacks |
| Forecast prose | Libre Caslon | 1.125rem / 1.65 (18px) | 0 | Sentence case; the forecaster writes like a person |
| Body / record text | Libre Caslon | 1rem / 1.6 (16px) | 0 | On paper and on bakelite (in `--paper`) |
| Data figure (hero) | IBM Plex Mono 500 | 2.25rem / 1.1 (36px) | 0 | Tabular; the printed value beside the master dial |
| Data figure (table) | IBM Plex Mono 400 | 0.9375rem / 1.5 (15px) | 0 | Tabular, right-aligned in columns |
| Log / caption | IBM Plex Mono 400 | 0.8125rem / 1.55 (13px) | +0.02em | UPPERCASE for log stamps, sentence case for captions |

**Five type laws.**

1. **Oswald never writes a sentence.** Panel lettering is names,
   labels and short orders — "PRESSURE", "PATCH TO STATION",
   "ISSUED 06:00". The moment a line needs a verb and a full
   stop, it belongs to Caslon. A paragraph set in Oswald is a
   sign, not a bureau.
2. **Figures are mono, always.** Every number the bureau commits
   to — pressure, temperature, wind, counts, times, requisition
   numbers — is IBM Plex Mono, tabular, so columns align and a
   figure can be checked against the sheet digit by digit. A
   proportional-font number anywhere on the page is a defect.
3. **Caslon carries the argument.** Explanation, method, the
   forecaster's reasoning and all error and empty states are
   Caslon prose in the Forecaster register (§12). The bureau
   persuades in sentences, not in labels.
4. **Warmth never changes type.** The warm-up (§6.1) changes the
   *light* on letters, never their face, weight or spacing — no
   layout shift as the room warms (zero CLS is a law, not a
   target: letter shells are final from first paint).
5. **The log is stamped, not styled.** Maintenance-log and
   requisition entries (§6.13, §6.15) are mono, uppercase,
   timestamped, and identical in form every time — the stamp is
   the style.

**Scale behaviour.** Panel titles hold their size across
breakpoints until <768px, where the hero panel title drops to
2.5rem/1.08 and section titles to 1.375rem; data figures never
shrink below 0.875rem in tables — a figure too small to check
against the sheet is a figure the bureau has stopped standing
behind. Oswald's letterspacing is part of the lettering and is
never tightened to make a long name fit; long names wrap to a
second line on the panel instead (panels are sized for their
lettering at build time, §15).

---

## 4. Layout language

The page is a **bench**: a run of brushed-aluminium panels
bolted to a bakelite worktop, wired together by patch cords,
organised around one centre panel that carries the master dial.
The visitor reads the bench left to right, top to bottom, the
way a forecaster walks it at the start of a shift.

**The panel.** Every content section is a panel: an
`--aluminium` frame (2px, with a brushed gradient that runs
horizontally, never vertically — brushed metal is drawn in one
direction), four rivets (9px circles at 14px insets, drawn once
as SVG symbols, shaded `--aluminium-dark` on the lower-right
quadrant), a `--bakelite` or `--paper` face, and an instrument
label (§3) lettered at the frame's top-left, *on the metal*, the
way real panels are engraved. Panel padding is 28px on ≥1200px,
20px below. Panels never float, never cast soft shadows, and
never round their corners beyond 3px — hardware is square, and
the one softness in the room is light.

**The grid.** ≥1200px: a 12-column bench, content max-width
1240px, gutter 24px. Panels span in whole instruments: the
master panel 8 columns with its dial rail at 4; station panels
in rows of 3×4 columns; the sheet (§6.12, §6.17) full width when
it appears, because the record is never squeezed into a sidebar.
768–1199px: 8 columns, station panels 2 per row, master panel
full width with the dial rail beneath it. <768px: one column;
panels stack in shift order; the master dial stays in its panel
(§6.8's breakpoints) and the cords become vertical drops (§6.2).

**Spacing rhythm.** The bench breathes in panel units: 24px
between panels horizontally, 40px between panel rows, 96px
between bench sections (a walk between benches). Inside a panel,
the rhythm is the instrument rhythm: label 12px above its
instrument, instrument 20px above its printed value, value 28px
above the panel's foot rule. Whitespace in this theme is *the
dark of the worktop* — the bakelite-deep ground visible between
panels is not emptiness, it is the bench the instruments sit on,
and it is never filled with decorative tubes, gauges or clip
art. The one licensed decoration is the footer's single tube
(§6.16), and it is not decoration — it is staff.

**The centre.** The master forecast dial (§6.8) pins at the
centre panel through the hero and first bench section
(§13, beats 3–5): the room is organised around its main
instrument the way the bureau is. Everything else — the
filament rail (§6.5) down the left page edge, the cord field
(§6.2) behind the panels' top edges, the nameplate (§6.10)
bolted across the top — is fixed furniture in declared places,
so a returning visitor's hands know the room.

**Density rules.** One instrument per panel face; a panel that
needs two dials gets a divider rule and two labels, never two
unlabeled dials. Tables (§6.12) are the only dense surface, and
their density is the record's density — earned, ruled, and
printed on paper. Cards (§6.11) carry one station each. The
footer (§6.15) is the only place the room relaxes: log, tube
rack and colophon share one deep bench.

---

## 5. Full motion system

Motion in the bureau is **electrical and mechanical, in that
order**: things warm (electrical, slow attack, long decay) and
things plug, snap and sweep (mechanical, fast attack, small
settle). Nothing floats, bounces like rubber, or fades like a
presentation. Every value below is the theme's own translation
of the motion vocabulary; refused terms are refused with
in-world reasons, per the anti-fitter law.

**Named easings** (the only curves in the theme):

| Token | Curve | Character |
|---|---|---|
| `--ease-warm` | cubic-bezier(0.25, 0.6, 0.3, 1) | Filament attack: quick to glow, long to full heat |
| `--ease-cool` | cubic-bezier(0.55, 0, 0.7, 0.4) | Cooling decay: glow leaves slower than it came |
| `--ease-sweep` | cubic-bezier(0.3, 1.25, 0.45, 1) | The valve sweep: fast rise, ≤2.5% overshoot, settle |
| `--ease-snap` | cubic-bezier(0.2, 0.9, 0.3, 1.15) | The jack snap: 120ms in, one 2px bounce |
| `--ease-drape` | cubic-bezier(0.35, 0, 0.2, 1) | Cord re-drape: gravity first, swing settles after |
| `--ease-settle` | cubic-bezier(0.4, 0, 0.2, 1) | The electrical settle: a panel coming to rest |

**The shared loop.** One `requestAnimationFrame` loop drives
every scrubbed value on the page — dial sweeps, filament
frontier, cord re-drapes, parallax light — with per-channel
lerp: dials 0.14 (valves respond briskly), cords 0.1, filament
and light 0.07 (temperature lags; that lag *is* the theme).
No element runs its own scroll listener or its own loop; a
second loop in a build is a §10 failure. The loop idles at zero
cost when nothing is in motion and the tab is visible, and
pauses entirely when the tab is hidden.

**Term by term.**

- **Entrance — the warm-up** (§6.1): the page does not appear,
  it is *switched on*: filaments and lettering warm from
  `--filament-cold` to working amber over 2000ms with per-letter
  stagger, one settle flicker, hold. This is the theme's only
  load choreography, and it happens once per session (§6.1).
- **Scroll-triggered reveals — plugging in** (§6.3): a section
  does not fade up; its cord plugs in (120ms snap) and *then*
  its panel warms to lit over 600ms `--ease-warm`. Cause before
  effect, always visible: connection, then light.
- **Scroll-driven / scrubbed animation** — dials (§6.4) sweep
  scrubbed to scroll through their panel's range, with valve
  character from `--ease-sweep`; the filament frontier (§6.5)
  is scrubbed to whole-page progress.
- **Parallax** — two rates only, both physical: the brushed
  panel light (§6.9's light pass, and a faint global version in
  the hero) moves at 0.3× scroll, and cord shadows at 0.6×.
  Nothing else parallaxes; a bureau bolted to a bench does not
  drift in layers.
- **Pinned scenes** — the master dial pins (§6.8) for one bench
  section while its three readings cycle; the pin is a clamp on
  the bench, released with a settle, never a theatrical stage.
- **Masked line reveals** — *refused.* Forecasts are not
  unveiled line by line like headlines; they are printed, then
  lit. The warm-up's per-letter warming does the kinetic work
  honestly: the letters were always there, in the dark.
- **Blur-to-sharp** — *refused.* Tubes do not blur; they are
  dark, then they glow. A blurred-then-sharp forecast implies
  the bureau couldn't see its own figures.
- **Kinetic typography** — one licensed form: the hero panel
  title's letters warm at staggered temperatures (§6.1) — type
  as a row of cathodes, each at its own age. No scaling, sliding
  or rotating type anywhere.
- **Marquee** — *refused.* News does not scroll past a
  forecaster; bulletins are pinned to the board and read in
  full. The station index (§7) is a table for the same reason.
- **Counters** — station counts and sheet figures count with
  valve character (§6.4's digits): fast rise, tiny overshoot in
  the last digit only, stop dead on the sheet's figure — and
  always *from a printed starting value on the sheet*, never
  from zero (§6.17).
- **Progress indicator** — the warming filament (§6.5): the
  reader's position is a temperature frontier down the page
  edge. No bars, no percentages, no scroll percentage readouts.
- **Micro-interactions** — hover warmth (§6.6), click-to-plug
  (§6.7), jack snap (§6.3), the valve replacement (§6.16):
  every interaction is an act of the room's own craft —
  warming, patching, maintaining.
- **Hover physics** — warmth, not movement (§6.6): panels do not
  lift, tilt or lean toward the pointer. Magnetic and tilt
  effects are *refused* — a bolted panel that leans is broken.
- **Page transitions** — a power dip (§6.14): the room dips to
  standby (300ms), the new page warms in on the same curve as
  §6.1 but at half length (1000ms), ceiling 3000ms with
  watchdog.
- **Skeleton loading** — standby panels (§6.14): unpowered
  panel shells with the record's last printed values already in
  place — the bureau on standby is still readable.
- **Ambient loops** — exactly two licensed: idle filament
  breathing (§6.4, ±4% luminance, 5.7s period, hero dials only)
  and the panel light's slow pass in the hero (§6.9's mechanism
  at ambient scale). Everything else that moves is triggered.
  Valve 7's flicker (§6.16) is not an ambient loop; it is a
  fault, rationed and purposeful.
- **Reduced motion** — the bureau fully warmed and lit from
  first paint: no warm-up, no sweeps (needles rest at value),
  no plugging animation (cords rest draped, panels lit),
  filament printed at full amber, breathing and flicker off.
  Every element specifies its own variant in §6.

---

## 6. Signature elements

### 6.1 The warm-up

- **What & why.** On first load the whole hero is *switched
  on*, not shown: every filament, letter and dial begins at
  `--filament-cold` and warms to working temperature over
  ~2000ms, letters staggering like cathodes of slightly
  different ages, each flickering exactly once as it stabilises,
  the master dial (§6.8) sweeping last. It belongs because
  arrival in this room is a power-up ritual — the bureau has a
  mains switch, and the visitor throws it. It is also the
  theme's thesis in one gesture: the content was there in the
  dark the whole time; the light is a courtesy.
- **Structure.** The DOM ships complete and fully printed —
  headline, figures, dial faces with needles at rest position
  (pointing at their printed values, §6.4). The warm-up is a
  JS-armed overlay state: a `data-warming` attribute on the
  hero root drives CSS custom-property `--heat` (0→1) per
  element group; letters are wrapped in spans *by the script*
  (never in the shipped HTML, so no-JS pages have clean text),
  each span carrying `--heat-delay` from a seeded table (seed =
  character index × 37 mod 90, ms) so two builders produce the
  same stagger. Glow is rendered as `color` interpolation on
  lettering plus a `box-shadow`/`drop-shadow` halo on filament
  strokes — never as opacity on content.
- **Motion spec.** Trigger: load, first visit of the session
  only (a `sessionStorage` flag; returning visitors get the
  600ms "already warm" variant — the bureau remembers being
  on). Heat curve: `--heat` 0→1 over 2000ms `--ease-warm` per
  element, staggered 0–90ms per letter, dial faces at +400ms,
  master dial sweep begins at +1400ms (§6.4's sweep, 900ms).
  The settle flicker: one dip to 82% luminance for 60ms at each
  letter's 92% heat point — exactly one, seeded, never random.
  Any scroll or click during warm-up fast-forwards it (heat
  snaps to 1 over 150ms): the ritual never detains a reader.
- **States.** Cold (pre-arm, first paint: content printed,
  unlit, fully legible in `--paper`/`--ink`) / warming /
  flicker-settle / at working temperature / fast-forwarded.
- **Content merge.** The warm-up warms *the hero's actual
  content* — its headline letters, its dial, its figures. There
  is no separate splash or logo ritual; remove the forecast and
  there is nothing to switch on.
- **Failure fallback.** Watchdog at 2600ms: if `--heat` has not
  reached 1 (blocked script, starved frames), the attribute is
  removed and the hero renders at full working temperature —
  the "warmed-up fallback at full brightness" the original
  entry demands. No-JS: the attribute is never set; the hero
  ships lit. Content is legible at every heat value including 0
  (cold letters are `--paper-dim` on bakelite, 5.1:1 — dim,
  never invisible: the law).
- **Reduced-motion variant.** No warm-up at all: the hero
  renders at working temperature from first paint. The ritual
  is the first thing the theme surrenders, gladly.
- **Performance budget & mobile variant.** One custom-property
  animation across ≤120 letter spans + hero instruments;
  transform/opacity-free (colour and shadow only, hero-scoped,
  once per session). Budget ≤0.5ms/frame during the 2s window.
  Mobile: stagger compressed (0–45ms), halo radius halved,
  dial sweep unchanged — the ritual survives small, it does not
  get cut.
- **Choreography timeline (v2).** t=0 first paint (printed,
  cold, legible) → script arms ≤t=100ms → letters warm
  t=100–2100ms staggered → dial faces warm from t=500ms →
  settle flickers land per-letter ≈t=1900–2000ms → master dial
  sweeps t=1500–2400ms → room at working temperature t≈2400ms →
  watchdog deadline t=2600ms passes unused.
- **State matrix (v2).** *Rest:* at working temperature.
  *Hover:* §6.6 warmth, unaffected by warm-up state. *Focus:*
  any focus inside the hero fast-forwards warm-up (keyboard
  visitors never wait for a ritual). *Active:* click
  fast-forwards. *Scrolled-past:* warm-up completes regardless —
  heat is not scroll-gated. *Disabled:* n/a. *Touch:* first tap
  fast-forwards; no hover dependency.
- **Breakpoints (v2).** ≥1200px: full stagger, full halo.
  768–1199px: stagger 0–70ms. <768px: stagger 0–45ms, halo
  halved, dial sweep identical (the instrument does not shrink
  its behaviour with its panel).
- **Edge cases & failure modes (v2).** *Slow network / font
  swap mid-warm:* letter shells are sized in the fallback font
  metrics' worst case; a late Oswald load changes face, never
  layout (law 4, §3). *Session flag set but tab restored from
  bfcache:* heat state is re-read from the attribute, not
  assumed. *User returns within session:* 600ms variant.
  *Warm-up interrupted by navigation:* §6.14's transition owns
  the exit; no half-warmed page is ever cached.
- **Accessibility spec (v2).** The warm-up is decorative state
  over complete content: nothing is `aria-hidden`, reading
  order is the DOM order from t=0, and screen-reader text is
  never split by the letter spans (spans are `aria-hidden`,
  the intact headline is the accessible name via
  `aria-label` on the heading). Focus fast-forward (above)
  keeps keyboard users out of the animation entirely.
- **Tokens consumed (v2).** `--filament-cold`, `--amber`,
  `--amber-hot`, `--paper-dim`, `--ease-warm`, `--dur-warmup`
  (2000ms), `--dur-warmup-return` (600ms), `--heat` (runtime).

### 6.2 Patch-cord catenaries

- **What & why.** SVG patch cords drape between the bench's
  panels in true catenary curves — the page's structure is
  literally wired. As the visitor scrolls, a cord unplugs from
  the panel left behind and re-drapes to the panel now in view,
  with a small swing settle. It belongs because in the bureau,
  connection is a physical act done by hand; a theme whose
  sections are "linked" by implication has missed its own room.
  The cords are also the page's honest diagram: they show which
  panel feeds which — the observation panel feeds the dial
  panel, the dial panel feeds the sheet — the computation's own
  wiring, drawn.
- **Structure.** One SVG layer behind the panels' top edges
  (`position: absolute`, `aria-hidden`, `pointer-events:
  none`), one `<path>` per cord, each path computed from its
  two jack anchor points (DOM elements with `data-jack`
  attributes on panel corners) using the catenary
  approximation: a cubic Bézier whose control points drop by
  `sag = 0.18 × span + 14px` below the chord. Cord stroke:
  3.5px `--cord-red` for signal cords, 3.5px `--bakelite-deep`
  with a 1px `--aluminium-dark` edge for power cords — the two
  cord types the room owns, declared per cord in markup. Plug
  ends are 10×16px rounded rects drawn at the anchors, rotated
  to the path's end tangent. Paths are recomputed on resize
  (debounced 200ms) and on the re-drape beats only — never per
  frame; only the swing settle animates, via the shared loop.
- **Motion spec.** Trigger: scroll, at panel boundaries (the
  shared loop's scroll position crossing a panel's top edge
  −20% viewport). Re-drape: the free end lifts (path morph to
  a raised curve, 180ms `--ease-settle`), travels to the new
  anchor (260ms `--ease-drape`), the plug snaps (§6.3 owns the
  snap), then the catenary settles with two decaying swings
  (sag overshoot +6px → −3px → rest, 700ms total). One cord
  moves at a time; a fast scroll queues only the *final*
  position — intermediate panels are skipped, as a forecaster
  skipping benches would not re-patch each one.
- **States.** Draped (rest) / lifting / travelling / settling /
  parked (reduced motion or <768px vertical mode, §6.2
  breakpoints).
- **Content merge.** The cords connect *the content's own
  dependencies*: observation → computation → forecast → sheet.
  The wiring diagram is the page's information architecture;
  reordering sections re-wires the room, and §15's build order
  requires the cord map to be declared from the content graph,
  never decorated on afterwards.
- **Failure fallback.** Watchdog: if the SVG layer fails to
  initialise within 1400ms, it is removed — panels stand on the
  bench unwired and nothing is lost but the diagram. No-JS:
  no cords are drawn (they are script-built); the panels' own
  numbering (Panel 1 → Panel 2, lettered in §6.10's nav)
  carries the order. Content never depends on a cord.
- **Reduced-motion variant.** Cords rest fully draped between
  their *home* anchors (the first panel of each run) and never
  travel; the diagram is printed, static, complete.
- **Performance budget & mobile variant.** ≤6 paths, path
  morphs only on beats (never continuous); ≤0.3ms/frame during
  the 700ms settle, zero at rest. Mobile (<768px): cords become
  short vertical drops between stacked panels (sag 10px, no
  travel — the free end's anchor is always the next panel
  down); the swing settle is cut, the snap (§6.3) remains.
- **Choreography timeline (v2).** Panel boundary crossed at
  t=0 → lift 0–180ms → travel 180–440ms → plug snap at 440ms
  (§6.3, 120ms) → target panel begins warming at 500ms (§6.3)
  → swing settle 440–1140ms → cord at rest; watchdog deadline
  t=1400ms passes unused.
- **State matrix (v2).** *Rest:* draped. *Hover:* hovering a
  panel (§6.6) does not move cords — hands off the wiring until
  you click (§6.7). *Focus:* focusing a panel's jack (jacks are
  not focusable; the panel's heading is) — no cord motion on
  focus, ever: keyboard traversal must not rewire the room.
  *Active:* §6.7's click-to-plug drives a cord directly.
  *Scrolled-past:* cords rest at the last settled wiring; the
  room keeps the patch it was left in. *Disabled:* a cord to a
  panel with no data (a silent station's panel, §6.17) is drawn
  *unplugged at one end*, draped to the bench — the honest
  state, designed, not an error. *Touch:* no hover states; tap
  = §6.7.
- **Breakpoints (v2).** ≥1200px: full horizontal drapes, sag
  formula as specified. 768–1199px: sag × 0.8, ≤5 cords.
  <768px: vertical drops, no travel, as above.
- **Edge cases & failure modes (v2).** *Panels reflow after
  image load:* anchors are re-measured on `load` and on a
  ResizeObserver pass over panel boxes; cords re-drape
  instantly (no animation) to the corrected anchors — a cord
  pointing at empty bench is a §10 failure. *Very long pages:*
  cord runs are per-bench-section, never full-page spans (a
  3000px catenary is a clothesline, not a patch cord).
  *Content added dynamically (more stations):* new panels join
  the cord map at the end of their run; existing wiring is
  untouched.
- **Accessibility spec (v2).** The SVG is decorative
  (`aria-hidden="true"`); the connection it draws is duplicated
  in text — each panel's label names its feed ("FROM PANEL 2 —
  OBSERVATIONS") — so the diagram's information survives
  without the drawing. No focusable elements inside the layer.
- **Tokens consumed (v2).** `--cord-red`, `--bakelite-deep`,
  `--aluminium-dark`, `--ease-drape`, `--ease-settle`,
  `--dur-drape` (700ms), `--cord-sag` (0.18).

### 6.3 Jack-snap plugging

- **What & why.** When a section arrives in view, its cord's
  plug snaps into the panel's jack — 120ms in, one tiny bounce
  — a beat *before* the panel's content warms up. Sections do
  not reveal in this theme; they are *connected*, and then they
  light. It belongs because it is the smallest complete sentence
  the room speaks: cause (connection) visibly precedes effect
  (light), and the visitor learns in the first scroll that
  reading this page is patching this bureau.
- **Structure.** Each panel carries one jack: a 22px circular
  socket (radial-gradient `--aluminium-dark` rim, `--bakelite-deep`
  bore) at its top-right frame corner, marked `data-jack`. The
  plug is the cord path's end cap (§6.2). The snap itself is a
  transform on the plug group: translate from 14px short of the
  socket to seated, with the cord's last segment following via
  §6.2's path recompute at the snap's end. The panel's warm-up
  is a `--heat`-style property scoped to the panel (independent
  of §6.1's hero ritual), driving label and content glow from
  printed-dim to lit.
- **Motion spec.** Trigger: panel's top edge crossing 75%
  viewport height (shared loop), or §6.7's click. Snap: 120ms
  `--ease-snap`, plug travel 14px, bounce 2px at seat. Beat:
  90ms of held darkness-with-plug-seated. Panel warm: 600ms
  `--ease-warm` from printed state to lit. A panel plugs
  exactly once per page view; scrolling back up never unplugs
  it (the bureau stays patched — see edge cases).
- **States.** Unplugged (panel printed, dim-lit at 88% — the
  standing readability floor) / snapping / seated-dark (the
  90ms beat) / warming / lit.
- **Content merge.** The jack is on the panel whose content it
  lights; the snap is the section's own arrival, not a
  page-wide effect. The panel's printed label names the cord's
  source (§6.2), so the snap also *says* what was connected.
- **Failure fallback.** Watchdog per panel at 1400ms after
  first intersection: if the snap/warm sequence has not
  completed, the panel is set lit directly. No-JS and pre-arm
  state: every panel ships at the 88% printed floor *with its
  full content legible* — the warm to 100% is an enhancement
  over a readable panel, never a reveal of hidden content.
- **Reduced-motion variant.** No snap, no beat, no warm: panels
  are lit at 100% from first paint, plugs drawn seated. The
  connection is shown, not performed.
- **Performance budget & mobile variant.** One transform + one
  property ramp per panel, once per panel per view; ≤0.2ms/
  frame during the 600ms warm. Mobile: identical (the snap is
  the theme's signature beat and is cheap); only the cord
  travel feeding it simplifies (§6.2).
- **Choreography timeline (v2).** t=0 panel crosses threshold →
  snap 0–120ms → seated beat 120–210ms → panel warms
  210–810ms → panel's dial (if any) begins its sweep at 500ms
  (§6.4) → lit at 810ms; watchdog deadline t=1400ms passes
  unused.
- **State matrix (v2).** *Rest (unplugged):* printed at 88%.
  *Hover:* §6.6 warmth may raise an unplugged panel's glow but
  never plugs it — attention is not connection. *Focus:*
  focusing anything inside a panel plugs it (keyboard arrival
  is arrival). *Active:* §6.7 re-plugs on demand. *Scrolled-
  past:* stays lit. *Disabled:* a panel whose data failed
  (silent station) never plugs; its jack stays empty and its
  face carries the printed "NO REPORT — SEE SHEET" line
  (§6.17) — the unplugged state is content, not breakage.
  *Touch:* scroll and tap behave as desktop scroll and click.
- **Breakpoints (v2).** ≥1200px and 768–1199px: as specified.
  <768px: the jack moves to the panel's top-left (thumb side
  of the stack), snap travel 10px; timing unchanged.
- **Edge cases & failure modes (v2).** *Fast scroll through
  many panels:* panels plug in order, warms overlap freely,
  snaps never queue more than 2 deep — deeper panels snap
  instantly to seated and warm normally. *Scroll back up:*
  nothing unplugs (a bureau, once patched for the shift, stays
  patched; the *cord* travel of §6.2 is the only thing that
  re-patches, and it serves the panel in view). *Panel taller
  than viewport:* threshold uses the top edge only, so tall
  panels plug on arrival like any other.
- **Accessibility spec (v2).** The snap is visual only; panel
  content is in the reading order regardless of plug state.
  The plug state is not announced (it is ambience, not
  information); the information it carries — "this panel is
  live" — is duplicated by the panel's printed status line.
  Jacks are not interactive and not focusable; §6.7's plug
  action lives on the panel itself (a real button behaviour on
  the panel's label, §6.7's spec).
- **Tokens consumed (v2).** `--aluminium-dark`,
  `--bakelite-deep`, `--amber`, `--ease-snap`, `--ease-warm`,
  `--dur-snap` (120ms), `--dur-panel-warm` (600ms).

---

### 6.4 Forecast dials that sweep with warmth

- **What & why.** The bureau's instruments: analogue dials
  whose needles sweep to their values scrubbed to scroll, with
  valve character — quick rise, slight overshoot, settle — and
  the value *printed beside the dial in mono*, always, per the
  law. The dial is how the reading feels; the print is what the
  reading is. It belongs because data in this room is read off
  instruments the reader drives by reading: scroll is the hand
  on the bench, and the needle answers it.
- **Structure.** Each dial is inline SVG: a 180px face (paper
  dial card on dark panels, bakelite card on paper panels),
  engraved tick arc with the scale's min/max lettered in Oswald
  10px, a needle (SVG line + counterweight, transform-origin at
  the hub), a hub rivet, and — outside the SVG, in the panel's
  DOM — the printed value in IBM Plex Mono with its unit and
  tendency ("1013 hPa — FALLING 2 / 3H"). The needle's angle is
  a pure function of the dial's declared value and scale,
  computed in the shared loop; the printed value is static
  HTML, present with no script at all. Scales are declared per
  dial in markup (`data-min`, `data-max`, `data-value`), and
  every `data-value` must equal a figure on the Observation
  Sheet (§6.17) — §10's figure audit greps them.
- **Motion spec.** Trigger: scrubbed to scroll while the dial's
  panel crosses the viewport's middle band (panel top at 85%
  → panel bottom at 40% maps to needle 0→value), through the
  shared loop at lerp 0.14. Valve character is layered on the
  scrub: when the target value is first reached, the needle
  overshoots by ≤2.5% of scale for 180ms and settles over
  400ms (`--ease-sweep`) — once per dial per view, at the
  moment of arrival, not continuously (a needle that trembles
  at its reading forever is a faulty instrument). Total
  arrival sweep for a dial entering at rest: ~900ms. Scrolling
  back up reverses the scrub without the overshoot (the valve
  only overshoots on warm-up, as real valves do).
- **States.** At rest (needle at printed value — the shipped
  state) / scrubbing / overshoot-settle (the once-only arrival)
  / idle breathing (hero dials only: the *glow* behind the face
  breathes ±4% luminance over 5.7s; the needle never breathes).
- **Content merge.** A dial's value is its section's actual
  forecast figure — the pressure dial is in the pressure
  section and reads the sheet's pressure. Dials are never
  decorative gauges of nothing: a panel without a figure from
  the sheet does not get a dial (§9).
- **Failure fallback.** The needle ships *at value* in the
  static SVG (the transform is script-driven from that resting
  state), so no-JS, blocked script, or a starved loop all leave
  a correct instrument. Watchdog at 2000ms per dial: if the
  loop has not run the dial's arrival, the overshoot is
  cancelled and the needle is confirmed at value. The printed
  value makes even a fully failed dial honest.
- **Reduced-motion variant.** Needles rest at value; no scrub,
  no overshoot, no breathing. The dial is a printed instrument,
  complete.
- **Performance budget & mobile variant.** SVG transforms only,
  ≤8 dials per page, shared loop; ≤0.3ms/frame while scrubbing.
  Mobile: dial faces 132px, tick labels reduced to min/max/mid,
  scrub band widened (top 90% → bottom 30%) so short scrolls
  still complete the sweep; printed value unchanged in size
  (law: the print never shrinks, §3).
- **Choreography timeline (v2).** Panel plugs at t=0 (§6.3) →
  panel warm begins t=210ms → dial scrub arms at t=500ms as the
  panel enters the band → needle rises with scroll, ~70% of
  travel in the first 40% of the band → arrival: overshoot
  180ms → settle 400ms → needle at rest on the figure by
  ≈t=1400ms from plug; watchdog deadline t=2000ms passes
  unused.
- **State matrix (v2).** *Rest:* at value. *Hover:* §6.6 warms
  the panel; the needle does not respond to hover (instruments
  are not toys). *Focus:* a dial is not focusable; its printed
  value is ordinary text in the reading order. *Active:* §6.7's
  click-to-plug re-sweeps the panel's dials (the one deliberate
  replay). *Scrolled-past:* needle holds at value. *Disabled:*
  a dial for a silent station is not rendered; the panel
  carries the printed no-report line instead (§6.3, §6.17).
  *Touch:* scrub is scroll-driven, identical; no touch-specific
  needle behaviour.
- **Breakpoints (v2).** ≥1200px: 180px faces, full tick
  lettering. 768–1199px: 156px faces, minor ticks unlettered.
  <768px: 132px faces, min/max/mid only, as above.
- **Edge cases & failure modes (v2).** *Value outside scale*
  (a record storm day): the scale is declared from the sheet's
  own extremes for the season, and an out-of-scale value pins
  the needle at the end stop with the printed value in
  `--cord-red` and the line "OFF THE CARD — SEE SHEET" — the
  instrument admits its limit in print. *Long pages with many
  dials:* scrub bands are per-panel, so dials never compete.
  *Reverse scroll mid-overshoot:* the overshoot cancels and the
  scrub resumes — no stacked settles.
- **Accessibility spec (v2).** The SVG is `role="img"` with an
  aria-label repeating the printed value ("Pressure, 1013
  hectopascals, falling"); the adjacent printed value is the
  primary text and is *not* aria-hidden — the dial is the
  illustration of a figure that exists in text. Needle/scale
  contrast: needle `--cord-red` on `--paper` face 4.6:1.
- **Tokens consumed (v2).** `--paper`, `--bakelite`, `--ink`,
  `--cord-red`, `--amber`, `--ease-sweep`, `--dur-settle`
  (400ms), `--loop-lerp-dial` (0.14).

### 6.5 The warming-filament progress line

- **What & why.** A filament runs down the left page edge: dark
  red at the top, warming to full amber at the bottom, its
  bright frontier marking how far through the page — through
  the shift — the reader has come. Progress as temperature. It
  belongs because the bureau measures everything in its own
  units, and a percentage readout or a SaaS progress bar would
  be a foreign object bolted to the bench.
- **Structure.** A fixed 3px rail at the left viewport edge
  (inset 0 on ≥1200px, overlaid on the bench's edge), two
  stacked gradients: the cold track (`--filament-cold` at 55%)
  full height, and the warm frontier — a linear-gradient from
  `--amber-hot` through `--amber` to transparent — whose length
  is set by a custom property `--frontier` (0–100%) from the
  shared loop (lerp 0.07: the frontier *lags* scroll slightly,
  as temperature lags current — the lag is the meaning). At the
  frontier point sits a 7px filament bead (radial gradient,
  `--amber-hot` core). Behind the rail, a 14px soft amber halo
  at ≤8% opacity, frontier-scoped. The rail is pure decoration
  over the page's own section numbering (§6.10) — no
  information lives only in the filament.
- **Motion spec.** Trigger: scroll, scrubbed, whole-page
  progress (scrollTop / (docHeight − viewport)). Frontier
  follows at lerp 0.07; at page top the first 12% is already
  warm (the bureau was on before you arrived — the frontier
  never starts at absolute cold except during §6.1's warm-up,
  when it warms with the hero). At the footer's end the
  frontier reaches full amber and the bead parks beside the
  maintenance log (§6.15) — the shift is done, the room is
  warm.
- **States.** Warming (frontier moving) / steady (frontier at
  rest mid-page) / full (page bottom) / printed (reduced
  motion: rail at full amber, no bead).
- **Content merge.** The frontier's position is checked against
  the bench's panels as it passes them — it crosses each
  panel's jack (§6.3) at the moment that panel plugs, so the
  two progress systems (temperature and connection) agree.
  §10's gate includes the sync check: frontier at panel = panel
  lit, ±1 beat.
- **Failure fallback.** The rail is JS-driven decoration; if
  the loop never runs, the rail renders at its shipped state —
  full-length cold track with the warm gradient at 12% — which
  reads as a design detail, not a broken widget. No-JS: the
  rail is absent (it is script-built) and nothing refers to it.
- **Reduced-motion variant.** The rail prints at full amber for
  its whole length — the bureau fully warmed — with no bead and
  no frontier. Progress is then carried by §6.10's panel
  numbering alone, as it is in every state (the filament is
  never the only progress signal).
- **Performance budget & mobile variant.** One custom property
  on a fixed element; ≤0.1ms/frame. Mobile (<768px): the rail
  moves to the top edge as a 3px horizontal filament (left =
  start), halo removed, bead kept — the frontier survives the
  small bench; it is never cut entirely, because a page with no
  progress signal breaks the room's contract.
- **Choreography timeline (v2).** Page load: frontier warms
  0→12% with §6.1 (t=100–2100ms) → scroll: frontier follows at
  0.07 lerp, crossing jack 1 as panel 1 plugs → mid-page:
  frontier ≈50%, bead at the current panel's shoulder → footer:
  frontier 100%, bead parks at the log (t = arrival) →
  watchdog: none needed (a stalled frontier is indistinguishable
  from a paused reader, and the fallback state is honest).
- **State matrix (v2).** *Rest:* frontier at the reader's true
  position. *Hover/focus/active:* no response — the filament
  serves scroll only. *Scrolled-past:* scrolling up cools the
  frontier back down the rail (temperature is reversible; the
  reader going back up the page is the room cooling behind
  them — panels, once lit, stay lit: §6.3). *Disabled:* n/a.
  *Touch:* identical, driven by scroll position.
- **Breakpoints (v2).** ≥1200px: left-edge vertical rail as
  specified. 768–1199px: same rail, halo at 6%. <768px: top
  horizontal filament, as above.
- **Edge cases & failure modes (v2).** *Very short pages* (the
  404, a single-panel page): the frontier maps to the whole
  document, so a one-screen page sits at ~full warmth — correct:
  there is barely a shift to walk. *Infinite-scroll listings*
  are not built in this theme (§7 refuses them); the frontier
  assumes a finite bench. *Resize mid-page:* frontier
  recomputed from the new document height in one frame, no
  animation.
- **Accessibility spec (v2).** `aria-hidden` decoration. The
  progress it shows is duplicated by the panel numbering and
  the nav's current-panel state (§6.10), both in text. It is
  never a `progressbar` role — it is not precise, and claiming
  a percentage it does not measure would break the law.
- **Tokens consumed (v2).** `--filament-cold`, `--amber`,
  `--amber-hot`, `--loop-lerp-filament` (0.07), `--dur-warmup`
  (shared with §6.1).

### 6.6 Hover warmth

- **What & why.** Hovering a panel raises a local amber glow
  beneath and behind it, as if its tube were being driven
  harder; on leave, the glow decays slowly (~600ms), like
  cooling glass. Attention has thermal consequences in an
  analog room. It belongs because it is the theme's entire
  hover philosophy in one behaviour: the room does not move
  when you point at it — it *warms*. Panels never lift, scale,
  tilt or slide on hover (§5 refuses them); heat is the only
  answer a bolted instrument can give.
- **Structure.** A `::after` halo on each panel: radial gradient
  (`--amber` 14% → transparent 70%), inset −18px, behind the
  panel face, above the bench ground, opacity driven by a
  per-panel `--warmth` property (0→1). The halo warms the
  *bench around the panel*, not the panel's face — the
  instrument's own light comes from §6.3's plug. A fine
  filament line along the panel's bottom frame edge brightens
  with the same property, so the warmth reads as the panel's
  own tube working, not a generic drop glow.
- **Motion spec.** Trigger: pointerenter / focus-within.
  Rise: 240ms `--ease-warm` to full. Decay: 600ms
  `--ease-cool` from leave — deliberately asymmetric, because
  glass cools slower than it heats. Only one panel holds full
  warmth at a time; moving directly between panels cross-fades
  (old decays from its current value, new rises) with no gap of
  full darkness. Warmth raises the panel's dial glow (§6.4) by
  +6% luminance and nothing else — values, needles and text
  never change under hover.
- **States.** Cold (rest) / warming / warm / cooling. Focus
  produces the identical warmth (keyboard attention is
  attention), held while focus remains inside.
- **Content merge.** The warmth belongs to the panel hovered
  and to nothing else; it is centred on that panel's own tube
  position (its bottom frame edge, where the room's valves sit
  under the bench). It cannot be applied to text blocks,
  images or buttons outside panels — §11's components inherit
  it only where they live inside a panel.
- **Failure fallback.** The halo is a pseudo-element with
  opacity 0 at rest; if the script never runs, focus-within
  still drives it via pure CSS (`:focus-within` sets
  `--warmth` through a CSS-only rule), and pointer hover is
  pure CSS too — the script only arbitrates the one-warm-panel
  rule. Worst case (no CSS support for custom properties):
  panels simply don't glow; nothing else changes.
- **Reduced-motion variant.** Warmth appears and disappears
  instantly (no rise/decay ramps) at reduced peak (8% halo) —
  the state is still communicated, the physics is not
  performed.
- **Performance budget & mobile variant.** Opacity on one
  pseudo-element per panel; ≤0.1ms/frame. Mobile/touch: no
  hover exists — warmth is driven by §6.7's tap instead (a tap
  warms the panel it plugs), and the halo peak is 10% so touch
  feedback stays quiet.
- **Choreography timeline (v2).** t=0 pointer enters → halo
  0→100% by t=240ms, filament edge at full by t=300ms → hold
  while hovered → t=leave → decay 600ms `--ease-cool` → cold
  by t=leave+600ms. Focus path identical, timed from
  focus-within.
- **State matrix (v2).** *Rest:* cold. *Hover:* warm as above.
  *Focus:* warm, held. *Active:* during §6.7's click, warmth
  spikes to 120% halo for 120ms (the plug's effort) then
  returns to hover level. *Scrolled-past:* no effect.
  *Disabled:* a disabled panel (silent station) takes no
  warmth — you cannot warm an instrument that has not
  reported; its printed no-report line is its state. *Touch:*
  tap-driven, as above.
- **Breakpoints (v2).** All sizes: same behaviour; halo inset
  −12px at 768–1199px, −8px and 10% peak <768px.
- **Edge cases & failure modes (v2).** *Pointer sweeping
  across many panels:* warmth follows with per-panel decay —
  a trail of cooling panels is correct behaviour (a hand
  passing over the bench), capped at 3 simultaneously visible
  halos by the arbitration rule. *Hover during §6.1 warm-up:*
  warmth adds over the heat state without resetting it.
  *Panel partially off-screen:* halo is clipped by the panel's
  own box; no viewport-level glow ever appears.
- **Accessibility spec (v2).** Warmth is never the only signal
  of anything: hover changes no information, focus warmth
  accompanies the standard focus ring (2px `--amber` outline
  on the focused element itself, offset 2px — the ring, not
  the halo, is the focus indicator). Halo contrast is
  decorative and exempt; the focus ring on `--bakelite`
  measures 6.3:1 (§2).
- **Tokens consumed (v2).** `--amber`, `--ease-warm`,
  `--ease-cool`, `--dur-warm-rise` (240ms), `--dur-cool`
  (600ms), `--warmth` (runtime).

---

### 6.7 Click-to-plug

- **What & why.** Clicking a panel's patch label plugs a loose
  cord into it — the cord swings in with a catenary bounce, the
  jack snaps, and the panel's dials re-sweep to their values.
  The reader patches the bureau. It belongs because it is the
  theme's one deliberate replay: everything else happens by
  reading, but this happens by *hand*, and it teaches the
  room's craft better than any tour — you do not truly know a
  panel until you have connected it yourself.
- **Structure.** Each panel's instrument label (§3) is a real
  `<button>` — the panel's patch point — lettered with the
  panel name and a jack glyph (◯/● for unplugged/plugged). One
  loose cord per bench section lives draped on the bench beside
  the first panel (drawn by §6.2's layer, its free end parked
  on a bench hook). On activation, the loose cord's free end
  animates to the clicked panel's jack (§6.2's travel + §6.3's
  snap), the panel warms (§6.3's warm at double rate — a hand
  patch is eager), and its dials re-run their arrival sweep
  (§6.4, overshoot included — the one place the overshoot
  replays). Clicking a second panel moves the loose cord;
  clicking the panel it already serves re-sweeps without
  re-plugging.
- **Motion spec.** Trigger: click/tap/Enter/Space on the patch
  label. Cord lift 180ms `--ease-settle` → travel 320ms
  `--ease-drape` (longer than §6.2's scroll travel — a hand
  carries the cord) → snap 120ms `--ease-snap` → panel warm
  300ms `--ease-warm` → dials sweep from 500ms, arrival by
  ~1400ms. The previously served panel keeps its own §6.2 cord
  and stays lit; only the loose cord moves.
- **States.** Loose cord: parked / carried / plugged-to-panel-X.
  Patch label: unplugged (◯) / plugging / plugged (●) /
  re-sweeping.
- **Content merge.** The cord plugs into the panel clicked and
  re-reads *that panel's own figures*. It is not a generic
  "interact with me" affordance: panels without dials (the
  sheet, §6.12) have no patch label — you do not patch a piece
  of paper.
- **Failure fallback.** If the cord layer is absent (its
  watchdog fired, §6.2), the patch label still works: it warms
  the panel and re-sweeps the dials without the cord's travel —
  the craft degrades to the reading, never to nothing. If JS
  is absent, the label is a plain anchor to the panel's own
  section (progressive enhancement: `href="#panel-id"`).
- **Reduced-motion variant.** No travel, no snap: the loose
  cord appears at the clicked panel's jack (or not at all, if
  the layer is in its static mode), the panel lights, dials
  rest at value. The *fact* of patching is kept; the journey
  is not performed.
- **Performance budget & mobile variant.** Reuses §6.2/§6.3/
  §6.4 machinery; ≤0.3ms/frame during the 1400ms sequence.
  Mobile: the loose cord's travel becomes a vertical drop from
  the bench hook (§6.2's mobile mode), travel 220ms; the patch
  label's hit area grows to the panel's full header strip
  (44px min height) — patching with a thumb must be easier
  than patching with a mouse, not harder.
- **Choreography timeline (v2).** t=0 click → warmth spike
  (§6.6, 120ms) → lift 0–180ms → travel 180–500ms → snap
  500–620ms → seated beat 620–680ms → panel warm 680–980ms →
  dials sweep 1000–1400ms (overshoot at arrival) → label glyph
  ● set at snap; watchdog: if the sequence stalls >2000ms, all
  end states are applied directly.
- **State matrix (v2).** *Rest:* parked or plugged. *Hover:*
  the label takes §6.6 warmth; the parked cord's free end
  lifts 4px in anticipation (the only hover motion on a cord —
  a hand hovering over the bench). *Focus:* same lift + focus
  ring on the label. *Active:* the sequence above.
  *Scrolled-past:* the loose cord stays where it was left —
  scrolling never recalls it. *Disabled:* panels without dials
  render no label (not a disabled label — an absent one; the
  room does not offer switches that do nothing). *Touch:* tap
  = click; no anticipatory lift.
- **Breakpoints (v2).** ≥1200px: as specified. 768–1199px:
  travel 280ms. <768px: vertical-drop mode, full-width label
  strip, as above.
- **Edge cases & failure modes (v2).** *Rapid clicking across
  panels:* the sequence is interruptible — a new click
  re-targets the cord from its current position (no queue, no
  cord ever in two places). *Clicking during §6.1 warm-up:*
  warm-up fast-forwards first (§6.1), then the patch runs.
  *Panel with a failed dial (silent station):* no label, per
  Disabled above — the bureau does not let you patch a dead
  line for fun.
- **Accessibility spec (v2).** The label is a button with an
  accessible name that states the act and the result: "Patch
  the loose cord to the Pressure panel and re-read its dials."
  Completion is announced in the visually-hidden live region
  ("Pressure panel re-read: 1013 hectopascals, falling") —
  the *figures* are announced, not the animation. Focus ring
  per §6.6. Target ≥44px in all breakpoints (the desktop label
  is 36px tall with an extended 44px hit area via padding).
- **Tokens consumed (v2).** `--cord-red`, `--ease-drape`,
  `--ease-snap`, `--ease-settle`, `--dur-snap` (120ms),
  `--dur-panel-warm` (600ms, run at 300ms here).

### 6.8 The master forecast dial

- **What & why.** One great dial — 320px on desktop — on the
  centre panel, reading the sheet's headline figure (sea-level
  pressure, §6.17), pinned through the hero and the first bench
  section while three readings cycle beneath it: pressure,
  tendency, and the forecaster's one-line verdict in Caslon.
  The room is organised around its main instrument; the pin
  makes the organisation visible — as you walk the first bench,
  the master dial stays with you, the way the duty forecaster's
  eye keeps returning to it.
- **Structure.** §6.4's dial machinery at ceremonial scale:
  SVG face 320px, double tick ring (outer: hPa 950–1050;
  inner: the tendency arrow track), needle with counterweight,
  and beneath the face a printed readout strip — three readings
  in mono, cross-fading as the pin progresses, each *also*
  printed in full in the panel's static text below the strip
  (the strip is a highlight, never the only copy: the law).
  The pin is `position: sticky` within the centre panel's
  bench section, with the panel's frame extending as a rail —
  the dial rides its own panel, never floats over other
  content (standing rule: animated objects never cover the
  content they belong to; the dial covers nothing — its rail
  is reserved space in the layout from first paint).
- **Motion spec.** Trigger: scroll through the pinned range
  (≈180vh of bench). The dial scrubs as §6.4 (lerp 0.14) to
  the sheet's pressure on entry; through the pin, the readout
  strip cycles: reading 1 (pressure) for the first 40% of the
  range, reading 2 (tendency, with its arrow dial waking —
  a 24px sub-needle swings to FALLING) 40–75%, reading 3 (the
  verdict line warms letter by letter, §6.1's mechanism at
  reading scale) 75–100%. Release: the panel un-pins with a
  300ms `--ease-settle` settle — a clamp coming off, felt as a
  2px frame shift, nothing more.
- **States.** Approaching (dial scrubbing in) / pinned-reading
  1/2/3 / releasing / parked (past the pin: the dial rests in
  its panel at value, a normal instrument again).
- **Content merge.** The master dial reads the *page's headline
  forecast* — on a service home page, today's pressure and
  verdict; on a station page (§7), that station's headline
  figure. It is never a brand ornament: a build that pins a
  dial reading nothing has built a clock in a weather bureau.
- **Failure fallback.** Sticky positioning is the enhancement;
  without it (or with JS off) the dial sits in its panel at
  value with all three readings printed beneath in order — the
  complete static form loses only the cycling highlight.
  Watchdog: if the shared loop stalls during the pin, the
  strip freezes on the current reading (all three remain
  printed below) — never on a blank.
- **Reduced-motion variant.** No pin: the dial rests at the top
  of its panel, all readings printed, sub-needle at FALLING.
  The centre panel is simply first, as it is in the room.
- **Performance budget & mobile variant.** One sticky element,
  one SVG, cross-fades on a strip; ≤0.3ms/frame. Mobile
  (<768px): **the pin is cut** — a 320px dial pinned over a
  phone bench would crowd out the shift; the dial renders at
  232px in flow, readings stacked beneath it in print order.
  768–1199px: dial 264px, pin retained at 120vh range.
- **Choreography timeline (v2).** Hero warm-up sweeps the dial
  last (§6.1, t≈1500–2400ms) → scroll: pin engages as the
  centre panel's top reaches viewport top → reading 1 holds
  0–40% → tendency sub-needle swings at 40% (400ms
  `--ease-sweep`) → reading 2, 40–75% → verdict letters warm
  75–90% → reading 3 complete at 90% → pin releases at 100%
  with the 300ms settle; watchdog: strip freeze (above) if the
  loop stalls >2000ms.
- **State matrix (v2).** *Rest (parked):* at value, readings
  printed. *Hover:* §6.6 warmth on the centre panel; the dial
  does not respond. *Focus:* the readout strip is plain text;
  focusing it does not disturb the cycle (focus is never
  punished with motion). *Active:* the centre panel has no
  patch label — the master dial is patched by the bureau, not
  the visitor (§6.7's rule: the room's main instrument is not a
  toy). *Scrolled-past:* parked. *Disabled:* if the sheet's
  headline figure is missing (no forecast issued), the dial is
  not rendered and the centre panel carries the printed
  "NO FORECAST ISSUED — NEXT ISSUE 12:00" card (§11) — an
  empty centre panel with a printed reason, never a dead dial.
  *Touch:* pin and cycle identical on ≥768px; cut <768px.
- **Breakpoints (v2).** ≥1200px: 320px dial, 180vh pin.
  768–1199px: 264px, 120vh pin. <768px: 232px, no pin.
- **Edge cases & failure modes (v2).** *Short first bench*
  (content thinner than the pin range): the pin range is
  clamped to the section's real height; readings compress to
  pressure + verdict (tendency remains printed, uncycled) —
  the cycle never invents scroll length. *Verdict longer than
  one line:* the strip is sized for two Caslon lines at build
  time; longer verdicts are edited, not shrunk (§3 law: type
  does not shrink to fit). *Browser without sticky support:*
  the fallback above — in-flow dial, full print.
- **Accessibility spec (v2).** The dial's aria-label carries
  all three readings in order; the cycling strip is
  `aria-hidden` (a highlight of text that exists accessibly
  below it). The pin never traps focus: sticky, not fixed, and
  content flows past it in DOM order. Verdict text contrast:
  Caslon `--paper` on `--bakelite` 10.4:1 (§2).
- **Tokens consumed (v2).** `--paper`, `--bakelite`, `--ink`,
  `--cord-red`, `--amber`, `--ease-sweep`, `--ease-settle`,
  `--loop-lerp-dial` (0.14), `--dur-settle` (400ms).

### 6.9 Riveted panel image windows

- **What & why.** Photographs sit in riveted aluminium windows
  fitted into panels — a station's coastline, the bureau's own
  bench in 1954, a forecaster at the chart table. On entry, a
  slow light passes across the *brushed metal frame*, never
  across the photograph. It belongs because in this room an
  image is an instrument fitted into the panel by a person with
  a screwdriver; the light pass is the room's light catching
  the fitting as you arrive — the photograph itself is evidence
  and is never lit, filtered, warmed or performed.
- **Structure.** A figure inside the panel: aluminium frame
  (10px, brushed horizontal gradient, four rivets as §4), the
  photograph at its natural aspect (declared in markup; frames
  are built to the photograph, never cropped to a house ratio
  — the bureau does not trim evidence), and a caption strip
  *on the metal* beneath the image: Oswald instrument label
  with the photograph's provenance ("SKERARD STATION — LOOKING
  SOUTH — 1954"), plus a Caslon line if the caption needs a
  sentence. The light pass is a skewed linear-gradient overlay
  on the frame only (a pseudo-element clipped to the frame's
  border-box ring via `mask` on the padding box), animated
  across in one pass.
- **Motion spec.** Trigger: the window entering the viewport's
  middle band. Light pass: one sweep across the frame, 1400ms
  `--ease-settle`, gradient peak 18% white — exactly once per
  window per view. The photograph: no motion, no scale, no
  fade — it is printed matter; it is simply *there*, from first
  paint, at full opacity (the law applied to images: the pass
  lights the frame, the picture never waits for anything).
  Hero ambient version: in the hero only, one window's frame
  takes the slow ambient light (§5's second licensed loop,
  11s period, 8% peak).
- **States.** Unlit frame / light passing / lit-at-rest (frame
  indistinguishable from any panel frame — the pass leaves no
  permanent difference; a frame that stays shiny is a shop
  window, not a bureau fitting).
- **Content merge.** The window is *in* the panel whose content
  it evidences — the station panel carries the station's
  photograph. A photograph that belongs to no panel belongs to
  no page in this theme; there are no full-bleed hero images
  (§9).
- **Failure fallback.** Nothing to fall back from: image,
  frame and caption are static HTML/CSS. If the image file
  fails, the frame holds a printed plate: the caption plus
  "PLATE MISSING — SEE SHEET" in mono on `--paper` — the
  bureau labels an empty frame rather than leaving a broken
  hole (alt text carries the same words for AT).
- **Reduced-motion variant.** No light pass. The frame is a
  frame.
- **Performance budget & mobile variant.** One gradient pass
  per window, ≤6 windows per page, ≤0.15ms/frame during passes.
  Images: responsive `srcset`, the largest source ≤180KB
  (§14). Mobile: frame 8px, rivets 7px, caption label wraps to
  two lines on the metal (the metal grows; the photograph is
  never cropped tighter).
- **Choreography timeline (v2).** Window enters band at t=0 →
  frame light begins t=150ms → pass completes t=1550ms →
  frame at rest; the photograph was fully present from t=0
  (and from first paint). Hero ambient loop runs independently
  on its 11s period. Watchdog: none — nothing here can strand.
- **State matrix (v2).** *Rest:* printed, framed. *Hover:*
  §6.6 warms the *panel*; the window's frame takes no extra
  light (two light effects on one fitting is a showroom).
  *Focus:* if the figure is linked (station windows link to
  the station page, §7), the focus ring sits on the frame's
  outer edge, 2px `--amber`. *Active:* no press effect — you
  do not press a photograph. *Scrolled-past:* at rest.
  *Disabled:* the missing-plate state above. *Touch:* tap
  follows the link if present; no light pass is triggered by
  touch (passes are arrival events, not touch feedback).
- **Breakpoints (v2).** ≥1200px: frame 10px, full caption.
  768–1199px: frame 10px, caption label may wrap. <768px:
  frame 8px, rivets 7px, caption two lines licensed.
- **Edge cases & failure modes (v2).** *Portrait vs landscape
  plates:* frames are built per-plate from declared aspect;
  mixed galleries (§7's archive) align frames by their top
  metal edge, captions level — the bench is tidy even when the
  evidence is not uniform. *Very dark photographs:* no
  brightening, ever; the caption notes "NIGHT PLATE" when the
  bureau itself would. *Slow image load:* the frame and caption
  render immediately at final size (aspect declared), the
  plate area shows `--paper` with the caption — the window is
  never a layout shift.
- **Accessibility spec (v2).** Real `alt` text describing the
  photograph's evidence ("Skerard station anemometer mast
  against a clear sky, 1954"), never repeating the caption
  verbatim — caption is provenance, alt is content. Linked
  windows: the link's accessible name is the station name +
  "station page", not "image".
- **Tokens consumed (v2).** `--aluminium`,
  `--aluminium-dark`, `--paper`, `--ink`, `--amber`,
  `--ease-settle`, `--dur-lightpass` (1400ms).

---

### 6.10 The brass nameplate masthead & panel navigation

- **What & why.** The site's header is a nameplate bolted to
  the top of the bench: the bureau's name engraved on a brass-
  toned aluminium plate ("THE TUBE WEATHER BUREAU — EST. 1950"
  in Oswald), the shift clock in mono, and beneath it the
  panel navigation — the bench's own index, each item lettered
  like a panel label and numbered like a panel ("PANEL 3 —
  STATIONS"). It belongs because you do not browse a bureau;
  you walk to the panel you need, and the header is the plate
  above the door that tells you whose bench this is and what
  shift it is.
- **Structure.** A `<header>` on `--bakelite-deep`: the plate
  (aluminium gradient, two rivets each end, name in Oswald
  1.25rem letterspaced, the est. line in mono 11px), a mono
  shift line ("DAY SHIFT — ISSUE OF 06:00 — SHEET № 214",
  generated from the sheet, §6.17 — the header already obeys
  the law), then a `<nav>`: panel items in a horizontal strip,
  each an anchor styled as a small panel tab with its number,
  name, and live state (a filled jack ● if its panel is lit —
  the nav mirrors the bench's patch state, §6.3). The current
  panel's tab carries a drawn amber underline — not drawn*:
  set, a 2px `--amber` rule, present in the static HTML for the
  server-known current page and updated by the shared loop's
  scroll position on long pages.
- **Motion spec.** Trigger: scroll (current-panel tracking via
  the shared loop) and load. On current-panel change, the
  amber rule lifts from the old tab (fade 150ms) and sets
  under the new (fade 150ms) — lettering does not animate; a
  nameplate is engraved, and engraved things do not move. The
  shift clock is *not* a live ticking clock: it prints the
  issue time of the current sheet and updates only when a new
  sheet is issued (a bureau clock that ticks seconds is a
  station clock cosplay; §9). Jack glyphs update at the moment
  their panels plug (§6.3), instantly.
- **States.** Tabs: upcoming (plain) / current (amber rule) /
  lit (● glyph) / current+lit. Plate: constant — the plate
  never changes state, in any theme state, ever.
- **Content merge.** The nav is generated from the page's
  actual panels (same source as §6.2's cord map): add a panel,
  the nav gains a tab and the bench gains a cord. A nav item
  pointing at no panel is a §10 failure.
- **Failure fallback.** Static HTML: plate, shift line and tabs
  all render with no script; the current tab for the page is
  server-marked. The jack glyphs default to ○ in static HTML
  and fill as panels plug — a no-JS visitor sees an unpatched
  bench index over fully lit panels, which is a correct, if
  quieter, room.
- **Reduced-motion variant.** Identical (nothing here moves
  except two 150ms fades, which become instant state changes).
- **Performance budget & mobile variant.** Static header, one
  fade pair per panel change; negligible. Mobile (<768px):
  the plate shrinks (name 1rem, est. line cut — the plate is
  smaller in a smaller room), tabs become a horizontally
  snap-scrolling strip under the plate with the current tab
  scrolled into view on change; no hamburger — a bureau index
  of ≤7 panels is a strip, not a menu mystery.
- **Choreography timeline (v2).** Load: plate present from
  first paint (it is furniture, it does not warm up — the
  *hero* warms, §6.1; the plate was screwed on in 1950) → hero
  warm-up runs below it → first panel plugs: its tab's glyph
  fills (instant) → scroll: current tab changes with the
  150ms rule handover; watchdog: none (every state here is
  reachable statically).
- **State matrix (v2).** *Rest:* current tab ruled. *Hover:*
  tab warms (§6.6 at half strength — nav tabs are small
  panels). *Focus:* ring + warmth. *Active:* anchor behaviour;
  on single-page benches, activation scrolls to the panel and
  the panel plugs on arrival (§6.3). *Scrolled-past:* the
  rule follows the bench. *Disabled:* a panel with no data
  keeps its tab (you can walk to a silent station's panel —
  §6.3) but its glyph is a hollow jack with a dash (○–),
  distinct from unplugged (○): the nav admits the silence.
  *Touch:* tap = activate; strip scrolls by swipe.
- **Breakpoints (v2).** ≥1200px: full plate, tabs inline.
  768–1199px: est. line moves beside the name; tabs inline,
  labels shortened to panel names only (numbers retained —
  numbers are how the room is indexed). <768px: snap strip as
  above.
- **Edge cases & failure modes (v2).** *More than 7 panels:*
  the bench is re-benched (§7) rather than the nav wrapping —
  a wrapped nav is a bench built too long. *Long panel names:*
  labels are edited at build time to ≤16 characters (the
  engraver's constraint, §3). *Sticky header:* the header is
  NOT sticky on ≥768px (the bench's plate stays at the door;
  the filament, §6.5, is the persistent furniture) — on
  <768px it sticks at 52px height (plate mini + strip) so a
  phone visitor keeps the index, the one concession to small
  rooms.
- **Accessibility spec (v2).** `<nav aria-label="Panels">`;
  current tab carries `aria-current="true"` (updated with the
  rule). Jack glyphs are `aria-hidden`; tab names are complete
  without them ("Panel 3, Stations"). Focus ring 2px `--amber`
  on `--bakelite-deep` (5.9:1). Mobile strip: tabs remain in
  DOM order for AT regardless of scroll position.
- **Tokens consumed (v2).** `--bakelite-deep`, `--aluminium`,
  `--aluminium-dark`, `--amber`, `--paper`, `--dur-tabfade`
  (150ms).

### 6.11 Station report cards

- **What & why.** The card family: one card per reporting
  station — a small bakelite card, riveted like a panel,
  carrying the station's name in panel lettering, its headline
  figures in mono (pressure, temperature, wind — the sheet's
  own columns, §6.17), a tendency arrow, and a status stamp:
  REPORTING (green), LATE (amber), SILENT (red, with the reason
  printed). Cards are how the bureau's network appears on a
  page: not a grid of identical SaaS tiles, but a rack of
  station cards in the card index by the door.
- **Structure.** An `<article>` card: header strip with the
  station name (Oswald 1rem) and station number (mono), a
  figure table of three rows (label + mono value + tendency),
  a stamp (rotated −4°, bordered mono uppercase, colour by
  status), and a footer line: "LAST REPORT 05:40 — NEXT DUE
  06:40" in mono 12px. Cards sit in a rack grid (§4). A SILENT
  card carries no figures — its figure rows are replaced by
  the printed reason ("RELAY FAULT — ENGINEER CALLED 04:15")
  and empty ruled lines where the figures would go: the card
  shows the *shape* of the missing report, honestly.
- **Motion spec.** Trigger: rack entering view. Cards warm in
  rack order (left to right, top to bottom) at 90ms stagger —
  §6.3's panel warm at card scale (cards do not plug; they are
  paper-and-bakelite records, and the stagger is a hand passing
  along the rack). The stamp on each card *lands* as the card
  warms: scale 1.25→1 + opacity, 160ms `--ease-snap` — a stamp
  is struck, not faded. Figures never count or sweep on cards
  (cards are records, not instruments — §6.4 owns motion data).
- **States.** Unwarmed (printed, at the 88% floor, §6.3) /
  warming / filed (warm, stamp struck) / silent (never warms
  past 88% — a silent station's card stays cool to the touch,
  its stamp struck in red at full strength so the silence is
  the loudest thing on the card).
- **Content merge.** Every figure on a card is a row of the
  sheet (§6.17); the rack is the sheet, dealt into cards. Sort
  orders (by number, by tendency, by status) re-deal the same
  cards — the data never changes with the sort.
- **Failure fallback.** Cards ship printed and complete; the
  warm/stamp sequence is enhancement. No-JS: stamps are part of
  the static markup (struck at print time, so to speak) and
  cards sit at full warmth. Watchdog: rack warm completes or
  is forced by 1800ms.
- **Reduced-motion variant.** Cards at full warmth, stamps in
  place, no stagger. The rack is filed.
- **Performance budget & mobile variant.** ≤12 cards per rack
  view (pagination §11, never infinite scroll), transforms on
  stamps only; ≤0.2ms/frame during the stagger. Mobile: rack
  becomes one column; card figure rows keep their three-column
  alignment (figures must stay checkable, §3) by shrinking
  labels to their abbreviations (PRES / TEMP / WIND — the
  abbreviations are the bureau's own, printed in the sheet's
  key, §6.12).
- **Choreography timeline (v2).** Rack enters band t=0 → card
  1 warms t=100ms, stamp strikes t=560ms → cards follow at
  90ms stagger, stamps 460ms after each card's warm begins →
  rack filed by ≈t=1600ms for 12 cards; watchdog deadline
  t=1800ms.
- **State matrix (v2).** *Rest:* filed. *Hover:* §6.6 warmth
  (cards are small panels). *Focus:* a card is a link to its
  station page (§7) — focus ring on the card frame + warmth.
  *Active:* no press effect; navigation follows. *Scrolled-
  past:* filed, still. *Disabled:* SILENT cards are not links
  (there is no station page to visit — the station has not
  reported; §7) and are not focusable; their reason is their
  content. *Touch:* tap follows the link; warmth from tap per
  §6.6.
- **Breakpoints (v2).** ≥1200px: 3 per row. 768–1199px: 2 per
  row. <768px: 1 per row, abbreviated labels as above.
- **Edge cases & failure modes (v2).** *A station goes silent
  between issues:* its card changes state at the next sheet —
  figures replaced by the reason, stamp re-struck in red; the
  change is a new issue of the card, never a live mutation
  mid-view (the bureau does not alter a filed card under the
  reader's eye). *44 stations:* the rack paginates (§11);
  the home page rack shows the 12 the sheet itself headlines.
  *Duplicate tendencies:* arrows are per-station from the
  sheet; no global "all falling" shortcut is computed in the
  browser.
- **Accessibility spec (v2).** Card link's accessible name:
  "Skerard station — pressure 1013, falling; temperature 11;
  reporting." (the figures, in words, not the layout). The
  stamp is `aria-hidden` decoration of a status that also
  appears in the name and in the footer line's text. Tendency
  arrows (↑↓→) are `aria-hidden` with the word printed beside
  them in the name. Stamp colour contrast: green stamp on
  bakelite 4.8:1, red 4.6:1 — stamps are large mono text and
  pass as such.
- **Tokens consumed (v2).** `--bakelite`, `--paper`, `--ink`,
  `--panel-green`, `--amber`, `--cord-red`, `--ease-snap`,
  `--ease-warm`, `--dur-stamp` (160ms).

### 6.12 Chart-paper forecast tables

- **What & why.** The record's native furniture: ruled tables
  on chart paper — the day's figures by station and hour, the
  sheet's own grid (§6.17) — set in mono with hairline rules,
  a Caslon headnote from the forecaster, and the bureau's key
  to its abbreviations printed at the foot. Tables are where
  the theme's law is most visible: this is the print the dials
  answer to. A build that charts everything and tables nothing
  has hidden the record behind instruments.
- **Structure.** A `<table>` on a `--paper` panel (the paper
  face, §4), full bench width. Header row: Oswald labels on a
  `--paper-dim` band. Body: mono figures, right-aligned;
  row rules 1px `--paper-dim`; every sixth row a slightly
  heavier rule (the chart paper's own ruling rhythm — real
  chart paper is ruled for the hand, and the eye needs a
  landing every few rows). Tendency column uses arrows + words
  ("FALLING"). The table's *caption is its provenance*: "FROM
  OBSERVATION SHEET № 214 — ISSUED 06:00 — 42 OF 44 STATIONS"
  — the count printed *in* the table, so a screenshot of the
  table carries its own honesty. Foot: the key (PRES = mean
  sea-level pressure, hPa…) in mono 12px.
- **Motion spec.** Trigger: table panel plugs (§6.3). Rows do
  not animate in — printed matter does not perform. The one
  licensed motion: the *current hour's row* warms — a soft
  amber wash (8%) fades in over 600ms `--ease-warm` once the
  panel is lit, marking "you are here in the day" the way a
  forecaster's finger rests on the current line. Sorting (by
  column, where offered) is instant — a re-print, not a
  shuffle animation; the bureau does not juggle its records.
- **States.** Printed / current-row warmed / sorted (column
  header gains a printed ▲ and the caption gains "— AS SORTED
  BY PRESSURE" so the print admits it was rearranged).
- **Content merge.** The table *is* content — the sheet dealt
  into rows. Its figures are the same figures the dials sweep
  to and the cards carry; §10's figure audit checks all three
  printings against §6.17.
- **Failure fallback.** A table needs no fallback: static,
  complete, printable (the print stylesheet *is* this panel —
  §14). If data fails to load for a client-side table, the
  panel carries the printed line "FIGURES NOT RECEIVED — LAST
  COMPLETE SHEET № 213 (00:00) FOLLOWS" above the previous
  sheet's table: the bureau shows the older record, labelled,
  rather than an empty grid or a spinner.
- **Reduced-motion variant.** The current-row wash is present
  at full strength instantly. Nothing else changes.
- **Performance budget & mobile variant.** Zero animation
  budget beyond the wash. Tables ≤48 rows per panel (paginate
  by hour blocks, §11). Mobile (<768px): the table scrolls
  horizontally *within its paper panel* — the paper is wider
  than the phone and the bureau says so — with the station
  column sticky at the left and a `--cord-red` edge line
  marking the scrollable edge; figures never wrap, shrink
  below 0.875rem, or transpose into stacked cards (a transposed
  table cannot be checked against the sheet, §3).
- **Choreography timeline (v2).** Panel plugs t=0 → panel lit
  t≈810ms (§6.3) → current-row wash fades t=900–1500ms → table
  at rest. No watchdog required (nothing can strand), but the
  wash is cancelled if the panel is scrolled past before
  t=900ms and applied instantly on return.
- **State matrix (v2).** *Rest:* printed, current row warm.
  *Hover:* row under pointer takes a 4% ink wash (a finger
  tracing a line — the one hover a table earns), instant on,
  200ms off. *Focus:* sortable headers are buttons with rings;
  row focus follows the reading order. *Active:* sort applies
  instantly with the caption amendment above. *Scrolled-past:*
  unchanged. *Disabled:* a column with no data (a silent
  station's hours) prints "—" with the reason in the foot key,
  never zeroes. *Touch:* horizontal scroll by swipe; row wash
  from tap-drag is disabled (fingers are not pointers here).
- **Breakpoints (v2).** ≥1200px: full table, all columns.
  768–1199px: wind-gust column folds into the wind column
  ("18 G26"). <768px: horizontal scroll mode as above.
- **Edge cases & failure modes (v2).** *More stations than
  rows:* paginate, never truncate silently — the caption's
  count always states how many of how many ("STATIONS 1–24 OF
  44"). *A figure corrected after issue:* the corrected cell
  carries a superscript † and the foot prints "† CORRECTED
  09:30 — WAS 1011" — the bureau corrects in the open, in the
  table, forever (§9's anti-slop: silent edits are the one
  unforgivable sin in a record-keeping theme).
  *Extremely long station names:* names column is sized at
  build; names wrap within their cell, figures never do.
- **Accessibility spec (v2).** Real `<th scope>` headers, a
  `<caption>` carrying the provenance line, sort buttons with
  `aria-sort` on the column. The current-row wash is
  duplicated by "(current hour)" appended to that row's hour
  cell for AT. Contrast: ink on paper 12.0:1 (§2); the amber
  wash never sits under text at more than 8% (contrast after
  wash ≥11:1, measured).
- **Tokens consumed (v2).** `--paper`, `--paper-dim`, `--ink`,
  `--amber`, `--cord-red`, `--ease-warm`, `--dur-panel-warm`
  (600ms).

---

### 6.13 The requisition form

- **What & why.** The conversion section, in the room's own
  furniture: a requisition slip on chart paper, pinned to a
  bakelite panel — the form a visitor files to ask the bureau
  for something (a station's full sheet, a forecast for a
  harbour, a subscription to the morning issue). Fields are
  ruled lines, not boxes; the submit control is a brass-toned
  "FILE REQUISITION" button lettered like a panel plate; and
  confirmation is a *stamp and a number*: "FILED — REQUISITION
  № 87" struck onto the slip, where 87 is derived from the
  sheet's printed count of requisitions filed today (§6.17) —
  the visitor's number exists in the bureau's arithmetic, not
  in a toast notification.
- **Structure.** A `<form>` on the paper face of its panel:
  slip header (Oswald "REQUISITION — TO THE DUTY FORECASTER"),
  fields as label + ruled-line inputs (transparent background,
  1px `--paper-dim` bottom rule that inks to `--ink` on focus,
  Caslon input text — visitors write in the forecaster's hand,
  so to speak; mono only for the email/coordinate fields where
  precision is the point). A select for the request type,
  styled as a printed list with radio "jacks" (○/●, §6.7's
  glyphs). The confirmation replaces the form's *foot* (not
  the form): the slip stays, its fields lock to their printed
  values, and the stamp + number + expected reply line ("THE
  DUTY FORECASTER REPLIES BY THE 12:00 ISSUE") are struck at
  the slip's foot. The filed requisition is also appended to
  the visitor's own copy — a "YOUR COPY" tear-off strip at the
  slip's foot (the carbon copy; it prints, §14).
- **Motion spec.** Trigger: submit. The button warms (its
  plate takes §6.6 warmth at double strength, 240ms) → the
  slip's jack glyph beside the header plugs (●, §6.3's snap at
  form scale, 120ms) → fields lock (rules ink from
  `--paper-dim` to `--ink`, 300ms stagger 40ms per field — the
  slip being written into the record) → stamp lands at the
  foot (160ms `--ease-snap`, §6.11's stamp) → number prints.
  Total ≈1100ms. Validation errors: the offending field's rule
  turns `--cord-red` and *trembles once* — 2px, 90ms, a hand
  tapping the line — with the error in Caslon beneath it in
  the Forecaster's voice (§12): never a shake animation, never
  a red modal.
- **States.** Blank / filling (rules inking per field on
  valid entry) / filing (the sequence) / filed (locked,
  stamped, copy strip live) / error (per-field, above).
- **Content merge.** The form asks for the bureau's actual
  goods — sheets, harbour forecasts, the morning issue — and
  its confirmation number derives from the bureau's actual
  count (§6.17). A newsletter signup wearing this slip as a
  costume is §9 slop; the requisition must requisition
  something the room really issues.
- **Failure fallback.** The form is a real form: with no JS it
  submits to the server and the confirmation is a server page
  in the same slip design, number assigned server-side from
  the same count. If submission fails (network), the slip
  stays filled and editable with the printed line "NOT FILED —
  THE LINE IS DOWN. YOUR SLIP IS KEPT; FILE AGAIN." — the
  visitor's words are never discarded by a failed request
  (watchdog: the filing sequence resolves to filed or
  not-filed within 4000ms, never spins — the theme has no
  spinner, §11).
- **Reduced-motion variant.** All states apply instantly:
  submit → filed, stamped, numbered. The stamp is a state,
  not a performance.
- **Performance budget & mobile variant.** One short sequence,
  transforms on the stamp only; ≤0.2ms/frame. Mobile: the slip
  is full-panel-width; radio jacks grow to 44px targets; the
  tear-off copy strip stacks beneath the stamp instead of
  beside it.
- **Choreography timeline (v2).** t=0 submit → button warms
  0–240ms → jack plugs at 240ms (120ms snap) → fields lock
  360–660ms staggered → stamp lands 820ms (160ms) → number
  prints 980ms → copy strip rules itself (a dashed perforation
  draws, 200ms) → filed by ≈1200ms; watchdog deadline 4000ms.
- **State matrix (v2).** *Rest:* blank slip, first field's
  rule gently darker (the slip invites a hand). *Hover:*
  button warmth. *Focus:* field rule inks to `--ink` + 2px
  `--amber` focus line under the rule (the ring equivalent —
  visible on paper at 1.7:1? No: the focus line is `--cord-red`
  2px, 4.6:1 on paper, because amber cannot print on paper,
  §2 — the theme's focus indicator on light surfaces is the
  red line, on dark surfaces the amber ring, §6.6). *Active:*
  the filing sequence. *Scrolled-past:* a filed slip stays
  filed (session state). *Disabled:* while filing, the button
  disables with its lettering struck to "FILING…" — an honest
  word, not a spinner. *Touch:* identical; targets ≥44px.
- **Breakpoints (v2).** ≥1200px: slip 7 columns of the panel,
  copy strip beside the stamp. 768–1199px: slip full panel
  width. <768px: stacked copy strip, 44px jacks, as above.
- **Edge cases & failure modes (v2).** *Double submit:* the
  second activation is ignored once filing begins — one slip,
  one number; the bureau does not file duplicates (and the
  confirmation says so if a repeat arrives server-side: "№ 87
  ALREADY FILED FOR THIS SLIP"). *Very long input:* fields are
  single-line ruled inputs; the message field is a ruled
  *area* of exactly 4 lines that scrolls internally — the slip
  never grows (a requisition slip is a fixed size; that is
  its discipline). *Autofill:* honoured fully; autofilled
  fields ink their rules as if typed.
- **Accessibility spec (v2).** Real `<label>`s, errors linked
  via `aria-describedby`, the error summary (if >1) is a
  printed list at the slip's head in Caslon ("Two lines need
  attention before this can be filed:") — never a dialog.
  Confirmation is announced via live region with the number
  and reply-by line. Radio jacks are real radio inputs with
  the glyph as decoration. Contrast: all text ink-on-paper
  12.0:1; the red focus line 4.6:1.
- **Tokens consumed (v2).** `--paper`, `--paper-dim`, `--ink`,
  `--cord-red`, `--amber`, `--bakelite`, `--ease-snap`,
  `--dur-stamp` (160ms), `--dur-filing` (1100ms).

### 6.14 Power dip transitions & standby skeletons

- **What & why.** Two linked states of the room's power.
  Leaving a page, the bureau *dips*: lights drop to standby
  over 300ms, and the next page warms in on §6.1's curve at
  half length — you never teleport between rooms in a building
  with one mains supply. And while content loads, panels stand
  at *standby*: complete panel shells, frames, labels and the
  record's last printed values already in place, their
  filaments at cold red — a bureau on standby is dim, never
  blank, and never filled with grey rectangles pretending to
  be furniture.
- **Structure.** Transition: a root-level `--heat` property
  (§6.1's mechanism, page scope) driven down to 0.25 (standby
  — never 0; a dipped room still shows its printed content at
  full legibility, only its glow leaves) and back up on the
  new page. Skeleton: server- or shell-rendered panel shells
  with real labels and the *previous issue's* figures printed
  and stamped "LAST ISSUE — 00:00" in the corner; when the new
  sheet's data lands, figures are re-printed (instant text
  swap, no cross-fade — print does not fade) and the stamp is
  replaced by the new issue line, with the panel warming
  (§6.3) to mark the change.
- **Motion spec.** Transition: dip 300ms `--ease-cool` →
  navigation (instant beneath the dip) → warm-in 1000ms
  `--ease-warm` (the return-visit variant of §6.1) → total
  ceiling 3000ms with watchdog: if the new page's load stalls,
  heat restores to 1 over the *old* page's printed content
  with the line "THE LINE IS DOWN" in the nameplate's shift
  line (§6.10) — the visitor is never held in a dim room.
  Skeleton dwell: minimum 400ms (a faster load shows no
  standby at all — the panel simply arrives warm), maximum
  4000ms before the not-received fallback (§6.12's pattern)
  prints.
- **States.** Powered / dipping / standby (loading) /
  warming-in / line-down (the fallback state, printed and
  honest).
- **Content merge.** The standby figures are real figures —
  last issue's, labelled as such — so even the loading state
  obeys the law: print first. A skeleton of empty shells would
  be a room with the record removed, and is a §10 failure.
- **Failure fallback.** This element *is* the fallback system
  for page-level failures; its own failure (no JS) reduces to
  ordinary full page loads, which the bureau tolerates
  perfectly — every page ships complete (§6.1).
- **Reduced-motion variant.** No dip, no warm-in: instant
  navigation between fully lit pages. Standby panels appear
  and resolve without warming (stamps swap only).
- **Performance budget & mobile variant.** One property ramp
  per transition; standby shells are static HTML. ≤0.2ms/
  frame. Mobile: dip shortened to 200ms (small rooms dip
  fast), warm-in 800ms; skeleton identical.
- **Choreography timeline (v2).** t=0 navigation requested →
  dip 0–300ms → new page's first paint at standby (printed,
  cold) → data lands (or is already present) → warm-in
  300–1300ms → room lit; watchdog deadline t=3000ms forces
  full heat + line-down line if data has not landed.
- **State matrix (v2).** *Rest:* powered. *Hover/focus:* no
  response — power states are not interactive. *Active:*
  activating a link begins the dip at once (feedback within
  50ms — the room acknowledges the hand on the switch).
  *Scrolled-past:* n/a. *Disabled:* during the dip, links are
  inert (the room is between rooms for 300ms, and says so by
  its light). *Touch:* identical.
- **Breakpoints (v2).** All: same system; mobile timings as
  above. The standby shell layout follows each panel's own
  breakpoints (§6 per element).
- **Edge cases & failure modes (v2).** *Back/forward cache:*
  a restored page restores at full heat with its state intact
  (bfcache is the room as you left it — no re-warm). *Prefetch
  hover:* no dip on hover, ever — the dip is a commitment,
  not a tease. *Slow data on one panel only:* that panel
  stands at standby while the rest of the page is lit — power
  is per-panel in the skeleton state even though the
  transition dips the whole room (a distinction the room
  itself makes: a bench can be on while one instrument is
  still warming).
- **Accessibility spec (v2).** Route changes are announced by
  the new page's title and heading as normal (the transition
  adds no aria behaviour and must not delay AT: the new page's
  content is in the accessibility tree from first paint, at
  standby). The line-down line is a live-region politeness-
  level announcement. Focus moves to the new page's heading on
  navigation, never left in a dipped page.
- **Tokens consumed (v2).** `--filament-cold`, `--amber`,
  `--ease-cool`, `--ease-warm`, `--dur-dip` (300ms),
  `--dur-warmup-return` (600ms, run at 1000ms page scale).

### 6.15 The tube-rack footer & maintenance log

- **What & why.** The footer is the bureau's back bench: a
  rack of the room's valves drawn as a row of tube silhouettes
  (23 steady, one — Valve 7 — with its own story, §6.16), the
  colophon lettered on a plate, and the **maintenance log**: a
  mono ledger, printed on the footer's paper strip, where the
  room records its own upkeep — valve replacements, relay
  repairs, the engineer's visits. The footer is a workplace,
  not a sitemap with a logo: it is where the bureau admits
  what it costs to keep the lights warm. Sitemap links live
  here too, lettered as panel labels on the bench's edge —
  present, useful, and clearly the least interesting thing on
  the bench.
- **Structure.** A `--bakelite-deep` bench, three runs: (1)
  the tube rack — an SVG row of 24 tube outlines (envelope,
  filament line, base pins), each filament at its state
  colour, rack label "VALVE RACK — 24 FITTED"; (2) the log —
  a `--paper` strip, mono entries, newest last, each entry
  stamped "HH:MM — TEXT — INITIALS", with the log's head
  printed "MAINTENANCE LOG — BUREAU COPY" and a standing first
  entry for the day from the sheet (§6.17); (3) the colophon
  plate + sitemap labels + the bureau's postal line (a bureau
  has an address; the room is a place). Log entries from
  visitor actions (§6.16, §6.13) append *to the visitor's own
  session log* rendered beneath the bureau's printed entries,
  headed "THIS VISIT" — the bureau's copy and the visitor's
  copy are never confused (the log obeys the law too: whose
  record is whose is printed on it).
- **Motion spec.** Trigger: footer entering view. The rack
  warms left to right at 60ms stagger (the bench being powered
  for the night) over ~1500ms total; the log does not animate
  (ledgers do not perform); the colophon plate takes §6.9's
  light pass once. Nothing in the footer loops — Valve 7's
  behaviour (§6.16) is the only motion after arrival, and it
  is a fault, not an ambience.
- **States.** Rack: warming / at temperature / one-valve-fault
  (§6.16). Log: printed / appended-to (visitor entries). 
- **Content merge.** The rack's count (24) is the sheet's
  declared valve count (§6.17); the log's printed entries are
  the bureau's real maintenance fiction, consistent across
  pages (the log is one log — §10 checks its entries match
  wherever the footer appears). The footer is the same back
  bench on every page, as a workplace is.
- **Failure fallback.** All static: rack drawn lit, log
  printed, plate lettered. No-JS loses only the visitor-append
  behaviour (§6.16 degrades as specified there).
- **Reduced-motion variant.** Rack at temperature from first
  paint; no stagger, no light pass. Valve 7 rests steady (its
  fault is motion, and reduced motion retires it — §6.16).
- **Performance budget & mobile variant.** One SVG (≤8KB),
  one stagger; ≤0.15ms/frame. Mobile: rack scales to 18
  visible tubes with the label amended "24 FITTED — 18 SHOWN
  ON THIS BENCH" (the room admits the smaller bench rather
  than shrinking tubes to illegibility); log entries wrap to
  two lines with the stamp kept whole.
- **Choreography timeline (v2).** Footer enters t=0 → rack
  warm begins t=100ms, stagger 60ms → rack at temperature
  ≈t=1600ms → plate light pass t=300–1700ms → footer at rest;
  watchdog: rack forced to temperature at t=2000ms if the
  stagger stalls.
- **State matrix (v2).** *Rest:* at temperature, log printed.
  *Hover:* sitemap labels warm (§6.6, half strength); tubes
  take no hover (you do not warm a valve by pointing at it —
  §6.16's tube is the exception, and it is a button).
  *Focus:* labels ring per §6.10. *Active:* navigation.
  *Scrolled-past:* at rest. *Disabled:* a log with no visitor
  entries shows no "THIS VISIT" head — the section exists
  only when it has entries (no empty furniture). *Touch:*
  identical.
- **Breakpoints (v2).** ≥1200px: three runs side by side
  (rack 4 cols, log 5, plate 3). 768–1199px: rack + plate on
  one row, log full width beneath. <768px: stacked; 18-tube
  rule as above.
- **Edge cases & failure modes (v2).** *Long logs:* the
  bureau copy prints the day's entries plus the standing
  weekly summary line ("WEEK 46 — 3 VALVES, 1 RELAY, 0
  FORECASTS LOST"); the full log lives on the bureau page
  (§7) — the footer is the day's page of the ledger, not the
  ledger. *Visitor entries across pages:* session-persisted,
  in order, with the page named in each stamp ("— ON THE
  STATIONS PAGE"). *Clock skew:* stamps use the bureau's
  printed shift time from the sheet, not the visitor's clock —
  the log is kept in bureau time, and says so in its head.
- **Accessibility spec (v2).** The rack SVG is decorative with
  a text equivalent in its label ("Valve rack: 24 fitted, all
  at temperature" — updated by §6.16's state). The log is a
  real list in reading order. Footer nav labelled
  `aria-label="Bureau"`. Contrast per §2 pairings (paper on
  bakelite-deep 11.2:1).
- **Tokens consumed (v2).** `--bakelite-deep`, `--bakelite`,
  `--paper`, `--ink`, `--amber`, `--filament-cold`,
  `--panel-green`, `--ease-warm`, `--dur-lightpass` (1400ms).

---

### 6.16 The valve-failure easter egg (Valve 7)

- **What & why.** One tube in the footer's rack — Valve 7 —
  occasionally flickers and dims: a genuine fault in the
  room's fiction, randomised to occur a few times per visit.
  Clicking it *replaces the valve*: the tube warms steady,
  and a line is appended to the maintenance log (§6.15):
  "VALVE 7 REPLACED — 21:43 — OK". It is the theme's
  anti-slop detail made interactive — the bureau's fiction
  includes its maintenance, and the visitor is allowed to do
  some. It belongs because it is the one playful thing in a
  disciplined room, and its discipline is the point: the fault
  is rationed, the repair is recorded, and the log line is
  written in the same stamp as every real entry.
- **Structure.** Valve 7 is a real `<button>` wearing the
  seventh tube's SVG (§6.15's rack, drawn as an interactive
  overlay aligned to the rack — the rack's decorative SVG
  skips position 7, and the button carries it). Its filament
  has three render states (steady / faulting / replaced). The
  fault scheduler: a seeded timer — first fault no earlier
  than 90s into the visit and only while the footer is in or
  near the viewport; faults last 6–14s; at most 3 per visit;
  never during §6.1's warm-up or §6.14's dip (the room does
  not fault while it is switching). Replacement appends to the
  session log (§6.15) with the bureau-time stamp, and Valve 7
  is steady for the rest of the visit — a replaced valve does
  not fail again on the same shift.
- **Motion spec.** Fault: filament luminance drops to 40% with
  an irregular flicker — a seeded random-walk between 35–70%,
  steps every 90–220ms, *hard-bounded* (never below 30%, never
  strobing faster than 3 steps/second — the photosensitivity
  cap §10 audits; this is a tired valve, not a strobe). The
  tube's glass cools (halo shrinks 30%). Replacement: click →
  the tube dims fully for 400ms (the swap — the room works
  one valve short, and the rack label's count flickers to "23
  AT TEMPERATURE" for those 400ms, the log-keeper's eye for
  detail) → new filament warms 800ms `--ease-warm` → steady,
  with a slightly *brighter* first minute (new valves run
  bright: +8% halo, decaying over 60s).
- **States.** Steady / faulting (flicker + dim) / being
  replaced (dark 400ms) / replaced-steady (brighter, then
  normal). After replacement the button's name changes to
  record the fact ("Valve 7 — replaced this visit, 21:43").
- **Content merge.** The egg lives inside the room's real
  systems: the rack (§6.15), the log (§6.15), the sheet's
  valve count (§6.17). It is not a game pasted into a footer;
  it is the footer's own tube, failing the way the log says
  tubes fail ("VALVE 7 — THIRD FAULT THIS MONTH — ORDER
  SPARES" is one of the bureau copy's printed entries, so the
  visitor's fault was *foreshadowed in print* — the law
  applied to an easter egg).
- **Failure fallback.** If the scheduler never runs, Valve 7
  is a steady tube and the log's printed foreshadowing stands
  as a joke for readers only. No-JS: the button is inert and
  its label reads as part of the rack; nothing is lost.
- **Reduced-motion variant.** No faults. Valve 7 is steady all
  visit; the button instead offers the log's story directly —
  its name reads "Valve 7 — the log says it faults; it is
  resting today" and clicking appends "VALVE 7 INSPECTED —
  OK" to the session log. The fiction survives; the flicker
  does not.
- **Performance budget & mobile variant.** One timer, one
  small SVG; negligible. Mobile: the button's hit area is the
  full tube cell (44px); the rack's 18-tube mode (§6.15)
  always includes position 7 in the shown set — Valve 7 is
  never the tube cut for space.
- **Choreography timeline (v2).** Fault begins (seeded, ≥90s,
  footer near viewport) → flicker 6–14s → if unclicked, the
  valve "recovers" to a dim 70% steady (it does not heal; it
  limps) and may fault again later (≤3 total) → click during
  fault or limp: dark 400ms → warm 800ms → steady + log line
  appended at the warm's start (the engineer writes it up as
  the new valve warms) → bright minute decays by t+60s.
- **State matrix (v2).** *Rest:* steady. *Hover:* the tube
  takes a faint warmth (§6.6 at quarter strength — a hand
  near the glass) and, if faulting, the flicker continues
  (hover does not fix valves). *Focus:* ring on the tube cell;
  if faulting, focus does not pause the fault (the room does
  not perform for focus) but the button's name announces the
  fault. *Active:* replacement sequence. *Scrolled-past:*
  faults only schedule when the footer is near the viewport —
  a fault nobody can see is not scheduled (the tree falls in
  an empty forest only in philosophy). *Disabled:* after
  replacement, the button remains enabled (it can be
  inspected) but its action appends nothing further — one
  replacement per visit; a second click warms it briefly and
  the name explains ("Valve 7 — replaced 21:43; it is the new
  one"). *Touch:* tap = click.
- **Breakpoints (v2).** All sizes: same behaviour; hit area
  per above.
- **Edge cases & failure modes (v2).** *Long visits:* the 3-
  fault cap is per visit; a replaced valve never faults again
  that visit, so an all-day dashboard tab gets at most one
  story. *Multiple tabs:* each tab's bureau is its own room —
  no cross-tab state (the log is a session copy, §6.15).
  *The visitor clicks during the 400ms dark:* queued clicks
  are ignored; you cannot replace a valve twice in one swap.
  *Seed collision (fault scheduled during a page transition):*
  the scheduler defers to the next steady period.
- **Accessibility spec (v2).** The button's accessible name
  always states the valve's condition in words ("Valve 7,
  faulting — press to replace it"). Fault onset is NOT
  announced live (an ambient fault is not an alert); the
  replacement *is* announced ("Valve 7 replaced. Logged at
  21:43."). Flicker is capped as specified (≤3 steps/s, ≥30%
  floor) and fully retired under reduced motion. The tube's
  state is also printed in the rack label's text (§6.15).
- **Tokens consumed (v2).** `--amber`, `--amber-hot`,
  `--filament-cold`, `--ease-warm`, `--dur-valve-swap`
  (400ms), `--dur-valve-warm` (800ms).

### 6.17 The Observation Sheet — the bureau's one record

- **What & why.** Not an animation: the theme's constitution
  as an element. The Observation Sheet is the single declared
  document every figure on the page traces to — issued three
  times a day by the duty forecaster, printed in full on the
  sheet page (§7) and excerpted, figure for figure, wherever
  dials, cards, tables and counters appear. It belongs as a
  numbered element because in this theme the record is a piece
  of furniture: builds begin from it (§15), audits check
  against it (§10), and elements from §6.4 to §6.13 cite it the
  way instruments cite a calibration.
- **Structure.** A document object (in a real build: one JSON
  or content record, rendered everywhere, never re-typed per
  component). The canonical sheet for the worked examples in
  this expansion — **Observation Sheet № 214, issued 06:00,
  day shift, duty forecaster E. Marlowe** — declares:
  pressure at the bureau **1013 hPa**, tendency **falling
  2 hPa / 3h**; temperature now **11 °C**, forecast max
  **14 °C**, min **7 °C**; wind **south-west 18 kt, gusting
  26 kt**; rain **70% after 15:00, 6 mm expected**; stations
  **44 fitted, 42 reporting** — silent: **Kestrel Point (relay
  fault, engineer called 04:15)** and **Port Nell (operator
  ill, relief sent)**; computations run today **3** (06:00
  main, 09:30 correction, 12:00 outlook); valves fitted
  **24**; requisitions filed so far **86** (so the next filed
  is № 87, §6.13); issues at **06:00 / 12:00 / 18:00**.
  Rendering: the sheet page prints it entire (Caslon prose
  headnote — the forecaster's summary paragraph — above the
  mono table of figures); excerpts elsewhere are *generated
  from the same record*, and any figure a builder types by
  hand into a component is a §10 failure on sight.
- **Motion spec.** None of its own — the sheet is print. Its
  figures are what other elements' motions mean: the master
  dial's scrub target (1013), the counters' destinations (42
  of 44), the form's next number (87). When a new issue lands
  (12:00), changed figures re-print instantly and their dials
  re-sweep once (§6.4's arrival, at half overshoot — a
  correction, not a first reading) with the sheet's issue line
  updating everywhere in the same frame.
- **States.** Current issue / superseded (kept, stamped
  "SUPERSEDED BY № 215 — 12:00", and still readable — the
  bureau does not unpublish a forecast it made; §9).
- **Content merge.** Total: the sheet *is* the content's
  source. Every other element in §6 is a view of it or an act
  upon it.
- **Failure fallback.** If the record fails to load, the site
  renders the last complete sheet, stamped with its issue time
  and the line of §6.12 ("LAST COMPLETE SHEET № 213 (00:00)
  FOLLOWS") — an old, honest record over a new, empty one,
  always.
- **Reduced-motion variant.** Identical (print). Re-issues
  swap figures without dial re-sweeps.
- **Performance budget & mobile variant.** One record, cached
  with the page; its full rendering is §6.12's table budget.
  Mobile: the sheet page prints entire regardless of screen —
  the record is never abridged for small benches (its table
  scrolls per §6.12).
- **Choreography timeline (v2).** Issue (06:00) → sheet
  printed → hero dial sweeps to 1013 (§6.1/§6.8) → cards dealt
  from it (§6.11) → 09:30 correction computation → any
  corrected figure re-prints with its † (§6.12) → 12:00 issue
  № 215 supersedes; dials re-sweep once; the old sheet is
  stamped, kept, and linked from the new one's head ("№ 214
  remains on file").
- **State matrix (v2).** *Rest:* current. *Hover/focus/
  active:* the sheet is a document; its page's elements carry
  their own states. *Scrolled-past:* n/a. *Disabled:* a sheet
  that cannot be issued (no observations) is itself the news:
  the centre panel carries §6.8's no-forecast card and the
  sheet page prints the reason — the record records its own
  absence. *Touch:* n/a.
- **Breakpoints (v2).** The sheet's table follows §6.12's
  breakpoints; its headnote is Caslon at §3 sizes at all
  widths.
- **Edge cases & failure modes (v2).** *Two issues with the
  same number* (a bureau error): numbers are issued by the
  record system, never by page templates. *A figure corrected
  twice:* both † entries print, oldest first — the audit
  trail is append-only. *A station reports late:* the count
  re-prints 43 of 44 with the late station's card re-dealt at
  the next issue, not mutated mid-issue (§6.11).
- **Accessibility spec (v2).** The sheet page is a document:
  heading order, table semantics (§6.12), and the headnote in
  prose — the record must be fully usable by a reader who
  never sees a dial, which is precisely the law restated for
  AT.
- **Tokens consumed (v2).** None directly (it is content, not
  chrome); its renderings consume §6.12's tokens.

### 6.18 The off-air panel (404 & empty states)

- **What & why.** The bureau's dead channel: a panel with its
  jack empty, its dial at rest on zero — no, not zero: at rest
  on its *stop pin*, needle parked where an unpowered
  instrument parks — its face printed "OFF AIR — THIS PANEL
  HAS NO SHEET", and beneath, in Caslon, the forecaster's
  directions back to the lit benches (links lettered as panel
  labels). It belongs because a record-keeping room handles
  absence the way it handles silence (§6.17): named, printed,
  and routed around — never a void with a mascot.
- **Structure.** One bakelite panel, centred on the bench:
  unplugged jack (§6.3's socket, empty), a dial face with the
  needle parked at its stop (SVG, static), the printed OFF AIR
  line in Oswald, the Caslon directions paragraph, three panel-
  label links (the forecast, the stations, the bureau), and —
  at the panel's foot — a log line in mono: "PANEL REQUESTED —
  NOT FITTED — LOGGED", because even a wrong turning is
  entered in the book (§6.15's visitor copy gains the entry in
  session). The same panel furniture serves empty states
  (a station with no archive, a search with no result) with
  its printed line changed: "NO SHEETS ON FILE FOR THIS
  STATION — THE BUREAU KEEPS WHAT IT HAS, AND SAYS WHAT IT
  HASN'T."
- **Motion spec.** Almost none, by design: the panel is
  unpowered. The single licensed beat: the parked needle
  *settles* once on arrival — a 3° drop onto the stop pin over
  500ms `--ease-settle`, the last of the room's power leaving
  the instrument — and the empty jack's bore catches §6.9's
  frame light once. No warm-up (§6.1 does not run: there is
  nothing to switch on), no filament progress past 12% (§6.5's
  frontier stops where the bench ends). Choreography specified
  as *nearly none* is a specification, and §10 checks it.
- **States.** Off air (only state). The links within it are
  fully live and warm on hover (§6.6) — the way back is lit
  even though the panel is not.
- **Content merge.** The panel names what was asked for (the
  requested path, printed in mono in the log line's second
  line) — the absence is specific, not generic.
- **Failure fallback.** It is one. Static by construction.
- **Reduced-motion variant.** Identical, minus the needle's
  settle (it ships parked).
- **Performance budget & mobile variant.** Static; the needle
  settle is one transform. Mobile: the panel is full-width;
  links stack as full-width label rows (44px).
- **Choreography timeline (v2).** t=0 paint (panel printed,
  needle 3° high) → settle 200–700ms → rest. Watchdog: none —
  a stalled settle leaves the needle 3° high on a printed
  panel, which no visitor can detect and no content depends
  on; the spec says so rather than pretending otherwise.
- **State matrix (v2).** *Rest:* off air. *Hover:* links warm.
  *Focus:* links ring normally. *Active:* navigation (with
  §6.14's dip — leaving a dead panel still dips the room; the
  mains is the mains). *Scrolled-past:* n/a (single panel).
  *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: panel 8 columns centred.
  768–1199px: 6 of 8. <768px: full width, stacked links.
- **Edge cases & failure modes (v2).** *A 404 for a page that
  exists but whose sheet failed:* §6.17's last-complete-sheet
  rule applies instead — off-air is only for what was never
  fitted. *Search with results:* not this panel (results are
  a table, §6.12's furniture). *Repeated wrong turnings:* the
  visitor log gains one entry per distinct path, not per hit
  — the book records events, not traffic.
- **Accessibility spec (v2).** The page's `<h1>` is the OFF AIR
  line itself (the state is the heading, not a decoration
  above one). The requested path is text. Links have full
  names ("Today's forecast", not "Panel 1"). HTTP status is a
  real 404 — the bureau does not soft-404 its dead channels.
- **Tokens consumed (v2).** `--bakelite`, `--paper`, `--ink`,
  `--cord-red`, `--aluminium-dark`, `--ease-settle`.

---

## 7. Page application map

| Page | How the bureau plays it |
|---|---|
| **Home — the day bench** | Nameplate (§6.10), warm-up hero (§6.1) with the master dial (§6.8) reading today's pressure, the forecaster's headnote in Caslon, the first bench of station cards (§6.11, the sheet's headline 12), the day table (§6.12), the requisition slip (§6.13), footer (§6.15). The home page is one shift, walked top to bottom (§13). |
| **Forecast / sheet page** | Paper-forward (ratio inverted, §2): the Observation Sheet entire (§6.17) — headnote, full table (§6.12), corrections with their † trail, superseded issues linked and readable. Dials appear once, at the head, as the sheet's summary instruments. This is the page screenshots of the site should look like: the record, not the room's mood. |
| **Stations index** | A table (§6.12 furniture), never a card wall: 44 rows, counts in the caption, silent stations in place with reasons. Cards (§6.11) are for headline racks; an index is a record and is printed as one. |
| **Station page** | The station as a small bench: its own dial trio (§6.4) reading its sheet rows, its photograph in a riveted window (§6.9), its archive as past sheets (tables), its silence — if it comes — announced by §6.3's unplugged panel state, never by a missing page. |
| **The bureau (about)** | The room itself: the bench photograph (§6.9), the forecasters named with their shifts (people, printed — no avatars, §11), the method in Caslon (how a forecast is made here, step by step, with the ENIAC honesty of §1: what the valves do and what the humans do), the full maintenance log (§6.15's ledger, whole). |
| **Requisition (contact / conversion)** | §6.13's slip as the whole page's centre, with the bureau's postal address and issue times printed beside it — a conversion page that also works with the form removed, because some visitors write letters. |
| **Archive (past sheets)** | Issues as a table by date; each issue's sheet entire; corrections preserved. The archive is the theme's proof of §9's first law: nothing the bureau published is ever unpublished. |
| **Search** | Results as a table (sheet, station, date columns) — search serves the record, so it wears the record's furniture. No result: §6.18's empty-state panel. |
| **404** | §6.18's off-air panel, real 404 status. |
| **Checkout / payment** | *Refused a themed treatment.* Money leaves the room: payment is handed to a plain, paper-white, unstyled-by-the-theme page with the bureau's name and the requisition number printed at its head — the bureau takes your card the way it takes a telegram, by handing you to the office next door, and says so in one Caslon line. (A themed checkout in a fiction this strong would cost more trust than it earns; §9.) |

**Cross-page rules.** The nameplate, filament and footer are
identical furniture on every page (same bench, same back
bench). The warm-up runs once per session (§6.1); subsequent
pages arrive via §6.14's dip at working temperature. Every
page's figures generate from the current sheet (§6.17) — a
page built from a stale copy of the figures is a §10 failure
even if the numbers happen to match, because the *route* was
wrong.

---

## 8. Worked examples

All three examples run on Observation Sheet № 214 (§6.17).
Every figure below is the sheet's; the arithmetic is the
sheet's own.

### 8.1 The hero — "The morning issue" (home page)

**The build.** Nameplate (§6.10) across the top, shift line
reading "DAY SHIFT — ISSUE OF 06:00 — SHEET № 214". Below it,
the hero panel: bakelite face, 8 columns; its label on the
metal reads "PANEL 1 — THE MORNING ISSUE". Inside: the panel
title in Oswald — "FAIR BY MORNING, RAIN BY TEA" (the
forecaster's headline, written by a human, in Caslon's
register but Oswald's lettering because it is the panel's
name) — the Caslon headnote (three sentences: what the night
brought, what the day will do, when the rain arrives), and at
the panel's right, the master dial (§6.8) at 320px with its
printed value beside it: **1013 hPa — FALLING 2 / 3H**. The
4-column rail beside the hero carries the day in four printed
figures (mono): MAX 14° · MIN 7° · WIND SW 18 G26 · RAIN 70%
AFTER 15:00. The first cord (§6.2) drapes from the hero
panel's jack down to Panel 2.

**Scroll timeline.** t=0 (load): page paints printed and cold
→ warm-up (§6.1) runs t=100–2100ms, letters staggering, dial
faces warming at t=500ms → master dial sweeps t=1500–2400ms,
overshoot at 1013 +2.5% of scale (≈1015.5 on the card) for
180ms, settles to **1013** → filament frontier (§6.5) reaches
12% with the hero → visitor scrolls: the master dial pins
(§6.8) as the first bench arrives; reading strip holds
PRESSURE 1013 through the pin's first 40% → at 40% the
tendency sub-needle swings to FALLING (400ms) → at 75% the
verdict line warms letter by letter: "The front is in no
hurry. Neither are we." → pin releases at the bench's end with
the 300ms settle. Nothing in the hero ever hid: at every
millisecond above, a screenshot shows a complete, legible
panel — cold, warming, or lit.

### 8.2 Mid-page — the stations bench (home page, Panel 3)

**The build.** After the day table (Panel 2, §6.12, the sheet
by hour), Panel 3 is the rack: label "PANEL 3 — STATIONS
REPORTING", headnote in Caslon ("Forty-two of the bureau's
forty-four stations reported by 06:00. The two that did not
are named on their cards."), and the rack of 12 headline cards
(§6.11). Card 1: SKERARD — PRES 1013 ↓ FALLING · TEMP 11° ·
WIND SW 18 — stamp REPORTING, footer "LAST REPORT 05:40 —
NEXT DUE 06:40". Card 9 is KESTREL POINT: no figures, ruled
empty lines, the printed reason "RELAY FAULT — ENGINEER
CALLED 04:15", stamp SILENT in red. Card 11 is PORT NELL:
"OPERATOR ILL — RELIEF SENT 05:10", stamp SILENT. The counts
reconcile in print on the panel itself: 10 reporting + 2
silent = the 12 dealt, and the caption under the rack reads
"12 OF 44 STATIONS — FULL INDEX ON THE STATIONS PAGE; 42 OF
44 REPORTING BUREAU-WIDE", tying the rack to the sheet's 42
without pretending the rack *is* the 44.

**Scroll timeline.** Panel 3's top crosses 75% viewport →
its cord's plug snaps (§6.3, 120ms) → 90ms beat → panel warms
210–810ms → cards warm in rack order from t=300ms at 90ms
stagger, stamps striking 460ms after each card begins (the
SILENT stamps strike at full red strength on cards that warm
only to 88% — the silence is filed as firmly as the reports)
→ the filament frontier crosses the panel's jack as it lights
(§6.5's sync) → rack filed by ≈t=1900ms. Scroll back up:
nothing unplugs, nothing un-stamps; the rack stays filed.

### 8.3 Conversion — filing a requisition (requisition page)

**The build.** The slip (§6.13) centred on its panel, head
"REQUISITION — TO THE DUTY FORECASTER". The visitor wants the
harbour forecast for Skerard by email each morning. Fields:
NAME (Caslon input), EMAIL (mono), REQUEST (radio jacks:
FULL SHEET / HARBOUR FORECAST / MORNING ISSUE — HARBOUR
FORECAST chosen), STATION (select: SKERARD), NOTE (ruled
area, 4 lines: "For the ferry office — we sail on the 07:10
regardless, but the passengers ask."). Beside the panel, in
Caslon, the terms in plain sentences: what is issued, when
(06:00 / 12:00 / 18:00), what it costs if anything, and the
postal alternative.

**Submit timeline.** t=0 FILE REQUISITION pressed → button
warms 0–240ms → header jack plugs at 240ms → fields lock
360–660ms, rules inking field by field (the note's text stays
exactly as written — filing never edits the visitor) → stamp
lands at 820ms: "FILED" → number prints at 980ms:
**REQUISITION № 87** — the sheet's 86 filed today, plus this
one; the arithmetic is printed under the number in mono 12px
("№ 87 OF TODAY — 86 FILED BEFORE YOURS") so the visitor can
see the number was derived, not generated → the reply line:
"THE DUTY FORECASTER REPLIES BY THE 12:00 ISSUE" → the YOUR
COPY tear-off rules itself at the slip's foot (perforation
draws, 200ms) → in the footer, the visitor's session log
(§6.15) gains "REQUISITION № 87 FILED — 06:41 — HARBOUR
FORECAST, SKERARD" — one act, three printings, all agreeing:
slip, copy, log. If the line is down: the slip keeps every
word, prints "NOT FILED — THE LINE IS DOWN", and no number is
issued — a number is only ever struck on a filed slip.

---

## 9. Anti-slop — what makes THIS theme look cheap

1. **Steampunk cosplay.** Gears, brass pipes, Victorian
   flourishes, sepia vignettes. The bureau is 1950s
   *institutional* — brushed aluminium, bakelite, painted
   lettering — not a fantasy airship. *Cure:* every object in
   the room must be justifiable as something a 1950s bureau
   owned and used; if it would look at home in a costume, it
   is cut.
2. **Glow that hides figures.** Amber washes over text, dials
   whose values exist only as needle positions, content that
   "reveals" by brightening from invisible. This breaks the
   law and is the theme's characteristic failure. *Cure:*
   print first (§6.17); every dial audited for its printed
   twin (§10).
3. **Flicker everywhere.** Random flickers on every tube and
   letter because "analog = flickery". A bureau where
   everything flickers is a bureau with a mains fault. *Cure:*
   flicker is licensed in exactly two places — §6.1's single
   settle flicker per letter, §6.16's Valve 7 — and §10 greps
   for others.
4. **Neon amber.** Amber pushed bright and saturated until the
   room reads as a warning sign or a crypto dashboard in a
   brown coat. *Cure:* amber is `--amber` and `--amber-hot`
   only, at the §2 ratios (~7% of the page, as light). If a
   screenshot's amber area exceeds its paper area, the build
   has failed §2.
5. **Dials that read nothing.** Decorative gauges with random
   or lorem values, needles at photogenic angles. *Cure:*
   every dial's `data-value` greps to the sheet (§6.4, §10);
   a panel with no figure gets no dial.
6. **Silent data edits.** Figures quietly updated, a silent
   station quietly dropped from the count, yesterday's wrong
   forecast quietly replaced. In a record-keeping theme this
   is not slop, it is fraud. *Cure:* corrections carry † and
   print their history (§6.12); superseded sheets stay
   readable (§6.17); silent stations are named (§6.11).
7. **The mascot forecaster.** A cartoon man in shirtsleeves
   giving a thumbs-up. The forecaster is a voice (§12) and a
   signature, never a character illustration. *Cure:* people
   appear in photographs (§6.9) and bylines, or not at all.
8. **Skeuomorphic clutter.** Panels crowded with dummy
   switches, dummy screws inside panels, gauges behind glass
   with reflections — hardware as wallpaper. *Cure:* rivets
   live on frames only (§4); every switch on a panel must
   switch something (§6.7's label is the model: it works).
9. **Full-bleed weather photography.** A dramatic storm photo
   as a hero background with the dial floating over it. The
   bureau's images are evidence in frames (§6.9), never
   wallpaper; weather drama belongs to the figures. *Cure:*
   no background images anywhere; the bench is the ground.
10. **SaaS furniture in costume.** A toast notification with a
    rivet drawn on it; a modal with a bakelite border; a
    spinner styled as a rotating dial. Costumed components are
    worse than plain ones because they confess the fiction is
    a skin. *Cure:* §11 — components are either genuinely of
    the room (log entries, stamps, slips) or plainly
    un-themed (the checkout rule, §7).
11. **Ticking clocks and live counters.** A seconds-ticking
    clock, numbers counting up on view for theatre. The
    bureau's time is issue time (06:00 / 12:00 / 18:00) and
    its counters stop dead on the sheet's figures (§6.4).
    *Cure:* anything that moves continuously must be one of
    §5's two licensed ambient loops.
12. **Warmth as the only state.** Hover/focus/active all
    expressed as "a bit more glow" until states are
    indistinguishable. *Cure:* states differ in kind, not
    degree — plugged vs unplugged (glyph), filed vs unfiled
    (stamp), reporting vs silent (printed word) — with warmth
    as accompaniment only (§6 state matrices).

---

## 10. Quality gate

Blocking checks — every one must pass before this theme ships
in a build. The gate is signed by someone other than the
builder (§15).

1. **Figure audit.** Every figure on every page greps to the
   current Observation Sheet (§6.17): dial `data-value`s,
   card figures, table cells, counters, the form's derived
   number. One unmatched figure fails the gate.
2. **Print-first audit.** With JS disabled and with all
   animations frozen at t=0, every page is complete and
   legible: dials at value with printed twins, panels lit at
   their floors, the sheet entire. (The law, tested.)
3. **Watchdog drill.** Block the shared loop: warm-up forces
   at 2600ms (§6.1), panels light by 1400ms (§6.3), dials
   confirm at value by 2000ms (§6.4), transitions restore by
   3000ms (§6.14). Any content still waiting at deadline +1ms
   fails.
4. **Flicker census.** Exactly two flicker sources exist in
   the build (§6.1 settle, §6.16 Valve 7); Valve 7's flicker
   respects its caps (≤3 steps/s, ≥30% floor). A third flicker
   fails.
5. **Ambient census.** Exactly two ambient loops (§5). Any
   other continuous motion fails.
6. **Filament sync check.** The frontier (§6.5) crosses each
   panel's jack within one beat of that panel plugging (§6.3)
   at three scroll speeds (slow, steady, fast).
7. **Contrast audit.** Every text pairing measures at or
   above its §2 table value; amber never appears as text on
   paper; the red focus line on paper and amber ring on
   bakelite are both present and correct per surface (§6.13).
8. **Reduced-motion pass.** With `prefers-reduced-motion`:
   the bureau renders fully warmed, needles at value, cords
   draped, Valve 7 retired, transitions instant — and loses
   no content, state or figure.
9. **One-loop check.** Exactly one rAF loop drives all
   scrubbed values (§5); no element owns a scroll listener.
10. **Silent-station honesty.** The count of reporting
    stations, everywhere it appears, names or links the
    silent ones with reasons; no page shows "44 reporting"
    or drops a silent station from its denominator.
11. **Correction trail.** Issue a test correction: the †
    prints with its history (§6.12), the superseded sheet
    remains readable (§6.17), dials re-sweep once at half
    overshoot.
12. **Log consistency.** The maintenance log's bureau copy is
    identical on every page; a valve replacement and a filed
    requisition append correctly to the visitor copy with
    bureau-time stamps (§6.15, §6.16, §6.13).
13. **Performance budget.** §14's budget holds on a mid-range
    Android over 4G: LCP ≤2.5s, per-frame animation cost
    ≤1.6ms, no layout shift from the warm-up (CLS 0 from
    motion systems; letter shells are final at first paint).
14. **The screenshot test.** A screenshot at any scroll
    position, at any animation moment, shows a complete,
    legible, plausible bureau — no half-lit panels hiding
    content, no needles mid-sweep without printed values, no
    frame that could be mistaken for a broken page. If a
    screenshot needs the caption "wait for the animation",
    the build fails.

---

## 11. Component inventory

Every component a real site in this theme needs, with its
themed treatment. The inventory's rule: a component is either
a real object of the room, or it is refused and replaced by
one — nothing wears the room as a costume (§9.10).

| Component | Treatment in this theme |
|---|---|
| **Primary button** | A panel plate: aluminium frame, Oswald lettering, warms on hover (§6.6), plugs its jack glyph on active. Used for the one main act per panel ("FILE REQUISITION", §6.13). |
| **Secondary button** | A lettered label on the bench (no plate): Oswald, amber rule on hover. For bench-level acts ("SEE THE FULL SHEET"). |
| **Text link** | Caslon, underlined with the `--paper-dim` rule that inks to `--cord-red` on hover — a pencil line becoming a cord. |
| **Text input** | A ruled line on paper (§6.13): label above in Oswald, rule inks on focus, red focus line beneath (§6.13's accessibility spec). |
| **Select** | A printed list box on the slip: the chosen station shows with its number; the open list is a paper card with ruled rows — no custom dropdown theatrics. |
| **Radio / checkbox** | Jack glyphs (○/●) as real inputs (§6.13): to choose is to plug. Checkboxes in lists (station filters) are pencil ticks in mono squares — the checklist hand, borrowed honestly. |
| **Table** | §6.12 entire: chart paper, mono figures, provenance caption, correction †s. |
| **Card** | §6.11 entire: the station card. There is no generic card; a card in this theme is a station card or a sheet excerpt card (same furniture, table rows instead of figure rows). |
| **Badge / status** | A stamp (§6.11): bordered mono uppercase, struck, colour by state. Statuses that are not worth a stamp do not get badges. |
| **Alert** | A printed warning card on the bench: paper card, red rule, Caslon text, the figures it concerns in mono ("GALE WARNING — SW 34 KT AFTER 18:00 — FROM SHEET № 214"). Never a banner that slides, never dismissible into amnesia — it stays while its sheet is current and is filed with it. |
| **Modal / dialog** | *Refused.* A bureau does not dim the room to show you a box. What modals usually carry goes to: confirmations → the log (§6.15) and the slip's stamp (§6.13); detail → a panel on a page (§7); warnings → the alert card above. |
| **Toast** | *Refused.* Nothing in a bureau appears at the corner and vanishes. Every outcome is written somewhere permanent: filed (stamp), logged (log), or printed (sheet). |
| **Spinner / loader** | *Refused.* Standby is §6.14: printed shells with last issue's figures. A bureau that cannot show you the last record while it fetches the new one has lost the record. |
| **Tabs** | Panel switches: a row of small bakelite toggles lettered in Oswald, switching which instrument a panel shows (PRESSURE / TEMPERATURE / WIND on a station panel) — the switch physically re-labels the panel and its dial re-reads (§6.4). Tabs that switch *pages of marketing copy* are not built; benches have panels, not tabs. |
| **Accordion** | The valve list: the bureau page's (§7) rack inventory as ruled rows that open to each valve's log history — an accordion whose content is a ledger, opened by its stamp line. Generic FAQ accordions wear the ruled-row furniture plainly (paper rows, Oswald heads) without pretending to be hardware. |
| **Pagination** | Shift pages: "SHEETS 1–12 OF 44 — EARLIER / LATER" as panel labels at the table's foot (§6.12). Numbered, finite, printed — the archive has edges and says so. |
| **Breadcrumb** | The bench path in the nameplate's second line: "BUREAU › STATIONS › SKERARD" in mono — the walk, printed. Present on sub-pages only; the home bench needs no path to itself. |
| **Search input** | A requisition-line field (§6.13 furniture) labelled "ASK THE INDEX" — search is a request to the bureau, and results are a table (§7). |
| **Tooltip** | *Refused as hover bubbles.* Instrument explanations live in the sheet's key (§6.12) and in Caslon headnotes. A definition that matters is printed; one that doesn't is cut. (Native `title` on genuinely terse glyphs — the tendency arrows carry their word beside them instead, §6.11.) |
| **Progress bar** | *Refused* — progress is the filament (§6.5) for pages and the stamp sequence for acts (§6.13). |
| **Avatar** | *Refused.* Forecasters are names, shifts and signatures (§7); the bureau does not draw its staff. |
| **Toggle switch** | A real one, sparingly: the bench's only literal switch is the "BUREAU TIME / YOUR TIME" toggle on the sheet page — a bakelite lever that re-prints the table's times. One switch that switches something real (§9.8). |
| **File upload** | A requisition attachment line (§6.13): "ATTACH A CHART — the bureau accepts paper of any size" with a plain file input styled as a slip line; the filed copy lists the attachment by name and size in mono. |
| **Empty state** | §6.18's panel furniture with its printed line. |
| **Error state (page)** | §6.18. **Error state (field)** | §6.13's red rule + Caslon line. **Error state (data)** | §6.12's not-received line over the last complete sheet. |
| **Footer** | §6.15 entire. **Header** | §6.10 entire. |

---

## 12. Content & copywriting voice

Two registers, kept apart by §3's type laws — the registers
*are* the fonts.

**The Panel register** (Oswald, uppercase, the room speaking
as hardware). Names, labels, orders, stamps. Terse to the
point of bluntness; no adjectives; numbers welcome. The panel
never explains and never apologises.

- ✓ "PANEL 3 — STATIONS REPORTING" · "FILE REQUISITION" ·
  "ISSUED 06:00" · "OFF AIR — THIS PANEL HAS NO SHEET"
- ✗ "Welcome to our stations dashboard!" · "Oops! Something
  went wrong" · "Your forecast is loading…"

**The Forecaster register** (Libre Caslon, sentence case, a
person writing). Headnotes, explanations, errors, empty
states, the verdict. Quietly confident, specific, dry at the
edges; writes what is known, what is not, and what happens
next — in that order. Never sells, never exclaims.

- ✓ "Forty-two of the bureau's forty-four stations reported
  by 06:00. Kestrel Point is silent — a relay fault, engineer
  called at 04:15. Its figures will be estimated from Skerard
  and marked as such."
- ✓ (error) "That line needs a station before the bureau can
  file it. Choose one from the list, or write 'any' and the
  duty forecaster will choose."
- ✗ "We're so excited to bring you today's weather!" ·
  "Something went wrong — please try again." (what went
  wrong? the forecaster says) · "No results found." (the
  bureau says what it *does* have, §6.18).

**Headline style.** The day's headline is a forecast in
words, written by the forecaster, in the panel register's
lettering (§8.1): "FAIR BY MORNING, RAIN BY TEA" — a claim
with times in it, checkable by evening. Headlines that cannot
be checked ("A DAY OF WEATHER AHEAD") are not headlines, they
are filler, and §9's spirit applies.

**Numbers in copy.** Always mono, always from the sheet,
always with units and tendency where the sheet has them:
"1013 hPa, falling 2 over 3 hours" — never "pressure is
dropping!", never a bare figure in prose without its unit.

**Fixed strings (verbatim, do not paraphrase).**

- The warm-up's only words are the content itself; the room
  adds no greeting.
- Log stamp for a replacement: **"VALVE 7 REPLACED — 21:43 —
  OK"** (time = bureau time at the act, §6.16).
- The requisition confirmation: **"FILED — REQUISITION № 87"**
  (number derived, §6.13) with **"THE DUTY FORECASTER REPLIES
  BY THE 12:00 ISSUE"** (issue = the next one after filing).
- The not-filed line: **"NOT FILED — THE LINE IS DOWN. YOUR
  SLIP IS KEPT; FILE AGAIN."**
- The off-air line: **"OFF AIR — THIS PANEL HAS NO SHEET."**
- The silent station's card reason is written per incident by
  the forecaster — it is the one fixed-format string that is
  never templated beyond its facts: "RELAY FAULT — ENGINEER
  CALLED 04:15."

**Empty-state voice.** The bureau states what it has, what it
hasn't, and where the nearest lit bench is (§6.18) — in
Caslon, in full sentences, without a joke. The room's humour
is dry and lives in the log, never in a visitor's dead end.

---

## 13. Full-page scroll choreography map

The home bench (§7), top to footer, in order. Every beat
names what the visitor sees and what it means; beats are
caused by the shared loop (§5) and by nothing else.

1. **First paint.** The bench stands printed and cold:
   nameplate, hero panel with its headline and figures legible
   in the dim, dials at value. *The bureau exists before it is
   switched on.*
2. **The warm-up** (§6.1, t≈100–2400ms). Letters warm in
   stagger, one settle flicker each, dial faces at t=500ms,
   the master dial sweeping last to 1013 with its overshoot
   and settle. The filament (§6.5) warms to 12%. *The shift
   begins; the visitor threw the switch by arriving.*
3. **The pin** (§6.8). Scrolling, the master dial stays at the
   centre while the first bench passes: pressure holds, the
   tendency sub-needle swings to FALLING at 40%, the verdict
   warms letter by letter at 75%, the clamp releases with its
   300ms settle. *The duty instrument walks the first bench
   with you.*
4. **Panel 2 plugs** (§6.3 + §6.2). The hero's cord re-drapes
   to the day-table panel; snap, beat, warm; the table's
   current-hour row takes its amber wash (§6.12). The filament
   frontier crosses the jack as it lights. *Reading becomes
   connection; the record lights.*
5. **Panel 3 — the rack** (§6.11). Plug, warm, cards dealt in
   rack order, stamps striking; the two SILENT cards stay cool
   and strike red. *The network reports — and its silences are
   filed as firmly as its reports.*
6. **The image window** (§6.9) in Panel 4 (the bureau's own
   bench, 1954): the frame's light passes once; the photograph
   never moves. *Evidence, fitted and lit.*
7. **The requisition panel** (§6.13) plugs in as it arrives —
   the slip blank, inviting, its first rule slightly darker.
   The filament is past halfway; the room is warm. *The
   visitor is offered the bureau's services at the point in
   the walk where the bureau has earned the asking.*
8. **The footer bench** (§6.15). The rack warms left to right;
   the log lies printed; the plate takes its light pass. The
   filament frontier reaches full amber and its bead parks
   beside the log. *The shift is walked; the room is at
   temperature.*
9. **Valve 7** (§6.16), on its own schedule, only if the
   visitor lingers: a fault, a repair, a line in the log.
   *The room admits it is maintained, and lets you help.*

**Reverse pass.** Scrolling back up: cords re-drape to the
panel in view (§6.2) — the only thing that re-patches; panels
stay lit and filed (§6.3); dials reverse-scrub without
overshoot (§6.4); the filament cools back down the rail
(§6.5). The room cools behind the returning visitor but
nothing it filed is unfiled.

**Jump scroll** (anchor link, find-in-page, scrollbar drag to
the foot): all intermediate panels are set directly to their
end states (plugged, lit, filed) in one frame — the bureau
does not perform a walk the visitor did not take — and the
filament sets to the true position. Landing mid-page is
indistinguishable from having walked there, minus the
journey's animations.

---

## 14. Whole-page performance budget

| Budget line | Limit |
|---|---|
| Total page weight (home, first load) | ≤850KB (HTML/CSS/JS ≤210KB gz; fonts ≤120KB — three families, subset to Latin + figures; images ≤500KB across ≤6 plates, §6.9) |
| Animation frame cost (shared loop, all channels) | ≤1.6ms/frame average during motion; 0ms at rest (loop sleeps) |
| Long tasks from motion systems | None >50ms; the warm-up's letter wrapping is the only DOM-heavy beat and is capped at 120 spans (§6.1) |
| Layout shift | CLS ≤0.02 total, 0 attributable to motion (shells final at first paint, §6.1/§6.9) |
| LCP (mid-range Android, 4G) | ≤2.5s — and the LCP element is printed content, legible in its cold state well before that (§6.1) |
| Inertials | Scroll never hijacked; the pin (§6.8) is sticky positioning, not a scroll trap |

**Cut order** (when the budget is exceeded, cut in this
order — the order is the theme's priorities, stated in
advance):

1. The hero ambient light loop (§6.9's ambient version) —
   ambience goes before behaviour.
2. Cord swing settle (§6.2) — cords still travel and plug;
   they stop swinging.
3. Idle filament breathing (§6.4) — hero dials rest.
4. The warm-up's stagger (letters warm together) — the ritual
   shortens before it is cut.
5. Image plates beyond the third per page.

**Never cut, at any budget:** the printed figures and their
sheet route (§6.17); the watchdogs (§10.3); the reduced-motion
variants; the filament (§6.5 — it shrinks to its mobile form,
never vanishes); the correction trail (§6.12); Valve 7's
accessibility caps (§6.16). A build that ships the glow and
cuts the print has inverted the law and fails §10 regardless
of its scores.

**Print.** The print stylesheet *is* the theme's final form:
paper ground, ink text, tables entire, dials replaced by
their printed values in place, cords and glows gone, the
sheet's provenance caption on every table (§6.12) and the
issue line at the head. A printed page from this theme should
be indistinguishable from the bureau's own paper — that is
not a fallback, it is the point.

---

## 15. Build-order checklist

In this order; each step leaves the site in a shippable state,
because the law (print first) is also a build sequence.

1. **The record.** Author the Observation Sheet (§6.17) as the
   single data source; no component is built before its
   figures exist.
2. **The printed bureau.** Static HTML/CSS of every page,
   fully lit, dials at value, tables entire, no JS. Ship-check
   this state against §10.2 — it is the fallback and the
   foundation.
3. **Tokens & type.** §2's palette as custom properties with
   the pairing table enforced in review; §3's scale and five
   laws; Oswald lettering sized to panels (long names wrapped,
   never shrunk).
4. **The bench.** Panels, rivets, frames (§4); nameplate and
   nav generated from the panel list (§6.10); footer with rack
   and log (§6.15, static states).
5. **The sheet's renderings.** Tables (§6.12), cards (§6.11),
   counters — all generated from step 1's record; hand-typed
   figures rejected in review.
6. **The shared loop.** One rAF loop, three lerp channels
   (§5); scroll position as its only input. No other loop or
   scroll listener is added after this step (§10.9).
7. **Dials.** §6.4's scrub + valve arrival on the loop;
   needles' resting transforms already correct from step 2.
8. **Plugging.** §6.3's snap + panel warm; §6.2's cords on the
   declared cord map; §6.5's filament + the sync check (§10.6).
9. **The master dial.** §6.8's pin and reading cycle; mobile
   pin-cut verified.
10. **Warmth & patch.** §6.6's hover/focus warmth (CSS-first);
    §6.7's click-to-plug driving steps 7–8's machinery.
11. **The warm-up.** §6.1 armed over the finished hero, with
    its session rule and fast-forward; watchdog set (2600ms).
12. **Transitions & standby.** §6.14's dip and standby shells
    (shells carry last issue's figures, step 5's route).
13. **The form.** §6.13 end-to-end including the server path
    (no-JS filing must work before the JS sequence is added)
    and the derived number from the record.
14. **Valve 7.** §6.16 last of the behaviours — the egg is
    fitted only when the room it lives in is complete —
    with its caps and its reduced-motion retirement.
15. **The gate.** §10 run entire, by a non-builder; the
    screenshot test (§10.14) at ten scroll positions; sign-off
    recorded in the maintenance log's build copy — where else.
