# D15 Developer Experience — End-to-End Example

## Scenario

A second developer joins "NoteNest," a small note-taking SaaS, and clones the repo
on a clean laptop. The measure of the developer experience is simple: one documented
command takes the clone to a running app with tests passing — and every version,
secret, and shortcut in the repo is exactly where the next developer expects it.

## Before — the slop version

README setup section:

```markdown
## Setup
1. Install Node (latest LTS) and the newest Docker.
2. npm install
3. Copy .env.example to .env and fill it in.
4. Start Postgres locally first, then `npm run dev`.
5. Ask in chat for the extra step that creates the local storage bucket.
```

`.env.example` as committed:

```bash
DATABASE_URL=postgres://notes_admin:Tr7!falcon@db.notenest.internal:5432/notes
PAYMENTS_API_KEY=<the project's live key, copied "so the demo works">
```

And in the same week's feature pull request: `package-lock.json` deleted and
regenerated (silently moving dozens of transitive versions), plus a merged
`// TODO: add validation later` above the checkout handler with no owner or date.

## What the skills caught

- **BAN-DX-002 — Floating tool versions** (defeats DET-CODE-028). "Latest LTS" and
  "newest Docker" install whatever exists on the day. **DX-002 / DX-003**: every
  runtime and tool version is declared exactly once, exactly, in one pin file.
- **BAN-DX-001 — Real secret in an example file** (defeats DET-CODE-018). The live
  payment key and a real database password are committed. **DX-006**: placeholders
  only — obviously non-functional values and reserved example hosts.
- **BAN-DX-003 — Setup steps outside the bootstrap** (defeats DET-CODE-032). "Ask
  in chat" and "start Postgres first" are setup steps living in memory and manual
  ritual. **DX-001**: one bootstrap command; **DX-010**: backing services are
  declared in a committed compose file and started by the bootstrap.
- **BAN-DX-031 — Casually regenerated lockfile** (defeats DET-CODE-028). The
  feature PR rewrote the resolved dependency tree as a side effect. **DX-061 /
  DX-062**: the lockfile is committed and canonical; installs run frozen; a
  lockfile regeneration is its own dedicated change whose diff is the review.
- **BAN-DX-041 — Bare TODO marker** (defeats DET-CODE-011). The marker names no
  register entry, owner, or trigger. **DX-086**: every TODO/FIXME/HACK carries a
  debt-register reference, e.g. `TODO(DEBT-123): …`.

## After — the corrected version

`mise.toml` — the one pin file (DX-002); the README names the bootstrap command
and links the pin file and `.env.example`, restating no versions (DX-012):

```toml
[tools]
node = "22.11.0"
# every runtime and CLI tool is pinned here, exactly once
```

```bash
# The entire setup, from a clean clone:
make setup        # installs pinned tools, frozen-installs from the lockfile,
                  # starts declared services, runs migrations, runs the tests
```

`.env.example` — complete, placeholders only (DX-005, DX-006):

```bash
# Connection string for the local database the bootstrap starts.
DATABASE_URL=postgres://app:change-me@localhost:5432/app_dev
# Payment provider test-mode key; use your own from the provider dashboard.
PAYMENTS_API_KEY=<redacted>
```

The app validates its configuration at startup and exits non-zero naming each
missing variable — there is no silent fallback to a production host or credential
(DX-007, BAN-DX-004). The validation shortcut is no longer a bare comment; it is a
register entry created in the same change that incurred it (DX-083):

```markdown
## docs/tech-debt.md
### DEBT-007 — Checkout handler validates postcode inline, format unchecked
- Location: src/checkout/handler.ts
- Quadrant: deliberate × prudent
- Interest: every postcode-format change must be made in this one handler and
  re-tested by hand; a malformed postcode reaches the payment provider.
- Owner: A. Rahman
- Repayment trigger: next change touching checkout validation
- Incurred: 2026-11-18
```

## Skills used

- [dev-environment](../skills/developer-experience/dev-environment/SKILL.md)
- [dependency-management](../skills/developer-experience/dependency-management/SKILL.md)
- [tech-debt](../skills/developer-experience/tech-debt/SKILL.md)
- [versioning](../skills/developer-experience/versioning/SKILL.md)
