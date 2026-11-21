# project-templates

## Metadata

- **Owner department:** D10 Project & Memory (PM)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository ; https://simonwillison.net/2021/Aug/28/dynamic-github-repository-templates/ ; https://docs.github.com/en/enterprise-cloud@latest/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file
- **Depends on:** none — standalone: this skill owns the scaffold itself; its input is the mandated project file set defined in this repo, not another skill's output — every project starts here. It feeds readme-writing, documentation-writing, progress-tracking, and handover.
- **Feeds into:** readme-writing, documentation-writing, progress-tracking, handover

## When to use / Do NOT use

- **Use when:** a new project repository is being created, the mandated file set changes, or the project template itself is being revised. This skill owns the scaffold every project starts from.
- **Do NOT use when:** the project already exists and only its content needs work (use the owning skill — readme-writing, changelog, decision-logs), or when backfilling one missing file by hand would leave the template unchanged (fix the template, then regenerate).

## Rules

1. **PM-001 — Full mandated set, or a recorded exception.** Generation emits the full extended mandated set for the project type (the Appendix A files plus the D-006 additions: LICENSE, CODEOWNERS, `docs/adr/`, issue and PR templates, .gitignore, dependabot.yml). Every file not emitted is listed in the generation record as not-applicable with a reason. A file is never silently absent.
2. **PM-002 — Templates carry variables, not content.** Template files contain structure, headings, fill-in prompts, and substitution tokens (`{{project_name}}`, `{{owner}}`, stack choices) — nothing else. A token is a variable to be replaced at generation time, never prose to be read.
3. **PM-003 — No invented facts, ever.** No template ships a name, metric, date, contact detail, testimonial, team member, or capability claim as sample content. Where a real project would state a fact, the template carries a prompt naming where the fact comes from (fact-sheet.md, the owner's input) — never a plausible invention.
4. **PM-004 — Empty sections stay honestly empty.** A section with no real content yet keeps its heading and its fill-in prompt, and nothing more. Filler prose written to make a section look finished is a defect, even when it is generic.
5. **PM-005 — Conditional files fire on triggers only.** CONTENT_METADATA, PAYMENT_SECURITY, and CLONE_DESIGN_SYSTEM are emitted only when the project type triggers them (content publishing, payments, a clone build). A condition stated in the owning playbook (for example, a step marked "if paid", or a recorded stack choice the file depends on) is a trigger for this rule: when the condition does not hold, the file is recorded not-applicable in the generation record with the condition as the reason. Where the owning playbook has not yet defined the trigger, the gap is recorded in the generation record — the drafter does not guess the classification.
6. **PM-006 — Generation is one reproducible command.** A fresh project is produced by running a generator (cookiecutter-style, Jinja + `cookiecutter.json`, or any equivalent) against the versioned template. Generation means producing exactly the file set listed in the project type's shipped manifest, `templates/mandated-manifest-<type>.txt` — the manifest is the normative artifact: where a generator's output and the manifest disagree, the manifest governs and the generator is fixed. GitHub template repositories copy structure but substitute no variables, so they are never the whole mechanism. Hand-assembling the file set is not generation. This repository ships a reference generator for exactly this contract — `python3 scripts/generate-project.py --type <type> --target <dir>` emits the manifest's file set (the template file where `templates/` carries one, an honest empty-section scaffold otherwise) and prints the manifest diff result; any equivalent generator satisfies the rule the same way.
7. **PM-007 — Output is never hand-patched.** A defect found in a generated project is fixed in the template and the project is regenerated, or the fix is recorded as a deliberate project-level divergence. Editing only the output guarantees the next project inherits the defect.
8. **PM-008 — The template is versioned and changelogged.** The template carries a semantic version and a changelog entry per change, like a product. A version with no changelog entry does not ship.
9. **PM-009 — Mandated-set changes are decisions first.** Any change that adds, removes, or renames a mandated file is recorded in the decision log before the template ships it. The template never drifts ahead of the recorded set.
10. **PM-010 — Public projects get the community files.** CODE_OF_CONDUCT, SUPPORT, and GOVERNANCE are emitted when the project is public, on top of GitHub's recognized community-profile floor (README, LICENSE, CONTRIBUTING, SECURITY). For a private project they are recorded not-applicable under PM-001, not forgotten. SECURITY in that floor is a single file with two named sections — vulnerability reporting (how to report) and the project's security design — never two separate files with the same name.
11. **PM-011 — Generated output passes the gates from the first commit.** A generated project passes markdownlint and the link checks with zero errors before its first commit. "We'll lint it later" is how unlinted scaffolds become permanent.
12. **PM-012 — Every template change is self-tested.** Before a template change merges, a sample project is regenerated from it and gates G-PM-001 to G-PM-003 are run against the output. An untested template change does not merge.

## BAN list

- **BAN-PM-001 — Invented social proof baked into the template.** Banned: template output containing sample testimonials, user counts, ratings, or press mentions presented as the project's own. Defeats: DET-CON-010. Bad: the generated README opens with "Trusted by 10,000+ teams" and two named-customer quotes the new project has never had. Instead: the README carries the heading and a prompt — "List real customers only, each with a producible source record (see real-content)" (PM-003). Severity: BLOCK.
- **BAN-PM-002 — Scaffold boilerplate shipped as project content.** Banned: generator or theme defaults surviving into the shipped files — a scaffold README describing the template itself, "Hello world!" posts, "Add a description here". Defeats: DET-CON-002. Bad: the new project's README explains how to use the template repository instead of what the project is. Instead: every default string is replaced by project structure and prompts at generation time, or the file is not emitted (PM-002). Severity: BLOCK.
- **BAN-PM-003 — Unreplaced substitution tokens in shipped files.** Banned: `{{project_name}}`, `{{owner}}`, or any `{{ }}` token visible in a committed project file. Defeats: DET-CON-003. Bad: the shipped CONTRIBUTING.md is titled "Contributing to {{project_name}}" because generation ran without the variable set. Instead: generation fails unless every declared variable has a value, and gate G-PM-002 scans the output before the first commit. Severity: BLOCK.
- **BAN-PM-004 — Compliance furniture without the process.** Banned: emitting a conditional file that asserts a practice the project does not run — above all a PAYMENT_SECURITY.md describing controls that do not exist. Defeats: DET-CON-028. Bad: a project with no payment flow ships a payment-security file claiming encrypted card handling and audit reviews. Instead: conditional files fire only on their real trigger (PM-005) and describe only processes that exist. Severity: BLOCK.
- **BAN-PM-005 — Draft markers left in generated files.** Banned: TODO, FIXME, or "content to follow" strings in any generated file's fields, headings, or metadata. Defeats: DET-CON-004. Bad: the generated SUPPORT.md ships with "TODO: add the real support email" as its contact section. Instead: an unknown value is an unfilled variable that blocks generation, or a fill-in prompt that names the missing fact (PM-002, PM-004). Severity: WARN.

## Gates

- **G-PM-001 — Manifest diff.** Verifies: PM-001, PM-005, PM-010. Check (automated): generate a fresh project into a scratch directory and run `diff <(cd <output> && find . -type f | sort) <repo>/templates/mandated-manifest-<type>.txt` — the manifest shipped in this repository's `templates/` directory, never a locally reconstructed copy. Scope: this is a generation-time (step-0) check; files that later playbook steps mandate (for example performance-budget.json, PRIVACY_REGISTER.md, the CI workflow) are expected additions recorded in progress.md, and when the diff is re-run later they are matched against those step records — they are not diff violations. Pass: zero differences, or every difference matched by a not-applicable entry with a reason in the generation record. Fail: block shipment. Recorded in: progress.md.
- **G-PM-002 — Unreplaced-token and marker scan.** Verifies: PM-002, PM-003. Check (automated): `grep -rn '{{' <output>/` and `grep -rn 'TODO\|FIXME' <output>/` — both must return nothing. Pass: zero hits. Fail: block shipment; fix the template or the variable set, never the output alone. Recorded in: progress.md.
- **G-PM-003 — Lint parity on generated output.** Verifies: PM-011. Check (automated): run `markdownlint <output>/**/*.md` on the freshly generated tree, using the starter configuration shipped with the mandated set (`templates/.markdownlint.json`, emitted into every generated project as `./.markdownlint.json`; DECISIONS D-017) unless the project has recorded its own documentation configuration in its decision log. Where markdownlint is not available in the agent's environment, the fallback is a documented manual style check of the generated Markdown against that same rule set — heading hierarchy, list and table structure, link syntax — with the check and its result recorded in progress.md; the automated run remains required wherever the tool exists. Pass: exit 0, zero errors, before the first commit (under the fallback: a recorded manual check with zero findings). Fail: block shipment. Recorded in: progress.md.
- **G-PM-004 — Exception register review.** Verifies: PM-001, PM-009. Check (manual): read the generation record for the new project; every absent mandated file has a stated reason, and every mandated-set change the template embodies has a decision-log entry that predates the template version. Pass: zero unexplained absences and zero unlogged set changes. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Template drift.** A fix is made inside one generated project and never lands in the template, so every later project re-inherits the defect. Catch it by asking of any project-level doc fix: "is this already in the template?"
- **Copy-the-last-project scaffolding.** The new repo is cloned from a previous project and find-replaced, inheriting that project's facts, decisions, and risks as silent defaults. Catch it: any file whose content names a source other than the template version and the new project's own inputs is suspect.
- **Vague prompts.** Fill-in prompts like "write something about the project" invite the generator to guess. Catch it: a prompt must name the fact it wants and where that fact lives; a prompt that names neither is rewritten before the template ships.
- **Manifest by memory.** Checking the emitted file set against what the author remembers the mandated set to be. Catch it: the manifest is a file in the template repo, and gate G-PM-001 diffs against that file — never against recollection.

## Examples

- [Example 1 — The README that arrived with customers](examples/example-1.md) — violates/corrects PM-003.
- [Example 2 — The security file nobody missed](examples/example-2.md) — violates/corrects PM-001.
- [Example 3 — Tokens and TODOs in the first commit](examples/example-3.md) — violates/corrects PM-002.

## Recall anchors

- Full set, or a recorded reason — never a silent gap.
- Structure and prompts ship; facts never do.
- An empty section is honest; a filled-looking one may not be.
- Fix the template, regenerate — never patch the output.
- Conditional files fire on real triggers only.

## Checklist

- [ ] Manifest diff is clean, or every absence has a recorded reason (PM-001, G-PM-001).
- [ ] No template file contains an invented name, metric, testimonial, or date (PM-003).
- [ ] Token and marker scan returns zero hits on the generated output (G-PM-002).
- [ ] Conditional files match the project type's triggers; undefined triggers are recorded as gaps (PM-005).
- [ ] Public projects include CODE_OF_CONDUCT, SUPPORT, and GOVERNANCE (PM-010).
- [ ] markdownlint passes on the generated tree before the first commit — or, where the tool is absent, the manual style check against the starter configuration is recorded (PM-011, G-PM-003).
- [ ] Template version bumped and changelogged; mandated-set changes have a prior decision-log entry (PM-008, PM-009).
