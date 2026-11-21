# Example 3 — Drag-only reordering vs. single-pointer alternative

## Before

A dashboard's card list can be reordered only by dragging: press, hold, and move along a path to the new position. A user with a tremor, a switch device, or a head pointer cannot sustain the press-and-move gesture, so a core feature of the page is simply unavailable to them (fails 2.5.7 Dragging Movements).

## After

Each card gains "Move up" and "Move down" buttons beside the drag handle — a single-pointer alternative requiring only simple clicks, no path-based movement. The buttons are sized to the 24×24 CSS px floor (AC-025) and are keyboard-operable in the same order as the visual list. Dragging remains for those who prefer it; it is no longer the only way.

*Demonstrates AC-029 — every dragging movement has a single-pointer alternative.*
