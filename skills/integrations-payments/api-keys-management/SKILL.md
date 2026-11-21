# api-keys-management

## Metadata

- **Owner department:** D11 Integrations & Payments (IN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Stripe, "API keys" (publishable, secret, and restricted keys) — https://docs.stripe.com/keys ; Stripe, "Create restricted API keys" — https://docs.stripe.com/keys/restricted-api-keys
- **Depends on:** secrets-management (D7 owns compromise-response depth)
- **Feeds into:** third-party-apis, webhooks, sdk-embeddables

## When to use / Do NOT use

- **Use when:** a project issues, stores, rotates, or revokes credentials: provider secret keys it consumes, webhook signing secrets, or API keys it issues to its own customers. Credentials are inventory with a lifecycle, not strings in a config file.
- **Do NOT use when:** the question is how a provider call is made (third-party-apis owns the adapter and its auth usage), how a webhook signature is verified (webhooks owns receiving mechanics; this skill owns the signing secret's lifecycle), or incident response beyond the first rotation (secrets-management in D7).

## Rules

1. **IN-201 — Keys live in secret storage, never in the repo.** Every credential is read at runtime from the environment or a secret manager. The repository carries only `.env.example` with obvious dummy placeholders (`sk_live_EXAMPLE`), and a real `.env` file is gitignored and never committed.
2. **IN-202 — Secret keys are server-side only.** A provider secret key is used only in server code. The browser or mobile client receives only keys the provider designed to be public (publishable keys) or a short-lived, narrowly scoped token minted server-side per session.
3. **IN-203 — One key per environment and purpose, least-privilege scope.** Keys are issued per environment (test, live) and per purpose (billing worker, reporting job), using restricted keys with the smallest permission set the provider offers wherever the provider supports them. A key's scope is written in the register (IN-211).
4. **IN-204 — Test and live credentials never mix.** Test and live keys are different keys held in different stores. A test key resolved in production configuration, or a live key in a development or CI environment, is a launch blocker.
5. **IN-205 — Keys you issue are shown once and stored hashed.** A customer API key's full value is displayed exactly once, at creation. At rest you store only a keyed hash of the value plus a non-secret prefix (e.g. `pk_live_9f3…`) that identifies the key in dashboards and logs without being usable as a credential.
6. **IN-206 — Every key is individually revocable.** Each key can be revoked on its own, without touching any other key, and revocation takes effect immediately. There is no shared "master key" whose revocation would be an outage, because there is no shared master key (IN-203).
7. **IN-207 — Rotation runs on a schedule and on suspicion, with overlap.** Each key carries a rotation date in the register. Rotation issues the replacement, deploys it, confirms the integration is green, and only then revokes the old key — overlap makes rotation routine instead of an outage.
8. **IN-208 — A found key is a leaked key: rotate first.** A key value appearing in a commit, a built bundle, a log, a screenshot, or a ticket is treated as compromised: rotate it before investigating how it got there. Deleting the line does not unpublish git history; history is leaked forever.
9. **IN-209 — Webhook signing secrets are keys.** Each webhook endpoint has its own signing secret, stored like any other credential, listed in the register, and rotatable without changing the endpoint URL. One secret shared across endpoints and providers is a defect.
10. **IN-210 — Key values are never logged.** Logs, error reports, analytics events, and support tickets record at most the key's prefix or last four characters. Redaction is applied at the logging layer, not left to each call site's memory.
11. **IN-211 — The key register is the inventory of record.** Every key has one register entry: provider, purpose, scope, environment, storage location, owner, and last rotation date. A key found in a store with no register entry is an orphan: it is revoked, not adopted.
12. **IN-212 — A client-visible key is never authorization.** Publishable keys shipped to the client are domain- or referrer-restricted where the provider allows, and the server still verifies every privileged outcome itself. Anything the client can read is public by definition, whatever its name.

## BAN list

- **BAN-IN-101 — The secret key in the client bundle.** Banned: embedding a provider secret key in frontend or mobile code that ships to users. Defeats: DET-CODE-018. Bad: the web app calls the provider with `sk_live_51H…` bundled into its JavaScript, so every visitor's browser downloads a full-access credential. Instead: the secret key stays in server-side secret storage (IN-201); the client gets the publishable key or a per-session scoped token (IN-202). Severity: BLOCK.
- **BAN-IN-102 — The committed credential.** Banned: a real key, password, or token as a literal in source, tests, or a committed config or `.env` file. Defeats: DET-CODE-018. Bad: `.env` with the live payment key is committed "temporarily" and cloned by every fork and CI cache from then on. Instead: the repo carries `.env.example` with dummy placeholders only; real values live in the secret store (IN-201). Severity: BLOCK.
- **BAN-IN-103 — Least privilege in name only.** Banned: claiming scoped credentials while every service, environment, and teammate uses the same single unrestricted key. Defeats: DET-FAKE-021. Bad: the register says "restricted billing key," but the billing worker, the reporting cron, and a developer's laptop all authenticate with the account's one full-access secret key. Instead: issue per-purpose restricted keys and record each scope in the register (IN-203, IN-211). Severity: BLOCK.
- **BAN-IN-104 — The key in the logs.** Banned: writing a full key value to logs, error reports, or debug output, including "temporary" request logging that captures authorization headers. Defeats: DET-CODE-029. Bad: a debug middleware logs every outbound request header, and the provider secret key sits in searchable log storage readable by the whole team. Instead: redact credentials at the logging layer and log only the prefix (IN-210). Severity: BLOCK.
- **BAN-IN-105 — Delete-the-line incident response.** Banned: responding to a leaked key by only removing it from the code or rewriting the visible file, while the same key stays active. Defeats: DET-CODE-018. Bad: the key is scrubbed from the repo in a follow-up commit, the ticket is closed, and the unchanged key still authenticates a month later — every clone made in between kept a copy. Instead: rotate first, then clean up; the old value is revoked before the incident is closed (IN-208). Severity: BLOCK.

## Gates

- **G-IN-101 — Secret scan.** Verifies: IN-201, IN-202. Check: automated — run a gitleaks-class secret scanner over the repository, the full git history, and the built client bundle and mobile package; assert the report is empty. Pass: zero findings (obvious placeholders such as `sk_live_EXAMPLE` in `.env.example` are allowlisted by value, not by path). Fail: block shipment and treat any real hit as a leak under IN-208. Recorded in: progress.md.
- **G-IN-102 — Environment separation check.** Verifies: IN-204. Check: automated — script resolves the credential identifiers the production configuration points at and asserts every one is a live key from the production store, and that development/CI configuration resolves only test keys. Pass: no test identifier in production scope and no live identifier outside it. Fail: block the release. Recorded in: progress.md.
- **G-IN-103 — Register audit.** Verifies: IN-203, IN-211. Check: automated — script lists the keys present in each secret store and diffs them against the key register. Pass: every stored key has a register entry with purpose, scope, owner, and rotation date, and every register entry resolves to a stored key. Fail: orphan keys are revoked and the audit re-run before release. Recorded in: progress.md.
- **G-IN-104 — Rotation drill.** Verifies: IN-207, IN-211. Check: manual with evidence — rotate one staging credential end-to-end using only the register's instructions: issue replacement, deploy, confirm the integration is green, revoke the old key. Pass: the integration never errors and the old key is rejected afterward. Fail: fix the register or the procedure and repeat. Recorded in: progress.md.
- **G-IN-105 — Revocation test.** Verifies: IN-206. Check: automated — create a throwaway key in the provider's test mode, confirm it authenticates, revoke it, and assert the provider now rejects it while a second key for the same account still works. Pass: revoked key rejected, sibling key unaffected. Fail: block shipment of any flow that issues keys. Recorded in: progress.md.

## Anti-patterns

- **Rotation theater.** A fresh key is issued on schedule and deployed, but the old one is never revoked "just in case," so every rotation adds a live credential instead of replacing one. Catch it: after any rotation, count active keys per purpose in the register audit (G-IN-103); the count must not grow.
- **The realistic placeholder.** `.env.example` ships with a value copied from a real key "so the format looks right," and someone later points staging at production with it. Catch it: placeholders are obviously fake (`sk_live_EXAMPLE`); the secret scan allowlists only those exact dummy values (G-IN-101).
- **The unnamed key.** The provider dashboard fills with keys labeled by creation date alone, and nobody can say which service breaks if one is revoked — so none ever are. Catch it: a key whose purpose cannot be stated in one sentence fails the register audit (IN-211).
- **Production keys on laptops.** Developers copy the live key into local `.env` files to "test the real thing," spreading the most powerful credential to the least controlled machines. Catch it: live keys exist only in the production store (IN-204); local work runs on test keys, and the environment separation check (G-IN-102) proves it.

## Examples

- [Example 1 — Moving a secret key out of the client bundle](examples/example-1.md) — corrects IN-202.
- [Example 2 — Replacing a committed .env with secret-store references](examples/example-2.md) — corrects IN-201.
- [Example 3 — Issuing a customer API key: shown once, stored hashed](examples/example-3.md) — corrects IN-205.

## Recall anchors

- If it shipped to a client, it is public — whatever its name.
- A found key is a leaked key: rotate first, investigate second.
- One key per environment and purpose, scoped as small as the provider allows.
- Shown once, stored hashed, identified by prefix.
- No register entry, no key: orphans are revoked, not adopted.

## Checklist

- [ ] All credentials resolve from secret storage; the repo holds only dummy placeholders (IN-201, G-IN-101).
- [ ] No secret key appears in the built client bundle or mobile package (IN-202, G-IN-101).
- [ ] Test and live keys are separate keys in separate stores, verified by the separation check (IN-204, G-IN-102).
- [ ] Every key has a register entry with purpose, scope, owner, and rotation date (IN-211, G-IN-103).
- [ ] Issued customer keys are shown once and stored only as hash + prefix (IN-205).
- [ ] A throwaway key revokes cleanly without affecting sibling keys (IN-206, G-IN-105).
- [ ] The staging rotation drill passed using only the register's instructions (IN-207, G-IN-104).
- [ ] Logs and error reports contain prefixes only, never full key values (IN-210).
