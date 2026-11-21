# D13 Accessibility & i18n — End-to-End Example

## Scenario

"NoteNest," a small note-taking SaaS, ships its checkout page in English and then
adds an Urdu locale. The target is recorded before build: WCAG 2.2 Level AA, with
the Urdu build fully RTL. The first AI-built version looks polished in a screenshot
and fails both a keyboard user and an Urdu reader in the first minute.

## Before — the slop version

```html
<style>
  *:focus { outline: none; }              /* outlines "looked messy" */
  .summary { margin-left: auto; left: 0; }
  [dir="rtl"] .page { transform: scaleX(-1); }   /* "RTL support" */
</style>

<form class="page">
  <div class="summary">Order summary</div>
  <input type="text" placeholder="Card number">
  <input type="text" placeholder="Expiry">
  <div class="pay-btn" onclick="pay()">Pay now</div>
  <p class="error" style="color:red"></p>   <!-- error = red text only -->
</form>
```

What is wrong, visibly: fields are labeled only by placeholders that vanish on
input; the focus outline is removed globally; the primary action is a clickable
`<div>` no keyboard can reach; an error is conveyed by color alone; and "RTL" is a
mirror transform that flips the layout visually while text, focus order, and logos
break underneath it.

## What the skills caught

- **BAN-AC-013 — Placeholder as the only label** (defeats DET-UX-022). **AC-028**:
  every field gets a persistent, programmatically associated visible `<label>`; a
  placeholder may show a format example only.
- **BAN-AC-011 / BAN-AC-042 — Focus outline removed for looks** (defeats
  DET-UX-018). **AC-024 / AC-085**: every interactive element shows a visible focus
  indicator; a sticky header must never fully obscure the focused element (2.4.11).
- **BAN-AC-043 — Pointer-only control** (defeats DET-UX-001). The `<div onclick>`
  pay action is dead for keyboard users. **AC-081 / AC-082**: native interactive
  elements first; everything operable by pointer is operable by keyboard alone.
- **BAN-AC-012 — Color-only state** (defeats DET-UX-021). **AC-023**: every color
  signal is paired with a redundant cue — an icon plus text naming the problem — so
  the form still reads correctly in grayscale.
- **BAN-AC-081 — Physical directional CSS** (defeats DET-UX-023). `margin-left` and
  `left: 0` do not mirror. **AC-162**: layout uses CSS logical properties only, so
  one stylesheet serves both directions.
- **BAN-AC-082 — Mirroring faked with transforms** (defeats DET-VIS-037).
  **AC-161**: direction is declared with `dir="rtl"` on the root and built on
  logical properties; content, focus order, and reading order follow it.
- **AC-171** for the Urdu build specifically: RTL QA is per script with real text —
  Arabic passing does not certify Nastaliq, whose taller line boxes need their own
  line-height and clipping checks (BAN-AC-085).

## After — the corrected version

```html
<html lang="ur" dir="rtl">   <!-- direction from locale metadata (AC-161) -->
<style>
  .summary { margin-inline-start: auto; inset-inline-start: 0; }
  :focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; }
  .field-error { /* icon + text, never color alone (AC-023) */ }
</style>

<form>
  <div class="summary">آرڈر کا خلاصہ</div>

  <label for="card">کارڈ نمبر</label>
  <input id="card" type="text" inputmode="numeric" autocomplete="cc-number"
         placeholder="4242 4242 4242 4242" aria-describedby="card-err">
  <p class="field-error" id="card-err" role="alert" hidden>
    ⚠ کارڈ نمبر نامکمل ہے — 16 ہندسے درج کریں۔
  </p>

  <label for="expiry">اختتامی تاریخ</label>
  <input id="expiry" type="text" autocomplete="cc-exp" placeholder="MM / YY">

  <button type="submit">ادائیگی کریں</button>   <!-- native, keyboard-operable -->
</form>
```

(The card number above is the payment provider's published test number, shown as a
format example in the placeholder — the field's real label is the persistent
`<label>`.) Embedded Latin runs — product names, prices, codes — are isolated with
`<bdi>` so the bidi algorithm orders them correctly inside Urdu sentences (AC-166),
code and URLs stay `dir="ltr"` (AC-167), and dates render through
`Intl.DateTimeFormat` for the locale instead of string manipulation (AC-170).
Conformance is claimed per criterion, per full page — never as a blanket
"accessible" statement (AC-032).

## Skills used

- [wcag](../skills/accessibility-i18n/wcag/SKILL.md)
- [keyboard-accessibility](../skills/accessibility-i18n/keyboard-accessibility/SKILL.md)
- [rtl-layouts](../skills/accessibility-i18n/rtl-layouts/SKILL.md)
- [internationalization](../skills/accessibility-i18n/internationalization/SKILL.md)
- [screen-readers](../skills/accessibility-i18n/screen-readers/SKILL.md)
