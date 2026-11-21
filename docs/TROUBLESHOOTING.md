# TROUBLESHOOTING.md — When you are stuck or something fails

For the single consuming agent using this repository on a project. You work alone: there are no leads to escalate to and no second agent to hand off to. Your escalation path is **skill → links → log → user → safe default**. This file is that path, in order.

## The stuck protocol (brief §6.3)

Getting stuck is normal. Hiding it, or inventing a way out, is not.

### Step 0 — Name the blocker type

The response differs by type. Log the type in `progress.md` with the entry.

| Type | What it is | Response |
|---|---|---|
| (a) Missing information | A fact, asset, or decision you do not have | Steps 1–4 below |
| (b) Two skills contradict | Loaded skills give incompatible instructions | The precedence order in `BOOTSTRAP.md` decides; log the conflict in `DECISIONS.md`; ask the user only if precedence does not resolve it |
| (c) External service down / tool failure | An outage or a broken tool | Retry twice with a short wait, then log it and continue with unblocked work. Do not ask the user about an outage they cannot fix |
| (d) Missing credential or secret | A key or login you were never given | The secrets handoff (`templates/SECRETS_CHECKLIST.md`): ask the user for the specific item; meanwhile build with test keys or defer that part (step 4) |
| (e) Ambiguous or impossible requirement | The requirement cannot be read one way, or cannot be done | Step 4, with concrete options |

Two special cases:

- **User requirements contradict each other** — list the contradiction and the options, and ask. Never silently pick one.
- **Requirements change mid-build** — update `requirements.md`, re-run the affected gates, and re-estimate. Major changes need the user's approval.

### Step 1 — Re-read the skill

Re-read the loaded skill's checklist and gates, once, thoroughly. If the same step has been attempted twice with the same result, stop retrying it and go to step 3 — do not attempt a failing step a third time without new information. A blocker that survives steps 1–2 is logged in the same working session; it is never carried silently into the next one.

### Step 2 — Check the links

Check `docs/DEPARTMENT_LINKS.md` and the skill's Depends on / Feeds into neighbours — the owning department's skill may hold the missing piece.

### Step 2b — If no skill covers it, it is a repo gap

Log it in `progress.md` as a GAP: what was needed, which skills were checked, what is missing. Report it through the feedback loop (a GitHub issue using the templates in `.github/ISSUE_TEMPLATE/`, or a note to the user if you cannot file issues). Then proceed with the closest skill plus that skill's own gates, and flag the workaround in `progress.md` as provisional. Never silently invent a skill or a process and present it as repo guidance.

### Step 3 — Log the blocker, keep working

Log the blocker in `progress.md`: what is blocked, what was tried, what is needed. Then continue with all unblocked work. A project with one blocked item and ten unblocked items keeps moving on the ten. If several blockers accumulate, batch them into ONE message to the user, with a concrete option per blocker — not one interruption per blocker.

### Step 4 — Ask the user, with concrete options

Ask a real question with options and a recommendation, never an open "what should I do?":

> "The Stripe secret from the secrets handoff was not provided. Option A: I build the checkout with the test key and you swap in the live key later. Option B: I defer checkout and ship everything else. Which one?"

> "The requirements say both 'guests can check out' and 'checkout requires an account' — which one is correct?"

Do not use step 4 to ask the user to make design decisions the skills already answer — that is a requirements gap, not a stuck case.

- **4b. While waiting, keep working.** Continue all unblocked work; log the blocked item in `progress.md` with the date asked. Never halt the whole project for one blocked item.
- **4c. If the user does not answer:** after one follow-up (or, in a single uninterrupted run, immediately), apply the safe default — ship the affected section as an honest empty state, or defer the feature with a dated TODO in `progress.md` — and record that the default was applied and why. Never guess the user's answer.
- **4d. If the user does not know:** say so plainly, recommend the option the skills favour, with reasons, and proceed only on the user's explicit choice.

### Step 5 — The never list

- **Never invent data** to get unstuck.
- **Never skip a gate.** A skipped gate is a failed deliverable, not a shortcut. If the user asks you to skip a security or QA gate, refuse the skip and offer the waiver process below instead.
- **Never silently drop a requirement.** Dropping one needs the user's explicit agreement, recorded in `requirements.md` (moved to a "Dropped, with reason" section, never deleted) and in `DECISIONS.md` (what was dropped, why, what the user was told, what replaces it).
- **Never guess on money, legal positions, or destructive actions.** Prices, charges, refunds, contract or compliance claims, deletions, and anything irreversible always go to step 4 with options — they are never resolved by a safe default.

### The waiver process (the one exception to "never skip a gate")

A gate may be waived only when the gate itself is wrong for this project: it contradicts another gate, it tests a feature the project does not have, or its tooling is unavailable to a single agent. Then:

1. Record the waiver in `progress.md` and `DECISIONS.md`: which gate, why it cannot pass, and what was checked instead.
2. A waiver of a security, legal, or Real Content gate (precedence ranks 1–3) needs the user's explicit agreement. Other waivers need only the written record.
3. Flag the gate as a repo gap through the feedback loop.

An unrecorded skipped gate is still a failed deliverable.

## Failure modes

### The repo cannot be fetched

You cannot load the repository (no network, no file access, the link fails). Fallback: ask the user to paste `bundles/core.md` and proceed with the core bundle only — the always-on skills, the condensed index, and the precedence order are in it. Flag the gap in `progress.md` (which departments you could not load) and load the full skills as soon as access returns. Do not reconstruct skills from memory and present them as the repo's.

### A bundle is too large for your context

Load less, in sequence. Load `bundles/core.md` first, then only the department bundle for the step you are on; when that step's gates pass, drop it and load the next. Never hold more than two bundles at once, and never load `bundles/ALL_SKILLS.md` whole — it is a reference for searching, not a context load. The routing rule in `BOOTSTRAP.md` (playbook first, else keyword → department) exists to keep loads this small.

### Two skills conflict

Apply the precedence order in `BOOTSTRAP.md` (security → legal/privacy → Real Content Rule → QA process gates → accessibility → …). Within one rank, the more specific skill wins. Log the conflict and its resolution in `DECISIONS.md`. Precedence never excuses skipping a gate: when a higher-ranked rule conflicts with a gate, re-run the gate's check against the higher rule's requirement instead of skipping it. Ask the user only if precedence and specificity both fail to resolve it.

### No playbook matches the project type

Use the closest playbook, chosen by three questions: (1) does it take payments? (2) does it have user accounts? (3) is it content-led or app-led? The playbook matching on the most answers wins; ties go to the SaaS playbook. Record the choice and your reasoning in `progress.md`. If no playbook matches on at least 2 answers, build a custom sequence from the routing rule in `BOOTSTRAP.md` and flag the missing playbook as a repo gap through the feedback loop.

### A gate cannot be run

First, use the skill's manual fallback: gates are written so a check that normally needs tooling has a manual form (a checklist walk, a diff, a read-through) — a manual pass is a real pass, recorded as manual in `progress.md`. If the gate cannot pass even manually because the gate is wrong for the project, use the waiver process above. What you may not do: mark it passed, skip it silently, or weaken its criterion on your own authority.

### The repo looks stale

At the start of work (BOOTSTRAP step 0), read the repo's `VERSION` and `CHANGELOG.md` and note the version in `progress.md`. If the repo is old relative to the tools you must use, warn the user, and re-verify the tool/API claims of every skill you load against current sources instead of trusting the repo. Record which claims you re-verified.

### A required tool is missing (tool bootstrap fails)

A gate's check names a tool — gitleaks, markdownlint, Playwright, axe-core, Lighthouse, a scanner — and the tool is not installed, or its install fails (no global install permission, a package-cache ownership error, a browser-binary download that stalls, scratch space in `/tmp` too small for the payload). First remedy: install the tool project-locally, never globally — a project-local npm or pip install (a devDependency, a project venv, a project-local npm cache when the shared cache is not writable), a manually downloaded browser binary pointed to by the tool's `executablePath` setting, or a vendored script that ships with the repo or the project (the `scripts/qa/` reference implementations are this pattern). A tool obtained this way runs the gate's check unchanged, so the gate passes or fails in its normal form: record the install in `progress.md` as a tool-form substitution — tool, version, and where it came from. A substitution changes only where the tool lives, never what is checked; the moment a workaround changes the check itself or its criterion, it is no longer a substitution — use the gate's own manual form or substitute-evidence path if it names one (recorded as that gate prescribes), and if it names none, use the waiver process above. The missing tool becomes a provisioning blocker, not a workaround, when the environment itself prevents every route: no network egress to fetch the tool or its browser binary, no writable location for a project-local install or scratch space, or a platform policy that forbids running it — and the gate has no manual form. Record it in `progress.md` as a blocked item (blocker, owner, unblocking condition, per Step 3), keep working on everything not behind that gate, and if the blocked gate is a launch gate, stop and ask per Step 4 instead of improvising a substitute the repo never sanctioned.

## FAQ

**Can I skip a gate just this once?**
No. Run it, run its manual fallback, or record a waiver. Those are the only three outcomes a gate can have.

**The user has not given me the real content (testimonials, stats, team names). Can I write plausible ones?**
No — that is the Real Content Rule's core case. Ask once, batched, with a per-item prompt; if there is no answer, ship an honest empty state and log the open item in `progress.md`.

**Do I need sub-agents or a team to use this repo?**
No. The repo is single-agent compatible by design (QB-08): play every role yourself, sequentially, loading one bundle at a time. Never tell the user a handoff or a second agent is needed.

**A tool or service is down. Should I stop?**
Retry twice with a short wait. Then log it and do all the unblocked work. An outage is not a question for the user.

**The user is asking for something illegal, deceptive, or a copy of someone else's product.**
Refuse that part and offer a lawful alternative (QB-13). For clone work, the D14/D16 ethics gates apply: authorization first, no protected assets, and reconstructed pages marked designed-not-cloned.

**I found a fake in something already shipped.**
Fix it, do not hide it: remove or correct it, record the incident in `progress.md` (what was fake, how it slipped through, which check failed), and note the miss so the check that failed gets strengthened (Real Content Rule step 8).
