# OmniForge — Repo-First Protocol (Claude Code)

Add this file's contents to the project's `CLAUDE.md` (or paste it at the start of a session) whenever a project is built with the OmniForge skill repository. It is a procedure to run at the start of every task, not background reading.

## Repository

- Repo: https://github.com/sisuppreme/ai-all-in-one-company (placeholder URL until the repo is published — use this exact address until the user provides the final one).
- Pinned version: OmniForge repo v1.1.0 (2026-11-21).

## At the start of every task

1. Clone the repo, or `git pull` your existing clone, at the start of every task — always work from the repo's current state, never from a stale local copy or from memory. Read `VERSION` and the top entry of the repo's root `CHANGELOG.md` and compare with the pin above. If the repo's version is **newer** than the pin, the repo wins: these instructions are stale, but do not stop and do not ask permission — follow the repo's current `BOOTSTRAP.md`, rebuild your picture of the skill set from the current `SKILLS_INDEX.md` (new skills and playbooks may exist since the pin; discover them from the index, never assume the set named anywhere in these instructions is complete), load bundles from the current repo, and tell the user once, briefly, that the repo has been updated to the new version and you are using the new files. If the version matches the pin or is older, proceed normally; if the repo is more than 6 months old, warn the user and re-verify tool and API claims against live sources. Note the version in the project's `progress.md` (step 5).
2. Read `BOOTSTRAP.md` in full — it is the entry point.
3. Scan `SKILLS_INDEX.md` by department section and Keywords; identify the task's departments. Do not read every entry.
4. Load only the relevant skills fully, plus the always-on core: `project-templates` + `progress-tracking` (D10), `secrets-management` (D7), `qa-gates` (D8). If the task matches a playbook type, load that playbook bundle from `bundles/`; otherwise load the matching department bundles. Honor each skill's `Depends on` field. Never load `bundles/ALL_SKILLS.md` whole — it is a human reference artifact only.
5. Docs before code: create `requirements.md`, `stack.md`, `progress.md`, `fact-sheet.md` first — no code before these exist. Record the repo version at the top of `progress.md`. Vague requirements bounce back to the user as questions.
6. Run the loaded skills' gates as you work; record every gate result in `progress.md` with evidence (command output, test result, screenshot). A gate without evidence is not passed. If two loaded skills conflict, apply the repo's precedence order (§5.7) and log the conflict in the project's `DECISIONS.md`.
7. Keep `progress.md` updated. Stop for user approval after requirements, before deployment, and before go-live.

Multi-session projects: the step 1 pull and version check runs at the start of every session. If the repo changed mid-project, note it in `progress.md` and adopt new or changed skills for work not yet done; do not retroactively rewrite completed, gate-passed work unless a changed gate affects safety, legal, or Real Content, in which case re-check the affected work against the new gate.

Small-task fast path: a single-file fix or one-skill task skips the full bootstrap — load the one skill and its gates, update `progress.md`.

## Fallback

If the repo cannot be fetched, say so explicitly — never silently rely on a stale clone, on memory, or on an old paste. Ask the user to paste the **current** `bundles/core.md` from the repo (plus the playbook bundle for the task, if one applies), warn that pasted content may be older than the repo itself, proceed with the pasted bundles only, and flag the gap in `progress.md`. Do not improvise unloaded skills.

## Rules that always apply

- You work alone: never claim a multi-agent handoff is needed or wait for another agent; department labels are roles you play sequentially yourself.
- Real Content Rule: never invent content, data, people, reviews, statistics, or functionality — if something is not verified, say so.
- Never ask for secrets in chat; secrets go in the project's environment or secret store and are referenced by name only (see the repo's `secrets-management` skill).
