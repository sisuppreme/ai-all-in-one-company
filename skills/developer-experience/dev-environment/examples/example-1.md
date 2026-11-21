# Example 1 — The nine-step README

## Before

```markdown
## Getting started

1. Install Node 20 (or newer) and pnpm.
2. Install Postgres 15 and create a database called `app_dev`.
3. Clone the repo and run `pnpm install`.
4. Copy `.env.example` to `.env` and ask the team lead for the real values.
5. Run `pnpm db:migrate`, then `pnpm db:seed`.
6. Start Redis — on Mac use brew services, on Windows use WSL.
7. Run `pnpm dev` in one terminal and `pnpm worker` in another.
8. If the seed fails, delete `node_modules` and try again.
9. The tests need the test database from step 2 but named `app_test`.
```

Setup is tribal knowledge spread over nine manual steps, two of which ("or newer", "ask the team lead") cannot be executed by a new developer or a clean machine at all.

## After

```markdown
## Getting started

git clone <repo> && cd <repo>
make setup        # installs pinned tools, dependencies, services, migrations, seed
make test         # full suite against the test database created by setup
make dev          # app + worker, services already running

Tool versions are pinned in `mise.toml` (Node, pnpm, Postgres client).
Backing services are declared in `.devcontainer/devcontainer.json` and
`docker-compose.yml`; `make setup` starts them. Copy `.env.example` to
`.env` — the placeholder values work for local development as-is.
```

One command reaches a running app; versions, services, migrations, and seed are all declared in committed files the command consumes.

## Note

Corrected under DX-001: any manual step beyond the bootstrap command is a defect in the setup; the After also satisfies DX-002 (versions in one pin file) and DX-010 (services declared, not hand-started).
