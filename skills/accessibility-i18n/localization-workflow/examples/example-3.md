# Example 3 — Silent fallback behind a "fully supported" locale claim

## Before

The Arabic locale launches with the storefront, product pages, and checkout translated. The returns flow was never sent for translation. In production, the missing keys quietly fall back to English: a user who has shopped entirely in Arabic reaches the returns screens and finds them in English, with no indication that the content is untranslated or that a translation is missing. The help page lists Arabic as a fully supported language, and the TMS dashboard shows the locale at "100%" because fallback strings count as covered. Support tickets from Arabic users are the first signal anything is wrong.

## After

During release preparation, G-AC-071 key parity reports the gap instead of hiding it:

```text
ar  returns.*  14 keys missing from locale catalog (present in source)
Result: primary-flow gap — release blocked for ar under tier "full"
```

The team chooses, explicitly, between the two honest options:

1. **Translate and review the returns flow**, then ship Arabic at the full tier; or
2. **Ship at a recorded lower tier**: the project file records Arabic as "UI-only — returns flow pending", the help page says exactly that, and in staging the untranslated screens render with the visible fallback marking so the gap stays findable. In production, the returns entry point carries a short Arabic notice that the following steps are shown in English, so the source-language content is marked, never silent.

The locale's claim, its recorded tier, and what users actually see now agree — and the 14 keys sit in the next release's frozen set with a named reviewer assigned.

Note: corrects AC-151, AC-152 — fallback is explicit and visible, and a locale is claimed "supported" only at the tier its UI, taxonomy, search, formatting, RTL, and descriptions have actually passed.
