# Example 2 — The quickstart that never ran

## Before

```markdown
## Getting started

    npm install
    npm run dev
```

Written from memory and never executed. In a clean checkout `npm run dev` fails — the package defines only a `start` script — and the install step silently needs a `.env` file the README never mentions. The README contradicts the project on the first two commands a reader runs.

## After

```markdown
## Quickstart

Requires Node 20+. Copy the environment template first; the app refuses to
start without it.

    npm install
    cp .env.example .env
    npm start        # http://localhost:3000
```

Verified by running the three commands verbatim, in order, in a clean clone: install exits 0, the app starts, and the URL answers. The gate result is recorded in progress.md.

Demonstrates PM-043 (quickstart executed verbatim before shipping).
