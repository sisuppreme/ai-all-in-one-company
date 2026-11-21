# Example 2 — A gradient signature replaced by a brand system

## Before

The "design system" for a route-planning tool, in full:

- Logo: a rounded square.
- Color: `linear-gradient(135deg, #7c3aed, #2563eb)` — used on the hero
  background, both buttons, the headline (clipped into the text), and
  every card border.
- Font: Inter, default weights.
- Everything else: framework defaults.

This is the purple-blue gradient signature (DET-VIS-017) plus gradient
headline text (DET-VIS-018) plus a default font pairing (DET-VIS-011) —
the template's identity, not the product's.

## After

The design brief names the divergence first: the product is about roads,
paper maps, and high-visibility signage. The system built from it:

- **Palette (tokens):** ink `#1c2430` (text/surfaces), paper `#f7f3ea`
  (background), signal amber `#e8a33d` (primary action — the color of
  road signage), route blue `#2f5da3` (secondary, used sparingly for
  map features), plus semantic success/warning/error. No gradients in
  the core system; the one permitted gradient is a topographic contour
  pattern drawn from an actual map of the service area.
- **Type:** a condensed grotesque for display headings (signage feel), a
  neutral text face for UI; tabular numerals for distances and times.
- **Device:** route-line motifs — a thin amber line that literally
  connects steps in onboarding and pricing, drawn from the product's own
  core visual.

The gradient is gone; what replaced it could not be mistaken for another
product's site.

Note: corrects FE-029 — distinctiveness is briefed before building; a brief that could describe any SaaS site is rejected.
