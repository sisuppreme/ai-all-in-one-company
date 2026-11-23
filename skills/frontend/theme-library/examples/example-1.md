# Example 1 — Theme #71 The Bioluminescent Census, built from the canonical spec

Corrects rules **FE-341** (build from the canonical expanded spec) and **FE-343** (the theme's one law governs).

## Before

A marine research institute's annual census page is built as a generic dark dashboard: a chart library renders the counts as bars and pies, a particle-rain canvas runs behind the hero because "it looks alive", and the headline number — 61,408 organisms — is typed into three components by hand, one of which says 61,480. Nothing on the page comes from a theme; the particles glow in colours no species owns, and the charts could belong to any analytics product.

## After

The build opens `expanded/theme-071.md` and follows it. The theme's one law — *nothing glows that is not counted* — governs every element: the swarm is 160 simulated organisms whose tint allocation is the census record's own species split, the hero figure aggregates to exactly 61,408 because the record's species counts sum to it, and the single red light on the page is the predator the sheet logs, appearing as the spec's §6.10 pass. The printed figure in bone text is the authority everywhere; the bloom is its portrait. Charts are gone — the population performs the statistics it counts. Gate G-FE-172 re-derives every printed total from the §6.17 record before the page ships.
