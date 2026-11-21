# internationalization

## Metadata

- **Owner department:** D13 Accessibility & i18n (AC)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** ICU, Unicode — https://icu.unicode.org/home ; Unicode CLDR plural rules — https://cldr.unicode.org/index/cldr-spec/plural-rules ; WCAG 2.2 (criteria 3.1.1, 3.1.2), W3C — https://www.w3.org/TR/WCAG22/
- **Depends on:** wcag (the `lang` requirements this skill implements are WCAG 3.1.1/3.1.2)
- **Feeds into:** localization-workflow (consumes the catalogs and context notes), rtl-layouts (consumes correct `lang`/`dir` metadata), inclusive-copy

## When to use / Do NOT use

- **Use when:** Engineering the source product so a new locale is data, not a code change — extracting strings into catalogs, wiring ICU MessageFormat and `Intl` formatting, setting `lang`/`dir`, and designing layout that survives translation. This skill owns engineering readiness: strings, formats, layout flexibility.
- **Do NOT use when:** Running the translation process itself — string freezes, translator handoff, review, fallback policy per string class (that is localization-workflow), doing direction-specific layout and mirroring work (rtl-layouts), or writing the source copy's wording (inclusive-copy).

## Rules

1. **AC-121 — Every user-facing string lives in a message catalog.** UI copy, emails, notifications, error messages, alt text, and PDF templates are externalized into catalogs keyed by meaning (e.g. `checkout.payButton`), never by English text or screen position. A user-facing literal in component code is a defect, not a shortcut.
2. **AC-122 — Whole messages are the unit of translation.** Any string with plurals, gender, lists, or embedded values is one ICU MessageFormat message. Word order is a property of the locale, so a sentence is never assembled from translated fragments.
3. **AC-123 — Plurals come from CLDR categories, never from code branches.** Plural and ordinal selection uses MessageFormat plural/selectordinal or `Intl.PluralRules`, driven by Unicode CLDR rules (Japanese uses one category, English two, Polish four, Arabic six). Code passes the raw count; it never tests `count == 1`.
4. **AC-124 — All formatting goes through locale APIs.** Dates, times, numbers, currencies, units, lists, and relative time ("in 3 days") are formatted with `Intl.DateTimeFormat`, `Intl.NumberFormat`, `Intl.ListFormat`, `Intl.RelativeTimeFormat` (or ICU4J/ICU4C equivalents) for the active locale, with the time zone stated explicitly where it matters. No value is formatted by string concatenation.
5. **AC-125 — Formatting is not conversion.** An amount is displayed in its own currency via `Intl.NumberFormat` with that currency code. The display layer never converts currency, units, or time zones silently; conversion happens only where the product explicitly defines it, and the result is labeled as converted.
6. **AC-126 — Every document and language change carries correct `lang` and `dir`.** Each page sets a valid BCP 47 `lang` on the root element and `dir` matching the locale's direction; inline passages in another language carry their own `lang` (WCAG 3.1.1, 3.1.2 — this is also how screen readers choose pronunciation). Direction is declared, never guessed from the text content.
7. **AC-127 — Language switching changes the whole experience.** Selecting a locale changes all UI strings, formats, sort order, and direction together — never body copy alone with English buttons, dates, and errors left behind.
8. **AC-128 — Locale behavior is data, not constants.** Sort order (via `Intl.Collator`), calendars, first day of week, numbering system, and name/address field order come from CLDR-backed locale data or explicit per-locale configuration — never from hard-coded arrays in code.
9. **AC-129 — Layout is designed for expansion and contraction.** Containers flex with text length: no fixed-width text buttons, no fixed-height single-line labels without an overflow behavior, and no text baked into images or canvas. Translated strings may run substantially longer or shorter than the source; the layout must absorb both.
10. **AC-130 — Fallback chains are explicit and visible in staging.** Each locale declares its fallback chain (e.g. `ar-EG` → `ar` → source locale). In staging builds, an untranslated string renders visibly marked as fallback so gaps are found before release; production fallback follows the policy localization-workflow sets per string class.
11. **AC-131 — Every string ships with a translator context note.** At authoring time, each catalog entry records where it appears, what its placeholders mean, and any character limit. A string a translator cannot interpret from the catalog alone is unfinished.
12. **AC-132 — Pseudo-localization runs before real translation.** A pseudo-locale build (expanded, accented, bracketed strings) is rendered and checked for hard-coded text (which stays in the source language), truncation, overflow, and mojibake before any translator is engaged.

## BAN list

- **BAN-AC-061 — Hard-coded user-facing string in a component.** Banned: a literal such as `<button>Save changes</button>` or an English error string embedded in code instead of a catalog key. Defeats: DET-NONE — no DET parameter names this signal; pattern owned by this skill. Bad: the settings screen renders from the catalog in German, but the delete-account dialog — hard-coded — stays in English, so the same action behaves differently across screens and locales. Instead: every string is a catalog key (`settings.deleteDialog.title`) resolved through the message system, so all screens localize together. Severity: BLOCK.
- **BAN-AC-062 — Sentence built by string concatenation.** Banned: assembling a message from fragments, e.g. `t('youHave') + ' ' + n + ' ' + t('newMessages')`. Defeats: DET-NONE — no DET parameter names this signal; pattern owned by this skill. Bad: in a locale whose word order puts the count first, the concatenation produces a garbled, ungrammatical message the user cannot act on. Instead: one MessageFormat message — `You have {count, plural, one {# new message} other {# new messages}}` — translated as a unit per locale. Severity: BLOCK.
- **BAN-AC-063 — Plural chosen by a `count == 1` branch in code.** Banned: `count === 1 ? t('item') : t('items')` or any code-side plural branching. Defeats: DET-NONE — no DET parameter names this signal; pattern owned by this skill. Bad: Polish, which needs four plural forms, gets the English two-form logic, so counts like 3 render with the wrong grammatical form and the text reads as broken. Instead: pass the raw count to a MessageFormat plural (or `Intl.PluralRules`) and let CLDR categories select the form. Severity: BLOCK.
- **BAN-AC-064 — Hand-rolled date, number, or currency formatting.** Banned: formatting by concatenation or fixed pattern (`month + '/' + day + '/' + year`, `'$' + amount.toFixed(2)`), parsing user input against one hard-coded format, or converting a price to another currency in the display layer. Defeats: DET-UX-027. Bad: a user in a day-first locale types 03/04/2026 meaning 3 April; the form, built around MM/DD/YYYY, rejects it or silently stores 4 March — the real requirement is revealed only by failing. Instead: format and parse through `Intl`/ICU for the active locale, state the expected format beside the field, and display amounts in their own currency. Severity: BLOCK.
- **BAN-AC-065 — Text baked into an image or locked in a fixed-width box.** Banned: headlines, labels, or button text rendered into image/canvas assets, or text containers with fixed pixel widths/heights and no overflow behavior. Defeats: DET-UX-023. Bad: the hero headline is a PNG in English; the German build either keeps the English image or ships a clipped, overflowing headline that pushes the primary call-to-action off-screen. Instead: real text in flexible containers, checked in the pseudo-localization render (G-AC-062); images carry no words the user must read. Severity: BLOCK.

## Gates

- **G-AC-061 — Hard-coded string scan.** Verifies: AC-121, AC-124. Check: run the project lint/grep over UI source for user-facing literals outside catalog imports (JSX text nodes, string literals passed to rendering, template text), e.g. the i18n lint rule set plus `grep -rn` spot patterns agreed for the stack; also grep for hand-rolled formatters (`toFixed(` in view code, manual month/day concatenation, custom date-format functions). Pass: zero findings in both scans. Fail: block shipment; each finding is externalized or routed through `Intl` before re-check. Recorded in: progress.md.
- **G-AC-062 — Pseudo-localization render.** Verifies: AC-129, AC-132, AC-121. Check: build with the pseudo-locale (expanded, accented, bracketed) and screenshot every primary screen and primary flow; inspect each shot for text still in the source language (hard-coded), clipped or overflowing strings, and mojibake. Pass: no source-language leftovers, no truncation or overflow on any primary screen. Fail: block shipment; fix the string or the container and re-render. Recorded in: progress.md.
- **G-AC-063 — Locale metadata and switch test.** Verifies: AC-126, AC-127, AC-130. Check: for each supported locale, load the primary pages and assert the root `lang` is the correct BCP 47 tag, `dir` matches the locale, a language switch re-renders strings, formats, and direction together, and one deliberately untranslated key in staging renders with the visible fallback marking. Pass: all assertions hold for every supported locale. Fail: block shipment for the failing locale. Recorded in: progress.md.
- **G-AC-064 — Message and context-note review.** Verifies: AC-122, AC-123, AC-131. Check: manual review of the catalog diff for the release — every new or changed entry is a whole MessageFormat message (no fragments), plurals use CLDR categories, and each entry carries a context note with placeholder meanings and limits. Pass: reviewer signs off with zero fragment messages and zero missing context notes. Fail: return entries to the author; the catalog does not go to localization-workflow. Recorded in: progress.md.

## Anti-patterns

- **The translated-body fig leaf.** The page's paragraphs are localized while navigation, buttons, form errors, and emails stay in the source language, so the product claims a locale it only half speaks. Catch it by switching locale and walking a complete process — including the error path — not by reading the landing page.
- **The source-length layout.** Design and QA only ever see the source language, so every container is sized to English and the first real translation breaks the UI. Catch it by reviewing designs against the pseudo-localized build, not the source build.
- **The locale constant.** A developer hard-codes `en-US` (or one currency, one time zone) "temporarily" in a formatter or a sort, and it ships because the default locale looks correct. Catch it by testing with a non-default locale and a non-Latin numbering system in the G-AC-063 pass.
- **Key-by-English-text catalogs.** Catalog keys are the English strings themselves, so fixing a typo in the source copy orphans every translation. Catch it at catalog review: keys name meaning and location, never copy.

## Examples

- [Example 1 — Hard-coded checkout strings externalized](examples/example-1.md) — violates/corrects AC-121.
- [Example 2 — Concatenated message and `count == 1` plural replaced by one ICU message](examples/example-2.md) — violates/corrects AC-122, AC-123.
- [Example 3 — Hand-rolled date and price formatting replaced by `Intl`](examples/example-3.md) — violates/corrects AC-124, AC-125.

## Recall anchors

- Localization is data, not code changes: if a new locale needs a developer, the engineering failed.
- Whole messages are translated; fragments and concatenation break word order.
- Code never branches on count — CLDR owns plurals.
- Format with `Intl`, in the amount's own currency: formatting is not conversion.
- `lang` and `dir` on every page — declared, never guessed.

## Checklist

- [ ] Every user-facing string (UI, email, errors, alt text, PDFs) resolves from a catalog key — G-AC-061 scan is clean.
- [ ] No sentence is built by concatenation; strings with values are whole ICU MessageFormat messages.
- [ ] Plurals and ordinals use CLDR categories via MessageFormat/`Intl.PluralRules`; no `count == 1` branch exists.
- [ ] Dates, numbers, currencies, units, and relative time all format through `Intl`/ICU for the active locale.
- [ ] No display-layer currency conversion; amounts show in their own currency.
- [ ] Root `lang` (BCP 47) and `dir` are correct per locale, and inline language changes carry their own `lang`.
- [ ] Pseudo-localization render passed with no source-language leftovers, truncation, or overflow — G-AC-062.
- [ ] Every catalog entry carries a translator context note with placeholder meanings and limits.
