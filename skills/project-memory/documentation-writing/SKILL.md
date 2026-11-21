# documentation-writing

## Metadata

- **Owner department:** D10 Project & Memory (PM)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Diátaxis — https://diataxis.fr/ ; Google developer documentation style guide, timeless documentation — https://developers.google.com/style/timeless-documentation ; Documentation checks in CI — https://datadef.io/guides/en/docs-checks-in-ci ; Documentation as code — https://sourcegraph.com/blog/documentation-as-code
- **Depends on:** none — standalone: docs are written from the product and code itself, checked against the running system; this skill sets the standards the other doc skills follow rather than consuming their output. It feeds readme-writing, runbook-writing, and changelog.
- **Feeds into:** readme-writing, runbook-writing, changelog

## When to use / Do NOT use

- **Use when:** writing or revising any project documentation page — tutorial, how-to, reference, or explanation — setting a project's doc standards, or reviewing docs before a release.
- **Do NOT use when:** the artifact is the README (use readme-writing), an incident procedure (runbook-writing), a decision record (decision-logs), a changelog (changelog), or marketing and site copy (D9 copywriting).

## Rules

1. **PM-021 — One page, one Diátaxis mode.** Every page is exactly one of tutorial (learning), how-to (task), reference (facts), or explanation (background), and the mode is declared in the page's front matter. A draft serving two modes is split before it ships.
2. **PM-022 — Verify before you write.** Every documented feature, flag, command, default value, and behavior is checked against the actual system — run it, or read the code/config that implements it — before the page ships. Behavior you cannot verify is not documented; it is filed as an open question.
3. **PM-023 — Name the reader need first.** Before drafting, state the reader and the job the page does for them in one line at the top of the draft. No identifiable reader need, no page.
4. **PM-024 — Docs as code.** Documentation lives in the same repository as the code it describes, in plain-text markup, reviewed in the same pull-request flow, and published on merge — never in a separate wiki or document store that drifts from the code.
5. **PM-025 — Docs ship with the code change.** A behavior change and its documentation change land in the same change. When that is impossible, a tracked doc-gap issue is filed in the same change and linked from the changed code or release notes.
6. **PM-026 — Owner and review trigger on every page.** Front matter carries `owner` and `last_reviewed`. A page is reviewed when code in its area changes or when its freshness window (a project-policy parameter) expires, whichever comes first.
7. **PM-027 — The word list governs terminology.** Product, feature, and concept names match the project word list and naming list exactly. A term not in the word list is defined at first use or not used.
8. **PM-028 — Write timelessly.** Document the current state in the present tense. "Currently", "new", "latest", and "now" never stand in for a version: version-specific facts carry the version number ("In 2.4, …") or are not stated.
9. **PM-029 — Match voice to mode.** How-tos address the reader in the imperative ("Run the migration"); tutorials guide step by step with the expected result at each step; reference pages state facts without narrative or persuasion.
10. **PM-030 — Execute every code sample.** Each command, API call, and config block in a page is run verbatim against the current system before the page ships or changes. A sample that fails is a documentation bug with the same priority as a code bug.
11. **PM-031 — One canonical page per fact.** A fact lives on exactly one page; other pages link to it instead of copying it. Duplicated passages found in review are replaced by links in the same change.
12. **PM-032 — Complete front matter or no merge.** Every page carries `mode`, `owner`, and `last_reviewed` in front matter. A page missing any field fails G-PM-011 and does not merge.

## BAN list

- **BAN-PM-011 — Documenting an unverified feature.** Banned: writing instructions, flags, or behaviors from a ticket, plan, or assumption without checking them against the running system. Defeats: DET-CON-014. Bad: a how-to documents `backup --dry-run`, a flag the CLI does not have, and readers script against it. Instead: run the feature or read its implementation first (PM-022); document only what the system demonstrably does. Severity: BLOCK.
- **BAN-PM-012 — Scaffold and default text shipped as documentation.** Banned: publishing generator boilerplate, template prompts, or placeholder sections ("Add a description here", empty headed sections) as finished docs. Defeats: DET-CON-002. Bad: the setup guide ships with the template's "TODO: describe your project" paragraph under the Installation heading. Instead: write the real content for the slot or delete the section; an honest gap is a tracked issue, not filler. Severity: BLOCK.
- **BAN-PM-013 — Draft markers in published docs.** Banned: `TODO`, `FIXME`, "content to follow", or "coming soon" (undated) in any published page, heading, or metadata field. Defeats: DET-CON-004. Bad: the reference page for webhooks ends with "TODO: add payload examples" on the live docs site. Instead: keep markers in the repo's issue tracker; published pages contain only finished statements. Severity: WARN.
- **BAN-PM-014 — Time-anchored claims left to rot.** Banned: "new for 2026", "our latest release", or undated "coming soon" feature claims on evergreen pages. Defeats: DET-CON-018. Bad: the concepts page still announces "New in 2024: dark mode" two major versions later. Instead: state the fact with its version ("Dark mode, added in 1.8") and let the freshness gate (G-PM-014) retire stale claims. Severity: WARN.
- **BAN-PM-015 — Model-default register in docs.** Banned: dense AI filler vocabulary (delve, tapestry, realm, "in today's fast-paced world", "it's important to note") standing in for technical content. Defeats: DET-CON-007. Bad: an explanation page opens with two paragraphs of elevated filler before naming the component it explains. Instead: cut to the subject; every paragraph names a component, mechanism, or fact the reader can check. Severity: WARN.

## Gates

- **G-PM-011 — Structure and front-matter lint.** Verifies: PM-021, PM-026, PM-032. Check: automated — run `npx markdownlint-cli "docs/**/*.md"` and a front-matter script asserting every page has `mode`, `owner`, and `last_reviewed`; the same commands run locally as a script or in CI. Pass: exit 0 and zero pages missing a field. Fail: block merge. Recorded in: progress.md.
- **G-PM-012 — Link check.** Verifies: PM-031. Check: automated — run `lychee docs/ README.md` for internal links on every change; external URLs on a scheduled run. Pass: zero broken internal links. Fail: block merge. Recorded in: progress.md.
- **G-PM-013 — Style and terminology lint.** Verifies: PM-027, PM-028. Check: automated — run `vale --minAlertLevel=error docs/` with the project's word list and timeless-writing rules (flagging "currently/latest/new" as version substitutes) configured as the Vale style. Pass: zero error-level alerts. Fail: block merge. Recorded in: progress.md.
- **G-PM-014 — Freshness gate.** Verifies: PM-026. Check: automated — a script reads `last_reviewed` from every page's front matter and fails any page older than the project's review window (policy parameter, set per project tier). Pass: no page past its window. Fail: block release until the page is reviewed and re-dated or the window is changed by a recorded decision. Recorded in: progress.md.
- **G-PM-015 — Reader task test.** Verifies: PM-022, PM-023, PM-030. Check: manual — a reader unfamiliar with the material completes one learn, one task, and one lookup using only the docs, with no outside help. Pass: all three tasks completed; every stall is filed as a documentation bug. Fail: rework the failing pages and retest before the docs ship. Recorded in: progress.md.

## Anti-patterns

- **The sprawling mega-page.** One page trying to be tutorial, manual, and rationale at once, growing by accretion because splitting feels like extra work. Catch it: if you can name two reader needs on one page, split it now (PM-021).
- **The changelog dump.** Release notes or commit messages pasted in as documentation — a record of what changed, mistaken for an explanation of how things work. Catch it: if the page reads as a dated list of changes, it belongs in changelog, not the docs tree.
- **The orphan page.** A correct page that no index, navigation, or other page links to, so no reader ever finds it and it rots unreviewed. Catch it: after writing, follow your own link to the page from the docs index; if you cannot, the page is not finished.
- **Copy-paste twins.** The same procedure pasted into several pages "for convenience"; fixes land in one copy and the others become quietly wrong. Catch it: search the docs for a distinctive sentence from any procedure you edit — every hit beyond the canonical page is a link waiting to replace a copy (PM-031).

## Examples

- [Example 1 — One page, two jobs](examples/example-1.md) — violates/corrects PM-021.
- [Example 2 — The flag that did not exist](examples/example-2.md) — violates/corrects PM-022.
- [Example 3 — "New and latest" forever](examples/example-3.md) — violates/corrects PM-028.

## Recall anchors

- One page, one Diátaxis mode, one reader need.
- If you did not run it, do not document it.
- Docs ship with the code change — or the gap is a tracked issue.
- No "new", "latest", "currently": state the version or the fact.
- Every page: mode, owner, last_reviewed — or it does not merge.

## Checklist

- [ ] The page declares exactly one Diátaxis mode in its front matter (PM-021).
- [ ] Every documented behavior was verified against the actual system (PM-022).
- [ ] Owner and last_reviewed are set, and the review trigger is known (PM-026).
- [ ] All terms match the project word list; any new term is defined at first use (PM-027).
- [ ] No time-anchored word stands in for a version number (PM-028).
- [ ] Every code sample was executed verbatim and passed (PM-030).
- [ ] markdownlint, lychee, and Vale error-level checks pass locally (G-PM-011, G-PM-012, G-PM-013).
- [ ] The doc change ships with its code change, or a doc-gap issue is filed and linked (PM-025).
