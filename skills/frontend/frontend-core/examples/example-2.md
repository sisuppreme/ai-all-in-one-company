# Example 2 — An unsized hero image becomes layout-stable

## Before

```html
<img src="/hero.jpg" alt="Dispatch board with today's routes">
```

```css
.hero img { width: 100%; height: auto; }
```

No dimensions are reserved. On a slow connection the hero text renders,
the user starts reading, and the arriving image pushes everything down by
600px — a layout shift that blows the CLS budget and loses the reader's
place.

## After

```html
<img src="/hero.jpg" width="1600" height="1000"
     alt="Dispatch board with today's routes">
```

```css
.hero img { width: 100%; height: auto; aspect-ratio: 8 / 5; }
```

The browser computes the box from the intrinsic ratio before the file
loads, so the space is reserved and nothing moves when the image arrives.
The same pattern applies to every content image and embedded video on the
page; the CLS assertion in CI (G-FE-001) verifies the result stays
≤ 0.1.

Note: corrects FE-003 — every image and video ships with reserved dimensions so layout is stable while assets load.
