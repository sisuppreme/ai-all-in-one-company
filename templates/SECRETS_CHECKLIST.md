# Secrets Checklist — Deploy-Time Handoff

Complete this checklist when a project built with this repository is deployed. It is the user-side companion to the D7 `secrets-management` skill (`skills/security/secrets-management/SKILL.md`), which governs the whole handoff — load that skill before starting. The protocol in one line: **a secret's name and purpose may appear in project files; its value must never appear in any project file, chat log, or commit.**

## Ground rules (read first)

- [ ] Every secret the project needs is listed below **by name and purpose only**. No value is written in this file, in `fact-sheet.md`, in `progress.md`, or anywhere else in the repo.
- [ ] All accounts (hosting, domain, payments, email) are in the **user's** name. The agent never owns the user's accounts.
- [ ] Verification uses **test/sandbox credentials only** (Stripe test keys, sandbox API keys). Live keys are entered by the user at deploy time and verified from the host's dashboard — never sent to the agent for a "quick test".

## Step 1 — Inventory (before any handoff)

The agent lists every secret it needs, by name + purpose, before asking for anything. One row per secret:

| Secret name (environment variable) | Purpose | Where it is obtained | Test value ready? | Live value ready? |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

- [ ] Every variable the code reads appears in this table — no code references a secret that is not inventoried (verified by gate **G-SE-045**, inventory and revocation review).
- [ ] Each secret has an owner, a scope no broader than its service needs, and a rotation date.

## Step 2 — Handoff, by agent capability

**Agent with a secret store (for example Muse/Claude with a vault flow):**

- [ ] The user enters each value in the platform's secret/vault flow.
- [ ] The agent references secrets by name only, in code and in conversation.

**Chat-only agent (for example Google AI Studio — no filesystem, no secret store):**

- [ ] The agent **never receives any secret value**. It does not ask the user to paste one into the chat "to store it" — there is nowhere safe for it to go.
- [ ] The agent writes code with `process.env.<NAME>` placeholders only.
- [ ] The user enters each live value directly in the host's dashboard environment settings (for example Vercel or Netlify environment variables) at deploy time, working from the Step 1 table.

## Step 3 — Files in the project repo

- [ ] `.env.example` exists and lists **every** variable from the Step 1 table, each with its purpose and where to obtain it — names and purposes only, every value an obvious placeholder (verified by gate **G-SE-044**, example-file audit).
- [ ] `.env` (the real local file, if the agent has filesystem access) is git-ignored and untracked: `git check-ignore .env` exits 0 and no `.env` appears in `git ls-files` (verified by gate **G-SE-042**, ignore and tracking check).
- [ ] A full-history secret scan over the repository returns zero findings (gate **G-SE-041**).
- [ ] The production client bundle contains no server secrets — only publishable/public keys (gate **G-SE-043**, client bundle scan).

## Step 4 — Verify with test credentials

- [ ] Test/sandbox values are in place in the test environment.
- [ ] The agent verifies each integration with a read-only or test-mode call that creates no real objects and no charges.
- [ ] Failures are fixed against the test setup before any live value is touched.

## Step 5 — Go live

- [ ] Live values entered by the user into the host's dashboard environment settings (Step 2 route — never via chat).
- [ ] Test data purged from the live system.
- [ ] Webhooks re-pointed from test endpoints to live endpoints.
- [ ] Monitoring and alerting live.
- [ ] Rollback tested.
- [ ] The user approves the switch from test to live.

## If a secret is ever exposed

If a value is pasted into chat, committed, or logged — at any point, by anyone:

1. **Revoke/rotate it immediately.** Treat it as public from the moment it was exposed; deleting the message or commit does not un-expose it.
2. The agent names the exact secret affected and tells the user to rotate it, before doing anything else.
3. The incident is recorded in `progress.md` with the secret **name**, the date, and the rotation status — never the value.
