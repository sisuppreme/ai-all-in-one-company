# Example 1 — Scaffold README replaced by a front door

## Before

```markdown
# my-app

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- @vitejs/plugin-react uses Babel for Fast Refresh
- @vitejs/plugin-react-swc uses SWC for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type aware lint rules...
```

The generator's README shipped untouched: it describes the framework template, never names the project, its audience, its status, or how to run the actual application.

## After

```markdown
# Ledgerline

Ledgerline is a small invoicing tool for freelance bookkeepers: it turns a
client list and a rate card into sent, tracked invoices.

**Status:** v1.2, in production use — 2026-11-15.

## Quickstart

Requires Node 20+ and a Postgres 15 database (see `.env.example`).

    npm install
    cp .env.example .env
    npm run db:migrate
    npm start        # http://localhost:3000

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Runbook](docs/runbook.md)
- [Changelog](CHANGELOG.md)
- [Decisions](docs/DECISIONS.md)
```

Demonstrates PM-042 (no boilerplate survives) and PM-041 (fixed front-door order: what, who, dated status, quickstart, link index).
