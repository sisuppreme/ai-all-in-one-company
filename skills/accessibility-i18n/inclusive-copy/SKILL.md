# inclusive-copy

## Metadata

- **Owner department:** D13 Accessibility & i18n (AC)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** WCAG 2.2 (criteria 2.4.4, 2.5.3, 3.3.1–3.3.3), W3C — https://www.w3.org/TR/WCAG22/ ; W3C WAI, "Writing for Web Accessibility" — https://www.w3.org/WAI/tips/writing/
- **Depends on:** internationalization (copy lives in its message catalogs), wcag (the criteria this copy standard serves)
- **Feeds into:** localization-workflow (translates this source copy), screen-readers (accessible names and announcements are this copy read aloud)

## When to use / Do NOT use

- **Use when:** Writing or reviewing any words a user reads or hears — UI labels, buttons, links, instructions, error and empty-state copy, alt text, email and notification text — so the widest range of users can understand it and act on it, in the source language and in translation.
- **Do NOT use when:** Externalizing strings or wiring locale formatting (internationalization), running the translation pipeline (localization-workflow), or judging structural accessibility such as semantics, focus, and contrast (wcag, screen-readers, keyboard-accessibility).

## Rules

1. **AC-181 — Task copy is plain language.** Instructions, errors, and primary-flow text use common words and short sentences at a lower-secondary reading level. A term of art appears only when the task requires it, and is explained in the user's words at first use.
2. **AC-182 — One name per object, everywhere.** Every concept, object, and action carries the single term recorded in the project glossary — in navigation, buttons, errors, emails, help, and every translation. The same thing never appears under two names in one product (DET-CON-017).
3. **AC-183 — Link and button text stands alone.** Link text names its destination and button text names its action, so both make sense read out of context in a screen reader's link list (WCAG 2.4.4). The accessible name matches or contains the visible label (WCAG 2.5.3), so voice-control users can speak what they see.
4. **AC-184 — Error copy names the field, the problem, and the fix.** Each error is written in the user's terms, attached to the field it concerns, and says what to change (WCAG 3.3.1, 3.3.3). It never blames the user, never shows a bare code, and is never carried by color alone.
5. **AC-185 — Instructions and format hints come before the control.** Required formats, password rules, and constraints are stated before entry, not revealed by a failed submit (WCAG 3.3.2 practice; DET-UX-027). The user learns the rule before they can break it.
6. **AC-186 — Every state has words that say what happened and what is next.** Empty, loading, success, and failure states state the situation and the available action: an empty list explains why it is empty and how to fill it; a confirmation names what was actually done.
7. **AC-187 — No idiom, slang, or culture-specific metaphor carries meaning.** Copy is written literally, so it survives translation and reads plainly to users outside the source culture. A figure of speech is decoration only when the literal instruction stands complete without it.
8. **AC-188 — No ability-assuming or gendered-by-default language.** Copy does not assume how the user perceives or operates the product ("simply click", "see the report", "blind to errors"), and does not assign gender by default. Where a language requires gendered forms, they are chosen deliberately with MessageFormat `select`, never by accident.
9. **AC-189 — Alt text and captions are copy.** Alt text describes the image's content or purpose in the page; decorative images get empty `alt=""`. Alt text is never a file name, never "image of", and never a caption repeated word for word (DET-CON-027).
10. **AC-190 — The action comes first.** Instructions, headings, and errors front-load what the user must do or know; background and reasons follow. A user who reads only the first clause of each message can still complete the task.
11. **AC-191 — Formality is a per-locale decision.** Each locale's style guide records its politeness and formality level (e.g., German Sie/du, Spanish tú/usted), and translations are reviewed against it. The source language's level of familiarity is never imposed on a locale by default.
12. **AC-192 — Destructive-action copy names the object and the consequence.** The explanation states what will be deleted or changed and whether it can be undone; the confirm button repeats the action ("Delete project"), never a bare "Yes" or "OK" whose meaning depends on reading the dialog.

## BAN list

- **BAN-AC-091 — "Click here" and other context-free link text.** Banned: link or button text that names the gesture instead of the destination or action — "click here", "tap here", "learn more", "this page". Defeats: DET-UX-002. Bad: the billing page ends with "To download your invoice, click here", which a link list reads as one of six identical "click here" entries. Instead: "Download the March invoice (PDF)" — text that names the destination and stands alone. Severity: BLOCK.
- **BAN-AC-092 — Generic, coded, or blaming error messages.** Banned: errors that state no field, no problem, and no fix — "Invalid input", "Error 422", "You failed to enter a valid date", "Something went wrong" as the whole message. Defeats: DET-UX-006. Bad: checkout rejects the card expiry with "Invalid value. Try again", leaving the user to guess which value and what "valid" means. Instead: "Card expiry — this date is in the past. Enter a future date in MM/YY format." Severity: BLOCK.
- **BAN-AC-093 — Placeholder text as the only label.** Banned: a form field whose placeholder is its sole label or instruction, so the label vanishes on entry and is never announced as a name. Defeats: DET-UX-022. Bad: the search-filter field shows only "DD/MM/YYYY" as a placeholder; once typing starts, the expected format is gone and screen-reader users get no label at all. Instead: a persistent visible label "Start date" plus the hint "Format: DD/MM/YYYY" beside the field, before entry. Severity: BLOCK.
- **BAN-AC-094 — Directions that point at color alone.** Banned: copy that locates information by color — "fix the fields marked in red", "press the green button", "items in orange are overdue". Defeats: DET-UX-021. Bad: after a failed submit, "Correct the fields shown in red" tells a color-blind or screen-reader user nothing about which fields or what is wrong. Instead: name the field and the state in words — "Email address — this address is already registered" — with color as a redundant cue only. Severity: BLOCK.
- **BAN-AC-095 — Generic filler in place of an instruction.** Banned: marketing filler and AI-vocabulary padding where the user needs a fact or an action — "supercharge your workflow with our cutting-edge, seamless solution". Defeats: DET-CON-006. Bad: the import screen's only guidance is "Unlock the power of effortless data synergy", so the user learns nothing about file format, size limit, or what happens next. Instead: "Import a CSV file up to 10 MB. Columns: name, email, signup date." Severity: WARN.

## Gates

- **G-AC-091 — Banned-pattern lint over the catalogs.** Verifies: AC-183, AC-184, AC-189. Check: grep the message catalogs for the banned patterns — `grep -rniE "click here|tap here|learn more|read more"` over link/button keys; error-message keys matching bare codes (`error [0-9]{3}` with no other text) or color-only references (`marked in red|shown in red|green button`); alt-text values matching file-name patterns (`\.(png|jpe?g|svg)$`). Pass: zero findings. Fail: block shipment; rewrite each hit to the rule it violates and re-run. Recorded in: progress.md.
- **G-AC-092 — Reading-level scan of primary flows.** Verifies: AC-181, AC-190. Check: extract the source-locale strings of the primary flows (onboarding, checkout, the top task per product area) plus all error strings into a plain-text file and run a readability scorer (e.g., `textstat` Flesch-Kincaid grade). Pass: task copy scores at or below the project's agreed grade ceiling (default: grade 9); every string above it is rewritten or listed in progress.md with a written justification (e.g., a legally fixed term). Fail: block shipment for unrewritten, unjustified strings. Recorded in: progress.md.
- **G-AC-093 — Glossary conformance check.** Verifies: AC-182. Check: run the TMS/catalog glossary check (or a scripted term scan) comparing catalog strings against the project glossary's approved terms and its recorded do-not-use synonyms. Pass: zero do-not-use synonyms and zero concepts appearing under two names. Fail: block shipment; unify on the glossary term in every surface, including emails and help. Recorded in: progress.md.
- **G-AC-094 — Human plain-language review of flows and errors.** Verifies: AC-184, AC-185, AC-186, AC-190. Check: a reviewer who did not write the copy reads (a) every primary-flow string in order, (b) every error string triggered by deliberately failing each form, and (c) the link/button text as an out-of-context list. Pass: the reviewer can state, for each error, the field, problem, and fix without seeing the screen, and can predict each link's destination from its text alone; sign-off recorded. Fail: return failing strings to the author; the release does not proceed on the reviewer's "probably fine". Recorded in: progress.md.
- **G-AC-095 — Per-locale idiom and formality review.** Verifies: AC-187, AC-188, AC-191. Check: for each shipping locale, the locale reviewer checks the translated primary-flow and error strings against the locale style guide — formality level consistent throughout, no source idiom carried over literally, gendered forms deliberate. Pass: reviewer sign-off per locale with zero unresolved idiom or formality findings. Fail: block shipment for that locale only; other locales are unaffected. Recorded in: progress.md.

## Anti-patterns

- **The system talking about itself.** Copy narrates the software instead of guiding the user — "Your request has been successfully processed by the system" — instead of the user's outcome: "Payment sent. It arrives within one business day." Catch it by asking of every message: what does the *user* now know or do?
- **The buried requirement.** A long explanatory paragraph sits above the form while the actual constraint (character limit, required format, deadline) appears only in the last sentence or after a failure. Catch it by reading each flow's copy first-clauses only (AC-190): if the requirement is not there, it is buried.
- **The cheerful void.** An empty state performs enthusiasm instead of helping — "Nothing here yet! 🎉" — with no reason and no next step, so a new user cannot tell whether the product is broken or just unused. Catch it by checking every empty state against AC-186: situation plus action, or it is a void.
- **The apology loop.** Every failure opens with the same ritual — "Oops!" — whatever went wrong, training users to ignore the opening words entirely, including when the message is serious. Catch it by listing all error strings side by side: identical openings across unrelated failures are the tell.

## Examples

- [Example 1 — Context-free links and buttons rewritten to stand alone](examples/example-1.md) — violates/corrects AC-183.
- [Example 2 — Blaming, coded error replaced by field, problem, and fix](examples/example-2.md) — violates/corrects AC-184, AC-185.
- [Example 3 — Idiom and ability-assuming copy rewritten plainly](examples/example-3.md) — violates/corrects AC-187, AC-188.

## Recall anchors

- If a link list can't explain it, the link text failed.
- Every error: field, problem, fix — in the user's words, before blame, without a code.
- One thing, one name — the glossary term, on every surface, in every language.
- Say it literally: if an idiom carries the meaning, translation will drop it.
- Instructions before the control; the action before the explanation.

## Checklist

- [ ] Link and button text names its destination or action and stands alone out of context — G-AC-091 lint is clean.
- [ ] Every error message names the field, states the problem, and gives the fix; no bare codes, no blame, no color-only references.
- [ ] Required formats and constraints are stated before the control, not revealed by failure.
- [ ] Empty, loading, success, and failure states each say what happened and what to do next.
- [ ] Every concept uses its single glossary term on all surfaces — G-AC-093 check is clean.
- [ ] No idiom, slang, or ability-assuming phrase carries meaning in shipped copy.
- [ ] Alt text describes content or purpose; decorative images use empty `alt=""`; no file names.
- [ ] Primary-flow copy passed the reading-level scan (G-AC-092) and the human plain-language review (G-AC-094).
- [ ] Each shipping locale has a recorded formality level and a signed idiom/formality review — G-AC-095.
