# personas-jtbd

## Metadata

- **Owner department:** D1 Product & Requirements (PR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Christensen Institute, "What is Jobs to Be Done Theory?" — https://www.christenseninstitute.org/video/what-is-jobs-to-be-done-theory/ ; Harvard Business School Online, "The Jobs to Be Done Framework" — https://online.hbs.edu/blog/post/jobs-to-be-done-examples
- **Depends on:** user-research
- **Feeds into:** user-stories, requirements-writing, roadmapping

## When to use / Do NOT use

- **Use when:** research findings must be turned into a working set of personas; a trade-off discussion needs a named user and job to reason about; a story needs its role.
- **Do NOT use when:** no research findings exist yet (go to user-research first, or label the persona HYPOTHETICAL under PR-048). Never use a persona as public proof — testimonials and customer claims belong to real-content, sourced from real customers only.

## Rules

1. **PR-041 — Small set, one per job cluster.** The persona set holds 3–5 personas, one per distinct job cluster. Two personas with the same job are merged into one.
2. **PR-042 — JTBD format is exact.** Every persona's core need is written as: "When [situation], I want [motivation], so I can [expected outcome]." No other phrasing carries the job.
3. **PR-043 — Jobs name progress, not features.** The job statement names a circumstance and the progress sought. It never names a product feature, a screen, or a demographic as the job.
4. **PR-044 — Demographics earn their place.** A demographic attribute appears on a persona only where it changes the job or its constraints, and it cites the finding that shows the effect.
5. **PR-045 — Evidence-linked and versioned.** Each persona carries its evidence date and links to the finding IDs it was built from. Any change to the persona bumps its version.
6. **PR-046 — Forces before features.** For each persona's job, the forces of progress are analyzed — push of the current situation, pull of the new solution, anxiety about change, habit of the present — before any feature is proposed from that persona.
7. **PR-047 — Personas are cited in trade-offs.** A trade-off decision names the persona(s) and job(s) it serves. A decision naming neither is returned for rework.
8. **PR-048 — Real basis or labeled construct.** A persona built without research findings is labeled HYPOTHETICAL at the top of its card, holds no citation rights in requirements or copy, and is replaced or removed at the first real study.
9. **PR-049 — Representative tasks are observed tasks.** Each persona lists tasks drawn from research findings, phrased as the user phrases them — not tasks invented to match planned features.
10. **PR-050 — Retire dead personas.** A persona whose job cluster no longer appears in current research is archived with a date, not silently kept in the active set.

## BAN list

- **BAN-PR-021 — Stock-photo biography.** Banned: persona detail (name, age, hobbies, photo) with no research finding behind it. Defeats: DET-CON-019. Bad: "Meet Sarah, 34, marketing manager, loves yoga" invented in one sitting to fill a template. Instead: build the persona from clustered findings and omit any biography no finding supports. Severity: BLOCK.
- **BAN-PR-022 — Feature stated as the job.** Banned: a JTBD statement whose "I want" is a product feature. Defeats: DET-CON-028. Bad: "When I open the app, I want a dashboard, so I can see the dashboard." Instead: "When the morning shift starts, I want to know which orders are late, so I can reassign drivers before customers call." Severity: BLOCK.
- **BAN-PR-023 — Demographic-only persona.** Banned: segmenting personas by demographics alone ("Millennial moms", "Gen-Z users") with no distinct job behind the split. Defeats: DET-CON-011. Bad: three personas that differ only in age band, each asserting what that age band "wants" with no study cited. Instead: cluster by job; add demographics only where a finding shows they change the job (PR-044). Severity: WARN.
- **BAN-PR-024 — Persona quoted as proof.** Banned: using a persona as customer evidence in public copy, decks, or sales material. Defeats: DET-CON-010. Bad: the landing page quotes the persona — "Sarah loves our exports!" — as a testimonial. Instead: testimonials come only from real customers with source records, handled by real-content; personas never appear in public copy. Severity: BLOCK.

## Gates

- **G-PR-021 — JTBD format lint.** Verifies: PR-042. Check: automated — run a regex over every JTBD statement confirming it matches the "When …, I want …, so I can …" pattern with all three parts non-empty. Pass: 100% match. Fail: block persona sign-off. Recorded in: progress.md.
- **G-PR-022 — Evidence-link check.** Verifies: PR-045, PR-048. Check: automated — run a script confirming every persona carries at least one finding link that resolves in the research file, or carries the HYPOTHETICAL label. Pass: 100% of personas qualify one way or the other. Fail: block persona sign-off. Recorded in: progress.md.
- **G-PR-023 — Job-distinctness review.** Verifies: PR-041. Check: manual — read all job statements side by side and confirm each names a different job. Pass: no two jobs are interchangeable. Fail: merge the duplicates and rework the set. Recorded in: progress.md.
- **G-PR-024 — Forces completeness.** Verifies: PR-046. Check: manual — for each persona, confirm the forces section names push, pull, anxiety, and habit, each with a finding reference. Pass: all four present for every persona. Fail: warn, and block any feature proposal drawn from an incomplete persona. Recorded in: progress.md.

## Anti-patterns

- **Persona sprawl.** Nine personas, most differing only in age or city. Catch it: list the jobs in one column; if jobs repeat, the set is sprawl, whatever the cards look like.
- **The composite friend.** One persona stitched from every finding until it describes no actual person. Catch it: check that each attribute resolves to findings about the same job cluster, not the whole research file.
- **Frozen personas.** Version 1.0 personas still driving decisions two studies later. Catch it: compare persona evidence dates against the latest study date; a gap means the set is stale.
- **Persona as decoration.** Personas exist in a document that no decision ever cites. Catch it: search recent decision records for persona names; zero hits means the set is wallpaper and discovery is running on instinct.

## Examples

- [Example 1 — Rewriting a feature as a job](examples/example-1.md) — corrects PR-042, PR-043.
- [Example 2 — Building a persona from findings instead of biography](examples/example-2.md) — corrects PR-045, PR-049.
- [Example 3 — Forces of progress before a feature proposal](examples/example-3.md) — corrects PR-046.

## Recall anchors

- One persona per job cluster, three to five in total.
- When / I want / so I can — no other phrasing carries the job.
- Demographics appear only where they change the job.
- Forces before features.
- A persona is a reasoning tool, never public proof.

## Checklist

- [ ] The set holds 3–5 personas, one per distinct job (G-PR-023).
- [ ] Every JTBD statement passes the format lint (G-PR-021).
- [ ] Every persona carries finding links or the HYPOTHETICAL label (G-PR-022).
- [ ] No demographic appears without a finding showing it changes the job (PR-044).
- [ ] Push, pull, anxiety, and habit are recorded for every persona (G-PR-024).
- [ ] Recent trade-off decisions cite personas by name (PR-047).
- [ ] No persona text appears in any public-facing artifact (BAN-PR-024).
