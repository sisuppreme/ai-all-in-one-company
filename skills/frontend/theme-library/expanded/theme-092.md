# 92. Museum After Dark — Expanded (v1 + v2)

**Identity (preserved from the original entry, deepened — never
redesigned).** The museum at 2 a.m.: a nearly black site explored
on a night guard's round. Artworks exist in darkness until the
roaming torch beam finds them; wall labels illuminate a beat
after the art, because the guard reads second. Palette anchors:
gallery night `#07090C` · shadow wall `#1C2126` · torch-lit ivory
`#F2EAD8` · brass plaque gold `#B08D4F` · guard's green `#4A5D57`.
Type: Marcellus (display — quiet Roman capitals) + Source Serif 4
(body). Rooms I–VII, a fixed darkness overlay with a radial light
pool, brass accession numbers on every object, flippable wall
labels whose backs are the guard's notes, and a 4-second watchdog
that raises the house lights if the beam system ever fails.
Reference implementation: demos/museum-after-dark.html.

## 1. Concept & world

Museum After Dark is a museum website after closing. Every museum
has two lives sharing one building: the day life — white walls,
school groups, labels read in flat even light — and the night
life, which almost nobody is allowed to see: the same rooms gone
nearly black, the air still, a guard walking his round with a
torch, checking locks, pausing at the objects he has privately
adopted over years of nights. The day museum explains itself.
The night museum is *found*, object by object, in the order a
man walks. This theme builds the site out of the second life.
The visitor is not browsing a collection database; they are
shadowing the round — Rooms I to VII in the guard's order — and
nothing on the page is revealed by a webpage's usual machinery
of fades and slides. Things are *lit*. The torch pool travels
(§6.1), the art is found first and its label a half-beat later
(§6.4), the portraits notice the light (§6.3), the dust exists
only where the light is (§6.2), and even the statistics must
wait to be found before they may count (§6.11).

The fiction is disciplined, and the discipline is the design.
The beam is never a cursor and never follows the pointer — the
original entry is explicit, and this expansion holds it as law:
the light belongs to the guard, and the guard walks by scroll,
room to room, at the pace of a man who has done this ten
thousand times. The visitor's power is the walk itself, plus
two honest interactions: turning a wall label over to read what
the guard wrote on its back (§6.10), and booking a place on the
one night a month the museum lets the public walk the round
themselves (§6.16). Everything else — the swinging lanterns
(§6.6), the flickering corridor spots (§6.9), the frieze the
light walks along (§6.7) — is the building behaving the way the
building behaves at night, whether or not anyone is watching.

**The theme's one law: darkness is an overlay, never a hiding
place.** Two clauses, both audited by the gate. (1) *Nothing is
ever hidden — only unlit.* Every artwork, label, paragraph and
price ships fully rendered in the DOM at full semantic weight;
the night is a fixed overlay and a radial light pool composited
above finished content. Delete the overlay and the beam script
entirely and the page must read, complete and in order, as a
quiet dark-themed museum site. A build in which any content's
visibility depends on the beam arriving has broken the law and
fails the gate outright. (2) *The house lights always exist.*
A 4000ms watchdog (§6.1) watches the beam system confirm itself;
if it does not — script error, rAF starvation, a backgrounded
tab — the overlays are killed and replaced by a static vignette
with the ambient floor raised: the museum under house lights,
less romantic, fully legible. A real guard's first duty on a
failed round is to put the lights on. So is the page's.

**The readability covenant.** This theme was praised in demo and
corrected in the same breath: darkness must never make things
unreadable. The covenant is therefore written into the tokens,
not left to taste. Ambient light outside the beam is lifted so
that all body text holds at least 4.5:1 against its local
background *without* the beam's help (measured values in §2);
the beam adds drama, warmth and focus — never basic legibility.
Any element whose contrast depends on the beam to pass is a
defect, and §10 tests for it with the beam parked in another
room.

**Best-fit sites and audiences.** Museums and galleries running
a night opening, a late programme or an exhibition microsite;
heritage houses and historic sites whose after-hours tours are
their premium product; exhibition landing pages for a single
dark-room show (photography, old masters, relics, astronomy);
archives and libraries mounting a "by night" treasures
exhibition. The audience it suits is the deliberate visitor:
members, donors, romantics, photographers, the people who book
the 9 p.m. slot on purpose. Conversion in this world is
membership, night-tour booking, exhibition tickets and
patronage — purchases made slowly, by people savouring the
approach, and the page is built to be savoured at exactly that
pace.

**When NOT to use it.** Not for a general collection database or
a research portal: scholars need 4,000 records in flat light
with filters, and a torch round over a catalogue is a prank,
not a tool — §7 routes search results to a lit index surface
(§6.17) and even that keeps the round's pace. Not for
children's museum programming aimed at under-tens: the register
is 2 a.m. stillness and one dry joke about a statue, and it
will read as gloom to a seven-year-old. Not for bright,
high-volume retail (a museum *shop* bestseller grid wants day
light and speed). Not for any team that cannot maintain the
accession discipline: every object on the page carries a real
brass accession number tied to the collection record (§6.15),
and a page whose numbers are decorative lies in the theme's
own language. And never as a dark-mode skin over an unrelated
site: the darkness here is a place with a keeper, a route and
a closing time, not a colour preference.

## 2. Palette

Five anchors, inherited exactly. Derived tokens form a closed
list: a token not in this table does not exist in the theme,
and the gate greps built CSS for undeclared hex values. The
world is a black gallery lit by one warm torch: ivory carries
the reading, brass carries the institution, green carries the
guard — and the night itself is a *material* with a measured
floor, not an absence.

| Token | Hex | Role | Ratio / use |
|---|---|---|---|
| `--night` | `#07090C` | Gallery night — page ground, the dark between rooms | ~55% of pixels |
| `--wall` | `#1C2126` | Shadow wall — panels, label stock, unlit surfaces | ~25% |
| `--ivory` | `#F2EAD8` | Torch-lit ivory — all body text, lit artwork grounds | text primary |
| `--brass` | `#B08D4F` | Plaque gold — accession numbers, room plaques, rules, counters | signals & metal only |
| `--guard` | `#4A5D57` | Guard's green — the keeper's traces: label backs, notes, route line | accents ~3% |
| `--ivory-dim` | `#CFC5AC` | Ivory at rest outside the beam — body text's unlit state | derived, text |
| `--ivory-faint` | `#9A917C` | Captions and credits at ambient level | large/caption only |
| `--wall-lift` | `#262D34` | Wall under ambient lift — card grounds, form fields | surfaces |
| `--brass-lit` | `#D9BC7E` | Brass inside the beam — glints, struck counters | transient only |
| `--beam-warm` | `#FFE9BE` | The torch pool's heart — a gradient stop, never a flat fill | overlay only |
| `--green-lit` | `#7E978E` | Guard's green inside the beam — note ink brightened | transient only |
| `--alarm` | `#B4552D` | Oxide red — errors and the one alarm notice; the building's only red | <0.5%, errors only |

**Measured contrast (computed from the hex values, this
expansion).** Ivory on night: 14.6:1 — display and body pass
everywhere. Ivory-dim on wall: 8.9:1 — body text outside the
beam passes AA and AAA for normal text; this pair is the
readability covenant's working proof. Ivory-faint on wall:
4.6:1 — passes AA for normal text, restricted to captions and
credits of 13px and up, never for essential instructions.
Brass on night: 5.4:1 — passes for the 12px+ accession numerals
and plaque text it serves; brass on wall: 4.1:1, so plaques sit
on night or carry a 1px night keyline. Guard green on night:
2.6:1 — *never text on night*; the guard's notes are set in
`--green-lit` on wall (4.9:1) or ivory on green. Beam-warm is a
gradient heart inside an overlay, not a surface: no text is
ever set on it. Alarm on night: 3.9:1 — used only for error
glyphs and rules paired with ivory error text (14.6:1), never
as the sole carrier of an error.

**Pairing rules.** Text is ivory or ivory-dim, on night or
wall, full stop — there is no third text colour. Brass is
metal: numbers, plaques, hairlines, the torch-line; it is
never a paragraph and never a link colour (links are ivory,
underlined by a brass rule that thickens on hover). Green
belongs to the guard alone: label backs, his notes, the
footer route, the "round completed" states — if green appears
anywhere the guard has not been, it is wrong. Alarm appears
only where something has genuinely failed.

**The beam's colour discipline.** The pool is the only
warm light in the building and its warmth is a gradient,
never a fill: `--beam-warm` exists at 34% in the heart,
falls through 12% in the halo, and reaches 0% at the
pool's edge — a build that tints a whole room warm has
installed ceiling lights and called them a torch. Warmth
also never crosses into the text: ivory inside the beam
stays `--ivory` (the light reveals the page's own colour;
it does not dye it), and the single exception is brass,
which is *allowed* to answer light — `--brass-lit` exists
because metal glints, and paper does not. That asymmetry
is the palette's physics: in this building, light changes
only what light would change in the real one — metal,
glass (§6.6's lanterns), and the gilt of frames (§6.3) —
while print, stone and wall hold their colours and simply
become easier to see. A build that warms its body text
under the beam has broken the physics and, with it, the
covenant's contrast measurements, which are taken on the
text's true colours.

**Dark-mode behaviour.** The theme *is* the dark; there is no
light inversion and `prefers-color-scheme: light` does not
brighten the museum — a visitor who needs light gets the
**house-lights variant** instead: an explicit toggle (and the
watchdog's fallback state, §6.1) that raises `--night` to
`#14181D`, `--wall` to `#2A3138`, lifts ambient so the beam's
contribution becomes a gentle warm emphasis, and holds every
other token. It is presented in the guard's language — "House
lights" — never as a generic theme switch. Forced-colors mode:
the darkness overlay and beam are removed entirely, artworks
get 1px borders, plaques become bordered chips, and the round
is conveyed by the room plaques alone.

## 3. Typography

Two families, inherited exactly, and the division of labour is
the institution's: **Marcellus** speaks for the museum —
display, room names, exhibition titles — in its quiet Roman
capitals, one weight, never bolded, never italicised, because
stone inscriptions do not shout. **Source Serif 4** does
everything else: body, labels, the guard's notes, data. There
is no sans anywhere on the page; the night museum has no
signage voice, only inscription and print. Numerals in
accession numbers and counters are Source Serif 4 tabular
lining figures — a `1962.014` must not wobble as it counts.

| Role | Font | Size / line-height | Tracking | Notes |
|---|---|---|---|---|
| Display (exhibition title) | Marcellus | clamp(44px, 7vw, 76px) / 1.04 | +0.01em | §6.5 catches light letter by letter |
| Room name | Marcellus | clamp(30px, 4vw, 44px) / 1.1 | +0.02em | Always paired with its brass plaque numeral |
| Section head | Marcellus | 24–28px / 1.2 | +0.015em | Never centred; rooms are entered from the left |
| Body | Source Serif 4 | 17px / 1.62 (≥1200), 16px / 1.6 (<768) | 0 | Max measure 62ch; the night is read slowly |
| Wall label | Source Serif 4 | 15px / 1.55 | 0 | Object name in small-caps ivory, then maker, date, medium |
| Guard's note (label back) | Source Serif 4 italic | 14px / 1.5 | 0 | Green-lit on wall; italics are his handwriting, used nowhere else |
| Accession number | Source Serif 4 tabular | 11.5px / 1.4 | +0.08em | Brass, always prefixed by the room: `III · 1962.014` |
| Counter figure | Source Serif 4 tabular | 30px / 1.1 | +0.02em | Brass; counts only when lit (§6.11) |
| Caption / credit | Source Serif 4 | 13px / 1.5 | 0 | Ivory-faint; the only role allowed at 4.6:1 |

**Type laws.** (1) *Marcellus never sets a sentence.* It names
things — exhibitions, rooms, objects of honour — and stops;
the moment a paragraph appears in capitals the museum is
shouting in its own gallery. (2) *Italics belong to the guard.*
Source Serif italic appears only in his notes and quoted
speech; emphasis in body copy is weight or position, never
italic, so the visitor learns to feel a small jolt — *the
keeper was here* — whenever italics appear. (3) *Numbers are
evidence.* Every figure on the page — counters, prices, dates,
the frieze's length — is set tabular and traces to the
collection record (§6.15); a number that cannot be traced is
cut, not styled. (4) *Labels are read second.* Label type is
deliberately a step quieter than the art it serves: 15px
against the object's full-bleed presence, so the eye goes to
the work first and the words second, matching the beam's own
sequence (§6.4). (5) *No text under 11.5px, ever* — the night
is dark enough without small print; credits that cannot fit at
13px are moved to the colophon (§11), not shrunk.

**The accession format.** One format, everywhere, no
variants: `ROOM · YEAR.SEQUENCE` — the room's Roman
numeral, the year the object entered the collection, and
its sequence within that year, zero-padded to three:
`IV · 1908.007`. The format is data, not decoration: the
room prefix means a number can be checked against the
room the visitor is standing in, and §6.11's audit counts
by prefix. An object moved between rooms keeps its number
(the number is its birth certificate, not its address)
and its label gains one line — "Hung in Room II until
2019" — because in a museum, provenance includes walls.
A build that renumbers an object to match its room has
falsified the record for tidiness, which is the one sin
this theme's whole apparatus exists to prevent.

## 4. Layout language

The page is a **round**: a fixed sequence of seven rooms,
walked in order, each room a full section whose doorway is a
cross-dissolve (§6.14) and whose name is a brass plaque
(§6.13). The guard does not teleport and neither does the
layout: there are no grids of equal cards anywhere except the
object store (§6.15), because a museum's rooms are not a
spreadsheet. Each room holds one principal object at large
scale, its label at reading distance, and air — the night
itself is the whitespace, and it is spent generously: rooms
breathe at 18–26vh of night between principal objects at
≥1200px.

**Grid and measures.** A 12-column grid at ≥1200px with a
reading column of columns 3–9 (max 62ch) for text and full-bleed
columns 1–12 reserved for the frieze (§6.7) and the masterpiece
(§6.8). Artworks hang on the wall's own rhythm: principal
objects sit on a baseline 96px below their room plaque, labels
hang 24px to the right of the object's frame edge at desktop —
the museum convention, object left, label right, never below
centred like a caption on a blog. At 768–1199px the label moves
beneath the object at 16px, right-aligned to the frame edge.
Below 768px the round is a single column, labels full-width
beneath objects, and the beam's radius shrinks (§6.1) rather
than the type.

**The darkness overlay.** One fixed layer above content,
below the plaques and the torch-line: a radial gradient pool
(`--beam-warm` heart → transparent at ~430px) composited over
a night wash at 88% opacity. The wash is what "unlit" means;
the covenant of §2 guarantees everything beneath it is legible
before the pool arrives. The overlay is `pointer-events:none`
in every state, carries no text, and is `aria-hidden`. A thin
**torch-line** — 2px, brass at 30% — runs along the very top of
the viewport, filling with `--brass-lit` in proportion to the
round completed; it is the page's only progress indicator and
it belongs to the building, not the browser.

**Density rules.** One principal object per viewport height,
minimum. Two objects may share a view only in the object store
(§6.15) and the frieze (§6.7), where multiplicity is the point.
Room plaques, accession numbers and the torch-line are the
only repeated furniture; everything else is an object, a
label, or night. If a room feels empty, the cure is a larger
object or a longer look — never a second widget.

**Room-by-room build sheet.** The round is fixed; a build
that reorders rooms has built a different museum. Each room
declares its principal object, its active elements and its
ambient rule — the sheet the gate (§10) checks the DOM
against:

| Room | Principal content | Elements active | Ambient rule |
|---|---|---|---|
| I — The Vitale | Entrance wall: counters band, the show's poster object | §6.5 (hero above), §6.11, §6.4 | Counters strike only on the beam's first park |
| II — First Portraits | Portrait pair, one landscape | §6.3, §6.4, §6.10 | Blinks at full rate only while the beam is in II or III |
| III — The Long Wall | The Procession Frieze, full bleed | §6.7, §6.2 (44 motes), §6.4 | Dust at its thickest; the room is 300vh of scrub |
| IV — The Marble Boy | The boy on his plinth, one portrait | §6.10 (the famous back), §6.3, §6.4 | The quietest room: no counters, no spots, one label |
| V — The Masterpiece | The pinned painting, three labels | §6.8, §6.4, §6.1 (beam parks longest) | Beam dwell is the room's whole climate |
| Corridor | Works on paper, four spots | §6.9, §6.14 (doorways both ends) | The only room whose lights are the building's, not the guard's |
| VI — The Night Desk | Booking desk, programme table, lantern | §6.16, §6.6, §6.11 (miniature band) | Lantern light, steadied by the form's focus |
| VII — The Quiet Room | One closing object, the plan, the door | §6.12, §6.4 | Beam parks centre-room and does not travel again |

**Beam geometry.** The pool is not a circle pasted on the
page; it is an ellipse corrected for the wall: at desktop
the gradient's vertical radius is 0.92× its horizontal
(430px × 396px), because a torch held at chest height
throws a taller pool on a wall than the visitor's screen
geometry suggests, and the correction keeps lit objects
from appearing to float inside a perfect disc — perfect
discs read as UI, ellipses read as light. The halo
(§6.1) is a true circle at 1100px and 12%: distance haze
does not keep the wall's correction. Both layers clip at
the doorway bands (§6.14) so a room being entered is lit
before its predecessor fully dies — the guard's light
spills through a doorway ahead of him, as light does.

## 5. Full motion system

One shared `requestAnimationFrame` loop drives every scrubbed
value on the page — beam position, halo lag, frieze travel,
counter ticks, pupil offsets, patina — through a single lerp
at **0.12** (the beam's own spring is layered on top, §6.1).
No scroll handler writes styles. Named easings, used
consistently and nowhere else: `--ease-round`
(cubic-bezier(0.22, 1, 0.36, 1)) for the beam's room-to-room
travel and doorway dissolves; `--ease-lamp` (cubic-bezier(0.34,
1.3, 0.64, 1)) for lantern sway settle and label glow;
`--ease-flicker` (steps(6)) for flame and faulty-lamp
sequences — the only stepped easing, because faulty light does
not interpolate; `--ease-strike` (cubic-bezier(0.7, 0, 0.2, 1))
for stamps, seals and the booking confirmation.

**Every motion term, in this theme's language.** *Scroll-
triggered reveals:* rooms are not revealed — they are entered;
the beam's arrival (§6.1) is the trigger for each room's
label glow (§6.4), counters (§6.11) and spots (§6.9), all
keyed to the beam, never to bare IntersectionObserver timers,
so the fiction has one cause. *Scroll-driven / scrubbed:* the
frieze (§6.7) and the masterpiece pin (§6.8) are true scrubs
bound to the shared loop; the beam widens by up to 8% with
travel velocity and settles as the guard slows. *Parallax:*
three depths only — artworks at 1.0, their labels at 1.02
(they hang slightly proud of the wall), the dust layer at
0.96 inside the beam (§6.2); nothing else moves at a different
rate, because a museum wall is flat and lying about its depth
is slop. *Pinned sections:* exactly one — the masterpiece,
~260vh (§6.8). *Smooth scrolling:* the round is walked at
natural scroll; anchor jumps from the plaques (§6.13) run a
1400ms `--ease-round` glide with the beam leading the eye.
*Progress indicator:* the torch-line (§4). *Staggered and
masked reveals:* the entrance sequence (§6.5) and the nav
plaques' glint stagger at 90ms; masked line reveals are
refused — print in a museum does not wipe in, it is *lit*.
*Kinetic typography:* the hero title catching light letter by
letter (§6.5) is the theme's only kinetic type. *Marquee:*
refused — nothing in a night museum runs on a loop of text;
the closest legal relative is the frieze, which is an artwork,
not a ticker. *Counters:* brass, only when lit (§6.11).
*SVG line-draw:* the footer floor-plan route (§6.12), drawn
once, in brass, ending at the door. *Image scale-in-frame:*
artworks never scale; light warms them (§6.9). A photograph
that zooms is a shop; a painting that warms under a lamp is a
museum. *Hover / micro-interactions:* hover lingers the torch
— the hovered object's local glow deepens over 300ms
`--ease-lamp` (§6.4's lamplight, deepened); labels flip
(§6.10); plaques glint. *Magnetic buttons and tilt:* refused —
the visitor holds no torch and tilts no paintings. *Custom
cursor:* refused absolutely; the normal system cursor is the
only pointer, and the beam is scroll-driven, never a pointer
replacement (the original entry's explicit rule). *Skeleton
loading:* the unlit room (§6.18) — frames at ambient level
with a single slow beam-pass. *Page transitions:* doorway
cross-dissolves (§6.14) with a 3000ms ceiling. *Reduced
motion:* the beam parks as a static vignette centred on the
reading column, all art shown lit, counters at final values,
lanterns still, portraits still, the frieze scrollable as a
plain horizontal panel — the finished, lit museum, complete.

**Ambient loops — exactly three licensed.** The lanterns'
pendulum sway (§6.6), the dust drift inside the beam (§6.2),
and the corridor spots' breathing once settled (§6.9). Each
pauses when its room leaves the viewport and under
`document.hidden`. Anything else that moves on a timer is a
gate failure: stillness is this theme's loudest material and
it is rationed like light.

**Master timing table.** Every named duration in the
theme, in one place — a build that needs a duration not
in this table invents it in §6 first, then adds it here:

| Beat | Duration | Easing | Owner |
|---|---|---|---|
| Beam bloom (entrance) | 600ms | `--ease-round` | §6.5 |
| Title sweep / letter catch | 1100ms / ~55ms per letter | `--ease-round` | §6.5 |
| Beam room-to-room glide | ~900–1400ms perceived | spring 42/11 over lerp 0.12 | §6.1 |
| Label glow after park | +500ms delay, 700ms in | `--ease-lamp` | §6.4 |
| Plaque glint stagger | 90ms apart, 500ms sheen | `--ease-lamp` | §6.13 |
| Lantern amplitude build | 2000ms | `--ease-lamp` | §6.6 |
| Blink | ~130ms, every 2.6–7.2s seeded | `--ease-lamp` | §6.3 |
| Counter strike | 1400ms at 30ms quanta | `--ease-round` | §6.11 |
| Label flip / return | 550ms / 450ms | `--ease-round` | §6.10 |
| Spot strike sequence | 0/180/390/640ms, settle ≤700ms | `--ease-flicker` steps(6) | §6.9 |
| Doorway dissolve | 800ms (600ms mobile) | `--ease-round` | §6.14 |
| Route draw | 2600ms | `--ease-round` | §6.12 |
| Stamp strike | 140ms at submit +500ms | `--ease-strike` | §6.16 |
| Skeleton beam-pass | 2400ms, ≤3 passes | `--ease-round` | §6.18 |
| Watchdog deadline | 4000ms | — (a deadline, not a motion) | §6.1 |

**Velocity is a mood, rationed.** The beam widens with
travel speed (§6.1) and the lanterns rock harder (§6.6),
and that is the whole of the theme's velocity response.
Nothing speeds up its *performance* because the visitor
is hurrying: label delays do not shorten, the flicker
does not quicken, the pin does not release early. A guard
who runs because a visitor runs has stopped being the
calm centre of the building, and a page whose every
animation is scroll-velocity-reactive reads as anxious,
not alive. The two licensed responses share one trait —
they are the physics of carried things (a lamp's pool
spreads as it moves; a hanging lantern swings when its
building is walked through), not rewards for scrolling
fast. Any proposed third velocity response must name its
physical cause in the building or be refused at review.

**The one-cause rule.** Every scroll-triggered event in
the table traces to a single cause — the beam's position
or a doorway crossing — computed once per frame in the
shared loop and published as CSS properties and classes.
No element runs its own scroll listener, its own
IntersectionObserver carnival, or its own clock for a
scrubbed value. This is not tidiness: it is what makes
the fiction true. A museum in which the label glows
because a timer fired, the counter strikes because a
different observer fired, and the beam arrives third is a
building with three guards who do not speak. One loop,
one guard.

## 6. Signature elements

### 6.1 The roaming torch beam

- **What & why.** A warm radial light pool, ~430px radius at
  desktop, that travels room to room as the visitor scrolls —
  the guard's round made visible. It is the theme's engine and
  its argument: attention in a museum is a physical act
  performed by a person carrying light, and every other element
  on the page takes its cue from where the light currently is.
- **Structure.** A fixed overlay div (`.beam-layer`) above
  content, below plaques: one radial-gradient pool
  (`--beam-warm` at 34% heart → transparent) composited over
  the night wash, plus a second, wider halo layer at 1100px
  and 12% (§5). Both `pointer-events:none`, `aria-hidden`. The
  pool's centre is a pair of CSS custom properties
  (`--beam-x`, `--beam-y`) written only by the shared rAF loop.
  Room anchors are the principal objects' centres, read from
  the DOM at arm time and on resize.
- **Motion spec.** Trigger: scroll position mapped to the
  current room anchor. Travel runs on a spring layered over the
  shared lerp: stiffness 42, damping 11 — the pool glides,
  overshoots by at most 6px, and settles like a carried lamp.
  Radius breathes ±2% on a 7000ms sine and widens up to +8%
  with travel velocity, narrowing as the guard slows. Room-to-
  room travel across a full room height takes ~900–1400ms of
  perceived glide. A slow patrol sway (±14px horizontal,
  11000ms) keeps the parked beam alive without moving it off
  its object.
- **States.** Travelling (between anchors, widened) → parked
  (on an object, breathing) → lingering (deepened by hover,
  §6.4) → house-lights (watchdog state, below). Scrolled-past
  rooms keep a faint warm residue in the halo only — the guard
  has been there; the room is not re-darkened to black.
- **Content merge.** The beam *is* the navigation: where it is,
  is where the visitor is on the round. Remove it and the page
  loses its wayfinding, not a decoration — the plaques (§6.13)
  report its room, the labels (§6.4) answer its arrival.
- **Failure fallback.** The 4000ms watchdog: the beam system
  must confirm itself (loop running, anchors resolved, one
  travel completed or parked) within 4000ms of arming, or the
  overlay is killed, the wash drops to the house-lights lift
  (§2), and a static vignette remains. No-JS: no overlay is
  ever inserted — it is created by the arming script — and the
  page stands as a lit dark site.
- **Reduced-motion variant.** The pool parks as a static
  vignette centred on the reading column; no travel, no sway,
  no breathing. The wash sits at house-lights lift.
- **Performance budget & mobile variant.** Two gradient layers,
  transform/opacity only, zero per-frame layout; the loop
  sleeps when the tab is hidden. Mobile (<768px): pool radius
  240px, halo cut entirely, spring softened (stiffness 30) so
  travel reads as a gentle drift on a small screen.
- **Choreography timeline (v2).** t=0 arm (overlay inserted,
  wash at 88%) → t=0–600ms bloom (§6.5) → parked on the hero
  object → on scroll: velocity sampled each frame → pool
  widens to +8% within 200ms of travel start → anchor handoff
  at room boundary → settle overshoot ≤6px over ~350ms →
  parked, breathing resumes at t=+700ms → watchdog deadline
  t=4000ms passes unused (confirmation logged at first park).
- **State matrix (v2).** *Rest:* parked, breathing. *Hover:*
  the beam itself has none; hover acts on objects (§6.4).
  *Focus:* keyboard focus on an object in another room glides
  the beam to it over 900ms `--ease-round` — a keyboard
  visitor is walked to, not left in the dark. *Active:* n/a.
  *Scrolled-past:* halo residue only. *Disabled / no-JS:* no
  overlay; house-lights lift. *Touch:* identical — the beam
  follows scroll, never the finger.
- **Breakpoints (v2).** ≥1200px: pool 430px, halo 1100px.
  768–1199px: pool 340px, halo 800px at 9%. <768px: pool
  240px, no halo, wash 84% (smaller screens get slightly more
  ambient, because the pool covers less of the text).
- **Edge cases & failure modes (v2).** *Anchor missing*
  (an object removed by a CMS): the beam parks on the room
  plaque instead and the watchdog logs the gap — it never
  parks on empty wall. *Very fast scroll to the footer:* the
  spring is clamped to a maximum travel speed; the pool
  arrives late but composed, and intermediate rooms' labels
  (§6.4) fire their glow from the scroll sweep, not the park.
  *Resize mid-travel:* anchors re-read, target recomputed,
  no jump — the spring continues from its current position.
  *Scroll up:* the guard walks back; residue rooms re-warm
  at half depth, labels do not re-perform their first glow.
- **Accessibility spec (v2).** Purely presentational:
  `aria-hidden`, absent from tab order, and no information is
  carried by the beam that is not also in the DOM (room
  position is announced by the plaques, §6.13). Contrast is
  guaranteed by the covenant with the beam anywhere (§2).
- **Tokens consumed (v2).** `--night`, `--beam-warm`,
  `--beam-r` (430px), `--halo-r` (1100px), `--ease-round`,
  `--lerp` (0.12), `--wash` (88%).

### 6.2 Dust motes visible only in the beam

- **What & why.** ~36 motes drift and twinkle inside a layer
  masked to the beam's exact position; outside the light they
  do not exist. It belongs because it gives the light a
  *medium*: the visitor sees the air the guard breathes, and
  the beam stops being a graphic effect and becomes a volume.
- **Structure.** A canvas (or 36 divs at low counts) inside
  `.beam-layer`, clipped by a radial mask sharing `--beam-x /
  --beam-y / --beam-r`. Motes are 1–2.5px ivory dots at
  20–70% opacity, each with a seeded drift vector and twinkle
  phase — seeded, never runtime-random, so two builds render
  the same air.
- **Motion spec.** Drift 4–11px/s along each vector with a
  slow sinusoidal wander; twinkle on a 2600–4800ms cycle per
  mote; motes fade at the mask's edge over the outer 15% of
  the radius. The layer inherits the beam's spring exactly —
  it is masked *to* the beam, so it cannot lag or lead it.
- **States.** Inside beam: drifting, twinkling. At mask edge:
  fading. Outside: nonexistent (not hidden — clipped).
  Tab hidden or room off-screen: the loop segment sleeps.
- **Content merge.** The motes are the room's air made
  visible; they thicken slightly (36 → 44) in the frieze room
  (§6.7), where a 12-metre wall has stood in the dark longest
  — atmosphere with a curatorial reason.
- **Failure fallback.** Canvas failure or low-power device:
  the layer is simply absent. Nothing references it; the
  beam reads clean. No watchdog needed — the fallback is
  silence, and silence is in-theme.
- **Reduced-motion variant.** Motes are printed static at
  30% opacity inside the parked vignette, or omitted on
  low-power devices; no drift, no twinkle.
- **Performance budget & mobile variant.** Canvas 2D, ≤44
  points, one draw per frame shared with the main loop;
  budget ≤0.3ms/frame. Mobile: 18 motes, twinkle cut.
- **Choreography timeline (v2).** t=0 (beam parked) motes
  fade in over 1200ms → continuous drift → on beam travel,
  motes streak ≤2px along the travel vector (air displaced
  by the walk) → settle by t=+500ms after park → on room
  exit, fade with the wash, no independent exit.
- **State matrix (v2).** *Rest:* drifting. *Hover/focus/
  active:* none — the air does not respond to the visitor.
  *Scrolled-past:* absent with its room. *Disabled:* static
  or absent (above). *Touch:* identical to desktop.
- **Breakpoints (v2).** ≥1200px: 36 motes (44 in the frieze
  room). 768–1199px: 26. <768px: 18, radius-matched to the
  240px pool.
- **Edge cases & failure modes (v2).** *Mask unsupported:*
  the layer falls back to the beam div's own
  `overflow:hidden` rounded clip; if neither works, the
  layer is not inserted. *Beam at viewport edge:* motes
  clip with the mask — no motes ever appear in unlit space,
  which would break the fiction and the law's spirit.
- **Accessibility spec (v2).** Decorative, `aria-hidden`,
  no motion essential to comprehension; fully suppressed
  under reduced motion except as a static texture.
- **Tokens consumed (v2).** `--beam-x`, `--beam-y`,
  `--beam-r`, `--ivory`, `--mote-count` (36).

### 6.3 Portraits whose pupils follow the beam

- **What & why.** Three portraits' pupils track the light
  pool's position, clamped to a few pixels, and each portrait
  blinks on its own unsynchronised schedule; the gilt frames
  lean almost imperceptibly toward the light. The collection
  is awake at night — the museum's fiction told by its
  artworks, not by copy claiming spookiness.
- **Structure.** Each portrait is a layered composition:
  frame (CSS gilt border with gradient), face plate (image
  or painted SVG), and a pupil layer — two absolutely
  positioned pupils whose offset is computed from the beam's
  position relative to the portrait's centre. Eyelids are a
  scaleY-clipped overlay per portrait. All three portraits
  are real collection objects with accession numbers and
  labels (§6.4), not decorative heads.
- **Motion spec.** Pupil offset = beam direction clamped to
  ±3px horizontal, ±2px vertical, eased through the shared
  loop so the gaze *drifts* rather than snaps. Blinks: each
  portrait on its own seeded schedule, every 2.6–7.2s, lid
  closes and opens in ~130ms `--ease-lamp`. Frame lean:
  rotate toward the beam by at most 0.4deg, so slow it reads
  as unease, not animation.
- **States.** Beam near: gaze on the light. Beam in another
  room: gaze rests at centre, blinks continue at half rate
  — they watch less when unwatched. Hover on a portrait:
  its gaze drops to its own label, as if caught looking.
  Scrolled-past: still, mid-blink states never persist.
- **Content merge.** The portraits are exhibits on the round
  (Rooms II, IV and V); their behaviour *is* their wall
  text's claim — the guard's note on the back of one label
  (§6.10) reads "She watches the torch. They all do, a
  little." Remove the pupils and a printed sentence on the
  page becomes a lie.
- **Failure fallback.** Pupils are an enhancement layer over
  complete portrait images; if the layer fails, the
  portraits hang as ordinary lit portraits. Blinks are
  timer-driven and independently fail-safe: a stuck lid is
  reset by a 600ms watchdog per blink.
- **Reduced-motion variant.** Pupils centred, lids open,
  frames square. The portraits are simply portraits.
- **Performance budget & mobile variant.** Six pupil nodes +
  three lids, transform-only; ≤0.1ms/frame. Mobile: pupils
  kept (they are the point), frame lean cut, blink rate
  halved.
- **Choreography timeline (v2).** Beam enters room → pupils
  begin drifting toward it over ~800ms → beam parks → gaze
  settles on the pool's centre → blink schedule runs
  independently (seeded offsets 0ms / 1900ms / 3400ms) →
  beam departs → gaze returns to centre over 1200ms, slower
  than it came — reluctance is a timing decision.
- **State matrix (v2).** *Rest:* centred gaze, blinking.
  *Hover:* gaze to own label (above). *Focus:* keyboard
  focus on the portrait sends its gaze to the label and
  holds it while focus lasts — the same joke, told accessibly.
  *Active:* n/a. *Scrolled-past:* frozen open-eyed.
  *Disabled/no-JS:* static portraits. *Touch:* no hover
  state; a tap flips the label (§6.10) and the gaze drops
  for 1200ms as if caught.
- **Breakpoints (v2).** ≥1200px: full behaviour, lean on.
  768–1199px: lean off, pupils ±2.5px. <768px: pupils ±2px,
  blinks kept (they cost nothing and carry the fiction on
  the smallest screen).
- **Edge cases & failure modes (v2).** *Beam directly over
  the portrait:* gaze centres — a portrait does not look at
  a light in its own face. *Two portraits in one room
  (Room IV pair):* both track; their blink schedules are
  seeded apart so they never blink in unison, which would
  read as a glitch instead of a haunting. *Image swap by
  CMS:* pupil layer positions are percentage-based within
  the eye line declared in the object record; a portrait
  without eye-line data ships without pupils — never guess
  where eyes are.
- **Accessibility spec (v2).** The portraits' alt text
  describes the sitter, not the behaviour; the behaviour is
  decorative and `aria-hidden` at the layer level. Nothing
  about the gaze is announced. Blink frequency is far below
  any photosensitivity threshold and lids are small-area.
- **Tokens consumed (v2).** `--ease-lamp`, `--ivory`,
  `--brass` (frames), `--pupil-max` (3px), `--blink-dur`
  (130ms).

### 6.4 Labels that light a beat after the art

- **What & why.** Each wall label rests legible at ambient
  level with its own soft lamplight, then deepens its glow
  ~0.5s after its artwork is centred by the beam. The guard
  looks at the art first and reads second; the page teaches
  the visitor to do the same. It is the theme's pedagogy in
  a half-second delay.
- **Structure.** A label card (`.wall-label`) on `--wall`
  stock hanging at the object's right (desktop) or beneath
  it (smaller screens, §4): object name (small caps), maker,
  date, medium, accession line (§3), and the flip affordance
  (§6.10). The glow is a warm box-shadow + background lift
  to `--wall-lift`, driven by a `.lit` class armed by the
  beam system when the object parks.
- **Motion spec.** Beam parks on object at t=0 → label glow
  begins t=+500ms → background and shadow deepen over 700ms
  `--ease-lamp` → rest at lit level while the beam stays.
  Beam departs: glow recedes over 900ms, slower than it
  came. Hover at any time deepens the same glow over 300ms
  (the torch lingers) and adds 4% to the object's own warmth.
- **States.** Ambient (legible, unlit — the covenant state)
  → glowing (beam parked + 500ms) → lingering (hover) →
  receding (beam gone) → ambient. Flipped state is §6.10's
  and composes with all of these: a flipped label keeps its
  glow level.
- **Content merge.** The label is the object's own museum
  furniture; the glow sequence is meaningless without the
  label's real text — name, maker, the accession number —
  which is the collection record (§6.15), not filler.
- **Failure fallback.** Labels are fully legible at ambient
  in every failure mode; the glow is an enhancement layered
  on a card that never depended on it. If the beam system
  is in house-lights state, all labels sit at a permanent
  gentle lit level.
- **Reduced-motion variant.** No glow animation: labels in
  the current room are simply at lit level, others ambient.
- **Performance budget & mobile variant.** Box-shadow and
  background on ≤2 labels at once; shadow blur capped at
  24px. Mobile: glow becomes background-only (no shadow),
  delay shortened to 350ms — smaller screens, quicker reads.
- **Choreography timeline (v2).** t=0 beam parks → t=+500ms
  glow starts → t=+1200ms label at full lit level → the
  object's counter (§6.11), if any, is already running —
  data first, words second, matching the guard's habit →
  beam departs → t=+900ms label back to ambient.
- **State matrix (v2).** *Rest:* ambient. *Hover:* linger
  (above). *Focus:* a focused label takes the full lit
  level instantly — a keyboard reader never waits 500ms
  for permission to read. *Active:* press begins the flip
  (§6.10). *Scrolled-past:* ambient. *Disabled:* permanent
  lit level (house lights). *Touch:* tap = flip; the glow
  follows the beam only.
- **Breakpoints (v2).** ≥1200px: label right of object,
  glow with shadow. 768–1199px: beneath, right-aligned,
  shadow kept. <768px: full-width beneath, background-only
  glow, 350ms delay.
- **Edge cases & failure modes (v2).** *Long label text*
  (a bequest with three donors): the card grows downward;
  the glow is size-independent. *Beam passes quickly*
  (fast scroll): labels glow from the sweep if the beam
  crossed their object for ≥120ms, else stay ambient — a
  label must not strobe for a guard running past.
  *Two objects share one label* (a pair, Room IV): one
  glow, both objects listed — the museum's real convention.
- **Accessibility spec (v2).** Label text meets the
  covenant at ambient (ivory-dim on wall, 8.9:1) and at lit
  level; the glow change is decorative and never the only
  signal of anything. Focus order: object link, then its
  label's flip control (§6.10).
- **Tokens consumed (v2).** `--wall`, `--wall-lift`,
  `--ivory`, `--ivory-dim`, `--brass`, `--ease-lamp`,
  `--label-delay` (500ms).

### 6.5 Kinetic hero title catching light

- **What & why.** The exhibition title starts dim and
  catches light letter by letter as the beam's first sweep
  crosses it, then keeps a slow staggered glow pulse. The
  name of the show is discovered by the round, like
  everything else in the building — the entrance is the
  theme's thesis performed once, at the door.
- **Structure.** The title (Marcellus, §3) split into
  per-letter spans by the arming script only — the DOM
  ships the title as one whole text node inside an `h1`,
  fully legible at ambient. Each span carries a warm
  text-shadow and colour transition from `--ivory-dim` to
  `--ivory` with a `--beam-warm` bloom at the catch moment.
  Beneath: the standfirst, the night-opening hours, and the
  booking link (§6.16) — all printed, none animated in.
- **Motion spec.** Beam bloom: pool opens at centre over
  600ms `--ease-round` from 40px to full radius → first
  sweep crosses the title left to right over 1100ms → each
  letter catches as the pool's leading edge reaches it
  (~55ms per letter at display size) with a 180ms bloom
  overshoot → letters settle to ivory → a slow staggered
  pulse (each letter +6% warmth, 5200ms cycle, offset by
  position) continues while the hero is on screen. Nav
  plaques glint in stagger (§6.13) as the sweep completes.
- **States.** Pre-arm: whole title at ambient, legible.
  Catching: letters lighting in sequence. Rest: ivory,
  pulsing gently. Scrolled-past: pulse stops (loop sleeps).
  Returning within session: title starts lit, sweep skipped
  (`sessionStorage` flag `mad-intro`).
- **Content merge.** The letters are the exhibition's real
  name — the catch-light is how the visitor learns what
  show they are in, and the pulse keeps the name warm while
  they read the hours beneath it.
- **Failure fallback.** Watchdog at 2400ms: if the sweep
  has not completed (rAF starved), all letters jump to lit.
  No-JS: no spans, no sweep — the title stands at ambient,
  which the covenant makes fully legible.
- **Reduced-motion variant.** Title at full ivory from
  first paint; no sweep, no pulse.
- **Performance budget & mobile variant.** Text-shadow on
  ≤~24 letters, hero only; the pulse is a single shared
  keyframe with per-letter delay. Mobile: title at the
  clamp's floor, sweep 800ms, pulse cut (battery and
  dignity).
- **Choreography timeline (v2).** t=0 arm → t=0–600ms beam
  bloom → t=600–1700ms sweep + letter catches → t=1700ms
  standfirst's label-glow fires (§6.4) → t=1800ms plaques
  glint stagger (90ms apart) → t=2600ms pulse begins →
  watchdog deadline t=2400ms passes unused.
- **State matrix (v2).** *Rest:* lit, pulsing. *Hover:*
  none — a title is not a control. *Focus:* focus entering
  the hero completes the catch instantly. *Active:* n/a.
  *Scrolled-past:* pulse asleep. *Disabled:* static ivory.
  *Touch:* identical; the sweep is timed, not gestured.
- **Breakpoints (v2).** ≥1200px: display clamp max 76px,
  sweep 1100ms. 768–1199px: sweep 950ms. <768px: 800ms,
  pulse off, letters catch in two-letter steps (fewer
  simultaneous shadows on small GPUs).
- **Edge cases & failure modes (v2).** *Long exhibition
  titles* (three lines): the sweep follows reading order
  across lines; total catch time is capped at 1900ms by
  tightening per-letter delay — the guard does not dawdle.
  *Font swap late:* letters are spans of real text; a
  Marcellus swap mid-sweep reflows once and the sweep
  continues by letter index, not position.
- **Accessibility spec (v2).** The `h1` reads as one title
  to assistive tech (spans are presentational, the text
  node intact via `aria-label` on the heading if split).
  The catch is never required to read the title — ambient
  contrast is 8.9:1 before it starts.
- **Tokens consumed (v2).** `--ivory`, `--ivory-dim`,
  `--beam-warm`, `--ease-round`, `--ease-lamp`.

### 6.6 Swinging guard's lanterns

- **What & why.** Two lanterns — one in the hero, one in
  Room VI — swing with pendulum physics and carry a 6-step
  flickering flame. The guard is present in the page's
  furniture even when his beam is elsewhere: his lamps mark
  where he has been and where he will check last.
- **Structure.** Each lantern is an inline SVG (≤4KB):
  brass cage, glass, flame path — hung from a fixed point
  by a chain line whose rotation origin is the hanging
  point. The swing is a rotation of the whole lantern group;
  the flame is a separate path with its own flicker and a
  drop-shadow glow. Each lantern hangs beside a real object
  (the hero's beside the title's standfirst; Room VI's
  beside the night desk, §6.16) — furniture with an address.
- **Motion spec.** Pendulum: period ~2800ms, amplitude
  ±2.2deg, driven as a damped sine in the shared loop, with
  a pass-through wobble (a secondary 0.6deg sine at 1.7×
  frequency) so the swing never looks metronomic. Flame:
  6-step flicker via `--ease-flicker`, step changes every
  90–160ms (seeded), flame scaleY 0.92–1.08, glow opacity
  breathing with it. Scroll velocity adds up to +0.8deg of
  amplitude — the guard's walk rocks his lamps.
- **States.** Swinging (room on screen) → still (room off
  screen or tab hidden — the loop segment sleeps and the
  lantern parks at ≤0.3deg, never mid-swing frozen at an
  angle) → relit (on return, amplitude rebuilds over
  2000ms). Hover: none. The lanterns are not controls.
- **Content merge.** The hero lantern lights the standfirst
  it hangs beside — its glow pool is part of that text's
  ambient. Room VI's lantern is the booking desk's lamp:
  the form (§6.16) sits in its light, and its flame steadies
  (flicker amplitude halves) while the form has focus, as
  if set down on the desk.
- **Failure fallback.** A lantern that fails to animate is
  a still lantern: SVG complete, flame printed at mid-step.
  No watchdog needed beyond the loop's own health (the
  beam watchdog's house-lights state leaves lanterns lit
  and still).
- **Reduced-motion variant.** Lanterns hang straight, flame
  steady at step 3. Fully printed.
- **Performance budget & mobile variant.** Two SVGs, one
  rotation + one stepped path each; negligible. Mobile:
  hero lantern kept, Room VI lantern kept (it lights the
  form), wobble layer cut.
- **Choreography timeline (v2).** Room enters → amplitude
  0→full over 2000ms `--ease-lamp` → steady pendulum +
  flicker → scroll velocity spikes add amplitude within
  300ms → room exits → amplitude decays over 1200ms to park
  → loop segment sleeps.
- **State matrix (v2).** *Rest:* swinging gently. *Hover:*
  none. *Focus:* Room VI lantern steadies when the form
  (§6.16) holds focus. *Active:* n/a. *Scrolled-past:*
  parked. *Disabled:* still, lit. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: full physics + wobble.
  768–1199px: amplitude ±1.8deg. <768px: amplitude ±1.4deg,
  lantern scale 0.8, hung above its object rather than
  beside it (no horizontal room in a phone's corridor).
- **Edge cases & failure modes (v2).** *Flame flicker and
  photosensitivity:* the flicker is small-area (≤28px),
  low-contrast (warm on warm), and step changes are
  ≤7/second at micro scale — within safe bounds, and cut
  entirely under reduced motion. *SVG blocked:* a CSS
  lantern silhouette (border + radial gradient) ships as
  the img fallback — the lamp is present even unbuilt.
- **Accessibility spec (v2).** Decorative, `aria-hidden`;
  the lantern's light contribution is ambient styling, and
  no text depends on its glow to pass contrast (§2).
- **Tokens consumed (v2).** `--brass`, `--brass-lit`,
  `--beam-warm`, `--ease-flicker`, `--ease-lamp`,
  `--swing-amp` (2.2deg).

### 6.7 The Procession Frieze scrub

- **What & why.** A 12-metre frieze gets a reading mechanism
  sized to it: in its room, scroll moves the frieze track
  horizontally while a local glow travels inside the panel
  with the beam, so figures light as they pass. The wall
  moves; the light walks; neither alone would let a visitor
  *read* a procession.
- **Structure.** A pinned-adjacent (not pinned — a long
  scrub region of ~300vh) full-bleed panel: the frieze as a
  wide image/SVG track (figures in repeat with named
  episodes), a local radial glow layer inside the panel
  sharing the beam's logic at panel scale, figure captions
  beneath the panel keyed to the currently lit episode, and
  the frieze's own label (§6.4) with its true accession
  number and figure count (§6.11 counts them).
- **Motion spec.** Scroll progress through the 300vh region
  maps to track translation 0 → −(track width − viewport
  width) through the shared lerp (0.12) — no direct scroll
  binding, so the wall glides with weight. The local glow
  leads the track's reading edge by 12% of panel width.
  Episode captions cross-fade (400ms `--ease-round`) as the
  glow crosses each episode boundary. At region end, the
  track rests at its final figure for a full viewport
  before the room releases.
- **States.** Approaching (track at first figure, glow at
  its left) → scrubbing → resting at final figure →
  released. Scrolled back up: the procession walks
  backwards at the same fidelity — a procession reversed
  is still legible, and the captions follow.
- **Content merge.** The frieze is a real, named artwork
  with episodes that have titles; the captions are its
  scholarship. The mechanism exists because the object is
  12 metres long — remove the object and the mechanism has
  nothing to read.
- **Failure fallback.** No-JS or loop failure: the panel
  becomes a horizontally scrollable strip (native
  `overflow-x`) with all captions listed beneath in order.
  The frieze is never trapped inside a dead scrub.
- **Reduced-motion variant.** The native scrollable strip,
  glow parked at the reading edge, captions listed.
- **Performance budget & mobile variant.** One transformed
  track, one gradient; the track image is a single wide
  asset (budgeted in §14) with a 50%-scale mobile version.
  Mobile: scrub region 220vh, captions above the panel
  (below is thumb-covered while scrolling).
- **Choreography timeline (v2).** Region enters → beam
  hands off to the panel glow over 500ms → scrub: glow
  leads, figures warm as crossed, captions cross-fade at
  boundaries → final figure rests 100vh → glow hands back
  to the roaming beam over 500ms as the next room's doorway
  (§6.14) begins.
- **State matrix (v2).** *Rest:* first figure lit.
  *Hover:* hovering a figure pauses the caption cross-fade
  on that episode (the track itself never pauses — the
  visitor's scroll is the only motor). *Focus:* a focused
  episode link scrolls the region to that figure — the
  scrub is addressable, not a ride. *Active:* n/a.
  *Scrolled-past:* final figure, glow out. *Disabled:*
  native strip. *Touch:* scroll-driven identically.
- **Breakpoints (v2).** ≥1200px: 300vh region, full track.
  768–1199px: 260vh, track at 80% height. <768px: 220vh,
  captions above, figure height 38vh (figures must stay
  legible, so the track travels further per figure).
- **Edge cases & failure modes (v2).** *Track image
  shorter than declared:* episode boundaries are computed
  from the loaded image's real width, and the caption set
  is trimmed to episodes that exist — never caption a
  figure that is not there. *Fast scroll through:* the
  lerp lets the track arrive late; captions are keyed to
  actual track position, not scroll position, so they can
  never describe a figure not on screen.
- **Accessibility spec (v2).** The region is a labelled
  landmark ("The Procession Frieze — scroll to walk its
  length"); episodes are also present as a list of links
  in the room's label, so the content is reachable without
  scrubbing. Contrast of captions is covenant-grade.
- **Tokens consumed (v2).** `--wall`, `--ivory`,
  `--beam-warm`, `--ease-round`, `--lerp` (0.12),
  `--frieze-vh` (300vh).

### 6.8 Pinned masterpiece with rotating labels

- **What & why.** One masterpiece pins for ~260vh while
  three wall labels — the painting, the detail, the guard —
  rotate through beside it in sequence. One object, three
  ways of knowing it: what it is, what to look at, and what
  the night man thinks. The pin is an argument about
  attention, made with the visitor's scroll as the docent.
- **Structure.** A sticky stage (the painting at full
  column width, §4) with a label rail beside it holding
  three label cards (§6.4 stock) in a stack; scroll
  progress through the 260vh range selects the active
  label. The painting itself carries two detail insets
  (cropped plates of its own surface) that the second
  label references. Accession number and credit line are
  printed on the stage and never rotate — the object's
  identity is not one of the three views.
- **Motion spec.** Pin range 260vh. Label rotation at
  33% and 66% of range: outgoing label recedes (glow out,
  300ms), incoming label glows in on the §6.4 pattern
  (500ms delay compressed to 250ms here — the guard is
  already standing at this one). At 50% (the detail
  label's reign), the relevant detail inset warms +6%
  inside the painting's frame. The beam parks on the
  painting for the whole pin — the only room where it
  stays for three labels' worth of time.
- **States.** Entering (first label) → detail (second) →
  the guard (third) → releasing (pin ends, beam resumes
  its round). Scrolled back: the sequence reverses, labels
  in reverse order, no shortcuts.
- **Content merge.** The three labels are real texts: the
  curatorial label, a looking-guide to two actual details
  visible in the plates, and the guard's note (the §6.10
  flip's content, here given a full card — this is the
  object he has adopted). The pin's length is justified by
  3 × ~87vh of reading, not by spectacle.
- **Failure fallback.** No-JS / no-sticky: the three
  labels print in a row beneath the painting in order.
  The argument survives as a list; nothing is hidden in
  the unpinned state.
- **Reduced-motion variant.** Unpinned; labels stacked,
  all lit, in order.
- **Performance budget & mobile variant.** One sticky
  element, three cards, no canvas. Mobile: the pin
  shortens to 200vh and the label rail moves beneath the
  painting (side-by-side does not fit a corridor of 360px).
- **Choreography timeline (v2).** t=0 pin engages, beam
  parks → 0–33%: label I lit → 33%: cross-fade 300ms →
  33–66%: label II, detail inset warms at 50% → 66%:
  cross-fade → 66–100%: label III (the guard's) → 100%:
  pin releases, beam widens +4% and walks on.
- **State matrix (v2).** *Rest:* label I. *Hover:* hovering
  a detail inset previews its warmth (+3%) without
  changing the active label. *Focus:* each label card is
  focusable in DOM order; focus scrolls the pin range to
  that label's third — keyboard visitors get the same
  three readings. *Active:* n/a. *Scrolled-past:* third
  label rests lit until the room exits. *Disabled:*
  stacked labels. *Touch:* scroll-driven identically.
- **Breakpoints (v2).** ≥1200px: rail right, 260vh.
  768–1199px: rail right at narrower measure, 240vh.
  <768px: rail beneath, 200vh, detail insets stack inside
  the frame's lower edge.
- **Edge cases & failure modes (v2).** *Sticky unsupported
  (old browser):* the stage degrades to the stacked-label
  layout automatically via `@supports` — the fallback is
  the layout, not an error. *Painting image taller than
  the stage:* the stage scales to the frame; the pin range
  is unchanged, because the labels' reading time, not the
  image, sets the 260vh.
- **Accessibility spec (v2).** The active label is
  `aria-current` in the rail; all three labels are in the
  accessibility tree at all times (rotation is visual
  emphasis, never removal). The pin never traps focus —
  it is scroll geometry, not a modal.
- **Tokens consumed (v2).** `--wall`, `--ivory`, `--brass`,
  `--ease-round`, `--ease-lamp`, `--pin-vh` (260vh).

### 6.9 Corridor spotlights flicking on

- **What & why.** Four corridor spotlights arrive with a
  staggered faulty-lamp flicker, then settle into a gentle
  sway and breathing opacity; the artwork beneath each
  warms as its light arrives. The building's infrastructure
  has character — lights that struggle, then serve — and
  the corridor between Rooms V and VI is the one place the
  museum admits its wiring is old.
- **Structure.** Four spot fixtures (small SVG cones + glow
  pools) along the corridor section, each above a real
  corridor object (works on paper, hung in the passage as
  museums do). Each spot is an independent layer with its
  own seeded flicker pattern; the glow pool is a radial
  gradient at wall scale, warmer and smaller than the
  beam's — a different species of light.
- **Motion spec.** Trigger: corridor enters view. Spots
  fire in stagger (0 / 180 / 390 / 640ms — irregular, like
  a real bank of old lamps). Each flickers 3–5 times over
  400–700ms on `--ease-flicker` (opacity steps 0 → 40% →
  10% → 70% → 100%), then settles: sway ±1.7deg on a
  6000ms pendulum, opacity breathing ±4% on 8000ms. The
  object beneath warms +5% across the flicker, completing
  as its lamp settles.
- **States.** Dark (corridor unentered) → striking
  (flicker) → settled (sway + breathe) → off (corridor
  scrolled well past; the guard does not leave corridor
  lights burning). Re-entry: spots come on clean, no
  flicker — the struggle happens once per visit.
- **Content merge.** Each spot lights a specific corridor
  object named in the room's label; the flicker is the
  reason the label carries the line "The corridor lights
  are being replaced in spring. Until then, they
  rehearse." Infrastructure and interpretation in one.
- **Failure fallback.** A spot that fails to settle is
  forced to full by a 1500ms per-spot watchdog. All
  corridor objects are covenant-legible under ambient
  alone; the spots are warmth, not permission to see.
- **Reduced-motion variant.** Spots on at full, no
  flicker, no sway, no breathing.
- **Performance budget & mobile variant.** Four gradient
  pools + transforms; flicker is opacity steps (cheap).
  Mobile: two spots (the corridor narrows), flicker
  shortened to 2–3 steps.
- **Choreography timeline (v2).** Corridor enters → t=0
  spot I strikes → t=180ms II → t=390ms III → t=640ms IV →
  each settles by strike+700ms → t≈1400ms all settled,
  sway phase-offset per lamp → objects at full warmth →
  corridor exits → spots off over 600ms.
- **State matrix (v2).** *Rest (settled):* swaying,
  breathing. *Hover:* hovering a corridor object steadies
  its lamp (sway pauses) — the light attends. *Focus:*
  focused object's lamp on full and steady instantly.
  *Active:* n/a. *Scrolled-past:* off. *Disabled:* on,
  steady. *Touch:* no hover; lamps settle identically.
- **Breakpoints (v2).** ≥1200px: four spots, full flicker.
  768–1199px: four spots, sway ±1.2deg. <768px: two spots,
  flicker 2–3 steps, breathing cut.
- **Edge cases & failure modes (v2).** *Photosensitivity:*
  the flicker is the theme's one real risk — it is capped
  at ≤5 steps over ≥400ms per lamp (≤12.5 changes/sec at
  small area and low contrast, warm-on-dark), never
  full-screen, never synchronised across lamps, and
  removed entirely under reduced motion. A build that
  speeds the flicker up fails the gate on safety, not
  taste. *Corridor skipped by anchor jump:* spots come
  on settled (the visitor arrived after the rehearsal).
- **Accessibility spec (v2).** Decorative layers
  `aria-hidden`; object text never depends on spot state.
  The flicker cap above is part of this spec, not a
  styling note.
- **Tokens consumed (v2).** `--beam-warm`, `--ivory`,
  `--ease-flicker`, `--sway-amp` (1.7deg), `--spot-delay`
  (180ms base).

### 6.10 Flippable wall labels

- **What & why.** Every label flips — click or keyboard —
  to its back: the guard's note in small italic type. The
  official story and the night story are two sides of one
  card, and turning the card is the visitor's one act of
  trespass the museum permits. On the Marble Boy, the back
  reads: *"Reported moving between shifts. It does not."*
- **Structure.** A 3D flip card per label (front: §6.4's
  label; back: `--guard`-tinted stock, italic Source Serif,
  the guard's note + his round time "02:40" and initials).
  The flip is a rotateY on a wrapper with perspective;
  both faces are in the DOM, the back `aria-hidden` until
  flipped. Every label in the building flips — no exceptions,
  because a label that doesn't turn teaches the visitor to
  stop trying.
- **Motion spec.** Flip: 550ms `--ease-round`, rotateY
  0→180deg with a 40ms mid-flip shadow deepen (the card
  catches no light edge-on). Flip back: 450ms — returning
  to the official story is quicker than leaving it. Only
  one label per room may rest flipped; flipping a second
  returns the first (900ms, delayed 150ms) — the guard
  tidies behind the visitor.
- **States.** Front (official) → flipping → back (the
  guard's) → flipping back → front. Hover: the card's
  corner lifts 2px with a "turn" affordance (a small brass
  corner fold). Focus: full lit level (§6.4) + visible
  outline. Scrolled-past while flipped: it stays flipped
  until another in its room flips — the note waits for the
  next visitor, as a note would.
- **Content merge.** The backs are written per object and
  carry real night knowledge: condition worries ("North
  frame loose — reported Tuesday"), affections ("Best
  light in the building, 3 a.m."), and the one dry joke.
  A back that says something generic ("Interesting
  piece!") fails the anti-slop gate (§9) — the guard does
  not write brochure copy.
- **Failure fallback.** 3D transforms unsupported: the
  flip degrades to a cross-fade swap (300ms). No-JS: both
  faces print stacked, back beneath front, labelled
  "The guard's note:" — the trespass becomes a footnote,
  but the text is never lost.
- **Reduced-motion variant.** Instant cross-fade swap;
  no rotation.
- **Performance budget & mobile variant.** Transform on
  one card at a time; backface cost negligible. Mobile:
  flip axis stays rotateY but duration 450ms, and the
  card grows 4% mid-flip to keep the smaller back-text
  legible through the turn.
- **Choreography timeline (v2).** t=0 activate → t=0–275ms
  first half-turn, shadow deepens at 40ms → t=275ms edge-on
  → t=275–550ms second half, back lands with §6.4's glow
  inherited → if a roommate was flipped: it begins back at
  t=150ms, lands t=600ms → rest: back lit at the label's
  current glow level.
- **State matrix (v2).** *Rest:* front. *Hover:* corner
  lift + fold. *Focus:* lit + outline; Enter/Space flips.
  *Active:* mid-flip press state (scale 0.99). *Scrolled-
  past:* state persists per room rule. *Disabled:* both
  faces stacked in print. *Touch:* tap flips; the corner
  fold is printed permanently at 40% on touch (no hover to
  reveal it).
- **Breakpoints (v2).** ≥1200px: card at label size (§3).
  768–1199px: same, beneath objects. <768px: full-width
  card; back text 14px floor holds (§3 law 5) — the note
  wraps longer rather than shrinking.
- **Edge cases & failure modes (v2).** *Long guard's note*
  (he has moods): the back scrolls internally at most
  3 lines with a fade — beyond that, the note is edited,
  not scrolled; a label back is a card, not a document.
  *Rapid double-flip:* inputs during a flip are queued to
  one reversal; the card never spins. *Print:* backs print
  beneath fronts (the no-JS layout) — a printed label set
  includes the notes, marked as such.
- **Accessibility spec (v2).** The flip control is a real
  `<button>` wrapping the card, `aria-pressed` states the
  side, and the back's text enters the accessibility tree
  only when shown. Focus returns to the button after the
  flip. Target size: the whole card, ≥120×44px.
- **Tokens consumed (v2).** `--wall`, `--guard`,
  `--green-lit`, `--ivory`, `--brass`, `--ease-round`,
  `--flip-dur` (550ms).

### 6.11 Brass counters that tick only when lit

- **What & why.** Objects on view, frieze figures, night
  visitors and years on the round count up in brass
  numerals — only when their plaque enters the beam. Even
  statistics must be found by the round; data obeys the
  museum's night rules, and a number nobody has walked to
  yet has not been *seen* this visit.
- **Structure.** A counter band (usually Room I's end wall
  and repeated in miniature at the night desk, §6.16):
  four figures, each a tabular Source Serif numeral (§3)
  on a small brass plaque with its caption beneath. The
  final values live in the DOM as the printed text; the
  count-up is a JS re-write from a declared start (the
  previous season's figure, printed in the caption — so
  even the animation's *start* is a real number).
- **Motion spec.** Trigger: beam parks within the band's
  room. Count: 1400ms `--ease-round`, figures stepping in
  tabular increments (no rolling digits, no slot machines
  — numerals replace cleanly at 30ms quanta). All four
  start together; longer counts (frieze figures, 214) run
  the same 1400ms — rate differs, duration doesn't, like a
  guard reading four numbers off one plaque.
- **States.** Unlit (at previous season's figure, captioned
  as such) → counting → struck (final figure, a faint
  brass brighten to `--brass-lit` for 400ms at landing) →
  rest. Scrolled-past and back: stays struck — a counted
  thing stays counted.
- **Content merge.** The four numbers are the exhibition's
  true vitals from the collection record (§6.15): objects
  on view = the objects actually on the page's round;
  frieze figures = the figures in §6.7's track; the gate
  audits the DOM to prove the counts match the content.
- **Failure fallback.** No-JS: final figures printed (the
  DOM's text *is* the final value; JS rewinds it to count).
  Loop failure: figures stay at printed finals. There is
  no state in which a counter shows a wrong number.
- **Reduced-motion variant.** Final figures, no count.
- **Performance budget & mobile variant.** Text writes at
  30ms quanta on ≤4 nodes for 1400ms — trivial. Mobile:
  identical (the band stacks 2×2), count 1100ms.
- **Choreography timeline (v2).** Beam parks in band's
  room → t=+300ms (after the room's first label begins its
  glow, §6.4 — the guard glances at the plaque after the
  art) → count 1400ms → landing brighten 400ms → rest.
- **State matrix (v2).** *Rest (unlit):* previous figure,
  captioned. *Hover:* plaque glints (§6.13's glint) — no
  recount. *Focus:* a focused counter reads its final
  value (screen readers always get finals; the count is
  visual only). *Active:* n/a. *Scrolled-past:* struck.
  *Disabled:* finals printed. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: four in a row on the end
  wall. 768–1199px: four in a row, smaller plaques.
  <768px: 2×2 stack, captions beneath each figure.
- **Edge cases & failure modes (v2).** *Figure updated by
  the museum mid-season:* the final value is content, the
  start value is content; the animation between them is
  derived — nothing in the motion code hard-codes a number.
  *Beam arrives during a doorway dissolve (§6.14):* the
  count waits for the dissolve to finish; two performances
  never overlap.
- **Accessibility spec (v2).** Counters are `aria-hidden`
  during the count with a visually hidden final-value twin
  — assistive tech hears the true figure once, not a
  slot machine. Plaque contrast: brass on night 5.4:1 at
  30px (large) passes.
- **Tokens consumed (v2).** `--brass`, `--brass-lit`,
  `--night`, `--ease-round`, `--count-dur` (1400ms).

### 6.12 Footer floor-plan route

- **What & why.** The footer is a floor plan of the museum
  with the guard's route drawn through the six mapped rooms
  in brass SVG stroke as it arrives, ending at the door.
  The round completes itself as a drawing: the visit,
  mapped, is the souvenir — and the footer's links live on
  the plan, in the rooms they belong to.
- **Structure.** An inline SVG floor plan (walls in
  `--wall-lift` strokes on night, room numerals in
  Marcellus, doors as gaps in walls — drawn from the
  building's real plan proportions, simplified). The route
  is one brass path through Rooms I–VI and out. Footer
  links (visit, membership, contact) sit as labelled
  points on the plan: the ticket desk, the members' door,
  the night desk (§6.16). Colophon and legal lines print
  beneath in caption size.
- **Motion spec.** Trigger: plan enters view. Route draws
  over 2600ms `--ease-round` (stroke-dashoffset), room
  numerals fading in as the route enters each room
  (200ms each, sequenced by path length). At the door, the
  path ends in a small brass door-gap flash (300ms) —
  the guard clocks out. Draw happens once per session.
- **States.** Undrawn (plan printed, route at 12% opacity
  — the plan is legible before the performance) → drawing
  → complete (route at full brass, door flashed) → rest.
  Hover on a room: its numeral brightens and the room's
  name prints beside the plan.
- **Content merge.** The plan is the round the visitor
  just walked (§6.1–§6.11), redrawn as evidence; its links
  are placed where those functions live in the building.
  A footer that is a sitemap in a trench coat would waste
  the theme's best closing gesture.
- **Failure fallback.** No-JS: route printed at full
  opacity — the drawn state is the DOM state; JS rewinds
  the dash to perform the draw. SVG failure: the footer
  degrades to a text room list with the same links.
- **Reduced-motion variant.** Route printed complete; no
  draw.
- **Performance budget & mobile variant.** One SVG ≤9KB,
  one dash animation. Mobile: plan rotates to a vertical
  stack of rooms (the round drawn downward), draw 2000ms,
  room names always printed (no hover to reveal them).
- **Choreography timeline (v2).** Plan enters → t=+200ms
  draw begins → rooms numeral-in as route passes (I at
  ~300ms … VI at ~2100ms) → t=2800ms door flash → t=3100ms
  colophon label-glow (§6.4 pattern) → rest.
- **State matrix (v2).** *Rest:* drawn, complete. *Hover:*
  room name + brighten (above). *Focus:* footer links are
  ordinary links in DOM order (plan order: desk, members'
  door, night desk, then legal) — focus on a link
  brightens its room. *Active:* link press, standard.
  *Scrolled-past:* stays drawn. *Disabled:* printed route.
  *Touch:* room names always visible; tap = hover state.
- **Breakpoints (v2).** ≥1200px: plan at full width,
  horizontal. 768–1199px: plan at 80% width. <768px:
  vertical stack plan, names printed.
- **Edge cases & failure modes (v2).** *Seventh room
  added (a new gallery):* the route path is generated
  from the room list, not hand-drawn coordinates alone —
  rooms are nodes with plan positions in the collection
  record, and the path connects them in round order; a
  room missing from the plan fails the gate loudly
  rather than drawing a route through a wall.
- **Accessibility spec (v2).** The SVG is `aria-hidden`
  with a text equivalent (the room list) adjacent; links
  are real links with real text, never SVG-only hotspots.
- **Tokens consumed (v2).** `--night`, `--wall-lift`,
  `--brass`, `--brass-lit`, `--ease-round`, `--draw-dur`
  (2600ms).

### 6.13 Brass room-plaque navigation

- **What & why.** The site's navigation is a row of brass
  room plaques — Room I…VII with their names — fixed along
  the top beside the torch-line (§4). Museums direct you
  with plaques on walls, not hamburger menus; and at night,
  the plaque of the room the guard is in carries his light.
- **Structure.** A fixed header strip on `--night` at 92%:
  the museum wordmark (Marcellus, ivory), the seven plaques
  (brass-bordered chips: numeral in Marcellus, name in
  13px serif), and the house-lights toggle (§2). Each
  plaque is an anchor to its room. The current room's
  plaque is filled `--wall-lift` with a `--brass-lit`
  numeral — state read from the beam's room (§6.1), the
  same single source as everything else.
- **Motion spec.** Plaques glint in stagger (90ms apart)
  as the hero sweep completes (§6.5): a `--brass-lit`
  sheen crosses each plaque over 500ms `--ease-lamp`, once.
  Current-room change: the fill cross-fades 300ms; the
  numeral brightens over 500ms. Plaque click: the 1400ms
  glide (§5) with the beam leading.
- **States.** Rest (brass on night) → current (filled,
  lit numeral) → hover (sheen + numeral brightens) →
  focus (ivory outline, filled). A room not yet walked
  reads identically to one walked — the plaques are a map,
  not a progress test; the torch-line (§4) carries progress.
- **Content merge.** The plaques are the round's table of
  contents and its wayfinding in one; remove them and the
  visitor can neither jump the round nor know its shape.
- **Failure fallback.** Plain anchor list in a dark header
  — with JS dead, anchors jump natively and the header is
  a normal nav. Nothing about the plaques' function
  depends on the beam; only the current-room fill does,
  and it degrades to "no room marked," never a wrong room.
- **Reduced-motion variant.** No glint stagger; fills
  change instantly.
- **Performance budget & mobile variant.** Seven chips,
  CSS only. Mobile: plaques collapse to a horizontal
  scroll strip under the wordmark (numerals only, names
  on the current plaque), torch-line above it; no menu
  button — seven rooms fit a strip, and a museum with
  seven rooms does not need a drawer.
- **Choreography timeline (v2).** Entrance: glint stagger
  at §6.5 t=1800ms → on room change: old fill out 300ms,
  new numeral brightens by t=+500ms → on anchor click:
  beam departs immediately, glide 1400ms, arrival fill
  lands with the park.
- **State matrix (v2).** *Rest:* as above. *Hover:* sheen.
  *Focus:* outline + fill; `aria-current="location"` on
  the beam's room. *Active:* press dips the plaque 1px.
  *Scrolled-past:* n/a (fixed). *Disabled:* static nav.
  *Touch:* strip scrolls; tap = click.
- **Breakpoints (v2).** ≥1200px: full plaques with names.
  768–1199px: names shorten to the room's short title.
  <768px: numeral strip (above).
- **Edge cases & failure modes (v2).** *Room names long*
  ("Room VI — Works on Paper & the Night Desk"): short
  titles are declared in the room record; the plaque never
  truncates mid-word. *Beam between rooms:* the plaque of
  the room being *entered* fills — the map reports the
  destination, as a guard would call it.
- **Accessibility spec (v2).** A real `<nav>` with a list;
  current room conveyed by `aria-current`, never by fill
  alone (the numeral also bolds). Contrast: brass on night
  5.4:1 for numerals; names in ivory-dim 8.9:1-equivalent
  on night (higher) — passes.
- **Tokens consumed (v2).** `--night`, `--wall-lift`,
  `--brass`, `--brass-lit`, `--ivory-dim`, `--ease-lamp`.

### 6.14 Doorway transitions & the house-lights loader

- **What & why.** Between rooms, and between pages, the
  visitor passes through a doorway: a cross-dissolve in
  which the old room's light dies to a door-frame of night
  and the new room's beam blooms. Loading, when it must
  exist, is the house lights coming up — a state the
  building honestly has — never a spinner in the dark.
- **Structure.** In-page: room boundaries carry a doorway
  band (a 24vh night gradient with a hairline brass door
  frame at its centre line). Page-to-page: a transition
  overlay (night, with a centred door outline in
  `--wall-lift`) inserted by the router script only. The
  loader state reuses §6.1's house-lights lift: wash
  raised, a single line of text — "House lights." — and
  nothing else moving.
- **Motion spec.** Doorway dissolve: 800ms `--ease-round`
  cross-fade of the two rooms' ambient levels as the
  boundary crosses viewport centre; the beam hands over
  continuously (no dissolve on the beam itself — the
  guard walks through). Page transition: overlay in
  250ms, hold only while routing (hard ceiling 3000ms,
  §6.18's watchdog applies), new page's beam blooms per
  §6.5 (sweep skipped on internal arrivals — the guard
  is already inside).
- **States.** Closed (overlay out) → entering → holding
  (only under real load) → opening → gone. A hold past
  1200ms raises the house lights inside the overlay and
  prints the wait honestly: "The next room is being
  lit." Past 3000ms the overlay is removed regardless —
  a visitor is never held in a doorway by a loader.
- **Content merge.** Doorways are the building's real
  joints; the dissolve marks the same thresholds the
  floor plan (§6.12) draws. The loader's language is the
  watchdog's language (§6.1): one building, one set of
  states.
- **Failure fallback.** Transitions are progressive
  enhancement over ordinary links and ordinary scroll;
  any failure leaves standard navigation. The overlay is
  inserted only by the script that can remove it.
- **Reduced-motion variant.** No dissolve: rooms butt
  directly; page changes are instant, house-lights state
  still available under real load.
- **Performance budget & mobile variant.** Opacity on one
  overlay; doorway bands are gradients. Mobile: dissolve
  600ms, doorway band 16vh.
- **Choreography timeline (v2).** Boundary at centre →
  old room ambient −20% over 400ms → door hairline peaks
  → new room ambient restores over 400ms → beam continuous
  throughout → page route: overlay 250ms → bloom 600ms →
  out.
- **State matrix (v2).** *Rest:* absent. *Hover/focus:*
  none (not a control). *Active:* during route only.
  *Scrolled-past:* n/a. *Disabled:* absent; native
  navigation. *Touch:* identical.
- **Breakpoints (v2).** ≥1200px: 24vh bands. 768–1199px:
  20vh. <768px: 16vh, dissolve 600ms.
- **Edge cases & failure modes (v2).** *Back button mid-
  transition:* overlay is removed on `pageshow`
  unconditionally — a restored page never wears a stale
  doorway. *Prefetch hit (instant load):* the overlay
  never appears; transitions have a 200ms minimum route
  time before they may show at all.
- **Accessibility spec (v2).** Overlay `aria-hidden`;
  route changes are announced by the new page's heading
  through normal document flow. The hold text is a live
  region if the hold exceeds 1200ms.
- **Tokens consumed (v2).** `--night`, `--wall-lift`,
  `--brass`, `--ease-round`, `--hold-ceiling` (3000ms).

### 6.15 Object cards — the night store

- **What & why.** The collection listing — prints,
  editions and objects for sale or loan — presented as
  objects resting in a dark store room: cards at ambient
  level that warm as the beam's room reaches them, each
  carrying its true accession number, price or loan terms,
  and nothing else. Even commerce in this museum happens
  under the round's discipline.
- **Structure.** A grid of object cards (image plate on
  `--wall`, name, maker, accession line, price/terms in
  tabular serif, one action — "Reserve" or "Enquire" —
  as a text link with brass rule). Cards are real links
  to object pages. The beam does not visit the store room
  object-by-object; the room's ambient warms +4% when the
  round arrives, and hover gives a card the §6.4 linger.
- **Motion spec.** Room arrival: cards warm in a 60ms
  stagger (a shelf being lit, not a cascade of reveals).
  Hover: card plate warms +6%, glow 300ms `--ease-lamp`.
  No entrance animations beyond the warm — objects in a
  store do not perform.
- **States.** Ambient → warmed (room active) → hover/
  focus (lingered) → reserved (a brass "On reserve"
  plaque replaces the action — state from the record,
  never from a click's optimism). Sold/loaned objects
  remain visible, plaqued "Out on loan" — a store that
  hides its gaps lies about the collection.
- **Content merge.** Every card is a collection record:
  accession number, price and terms trace to §6.11's
  audit rule — the store's object count is one of the
  brass counters' sources.
- **Failure fallback.** A plain lit grid; the warm is
  styling. Images carry alt text and fixed aspect boxes
  so a slow image never reflows the shelf.
- **Reduced-motion variant.** No stagger; cards at warmed
  level in the active room.
- **Performance budget & mobile variant.** Images lazy
  below the fold, AVIF/WebP, ≤60KB per plate at mobile
  sizes. Mobile: one column, plates at 4:3, warm stagger
  cut.
- **Choreography timeline (v2).** Round enters store room
  → ambient +4% over 600ms → cards warm staggered 60ms →
  rest → hover linger per card → room exit: ambient
  settles back over 900ms.
- **State matrix (v2).** *Rest:* ambient. *Hover:* linger.
  *Focus:* card link outlined, plate warmed instantly.
  *Active:* press, standard. *Scrolled-past:* ambient.
  *Disabled:* lit grid. *Touch:* first tap warms, second
  follows the link — no, simpler and honest: tap follows
  the link; warming is scroll-arrival only on touch.
- **Breakpoints (v2).** ≥1200px: 3 columns. 768–1199px:
  2 columns. <768px: 1 column, plates 4:3.
- **Edge cases & failure modes (v2).** *Object without an
  image* (in conservation): the card shows its frame —
  an empty gilt frame plate with the line "In
  conservation — back in spring." An object is never
  represented by a stock photo; a false image is the
  store's one unforgivable lie. *Long titles:* two lines
  max, then the maker line yields — accession line never
  truncates.
- **Accessibility spec (v2).** Cards are single links
  (no nested interactive elements); price and state are
  text, never colour-only. Focus order follows the shelf.
- **Tokens consumed (v2).** `--wall`, `--wall-lift`,
  `--ivory`, `--ivory-dim`, `--brass`, `--ease-lamp`.

### 6.16 The night desk — booking form

- **What & why.** The conversion moment: booking a place
  on the monthly public night round (or a membership) at
  the guard's desk in Room VI, under his lantern (§6.6).
  The form is a desk ledger — ruled lines, serif entries,
  a brass stamp for the confirmation — because in this
  building even a transaction is written into a book.
- **Structure.** A form on `--wall` stock with ruled
  field lines (bottom-border rules in `--wall-lift`,
  brass on focus): name, email, places (stepper, 1–6),
  night (a select of real upcoming round dates with
  places remaining — real numbers from the booking
  record), and a notes line. Submit is a text button,
  "Enter it in the book." Errors print beneath their
  fields in the guard's voice (§12) in ivory with an
  alarm rule. Confirmation replaces the form with a
  stamped ledger entry: booking reference (generated
  from the date + sequence, e.g. `ROUND · 12 DEC · № 07`),
  the details reprinted, and the stamp (§5's
  `--ease-strike`) striking once.
- **Motion spec.** Focus: the field's rule warms to brass
  over 250ms and the lantern (§6.6) steadies. Field
  completion: a small brass tick draws (SVG stroke,
  200ms) at the line's end. Submit: the desk lamp dips
  200ms (the guard looks down to write) → confirmation
  entry fades up 400ms → stamp strikes at t=+500ms:
  scale 1.6→1 in 140ms `--ease-strike` with a 60ms
  overshoot shadow — once, never looping.
- **States.** Rest (ruled, dim) → focused (brass rule) →
  valid (tick) → error (alarm rule + voice) → submitting
  (lamp dip; button disabled with its text changed to
  "Writing…") → entered (stamped confirmation). The form
  never clears on error; entries persist through every
  failure, including a network failure, which reports:
  "The book is unreachable — your entry is kept here.
  Try again."
- **Content merge.** The booking is for the round the
  visitor has just walked virtually; the dates and
  remaining places are the museum's real night programme,
  and the confirmation's reference format is the desk's
  own. Remove the fiction and the form still works —
  remove the form and Room VI is a desk with nothing on it.
- **Failure fallback.** A standard HTML form posting to a
  real endpoint; JS enhances (ticks, stamp) but the
  no-JS path submits and confirms on a plain page in the
  theme's dress. Validation exists server-side regardless.
- **Reduced-motion variant.** No stamp strike (stamp
  printed), no lamp dip; ticks appear instantly.
- **Performance budget & mobile variant.** No libraries;
  the stamp is one SVG ≤3KB. Mobile: single column,
  stepper becomes a select (thumbs miss steppers in the
  dark), stamp at 0.8 scale.
- **Choreography timeline (v2).** Focus → rule warms
  250ms, lantern steadies by 600ms → blur with valid
  entry → tick draws 200ms → submit → lamp dips 200ms →
  response → entry fades 400ms → stamp strikes at +500ms
  (140ms) → rest, stamped.
- **State matrix (v2).** *Rest:* ruled dim. *Hover:*
  rule lifts to `--ivory-faint`. *Focus:* brass rule +
  visible outline offset. *Active:* button press dip.
  *Disabled:* submitting state only, with live text.
  *Scrolled-past:* n/a. *Touch:* 48px fields, 16px input
  text (no iOS zoom), stepper→select per above.
- **Breakpoints (v2).** ≥1200px: two-column ledger
  (details left, summary right). 768–1199px: one column,
  summary above the button. <768px: one column, select
  stepper, stamp 0.8.
- **Edge cases & failure modes (v2).** *Night sells out
  while the form is open:* on submit the error is
  specific and kind — "That round filled while you were
  writing. The next is 9 January — shall I move your
  entry?" with a one-tap move, never a dead end.
  *Duplicate submit:* the button disables at first press
  and the reference is idempotent per session — the book
  does not take the same entry twice. *Autofill:* fields
  are standard types with autocomplete attributes; the
  tick fires on autofilled validity too.
- **Accessibility spec (v2).** Labels are real `<label>`s
  (the ledger line is styling, not a substitute); errors
  are `aria-describedby`-linked and announced; focus is
  never lost on submit — it moves to the confirmation
  heading. Contrast: ivory on wall 14.6:1-equivalent;
  alarm rules are paired with text, never alone.
- **Tokens consumed (v2).** `--wall`, `--wall-lift`,
  `--ivory`, `--brass`, `--alarm`, `--ease-strike`,
  `--ease-lamp`, `--stamp-dur` (140ms).

### 6.17 The guard's log — search & exhibition index

- **What & why.** Search, in a night museum, is asking the
  guard. The index page is his log book: a single search
  line and the exhibition/object index printed as log
  entries — each with room, accession number and a line of
  his description — lit evenly under house lights, because
  a visitor with a question has left the round's fiction
  and wants an answer, not a walk.
- **Structure.** A lit surface (house-lights tokens, §2):
  search input (serif, large), filter chips by room
  (the plaques' short titles), results as log rows —
  object name, room plaque numeral, accession line, one
  line of description, link. Results count printed in
  brass tabular numerals. This is the one page where the
  beam does not perform; a small parked vignette at the
  page's edge acknowledges the building without taxing
  the task.
- **Motion spec.** Filtering is instant (no animation on
  results — answers do not fade in). The only motion:
  the count numeral replaces cleanly (§6.11's quanta),
  and a chosen result's row warms 200ms before navigation
  (the guard's finger on the line). Page load: none —
  the log is open when you arrive.
- **States.** Rest (full index) → filtered (count true)
  → empty (§6.18's voice) → error (index unreachable:
  the log prints what it has, cached, with the line
  "The log is a copy tonight — the desk has the original."
  and a desk link).
- **Content merge.** The log's descriptions are the
  guard's lines from the label backs (§6.10), reused —
  search here surfaces the night knowledge, not the
  catalogue's dry fields alone.
- **Failure fallback.** The index is server-rendered and
  complete without JS; search degrades to a GET form.
  No result is ever behind a client-side wall.
- **Reduced-motion variant.** Identical (there is almost
  no motion to reduce — deliberately).
- **Performance budget & mobile variant.** Rows are text;
  the page is the fastest on the site and §14 budgets it
  so. Mobile: chips wrap, rows stack room numeral above
  name.
- **Choreography timeline (v2).** Query typed → debounce
  200ms → results replace in one frame, count updates →
  row chosen → warm 200ms → doorway transition (§6.14)
  to the object's room, beam arriving with the visitor.
- **State matrix (v2).** *Rest:* open log. *Hover:* row
  warms slightly. *Focus:* input has the brass rule
  (§6.16 pattern); rows are links in order. *Active:*
  standard. *Disabled:* n/a. *Touch:* 48px rows.
- **Breakpoints (v2).** ≥1200px: rows in two columns
  (log spread). 768–1199px: one column. <768px: one
  column, chips scroll horizontally.
- **Edge cases & failure modes (v2).** *Query matches an
  object out on loan:* it appears, plaqued (§6.15's
  state) — the log does not pretend the collection is
  all home. *Accession-number query:* an exact accession
  match pins to the top with its room — the guard knows
  the numbers by heart, and the log should too.
- **Accessibility spec (v2).** Results count is a polite
  live region; the search input is labelled "Ask the
  log"; house-lights contrast throughout (this page is
  the covenant's easiest pass and sets the bar).
- **Tokens consumed (v2).** `--night` (house-lift),
  `--wall`, `--ivory`, `--brass`, `--ease-lamp`.

### 6.18 The unlit room — skeletons, empty states & the 404

- **What & why.** Every absence in the building gets the
  same honest treatment: a room with its frames hung and
  nothing lit yet (loading), a room with nothing in it
  (empty), and Room VIII — which does not exist (404).
  Absence, in this theme, is a place, not an error
  template.
- **Structure.** *Skeleton:* the room's layout printed at
  ambient level — frame rectangles on the wall at true
  aspect ratios, label cards as ruled stock — with one
  slow beam-pass across them every 4000ms (the guard
  checking a room being hung). *Empty state:* the room
  printed complete with one line in the guard's voice
  (§12) and the way onward. *404:* a doorway onto night,
  a plaque reading "Room VIII", and the line: "There is
  no Room VIII. The round goes I to VII — here is the
  plan." with §6.12's floor plan beneath.
- **Motion spec.** Skeleton beam-pass: the pool (§6.1's
  gradient at 60% strength) crosses the room over 2400ms
  `--ease-round`, pauses 1600ms, repeats — maximum three
  passes, then the room rests ambient (a room that loads
  forever stops performing and simply says so, §6.14's
  hold language). Empty and 404: no motion except the
  plaques' rest state.
- **States.** Loading → loaded (content replaces the
  skeleton in place, no flash of lit-then-dark: new
  content arrives at ambient and the beam finds it on
  the round's schedule) → timed-out (house lights + the
  honest line + retry). Empty and 404 are terminal
  states, complete as printed.
- **Content merge.** The skeleton's frames are the real
  objects' frames at their real aspects from the record
  — the room being hung is this room. The 404's floor
  plan is §6.12's, reused: even being lost ends with
  the map.
- **Failure fallback.** The skeleton *is* a fallback
  state; its own failure is impossible (it is static
  print plus one optional gradient pass). The 404 works
  with every system dead — it is the watchdog's natural
  home.
- **Reduced-motion variant.** No beam-pass; skeleton
  frames static at ambient.
- **Performance budget & mobile variant.** Gradients and
  print only. Mobile: frames stack at their aspects; the
  404 plan uses §6.12's vertical variant.
- **Choreography timeline (v2).** Room requested → frames
  printed immediately (no blank night) → beam-pass at
  t=600ms, 3000ms, 5400ms → content lands → frames fill
  in place → beam resumes the round → timeout at 3000ms
  of *content* wait hands over to §6.14's hold language.
- **State matrix (v2).** *Rest:* as per state above.
  *Hover/focus:* retry (when present) is a §6.16-pattern
  text button. *Active:* standard. *Disabled:* n/a.
  *Touch:* identical.
- **Breakpoints (v2).** All sizes: layout mirrors the
  room it stands for (§4 measures), so a skeleton never
  promises a shape the room won't keep.
- **Edge cases & failure modes (v2).** *Partial load*
  (objects arrive, labels lag): frames fill, label cards
  stay ruled stock with their glow (§6.4) — a label that
  arrives late lights late, which the fiction already
  believes in. *Empty search (§6.17):* the log's empty
  line is this element's voice: "Nothing in the log
  under that name. The guard suggests the plan." + plan
  link.
- **Accessibility spec (v2).** Loading states carry
  `aria-busy` on the room and a visually hidden status;
  the 404's heading is a real `h1`. Nothing about an
  absence is conveyed by darkness alone — each state has
  its printed line.
- **Tokens consumed (v2).** `--night`, `--wall`,
  `--wall-lift`, `--ivory-dim`, `--brass`, `--ease-round`.

## 7. Page application map

**Home (the round itself).** The full sequence: hero title
catching light (§6.5), Rooms I–VII in order — counters
(§6.11) closing Room I, portraits (§6.3) in II, IV and V,
the frieze (§6.7) as Room III's whole wall, the masterpiece
pin (§6.8) in Room V, corridor spots (§6.9) between V and
VI, the night desk (§6.16) in VI, and Room VII as the
closing room (one quiet object, the plan, the door). The
footer floor plan (§6.12) signs the visit.

**Exhibition microsite.** One show, fewer rooms: the round
compresses to III–V rooms without breaking order or the
law; the masterpiece pin becomes the show's key work; the
desk books that show's night openings only.

**Collection / object detail.** The object at principal
scale in its room's dress: label (§6.4) with flip (§6.10),
related objects as a short corridor (spots optional), the
accession record printed in full, and the store state
(§6.15) if the object is held in the night store.

**Listing (the night store).** §6.15's room, reached from
the round or directly (direct arrivals get the room lit at
house-lights lift until their first scroll — a visitor who
came to buy is not made to walk for it).

**Search / index.** §6.17's log under house lights — the
round's fiction explicitly set aside for task speed, and
the doorway (§6.14) returns the visitor to the round at
the right room when a result is chosen.

**About / the museum's night programme.** The guard gets a
page: the round's history, the night programme's real
dates, membership — written in the institution's voice
(§12), with one portrait of the building at night and no
beam performance (the programme page is read by day, by
people planning; it wears the palette, not the patrol).

**Contact / membership.** §6.16's desk pattern reused —
ledger forms, stamped confirmations — in a lit room off
the round, linked from the members' door on the plan
(§6.12).

**404 / error.** §6.18's Room VIII, always, with the plan.

**Membership & patronage.** Patrons are the museum's
night people, and their page is Room VII's dress without
the round: the quiet object, the plan, and the desk form
(§6.16) re-pointed at membership tiers whose prices print
in the programme table's ledger format (§11). The one
addition the tier table earns is a column the day site
never has — *nights included* — because in this theme
membership is denominated in rounds walked, not discounts
taken. Patron names, where the museum prints them, are
set as a benefactors' wall: Marcellus, alphabetical, no
tier order — the night does not rank its friends.

**Education & study visits.** School and university
groups book the round as a study visit, and their page
breaks the fiction on purpose, in the open: it wears the
palette and the plaques but runs at house-lights lift
throughout, prints the learning objectives as a label set
(§6.4 stock, no flips — the guard's backs are not
curriculum), and gives teachers the floor plan (§6.12)
as a downloadable sheet. The break is declared in the
page's first label: "This room is lit. Groups learn
better with the lights up; the round itself is walked
after dark." A theme that cannot say where its fiction
stops will lie everywhere else too.

## 8. Worked examples

### 8.1 The hero — "Vermeer by Night" opens

The exhibition is real within the example: *Vermeer by
Night — nine paintings, one torch*, Rooms I–III of the
round borrowed for the show. **Build:** the hero room is
night at 88% wash; the title (Marcellus, 76px at desktop)
ships as one `h1` text node at ambient; the standfirst
reads "Nine paintings. One torch. The guard has walked
this round for eleven years — tonight, you walk it with
him." with the night-opening hours and the §6.16 booking
link beneath; the hero lantern (§6.6) hangs at the
standfirst's left; the first painting (the show's poster
work) hangs right of the reading column with its label
(§6.4) and accession line `I · 1632.041`. **Scroll
timeline:** t=0 arm, beam blooms 600ms → sweep catches
the title's 17 letters over ~1100ms → the painting's
label begins its glow at sweep-end + 500ms → plaques
glint at t=1800ms → the visitor scrolls: the beam widens
+6% with travel, hands the hero painting a last warm
residue, and walks to Room I's counters (§6.11), which
strike *9 objects on view · 214 frieze figures (the
permanent collection's, down the corridor) · 41 night
visitors booked · 11 years on the round* — every figure
traceable: nine paintings are on the page, 41 is the
booking record's real remaining-places sum for the
season's nights, 11 is in the standfirst's own sentence.

### 8.2 Mid-page — the Marble Boy (Room IV)

The object: a marble boy, accession `IV · 1908.007`, on a
plinth at the room's centre, lit by the parked beam; its
label (§6.4) at its right. **Build:** the boy's plate is a
photograph with fixed aspect (3:4) and a gilt-free stone
frame — marble gets no gilt; the frame rule is §9's
material honesty. The label front: name, "Roman, 2nd
century, after a Greek original", marble, the accession
line, and a condition line "Stable. Watched." The flip
(§6.10) back reads, in full: *"Reported moving between
shifts. It does not. — R., 02:40."* Beside the pair, at
half scale, hangs one of §6.3's portraits, whose gaze the
boy's presence explains: she watches the torch; the boy,
famously, does not move. **Scroll timeline:** doorway
dissolve (§6.14) from Room III's frieze → beam travels
1400ms, settles on the boy → label glow at +500ms → the
portrait's pupils drift to the light over 800ms → a blink
at her seeded offset → the visitor flips the label: 550ms
turn, the roommate rule irrelevant (one label in the
room) → scrolling on, the boy keeps the halo's residue;
the portrait's gaze returns to centre over 1200ms —
reluctantly (§6.3).

### 8.3 Conversion — booking the December round

At the night desk (Room VI), under the steadied lantern
(§6.6/§6.16): the visitor books 2 places for the round of
Friday 12 December. **Build:** the form (§6.16) offers
three real nights — 12 Dec (7 places left), 19 Dec (full —
printed, plaqued "Full", not selectable, because the book
does not hide its full nights), 9 Jan (12 left). Places
stepper 1–6; price line prints from the record: "£18 a
place · members £12" — and the total for 2 at member rate
is computed and printed in the summary as £24, the same
arithmetic the confirmation repeats. **Timeline:** focus
warms the first rule, lantern steadies → entries tick as
completed → a mistyped email earns the guard's error:
"The address won't reach you as written — check it
before I write it in the book." → corrected, submit →
lamp dips → confirmation entry fades up: *2 places ·
Fri 12 December · the round begins at 21:30 at the
members' door* → the stamp strikes at +500ms:
`ROUND · 12 DEC · № 07` → beneath, the one practical
line in the institution's voice: "Bring nothing bright.
The museum provides the dark." Every number on the page
— 7 left, £18, £24, № 07 as the seventh entry for that
night — traces to the booking record the example declares.

## 9. Anti-slop — what makes THIS theme look cheap

1. **The torch cursor.** The beam follows the pointer and
   the theme becomes a flashlight toy. *Cure:* the beam
   is scroll-driven, spring-carried (§6.1); the pointer
   is a normal cursor, always.
2. **Darkness as a hiding place.** Content at 20% opacity
   "revealed" by the beam — illegible, unlawful, and the
   exact defect this theme was once corrected for. *Cure:*
   the covenant (§2): everything passes contrast unlit;
   §10 tests with the beam parked elsewhere.
3. **Spooky kitsch.** Fog overlays, gothic fonts, a
   howling-wind audio toggle, "haunted museum" copy.
   *Cure:* the building is a workplace at night, not a
   ghost train; Marcellus and Source Serif, dry notes,
   one joke maximum per room (§12).
4. **Fake accession numbers.** `№ 001` sprinkled as
   decoration. *Cure:* every number traces to the record
   and the format is room + year + sequence (§3); the
   gate greps for orphans.
5. **Portraits that perform.** Pupils darting, constant
   blinking, heads turning. *Cure:* ±3px drift, seeded
   blinks, 0.4deg lean (§6.3) — unease is a dosage.
6. **Every room a pin.** Pinning everything because the
   masterpiece worked. *Cure:* exactly one pin (§6.8);
   the round's pace is walking, not a series of elevators.
7. **Labels as lorem.** Wall text that says nothing in
   museum language. *Cure:* labels carry name, maker,
   date, medium, accession and one true condition line;
   a label that could hang beside any object hangs beside
   none (§10 audit).
8. **Brass everywhere.** Gold gradients on buttons,
   headings, backgrounds. *Cure:* brass is metal and
   rationed — plaques, numerals, rules, the route (§2);
   under 6% of pixels, or it stops reading as metal.
9. **The beam as the only light logic.** Hover states,
   focus states and errors all waiting for the beam.
   *Cure:* focus and error states are instant and
   beam-independent (§6.4, §6.16) — the visitor's needs
   outrank the guard's schedule.
10. **A gift-shop grid in fancy dress.** §6.15 with
    badges, star ratings and "trending" sorts. *Cure:*
    the store is a store room: accession order, true
    states, no merchandising theatre.
11. **Watchdog theatre.** A "house lights" fallback that
    exists in the spec but was never wired. *Cure:* §10
    drills it — kill the beam script in testing and watch
    the lights come up inside 4000ms, or the build fails.
12. **Green creep.** The guard's green used for buttons
    and links because it was in the palette. *Cure:*
    green is a person, not a colourway (§2) — his notes,
    his route, his states, nothing else.

## 10. Quality gate

Blocking — all must pass before this theme ships:

- [ ] **Law drill 1 (nothing hidden):** with all theme JS
  deleted, every room reads complete and in order; no
  content's visibility depends on the beam.
- [ ] **Law drill 2 (house lights):** with the beam script
  broken at runtime, the watchdog raises house lights
  within 4000ms and the page is fully legible.
- [ ] **Covenant test:** body text in every room passes
  4.5:1 measured, with the beam parked in a different
  room; captions at 13px+ pass 4.5:1; no text role relies
  on the beam.
- [ ] **Beam audit:** the beam is scroll-driven only;
  pointer position appears nowhere in its inputs; normal
  system cursor everywhere.
- [ ] **Number audit:** every counter, price and accession
  number traces to the declared record; §6.11's figures
  match the DOM content they claim to count.
- [ ] **Label audit:** every object has a label; every
  label flips; every back is object-specific (no back
  text repeats across two objects).
- [ ] **Flicker audit:** corridor spots (§6.9) within the
  step/rate caps; no synchronised flashing anywhere.
- [ ] **Ambient census:** exactly three licensed ambient
  loops (§5) running; everything else still.
- [ ] **Pin census:** exactly one pinned section (§6.8).
- [ ] **Reduced-motion pass:** the whole round walked
  under `prefers-reduced-motion` — lit, complete, still.
- [ ] **Performance:** §14 budgets met on a mid-tier
  phone; the shared loop holds 60fps with beam + dust +
  lanterns live.
- [ ] **Focus walk:** keyboard-only round completed;
  focus glides the beam (§6.1), labels flip by keyboard,
  the form (§6.16) submits, focus never strands.

## 11. Component inventory

Every component a real museum site in this theme needs,
with its treatment — or its refusal, with the in-theme
replacement. Treatments inherit §2–§5 unless stated.

- **Buttons.** Primary: ivory text on `--wall-lift` with a
  brass rule beneath that thickens on hover — never a
  filled gold button (§9.8). Secondary: ivory text, hairline
  wall-lift border. The desk's submit is §6.16's pattern.
- **Inputs / textarea / select.** Ledger lines (§6.16):
  ruled bottom border, brass on focus, ticks on validity,
  guard-voiced errors. Selects are native, styled to the
  rule — the book does not fake a dropdown.
- **Labels & help text.** Real `<label>`s above the rule;
  help text in caption size, ivory-faint, in the
  institution's voice.
- **Checkboxes / radios.** Small brass squares/rings drawn
  in CSS, tick in ivory; used for membership options at
  the desk (member / non-member rate) and nowhere frivolous.
- **Tables.** The night programme table (dates, places
  left, price) set as a ledger: ruled rows, tabular
  numerals, full nights printed and plaqued (§8.3) — never
  hidden or greyed into illegibility.
- **Cards.** §6.15's object cards are the only card species.
- **Badges / plaques.** State plaques (On reserve / Out on
  loan / Full): brass-bordered chips, ivory text — state as
  furniture, never coloured dots.
- **Alerts.** A notice from the building (a room closed for
  conservation) prints as a wall notice: wall stock, ivory
  text, alarm rule only if it affects tonight's round.
- **Modal.** Refused. A museum at night does not interrupt;
  the label flip (§6.10) and the doorway (§6.14) carry
  everything a modal would. Genuinely blocking choices
  (none known) go to a lit page of their own.
- **Toast.** Refused. Confirmations are stamped into the
  book (§6.16) or printed as wall notices; nothing in this
  building pops up and vanishes.
- **Tabs.** Refused inside rooms. The one tab-like act —
  the masterpiece's three labels (§6.8) — is scroll-called,
  not tabbed; elsewhere, content is sequenced by the round.
- **Accordion.** The programme page's questions (what to
  bring, where to meet) use a printed list with details/
  summary in ledger dress — the only accordion, and it is
  honest HTML, styled, with the guard's answers (§12).
- **Pagination.** Refused in the store (§6.15 is one room);
  the log (§6.17) prints its full index. A collection too
  big for one room belongs in the day site's database (§1).
- **Breadcrumbs.** The plaques (§6.13) are the breadcrumbs;
  object pages add their room plaque lit. No second system.
- **Progress.** The torch-line (§4) is the only indicator.
- **Spinner / loader.** Refused; the house-lights hold
  (§6.14) and the unlit room (§6.18) are the loading states.
- **Skeleton.** §6.18's frames on the wall.
- **Tooltip.** Refused. Anything worth saying is a label;
  labels flip (§6.10).
- **Search.** §6.17's log.
- **Forms.** §6.16's ledger pattern, reused for membership
  and contact (§7).
- **Footer.** §6.12's floor plan.
- **Navigation.** §6.13's plaques.
- **Hero.** §6.5's title room pattern.
- **404 / empty / error.** §6.18's Room VIII and unlit room.

## 12. Content & copywriting voice

Two registers, and the visitor should feel the seam.
**The Institution** (Marcellus's partner voice: labels,
hours, prices, programme) writes in calm, complete
sentences with museum nouns — object, gallery, bequest,
on loan — and never exclaims. **The Guard** (italic, §3)
writes the backs, the errors, the empty states: short,
dry, first-person-plural-free, a man who has seen the
collection ten thousand times and loves exactly some of
it. His humour is rationed to one line per room and is
always at the building's expense, never the visitor's.

- **Headlines:** the exhibition's true name, nothing
  added. ✓ "Vermeer by Night" ✗ "Step Into a World of
  Nocturnal Wonder!"
- **Labels:** name, maker, date, medium, one true line.
  ✓ "Stable. Watched." ✗ "A fascinating piece with a
  rich history."
- **Errors (the guard, kind and specific):** ✓ "The
  address won't reach you as written — check it before
  I write it in the book." ✗ "Invalid email format."
- **Empty states:** ✓ "Nothing in the log under that
  name. The guard suggests the plan." ✗ "No results
  found 😢" (no emoji anywhere in the building).
- **Buttons:** verbs from the desk. ✓ "Enter it in the
  book." / "Book the round" ✗ "Submit" / "Get Started!"
- **Fixed strings (verbatim, never paraphrased):** the
  Marble Boy's back — *"Reported moving between shifts.
  It does not."*; the corridor label's line — "The
  corridor lights are being replaced in spring. Until
  then, they rehearse."; the confirmation's closing line
  — "Bring nothing bright. The museum provides the dark."
- **Numbers:** always real, always tabular, always
  traceable (§6.11's audit). A voice rule as much as a
  data rule: the institution does not round its years on
  the round.

## 13. Full-page scroll choreography map

The round, beat by beat, top to footer:

1. **The door (hero).** Beam blooms (600ms) → title
   catches letter by letter (§6.5) → hero painting's
   label glows at +500ms after the sweep → plaques glint
   → lantern swaying. *Feels like: being let in.*
2. **Room I — the vitals.** Beam walks in; counters
   strike (§6.11) after the first label's glow begins.
   *Feels like: the guard checking his board.*
3. **Room II — first portrait.** Pupils drift to the
   light (§6.3); a blink lands mid-look. *Feels like:
   being noticed.*
4. **Room III — the frieze.** Doorway dissolve → the
   300vh scrub (§6.7): glow leads, figures warm, captions
   change hands. *Feels like: walking a wall that is
   walking with you.*
5. **Room IV — the Marble Boy.** Beam parks; label
   glows; the visitor flips it (§6.10) and reads the
   joke standing in the light. *Feels like: trespass,
   permitted.*
6. **Room V — the masterpiece.** The pin (§6.8): three
   labels, three ways of knowing, the beam staying
   longer than anywhere. *Feels like: the guard's
   favourite stop.*
7. **The corridor.** Spots rehearse and settle (§6.9);
   works on paper warm one by one. *Feels like: the
   building's age, admitted.*
8. **Room VI — the night desk.** Lantern steadies; the
   form (§6.16) is written in; the stamp strikes.
   *Feels like: business, conducted properly.*
9. **Room VII — the quiet room & the plan.** One object,
   fully lit by a parked beam; then the footer plan
   draws the route home (§6.12) and the door flashes.
   *Feels like: clocking out, souvenir in hand.*
**Reverse pass:** the guard walks back — residue warms at
half depth, labels do not re-perform, counters stay
struck, spots come on clean. **Jump scroll:** anchors
glide (§6.13) with the beam leading; a scrollbar drag to
the footer lands the visitor with the plan drawn and the
intervening rooms' states settled silently — the round
never punishes a visitor for arriving out of order.

## 14. Whole-page performance budget

- **Total page weight:** ≤900KB initial (hero room +
  system), rooms' plates lazy within 200vh of approach.
  The frieze track is the single largest asset: ≤220KB
  desktop, ≤110KB mobile variant.
- **Frame budget:** the shared loop (beam spring, halo,
  dust ≤44 points, two lanterns, pupil offsets, counters)
  must hold ≤1.8ms/frame of JS on a mid-tier phone;
  gradients and transforms are compositor work and are
  capped at 4 simultaneous animated layers per viewport.
- **Long tasks:** none over 50ms after first paint; the
  anchor read (§6.1) is one layout pass, cached, re-run
  only on resize (debounced 200ms).
- **Fonts:** Marcellus (1 weight) + Source Serif 4 (2
  weights + italic) subset, ≤120KB total, `font-display:
  swap` — a title that catches light must not wait for
  its typeface to begin.
- **Cut order when over budget:** (1) dust count 44→18;
  (2) halo layer; (3) lantern wobble layer; (4) frieze
  track resolution; (5) plaque glint stagger. **Never
  cut:** the watchdog, the ambient lift (the covenant is
  a budget line, not a garnish), label text, or the
  accession numbers.

**Asset-by-asset budget.** The 900KB ceiling is not a
mood; it is allocated, and the allocation is audited:

| Asset | Budget | Notes |
|---|---|---|
| HTML + CSS + JS (the whole system) | ≤180KB gz | One loop, no framework, no icon font |
| Fonts (Marcellus + Source Serif 4 subsets) | ≤120KB | §14 above; italic included — the guard's voice is not optional |
| Hero painting plate | ≤140KB | The one image allowed to be rich; AVIF first |
| Frieze track | ≤220KB / ≤110KB mobile | §6.7; a 12-metre object earns its bytes |
| Portraits (3) + masterpiece + details (2) | ≤60KB each | Fixed aspects declared; no layout shift |
| Store plates (§6.15) | ≤45KB each, lazy | Below-fold only |
| SVGs (lanterns ×2, spots ×4, floor plan, stamp) | ≤24KB total | Inline; the plan is the largest at ≤9KB |
| Beam / halo / doorway gradients | 0KB | Pure CSS — light is free or it is wrong |

**The second night — returning visitors.** The theme
keeps three session facts and no more: the intro has been
walked (`mad-intro`, §6.5), the route has been drawn
(§6.12), and the corridor spots have rehearsed (§6.9).
A returning visitor within the session gets the museum
already awake: title lit, route printed, spots clean.
Across sessions, nothing is remembered — the museum does
not track its visitors, and a theme whose fiction is a
man walking alone at night must not grow a surveillance
habit in its storage. One exception, and it is the
visitor's own act: a flipped label (§6.10) is *not*
remembered either. The guard tidies the rooms between
nights; every visit begins with every label official-side
up, and the trespass is fresh each time. That restraint
is a feature to defend in review: the first stakeholder
request to "remember their place in the round" is
refused with this paragraph.

**Print.** The round prints as the lit museum: wash and
beam removed, labels front-side with their backs printed
beneath (§6.10's no-JS layout), the floor plan drawn,
counters at final values. A printed visit is a legitimate
souvenir and the stylesheet is a build deliverable, not
an afterthought — the gate (§10) includes one printed
walk of the home page checked for orphaned labels and
cut accession lines.

## 15. Build-order checklist

1. Print the lit museum first: all rooms, labels, forms
   and the plan as static HTML at house-lights lift —
   the page the law requires to exist underneath.
2. Apply the palette and type (§2–§3); run the covenant
   contrast measurements on the static page.
3. Hang the plaques (§6.13) and torch-line; wire anchors.
4. Build the darkness overlay and beam (§6.1) with the
   4000ms watchdog — and drill the watchdog before
   anything else is allowed to depend on the beam.
5. Key the label glows (§6.4) and counters (§6.11) to
   beam arrival.
6. The entrance: bloom + title catch (§6.5), session flag.
7. Portraits (§6.3) and lanterns (§6.6) — the life layer.
8. The frieze scrub (§6.7), then the masterpiece pin
   (§6.8), then corridor spots (§6.9) with the flicker
   caps verified.
9. Label flips (§6.10) with the roommate rule.
10. Doorways (§6.14); the store (§6.15); the log (§6.17).
11. The desk form (§6.16) end-to-end against the real
    booking endpoint, including the sold-out-while-writing
    path.
12. The footer plan draw (§6.12); Room VIII and the
    unlit room (§6.18).
13. Reduced-motion pass over everything; forced-colors
    pass; house-lights toggle wired.
14. Run §10's gate — both law drills first.
15. Gate signed by a non-builder who walked the round
    keyboard-only, in the dark, and then with the lights
    up.

**A last word on temperament.** Every system in this
theme — the spring in the beam, the rationed warmth, the
one-cause loop, the watchdog with its hand on the house
lights — exists to protect a single feeling: that the
visitor is being *accompanied*, competently and quietly,
through a building that is loved by the person who locks
it. Builds that keep every number in this expansion and
lose that feeling have failed in the way §9 cannot
enumerate. The final test is not in the gate: it is a
fresh visitor, at midnight, saying *someone works here
who cares* — and being right.
