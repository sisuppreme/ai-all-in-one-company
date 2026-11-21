# Example 2 — Gradient headline and straight quotes finished properly

## Before

```html
<h1 class="hero-title">Billing that "just works" - finally</h1>
```

```css
.hero-title {
  background: linear-gradient(90deg, #7c3aed, #2563eb);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
```

The headline's emphasis is a purple-to-blue gradient — the default generated
look — and the prose inside it uses typewriter quotes and a hyphen where a
dash belongs.

## After

```html
<h1 class="hero-title">Billing that “just works” — finally</h1>
```

```css
.hero-title {
  font: var(--type-display);
  font-weight: 700;
  color: var(--color-text-strong);
}
.hero-title em {
  font-style: italic;
  color: var(--color-accent);
}
```

Emphasis now comes from weight, scale, and one solid accent on the key phrase,
and the sentence itself is finished: real quotation marks and an em dash.

Note: corrects FE-145 and FE-144 — emphasis is solid, never a gradient clip; micro-typography (quotes, dashes) is finished work.
