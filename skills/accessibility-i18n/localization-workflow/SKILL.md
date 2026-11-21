# localization-workflow

## Metadata

- **Owner department:** D13 Accessibility & i18n (AC)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** ICU MessageFormat documentation, Unicode — https://unicode-org.github.io/icu/userguide/format_parse/messages/ ; Unicode CLDR — https://cldr.unicode.org/
- **Depends on:** internationalization (produces the catalogs, ICU messages, and translator context notes this workflow moves through the pipeline)
- **Feeds into:** rtl-layouts (translated RTL locales enter direction and per-script layout verification), accessibility-audit (localized builds and flows are audit scope)

## When to use / Do NOT use

- **Use when:** Running the translation process for a release — string freeze, translator handoff with context, automated import checks, in-context and native-speaker review, fallback policy, and the per-locale release decision. This skill owns the process: extraction, translation, review, QA, release.
- **Do NOT use when:** Engineering the source product for localization — catalog structure, ICU MessageFormat authoring, `Intl` formatting, layout flexibility (that is internationalization), doing RTL mirroring and per-script layout QA (rtl-layouts), or deciding the source copy's wording and reading level (inclusive-copy).

## Rules

1. **AC-141 — Localization runs as a pipeline with tracked states, not correspondence.** Each string moves through extraction → freeze → handoff → translation → automated checks → in-context review → release, and its state per locale is visible in the translation management system (TMS) or catalog tooling. A string whose state nobody can state is not in the pipeline, whatever an email thread says.
2. **AC-142 — Source strings freeze per release.** At the freeze point the release's key set and source text are fixed; translators work against the frozen set. Strings authored after the freeze belong to the next release unless they pass AC-150 change control.
3. **AC-143 — Every handoff ships translator context.** Each string goes out with its context note from the catalog (where it appears, what each placeholder means), a screenshot or screen reference, any character or byte limit, the project glossary, and the do-not-translate list (product names, legal names, code-like tokens). A string sent without context is sent back, not guessed at.
4. **AC-144 — Placeholder and ICU integrity is machine-checked on every import.** Every imported message is parsed as ICU MessageFormat and its placeholder set (names, types, plural/select structure) is compared against the source message. A mismatch or an unparsable message fails the build — it is never a typo to fix later.
5. **AC-145 — Key parity is enforced per locale.** Every locale catalog carries every source key. A missing key in a primary locale is a release blocker for primary flows; elsewhere it follows the fallback policy in AC-151 and is counted in the release report, never silently absent.
6. **AC-146 — Translation memory and the glossary are maintained as project assets.** Approved translations are reused through translation memory, product terms follow the glossary in every locale, and the do-not-translate list is honored exactly. The same concept never appears under two translated names in one locale.
7. **AC-147 — Machine translation is labeled and never ships unreviewed.** MT output is marked as MT in the pipeline wherever it is used as a draft. Native-speaker human review is mandatory before release for legal, payment, health, and safety strings, and for all primary-flow strings; MT alone never satisfies review for those classes.
8. **AC-148 — Every locale has a named human reviewer, and review happens in context.** "The vendor delivered it" is not review. The named reviewer walks the primary flows on a staging build in the real UI — real layout, real data lengths, real error paths — and signs off per locale; string-list proofreading alone does not sign off a locale.
9. **AC-149 — Length and expansion risk are flagged at translation time.** Translations are checked against the character/byte limits recorded in the context notes as they are delivered, and over-limit strings are resolved with the translator (shorter wording, approved abbreviation) before layout QA — overflow is not discovered by a screenshot at the end.
10. **AC-150 — A post-freeze source change invalidates that key's translations.** Any change to a frozen source string marks its translations in every locale as stale until re-translated or re-checked against the new source. The changed key ships in a locale only after that re-check; the old translation never rides along by default.
11. **AC-151 — Fallback is explicit, visible, and honestly claimed.** Each locale declares its fallback chain. In staging, untranslated strings render visibly marked as fallback. In production, fallback follows the recorded per-string-class policy, and any source-language content shown to users is marked as such — never silently presented as translated. A locale is claimed "supported" only when its UI, taxonomy, search, formatting, RTL, and descriptions have each passed their gates.
12. **AC-152 — Each locale's support tier is recorded and matches every public claim.** The project files record a tier per locale (full / UI-only / best-effort) with the release validation report: keys translated, checks passed, reviewer sign-offs. Help pages, marketing copy, and sales answers cite the tier; a best-effort locale is never described as fully supported.

## BAN list

- **BAN-AC-071 — Machine translation shipped without human review.** Banned: MT output released as final copy, above all on legal, payment, health, safety, or primary-flow strings. Defeats: DET-UX-006. Bad: a machine-translated checkout error tells users in the target language that their payment "will be punished" instead of "will be charged", and users abandon a working flow because the message is garbled and frightening. Instead: MT is labeled as a draft in the pipeline and passes native-speaker review (AC-147) before release; unreviewed MT stays out of the build. Severity: BLOCK.
- **BAN-AC-072 — Translations imported without placeholder/ICU validation.** Banned: accepting a locale file whose messages were never parsed or compared against the source placeholders. Defeats: DET-UX-010. Bad: a translated plural message loses a closing brace; at render time the message throws, the order-history view fails to load, and localized users get a blank screen where the source locale works. Instead: every import runs the G-AC-071 parse-and-compare check; a broken message fails the build and returns to the translator. Severity: BLOCK.
- **BAN-AC-073 — Silent fallback presented as a translated locale.** Banned: serving source-language strings in production with no marking while the locale is listed as supported. Defeats: DET-UX-015. Bad: the Arabic storefront is advertised as fully Arabic, but the returns flow renders in English with no indication, so the same product behaves differently across its own screens depending on locale. Instead: fallback follows AC-151 — visibly marked in staging, policy-governed and source-marked in production, and the locale's claim matches its recorded tier (AC-152). Severity: BLOCK.
- **BAN-AC-074 — Translation accepted with no length check against its limits.** Banned: delivering strings whose recorded character/byte limits were never checked, leaving expansion to layout QA. Defeats: DET-UX-023. Bad: an unchecked long translation of the checkout button label overflows its fixed bar on a 360px viewport and pushes the pay action off-screen, breaking the primary task on mobile for that locale only. Instead: limits travel with the string (AC-143) and are enforced at delivery (AC-149, G-AC-072); over-limit strings are reworded before layout QA. Severity: BLOCK.
- **BAN-AC-075 — Post-freeze source change shipped over stale translations.** Banned: editing a frozen source string and releasing while locales still carry the translation of the old text. Defeats: DET-UX-013. Bad: the source flow drops its "verify your phone" step, but the localized onboarding still instructs users to complete that step, and localized first-time users stall mid-flow looking for a screen that no longer exists. Instead: the change invalidates the key in every locale (AC-150); it re-enters translation and ships only after re-check. Severity: BLOCK.

## Gates

- **G-AC-071 — Key-parity and placeholder-integrity check (automated).** Verifies: AC-144, AC-145. Check: run the catalog validation script over every locale file for the release: diff each locale's key set against the frozen source key set, parse every message with the ICU MessageFormat parser, and compare each message's placeholder names/types and plural/select structure against the source message. Pass: zero missing keys in primary locales, zero unparsable messages, zero placeholder mismatches across all locales. Fail: block shipment; offending keys return to translation and are re-imported. Recorded in: progress.md.
- **G-AC-072 — Length-limit check (automated).** Verifies: AC-143, AC-149. Check: for every catalog entry carrying a character or byte limit in its context note, compare each locale's delivered string length against the limit and produce an over-limit report per locale. Pass: zero over-limit strings in primary flows; any elsewhere are individually waived in writing by the locale reviewer. Fail: block shipment for the affected locale until strings are reworded and re-checked. Recorded in: progress.md.
- **G-AC-073 — Visible-fallback check (automated + staging walk).** Verifies: AC-151, AC-152. Check: in the staging build, force one deliberately untranslated key per locale and confirm it renders with the visible fallback marking; then inspect the production configuration and confirm fallback follows the recorded per-string-class policy and the locale's public claim matches its recorded support tier. Pass: marking renders in staging for every locale, and no production locale claims a tier above its record. Fail: block shipment for the mis-claimed or unmarked locale. Recorded in: progress.md.
- **G-AC-074 — In-context review sign-off (manual).** Verifies: AC-147, AC-148. Check: the named reviewer for each locale walks the primary flows on the staging build in that locale — including one error path and one empty state — and records sign-off; legal, payment, health, and safety strings additionally carry native-speaker review evidence, and any MT-drafted string in those classes shows its review record. Pass: sign-off recorded for every shipping locale, with review evidence for every critical string class. Fail: the locale does not ship; it waits for review or drops to a lower recorded tier. Recorded in: progress.md.

## Anti-patterns

- **The spreadsheet pipeline.** Strings are emailed around as spreadsheets, versions fork, and nobody can say which file is current or which strings were reviewed. Catch it by asking for any string's pipeline state: if the answer requires searching an inbox, there is no pipeline (AC-141).
- **The 100%-translated dashboard.** The TMS reports full coverage because missing keys quietly fall back and empty strings count as translated, so the release looks complete while users see source-language screens. Catch it by reconciling the dashboard against the G-AC-071 key-parity report and the G-AC-073 fallback walk, never by quoting the percentage.
- **Review theater.** A reviewer signs off from a bilingual string list without ever opening the product, so correct words land in the wrong places — a verb translated as a noun, a label that belongs to another screen. Catch it by requiring the sign-off to name the staging build and the flows walked (G-AC-074).
- **Big-bang localization.** All translation is deferred to the end of the release, so review, length fixes, and re-checks compete with the ship date and lose. Catch it at planning: if the freeze date sits after feature-complete with no review window, the schedule — not the reviewers — is the defect.

## Examples

- [Example 1 — Broken plural import caught by placeholder-integrity check](examples/example-1.md) — violates/corrects AC-144, AC-145.
- [Example 2 — Context-free handoff mistranslates a payment button](examples/example-2.md) — violates/corrects AC-143, AC-147.
- [Example 3 — Silent fallback behind a "fully supported" locale claim](examples/example-3.md) — violates/corrects AC-151, AC-152.

## Recall anchors

- A pipeline with states, not an email with a spreadsheet.
- Broken placeholder, broken build — integrity is machine-checked, never eyeballed.
- Machine translation is a draft with a label, never a reviewer.
- Fallback is visible or it is a false claim: supported means every surface passed.
- Change the source, invalidate the translations — stale strings never ride along.

## Checklist

- [ ] Source strings are frozen for the release and the frozen key set is the one translators received — AC-142.
- [ ] Every handed-off string carried its context note, screenshot/screen reference, limits, glossary, and do-not-translate list — AC-143.
- [ ] G-AC-071 passed: zero missing keys in primary locales, zero unparsable messages, zero placeholder mismatches.
- [ ] G-AC-072 passed: no over-limit strings in primary flows; waivers elsewhere are written and signed.
- [ ] Every locale has a named reviewer; MT-drafted strings are labeled, and legal/payment/health/safety strings carry native-speaker review — AC-147, AC-148.
- [ ] G-AC-074 sign-off is recorded per locale from an in-context staging walk, error path included.
- [ ] Post-freeze source changes invalidated their keys in all locales and were re-checked before shipping — AC-150.
- [ ] Staging fallback renders visibly marked, production fallback matches the recorded policy, and each locale's public claim matches its recorded support tier — AC-151, AC-152, G-AC-073.
