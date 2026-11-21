# Example 2 — Focus buried under a sticky header vs. visible, unobscured focus

## Before

A page ships with a global reset (`*:focus { outline: none; }`) and a 72px sticky header. A keyboard user tabs through the page: there is no indicator to follow, and when focus reaches the first link below the header, the browser scrolls it to the very top of the viewport — directly underneath the sticky header, fully hidden. The user is tabbing blind (fails 2.4.7 and 2.4.11).

## After

The reset is removed and replaced with a designed `:focus-visible` indicator drawn from the mapped focus token. The page sets `scroll-margin-top: 88px` on focusable content (header height plus clearance), so a scrolled-to focused element always lands fully below the sticky header. The G-AC-013 spot check confirms, at every Tab stop, that the indicator is visible and the focused element is not entirely obscured by the header, cookie banner, or chat widget.

*Demonstrates AC-024 — focus is visible and never fully hidden by author-created content.*
