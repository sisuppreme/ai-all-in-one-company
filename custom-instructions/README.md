# Custom Instructions — Platform Notes

This folder holds one ready-to-paste instruction set per platform. Paste **one** file — the one for your platform. This README itself is never pasted anywhere; it records where each set lives on its platform, whether it persists, its size limit, and how to refresh it when the repo releases a new version.

All four sets encode the same repo-first protocol and are pinned to **OmniForge repo v1.2.0 (2026-11-23)**. As of v1.2.0 (the theme-library release), all four sets also carry the premium design standard: the frontend theme library is loaded before any website UI is built, the motion and scroll-experiences premium standard applies in full, and the standing design rules (system cursor only, reveals never leave content invisible, elements merged with content, smoothed scroll motion, `prefers-reduced-motion` honoured, "premium beyond premium" bar) are stated in each set. The repo URL in every set (https://github.com/sisuppreme/ai-all-in-one-company) is a placeholder until the repo is published; when the final URL is known, it changes in the repo first and the pasted copies are refreshed from the repo (see the update procedure below).

## Per-platform notes

### Google AI Studio — `ai-studio.md`

- **Where it lives:** the **System instructions** field of an AI Studio prompt (in the Run settings panel). The prompt, including its system instructions, is saved with the prompt; AI Studio prompts can be saved to Google Drive.
- **Persistence:** applies to every turn of that saved prompt. It does **not** carry into a new, separate prompt — reopen the saved prompt, or paste the instructions again.
- **Limit:** Google publishes no character limit for the system instructions field; the practical limit is the model's total token budget, which the instructions share with the conversation.
- **Fit:** the full repo-first protocol fits. This is the fullest of the four sets, and it is the file used verbatim in the Phase 6 single-agent proof run.

### Claude Code — `claude-code.md`

- **Where it lives:** in a `CLAUDE.md` file — the project root (`./CLAUDE.md`, shared with everyone on the project) or the user level (`~/.claude/CLAUDE.md`, applies to all of your projects).
- **Persistence:** Claude Code reads `CLAUDE.md` automatically at the start of every session, so the instructions persist across sessions for as long as the file is there.
- **Limit:** Anthropic publishes no hard character limit for `CLAUDE.md`. The file is loaded into context at session start, so every line costs context — keep it to the protocol, not a copy of the skills.
- **Fit:** the full repo-first protocol fits.

### Claude (chat / Projects) — `claude.md`

- **Where it lives:** a Claude Project's **custom instructions** (Project settings → Set project instructions). It can also be pasted at the start of a single chat, where it lasts only for that chat.
- **Persistence:** project instructions apply to every chat inside that project and persist until they are edited; they do not apply to chats outside the project.
- **Limit:** Anthropic does not publish a character limit for project custom instructions in its help documentation. The instructions are prepended to every conversation in the project, so they consume context on every turn — concise wins. (Third-party reports of specific caps conflict with each other; do not rely on them.)
- **Fit:** the full repo-first protocol fits.

### Generic agents — `generic.md`

- **Where it lives:** wherever the agent accepts standing instructions — a system prompt, a configuration or instructions file, or the first message of a session.
- **Persistence:** entirely platform-dependent. If the agent has no persistent instruction store, the set must be pasted again at the start of each session.
- **Limit:** no universal limit exists. The set is deliberately compact so it fits field-limited platforms; if a platform's field is too small even for `generic.md`, paste only the repo URL plus the one-line repo-first instruction ("Before starting any task, load this repository, read BOOTSTRAP.md and SKILLS_INDEX.md, and pull in the relevant skills") and keep `bundles/core.md` ready as the working fallback.

## Update procedure (repo §11)

The repo is versioned semantically (MAJOR.MINOR.PATCH) over its interface — skill paths, rule IDs, gate IDs, index fields, and bundle filenames:

**Agent-side self-update (since v1.1.0):** the manual refresh below is no longer the only line of defence against a stale pin. Every set now instructs the agent itself to fetch the repo fresh at the start of every task and every session, compare `VERSION` with the pin, and — when the repo is newer — adopt the repo's current files automatically and without asking permission: the current `BOOTSTRAP.md`, the skill set rediscovered from the current `SKILLS_INDEX.md` (so skills and playbooks added after the pin are found, not assumed away), and the current bundles. The agent tells the user once, briefly, that the repo has been updated and it is using the new files. On multi-session projects the check repeats each session; a mid-project repo change is noted in `progress.md` and adopted for work not yet done, without rewriting completed, gate-passed work unless a changed gate touches safety, legal, or Real Content. When the agent cannot fetch at all, it must say so, ask for the **current** `bundles/core.md` (plus the relevant playbook bundle), and warn that pasted content may be older than the repo — it never silently works from memory or an old paste. The manual refresh procedure below still applies to the pasted instruction text itself, so the instructions a platform holds match the release they were copied from:

- **MAJOR release** (a renamed or removed skill, a changed rule or gate ID, a changed index field) or **MINOR release** (a new skill, a new detection parameter, a new playbook): refresh every pasted copy. Open `custom-instructions/` at the new repo version, copy the file for your platform, and replace the pasted text wholesale; the version pin line inside the file already names the new version and date.
- **PATCH release** (wording fixes, claim corrections, example updates): refreshing is optional but recommended at the next convenient session.
- Before refreshing, check what changed in the repo's root `CHANGELOG.md` (top entry).
- Never hand-edit a pasted copy — always re-copy from the repo, so the pasted text and the repo cannot drift apart.
- If you work through the fallback (a pasted `bundles/core.md`), re-paste the regenerated core bundle from the new release at the same time — bundles are regenerated on every release.
