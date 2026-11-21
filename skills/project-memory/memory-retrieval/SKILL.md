# memory-retrieval

## Metadata

- **Owner department:** D10 Project & Memory (PM)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Docs as code (Sourcegraph) — https://sourcegraph.com/blog/documentation-as-code ; GitHub Docs, creating a default community health file — https://docs.github.com/en/enterprise-cloud@latest/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file
- **Depends on:** project-templates, readme-writing, decision-logs
- **Feeds into:** handover, progress-tracking

## When to use / Do NOT use

- **Use when:** designing or auditing how a project's own record is found again — canonical locations for facts, index pages, file and heading naming, superseded-document handling, and the tests that prove a fresh reader (or the single agent returning later) can retrieve what the project knows using only the repo.
- **Do NOT use when:** the task is writing the documents themselves (documentation-writing, readme-writing, runbook-writing own content), recording a decision (decision-logs), or transferring the project (handover — this skill supplies handover's retrieval acceptance tests, not the transfer process).

## Rules

1. **PM-161 — One canonical home per fact.** Every fact (version, database choice, price, escalation path, status) is stated in exactly one file. Every other document that needs it links to that file; it never restates the value.
2. **PM-162 — Fixed names and locations.** Mandated files use the set's fixed names and paths. A project never renames, moves, or re-extensions a mandated file to suit local taste.
3. **PM-163 — Two hops maximum.** Every mandated file is reachable from README.md or the docs index in at most two link hops. A file no index path reaches is treated as missing.
4. **PM-164 — Indexes link, never restate.** DECISIONS.md links every ADR; the README and docs index link every mandated file. An index entry is a title plus a link — copying the target's content into the index creates a second home and violates PM-161.
5. **PM-165 — Duplicates become links on sight.** When a duplicated fact is noticed, the non-canonical copy is replaced by a link to the canonical home in the same change — not filed for later cleanup.
6. **PM-166 — Superseded means marked, never silently deleted.** A replaced document stays in place with a SUPERSEDED banner naming and linking its replacement. Deleting or overwriting it without the marker is forbidden, so an old answer is always visibly old.
7. **PM-167 — Guessable terms.** File names, headings, and vocabulary follow the set's conventions and the project word list, so a searcher can guess the term that will hit (decision → DECISIONS.md and `docs/adr/`, incident → postmortem and runbook). One concept, one term, everywhere.
8. **PM-168 — Repo-only retrieval.** Retrieval must work with the repo alone: plain-text search (`grep`, `git log`) over consistently named files, plus the index pages. No hosted search service, wiki, or chat history may be a required step in finding a project fact.
9. **PM-169 — The project owns a query list.** Every project maintains `retrieval-queries.md`: at least 10 known-fact questions a newcomer would actually ask (which database, current version, on-call escalation, how to deploy), each naming the canonical file that answers it. It is created at project start and extended whenever a new class of fact appears.
10. **PM-170 — Test with the project's own questions.** The scripted known-fact search runs PM-169's list, never a generic list shipped with a template — a generic list tests the template's facts, not the project's.
11. **PM-171 — Crawl on cadence.** The orphan crawl (G-PM-081) and the known-fact search (G-PM-082) run at every release or work-cycle boundary, and their results are recorded in progress.md like any other gate.
12. **PM-172 — Change the home, then sweep.** When a fact changes, only its canonical home is edited; before the change closes, a repo-wide search for the old value returns no live copies (hits inside marked superseded documents and the changelog are the only permitted remains).

## BAN list

- **BAN-PM-081 — The copied fact.** Banned: pasting a fact's value into a second document instead of linking to its canonical home. Defeats: DET-CON-015. Bad: the supported database version is stated in stack.md, the README, and a runbook; stack.md is updated and the other two keep answering with the old version. Instead: state the fact once in its canonical home and link to it from every other document (PM-161). Severity: BLOCK.
- **BAN-PM-082 — The vanished predecessor.** Banned: deleting or silently overwriting a superseded document so no trace of the replacement relationship remains. Defeats: DET-CON-018. Bad: the old deployment guide is deleted when the new one lands; a month later a cached copy circulates and nobody can tell it is stale. Instead: keep the document, add a SUPERSEDED banner, and link to its replacement (PM-166). Severity: BLOCK.
- **BAN-PM-083 — The renamed mandated file.** Banned: giving a mandated file a project-specific name or location (`our-decisions.md`, `docs/final/ARCHITECTURE-v2.md`). Defeats: DET-CON-017. Bad: decisions live in `team-notes.md`, so the standard search for DECISIONS.md returns nothing and the project's rationale reads as absent. Instead: use the set's fixed name and path; put project flavor in the content, not the filename (PM-162). Severity: WARN.
- **BAN-PM-084 — The mirrored document.** Banned: copying a whole document into additional folders "for convenience" (the runbook duplicated under docs/, ops/, and the service folder). Defeats: DET-CON-025. Bad: three identical runbooks exist; the fix lands in one and the other two keep prescribing the broken procedure. Instead: keep one canonical document and link to it from each place that needs it (PM-161, PM-165). Severity: BLOCK.

## Gates

- **G-PM-081 — Orphan crawl.** Verifies: PM-163, PM-164. Check: automated — starting at README.md and the docs index, follow Markdown links to depth 2 and diff the reached set against the mandated file manifest: `grep -rhoE '\]\([^)]+\.md\)' README.md docs/ | sort -u`, compared with the manifest list. Pass: every mandated file is reached; zero orphans. Fail: block shipment until the file is linked or the manifest is corrected. Recorded in: progress.md.
- **G-PM-082 — Known-fact search test.** Verifies: PM-169, PM-170. Check: automated — for each row of `retrieval-queries.md`, run `grep -ril '<query term>' --include='*.md' .` and confirm the row's named canonical file appears among the hits. Pass: 10 of 10 queries return their canonical file. Fail: fix naming, headings, or the canonical home — never edit the query list to match a broken layout. Recorded in: progress.md.
- **G-PM-083 — Duplicate-value sweep.** Verifies: PM-161, PM-172. Check: automated — sample five load-bearing facts from their canonical homes (current version, database, escalation path, deploy command, support promise) and `grep -rn '<value>' --include='*.md' .`; each value must appear definitionally in exactly one file, elsewhere only inside links, the changelog, or marked superseded documents. Pass: no live second home for any sampled fact. Fail: replace the copies with links (PM-165) and re-run. Recorded in: progress.md.
- **G-PM-084 — Superseded-marker check.** Verifies: PM-166. Check: automated — every file the index or DECISIONS.md marks superseded carries a SUPERSEDED banner linking its replacement: `grep -L 'SUPERSEDED' <superseded files>` returns nothing; `git log --diff-filter=D --name-only` shows no mandated document deleted without a superseding entry. Pass: both checks clean. Fail: restore and mark the document before shipping. Recorded in: progress.md.
- **G-PM-085 — Fresh-reader retrieval test.** Verifies: PM-167, PM-168. Check: manual — a reader or agent with no prior project context answers five questions drawn from `retrieval-queries.md` using only the repo (no asking the author, no chat history), timed. Pass: all five answered correctly from canonical files within the project's agreed time budget. Fail: each miss is a retrieval defect — fix the index, name, or canonical home, then retest. Recorded in: progress.md.

## Anti-patterns

- **Index rot.** The index pages exist and pass a glance, but still list the file set as it stood at kickoff — new mandated files were added and never linked. Catch it: diff index link targets against the manifest (G-PM-081), not against last month's index.
- **Synonym scatter.** The same concept is filed under different terms in different documents — deploy, release, ship, rollout — so any single search term misses copies. Catch it: search each concept by its word-list term only; any hit under a synonym is a PM-167 defect.
- **Deep nesting.** Mandated files are buried under project-specific subfolders (`docs/final/v2/real/`), so paths cannot be guessed and two-hop reachability quietly breaks. Catch it: if you cannot predict a mandated file's path from the convention, the layout is wrong.
- **The chat-only answer.** A retrieval question gets answered from conversation memory, everyone moves on, and the repo still cannot answer it. Catch it: if a human or agent had to ask, the repo failed — land the fix in the files, not just in the reply.

## Examples

- [Example 1 — The database version in three places](examples/example-1.md) — corrects PM-161.
- [Example 2 — The deployment guide that vanished](examples/example-2.md) — corrects PM-166.
- [Example 3 — The template's retrieval test](examples/example-3.md) — corrects PM-169.

## Recall anchors

- One fact, one home; everything else is a link.
- If it is not reachable in two hops, it does not exist.
- Mark superseded — never silently delete.
- Test retrieval with the project's own questions.
- If grep cannot find it, the project does not know it.

## Checklist

- [ ] Every sampled fact has exactly one canonical home; all other mentions are links (PM-161, G-PM-083).
- [ ] All mandated files use the set's fixed names and paths (PM-162).
- [ ] Orphan crawl passes: zero mandated files unreachable within two hops (G-PM-081).
- [ ] `retrieval-queries.md` exists with ≥10 project questions, each naming its canonical file (PM-169).
- [ ] Known-fact search test passes 10/10 against the project's own list (G-PM-082).
- [ ] Every superseded document carries a SUPERSEDED banner linking its replacement (PM-166, G-PM-084).
- [ ] Fresh-reader test passed and recorded in progress.md (G-PM-085).
