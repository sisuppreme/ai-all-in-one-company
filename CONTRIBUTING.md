# Contributing to This Repository

This file governs contributions to **this repository** — the skill system itself (skills, detection parameters, playbooks, bundles, gates, docs). It is not a template for projects built with the repo; per-project files live in `templates/`.

Every contribution is a change to a system that a single agent must be able to consume alone. If a change only makes sense with a team of humans coordinating around it, it does not belong here.

## Before you start

- Read `BOOTSTRAP.md` and the relevant section of `SKILLS_INDEX.md` so you are working from the current catalog, not from memory.
- Check `docs/DECISIONS.md` for recorded decisions that constrain your change. A change that contradicts a recorded decision needs a new decision entry, not a silent override.
- File or reference an issue for the change (see "Issues" below). Gap reports, bug reports, and skill requests each have a template in `.github/ISSUE_TEMPLATE/`.

## Skill format (mandatory, no exceptions)

Every skill is a folder under `skills/<department-slug>/<skill-name>/` containing `SKILL.md` plus an `examples/` subfolder. `SKILL.md` follows the mandatory section template, in this exact order:

`# <skill-name>` / `## Metadata` / `## When to use / Do NOT use` / `## Rules` / `## BAN list` / `## Gates` / `## Anti-patterns` / `## Examples` / `## Recall anchors` / `## Checklist`

The authoritative template, with per-section drafting rules, is **`templates/SKILL_TEMPLATE.md`** — start every new skill from it. Key constraints:

- **Length cap:** no `SKILL.md` exceeds 400 lines / ~5,000 words. A skill that needs more is split into a core skill plus sub-skills, each independently loadable, with the split recorded in the index.
- **Rules:** numbered, each with an ID (see "Registry discipline"). A rule must be verifiable — if a reviewer cannot check whether it was followed, rewrite it until they can.
- **BAN entries:** each carries an ID, the banned pattern in one line, the DET parameter it defeats, a bad example, the correct replacement (`Instead:`), and a severity (BLOCK or WARN). An entry without a DET reference and a replacement fails validation. An item appears in the BAN list **or** in Anti-patterns, never both.
- **Gates:** each specifies a gate ID, the rule IDs it verifies, the exact check, the pass criterion, the fail action, and that the result is recorded in `progress.md`. Every skill ships at least 3 gates, at least 1 of them automated where the domain permits.
- **Examples:** at least 3 files in `examples/`, each with `## Before` / `## After` and a one-line note naming the rule ID it demonstrates. Code examples must be complete and runnable as written.
- **Recall anchors:** at most 5 one-line reminders.
- **Metadata:** owner department, skill version (semver), date last verified, source links (real URLs only — never invent a tool, API, statistic, or source), Depends on, Feeds into.

## Registry discipline

All rule, gate, and BAN IDs are assigned in **`docs/RULE_ID_REGISTRY.md`** before use. The rules are absolute:

- IDs are unique repo-wide. Within a department, each skill owns a fixed block (rules: 20 per skill, gates: 10 per skill, BAN entries: 10 per skill), assigned in catalog order.
- **Renumbering is forbidden.** A deprecated ID is retired, never reused.
- A skill that exhausts its block requests a registry amendment recorded in `docs/DECISIONS.md`. It never borrows a neighbour's numbers.
- Gates cite the rule IDs they verify; playbooks cite gate IDs that actually exist in the skills. A citation to a non-existent ID is a defect.

## DET citation honesty

A BAN entry may cite a detection parameter (`DET-<FAMILY>-<NNN>`) only when that parameter's defined signal semantically matches the banned pattern. Two honest alternatives exist when it does not:

- If a different existing parameter matches semantically, cite that one.
- If no DET parameter names the signal, write exactly: `Defeats: DET-NONE — no DET parameter names this signal; governed by <rule IDs>`.

Never cite a nearest-match parameter as if it were exact. Fake traceability is worse than an admitted gap: a gap can be routed (file a gap report), a fake citation silently misleads every future detection pass.

## After changing any skill

1. **Validate.** Run:

   ```bash
   python3 scripts/validate-skills.py
   ```

   It must report ALL PASS before the change is submitted. It checks section presence and order, the 400-line cap, ID placement inside registry blocks and repo-wide uniqueness, gate counts, BAN DET references and replacements, example files, and recall-anchor counts. If validation fails because of your change, fix the change — never edit the validator to make it pass.

2. **Regenerate the bundles.** Bundles under `bundles/` are generated artifacts, never hand-edited:

   ```bash
   python3 scripts/build-bundles.py
   ```

   A bundle whose source skills changed without regeneration is a ship-blocking defect.

3. **Regenerate the index.** `SKILLS_INDEX.md` is generated from skill metadata by `scripts/build-index.py`, never hand-maintained. Re-run it so paths, sizes, and dependency fields stay correct.

4. **Record the release.** If the change is part of a release, update the repo-root `CHANGELOG.md` and follow the versioning rules: MAJOR for a renamed/removed skill or a changed rule/gate ID, MINOR for a new skill, detection parameter, or playbook, PATCH for wording fixes, claim corrections, and example updates. A skill is never silently deleted — it is marked deprecated with a pointer to its replacement and removed only in a MAJOR release.

## Issues

Use the template that matches the problem; each one asks for exactly what a maintainer needs to route the issue to the owning department:

- **Gap report** (`.github/ISSUE_TEMPLATE/gap-report.md`) — a project type, task, playbook, or skill the repo does not cover.
- **Bug report** (`.github/ISSUE_TEMPLATE/bug-report.md`) — a skill, rule, or gate that produced a wrong result; name the skill and gate/rule ID.
- **Skill request** (`.github/ISSUE_TEMPLATE/skill-request.md`) — a new skill the catalog needs; name the job it would do and the department that should own it.

Claims in issues and in skills follow the same rule: no fact without a source. If you cannot verify a claim, mark it UNVERIFIED rather than presenting it as fact.
