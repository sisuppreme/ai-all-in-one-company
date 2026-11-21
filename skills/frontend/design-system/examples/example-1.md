# Example 1 — Uniform sections recomposed by role

## Before

Render spec of a product page, top to bottom — every section identical in
structure:

| Section | Padding | Alignment | Loudest element |
|---|---|---|---|
| Hero | 96px / 96px | centered | heading |
| Features | 96px / 96px | centered | heading |
| Story | 96px / 96px | centered | heading |
| Pricing | 96px / 96px | centered | heading |
| FAQ | 96px / 96px | centered | heading |

Five roles, one template. DET-VIS-001 (uniform padding), DET-VIS-002
(centered everything), and DET-VIS-010 (heading always loudest) hit
together — a cluster, scored as a major.

## After

The same content, composed per role:

| Section | Padding | Alignment | Loudest element |
|---|---|---|---|
| Hero | 64px / 48px | left, product shot right | product screenshot |
| Features | 80px / 80px | left | the featured feature's demo |
| Story | 48px / 48px | narrow column, offset | the founder's quote, set large |
| Pricing | 80px / 64px | centered (comparison reads best centered) | the price figures |
| FAQ | 64px / 96px | narrow column, left | the questions themselves |

Padding now paces the page: tight where content is dense, wide before the
close. Proof elements (screenshot, quote, prices) outrank their headings
twice. Centering survives only where the content role earns it.

Note: corrects FE-025 — section composition follows content role; identical padding, alignment, and loudest element across sections fails system review.
