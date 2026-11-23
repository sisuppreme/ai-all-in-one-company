# 42. Salt Mirror — Expanded (v1 + v2)

> Expansion of theme #42 from `themes-026-050.md`, written directly to
> the full standard: the v1 10-part structure plus the v2 deepening
> layers (per-element choreography timelines, state matrices, breakpoint
> behaviour, edge cases, accessibility specs and token lists; per-theme
> component inventory, copywriting voice, three worked examples, scroll
> choreography map, performance budget, build-order checklist).
> Identity preserved exactly: the same concept, the same five palette
> anchors, the same two typefaces, the same nine signature elements —
> deepened, never redesigned — plus nine page-family elements.

## 1. Concept & world

Most websites are browsed. This one is **crossed**. The page is a salt
flat: an endless white plain under a strict horizontal horizon, and
everything that stands on the flat — the headline, the images, one
distant mountain — is doubled beneath the horizon line in a water
mirror that shimmers when disturbed. Scrolling is not navigation; it
is the walk itself. At load the mountain is a speck (scale 0.12) at
the far end of the plain. Across the entire scroll of the page it
grows — almost imperceptibly per screen, by a true perspective law —
until the visitor arrives: the final section pins, the mountain stands
at full size, and the page's one warm thing, a small orange flag at
the destination, is revealed. The whole page is a single approach to
a single goal, and the goal is the conversion section. There is no
other plot.

The world is the flat, treated as a complete interface vocabulary
rather than a backdrop. The page has a **horizon** (the strict line
that divides every composition; above it the world, below it the
mirror), the **plain** (the sections between departure and arrival —
views across empty ground, each holding one object and its
reflection), the **mountain** (the destination object, riding the
horizon for the whole journey, the page's only honest gauge of
progress), the **distance** (the one true number, counted down in
metres from a declared total), **waypoints** (the sections' distance
stamps, computed from the same function that moves the mountain), and
the **flag** (the single warm element, at the destination, which the
copy never explains). Nothing on the page is landscape decoration.
The geography is the information architecture: **distance is the
page's argument about wanting**, performed by the scroll itself.

**The theme's one law: the mountain is the only honest gauge.** Every
figure of progress on the page — the mountain's scale, the distance
counter, every waypoint stamp — is one declared approach function
printed several ways (§6.2, §6.5, §6.16), and the function is printed
on the page (§6.14) so a visitor can audit it. The horizon hairline
thickens as you travel, nearly invisibly, and it is *not* a gauge:
it is weather, not data, and no copy may ever point at it as
progress. A Salt Mirror build that adds a progress bar, a percentage,
or a second moving number has not bent the theme — it has hung a
dashboard over the flat, and the quality gate (§10) fails it on
sight. Everything else in this theme is craft. That one is surveying
ethics.

**The warm law (the palette's constitution, §2): exactly one warm
element exists on the entire page** — the small orange flag at the
destination — and the copy never explains it. Not the CTA, not a
badge, not a hover state, not the focus ring. Warmth is rationed to
the goal itself, so that the visitor's eye learns the geography the
way a walker's does: everything is white and grey-blue until the one
thing that matters.

**Crossing is the interaction model.** The visitor's acts are a
walker's acts: they disturb the water as they move (§6.3), they watch
the one number fall (§6.5), they draw their own sight line to the
goal (§6.6), and at the end they break the mirror-calm with a single
touch (§6.9) and arrive. The site does not have users skimming a
feed; it has travellers who understand that the distance was the
content. That is why the theme fits a single, genuinely desired
destination — one lodge, one product launch, one appointment, one
piece of work at the end of a long story — and why it curdles around
anything plural, urgent or interchangeable.

**Best-fit sites and audiences.**

- One-destination hospitality: a remote lodge, a desert camp, an
  island house, a retreat — where the journey is honestly part of the
  offer and the booking form is the arrival.
- A single flagship product or work: one watch, one instrument, one
  book, one exhibition — a page that is an approach to a single
  object, with the object small on the horizon until the end.
- Long-form pilgrimage stories: an expedition, a restoration, a
  record attempt — narratives with a real distance in them, where the
  metres counted down are metres that were actually travelled.
- Galleries and portfolios of one: a single collection, a single
  artist's one body of work, presented as views across a plain.
- Memorial and dedication pages: one name at the end of a quiet page,
  where restraint is the respect and the arrival is the point.

**When NOT to use it.**

- For plural content. If the page has five equal offers, there is no
  destination; five mountains is a range, and a range is a different
  theme. Choose another.
- For urgent transactions. The crossing is paced — the mountain grows
  across the whole page and the arrival pins. A visitor paying a bill
  in forty seconds should not have to walk 4,800 metres for the
  button.
- Where the distance would be theatre. If the publisher cannot state
  what the one destination is and why it deserves a whole plain, the
  emptiness is padding. Choose another theme.
- For content that must be scanned. The plain holds one object per
  screen by law (§4); a reference page, a dashboard or an index
  starves here.
- For audiences who must never be asked to scroll far. The theme's
  whole argument is the approach; a page whose readers will only ever
  see the speck wastes it and misrepresents what waits at the end.

## 2. Palette

Five anchors, inherited unchanged. The palette is a salt flat at
midday: white ground, grey crust, the pale blue the sky lends the
mirror, the blue-grey of far rock — and one warm thing, rationed by
law. Nothing else is admitted; every other colour on the page is one
of these five, tinted, shaded, or set at an opacity over salt.

| Token | Hex | Role | Usage ratio | Pairing & contrast notes |
|---|---|---|---|---|
| `--salt` | `#FAFAF7` | The ground of everything: page background, the mirror's field, all open space | ~78% of pixels | The page is mostly this. Mountain on it: **6.85:1** (AA). Mountain-deep on it: **9.95:1** (AAA) — the default text pairing. Reflection on it: 1.77:1 — the mirror is atmosphere, never text. |
| `--crust` | `#E8E6DF` | The salt's crust: section grounds at the plain's stations, skeleton fills, the mirror's shallow band | ~9% of pixels | Mountain-deep on crust: **8.33:1** (AAA); mountain on crust 5.73:1 (AA). Crust on salt is 1.19:1 — a ground change, never a line that must be read. |
| `--reflection` | `#A8C3CF` | The sky in the water: reflection tints, haze, the sight line's far half, waypoint rules | ~7% of pixels | Never text on salt (1.77:1). On mountain-deep it is 5.63:1 — reflection may letter the dusk fields (§2, dark ruling) and nothing else. |
| `--mountain` | `#4A5A63` | The destination and all standing objects: the mountain, headline ink at display sizes, image frames, the CTA ground | ~5% of pixels | Salt on it: **6.85:1** (AA) — the CTA and the arrival band carry salt text. On salt 6.85:1 — display and apparatus only; body text uses `--mountain-deep`. |
| `--flag` | `#D96C4A` | **The one warm thing.** The flag at the destination. Nothing else. Ever. | <0.1% of pixels | On salt 3.24:1; on mountain 2.11:1 — it is a seen thing, never a read thing: it carries no text, no icon that must be decoded, no state that must be perceived. Its low contrast is survivable *because* nothing depends on reading it. |

**Derived tokens (closed list — no others may be introduced).**

| Token | Hex / value | Derivation & use |
|---|---|---|
| `--mountain-deep` | `#33424A` | The mountain shaded toward ink: all body text and apparatus on salt and crust. **9.95:1** on salt, 8.33:1 on crust. The page's reading colour. |
| `--reflection-deep` | `#5F8296` | The reflection deepened: waypoint figures' rules, the sight line's near half, focus-adjacent line work on salt. 3.92:1 on salt — graphical and ≥18px apparatus only, never body text. |
| `--crust-deep` | `#CFC9BA` | Crust shaded: the horizon hairline at full thickness, skeleton line-work, the mirror's depth veil stops. 1.58:1 on salt — line-work only, never text, never an affordance alone. |
| `--haze` | `rgba(168,195,207,.30)` | Reflection at 30%: the heat-haze band at the horizon (§5) and the mirage's shimmer field (§6.17). Decorative only; content beneath must meet contrast with the haze removed. |
| `--glint` | `#FFFFFF` | Pure white: salt-crystal glints (§5). A sparkle needs no contrast — it is a light event, not information; nothing is ever communicated by a glint alone. |
| `--fade-depth` | `linear-gradient(rgba(250,250,247,0), rgba(250,250,247,.55))` | The mirror's depth veil: laid over every reflection, clear at the horizon, veiling to 55% salt at the reflection's foot — reflections fade with depth, as water does. |

**Dark-mode behaviour: the theme does not invert — the flat goes to
dusk.** The plain at night is still pale (moonlit salt does not turn
black), so under `prefers-color-scheme: dark` the *sky* changes, not
the ground: the above-horizon fields and the arrival band deepen to
`--mountain-deep` grounds, the mountain itself silhouettes to
`#2C3941` (11.35:1 against salt — it reads as a shape against the
pale flat, darker than the dusk sky behind it), the reflection
deepens to `#7E9CA9` (2.78:1 on salt — still atmosphere, still never
text), and text on the dusk fields is salt (9.95:1) with reflection
permitted for apparatus (5.63:1). The flag does not change: the one
warm thing burns at the same hex in both schemes — a walker should
find the same flag by night. A build that inverts the salt to black
has not made a dark mode; it has flooded the flat, and §10 fails it.

**Pairing law.** Text is mountain-deep on salt and crust; salt on
mountain and mountain-deep; reflection only as apparatus on
mountain-deep dusk fields. Flag carries no text. Reflection, crust
and crust-deep never carry text on salt. Any other pairing is a build
error, not a variation.

**The warm audit.** `--flag` may appear in exactly one component
(§6.7) in exactly one instance on the page. Its hex may not be used
for hover tints, error states, focus rings, link underlines, chart
accents or "just the submit button". The audit is a grep, and it is
blocking (§10, gate 2).

## 3. Typography

Two typefaces, inherited unchanged. **Instrument Serif** is the
standing voice — it sets everything that *stands on the flat*: the
destination word, headlines, section titles, the names of things.
**Inter** is the measuring voice — light (300) for body, medium (500)
for apparatus — and sets everything that *measures the flat*: body
prose, captions, waypoints, the distance counter. There is no third
typeface. Instrument Serif has a single weight; emphasis in the
standing voice is size, never bold. Emphasis in the measuring voice
is weight (300 → 500), never italic display.

| Role | Face | Size / line-height | Tracking | Rules |
|---|---|---|---|---|
| Destination word (hero) | Instrument Serif 400 | 64–120px / 1.0, `clamp(4rem, 10vw, 7.5rem)` | +0.01em | One word (or a name). It is written onto the crust letter by letter (§6.4). Never more than one line; a name that needs two lines is set smaller, never wrapped. |
| Headline | Instrument Serif 400 | 40–64px / 1.05, `clamp(2.5rem, 5.5vw, 4rem)` | 0 | The mirrored headline (§6.4) is the only headline with a reflection. Section headlines stand unmirrored (type law 1). |
| Section title | Instrument Serif 400 | 30–42px / 1.12 | 0 | The name of the view: a place, an object, a fact of the route. |
| Body | Inter 300 | 17–19px / 1.65 | 0 | Measure 56–62ch. The plain is read slowly; line-height never drops below 1.6 anywhere on the page. |
| Caption / context | Inter 300 | 14.5–15.5px / 1.55 | 0 | Stands beneath its plate (§6.12), unmirrored: the water takes shapes, not sentences (type law 1). |
| Apparatus (waypoints, labels) | Inter 500 | 11–13px, uppercase | +0.14em | Distance stamps, station names, the counter's label. Uppercase is rationed to apparatus only. |
| Distance counter | Inter 500 | 15–17px, `tabular-nums` | +0.06em | The page's one moving number (§6.5). Always printed with its unit and its label: `REMAINING 3,214 M`. |

**Type laws.**

1. **Only shapes reflect; sentences don't.** Display type (the hero
   headline, the destination word) and images cast reflections —
   they are objects standing on the flat. Body text, captions and
   apparatus never reflect: a mirrored paragraph is unreadable, and
   the theme does not print unreadable text even as decoration.
   Mirrored display copies are `aria-hidden` duplicates (§6.4).
2. **The counter is the only number that moves.** Waypoint stamps are
   computed but printed still (§6.16); prices, dates and counts
   elsewhere on the page are set once and never animate. A page with
   two moving numbers has two gauges, and the one law (§1) forbids
   it.
3. **Serif stands, sans measures.** A headline set in Inter or a
   waypoint set in Instrument Serif is a category error the gate
   (§10) can grep for.
4. **Distance is lettered before it is described.** Every section
   opens with its waypoint stamp (§6.16) in apparatus; prose follows.
   A section that begins with a paragraph has skipped its own survey.
5. **No exclamation, no urgency.** The flat does not shout and the
   destination does not hurry anyone. Full stops and distances only
   (§12).

## 4. Layout language

**The horizon divides every composition.** Each composed view — the
hero, each paired plate (§6.12), the arrival — is split by a
horizontal horizon: the object stands above the line, its reflection
falls below it. The page's **master horizon** sits at 56% of viewport
height: the fixed hairline and the mountain (§6.2) ride it for the
whole journey, so the visitor's eye learns one line and every local
composition agrees with it. A composition whose local horizon fights
the master line (a plate whose reflection starts at a different
height while the mountain is on screen) is a surveying error.

**The horizon band is empty by law.** Nothing but the mountain, its
reflection and the hairline occupies the band ±90px around the master
horizon at any scroll position. Text blocks are placed in the sky
field above the band or stand as objects whose bases rest on local
horizons inside their own sections; body copy never crosses the band.
This is what makes the fixed mountain possible without ever covering
content (§6.2): the corridor it travels in is empty by design, not by
z-index.

**The plain is one column, mostly empty.** Content reads in a single
centred column, max 1120px, measure 56–62ch, inside a page that is
~78% salt. Sections are **views**: each is at least 100vh tall, holds
exactly one object (one plate, one statement, one table of the
route), and is separated from the next by open ground — vertical
space is not padding here, it is *distance*, declared in the build as
fractions of the approach (§6.16's stamps are computed from the same
positions). Two objects on one screen is a crowd; the density law
fails it.

**Reflections fall, they do not float.** A reflection is the object's
exact vertical mirror, sharing its base line at the horizon, rendered
at 62% opacity under the `--fade-depth` veil, rippled (§6.3) but
never offset, rotated or shadowed. A reflection detached from its
object's base — drifting, drop-shadowed, at a jaunty angle — is a
sticker, and §9 names it.

**The arrival is the only dense place.** Density rises exactly once,
at the end: the arrival section holds the full-size mountain, the
flag, the CTA and the form (§6.13) in one composed field. Everywhere
else the law is one object per screen. A busy plain with a quiet
arrival has the geography backwards.

**Corner radius is 0** except the flag's cloth (§6.7) and form fields'
2px. Salt, water and rock are not rounded; cards (§6.12) are plates
standing on the flat, flat themselves.

## 5. Full motion system

Five named easings, used by every element and no others:

| Token | Curve | Character | Used by |
|---|---|---|---|
| `--ease-glide` | `cubic-bezier(.3,.6,.2,1)` | The horizon glide: long, level, unhurried — motion that has a plain to cross | Mountain settles (§6.2), CTA lean (§6.8), hero composition (§6.11) |
| `--ease-assemble` | `cubic-bezier(.25,.8,.3,1)` | A thing taking its place on the flat: arrives, stands, stops | Reflection assembly (§6.1), plates (§6.12), arrival (§6.13) |
| `--ease-ripple` | `cubic-bezier(.2,.7,.3,1)` | Water answering a touch: quick out, slow calm | Velocity ripples (§6.3), mirror-break (§6.9), letter ripples (§6.4) |
| `--ease-draw` | `cubic-bezier(.45,0,.35,1)` | A line drawn by a steady hand across a map | Sight line (§6.6), footer rule (§6.14) |
| `--ease-flutter` | `cubic-bezier(.34,1.3,.44,1)` | Cloth in a gust: the system's one licensed overshoot, reserved for the flag | Flag flutter (§6.7) only |

**Every motion term, translated into the flat's language:**

- **Scroll-triggered reveals** are arrivals: an object is first seen
  the way things are seen on a plain — small, at its horizon, then
  present. Plates (§6.12) assemble their reflections as they enter;
  nothing fades up out of the salt like a SaaS card.
- **Scroll scrub** is the walk itself: the mountain (§6.2), the
  distance (§6.5), the hairline's thickening and the waypoint stamps'
  truth are pure functions of scroll position, driven by the shared
  loop. The page's master variable is **P** (approach progress,
  0→1), defined in §6.2.
- **Parallax** is mirrored: an object and its reflection move at
  mirrored rates (+r above the horizon, −r below it, §6.12). There
  is no decorative background parallax; the only things that move
  against the scroll are objects and their water.
- **Pinned scenes:** exactly one — the arrival (§6.2 phase 2, §6.13).
  The mountain's ride is fixed, not pinned; pinning anywhere else is
  refused: a plain is crossed, not camped on.
- **Masked reveals** happen across the horizon: the mirrored headline
  is unmasked upward from the line (§6.4) — the mask edge is the
  horizon itself.
- **Blur-to-sharp is refused.** Objects on a flat are sharp at any
  distance — small, but sharp. Only reflections distort, and they
  distort as water (displacement), never as defocus. A blurred hero
  is a camera effect and there is no camera on the flat.
- **Kinetic typography** is refused except the destination word
  (§6.4): written letter by letter onto the crust, once, at the
  departure. Type does not perform on the plain.
- **Counters:** exactly one — the distance (§6.5). It does not tick,
  spin or odometer; it is scrubbed to the walk, settling in whole
  metres.
- **Progress** is the mountain (§6.2). The horizon hairline thickens
  1px → 3px across P as *weather* (§1's law: it is not a gauge and no
  copy may cite it). There is no progress bar, no percentage, no
  scroll-% readout, anywhere, ever.
- **Marquee is refused.** Nothing crosses the flat sideways forever.
- **Ambient loops:** exactly two — the heat haze at the horizon (a
  2px shimmer within ±14px of the line, 7000ms cycle, §6.2) and the
  salt glints (≤12 points page-wide, each a 300ms glint every 4–9s,
  §6.11). Both are sparse, both pause off-screen, both are cut first
  by the performance ladder (§14).
- **Micro-interactions:** the flag's flutter (§6.7), the mirror-break
  (§6.9), the water calming under a hovered plate (§6.12). Every
  interaction is something a walker could do to water, cloth or
  distance.
- **Hover physics:** no magnetism anywhere except the destination
  CTA's long lean (§6.8) — desire expressed as geography, rationed
  to the goal. Elsewhere hover stills or answers; nothing else leans,
  tilts or follows.
- **Page transitions** are a horizon hold (§6.15): the line is kept,
  the flat re-stands. The mountain's scale is session-persisted, so a
  returning page resumes the approach where the visitor left it.
- **Smooth scrolling:** the walk has distance. The shared loop lerps
  the mountain at `--lerp-approach` 0.06 — the slowest value in the
  library, because the mountain must feel almost still — ripples at
  0.12, the lean at 0.10. Native scroll is never hijacked; the flat
  smooths its instruments, not the visitor's legs.
- **The shared loop law.** One `requestAnimationFrame` loop owns
  every scrubbed value (P, mountain scale, distance, hairline,
  ripples, lean, haze phase). It writes only transform / opacity /
  custom properties, and stops writing a value when it settles within
  0.1% of target. Velocity (§6.3) is derived inside the loop from P's
  own delta — never from raw scroll events, so the water answers the
  walk, not the wheel.

**Watchdog law.** Every ceremony has a timer: if an observer or the
loop fails, the reflection assembly completes by 2400ms (§6.1), the
written word stands complete by 3000ms (§6.4), and any plate's
reflection stands assembled 1000ms after the plate enters (§6.12).
The DOM ships *arrived*: reflections assembled, the word written, the
mountain at its P-correct scale for P=0 (0.12). All pre-states exist
only under a JS-armed root class. No-JS is not a degraded mode — it
is the flat at rest, with the mountain small and the whole journey
still to walk by reading.

## 6. Signature elements

### 6.1 Reflection assembly

- **What & why.** On load, the mountain fades in above the master
  horizon, and then its reflection *assembles* beneath the line: the
  mirrored shape gathers out of rippling water and settles into a
  still, sharp-at-the-base reflection over 2000ms. It belongs because
  it is the theme's first sentence — before any copy is read, the
  visitor has learned the world's physics: things stand here, and
  the water doubles them. Every later reflection on the page obeys
  the grammar this one teaches.
- **Structure.** The hero composition (§6.11) holds the mountain SVG
  (`.mountain-object`) and, directly beneath the master horizon, its
  reflection: the same SVG in a `.reflection` wrapper, flipped
  (`scaleY(-1)`), clipped to the mirror field, passed through an SVG
  `feTurbulence` + `feDisplacementMap` filter whose `scale` is a
  custom property written by the shared loop, and veiled by
  `--fade-depth` at 62% opacity. The reflection is `aria-hidden`; the
  object carries the meaning. Both ship in final position in the DOM;
  the displacement's starting amplitude is JS-armed only.
- **Motion spec.** Trigger: load, gated on `document.fonts.ready`
  raced against a 600ms timer. t=0: the mountain fades 0→1 over
  800ms `--ease-assemble`. t=500ms: the reflection's displacement
  scale starts at 26 and decays to its rest value 3 over 1500ms
  `--ease-ripple`, while the reflection's opacity rises 0→0.62 over
  the same window — the mirror *settles out of disturbance*, it does
  not fade in like a ghost. Total ceremony ≤2000ms; a first scroll or
  click completes it instantly (displacement snaps to 3, opacity to
  0.62). Runs once per session; a repeat visit loads with the mirror
  already calm.
- **States.** Assembling → mirrored (rest) → disturbed (any scroll
  re-ripples it via §6.3) → calm again at rest. Scrolled-past: the
  assembly never re-runs; the mountain has left the hero and is
  riding the horizon (§6.2).
- **Content merge.** The assembling reflection belongs to the hero's
  central object — the destination itself. It is not an effect laid
  over content; it is the first appearance of the page's protagonist,
  doubled by the world it stands in. Remove the animation and the
  page loses the lesson, not the information.
- **Failure fallback.** No JS: mountain present, reflection present,
  displacement at rest value 3 (the filter's static attribute), veil
  applied. Watchdog: if the ceremony has not completed by 2400ms —
  loop stalled, fonts hung — displacement and opacity are forced to
  rest values by a timer that does not depend on the loop.
- **Reduced-motion variant.** The mirror is assembled at first paint:
  mountain at full opacity, reflection at 0.62 with rest displacement
  3. The physics is information; only its settling rests.
- **Performance budget & mobile variant.** One SVG filter on one
  element, displacement updated only while |scale − 3| > 0.1. Cost
  ≤0.3ms/frame during the ceremony, zero at rest. Mobile (<768px):
  the same ceremony, shortened — fade 600ms, settle 1100ms — and the
  turbulence base frequency halves (fewer octaves of water on a small
  screen).
- **Choreography timeline (v2).** t=0 fonts ready (or race lost) →
  t=0–800 mountain fades in → t=500 reflection opacity begins rising,
  displacement at 26 → t=1250 displacement ≈9, opacity ≈0.45 →
  t=2000 displacement 3, opacity 0.62, mirror calm → ceremony over;
  the destination word's writing (§6.4) begins at t=900 inside this
  window, so the eye goes object → mirror → word.
- **State matrix (v2).** *Rest:* calm mirror, displacement 3.
  *Hover:* none — the hero mountain is not interactive; hovering it
  changes nothing (the water answers the walk and the plates, §6.12,
  not a pointer over the destination). *Focus:* the mountain is not
  focusable. *Active:* n/a. *Scrolled-past:* assembly complete,
  element handed to §6.2's ride. *Disabled:* n/a. *Touch:* identical;
  a tap anywhere completes the ceremony early, as a click does.
- **Breakpoints (v2).** ≥1200px: mountain 560px wide at scale 1 (it
  sits at 0.12 during the assembly — 67px — and grows later, §6.2);
  mirror field 340px deep. 768–1199px: mountain 440px, mirror 260px.
  <768px: mountain 300px, mirror 180px, ceremony shortened as above;
  the reflection's veil gradient compresses proportionally.
- **Edge cases & failure modes (v2).** *SVG filters unsupported*
  (legacy engines): the reflection renders undisplaced — a still
  mirror; the assembly degrades to the opacity rise alone, which is
  still honest water. *Tab hidden mid-ceremony:* the watchdog forces
  rest values; no half-rippled mirror greets the returning visitor.
  *Session revisit:* ceremony skipped (sessionStorage flag), mirror
  calm at first paint.
- **Accessibility spec (v2).** The reflection is `aria-hidden="true"`
  and `focusable="false"`; the mountain SVG carries `role="img"` and
  the label the build declares (e.g. "Cerro Blanco, the destination").
  The ceremony moves no focus and announces nothing — it is weather
  over content that is already readable from first paint.
- **Tokens consumed (v2).** `--salt`, `--reflection`, `--mountain`,
  `--fade-depth`, `--ease-assemble`, `--ease-ripple`,
  `--dur-assembly` (2000ms), `--ripple-rest` (3).

### 6.2 The long approach

- **What & why.** The mountain grows from scale 0.12 to 1.0 across
  the *entire* page, scrubbed to scroll by a true perspective law, so
  slowly that no single screen shows it move — yet the speck of the
  first screen is unmistakably a presence by the third, and a wall by
  the arrival. It belongs because it is the theme made physical: the
  destination is the final section, and the whole page is one
  approach to it. It is also the progress gauge the one law (§1)
  permits — the only one.
- **Structure.** One `.mountain-ride` element, `position: fixed`,
  horizontally centred, its base seated on the master horizon
  (bottom edge at 56vh), `pointer-events: none`, z-index below
  content plates and above section grounds. It contains the mountain
  SVG at its scale-1 width (560px desktop) and its reflection
  (§6.3's water lives in the ride too, so object and mirror travel
  together). The transform `scale()` is written by the shared loop
  from P. The ride renders *behind* the horizon band's empty corridor
  (§4) — it never overlaps text because the band is empty by law.
  At the arrival, the ride docks: the fixed element hands off to an
  identical in-flow mountain inside the arrival section (§6.13) at
  the pin's start, same scale, same position — a crossfade of
  custody, not a jump.
- **Motion spec.** The master variable: **P**, approach progress,
  computed as scrolled distance ÷ total approach distance, where the
  total includes the arrival pin's length (§6.13). Remaining distance
  **d(P) = D0 × (1 − P)**, D0 declared per build (default 4800m,
  printed in §6.14). Scale follows perspective — apparent size is
  inversely proportional to remaining distance: **s(d) = 0.12 ×
  D0 ÷ d**, clamped: while d ≥ 576, s = 0.12 × 4800/d (at P=0,
  d=4800, s=0.12; at P=0.5, d=2400, s=0.24; at P=0.88, d=576, s=1.0).
  Phase 2 (the arrival pin, P from 0.88→1, d from 576→0): the
  mountain holds s=1.0 and the last metres are walked at full size —
  the flag reveals inside this phase (§6.7). The loop lerps the
  *rendered* P toward the target P at `--lerp-approach` 0.06, so the
  mountain trails the scroll by a breath and never jitters. The
  horizon hairline thickens 1px→3px linearly across P (weather, §1 —
  implemented as a custom property, never labelled, never announced).
- **States.** Approaching (P<0.88) → arriving (pin, 0.88≤P<1) →
  arrived (P=1: ride docked, mountain in-flow, full size, still).
  Scrolled back up: the approach reverses exactly — the mountain
  shrinks by the same law; a walker may retreat, and the gauge does
  not lie about it. The deepest P reached is remembered only by the
  session-persistence of transitions (§6.15), never by the gauge.
- **Content merge.** The mountain *is* the destination section's
  subject, present from the first screen. The page does not decorate
  its scroll with a mascot; it shows the visitor the thing they are
  travelling to, at its true apparent size, the entire way. The CTA
  section is not "revealed" at the end — it is *reached*.
- **Failure fallback.** No JS: the mountain stands in the hero at
  0.12 (§6.1) and again, in-flow at full size, in the arrival section
  — the two static appearances bookend a journey the reader makes by
  reading. Loop killed mid-page: the ride freezes at its last scale;
  content is unaffected (the corridor is empty), and §6.5's counter
  watchdog prints the P-correct distance from the raw scroll position
  so the one number never freezes wrong.
- **Reduced-motion variant.** The mountain does not ride. It appears
  in the hero at 0.12 and in the arrival at 1.0 — two stills, the
  departure and the destination — and the distance counter prints
  each section's waypoint value (§6.16) as the reader passes it,
  stepped, not scrubbed. The geography survives; the walk is told,
  not performed.
- **Performance budget & mobile variant.** One fixed element, one
  transform write per frame while P is unsettled; ≤0.2ms/frame. The
  reflection inside the ride shares §6.3's filter budget. Mobile
  (<768px): scale-1 width 300px; the corridor law (§4) holds at
  ±60px; the lerp rises to 0.09 (a shorter page needs a less lagging
  gauge) — the law (s from d) is unchanged, only the smoothing is.
- **Choreography timeline (v2).** Continuous, not beat-based: at
  every frame, target P is read from scroll; rendered P closes 6% of
  the gap; s and d are recomputed from rendered P by the declared
  formulas and written (scale transform, counter text throttled to
  whole-metre changes, hairline property). At P=0.88 the pin engages
  (§6.13) and custody of the mountain passes to the arrival over
  300ms `--ease-glide` (fixed and in-flow copies crossfade at
  identical scale/position). At P=1 the loop stops writing: arrived
  values are final.
- **State matrix (v2).** *Rest (scroll still):* mountain at its
  P-true scale, mirror calm (§6.3). *Hover:* none — the ride is
  pointer-events-none by construction. *Focus:* not focusable.
  *Active:* n/a. *Scrolled-past (P=1):* docked, still, the flag
  revealed (§6.7). *Disabled:* if the build has no arrival (a
  one-screen page), §6.2 is absent and §10's gate 1 fails the build
  — the theme requires a destination. *Touch:* identical; fling
  scrolling is absorbed by the 0.06 lerp, which is precisely what
  the lerp is for.
- **Breakpoints (v2).** ≥1200px: ride width 560px, corridor ±90px.
  768–1199px: 440px, corridor ±75px. <768px: 300px, corridor ±60px,
  lerp 0.09. The scale *law* never changes with breakpoint — only
  the instrument's size; a phone walker is not closer to the
  mountain than a desktop walker at the same P.
- **Edge cases & failure modes (v2).** *Very short page:* if the
  natural scroll length makes P race (total approach < 3 viewport
  heights before the pin), the build must add plain (empty sections
  are honest here — distance is content) until the approach reads;
  §10 gate 5 checks the ratio. *Browser find-in-page jump:* P snaps;
  the lerp closes the gap in ~1.2s and the mountain glides — no
  teleport, no stranded scale. *Resize mid-approach:* P is a ratio,
  recomputed from the new geometry on the next frame; scale is
  continuous across the resize. *The ride over a dark section:* the
  arrival band and dusk fields (§2) are the only dark grounds, and
  the mountain's silhouette hex is chosen against them (§2).
- **Accessibility spec (v2).** The ride is `aria-hidden` (the
  destination is announced in-flow by §6.11's hero and §6.13's
  arrival, both real content). Progress is never announced live —
  a screen-reader user reads the sections in order and meets the
  same arrival; the waypoint stamps (§6.16) give them the distances
  as text, which is the gauge in their medium. No content exists
  only in the ride.
- **Tokens consumed (v2).** `--mountain`, `--reflection`,
  `--fade-depth`, `--crust-deep`, `--ease-glide`,
  `--lerp-approach` (0.06), `--d0` (declared per build), `--horizon`
  (56vh).

### 6.3 Velocity ripples

- **What & why.** Every reflection on the page — the mountain's and
  each plate's (§6.12) — ripples with an amplitude proportional to
  scroll velocity, and calms when the visitor rests. It belongs
  because it makes the mirror a material with a memory of movement:
  walking disturbs the water; standing still lets it clear. It is
  the theme's ambient feedback — the page answering the walk without
  a single widget.
- **Structure.** Each `.reflection` carries the SVG displacement
  filter of §6.1 (one shared `<filter>` definition, referenced by
  all reflections; per-element amplitude via the filter's `scale`
  cannot vary per element with a shared filter, so each reflection
  instead wraps its mirrored layer in a group whose CSS
  `transform: translateX()` micro-offsets are layered over a single
  shared displacement at rest amplitude — the *visible* ripple is
  the composition of the shared displacement (scale 3) and a
  per-element horizontal shear written by the loop as
  `--shear`). Simpler builds may give the mountain's reflection its
  own filter; the cap is two filter instances page-wide (§14).
  Amplitude state lives in the shared loop: `v` = |ΔP| per frame,
  smoothed at 0.12.
- **Motion spec.** Amplitude **a = clamp(v × 900, 0, 14)** in
  displacement-scale units above the rest value 3: a slow read
  (v≈0.001/frame) gives a≈0.9 — a breathing shimmer; a fast fling
  (v≈0.02) saturates at 14 — the water churns, briefly. When
  scrolling stops, a decays to 0 with a 900ms `--ease-ripple` tail:
  the mirror clears *after* the walker stops, never during. The
  shear component oscillates ±a/3 px at 0.8Hz while a > 1, phase
  offset per element by its index so the page's waters do not move
  in lockstep — a plain of mirrors, not a chorus line.
- **States.** Calm (a=0, rest displacement 3) → disturbed (a>0 while
  scrolling) → clearing (900ms tail) → calm. Hover on a plate forces
  its own reflection toward calm (§6.12) — looking closely stills
  the water — while the rest of the page keeps its weather.
  Scrolled-past reflections keep rippling: the water behind the
  walker is also disturbed; freezing off-screen reflections is a
  performance cut (§14), never a visual state.
- **Content merge.** The ripples belong to the content's own
  reflections — the mountain's, the plates' images. There is no
  generic water layer under the page; disturb the walk and you
  disturb the *things*, which is why it reads as physics rather
  than as an effect.
- **Failure fallback.** Filters unsupported: reflections render at
  rest displacement (the attribute value), shear still applies —
  the water reads as heat-shimmer instead of ripple, an acceptable
  flat. Loop killed: all amplitudes freeze, then the §6.1 watchdog
  pattern forces rest values within 1000ms; no reflection may be
  left churned by a dead loop.
- **Reduced-motion variant.** No velocity response at all:
  displacement fixed at 3, shear 0, at all times. Still water is
  the reduced-motion flat's honest state — and it is also the
  state's name in §12's copy rules.
- **Performance budget & mobile variant.** Shared-filter cost is
  paid once per reflection repaint; the loop writes one custom
  property per live reflection per frame, ≤8 reflections on screen
  by the density law (§4) → ≤0.5ms/frame worst case. Mobile: the
  amplitude cap drops to 9 and the shear is cut entirely
  (displacement only) — small water, small weather.
- **Choreography timeline (v2).** Per frame while scrolling: v
  measured from P's delta → smoothed v′ closes 12% toward v → a
  recomputed → written to on-screen reflections. On scroll stop:
  t=0 v=0 → t=0–900 a decays 14→0 (or current→0) on `--ease-ripple`
  → t=900 displacement at rest 3 across the page; a reflection
  entering mid-fling starts at the page's current a (it joins the
  weather, it does not start calm in a storm).
- **State matrix (v2).** *Rest:* a=0 everywhere. *Hover:* per-plate
  calming (§6.12); the mountain's reflection ignores hover.
  *Focus:* a focused plate calms exactly as a hovered one.
  *Active:* n/a. *Scrolled-past:* still weather-responsive until
  off-screen, then frozen at its last a and reset to calm before
  re-entry. *Disabled:* reflections of withdrawn content are
  removed with their objects — no orphan water. *Touch:* flings
  produce the largest a; the 900ms tail is the touch signature —
  it is tuned so a flicked page visibly settles, once, then rests.
- **Breakpoints (v2).** ≥1200px: cap 14, shear on. 768–1199px:
  cap 12, shear on at half amplitude. <768px: cap 9, shear off,
  tail 700ms (a shorter page clears faster).
- **Edge cases & failure modes (v2).** *Scroll bounce* (overscroll
  at the ends): v spikes without travel — P clamps at 0/1, so v is
  computed from clamped P and the bounce makes no weather.
  *Programmatic scroll* (anchor jump): v saturates for one frame,
  then the tail clears it — the water registers a teleport as a
  splash, which is correct. *Many reflections off-screen:* the
  loop writes only to elements intersecting the viewport ±50%.
- **Accessibility spec (v2).** Reflections are `aria-hidden`
  duplicates (§6.1); the ripple is never the sole carrier of any
  state (scroll position is textually available via §6.5/§6.16).
  The motion is displacement of a decorative duplicate — it does
  not move content, flash, or exceed vestibular thresholds: peak
  shear ±4.7px at 0.8Hz, below the library's ambient limits.
- **Tokens consumed (v2).** `--reflection`, `--fade-depth`,
  `--ease-ripple`, `--ripple-rest` (3), `--ripple-cap` (14),
  `--dur-calm` (900ms).

### 6.4 Mirrored headline & the written word

- **What & why.** Two type events open the page. The hero headline
  rises in the sky field while its mirrored copy is unmasked below
  the horizon — rippling, veiled, upside down — so the title obeys
  the world's physics: type is an object standing on the flat. And
  the destination word — the one word the whole page walks toward —
  is *written* letter by letter onto the salt crust beneath the
  headline, each letter landing with a single ripple in its own
  small reflection. It belongs because it sets the contract in the
  first three seconds: here, words are things, things reflect, and
  the most important word arrives the way everything on this page
  arrives — gradually, across a surface.
- **Structure.** `.hero-headline` in the sky field; `.hero-headline-
  mirror` below the master horizon: an `aria-hidden` duplicate,
  flipped, clipped by a mask whose edge is the horizon line, veiled
  by `--fade-depth`, displaced at rest amplitude (§6.3). The
  destination word is `.destination-word`, a single line of
  Instrument Serif at the §3 display size, set in mountain-deep on
  the crust band of the hero's lower field; each letter is a span
  (JS-split; the unsplit word ships in the DOM), and each letter
  carries a miniature reflection span beneath it in the crust's
  shallow mirror strip. Letters ship visible; the writing
  pre-states (letters at opacity 0, offset 6px down) are JS-armed
  only.
- **Motion spec.** Headline: trigger load (after §6.1's t=500).
  The headline rises 18px and fades 0→1 over 900ms `--ease-glide`;
  its mirror is unmasked from the horizon downward over 1100ms
  `--ease-assemble`, beginning at +250ms, at rest ripple. The word:
  trigger at t=900 (§6.1's timeline hands over). Letters land one
  at a time, 90ms apart, each dropping 6px into place over 260ms
  `--ease-assemble`; as each letter lands, its reflection ripples
  once — displacement pulse 3→11→3 over 600ms `--ease-ripple`,
  that letter only. A 7-letter word completes at ≈2000ms. The
  whole ceremony (with §6.1) is done by 2400ms; first scroll or
  click completes everything instantly. Once per session.
- **States.** Writing → written (rest). The mirror's ripple state
  thereafter belongs to §6.3. Scrolled-past: never re-written.
  Hover/focus: the word and headline are not interactive; nothing
  answers a pointer here — the departure is a place, not a control.
- **Content merge.** The headline is the page's actual title and
  the word is the destination's actual name — the two most real
  texts on the page are the two that perform. The effect is not
  applied to content; it is the content's first appearance, staged
  by the world's rules.
- **Failure fallback.** No JS: headline standing, mirror present at
  rest ripple, word printed whole on the crust. Watchdog: any
  letter not landed by 3000ms is forced to rest; the headline's
  mirror is unmasked by 1600ms if its trigger never fired. A
  build may never ship a half-written destination.
- **Reduced-motion variant.** Everything stands at first paint:
  headline up, mirror unmasked at rest ripple, word whole. The
  ceremony is theatre; the title is information, and information
  does not wait for theatre.
- **Performance budget & mobile variant.** ≤14 letter spans, one
  mask animation, one pulse at a time; ≤0.2ms/frame. Mobile: the
  word's size clamps (§3) but the writing is unchanged — 90ms per
  letter is the rhythm of the place, not of the screen. Words
  longer than 12 letters tighten to 60ms/letter (the ceremony's
  total is capped, the word is not shortened).
- **Choreography timeline (v2).** t=500 headline rise begins →
  t=750 mirror unmask begins → t=900 first letter lands, its
  reflection pulses → letters land at 90ms intervals, each pulse
  600ms, pulses overlapping by design (a word written across
  water) → t≈1400 headline at rest → t≈1850 mirror fully unmasked
  → last letter +600ms: final pulse settles → t≤2400 the
  departure is complete and still.
- **State matrix (v2).** *Rest:* written word, standing headline,
  calm mirror. *Hover:* none. *Focus:* neither element is
  focusable; the hero's first focusable element is §6.11's scroll
  cue / nav. *Active:* n/a. *Scrolled-past:* final states, forever.
  *Disabled:* n/a. *Touch:* a tap completes the ceremony, as a
  click does; touch never *starts* a letter early — the word
  writes at its own pace or stands complete.
- **Breakpoints (v2).** ≥1200px: word at full clamp, mirror field
  340px. 768–1199px: mirror 260px. <768px: mirror 180px; the
  word's mirror strip shallows to 0.4× the letter height (small
  water under small type); headline rise shortens to 12px.
- **Edge cases & failure modes (v2).** *Very long destination
  word* (a compound name): the 60ms tightening above, and below
  380px viewport the word scales by `clamp` to fit one line — it
  never wraps: a wrapped destination word is two words, and the
  page walks toward one. *Fonts late:* the writing waits for the
  §6.1 fonts race; letters are never written in a fallback face
  and re-written in Instrument Serif. *Mirror of a two-line
  headline:* forbidden by §3 (headline max one line at hero size);
  a build whose headline wraps must shrink it, not mirror a stack.
- **Accessibility spec (v2).** The word ships as one text node
  (letters split by JS only, with the parent given an
  `aria-label` of the whole word and letter spans `aria-hidden`)
  — a screen reader hears the destination once, whole. The
  headline's mirror is `aria-hidden`. Nothing in the ceremony
  moves focus or is announced.
- **Tokens consumed (v2).** `--mountain`, `--mountain-deep`,
  `--crust`, `--fade-depth`, `--ease-glide`, `--ease-assemble`,
  `--ease-ripple`, `--dur-write` (90ms/letter), `--ripple-rest` (3).

### 6.5 Distance countdown

- **What & why.** A single counter, fixed in the navigation
  (§6.10), counts down the remaining distance in metres — 4,800 m
  at the departure, 0 m at the arrival — scrubbed to the walk. It
  belongs because it is the one law's (§1) second printing: the
  mountain shows the distance, the counter *says* it, and the two
  are the same function (§6.2), so they can never disagree. It is
  the page's one true number, measuring the reader's journey
  through the content.
- **Structure.** An `<output class="distance-readout">` in the
  horizon navigation (§6.10): the apparatus label `REMAINING`, the
  value in Inter 500 tabular, the unit `M`. The value is text —
  updated by the shared loop only when the whole-metre figure
  changes. It is not a link, not a button, not a progress bar with
  numbers glued on; it is an instrument reading, set in type.
- **Motion spec.** Pure function of rendered P (§6.2):
  `d = round(D0 × (1 − P))`, printed with thousands separators
  (4,800 → 576 across the approach; 576 → 0 across the arrival
  pin). No ticking, no odometer roll, no easing of its own — it
  inherits the approach lerp (0.06), which is why it moves like
  something far away: in whole metres, settling. At P=1 it prints
  `REMAINING 0 M` and stops; the label does not change, no
  fanfare state exists.
- **States.** Counting (P<1) → arrived (0 M, still). Scrolled
  back up: it counts up again, exactly — retreat is measured as
  honestly as approach. Hover/focus: none (not interactive).
- **Content merge.** The number measures *this page's* content —
  the distance to the section the visitor is travelling to, in
  the units the build declared (§6.14 prints the declaration).
  It is not a generic scroll percentage wearing a unit; §10
  gate 1 requires D0 and the function to be printed on the page.
- **Failure fallback.** No JS: the readout prints the departure
  figure `REMAINING 4,800 M` in the nav, and each section's
  waypoint stamp (§6.16) carries the distances as static text —
  the journey is still measured, in print. Loop killed: a
  watchdog recomputes d from raw scroll position every 500ms and
  corrects the readout — the one number is never left wrong by a
  dead instrument.
- **Reduced-motion variant.** The readout updates in steps at
  section boundaries (each waypoint's printed value, §6.16) as
  the reader passes them, rather than scrubbing — the number
  still falls, in strides.
- **Performance budget & mobile variant.** One text write per
  whole-metre change; negligible. Mobile: the readout stays in
  the nav (§6.10's compact bar) at 13px — the instrument is never
  hidden to save space; a build that drops the counter on mobile
  has dropped the gauge, and §10 fails it.
- **Choreography timeline (v2).** Continuous with §6.2: each
  frame, d is recomputed from rendered P; if the rounded value
  changed, the text is written (batched with the loop's other
  writes). Across the arrival pin (P 0.88→1) the same rule runs
  — 576 metres over 150vh of pin scroll — the slowest, most
  legible counting on the page, by design.
- **State matrix (v2).** *Rest:* value at the P-true figure.
  *Hover:* none. *Focus:* not focusable; it is readable in place
  in the nav's tab order position as static text. *Active:* n/a.
  *Scrolled-past (P=1):* `0 M`, final. *Disabled:* a build with
  no declared D0 may not ship the counter — gate 1. *Touch:*
  identical; fling momentum moves P and the number follows at
  the lerp's pace, settling after the fling ends.
- **Breakpoints (v2).** ≥1200px: full readout in the nav's right
  cluster. 768–1199px: same, label shortened to the value +
  `M` only (the word REMAINING is carried by the nav's
  `aria-label`). <768px: value + `M`, 13px, always visible —
  never behind a menu.
- **Edge cases & failure modes (v2).** *D0 not divisible
  cleanly:* rounding is to whole metres, half up; the arrival
  must read exactly 0 (the formula guarantees it at P=1).
  *Negative or >D0 readings* (overscroll): P is clamped before
  d is computed — the counter never prints −3 M or 4,812 M.
  *Locale:* separators follow the document locale; the unit
  is always `M` (metres are the theme's unit; a build in miles
  declares `MI` in §6.14 and converts D0 honestly — it does not
  relabel metres).
- **Accessibility spec (v2).** The readout is plain text in the
  nav, *not* a live region — a number that changed every frame
  would shout over the page. Screen-reader users get the same
  distances from the waypoint stamps (§6.16), which are section
  headings' apparatus — the gauge in their medium, at their
  pace. The nav carries `aria-label="Remaining distance"` on
  the readout's container for context.
- **Tokens consumed (v2).** `--mountain-deep`, `--d0`,
  `--lerp-approach` (0.06).

### 6.6 Sight line draw

- **What & why.** In the journey section — the page's one
  explicitly cartographic moment — a thin sight line draws
  itself from the horizon point beneath the visitor's current
  position to the mountain, across a drawn elevation of the
  route. It belongs because it is the visitor's own route,
  surveyed: the line is drawn on the landscape they are
  crossing, from where they stand to where they are going. It
  is the one place the theme shows its working.
- **Structure.** An inline SVG in the journey section (the
  section §7 assigns it): a flat elevation strip — the plain as
  a hairline, the mountain's profile at the right at its
  section-true scale, a marker for the visitor's position
  computed from P at the moment the section enters — and the
  sight line itself, a 1.5px path in `--reflection-deep` from
  the visitor marker to the mountain's summit. The drawing is
  real content (a figure with a caption, §12); the line's
  draw-on is JS-armed over a shipped-drawn path.
- **Motion spec.** Trigger: the figure's top crosses 70% of
  viewport height. The line draws over 1600ms `--ease-draw`
  (`stroke-dashoffset` from full length to 0). As it draws, the
  visitor marker pulses once (a 6px ring expanding and fading,
  800ms `--ease-ripple`) at the moment the line leaves it. It
  draws once; scrolling away and back does not redraw — a
  surveyed line stays surveyed. If P has advanced past the
  figure's own waypoint by the time it enters (a fast reader),
  the visitor marker is placed at the figure's waypoint value
  — the drawing shows the route as surveyed, not a live GPS.
- **States.** Undrawn (JS-armed only) → drawing (1600ms) →
  drawn (rest). Hover: the figure's caption gains its rule
  (§11 divider treatment); the line itself does not answer.
  Focus: the figure is a single tab stop only if the build
  makes it a link to the arrival; otherwise it is not focusable.
- **Content merge.** The line connects two real things on the
  page: the visitor's measured position (§6.5's function,
  printed as the marker's distance label) and the destination.
  It is a diagram *of the page itself* — remove the page and
  the diagram is meaningless, which is the test of merged
  content.
- **Failure fallback.** No JS: the line stands drawn, the
  marker placed at the figure's waypoint, its label printed.
  Watchdog: if the draw has not completed by 2600ms after the
  trigger, the path is forced to drawn. The line can never be
  left half-drawn by a stalled loop.
- **Reduced-motion variant.** Drawn at first paint of the
  section. The survey is information; only its drawing rests.
- **Performance budget & mobile variant.** One path animation,
  ≤0.1ms/frame. Mobile: the elevation strip compresses
  horizontally (the route is drawn to the figure's width, the
  mountain profile at 0.6×), the draw shortens to 1100ms; the
  marker's pulse is cut (small screens, small weather).
- **Choreography timeline (v2).** t=0 trigger → t=0–1600 line
  draws left to right → t=0 marker pulse (concurrent, 800ms)
  → t≈1200 the line passes the route's midpoint waypoint tick
  → t=1600 line reaches the summit; the summit point holds a
  2px dot (drawn, permanent) → drawn state; caption rule
  (§11) settles at t=1700.
- **State matrix (v2).** *Rest:* drawn line, labelled marker.
  *Hover:* caption rule only. *Focus:* as hover, if focusable.
  *Active:* if linked, activation jumps to the arrival (the
  one licensed teleport — a map may be used as a map).
  *Scrolled-past:* drawn, still. *Disabled:* a build with no
  journey section omits §6.6 entirely — the element belongs
  to that section, not to the theme's every page. *Touch:*
  identical; no pulse on tap.
- **Breakpoints (v2).** ≥1200px: figure spans the content
  column (≤880px), elevation strip 120px tall. 768–1199px:
  strip 96px. <768px: strip 72px, mountain profile 0.6×,
  marker label moves above the line (it may not collide with
  the line at small widths).
- **Edge cases & failure modes (v2).** *P at extremes:* if
  the visitor reaches the journey section having barely
  scrolled (a short page), the marker sits near the left and
  the line is long — correct. If they arrive via anchor jump
  from the footer, the marker uses the section's waypoint
  (stated above) — the drawing never claims a position the
  function didn't give it. *Path length mis-measured*
  (`getTotalLength` on a hidden SVG): the figure is never
  `display:none` when armed; the watchdog covers the rest.
- **Accessibility spec (v2).** The SVG carries `role="img"`
  and a title naming the figure's fact: "Sight line from
  2,400 metres — your position — to the destination." The
  marker's distance is also printed as apparatus text beside
  the figure (not only inside the SVG). The draw is decorative
  over a complete, labelled diagram.
- **Tokens consumed (v2).** `--reflection-deep`,
  `--reflection`, `--mountain`, `--ease-draw`, `--ease-ripple`,
  `--dur-sight` (1600ms).

### 6.7 Flag flutter

- **What & why.** The page's only warm element: a small orange
  flag on a short pole at the destination, standing where the
  mountain meets the arrival ground. It flutters **once** when
  it is first revealed at the pinned arrival, and **once** when
  hovered (or focused) thereafter — never in a loop, never as
  an idle animation. It belongs because it is the goal made
  visible: after a page of white and grey-blue, one warm,
  living thing marks the exact spot the visitor has been
  walking to. Its restraint is its meaning — a flag that waved
  forever would be a decoration; a flag that moves twice is an
  event.
- **Structure.** An inline SVG, 54×40px at rest, planted at the
  arrival composition's ground line (§6.13): a 2px pole in
  `--mountain-deep`, and the cloth — a single path in `--flag`,
  the system's only `--flag` instance (§2's warm audit). The
  cloth's wave is a path morph between two authored shapes
  (rest shape, gust shape), driven by JS over the flutter's
  duration; the rest shape ships in the DOM. The flag is part
  of the arrival figure (§6.13) and is `aria-hidden` — it is
  a seen thing, and the arrival's heading carries its meaning
  in words.
- **Motion spec.** Reveal flutter: triggered when the arrival
  pin's progress crosses q=0.55 (d ≈ 300m, §6.2 phase 2) — the
  flag becomes visible as the mountain docks, standing still
  for one beat, then flutters once: three oscillations of the
  cloth path (gust → rest → smaller gust → rest) over 1200ms
  `--ease-flutter`, amplitude decaying 100% → 55% → 25%. Hover
  flutter: the same 1200ms gesture, re-triggerable only after
  it completes (no queue, no restart mid-flutter — a second
  hover during a flutter is ignored). There is no third kind
  of flutter. Ambient wind does not exist on this page.
- **States.** Hidden (before q=0.55 — the flag is not rendered
  at all, not faded, not scaled: absent, the way a real flag
  is absent from a horizon it is too far to see) → revealed
  (standing) → fluttering (1200ms) → standing. Scrolled back
  above the arrival: the flag stays revealed (the visitor has
  seen the destination; the page does not unshow it), standing.
- **Content merge.** The flag marks the destination the whole
  page approaches — it is planted in the arrival composition
  at the exact ground point the CTA serves. It is not a logo,
  not a badge on a card, not a sale sticker: it exists once,
  at the goal, because the goal is where a flag goes.
- **Failure fallback.** No JS: the flag stands in the arrival
  figure at rest shape — visible, warm, still. The reveal
  choreography is JS theatre; the flag's *presence* at the
  destination is content and ships in the DOM of §6.13.
- **Reduced-motion variant.** The flag is simply present at
  the arrival, at rest shape, from first paint of the section.
  No flutter of either kind. A still flag is not a lesser
  flag; it is the same flag on a windless day.
- **Performance budget & mobile variant.** One path morph,
  1200ms, twice per session at most (plus deliberate hovers);
  ≤0.1ms/frame while running, zero otherwise. Mobile: the
  flag is 44×33px; the hover flutter is replaced by a tap
  flutter on the arrival figure (touch has no hover — §
  state matrix) with the same once-per-gesture rule.
- **Choreography timeline (v2).** Reveal: q crosses 0.55 →
  t=0 flag rendered, standing → t=350 (one beat of stillness —
  the eye finds it before it moves) → t=350–1550 the flutter:
  gust peak at t≈600, second at t≈1000 (55%), third at
  t≈1350 (25%) → t=1550 standing, forever, unless hovered.
  Hover flutter: t=0 gust → same decay → t=1200 standing.
- **State matrix (v2).** *Rest:* standing, warm, still.
  *Hover:* one flutter (desktop, pointer over the arrival
  figure). *Focus:* focus on the arrival's CTA triggers one
  flutter — keyboard visitors get the event too. *Active:*
  n/a. *Scrolled-past:* standing. *Disabled:* n/a — the flag
  has no disabled state; it is not a control. *Touch:* tap on
  the arrival figure flutters once; taps elsewhere never do.
- **Breakpoints (v2).** ≥1200px: 54×40px at the arrival
  ground line, pole 34px. 768–1199px: 48×36px. <768px:
  44×33px, pole 28px. The flag never scales with the mountain
  — it is encountered only at full-size range, which is the
  point: some things are only visible when you arrive.
- **Edge cases & failure modes (v2).** *The double-warm
  failure:* a build that also tints the CTA `--flag` on hover
  fails §2's audit (grep counts `--flag` usages: exactly the
  cloth path, plus its token definition). *Reduced-motion +
  session revisit:* flag present and still — consistent.
  *Arrival reached by anchor jump:* the flag is revealed
  without the flutter if the jump lands past q=0.55 (the
  visitor teleported; the flag does not perform for a
  teleport) — it flutters on their first hover instead.
- **Accessibility spec (v2).** `aria-hidden`; no text, no
  meaning carried solely by it (§2: its contrast is low
  because nothing depends on reading it). The flutter is
  brief, small and non-repeating — within ambient limits.
  Focus-triggered flutter (§ state matrix) ensures the event
  is not pointer-exclusive.
- **Tokens consumed (v2).** `--flag`, `--mountain-deep`,
  `--ease-flutter`, `--dur-flutter` (1200ms).

### 6.8 Long-range CTA lean

- **What & why.** The arrival's CTA leans toward the visitor's
  pointer from as far as 300px away — a few pixels at most,
  like something calling across distance. It belongs because
  it is the theme's one piece of magnetism, rationed to the
  destination: after a page that refused every lean, tilt and
  follow, the goal itself reaches — slightly — for the
  visitor. Desire expressed as geography. Every other
  interactive element on the page stands still (§5).
- **Structure.** The CTA is a cut block (§11) inside the
  arrival composition (§6.13): mountain ground, salt label,
  min-height 52px. A proximity listener on the arrival section
  computes the pointer's distance to the CTA's centre; the
  shared loop writes a `translate` toward the pointer,
  magnitude **m = clamp((300 − dist) / 300, 0, 1) × 6px**,
  directed along the pointer vector, lerped at 0.10. The lean
  is transform-only; the button's box never moves for layout,
  focus or reading order.
- **Motion spec.** Proximity radius 300px from the CTA's edge.
  At 300px: m=0. At 150px: m=3px. At the edge: m=6px, held
  while hovered (the lean becomes the hover state — there is
  no additional hover travel; the button has *already* come to
  meet the pointer). On pointer exit, the lean releases over
  400ms `--ease-glide`. Press: the block presses 2px toward
  the page (`--ease-assemble` timing, 120ms) — the one
  conventional micro-interaction the theme permits itself, at
  the one place convention is welcome: the ask.
- **States.** Standing (pointer >300px) → leaning (0<m≤6) →
  hovered (m=6, rule inks per §11) → pressed (2px, 120ms) →
  standing. Focus (keyboard): the CTA does not lean — it
  takes the §11 focus ring and triggers the flag's flutter
  (§6.7) instead: the keyboard's welcome is the flag, not a
  lean it cannot see the cause of. Disabled (form invalid /
  submitting): lean suspended, block at rest, label per §6.13.
- **Content merge.** The leaning element is the destination's
  own action — the booking, the order, the pledge the whole
  approach exists for. Magnetism is not sprinkled on nav links
  and card buttons; it is the goal's gravity, and there is
  one goal.
- **Failure fallback.** No JS / no fine pointer: the CTA
  stands still and works — the lean is an approach, not a
  mechanism. Loop killed: the transform freezes wherever it
  is (≤6px — cosmetically irrelevant, functionally nothing).
- **Reduced-motion variant.** No lean, no press travel. The
  CTA stands, takes its ring, and works. The flag's focus
  flutter is also absent under reduced motion (§6.7) — the
  welcome is the words.
- **Performance budget & mobile variant.** One proximity
  computation per pointermove (throttled to the loop's
  frames), one transform write; negligible. Mobile / coarse
  pointers: the lean does not exist — touch has no approach,
  and faking one from scroll position is refused. The CTA's
  full size and placement carry the welcome instead.
- **Choreography timeline (v2).** Pointer enters 300px →
  loop begins writing m per the formula, closing at lerp
  0.10 (m reaches ≈90% of target in ~350ms) → pointer crosses
  the edge: m settles at 6px → press: 2px in 120ms, release
  200ms → pointer exits: m decays to 0 over 400ms
  `--ease-glide`. No step of this moves any other element.
- **State matrix (v2).** *Rest:* standing. *Hover:* m=6 +
  §11 hover rule. *Focus:* ring + flag flutter (§6.7);
  no lean. *Active:* 2px press. *Scrolled-past:* the lean
  only exists while the arrival is on screen; off-screen,
  the listener sleeps. *Disabled:* standing, dimmed per
  §11, lean off. *Touch:* no lean (above); tap = press
  state only.
- **Breakpoints (v2).** ≥1200px: radius 300px, max lean 6px.
  768–1199px: radius 220px, max lean 5px (a smaller room,
  a shorter call). <768px: no lean at any size — the CTA is
  full-width in the arrival column (§6.13) and needs no
  gravity.
- **Edge cases & failure modes (v2).** *Pointer teleports*
  (mouse jumps across the section): m follows the formula
  from the new position — the lerp absorbs the jump; the
  CTA never snaps. *Two CTAs in the arrival* (a primary and
  a secondary, §6.13 permits one secondary): only the
  primary leans; the secondary stands — one gravity well.
  *The lean and the mirror-break (§6.9):* a click that
  lands on the CTA does not also fire the arrival's ripple;
  the ripple's listener excludes interactive elements.
- **Accessibility spec (v2).** The lean is ≤6px, slow and
  pointer-caused — it never moves the target out from under
  a user (it moves *toward* the pointer, and its hit box is
  the untransformed box plus the transform, per platform
  behaviour; the build verifies a slow pointer can land it
  at maximum lean). Target ≥52px tall, ≥120px wide. Focus
  is the §11 ring — never the lean, never the flag's colour.
- **Tokens consumed (v2).** `--mountain`, `--salt`,
  `--ease-glide`, `--ease-assemble`, `--lean-max` (6px),
  `--lean-radius` (300px).

### 6.9 Mirror-break ripple

- **What & why.** A click (or tap) anywhere in the arrival
  section — on the ground, not on a control — breaks the
  mirror-calm with a single expanding ripple ring across the
  arrival's reflection field: one ring, growing from the
  touch point's mirror position, fading as it reaches the
  field's edge over 900ms. It belongs because it is the
  visitor's one disturbance of the world they have crossed
  to: everything on the page has answered the walk; at the
  destination, the visitor answers back, once per touch, in
  water. It is also the arrival's confirmation that the
  mirror is a material, not a picture.
- **Structure.** The arrival section (§6.13) carries a
  `.mirror-field` (its reflection zone, beneath the arrival
  horizon) with an SVG overlay for rings: each break spawns
  one `<ellipse>` centred at the click point mirrored across
  the arrival horizon, rx growing 0→field width × 0.6,
  ry = rx × 0.18 (the flat ellipse of a ripple on a
  horizontal mirror), stroke `--reflection-deep` at 1.5px,
  opacity 0.55→0. Rings are removed at animation end. The
  overlay is `pointer-events: none`, `aria-hidden`; the
  listener is on the section, excluding interactive
  descendants (§6.8's rule).
- **Motion spec.** Trigger: pointerdown on the arrival
  ground. One ring per pointerdown; a second pointerdown
  while a ring lives replaces it (the water takes the latest
  touch — no ring spam, max 1 live ring). Duration 900ms
  `--ease-ripple`: rx reaches 60% in the first 300ms, then
  slows into the fade — a real ripple's energy curve. The
  underlying reflections (§6.3) receive a local amplitude
  bump (a +6, decaying over the same 900ms) at the ring's
  centre, so the ring and the water agree.
- **States.** Calm → breaking (900ms) → calm. There is no
  idle state, no loop, no ambient ring. Scrolled away
  mid-ring: the ring finishes or is culled off-screen — it
  never follows the visitor up the page.
- **Content merge.** The ring expands across the *arrival's
  own reflection* — the doubled destination. The visitor
  disturbs the mirror of the thing they came for. A ripple
  on a generic background would be a toy; a ripple across
  the destination's reflection is a signature on the place.
- **Failure fallback.** No JS: no rings, and nothing is
  missing — the element is pure response, carrying no
  content. Loop killed mid-ring: the ring freezes, then the
  section's watchdog removes live rings after 1200ms — no
  fossil ripples.
- **Reduced-motion variant.** No ring. A pointerdown on the
  ground produces a brief, static thickening of the arrival
  horizon hairline (1px→3px for 300ms, opacity only — the
  §1 weather line acknowledging the touch without moving).
  Even this is optional; silence is also a valid reduced
  answer.
- **Performance budget & mobile variant.** One SVG element
  animated for 900ms per touch; ≤0.1ms/frame. Mobile:
  identical (tap = pointerdown); the ellipse's ry ratio
  holds at small widths, rx capped at the field's width.
- **Choreography timeline (v2).** t=0 pointerdown → ring
  spawns at the mirrored point, rx=0, opacity 0.55 → t=300
  rx at 60% of final, local ripple bump peaking → t=900
  rx final, opacity 0, element removed, bump decayed →
  calm. The flag (§6.7) does not flutter for a ground click;
  the water and the cloth have different triggers and do
  not borrow each other's.
- **State matrix (v2).** *Rest:* calm field. *Hover:* no
  response — water is not disturbed by a shadow. *Focus:*
  no response. *Active:* the pointerdown *is* the active
  moment; keyboard users get no ring (there is no ground
  to press by keyboard) and lose nothing. *Scrolled-past:*
  rings cull off-screen. *Disabled:* n/a. *Touch:* tap =
  ring, with the 300ms tap-delay removed by
  `touch-action: manipulation` on the section.
- **Breakpoints (v2).** ≥1200px: rx max = field width × 0.6
  (≈520px in the arrival column). 768–1199px: × 0.55.
  <768px: rx max = field width × 0.9 (a narrow field takes
  a relatively wider ring, so the gesture still reads).
- **Edge cases & failure modes (v2).** *Clicks on the form*
  (§6.13): excluded — typing is not a touch on the ground.
  *Rapid tapping:* replace-rule keeps one ring; the water
  reads as repeatedly touched, never as a screensaver.
  *The ring over text:* the mirror field holds reflections
  only (§4: sentences don't reflect), so a ring can never
  cross live text — legibility is structurally guaranteed.
- **Accessibility spec (v2).** Purely decorative response;
  `aria-hidden`, no announcement, no focus change. The
  gesture is an enhancement with no information content —
  nothing about the arrival depends on it.
- **Tokens consumed (v2).** `--reflection-deep`,
  `--reflection`, `--crust-deep`, `--ease-ripple`,
  `--dur-break` (900ms).

### Page-family elements

### 6.10 Horizon navigation (page family: navigation)

- **What & why.** A single slim bar fixed at the top of the
  viewport — the visitor's instrument panel for the crossing.
  Left: the wordmark (the destination's name, Instrument
  Serif, unmirrored — the instruments don't reflect, §3 law
  1). Centre: the route's stations as text links (the
  sections, named as places). Right: the distance readout
  (§6.5). It belongs because a crossing needs exactly three
  things from its furniture: whose flat this is, what the
  stations are, and how far remains. Nothing else is admitted
  to the bar.
- **Structure.** A `<header class="horizon-nav">`, 56px tall,
  salt ground at 92% opacity with a 1px bottom rule in
  `--crust-deep` — the bar is a hairline with instruments on
  it, not a banner. Stations are a `<nav>` of anchor links to
  the sections; the current station (from the shared loop's
  section tracking) is marked with a 2px mountain rule beneath
  its label and `aria-current="true"`. No menu button exists
  on desktop; on mobile the stations collapse into one
  "Stations" disclosure (§ state matrix), the readout never
  collapses (§6.5).
- **Motion spec.** The bar does not animate in — it is present
  at first paint (instruments are not revealed). The current-
  station rule slides between stations over 300ms
  `--ease-glide` as sections pass the viewport's centre. The
  bar's ground gains its crust rule only after the first
  scroll (at P=0 the bar is borderless over the hero's sky —
  the departure has no furniture edge). Nothing else moves.
- **States.** Departure (P=0, borderless) → travelling
  (ruled, current station marked) → arrived (P=1: readout at
  0 M, the arrival station marked). Hover on a station: its
  label inks mountain-deep → mountain, 150ms. Focus: §11
  ring. The wordmark is a link home (to P=0) — the only
  "back" the theme needs.
- **Content merge.** The nav's stations are the page's real
  sections and its readout is the page's real gauge (§6.5) —
  the bar is the journey's dashboard in the literal sense,
  and it carries no marketing: no CTA lives in the nav. The
  ask is at the destination; a nav CTA would be a second
  destination (§1).
- **Failure fallback.** No JS: the bar stands complete —
  wordmark, station anchors (native), the departure readout
  printed (§6.5). Current-station marking is absent (it is
  the only JS-dependent part) and nothing is lost: the
  stations are still links.
- **Reduced-motion variant.** The station rule jumps instead
  of sliding. Everything else is identical — the bar was
  never in motion to begin with.
- **Performance budget & mobile variant.** Static bar, one
  sliding rule; negligible. Mobile (<768px): 48px tall;
  stations behind the "Stations" disclosure (a native
  `<details>`-pattern panel listing the same anchors);
  wordmark shortens to the destination's mark if the build
  declares one; the readout stays right, always (§6.5).
- **Choreography timeline (v2).** Load: bar present. First
  scroll: bottom rule fades in over 300ms. Section changes:
  the current-station rule slides 300ms `--ease-glide`,
  `aria-current` migrates at the slide's midpoint (t=150) so
  assistive tech never hears two currents. P=1: the arrival
  station takes the rule; the readout settles at 0 M (§6.5).
- **State matrix (v2).** *Rest:* as above. *Hover:* station
  labels ink; the readout ignores hover. *Focus:* ring on
  the focused link; the current-station rule does not chase
  focus (it marks scroll position, not attention).
  *Active:* anchor jump — the approach snaps (§6.2's jump
  rule) and the bar's marks follow P. *Scrolled-past:* n/a
  (fixed). *Disabled:* a station whose section was withdrawn
  leaves the nav (§6.16's withdrawn rule) — the bar never
  links to a view that isn't there. *Touch:* stations
  disclosure opens on tap; targets ≥44px in the panel.
- **Breakpoints (v2).** ≥1200px: full bar, all stations
  inline (builds with >6 stations group the middle ones —
  a crossing has few stations by law, §4). 768–1199px:
  stations inline, wordmark may shorten. <768px: disclosure
  pattern, readout always visible.
- **Edge cases & failure modes (v2).** *Long station
  names:* apparatus truncates at 18ch with the full name in
  the link's accessible name — the bar never wraps to two
  lines; a wrapped instrument panel is a broken one.
  *Anchor jump to arrival:* the bar's state lands in
  "arrived" without ceremony (§6.2's jump rule governs).
- **Accessibility spec (v2).** Landmark `header` + `nav`
  with `aria-label="Stations"`. `aria-current` on exactly
  one station. The readout is plain text (§6.5's spec).
  Skip link (§11) is the bar's first element. Contrast:
  labels mountain-deep on salt 9.95:1; the current rule is
  decoration over a label that already reads.
- **Tokens consumed (v2).** `--salt`, `--crust-deep`,
  `--mountain`, `--mountain-deep`, `--ease-glide`.

### 6.11 The departure — hero composition (page family: hero)

- **What & why.** The first screen is the departure: a wide,
  empty composition — sky field above the master horizon,
  the mountain a speck at its centre, the mirrored headline
  (§6.4), the destination word written on the crust, the
  distance readout's first full statement, and one scroll
  cue. It belongs because the theme's promise is made here
  or nowhere: *there is one thing, it is far, and the page
  is the walk to it.* Everything the visitor needs to decide
  to travel is on this screen; everything else is the
  travelling.
- **Structure.** A 100vh (min 640px) section. Top: the nav
  (§6.10) overlays its sky. Centre band: the mountain ride
  at P=0 (§6.2 — 0.12 scale, 67px wide on desktop) seated on
  the master horizon, with §6.1's assembling reflection
  below. Upper-left quadrant: the headline (§6.4) in the sky
  field. Lower field, on a crust band: the destination word
  (§6.4). Bottom-left: the departure statement — one line of
  body copy and the full readout (`REMAINING 4,800 M — THE
  LODGE`, in the build's terms). Bottom-right: the scroll
  cue, a text link ("Walk", §12) anchored to the first
  station, with a 24px vertical rule that draws and undraws
  on a 2400ms cycle — the hero's one permitted idle motion
  besides the haze and glints (§5).
- **Motion spec.** The §6.1 + §6.4 ceremonies run here
  (assembly 2000ms, headline from t=500, word from t=900,
  all complete by 2400ms). The heat haze shimmers at the
  horizon (±14px band, 7000ms cycle, amplitude 2px, §5).
  Salt glints: ≤5 in the hero (of the page's ≤12), each a
  300ms `--glint` sparkle every 4–9s at seeded positions on
  the crust band. The scroll cue's rule cycles 2400ms
  `--ease-draw` (draw 900ms, hold 600ms, undraw 900ms) —
  it stops cycling the moment P>0.01 (the visitor is
  walking; the cue has done its work) and never resumes.
- **States.** Ceremony → standing (rest) → departed
  (scrolled past: the hero's local elements rest; the
  mountain has joined the ride). The glints and haze pause
  when the hero leaves the viewport (IntersectionObserver)
  — ambient motion never plays to an empty room.
- **Content merge.** The hero contains no teaser copy, no
  preview cards, no "highlights" — it contains the
  destination (small), its name (written), the distance
  (printed) and the first step (the cue). It is not an
  introduction to the content; it is the content's far end,
  seen from its near end.
- **Failure fallback.** No JS: the complete departure
  stands — mountain at 0.12 with calm reflection, headline
  and its mirror, word whole, readout printed, cue a plain
  anchor. The ceremonies are the only JS-dependent layer.
- **Reduced-motion variant.** The standing departure at
  first paint; no haze, no glints, the cue's rule static
  and fully drawn. The composition is unchanged — stillness
  was always its subject.
- **Performance budget & mobile variant.** The hero pays
  §6.1 + §6.4's budgets plus ≤5 glint timers; ≤0.6ms/frame
  during ceremony, ≤0.2 at rest. Mobile: min-height 560px;
  the headline moves above the mountain's corridor (the
  corridor law, §4, at ±60px); the departure statement and
  cue stack at the bottom; glints ≤3.
- **Choreography timeline (v2).** t=0 nav present, bar
  borderless → t=0–800 mountain fades (§6.1) → t=500
  headline rises, reflection assembles → t=900 word begins
  writing → t≈2000 assembly settles → t≤2400 word complete,
  departure statement fades in last (400ms `--ease-assemble`
  — the facts arrive after the place) → rest: haze + glints
  + cue cycle only → first scroll: cue cycle stops, nav
  gains its rule (§6.10).
- **State matrix (v2).** *Rest:* standing departure.
  *Hover:* only the cue and nav answer (§6.10). *Focus:*
  the cue takes §11's ring; nothing else in the hero is
  focusable except nav. *Active:* cue activation = anchor
  to station 1. *Scrolled-past:* ambient paused, ceremony
  never re-runs on return (session rule). *Disabled:* n/a.
  *Touch:* identical; the cue is a ≥44px target.
- **Breakpoints (v2).** ≥1200px: as structured. 768–1199px:
  headline 40px, mountain corridor ±75px. <768px: stacked
  bottom cluster, corridor ±60px, word on the crust band
  full-width, min-height 560px.
- **Edge cases & failure modes (v2).** *Short viewports*
  (landscape phones, 380px tall): min-height yields to
  content — the hero becomes 100svh with the statement
  below the fold rather than crushing the corridor; the
  horizon stays at 56% of the *first* screen by using
  `svh` units throughout the ride (§6.2). *The word is
  long:* §6.4's rules govern. *A build whose destination
  needs a sub-line:* one line of body copy is permitted
  under the word — the departure statement absorbs it; a
  second line is a second object (§4).
- **Accessibility spec (v2).** The hero's heading order:
  headline is the page's `h1`; the word is a `<p>` styled
  as display (it is a name, not a heading — the arrival's
  heading is the destination's `h1`-level peer, §6.13).
  The mountain's accessible name lives here (§6.2). The
  cue's text is "Walk to [station 1 name]", not "scroll".
- **Tokens consumed (v2).** `--salt`, `--crust`,
  `--mountain`, `--glint`, `--haze`, `--ease-assemble`,
  `--ease-draw`, `--horizon` (56vh).

### 6.12 Paired plates (page family: cards / listing)

- **What & why.** Every content image on the plain is a
  **paired plate**: the image standing on its local horizon,
  its exact reflection falling beneath it, a caption below
  the water. Listings are sequences of plates — one per view
  (§4) — each plate a thing the visitor has walked to. It
  belongs because it is how content exists in this world:
  nothing floats, nothing is cropped into a grid of
  thumbnails; an image is an object on the flat, with the
  water it deserves. A grid of twelve cards would be a
  parking lot on the salt.
- **Structure.** A `<figure class="plate">`: the image (or
  authored SVG) in `.plate-object`, base seated on the
  plate's local horizon line (a 1px `--crust-deep` rule at
  the image's foot, continuous with the composition); the
  `.reflection` (§6.1's construction: flipped, veiled,
  displaced at rest 3, §6.3-responsive); a `<figcaption>`
  beneath the mirror field — name, and one line of fact
  (§12). Plates in a listing are separated by open ground
  (§4: one per screen at ≥1200px; the listing's rhythm is
  walk–stand–walk). The whole figure may be a link (to the
  detail view) — the caption's title is the link text; the
  reflection is never a separate target.
- **Motion spec.** Entry: as the plate's base crosses 75%
  of viewport height, the object settles 12px into place
  over 600ms `--ease-assemble` while its reflection
  assembles beneath (opacity 0→0.62, displacement 14→3,
  900ms `--ease-ripple`) — §6.1's grammar at plate scale.
  Parallax: while the plate crosses the viewport, object
  and reflection translate at mirrored rates (§5): object
  −8px across the crossing, reflection +8px, written by the
  loop from the plate's own progress — they separate and
  rejoin like a thing and its water. Hover/focus: the
  reflection *calms* — its velocity amplitude is driven to
  0 over 400ms regardless of page weather (§6.3) and the
  displacement eases to 2: looking closely stills the
  water. That is the plate's only hover effect; the object
  does not lift, tilt or zoom.
- **States.** Approaching (reflection assembling) →
  standing (calm or weather-rippled) → examined (hover/
  focus: water stilled) → scrolled-past (assembled, still
  weather-responsive until off-screen). A plate whose image
  failed to load shows its caption and a crust ground with
  the image's declared aspect — a marked empty standing
  place (§ edge cases), never a broken-icon glyph.
- **Content merge.** The plate *is* the content item —
  product, room, artwork, person. Its reflection is not a
  style applied to a card; it is the item's presence in the
  world. The caption carries the item's real name and fact;
  the link, where present, goes to the item's real detail.
- **Failure fallback.** No JS: plate standing, reflection
  assembled at rest displacement, caption printed.
  Watchdog: reflection forced assembled 1000ms after the
  plate enters. Slow image: the reflection assembles on the
  object's *box* (aspect declared in markup) — the water
  does not wait for the photograph.
- **Reduced-motion variant.** Plates stand assembled; no
  settle, no parallax separation, no calming (the water is
  already still, §6.3). Hover changes nothing but §11's
  link underline.
- **Performance budget & mobile variant.** Per plate: one
  image + one flipped reuse (no second download — the
  reflection is the same resource, transformed), one filter
  reference (§6.3's shared budget). On-screen plates ≤3 by
  the density law → ≤0.5ms/frame. Mobile: plates stack one
  per view still (the law holds); reflection depth 0.5× the
  object's height (max 140px); parallax separation halves
  to ±4px.
- **Choreography timeline (v2).** Base crosses 75% → t=0
  object settle begins (600ms), reflection opacity rises →
  t=300 displacement ≈8 → t=900 reflection at rest 3,
  assembled → crossing: parallax writes per frame from the
  plate's progress → hover: t=0–400 amplitude →0,
  displacement →2 → unhover: the plate rejoins the page
  weather over 600ms.
- **State matrix (v2).** *Rest:* standing, weather ripple.
  *Hover:* water calms (desktop). *Focus:* water calms,
  identically; caption title takes §11's ring if linked.
  *Active:* link activation (if any) — §6.15's horizon
  hold. *Scrolled-past:* assembled; parallax complete
  (object and reflection rejoined at their rest offset 0).
  *Disabled:* a withdrawn item's plate is removed whole —
  object, water, caption; the listing's ground closes up
  (§6.16's stamp rule re-computes the survivors' distances
  only if the build's stamps are positional — §6.16
  governs). *Touch:* no hover calm; a tap is the link, or
  nothing.
- **Breakpoints (v2).** ≥1200px: plate object ≤720px wide,
  one per view. 768–1199px: ≤600px, one per view (views
  may shorten to 90vh). <768px: full column width,
  reflection ≤140px deep, one per view with 60vh of ground
  between plates.
- **Edge cases & failure modes (v2).** *Portrait vs
  landscape objects:* the reflection's depth is capped at
  0.62× the object's height for tall objects (a portrait's
  full mirror would flood the view) — the cap is declared
  in the build, applied uniformly. *Image with transparency
  (a cut-out product):* it stands on the horizon rule
  directly — the rule is its ground; a fake floor shadow is
  refused (§9). *The caption is long:* two lines max; the
  fact is edited, not shrunk (§3 sizes are floors).
- **Accessibility spec (v2).** The object image carries
  real alt text; the reflection is `aria-hidden` (a
  duplicate). Figure/figcaption semantics throughout. If
  the plate is a link, the whole figure is one target
  ≥44px in its caption zone, with the image itself
  clickable — one target, not three. Calm-on-focus gives
  keyboard users the same examined state as hover.
- **Tokens consumed (v2).** `--crust-deep`, `--reflection`,
  `--fade-depth`, `--mountain-deep`, `--ease-assemble`,
  `--ease-ripple`, `--ripple-rest` (3).

### 6.13 The arrival & destination form (page family: forms / conversion)

- **What & why.** The final section is the arrival: the
  mountain at full size, docked in-flow; the flag standing
  (§6.7); the CTA (§6.8); and beneath them, the destination
  form — the booking, order or pledge the whole page walks
  to. It belongs because the theme's geography must pay
  off: the visitor did not cross 4,800 metres for a mood.
  The arrival is the one dense composition (§4), and its
  form is written like a guest book at the end of a road —
  few fields, ruled lines, no boxes shouting for data.
- **Structure.** A section of 100vh + 150vh of pin travel
  (§6.2 phase 2). The pinned composition: the in-flow
  mountain (560px, its reflection in the arrival mirror
  field, §6.9), the flag at its ground line, the section
  heading (the destination's name, Instrument Serif 40–64px,
  unmirrored — the heading is read, not reflected; §3 law 1
  permits the exception because the arrival's mirror field
  is §6.9's water, already occupied), the CTA block (§6.8),
  and — released from the pin, immediately below — the
  form: single column ≤560px, fields as ruled lines (§11),
  the submit a cut block matching the CTA's grammar. The
  pin's progress q maps to §6.2's P 0.88→1.
- **Motion spec.** Pin engages when the arrival's top
  reaches the viewport top. q 0→0.25: custody crossfade of
  the mountain (fixed ride → in-flow, §6.2, 300ms
  `--ease-glide`). q 0.25→0.55: the arrival heading and CTA
  settle in (each 500ms `--ease-assemble`, staggered
  120ms) — they were not hidden before the pin (they ship
  visible in-flow below the fold of the pinned frame; the
  settle is a refinement for the pinning browser, and
  no-JS/no-pin builds show the section as a normal tall
  section with everything standing). q=0.55: the flag
  reveals and flutters (§6.7). q→1: the counter reaches 0
  (§6.5). Pin releases into the form. Form submit: the
  block presses (§6.8's press), the form's fields hold
  their values through any failure (§ edge cases), and on
  success the form is replaced by the confirmation — a
  ruled record (§6.14's voice) naming the reference the
  system actually returned.
- **States.** Approaching (pin not engaged) → arriving
  (q 0→1) → arrived (pin released; form live) → submitted
  (confirmation record). Scrolled back above the pin: the
  composition stands (flag revealed, §6.7's rule); the pin
  does not re-perform its settles.
- **Content merge.** The arrival's contents are the site's
  actual conversion objects — the real rooms, the real
  price, the real form. The mountain in-flow here is the
  same SVG as the ride (§6.2) — the destination the visitor
  watched for 4,800 metres is the one they book beneath.
  No arrival may be a decorative finale with the form
  exiled to another page: that severs the geography, and
  §10 gate 6 fails it.
- **Failure fallback.** No JS / no pin support: the
  section is a tall static section — mountain full-size,
  flag standing, heading, CTA, form, all present and
  working in order. The pin is choreography over a
  complete section, never the section's container.
  Watchdog: if the pin's scroll library fails, the section
  unpins into normal flow within 500ms (the build uses
  native `position: sticky`, so failure means ordinary
  scrolling — by construction, not by rescue code).
- **Reduced-motion variant.** No pin. The section stands
  as the static composition (mountain, flag, heading, CTA,
  form) and the counter steps to 0 as the section enters
  (§6.5). The arrival is a place, not a performance.
- **Performance budget & mobile variant.** The pin is
  native sticky (compositor-driven); the loop writes only
  q-derived values already budgeted in §6.2/§6.5/§6.7.
  Mobile: the pin shortens to 100vh of travel; the
  mountain is 300px; the form follows in the same column
  without a release gap — on a phone, arrival and ask are
  one screen's scroll apart, not two.
- **Choreography timeline (v2).** Pin engages → q 0–0.25
  custody crossfade → q 0.3 heading settles (500ms) →
  q 0.4 CTA settles → q 0.55 flag reveals, beat, flutters
  (§6.7's timeline) → q 0.75 the mirror field (§6.9) arms
  → q 1.0 counter at 0 M, pin releases → the form's first
  field is the next thing on the page; focus is never
  moved by the pin — the visitor scrolls into the form as
  they walked into everything else.
- **State matrix (v2).** *Rest (arrived):* full composition
  standing, form live. *Hover:* CTA lean (§6.8), flag
  flutter (§6.7), field rules per §11. *Focus:* fields
  take §11's focus rule; CTA focus flutters the flag
  (§6.7). *Active:* submit press (§6.8). *Scrolled-past:*
  (past the form) the footer record (§6.14) follows; the
  arrival does not chase. *Disabled:* submitting state —
  fields keep values, submit disabled with its label
  changed to the sending state (§12), lean suspended.
  *Touch:* no lean; tap targets ≥48px in the form.
- **Breakpoints (v2).** ≥1200px: pin travel 150vh,
  composition centred, form ≤560px. 768–1199px: pin
  120vh, mountain 440px. <768px: pin 100vh, mountain
  300px, form full column; the flag at its mobile size
  (§6.7).
- **Edge cases & failure modes (v2).** *Form failure
  (network/validation):* nothing the visitor wrote is
  cleared; the error note stands above the form in §12's
  voice ("NOT SENT — THE FLAT KEPT YOUR WORDS." pattern,
  build-specific per §12) and the failed field's rule
  inks `--reflection-deep` with its message beneath —
  never `--flag` (§2: errors are not warm). *A build with
  no form* (a pure exhibition): the arrival holds the CTA
  alone (to the one external destination — a ticket, a
  visit) and gate 6 checks the CTA resolves to a real
  action, not a dead button. *Very long form:* the pin
  still releases at q=1; the form's length is ordinary
  scroll — the arrival never traps the visitor in a pin
  to fill fields.
- **Accessibility spec (v2).** The pin never traps focus
  (sticky, not a scroll-jacking container — keyboard and
  switch users scroll through it natively). The arrival
  heading is the section's `h2` (or the page's second
  `h1`-level landmark per build). Form fields: real
  labels, apparatus style (§3), errors linked by
  `aria-describedby`, error summary in the record voice.
  The counter reaching 0 is not announced (it is not a
  live region, §6.5) — the arrival heading announces the
  place in the reading order, which is the announcement.
- **Tokens consumed (v2).** `--mountain`, `--salt`,
  `--flag`, `--reflection-deep`, `--ease-glide`,
  `--ease-assemble`, `--dur-pin` (150vh).

### 6.14 The far-shore footer — the record (page family: footer)

- **What & why.** The footer is the survey's record, printed
  at the far shore: the declared approach function, D0 and
  what it measures, the waypoint table in miniature, the
  build's credits, and the ordinary footer facts (contact,
  legal) set as apparatus. It belongs because the one law
  (§1) requires the workings to be *on the page* — the
  footer is where a visitor who doubts the gauge can read
  exactly how the mountain grew and check it against the
  counter they watched. A theme about honest distance files
  its instruments' calibration in public.
- **Structure.** A `<footer>` on a crust ground, in three
  ruled bands. Band 1 — **the declaration**: the function in
  apparatus and one sentence of prose: `D0 = 4,800 M — THE
  ROAD FROM THE HIGHWAY'S END TO THE LODGE. SCALE = 0.12 ×
  D0 ÷ REMAINING.` (build-specific, generated from the same
  constants the loop uses — § edge cases). Band 2 — the
  waypoint table (§6.16's stamps, as a real `<table>`:
  station, distance remaining at its head, what stands
  there). Band 3 — credits and facts: who built the site,
  the typefaces, contact and legal links as ruled text
  links. The footer's top rule draws itself (§6.6's
  grammar, 1200ms `--ease-draw`) when the footer enters —
  the record signs itself.
- **Motion spec.** Only the rule draw (once) and nothing
  else: the footer is the stillest part of the page after
  the arrival. Links take §11's hover rule. No reflections
  exist in the footer — the far shore is dry ground; the
  mirror ends at the arrival.
- **States.** Standing, in all states. The declaration's
  figures are static text (generated at build time from
  the loop's constants — if the constants change, the
  footer is regenerated; a hand-edited footer figure is a
  gate failure, §10 gate 3).
- **Content merge.** The footer is the audit trail of the
  page's own central mechanism, plus the site's real facts.
  It is not a sitemap farm: links here are the record's
  (about the method, contact, legal) — navigation lives in
  §6.10.
- **Failure fallback.** Static by construction; the rule
  ships drawn and the draw is JS-armed theatre over it.
- **Reduced-motion variant.** Identical, rule pre-drawn.
- **Performance budget & mobile variant.** Negligible.
  Mobile: bands stack; the waypoint table becomes two
  columns (station, distance) with the "what stands there"
  column folded into the station cell as a second line —
  the figures are never dropped to save width.
- **Choreography timeline (v2).** Footer top crosses 85%
  → rule draws 1200ms → rest. That is the entire timeline;
  a footer with more choreography has misunderstood the
  shore.
- **State matrix (v2).** *Rest:* the record, printed.
  *Hover:* link rules ink. *Focus:* §11 ring. *Active:*
  link navigation (§6.15). *Scrolled-past:* n/a — it is
  the end. *Disabled:* a withdrawn station is struck from
  the waypoint table in the same build that withdraws its
  section (§6.16). *Touch:* links ≥44px.
- **Breakpoints (v2).** ≥1200px: three bands, table at
  full width ≤880px. 768–1199px: table ≤720px. <768px:
  stacked bands, two-column table as above.
- **Edge cases & failure modes (v2).** *Constants drift:*
  the declaration must be generated, not typed — the
  build injects D0 and the formula's constants from the
  same source the loop reads (a config object rendered
  server-side or at build time). §10 gate 3 verifies by
  changing the constant in a test build and watching the
  footer follow. *A D0 with no real-world referent:* the
  declaration sentence must still say what D0 measures
  (the page's own scroll, honestly: "D0 = 4,800 M — THE
  LENGTH OF THIS PAGE, COUNTED AS DISTANCE") — an
  undeclared fiction fails gate 1.
- **Accessibility spec (v2).** The table is a real table
  with apparatus headers. The declaration's formula is
  also stated in prose (the sentence beside it) — a
  formula alone is not an explanation for every reader.
  Footer landmarks and link names are plain ("Contact",
  "Privacy"), never apparatus jokes.
- **Tokens consumed (v2).** `--crust`, `--mountain-deep`,
  `--reflection-deep`, `--ease-draw`, `--d0`.

### 6.15 Crust skeleton + horizon-hold transition (page family: loader / transition)

- **What & why.** Waiting on this page looks like the flat
  before anything stands on it: content regions load as crust
  grounds with a hairline horizon and the ghost of a standing
  place — never spinners, never shimmering grey bars aping
  text. And moving between pages is a **horizon hold**: the
  line is kept on screen, the old view's objects sink into
  their reflections, the new view stands up across the same
  line. It belongs because the theme's continuity is the
  horizon; a transition that cuts to a blank white page has
  dropped the visitor off the flat entirely.
- **Structure.** Skeleton: `.crust-wait` regions — a crust
  ground block at the content's declared aspect, a 1px
  `--crust-deep` horizon rule at the region's 56% (the master
  ratio, §4), and beneath it a veiled, still reflection of
  nothing (the `--fade-depth` veil alone). No fake text lines:
  the skeleton shows *where a thing will stand*, which is all
  a survey can honestly show. Transition: an overlay holding
  the master hairline at 56vh over a salt field; the outgoing
  page's scroll is frozen beneath it for the hold's duration.
- **Motion spec.** Skeleton: static (a waiting flat does not
  pulse — pulsing crust is a loading spinner in disguise).
  Content arriving replaces the crust region with §6.12's
  assembly (reflection assembles, 900ms). If content has not
  arrived in 4000ms, the region prints its wait line in §12's
  voice ("STILL CROSSING — THE LINE IS SLOW HERE." pattern)
  with a retry control if the build has one. Transition:
  600ms total — t=0–250 the overlay's salt field rises to
  cover, hairline held at 56vh; t=250–350 the line holds
  alone (the held breath); t=350–600 the new page is revealed
  standing (its objects at rest states, §6.1 ceremonies do
  not re-run), line dissolving into the new page's own
  horizon. The mountain's scale is session-persisted
  (sessionStorage: last P per page path is *not* kept — the
  new page's own P rules; what persists is the *ceremony
  flags*, §6.1/§6.4, so a traversed site does not re-perform
  its greetings).
- **States.** Waiting → arrived (per region). Transition:
  idle → holding → released. A failed navigation (offline
  mid-transition) restores the old page fully — the overlay
  lifts and the visitor is where they were, scroll intact.
- **Content merge.** The skeleton's shape is the content's
  surveyed shape (declared aspects, the real horizon ratio);
  the transition's held line is the page's own master
  horizon — the furniture of the crossing, doing its job.
- **Failure fallback.** No JS: no skeleton (content is
  server-rendered or the page is static — the theme's builds
  are content-first), transitions are plain navigations.
  The skeleton exists only for genuinely async regions
  (a booking calendar, a gallery's later plates) and is
  JS-inserted, so no-JS never sees a wait state it can't
  leave.
- **Reduced-motion variant.** Transitions are instant (a
  plain navigation — the hold is theatre). Skeletons are
  already static. Nothing else changes.
- **Performance budget & mobile variant.** Overlay is one
  fixed div + one rule; transition cost is paint-only.
  Mobile: identical; the hold shortens to 450ms (a smaller
  crossing, a shorter breath).
- **Choreography timeline (v2).** Async region mounts →
  crust stands (static) → content ready → reflection
  assembles 900ms (§6.12) → region live. 4000ms without
  content → wait line prints. Transition: as the 600ms
  spec above; focus moves to the new page's `h1` at t=600
  (never during the hold — focus must not land in a page
  that isn't standing yet).
- **State matrix (v2).** *Rest:* no overlay, no skeletons
  (all regions arrived). *Hover/focus:* skeleton regions
  are inert and unfocusable. *Active:* a link click starts
  the hold only if the navigation is same-site and the
  build's router intercepts; external links navigate
  plainly — the flat does not perform exits. *Scrolled-
  past:* n/a. *Disabled:* a region whose fetch is
  abandoned (user navigated away) discards its skeleton
  silently. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px / 768–1199px / <768px: the
  skeleton mirrors its region's breakpoints (§6.12's
  plate sizes); the hold's line is at 56vh at every size
  — the master horizon does not move for small screens.
- **Edge cases & failure modes (v2).** *Instant content*
  (cached): if content arrives <150ms after the skeleton
  mounts, the skeleton never renders (a flash of crust is
  worse than a breath of nothing). *Back/forward cache:*
  the page restores with ceremonies complete and the
  mountain at its P — bfcache state is the truth.
  *Transition on a browser without a router:* plain
  navigation; the theme never requires an SPA.
- **Accessibility spec (v2).** Skeleton regions carry
  `aria-busy="true"` and, past 4000ms, the wait line is a
  polite live announcement (the page's only live region —
  rationed like everything else). Transition: focus
  management as in the timeline; the overlay is
  `aria-hidden`.
- **Tokens consumed (v2).** `--crust`, `--crust-deep`,
  `--salt`, `--fade-depth`, `--ease-assemble`,
  `--horizon` (56vh), `--dur-hold` (600ms).

### 6.16 Waypoints — the route's figures (page family: data)

- **What & why.** Every section opens with its **waypoint
  stamp**: the station's name and the distance remaining at
  that point — `THIRD VIEW — REMAINING 2,880 M` — computed
  from the section's actual position in the approach, by the
  same function that moves the mountain (§6.2). It belongs
  because it is the one law's third printing, and the one
  that serves readers the ride cannot: the stamps are text,
  in the reading order, true at the place they stand. A
  visitor who reads with the ride hidden still walks a
  measured route.
- **Structure.** A `.waypoint` block at each section's head:
  a 1px rule in `--reflection-deep` (the stamp's line, 48px
  wide), the station name in apparatus, and the remaining
  distance in apparatus tabular — `REMAINING 2,880 M`. The
  value is computed at build time (or first render) from
  the section's scroll offset ÷ total approach × D0,
  rounded to the nearest 10m (a stamp is a surveyed mark,
  not a live readout — §6.5 is the live one), and printed
  as static text in the DOM. The footer's table (§6.14)
  republishes the same stamps from the same computation.
- **Motion spec.** The stamp does not animate. Its rule is
  drawn once as the section enters (600ms `--ease-draw`)
  — the surveyor marking the spot as you reach it — and
  the figures never count, tick or scrub (type law 2:
  the counter is the only moving number). On window
  resize that changes section offsets by >2%, stamps are
  recomputed and reprinted — a resurveyed route restamps
  itself.
- **States.** Unmarked (rule undrawn, JS-armed) → marked
  (rule drawn, figures printed — the no-JS default state).
  There are no hover/focus states: a stamp is a signpost,
  not a control.
- **Content merge.** The stamp's distance is the section's
  real position in the page's argument — the third view
  really is 1,920m into a 4,800m page. It teaches the
  visitor to read the page as a route, and it makes the
  sections' order auditable: a stamp that falls out of
  sequence exposes a reordered page (§10 gate 3).
- **Failure fallback.** Static text by construction; the
  only JS role is the rule's draw and the resize resurvey.
  If offsets cannot be measured (a section is
  `display:none` in a variant), its stamp prints the
  build-declared value from §6.14's table — declared beats
  broken.
- **Reduced-motion variant.** The rule ships drawn.
  Identical otherwise.
- **Performance budget & mobile variant.** One computation
  per section per resurvey; negligible. Mobile: the stamp
  stays at the section head, same size — a small screen
  does not shorten the route's signage.
- **Choreography timeline (v2).** Section head crosses 80%
  → rule draws 600ms → marked, forever. Resize resurvey:
  stamps reprint instantly (no draw — a resurvey is a
  correction, not a ceremony).
- **State matrix (v2).** *Rest:* marked. *Hover:* none.
  *Focus:* not focusable. *Active:* n/a. *Scrolled-past:*
  marked, still — the stamps behind the walker stay true.
  *Disabled:* a withdrawn section's stamp is withdrawn
  with it, and the footer's table is regenerated (§6.14)
  — the route never advertises a view that isn't there.
  *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: stamp at the content
  column's left edge. 768–1199px: same. <768px: same,
  rule 36px (the mark narrows, the figures don't shrink).
- **Edge cases & failure modes (v2).** *Two sections at
  the same offset* (a zero-height interstitial): stamps
  may share a value; the build must merge or drop one —
  two stations at one distance is a survey error the gate
  catches (gate 3). *The arrival's stamp:* it prints
  `REMAINING 576 M` at the section head (the pin's start)
  and the counter alone owns the last 576 — the stamp is
  the pin's surveyed length, stated. *Rounding:* nearest
  10m, and monotonic — stamps must strictly decrease down
  the page; the computation enforces it by construction
  (offsets increase), the gate verifies it by reading.
- **Accessibility spec (v2).** The stamp is part of the
  section's heading group (the `h2`'s apparatus line) —
  screen readers receive name + distance as they enter
  each section: the gauge, in text, at reading pace.
  Figures use tabular numerals and a real text unit
  (`M` with the nav's first stamp carrying
  `aria-label="metres"` context via §6.10's label).
- **Tokens consumed (v2).** `--reflection-deep`,
  `--mountain-deep`, `--ease-draw`, `--d0`.

### 6.17 The mirage (page family: empty state / search)

- **What & why.** The theme's honest nothing. Where a
  search finds no plate, or a listing's filter empties the
  plain, the page shows a **mirage**: a faint shimmering
  shape on the horizon — the suggestion of an object that
  is not there — which resolves, as the visitor reaches
  it, into plain words: there is nothing here, and the way
  back to what there is. It belongs because a salt flat's
  classic lie is the mirage, and this theme's ethics (§1)
  demand the lie be confessed on sight: the shimmer is
  labelled as shimmer, and it always resolves to the truth.
- **Structure.** A section in the listing's flow: at its
  horizon, a `.mirage-shape` — a blurred-edged silhouette
  (an SVG blob in `--haze` over `--reflection` at 30%)
  with the displacement filter at amplitude 9, suggesting
  a standing object; beneath it, no reflection (a mirage
  has no water — the tell, for visitors who have learned
  the page's physics). Below the horizon: the empty-state
  text in the Record voice (§12) — what was sought, that
  the plain holds none of it, and the nearest true things
  as real links (the unfiltered listing, the nearest
  stations).
- **Motion spec.** The shimmer is ambient while the
  section is on screen: displacement oscillates 7→11 over
  5000ms `--ease-ripple`, the shape's opacity breathes
  0.5→0.75 — it must look *unreliable*, and the text says
  so. On the section's centre crossing the viewport
  centre, nothing changes: a mirage does not pop when
  approached on a real flat either — it simply never
  arrives, and the words beneath it are the arrival.
  (The theme refuses the cute version where the shape
  dissolves on scroll: dissolution would claim the visitor
  dispelled it. They didn't. It was never there.)
- **States.** Shimmering (on screen) → read (the text is
  the state that matters). If the filter/search is cleared,
  the mirage section is replaced by the real plates with
  §6.12's assembly — the plain refills honestly.
- **Content merge.** The mirage stands exactly where the
  missing content would have stood, in the listing's own
  geography, and its text names the actual query and the
  actual nearest alternatives. It is the empty state *of
  this route*, not a generic "no results" graphic.
- **Failure fallback.** No JS: the text stands with a
  static, undisplaced shape — the words were always the
  content. Filter unsupported: the shape is a flat haze
  silhouette; the confession is unchanged.
- **Reduced-motion variant.** The shape is static at
  opacity 0.6, displacement fixed at 9. A still mirage is
  still a mirage; the text does the work.
- **Performance budget & mobile variant.** One small
  filtered SVG, animated only on screen; ≤0.2ms/frame.
  Mobile: the shape scales to the column; the shimmer's
  oscillation slows to 7000ms (small water, slow lies).
- **Choreography timeline (v2).** Section enters →
  shimmer begins (if motion allowed) → the visitor reads
  the text (no timed beats — the mirage keeps its own
  time) → filter cleared: shape fades 300ms
  `--ease-assemble` as the first real plate assembles in
  its place (§6.12's timeline takes over).
- **State matrix (v2).** *Rest:* shimmering shape + true
  text. *Hover:* links in the text take §11's rule; the
  shape ignores hover (you cannot examine a mirage).
  *Focus:* the text's links are the only focusables.
  *Active:* link navigation. *Scrolled-past:* shimmer
  pauses off-screen. *Disabled:* n/a. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: shape ≤420px wide at the
  section horizon. 768–1199px: ≤360px. <768px: ≤280px;
  the text column is the full measure.
- **Edge cases & failure modes (v2).** *The empty state
  of the whole site* (a search across everything): the
  mirage stands in the search view with the whole route
  as its "nearest true things" — the nav's stations.
  *A filter that empties only sometimes:* the mirage's
  text names the active filter (the sought thing is the
  filter's value, printed, not "your criteria").
  *Never* use the mirage for an error (a failed fetch is
  §6.15's wait line / §6.13's error voice — a mirage means
  "the plain holds none", not "the page broke").
- **Accessibility spec (v2).** The shape is `aria-hidden`.
  The text is a real heading + paragraph in the reading
  order, announced by the search's results count line
  (`role="status"` on the count, updated by the filter —
  the one place a count may change, because it is a
  result, not a gauge). The missing reflection is a
  visual tell only; the text confesses in words.
- **Tokens consumed (v2).** `--haze`, `--reflection`,
  `--mountain-deep`, `--ease-ripple`, `--ease-assemble`.

### 6.18 The unmirrored page (page family: 404 / empty state)

- **What & why.** The 404 is the one page with no
  reflection: a heading standing on a dry flat, no water
  beneath it, no mountain on the horizon, no distance to
  count. The absence is the message — the visitor has
  stepped off the surveyed route into a part of the flat
  the page does not double, because there is nothing there
  to double. It belongs because a theme this committed to
  its physics earns its error page from the same physics:
  the unmirrored page is what "not found" *looks like*
  here.
- **Structure.** A single composition: the heading
  (§12's fixed string: "Nothing is reflected here.") in
  Instrument Serif at headline size, standing on a horizon
  rule; beneath the rule — crust, dry, no mirror field, no
  veil. One line of body: the sought path, printed as
  apparatus (the direction the visitor asked for, in the
  survey's terms). Two links, as ruled text: the departure
  (P=0) and the nearest station (the build's most-visited
  section). The nav (§6.10) is present, but its readout
  prints `REMAINING — M` (a dash, not a number: off the
  route, the gauge honestly has no reading).
- **Motion spec.** None. The unmirrored page does not
  assemble, ripple, glint or haze. Its stillness is total
  and is the point: motion on this page would claim the
  place is alive in the site's world, and it is not.
- **States.** Standing, in all states, at all times. The
  links take §11's hover/focus treatments (furniture still
  works on dry ground).
- **Content merge.** The page's content is the confession
  and the way back — both real. The sought path is printed
  from the actual request (server-rendered), so the page
  names the exact nothing the visitor found.
- **Failure fallback.** This *is* the fallback page; it
  must work with everything else broken — server-rendered,
  no JS required, no async anything.
- **Reduced-motion variant.** Identical. There is no
  motion to reduce.
- **Performance budget & mobile variant.** The cheapest
  page on the site; it should be — it may be served under
  exactly the conditions (errors, spikes) where weight
  hurts. Mobile: identical composition, stacked.
- **Choreography timeline (v2).** None. t=0: the page.
  (Recorded explicitly so the absence is a decision, not
  an omission.)
- **State matrix (v2).** *Rest:* standing, dry. *Hover:*
  link rules ink. *Focus:* §11 ring. *Active:* link
  navigation (plain — §6.15's hold is not performed from
  the unmirrored page; you do not hold a horizon that
  isn't there). *Scrolled-past:* the page is one screen;
  there is no past. *Disabled:* n/a. *Touch:* links
  ≥44px.
- **Breakpoints (v2).** ≥1200px / 768–1199px / <768px:
  the composition scales by §3's clamps only. The horizon
  rule sits at 56% at every size — even off the route,
  the survey's line is where the survey put it.
- **Edge cases & failure modes (v2).** *Soft 404s*
  (empty detail pages, withdrawn plates): they route
  here or to §6.17 — never to a page that mirrors a
  heading over missing content. *The readout dash:* a
  build that prints a number on the 404 has invented a
  distance, failing gate 1. *Search engines:* the page
  returns a real 404 status; the theme's poetry does not
  extend to HTTP.
- **Accessibility spec (v2).** The heading is the page's
  `h1`; the sought path is text, not an image of text;
  the way-back links have plain names ("The departure",
  the station's name). The absent reflection is a visual
  statement only — the words carry the whole meaning.
- **Tokens consumed (v2).** `--salt`, `--crust`,
  `--mountain-deep`, `--crust-deep`.

## 7. Page application map

**Home — the full crossing.** Departure (§6.11), then the
plain's views in route order — each a paired plate (§6.12)
or a statement standing on its horizon, each opening with
its waypoint stamp (§6.16) — the journey section with the
sight line (§6.6) at the route's middle, and the arrival
(§6.13) at the end, with the record (§6.14) on the far
shore. The home page is the theme's complete sentence;
every other page type is a clause of it.

**Listing — a stretch of the plain.** One category's plates
in sequence, each in its own view (§6.12), stamps
recomputed for the listing's own length (a listing is a
shorter crossing: its own D0, declared in its own footer
record — the law scales, it does not bend). Filters live
at the listing's departure as ruled choices (§11); an
emptied listing shows the mirage (§6.17). There is no grid
view. A visitor who wants the grid wants another theme.

**Detail — one object, stood before.** The item at full
size on its horizon, its reflection complete, its facts
beneath the water; the distance apparatus falls away (you
have arrived at *this* thing — the readout is replaced by
the item's own apparatus: its name, its measure, its
price). A single "continue the crossing" link returns the
visitor to the route at the waypoint they left. The detail
page never re-runs the approach; arrival at a part is not
arrival at the destination.

**About — the surveyor's page.** The people and the
method, set as views across a short plain: who walks this
route, how D0 was chosen, what the flag is *not* explained
as (§12: the about page describes the method and still
never explains the flag). This is where §6.14's declaration
lives in long form. Deliberately deep in the site: casual
visitors don't need it; committed ones walk for it.

**Contact / booking — the arrival, directly.** §6.13's
section as its own page for visitors who arrive from
outside (search, a shared link): the mountain stands at
full size from the first screen (they have, in the only
sense that matters, already travelled), the flag stands,
the form follows. Depth is the home page's argument, not a
toll gate on every route — a direct arrival is never forced
to walk the plain to reach the form.

**The unmirrored page (404).** §6.18, everywhere,
unchanged.

## 8. Worked examples

### 8.1 The hero — the departure

*The commission: "Casa Salina", a four-room lodge at the
foot of a white ridge, 4,800 metres from the highway's end
across a salt flat. The page's destination is a booking
enquiry. D0 = 4,800 — the real approach distance, printed
in §6.14's declaration.*

- **The composition (§6.11).** First screen: salt and sky.
  The nav (§6.10) borderless: wordmark "Casa Salina",
  stations THE ROOMS / THE TABLE / THE ROUTE / ARRIVE, and
  the readout `REMAINING 4,800 M`. At the master horizon, a
  67px smudge of mountain with its reflection assembling
  beneath it (§6.1). Upper left, the headline: "Four rooms
  at the end of the white." — and its rippling mirror below
  the line. On the crust band, the word being written,
  letter by letter: **SALINA** — the lodge's name, the
  destination word. Bottom left, the departure statement:
  "The road ends at the highway. The rest is flat, and then
  us." Bottom right, the cue: "Walk — The Rooms".
- **The ceremony.** Fonts at t≈110ms: the mountain fades
  in; at t=500 its reflection starts settling out of
  disturbance as the headline rises; at t=900 the S lands
  on the crust and its little reflection ripples once;
  A-L-I-N-A follow at 90ms intervals. By t=2400 the screen
  is still: a speck, a doubled headline, a written name, a
  true number. A visitor who never scrolls has received
  the whole proposition.
- **Scroll timeline.** 0–40px: nothing moves but the
  readout's first metres and the cue's rule stopping its
  cycle. 40–400px: the hero's local reflection hands its
  weather to the ride (§6.2); the speck is 0.13 now. The
  visitor is walking.

### 8.2 Mid-page — the third view

*The same page, at the route's middle: "The Table" — the
lodge's dining room, a paired plate (§6.12), opening with
its waypoint stamp (§6.16), with the journey section's
sight line (§6.6) in the following view.*

- **Entry.** The stamp's rule draws: `THE TABLE —
  REMAINING 2,880 M` — the section's measured position,
  computed from its offset (60% of the approach behind the
  visitor, 2,880 of 4,800 remaining). The plate's base
  crosses 75%: the dining-room photograph settles 12px
  into place while its reflection assembles out of ripple
  beneath the horizon rule — the room, doubled in water
  that isn't there, on a flat that is all salt. Caption:
  "The long table. Dinner is at eight, because the light
  is."
- **The examination.** The visitor slows; the page's
  weather calms (§6.3's tail). They hover the plate: its
  water stills completely over 400ms while the mountain's
  reflection, further up the screen, keeps its shimmer —
  one water calmed by attention, the rest by rest. In the
  next view, the sight line draws from `YOU — 2,400 M` to
  the ridge's summit across the route elevation (§6.6).
  The mountain, by now, is 0.24 scale and has quietly
  become a presence.
- **What the visitor feels.** Distance accumulating as
  knowledge: they know how far they have come (the stamps),
  how far remains (the counter), and what the far end
  looks like (growing). Nothing has asked for anything.
  The page is saving its one ask for the one place it
  belongs.

### 8.3 Conversion — the arrival

*The same page's end: the pin, the flag, the form.*

- **Arrival.** The arrival section's top reaches the
  viewport top; the pin engages. q 0–0.25: the ride's
  mountain crossfades into the in-flow mountain standing
  over the arrival composition — same size, same place,
  custody changed. The counter runs the last metres:
  576… 402… 301… At q=0.55 the flag appears at the
  mountain's foot — small, orange, the page's first warm
  pixel — stands for a beat, then flutters once. The
  heading settles: "Arrive." The CTA stands beneath it,
  and as the visitor's pointer crosses the field toward
  it, it leans — 2px, 4px, 6px — to meet them (§6.8).
- **The asking.** The pin releases into the form (§6.13):
  name, direction (email), dates as ruled lines, one
  consent seam-line. The visitor mistypes the email; on
  blur the rule inks reflection-deep and the note stands
  beneath in the Record voice: "This direction will not
  carry — check it before you send." They fix it; they
  press SEND ACROSS. The block presses; the system
  answers; the form becomes the record: "SENT — REFERENCE
  CS-2026-0471. Your words are kept at the lodge." Above
  it, the counter reads `REMAINING 0 M`, and does not
  celebrate.
- **Failure rehearsed.** If the post fails, nothing they
  wrote is cleared; the note above the form reads "NOT
  SENT — THE FLAT KEPT YOUR WORDS. TRY AGAIN, OR WRITE TO
  THE LODGE DIRECTLY." and the direct address stands
  beside it. A visitor who walked 4,800 metres is never
  sent back to the departure by a network blink (§10,
  blocking gate 7).

## 9. Anti-slop — what makes THIS theme look cheap

1. **The postcard.** A photographic sky gradient, stock
   clouds, a lens-flare sun — landscape wallpaper behind web
   content. *Cure:* the palette is flat colour and drawn
   line; the sky is salt's negative space, not a picture.
   The only images are the content's plates (§6.12).
2. **Blue water.** Reflections tinted swimming-pool blue,
   or given wave textures and sparkle overlays. *Cure:*
   the mirror is the sky's pale `--reflection` under the
   `--fade-depth` veil, displaced, never textured. Water
   here is a behaviour (it ripples, §6.3), not a fill.
3. **Warm creep.** An orange hover here, a terracotta badge
   there, "just" the submit button in the flag's hex.
   *Cure:* §2's warm audit — a grep, run at the gate
   (§10 gate 2). One warm thing, one instance.
4. **Explaining the flag.** A caption, a tooltip, a line of
   copy about what the flag means. *Cure:* §12's fixed
   rule — the copy never explains it, anywhere, including
   the about page. Meaning that must be explained was
   decoration.
5. **The progress bar.** A thin bar, a percentage, a
   "you're 60% there!" — dashboard furniture over the flat.
   *Cure:* §1's law. The mountain is the gauge; the counter
   is its voice; there is no third printing of progress as
   *decoration* (the stamps, §6.16, are signage, printed
   still).
6. **The fast mountain.** Scale mapped linearly to scroll,
   so the mountain visibly zooms and the spell becomes a
   dolly shot. *Cure:* the perspective law (§6.2:
   s = 0.12 × D0/d) and the 0.06 lerp. If a reviewer can
   *see* it grow within one screen, it is growing too fast.
7. **Reflected paragraphs.** Body copy mirrored "for the
   aesthetic". *Cure:* type law 1 (§3) — sentences don't
   reflect; the water takes shapes. A mirrored paragraph is
   unreadable text printed twice.
8. **Parallax party.** Clouds drifting, layers sliding at
   five rates, the headline floating against the scroll.
   *Cure:* §5 — the only counter-scroll motion is the
   mirrored parallax of objects and their water (§6.12).
   The flat is still; things on it are still; only the
   walk moves.
9. **A CTA on every view.** "Book now" buttons sprinkled
   down the plain "for conversion". *Cure:* §4's density
   and §6.10's rule — the ask lives at the destination.
   A build that surfaces the CTA early has falsified its
   own geography: if you can book from anywhere, the
   distance was a lie.
10. **The mountain as logo.** The destination's silhouette
    reused as a brand mark in the nav, the favicon, the
    footer. *Cure:* the mountain is a *place*, present in
    the geography (§6.2/§6.11/§6.13); the wordmark is the
    name in type. A place used as a logo stops being a
    place.
11. **Ripples that never calm.** Ambient wave loops on
    every reflection, forever, regardless of the visitor.
    *Cure:* §6.3 — amplitude is velocity's function and
    decays to stillness in 900ms. Water at rest is this
    theme's resting face; permanent chop is a screensaver.
12. **The arrival that doesn't stop.** The pin skipped, the
    mountain sailing past full size, the flag a favicon-
    sized afterthought — the journey ends in a whimper of
    ordinary sections. *Cure:* §6.13's pin and custody
    handoff, §6.7's reveal beat. The end of the walk is
    the theme's whole argument; it is staged or the theme
    isn't built.

## 10. Quality gate

**Blocking (any failure stops the build):**

1. **Gauge-law audit.** D0 and the approach function are
   declared and printed on the page (§6.14); the mountain's
   scale, the counter and every waypoint stamp are the same
   function — verified by reading all three at three scroll
   positions and checking s = 0.12 × D0/d against the
   printed counter value. A second progress indicator
   (bar, percentage, scroll-%) anywhere fails on sight.
2. **Warm audit.** `grep` for `--flag` and its hex: exactly
   one component (§6.7), one instance, no text carried, no
   hover/focus/error usage. Any second warm element —
   including an unmodified browser-default orange focus
   outline left unstyled — fails.
3. **Three-printings agreement.** The counter (§6.5), the
   stamps (§6.16) and the footer declaration + table
   (§6.14) state the same D0 and consistent distances —
   stamps strictly decreasing, arrival stamp 576, counter
   reaching exactly 0. The footer is generated from the
   loop's constants (§6.14), verified by the constant-
   change test.
4. **No stranded content.** With JS disabled, the whole
   page reads: departure standing, word written, plates
   with reflections assembled, stamps printed, arrival
   complete with flag and working form. With JS on and the
   loop killed, every watchdog (§6.1's 2400ms, §6.4's
   3000ms, §6.12's 1000ms) fires and completes its element.
5. **The approach reads.** Total pre-pin approach length ≥
   3 viewport heights (§6.2), and a reviewer scrolling at
   reading pace cannot see the mountain grow within a
   single screen — checked by screen recording at P≈0.3,
   the law's most fragile zone.
6. **The arrival is real.** The pinned section contains
   the site's actual conversion (form or resolving CTA,
   §6.13) — not a decorative finale. The form works with
   the pin disabled and with JS disabled.
7. **Form-keeping.** A failed submit (simulated network
   error) leaves every field exactly as written, with
   §12's failure note. Any build that clears the form on
   error fails.
8. **Corridor law.** At every scroll position and
   breakpoint, no text or interactive element occupies the
   horizon band (§4: ±90px desktop, ±60px mobile) except
   the mountain, its reflection and the hairline — checked
   by overlaying the band in a test build at ten scroll
   positions.

**Standard (must pass, fixable in review):**

9. Density: one object per view on the plain (§4); the
   arrival is the only dense composition.
10. Exactly one pin (the arrival); §5's refusal list
    honoured — no marquee, no blur reveals, no kinetic type
    beyond §6.4, no magnetism beyond §6.8.
11. Ambient ration: haze + glints only (§5), glints ≤12
    page-wide, both paused off-screen; ripples calm within
    900ms of rest at every reflection.
12. The ceremonies (§6.1/§6.4) run once per session and
    never re-run; the counter is the only moving number
    (type law 2) — audited by watching a full crossing.
13. Every interactive element ≥44px; focus shows §11's
    ring (never the flag's colour); focus never lands on a
    reflection (all `aria-hidden`, all unfocusable).
14. Mobile: the pin shortens (§6.13), the counter stays
    visible (§6.5), plates keep one-per-view (§6.12), the
    lean is absent (§6.8).

## 11. Component inventory

Every component a real Salt Mirror site needs, with its
themed treatment. Components the theme refuses are listed
with their in-world replacement — a refusal without a
replacement is a gap, not a stance.

| Component | Themed treatment |
|---|---|
| Primary button | The destination block (§6.8): mountain ground, salt label, apparatus caps; exists at the arrival and in the form (submit) — nowhere else on the page. |
| Secondary button | Ruled text button: transparent, 2px bottom rule in mountain; hover inks the rule reflection-deep. Stands still — only the primary leans. |
| Text input | Ruled line (§6.13): apparatus label above, 2px rule below in crust-deep, inking mountain on focus; no box — the field is a line on the flat, filled like a guest book. |
| Textarea | Ruled sheet: lines every 33px (the body line unit), Inter 17px. |
| Select | Refused. Choices are stations: a short list of ruled radio lines, the chosen one's rule in mountain (§6.13's consent grammar generalised). A dropdown is a cupboard; the flat has no cupboards. |
| Checkbox | Seam box: unfilled square in mountain-deep; filled = mountain fill + salt tick. |
| Radio | Station line: the chosen line's rule inks mountain; the marker is a small filled circle in reflection-deep. |
| Toggle / switch | Refused. The flat has states of distance, not switches; use two station lines as radios. |
| Card | Paired plate (§6.12): the object on its horizon with its reflection. There are no other cards. |
| Table | The waypoint table (§6.14): real table, apparatus headers, no zebra striping — a ruled line under the header and under the arrival row only. |
| Tabs | Refused. Distance is not tabbed; stations are walked or anchored (§6.10). |
| Accordion | View expander: a station whose facts unfold downward like ground being crossed — the following content pushes down over 400ms `--ease-glide`; the heading gains its waypoint rule. |
| Modal / dialog | Refused. The theme has no overlays: a confirmation is the record (§6.13's success state, in-flow). Anything that must interrupt does not belong on a plain. |
| Toast | Refused. News is recorded, not toasted: confirmations appear as a one-line record at the section's foot, in the Record voice, and remain. |
| Tooltip | Refused. Explanation lives in captions and context lines; a plate that needs a tooltip needs a better caption. |
| Badge | Distance chip: apparatus text on crust — "2,880 M OUT" — the badge states where a thing lies on the route, never a marketing claim ("NEW" is banned, §12). |
| Alert | Mirage band (§6.17's grammar, minus the shimmer): a ruled band in the current view, message in §12's error voice, persistent until resolved. Never `--flag`. |
| Pagination | Waypoint pagination: "Further" / "Back" links lettered with the next station's name and its remaining distance — never numbered pages; a route is continuous. |
| Progress bar | Refused. Progress is the mountain (§6.2). |
| Spinner | Refused. Waiting is crust (§6.15). |
| Skeleton | §6.15's crust region with its horizon rule. |
| Search | The survey search: one ruled line at the listing's departure; results are plates on the plain (§6.12), and no results is the mirage (§6.17) — search results here are views, not a list. |
| Breadcrumbs | Replaced by the waypoint stamps (§6.16) plus the counter: the visitor's position is a distance, not a trail of pages. |
| Skip link | "Skip to the arrival" / "Skip to content" as a plain mountain-deep link appearing on first focus at the departure. |
| Focus ring | 2px mountain-deep outline, offset 3px, on every interactive element. Never `--flag` — the warm audit (§10 gate 2) includes focus styles. |
| Divider | The horizon hairline (1px crust-deep) or, within a view, a 2px rule in the ground's text colour at 30%. Wavy SVG dividers are refused — the water is in the reflections, not in the furniture. |

## 12. Content & copywriting voice

Two voices, cast like the type. **The Instrument** writes
apparatus: distances, station names, labels, the counter —
Inter 500, uppercase, terse, every figure from the declared
function. **The Record** writes prose: statements, captions,
errors, confirmations — Inter 300, sentence case, plain and
unhurried, the voice of someone who has walked the route and
is describing it for whoever comes next. The voices never
swap: apparatus never sentences, the record never shouts.

**Headline style.** Statements of place and distance. ✓
"Four rooms at the end of the white." / "One table, set at
eight, because the light is." ✗ "Discover your dream desert
getaway!!" (exclamation, salesmanship, a headline shouting
across a silent flat). Exclamation marks are banned from the
whole theme — distance does not shout.

**Label style.** Apparatus: noun + measurement. ✓
"REMAINING 2,880 M", "THE TABLE — THIRD VIEW". ✗ "Section
3", "You're 60% there!" (the counter counts metres;
percentages are a bar's language, §1).

**Error voice.** A surveying fact, stated plainly, with the
way back. ✓ "This direction will not carry — check it before
you send." ✓ "NOT SENT — THE FLAT KEPT YOUR WORDS. TRY
AGAIN, OR WRITE TO THE LODGE DIRECTLY." ✗ "Oops! Something
went wrong 😞" (the flat has no "oops", and no emoji
survives the crossing).

**Empty-state voice.** ✓ "The plain holds none of these.
The nearest true things:" — followed by real links (§6.17).
✗ "No results found. Try being less specific?" — the record
does not blame the walker.

**Confirmation voice.** ✓ "SENT — REFERENCE CS-2026-0471.
Your words are kept at the lodge." ✗ "Success! 🎉 You're
all set!" — a confirmation is a record entry, not a
celebration; the counter reaching 0 is the celebration, and
it is silent.

**The flag rule (fixed, absolute).** No copy — headline,
caption, alt text, about page, error, confirmation — ever
mentions, names, hints at or explains the flag. It is not
called "our flag", it is not a symbol "of" anything in
words. The moment copy explains it, it becomes a logo with
a caption, and §9 item 4 has happened.

**Banned words:** amazing, stunning, breathtaking (the flat
is breathed *on*, it does not take breath), journey of a
lifetime, unlock, seamless, oasis (unless the site is
literally one, with water), NEW (as a badge), oops.
**Owned words:** flat, horizon, remaining, the far, still,
white, station, view, arrive, kept, the end of the —.

**Fixed strings (verbatim, do not paraphrase):** the
counter's label — "REMAINING"; the 404 heading — "Nothing
is reflected here."; the scroll cue's verb — "Walk"; the
form failure pattern — "NOT SENT — THE FLAT KEPT YOUR
WORDS." (the build's own second clause may follow it).

## 13. Full-page scroll choreography map

The home crossing, top to bottom. Every beat in order; the
instruments run continuously beneath the beats (counter
§6.5 counting, mountain §6.2 growing, ripples §6.3 answering
the walk, haze at the horizon).

| Beat | Scroll zone | What happens | What the visitor feels |
|---|---|---|---|
| 1 | Load | Assembly (§6.1), headline rises, word writes (§6.4) | A place, far and doubled |
| 2 | 0–40px | Cue cycle stops; nav gains its rule (§6.10) | The walk has begun |
| 3 | First view enters | Stamp rule draws (§6.16); plate assembles (§6.12) | The first thing on the plain |
| 4 | Views 2–3 | Plates at their views; stamps fall: 3,840 → 2,880 M | Distance becoming knowledge |
| 5 | Route's middle | Sight line draws (§6.6): you → the summit | The route, surveyed |
| 6 | Views 4–5 | Mountain passes 0.3, then 0.45; water calms at each rest | A presence, growing |
| 7 | Last view | The final stamp: `REMAINING 960 M` | Nearness, stated |
| 8 | Arrival pin engages | Custody crossfade (§6.13); counter runs 576 → | Arrival, in metres |
| 9 | Pin q=0.55 | The flag reveals; a beat; one flutter (§6.7) | The one warm thing |
| 10 | Pin q→1 | Counter at 0 M; CTA leans to the pointer (§6.8) | The goal, reaching back |
| 11 | Pin releases | The form (§6.13), in the mountain's ground | The ask, at the end of the walk |
| 12 | Footer enters | The record's rule draws (§6.14): D0, declared | The workings, shown |

**Reverse pass.** Scrolling up: the mountain shrinks by the
same law, the counter counts up, plates stay assembled, the
sight line stays drawn, the flag — once seen — stays
standing (§6.7). The ceremonies never re-run. Retreat is
measured as honestly as approach; nothing on the page
pretends the visitor hasn't been where they've been.

**Jump-scroll catch-up.** Anchor jumps and flings:
everything passed stands assembled, stamps stand marked,
the mountain glides to its P-true scale at the lerp's pace
(~1.2s from a full jump — a glide, not a teleport, §6.2),
and the counter settles on the true figure. The flag does
not flutter for a teleport (§6.7); it is simply there.

## 14. Whole-page performance budget

| Budget | Limit |
|---|---|
| Total page weight (home) | ≤ 640KB, of which plate images ≤ 420KB |
| Fonts | Instrument Serif (1 weight) + Inter (2 weights) ≤ 90KB, `font-display: swap` |
| JS | ≤ 55KB gzipped (one loop, observers, pin, form) |
| Shared-loop cost | ≤ 1.4ms/frame average; writes only transform / opacity / custom properties |
| Long tasks | None > 50ms after load; the departure ceremonies are timer-sliced (§6.1/§6.4) |
| Reflection filters | ≤ 2 SVG filter instances page-wide (§6.3); ≤ 8 live reflections on screen |
| Arrival latency | Any plate's reflection assembled ≤ 1000ms after entering (watchdog law) |

**Cut order when the budget is exceeded** (cut in this
order, record each cut in the build notes):

1. Salt glints (§6.11) — gone entirely.
2. Heat haze (§5) — the horizon rests.
3. Plate parallax separation (§6.12) — plates stand still;
   their reflections keep the weather.
4. The horizon-hold transition (§6.15) — navigation becomes
   plain.
5. The sight line's draw (§6.6) — the line ships drawn for
   all visitors (its reduced-motion treatment).
6. Mirror-break's local ripple bump (§6.9) — the ring
   remains; the water bump goes.

**Never cut:** the approach loop and its law, the counter,
the waypoint stamps, the footer declaration, the form's
error-keeping, any watchdog, any reduced-motion variant.
A build that cuts the honesty to keep the ambience has
inverted the theme.

## 15. Build-order checklist

1. Declare the destination first: name the one thing at the
   end, its real conversion (§6.13), and D0 with its
   referent. Write the approach config object; everything
   else is generated from it.
2. Build the static flat: all views, all content, plates
   with reflections assembled, stamps printed, arrival
   complete, form working — with no JS. This is the site;
   the rest is the crossing.
3. Set the palette tokens and pairing law (§2); run the
   warm audit on the static build (it should already pass:
   one flag, in the arrival's figure).
4. Set the type scale and type laws (§3); verify only
   shapes reflect — grep the DOM for mirrored duplicates
   and confirm each is display type or an image.
5. Fix the master horizon (56vh) and the corridor (§4);
   build the ride (§6.2) behind the corridor and verify
   the corridor empty at ten scroll positions.
6. Add the shared loop; wire P, the scale law, the counter
   (§6.5) and the hairline from the one config object.
7. Generate the stamps (§6.16) from measured offsets and
   the footer (§6.14) from the config; verify the
   three-printings agreement by reading all three at three
   scroll positions.
8. Add the departure ceremonies (§6.1, §6.4) with their
   watchdogs and session rules; test with the loop killed.
9. Add velocity ripples (§6.3) with the calm tail; tune the
   amplitude cap against a fast fling and a slow read.
10. Add the plates' entry assembly and mirrored parallax
    (§6.12); verify reflections rejoin at rest offsets.
11. Build the arrival: native-sticky pin, custody handoff,
    flag reveal (§6.7), CTA lean (§6.8), mirror field
    (§6.9), form (§6.13) with error-keeping rehearsed
    against a simulated network failure.
12. Add the sight line (§6.6), the mirage (§6.17), the
    crust skeleton and horizon hold (§6.15), the
    unmirrored page (§6.18).
13. Add the ambient ration last — haze, then glints — only
    if the budget (§14) survives them.
14. Verify breakpoint behaviour per element (≥1200 /
    768–1199 / <768) and the reduced-motion flat end to
    end: mountain as two stills, counter stepping, water
    still.
15. Run §10 in full: gauge-law audit, warm audit,
    three-printings agreement, no-JS read, loop-killed
    read, corridor overlay test, approach-length check.
    Gate signed by someone who did not build the page.
