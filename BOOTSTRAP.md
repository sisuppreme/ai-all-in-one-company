# BOOTSTRAP.md — Start Here (Repo-First Protocol)

Any agent given this repository: complete these steps **before doing anything else**.

## The protocol

0. Read `VERSION` and the top entry of this repo's root `CHANGELOG.md`; note each loaded skill's last-verified date. If the repo version is over 6 months old, warn the user and re-check tool claims against live sources. Do not write anything yet.
1. Read this file (BOOTSTRAP.md) in full.
2. Scan `SKILLS_INDEX.md` — department sections first — to identify the task's departments. Do not read every entry in the index.
3. Load in stages — the staged route is the default, not an optimization. Stage 1: `bundles/core.md` (this protocol plus the always-on core). Stage 2, playbook tasks: the playbook's bundle from `bundles/` — it is the default complete load for the walk: the playbook, its routed skills' rules and checklists, and a digest of every cited gate's check and pass criteria. Do not load department bundles or full skills alongside it by default. Stage 3, only where a step needs what a bundle omits (examples, anti-patterns, a gate's full procedure): load that one skill in full. Where no playbook bundle applies, load **only the relevant skills fully**, plus the always-on core: `project-templates` and `progress-tracking` (D10), `secrets-management` (D7), `qa-gates` (D8). Honor each skill's Depends-on field.
4. Create the project docs FIRST — `requirements.md`, `stack.md`, `progress.md`, `fact-sheet.md` — no code before docs. Record the repo version + changelog entry at the top of `progress.md`, and verify the four docs exist before writing any code. The project type's manifest (`templates/mandated-manifest-<type>.txt`) governs the full file set: these four docs and each playbook's "docs to write first" are starting subsets, not the whole set — generate the full manifest set at scaffold time, and record any file that does not apply as not-applicable with a reason in the generation record (PM-001, PM-005). Gate G-PM-001 is the manifest diff that verifies the generated set against that file (see `project-templates`); it is a generation check, not a docs-exist self-check. `requirements.md` must state the goal, audience, key features, and acceptance criteria before design starts; vague requirements bounce back to the user.
5. Follow the loaded skills' gates at every step. After each phase, re-read the gate criteria, record a written pass/fail per criterion in `progress.md`, and run every scripted check the skill provides. A gate pass must cite evidence (command output, test result, or screenshot) in `progress.md`; a gate passed without evidence is not passed.
6. Update `progress.md` as work proceeds.

## Routing rule

- Task type matches a playbook → load that playbook's bundle from `bundles/`.
- No playbook match → match task keywords against the index Keywords field → identify the departments → load those department bundles.
- No match at all → load `bundles/core.md` and ask the user.

## Fetching and fallback

- Fetch the repo via git clone, GitHub raw URLs, or your file-fetch tool.
- If the repo cannot be fetched, ask the user to paste `bundles/core.md` and proceed with the core only, flagging the gap in `progress.md`.

## Hard rules

- **Real Content Rule:** every fact, figure, name, and claim in the output must be real and sourced — never invent data, testimonials, statistics, or functionality.
- **Never load `bundles/ALL_SKILLS.md` whole** — it is a reference/download artifact for humans and offline search only. Use `bundles/` or `SKILLS_INDEX.md`.
- **Small-task fast path:** a single-file fix or one-skill task skips the full bootstrap — load the one skill + its gates and update `progress.md`.
- **Approval points:** the user approves (1) `requirements.md` + the estimate after requirements, (2) the deploy target + cost before deployment, (3) the live switch before go-live. Get approval before provisioning anything above the estimate; agree a monthly cost cap upfront. A decision already recorded in the commissioning brief or in `requirements.md` counts as the approval for its point — do not re-ask what the brief already answers. Where no user is reachable (an unattended run), do not halt at an approval point: follow the §6.3 stuck protocol (`docs/TROUBLESHOOTING.md`) — log-and-continue (step 3), then the safe defaults (step 4c), subject to the never list (step 5) — and record the substitution (the decision taken, its basis, and that no user was reachable) in `progress.md`. The same rule applies at every playbook ◆ / stop-and-ask point.

## Precedence — when two skills disagree

Higher rank wins; log every conflict in the project's `DECISIONS.md`.

1. Security (D7), incl. D17 AI-safety rules
2. Legal / privacy (D14), incl. D16 clone-ethics
3. Real Content Rule — no fakes, ever
4. QA gates (D8, process gates only)
5. Accessibility (D13)
6. Requirements / scope (D1)
7. Architecture (D2)
8. Data integrity (D5)
9. Backend correctness (D4)
10. Production / deployability (D6)
11. Payments / integrations correctness (D11)
12. Performance (D12)
13. AI features (D17)
14. Content / SEO (D9)
15. Design / beauty (D3)
16. Clone fidelity (D16)
17. Customer experience (D18)
18. DX / maintenance (D15)
19. Project memory / docs (D10)

Tie rule: within one rank, the more specific skill wins; if still tied, ask the user and log the conflict. D8's gates inherit the rank of the department whose requirement they enforce; rank 4 covers only D8's own process gates. Precedence never excuses skipping a gate — when a higher-ranked rule conflicts with a gate, re-run the gate's check against the higher rule's requirement; do not skip it.

## When you are stuck

Follow the stuck protocol in `docs/TROUBLESHOOTING.md`. Never invent data, skip a gate, or silently drop a requirement to get unstuck.
