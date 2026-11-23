# Theme Library — Expansion Standard (20x depth, highest quality)

Ordered by MUHIUM, 2026-11-23: the theme library and UI/UX skills felt too
small and too thin. Every theme expands to roughly **20x its current detail**.
Quantity NEVER reduces quality: no filler, no repeated boilerplate, no generic
text that could belong to any theme. Premiumness is the point — when a theme
feels premium enough, push it one level further.

## Per-theme required structure (in this order)

1. **Concept & world** — the theme's story and mood; best-fit sites and
   audiences; when NOT to use it.
2. **Palette** — full token table: hex, role, usage ratio, pairing and
   contrast notes, dark-mode behaviour.
3. **Typography** — fonts, the full type scale, per-role rules (display,
   heading, body, caption, data), line-height and tracking specifics.
4. **Layout language** — grid, spacing rhythm, section choreography, density
   rules, how whitespace is used as a design material.
5. **Full motion system** — every motion term applied in this theme's own
   language, each with duration, easing and trigger: scroll-triggered reveals,
   parallax layers, pinned scenes, masked line reveals, blur-to-sharp reveals,
   animated counters, progress indicators, marquees, ambient loops,
   micro-interactions, hover physics, page transitions, image treatments.
6. **Signature elements** — the theme's own 8–12 elements PLUS page-family
   elements (navigation, hero, cards, forms, footer, loader/transition).
   EACH element gets a full build spec:
   - what it is and why it belongs to this theme
   - structure (DOM/canvas/SVG approach)
   - motion spec: exact durations, named easings, trigger points
   - states (rest, hover, active, scrolled-past)
   - how it merges with the site's content (never pasted-on decoration)
   - failure fallback (content fully visible if the animation never runs)
   - reduced-motion variant
   - performance budget and the cheaper mobile variant
7. **Page application map** — how the theme plays out across page types
   (home, listing, detail, about, contact/checkout equivalents).
8. **Worked example** — one complete section described end-to-end, as it
   would actually be built.
9. **Anti-slop** — what makes THIS theme look cheap, and the cure for each.
10. **Quality gate** — a checklist for this theme, with a minimum bar that
    must pass before the theme may be used in a build.

## Standing rules (never break)

- Normal system cursor only; no heavy cursor effects.
- No reveal may ever leave content invisible; every animation has a fallback;
  the page stays readable with JavaScript disabled.
- `prefers-reduced-motion` is honoured with a real variant per element.
- Scroll-driven motion is smoothed (requestAnimationFrame lerp); animated
  objects never cover the content they belong to.
- Elements merge with content — they carry the content, they are not
  decoration pasted on top of it.
- Every element states a performance budget; heavy effects ship with a
  cheaper mobile variant.

## Deepening pass — the 50x standard (v2, ordered 2026-11-23)

MUHIUM's ruling after reading the first expanded themes: good, but not yet
what they must be. The expansion goes to **50x — in detail, not just in word
count**. Every theme that has passed the standard above gets a deepening pass
adding ALL of these layers. New themes are written directly to v1 + v2.

**Per element, add:**
- A millisecond choreography timeline — beat by beat, what moves when, in
  what order, relative to the trigger.
- A full state matrix: rest / hover / focus / active / scrolled-past /
  disabled, on desktop and on touch — no state left undesigned.
- Breakpoint behaviour at ≥1200px, 768–1199px, and <768px — layout, motion
  intensity, and what is cut or simplified at each size.
- Edge cases and failure modes: slow network, no canvas/WebGL, low-power
  device, content longer or shorter than the design expects, user scrolling
  back up.
- An accessibility spec for the element: focus order and visible focus,
  aria/labelling, contrast at every state, touch target sizes.
- The exact design tokens (CSS variable names) the element consumes, so two
  builders produce the same element.

**Per theme, add:**
- A complete component inventory — every UI component a real site in this
  theme needs (buttons, inputs, tables, badges, alerts, pagination, modals,
  toasts, tabs, accordions…), each with its themed treatment.
- Content and copywriting voice rules for the theme: headline style, label
  style, error-message voice, empty-state voice — with examples.
- Three worked examples end-to-end: the hero, one mid-page section, and one
  conversion section (form/checkout/signup), each with its scroll timeline.
- A full-page scroll choreography map: every motion beat from the top of the
  page to the footer, in order, with what the visitor sees and feels.
- A whole-page performance budget: asset weight, animation frame budget,
  long-task limits, and what gets cut first when the budget is exceeded.
- A build-order checklist: the sequence in which the theme is implemented.

Depth is measured by these layers being complete and specific — never by
raw word count, and never by padding.

## Anti-filler law

- If a sentence could appear in any other theme unchanged, delete it or make
  it specific to this theme.
- Numbers beat adjectives: durations in ms, easings named, ratios stated,
  sizes in px/rem.
- Repetition across themes = failed expansion. Each theme's expansion is
  written from that theme's own world, not from a template with names swapped.
