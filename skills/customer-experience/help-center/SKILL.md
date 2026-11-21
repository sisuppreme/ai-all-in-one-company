# help-center

## Metadata

- **Owner department:** D18 Customer Experience (CX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://support.zendesk.com/hc/en-us/articles/4408846795674-Getting-started-with-your-help-center ; https://support.zendesk.com/hc/en-us/articles/4408883389338
- **Depends on:** support-ticketing
- **Feeds into:** in-app-chat, user-onboarding

## When to use / Do NOT use

- **Use when:** building or maintaining a help center — choosing its structure, writing or revising articles, configuring search, or running the review cycle that keeps articles matched to the current product.
- **Do NOT use when:** answering an individual customer's request (use support-ticketing / in-app-chat), writing marketing or landing-page copy (use copywriting), or documenting internal procedures for staff (use runbook-writing).

## Rules

1. **CX-041 — Real questions only.** An article is published only because a real, recurring customer question exists behind it (from tickets, chat transcripts, or search logs); no article is written to fill out a category or to make the center look complete at launch.
2. **CX-042 — One problem per article.** Each article solves exactly one problem end to end; a second problem gets its own article, cross-linked, never appended.
3. **CX-043 — Customer-language structure.** The hierarchy is category → section → article, at most three levels deep, and category and article names use the words customers use in tickets, not internal team, feature-code, or org-chart names.
4. **CX-044 — Steps match the current UI.** Every step names the exact label, button, or menu item as it appears in the current released UI; an article whose steps cannot be followed verbatim on the live product is unpublished or fixed before release.
5. **CX-045 — Review date on every article.** Each article carries a last-verified date; a UI release that changes a covered flow puts the affected articles into re-verification or archival in the same release cycle.
6. **CX-046 — Search tested with real phrasing.** Help search is tested with the actual phrasing customers used in tickets and prior searches, not with article titles; a query a customer would plausibly type must return the article that answers it.
7. **CX-047 — Zero-result searches are work items.** Search queries that return no result are logged and reviewed on the review cycle; repeated zero-result queries become a new article, a retitle, or added search terms — they are never ignored.
8. **CX-048 — Every article ends at a human.** Each article ends with a working path to human support (ticket form, chat, or email that actually creates a ticket per support-ticketing); an article with a dead end is not finished.
9. **CX-049 — Promises are linked, never restated.** Articles never state response times, support hours, or availability in their own text; they link to the single configured support-expectations page, so the promise exists in exactly one place.
10. **CX-050 — Reachable and resolving.** Every article is reachable without authentication unless it genuinely requires an account, and every link in every article resolves; a broken link found by the crawl gate is fixed or the article is pulled.
11. **CX-051 — Screenshots show the real, current UI.** Screenshots are captured from the current released product with sample data; a screenshot from an older UI version, a design mock, or another product is replaced before publication.
12. **CX-052 — Archive, don't abandon.** An article for a removed or changed feature is archived or rewritten in the release that changes the feature; the center never keeps live instructions for behavior the product no longer has.

## BAN list

- **BAN-CX-021 — Placeholder or filler articles.** Banned: publishing "coming soon," lorem ipsum, or generic launch-day FAQ articles with no real question behind them. Defeats: DET-CON-001. Bad: a "Getting started" article reading "Lorem ipsum dolor sit amet — content coming soon!" Instead: publish only articles written from real recurring questions, and leave the category unpublished until its first real article exists. Severity: BLOCK.
- **BAN-CX-022 — AI-spun articles about features that do not exist.** Banned: generating articles in bulk for features, settings, or integrations the product does not have. Defeats: DET-CON-025. Bad: twenty near-identical articles describing an "Advanced reporting" module that was never built. Instead: write one article per real question about shipped behavior, verified against the live product. Severity: BLOCK.
- **BAN-CX-023 — Stale steps and old-UI screenshots.** Banned: leaving live instructions or screenshots from a previous UI version after the flow changed. Defeats: DET-CON-018. Bad: an article saying "Click Settings → Billing in the left sidebar" with a screenshot of the old layout, months after billing moved to a top-level page. Instead: re-verify steps and recapture screenshots in the release that changes the flow, or archive the article. Severity: BLOCK.
- **BAN-CX-024 — Restated support promises.** Banned: writing response-time or availability promises into article text ("We reply within 4 hours!"). Defeats: DET-CON-028. Bad: an article footer promising a 4-hour reply while the configured support hours deliver next-business-day replies. Instead: link to the single configured support-expectations page and state no promise in the article itself. Severity: BLOCK.
- **BAN-CX-025 — Generic filler answers.** Banned: articles that gesture at help without solving the problem ("Simply adjust your settings to fix this issue"). Defeats: DET-CON-006. Bad: "To resolve sync problems, just update your preferences and it should work seamlessly." Instead: give the exact steps, in order, with the current UI labels, ending in the human-support path. Severity: WARN.

## Gates

- **G-CX-021 — Top-questions walkthrough.** Verifies: CX-041, CX-046, CX-050. Check: take the five most common real support questions; as an unauthenticated visitor, answer each using only help-center search; assert the correct article is found and every link in it resolves. Pass: 5/5 questions answered from search alone. Fail: block the release; fix search terms, titles, or links first. Recorded in: progress.md.
- **G-CX-022 — UI-label and link audit (automated).** Verifies: CX-044, CX-050, CX-051. Check: run a link-check crawl over the whole center (`linkchecker` or the platform's built-in broken-link report) and diff every bolded UI label quoted in article steps against the current release's label inventory. Pass: zero broken links, zero labels absent from the current UI. Fail: block publication of the affected articles. Recorded in: progress.md.
- **G-CX-023 — Zero-result search review.** Verifies: CX-047. Check: export the help-search zero-result report for the review period; confirm each repeated query (≥3 occurrences) has a resulting action — new article, retitle, or added search terms — logged in progress.md. Pass: no repeated zero-result query unactioned. Fail: schedule the articles before the next release. Recorded in: progress.md.
- **G-CX-024 — Human-path check.** Verifies: CX-048. Check: open every published article and follow its end-of-article support path in a test session; assert it reaches a form, chat, or address that creates a ticket. Pass: 100% of articles end at a working human path. Fail: block; repair or unpublish the dead-ended articles. Recorded in: progress.md.
- **G-CX-025 — Stale-article sweep.** Verifies: CX-045, CX-052. Check: list all articles whose last-verified date predates the latest UI release touching their flow; assert each is re-verified (date updated after a live walkthrough) or archived. Pass: zero live articles stale past a flow-changing release. Fail: archive the stale articles until re-verified. Recorded in: progress.md.

## Anti-patterns

- **Mirror-of-the-app navigation.** The category tree copies the product's internal module names and admin structure, so customers must already know the product to find help. Catch it: try finding an article using only the words from the ticket that prompted it.
- **Screenshot walls.** Articles that are mostly annotated screenshots with almost no text — unsearchable, untranslatable, and silently wrong after any redesign. Catch it: if deleting the images leaves no followable steps, the article fails CX-044 in spirit.
- **The orphan launch set.** A batch of articles written once at launch and never revisited while the product changes around them. Catch it: sort by last-verified date; a long untouched tail is the pattern, caught by G-CX-025 only if someone runs it.
- **Deflection-first framing.** Articles written to keep users away from support ("Before contacting us, try everything below") rather than to solve the problem. Catch it: read the first line — if it argues instead of answering, rewrite it.
- **Duplicate answers drifting apart.** The same question answered in two articles that slowly diverge after edits. Catch it: search the center for the question's key phrase; more than one live answer means merge and redirect.

## Examples

- [Example 1 — Stale steps after a UI move](examples/example-1.md) — violates/corrects CX-044.
- [Example 2 — Article born from a zero-result search](examples/example-2.md) — violates/corrects CX-047.
- [Example 3 — Promise restated in an article footer](examples/example-3.md) — violates/corrects CX-049.

## Recall anchors

- No real question, no article.
- Steps a stranger can follow verbatim on today's UI, or it doesn't ship.
- A failed search is a work order, not a dead end.
- Every article ends at a human.
- Promises live in one configured place — link, never restate.

## Checklist

- [ ] Every new article traces to a real recurring question (CX-041).
- [ ] Article and category names use customer wording, hierarchy ≤3 levels (CX-043).
- [ ] Steps followed verbatim on the live product; screenshots current (CX-044, CX-051).
- [ ] Last-verified date set on every touched article (CX-045).
- [ ] Search tested with real customer phrasing, not titles (CX-046).
- [ ] Zero-result report reviewed and repeated queries actioned (CX-047).
- [ ] End-of-article human path followed and working (CX-048).
- [ ] No response-time or availability promise written into article text (CX-049).
