# Example 2 — A mixed icon drawer becomes one icon set

## Before

Icons on one settings page, as shipped:

- A gear drawn from an outline set at 1.5px stroke.
- A filled duotone bell from a second set.
- A rounded, chunky trash can from a third set.
- "🚀" emoji as the icon for the "Performance" row.
- A hand-pasted SVG of a shield with no viewBox alignment to the grid.

Five visual languages in one list (DET-VIS-025), plus emoji standing in
for an icon (DET-VIS-016). Each was grabbed from wherever the generator
found one.

## After

One set, one stroke, one grid — the library's outline set at 24px viewBox,
1.8px stroke, round caps:

```html
<!-- All icons: <svg> from icons/ (single set), sized via the icon
     component so stroke and grid cannot drift per usage. -->
<Icon name="settings" />   <!-- gear, outline set -->
<Icon name="bell" />       <!-- notifications, outline set -->
<Icon name="trash" />      <!-- delete, outline set -->
<Icon name="gauge" />      <!-- performance, outline set — replaces 🚀 -->
<Icon name="shield" />     <!-- security, outline set -->
```

The emoji is gone, the shield is redrawn into the set, and the grep gate
(G-FE-033) fails any future import from outside `icons/`. A genuinely new
metaphor is added to the set as a system change, drawn to the same grid —
never pasted in from a second library.

Note: corrects FE-064 — one icon set, one stroke weight, one metaphor style across the whole library.
