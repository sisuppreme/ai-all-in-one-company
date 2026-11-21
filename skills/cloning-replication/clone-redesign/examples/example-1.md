# Example 1 — The hue-shifted token file

Scenario: an authorized competitor rebuild (clone-ethics record on file,
LG-182(d) ground, CL-141) of a reference invoicing app. Function parity is
owed for invoice creation, tax calculation, and overdue reminders. The
expression — tokens, type, brand — must be original.

## Before

Design-extraction had already run on the reference, producing a token file
and a CL-051 replace-list. The builder used that file as the starting point
for the redesign's `tokens.json`:

```json
{
  "color.primary":      { "$value": "#2050d9" },
  "color.primary-dark": { "$value": "#1a3fae" },
  "color.surface":      { "$value": "#f6f7fb" },
  "font.family":        { "$value": ["Inter", "system-ui", "sans-serif"] },
  "space.scale":        { "$value": [4, 8, 12, 16, 24, 32, 48] },
  "radius.card":        { "$value": 12 },
  "breakpoint.tablet":  { "$value": 768 }
}
```

Review notes attached to the commit: "Primary shifted from the sampled
`#1f4fd8` to `#2050d9` so it isn't a copy. Spacing and radius kept as-is —
they're just numbers. Font stack kept; Inter is everywhere anyway."

This is BAN-CL-071 in its textbook form: extracted values reused exactly
(spacing scale, radius, breakpoint, font stack), rounded, or hue-shifted by
one step (primary, primary-dark, surface). It violates CL-144 — the
extraction output was a negative reference and replace-list, never a value
source — and CL-146, because no original design record was authored; the
token file was derived, not created. G-CL-072 would fail it: the primary
sits within one hex step per channel of an extracted color, and the
spacing/radius/breakpoint collisions have no CL-145 functional-necessity
entry in the divergence log (a spacing scale is not dictated by function).

## After

The derived file is deleted. Before any page is built, the project commits
an original design record under CL-146: a new product name and wordmark
created for this rebuild, an imagery direction (flat illustration, no
photography), and a fresh DTCG token file authored from the brand brief —
with the extraction file consulted only as the list of values to avoid:

```json
{
  "color.primary":      { "$value": "#0e6b5c" },
  "color.primary-dark": { "$value": "#084f43" },
  "color.accent":       { "$value": "#c96a1e" },
  "color.surface":      { "$value": "#fdf9f2" },
  "font.family":        { "$value": ["Source Serif 4", "Georgia", "serif"] },
  "font.family-ui":     { "$value": ["Public Sans", "system-ui", "sans-serif"] },
  "space.scale":        { "$value": [5, 10, 15, 25, 40, 65] },
  "radius.card":        { "$value": 4 },
  "radius.control":     { "$value": 2 },
  "breakpoint.tablet":  { "$value": 820 }
}
```

Typefaces are recorded in the design record with license status (both
OFL-licensed). The divergence log (CL-152) records one deliberate
non-difference: amounts are still rendered in a tabular numeric format and
the legally required tax-invoice label keeps its statutory wording — both
entered as CL-145 functional-necessity exceptions, not as token collisions.

G-CL-072 is then run against the extracted set: zero colors within one hex
step per channel, zero identical spacing/radius/breakpoint values outside
the logged CL-145 entries, and no extracted font stack present. It passes,
and the pass is recorded in progress.md before the first page build starts.

## Note

Violates/corrects CL-144, CL-146, and BAN-CL-071. The fix is not a bigger
hue shift — G-CL-072 failures are re-authored, not nudged. The extraction
file did its job in both versions: in the Before as a palette (banned), in
the After as a map of what to avoid (its only permitted use).
