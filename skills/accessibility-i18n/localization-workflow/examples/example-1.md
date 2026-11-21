# Example 1 — Broken plural import caught by placeholder-integrity check

## Before

Source message (English):

```json
"cart.itemCount": "{count, plural, one {# item in your cart} other {# items in your cart}}"
```

Delivered German translation, imported without any parse or placeholder check:

```json
"cart.itemCount": "{anzahl, plural, one {# Artikel im Warenkorb} other {# Artikel im Warenkorb}"
```

Two defects ride in together: the placeholder was renamed from `count` to `anzahl`, so the application passes a value the message never receives, and the closing brace of the plural is missing, so the message is not valid ICU MessageFormat at all. In the running product the cart header throws at render time for German users — the page region comes up blank while the English build works fine. Nobody notices until a German user reports it, because the file "looked translated" in the spreadsheet.

## After

The import runs G-AC-071 before the strings reach a build:

```text
$ validate-catalogs --source en.json --locales de.json
de.json  cart.itemCount  ERROR  unparsable ICU message (missing closing brace)
de.json  cart.itemCount  ERROR  placeholder mismatch: source {count}, locale {anzahl}
Result: FAIL — 1 key blocked, build stopped
```

The key returns to the translator with the error report and the original context note. The corrected delivery:

```json
"cart.itemCount": "{count, plural, one {# Artikel in Ihrem Warenkorb} other {# Artikel in Ihrem Warenkorb}}"
```

Re-import passes: the message parses, the placeholder set matches the source exactly, and the key counts toward German key parity only now — not when the broken file arrived.

Note: corrects AC-144, AC-145 — placeholder and ICU integrity is machine-checked on every import and missing or broken keys block the release; a delivered file is not a translated string until it validates.
