# Example 1 — A global fade-up becomes selective, purposeful motion

## Before

```html
<section data-aos="fade-up" data-aos-duration="800">…hero…</section>
<section data-aos="fade-up" data-aos-duration="800">…features…</section>
<section data-aos="fade-up" data-aos-duration="800">…story…</section>
<section data-aos="fade-up" data-aos-duration="800">…pricing…</section>
<!-- …10 more sections, identical attributes… -->
```

Every section fades in and rises by the same distance over the same
800ms as it enters the viewport — one library default applied globally
(DET-VIS-040). Nothing about any individual arrival carries information;
the motion is wallpaper, and content is briefly invisible on every
scroll.

## After

```css
/* Sections render in their end state by default. No entrance animation. */
section { opacity: 1; transform: none; }
```

Two animations survive, each with a named purpose:

1. **Continuity** — when a dispatch board re-sequences after a change,
   cards animate (`transform` only, `--duration-move` token) from their
   old positions to their new ones, so the dispatcher sees *what moved*
   instead of a silently different list.
2. **Feedback** — the "Route saved" confirmation check draws itself in
   over `--duration-feedback` as the save resolves, then is still.

Everything else is simply present. Scrolling the page is now calm, the
content never waits on an effect, and the two remaining animations each
answer "what changed?" — the only question motion is for.

Note: corrects FE-084 — there is no global entrance animation; animation is reserved for arrivals that carry information.
