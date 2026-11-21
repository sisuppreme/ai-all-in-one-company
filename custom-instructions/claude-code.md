# OmniForge — Repo-First Protocol (Claude Code)

Add this file's contents to the project's `CLAUDE.md` (or paste it at the start of a session) whenever a project is built with the OmniForge skill repository. It is a procedure to run at the start of every task, not background reading.

## Repository

- Repo: https://github.com/sisuppreme/ai-all-in-one-company (placeholder URL until the repo is published — use this exact address until the user provides the final one).
- Pinned version: OmniForge repo v1.0.0 (2026-11-21).

## At the start of every task

1. Clone or open the repo. Read `VERSION` and the top entry of the repo's root `CHANGELOG.md`; if the version differs from the pin above, tell the user these instructions are stale. Note the version in the project's `progress.md` (step 5).
2. Read `BOOTSTRAP.md` in full — it is the entry point.
3. Scan `SKILLS_INDEX.md` by department section and Keywords; identify the task's departments. Do not read every entry.
4. Load only the relevant skills fully, plus the always-on core: `project-templates` + `progress-tracking` (D10), `secrets-management` (D7), `qa-gates` (D8). If the task matches a playbook type, load that playbook bundle from `bundles/`; otherwise load the matching department bundles. Honor each skill's `Depends on` field. Never load `bundles/ALL_SKILLS.md` whole — it is a human reference artifact only.
5. Docs before code: create `requirements.md`, `stack.md`, `progress.md`, `fact-sheet.md` first — no code before these exist. Record the repo version at the top of `progress.md`. Vague requirements bounce back to the user as questions.
6. Run the loaded skills' gates as you work; record every gate result in `progress.md` with evidence (command output, test result, screenshot). A gate without evidence is not passed. If two loaded skills conflict, apply the repo's precedence order (§5.7) and log the conflict in the project's `DECISIONS.md`.
7. Keep `progress.md` updated. Stop for user approval after requirements, before deployment, and before go-live.

Small-task fast path: a single-file fix or one-skill task skips the full bootstrap — load the one skill and its gates, update `progress.md`.

## Fallback

If the repo cannot be fetched, ask the user to paste `bundles/core.md`, proceed with the core bundle only, and flag the gap in `progress.md`. Do not improvise unloaded skills.

## Rules that always apply

- You work alone: never claim a multi-agent handoff is needed or wait for another agent; department labels are roles you play sequentially yourself.
- Real Content Rule: never invent content, data, people, reviews, statistics, or functionality — if something is not verified, say so.
- Never ask for secrets in chat; secrets go in the project's environment or secret store and are referenced by name only (see the repo's `secrets-management` skill).
