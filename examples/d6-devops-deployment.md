# D6 Example — Replacing a Hand-Carried Deploy with a Pipeline

## Scenario

The SaaS is live with real paying users. D6 owns how code gets to
production: the container image, the CI pipeline, the deploy mechanism,
and the way back when a release goes bad.

## Before

```dockerfile
FROM node:latest
WORKDIR /app
COPY . .
CMD npm install && npm start        # deps installed at container start, runs as root
```

```bash
# deploy.sh — run from the maintainer's laptop
scp -r ./build prod:/srv/app/       # overwrites the live version in place
ssh prod "pm2 restart app"          # done, no record of what shipped
```

```yaml
# .github/workflows/ci.yml — the only workflow
jobs:
  test:
    steps:
      - run: npm test || true       # failures cannot fail the job
```

A real database password sits in a committed `.env` file "temporarily".
Health, such as it is, means opening the homepage after a deploy.

## What the skills caught

- **BAN-DO-003 — Hand-carried deploy** (**DET-INF-004 — Manual,
  unreproducible deploys**): the deploy exists only on one laptop.
  **DO-042 — No manual deploy steps** and **DO-008 — Every deploy leaves
  a record** both fail; there is no record of what is running.
- **BAN-DO-031 — Floating `latest` tag in a deploy spec** (**DET-INF-026
  — Mutable or unpinned production artifacts**): `node:latest` means the
  same Dockerfile builds a different app next month. **DO-062 — Pin every
  base image**, **DO-068 — Immutable tags**.
- **BAN-DO-033 — Installing dependencies at container start** and
  **BAN-DO-034 — Root by default in the final stage**: **DO-065 —
  Dependencies before source**, **DO-064 — Final stage runs non-root**.
  No health declaration (**DO-070**), no `.dockerignore` (**DO-066**).
- **BAN-DO-002 — Neutered gating job** (**DET-INF-002 — CI exists but
  never gates**): `|| true` makes the test stage decorative. **DO-004 —
  Prove the pipeline can fail**; the broken-test drill **G-DO-001** is
  exactly this check.
- Committed secret: **DO-011 — Secrets come from the CI secret store
  only** (**DET-INF-005 — Secrets committed to version control**).
- **BAN-DO-151 — In-place overwrite deploy** (**DET-INF-017 — No rollback
  path for a bad deploy**): the previous version is destroyed by the act
  of deploying. **DO-301 — The rollback action is written before the
  release ships**; **DO-302 — The previous version stays deployable**.
- **BAN-DO-073 — The homepage health check** (**DET-INF-020 — No health
  check endpoint or probes**): a 200 homepage says nothing about the
  database or the queue. **DO-144 — Health checks reflect the ability
  to serve**.

## After

Multi-stage Dockerfile: pinned base (`node:22.11.0-alpine`), dependencies
installed from the lockfile in the build stage, final stage non-root,
`HEALTHCHECK` against `/healthz`, image tagged with the commit SHA and
promoted unchanged between environments (**DO-005 — Build once, promote
the same artifact**).

The pipeline (single definition, in the repo — **DO-001**) runs on push
and pull request with required checks (**DO-003**): lint, tests (no
`|| true`), image build, vulnerability scan (**G-DO-032**), then deploy
to staging, smoke test, and promotion to production behind environment
protection (**DO-045**). Secrets are injected from the CI secret store;
the committed `.env` was rotated first, because a committed secret is
public. Each deploy writes a record: SHA, timestamp, actor, result
(**DO-008**, audited by **G-DO-005**).

Rollback is one command, written before the release shipped: re-point
production to the previous retained image — the drill in staging
(**G-DO-151**) proves the switch and the switch-back before anyone
needs them at 2 a.m. Readiness is `/healthz`, which checks the database
and queue and fails closed; the homepage is never consulted.

## Skills used

- [ci-cd](../skills/devops-deployment/ci-cd/SKILL.md)
- [containers](../skills/devops-deployment/containers/SKILL.md)
- [deployment-strategies](../skills/devops-deployment/deployment-strategies/SKILL.md)
- [rollback](../skills/devops-deployment/rollback/SKILL.md)
- [hosting](../skills/devops-deployment/hosting/SKILL.md)
