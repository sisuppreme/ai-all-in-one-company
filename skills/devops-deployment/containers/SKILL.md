# containers

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Docker Docs, "Building best practices" — https://docs.docker.com/build/building/best-practices/ ; DORA, "Continuous delivery" capability (build once, promote the same artifact) — https://dora.dev/capabilities/continuous-delivery/
- **Depends on:** ci-cd
- **Feeds into:** deployment-strategies, kubernetes, servers-vps, hosting, rollback

## When to use / Do NOT use

- **Use when:** a service is packaged for deployment — writing or reviewing its Dockerfile, image tagging, build pipeline, or the image reference a deploy actually runs.
- **Do NOT use when:** the workload runs on a platform that builds and runs the artifact itself with no Dockerfile in the repo (use hosting instead), or for orchestrator manifests and scaling policy (use kubernetes / scaling).

## Rules

1. **DO-061 — One Dockerfile per service, multi-stage.** Each service has exactly one Dockerfile at its root: a build stage with the full toolchain, and a final runtime stage carrying only the built artifact and its runtime dependencies — no compiler, SDK, or build cache in the final stage.
2. **DO-062 — Pin every base image.** Base images are pinned to a specific version tag (e.g. `node:22.11-alpine`); production builds pin by digest (`node:22.11-alpine@sha256:…`). An unpinned or major-only tag (`node`, `node:22`) fails review.
3. **DO-063 — No secrets in any layer.** No secret value appears in `ENV`, `ARG`, `COPY`, or any intermediate layer. Build-time secrets use BuildKit secret mounts (`--mount=type=secret`); runtime secrets are injected by the platform at start.
4. **DO-064 — Final stage runs non-root.** The final stage creates a dedicated user and sets `USER` to it before `CMD`/`ENTRYPOINT`. A final stage with no `USER` instruction runs as root and fails review.
5. **DO-065 — Dependencies before source.** The Dockerfile copies the dependency manifest and lockfile and installs dependencies before copying application source, so source-only changes reuse the dependency layer. Installs run in CI mode from the lockfile (`npm ci`, `--frozen-lockfile`, or the ecosystem equivalent).
6. **DO-066 — Committed `.dockerignore`.** Every build context has a committed `.dockerignore` excluding at minimum `.git`, `.env*`, `node_modules` (or the local dependency dir), and local build output, so secrets and local artifacts never enter the context.
7. **DO-067 — One process per container, exec form.** Each container runs exactly one foreground process, started with exec-form `CMD`/`ENTRYPOINT` (JSON array), so the application is PID 1 and receives `SIGTERM` directly. Supporting processes (database, cache, cron) are separate containers.
8. **DO-068 — Immutable tags, never `latest`.** Images are tagged with the release version and commit SHA and referenced by version tag or digest in every deploy spec. The exact image reference of each deploy is recorded with the deploy.
9. **DO-069 — Scanned in CI, rebuilt on a schedule.** Every image is vulnerability-scanned in CI before promotion, and base images are rebuilt on a regular cadence (at least monthly, and on critical base-image advisories) so patches actually land instead of aging in a pinned tag.
10. **DO-070 — Health is declared.** The image declares a `HEALTHCHECK`, or the deploy platform's probe is configured against the app's health endpoint, so a hung process is detected and restarted rather than judged by the homepage loading.
11. **DO-071 — Resource limits are set.** Every deployed container declares CPU and memory limits (compose `deploy.resources`, platform settings, or orchestrator spec) sized from observed usage; an unbounded container that can starve its neighbours fails review.
12. **DO-072 — Logs go to stdout/stderr only.** The application writes logs to stdout/stderr and never to files inside the container, so logs survive via the platform's log pipeline instead of vanishing with the container filesystem.

## BAN list

- **BAN-DO-031 — Floating `latest` tag in a deploy spec.** Banned: production or staging deploys referencing `image: app:latest` (or no tag). Defeats: DET-INF-026. Bad: compose file ships `image: myapp:latest`, so every restart silently pulls different code. Instead: reference the immutable artifact built in CI, e.g. `image: myapp:1.4.2@sha256:9f2c…`, and record that reference with the deploy. Severity: BLOCK.
- **BAN-DO-032 — Secret baked into the image.** Banned: a real credential in `ENV`/`ARG`, or `COPY .env` into any stage. Defeats: DET-INF-005. Bad: `ENV DATABASE_URL=postgres://user:realpassword@db/app` in the Dockerfile. Instead: pass the value at runtime from the platform's secret store, and use `--mount=type=secret` for anything needed during the build. Severity: BLOCK.
- **BAN-DO-033 — Installing dependencies at container start.** Banned: `npm install`, `pip install`, or equivalent in the entrypoint or start command. Defeats: DET-INF-026. Bad: `CMD ["sh", "-c", "npm install && node server.js"]` — every restart is an untested upgrade. Instead: install from the lockfile in the build stage (`npm ci`) so the shipped image already contains its dependencies. Severity: BLOCK.
- **BAN-DO-034 — Root by default in the final stage.** Banned: a final stage with no `USER` instruction, leaving the base image's root default in production. Defeats: DET-INF-022. Bad: the Dockerfile ends at `COPY --from=build /app /app` and the process runs as uid 0. Instead: create an unprivileged user in the final stage (`RUN adduser -D app`) and set `USER app` before the entrypoint. Severity: BLOCK.
- **BAN-DO-035 — Frozen base image, never rebuilt or scanned.** Banned: pinning a base image once and shipping it indefinitely with no CI scan and no rebuild cadence. Defeats: DET-INF-025. Bad: `FROM node:18.0-alpine` untouched for a year, scan step absent from the pipeline. Instead: scan every image in CI and rebuild on the scheduled cadence, advancing the pin through reviewed update PRs. Severity: WARN.

## Gates

- **G-DO-031 — Dockerfile lint.** Verifies: DO-061, DO-064, DO-067. Check: `hadolint Dockerfile` runs in CI for every Dockerfile in the repo. Pass: exit code 0 with no errors. Fail: block merge until the Dockerfile is fixed. Recorded in: progress.md.
- **G-DO-032 — Image vulnerability scan.** Verifies: DO-069. Check: `trivy image --exit-code 1 --severity CRITICAL --ignore-unfixed <image-ref>` on the built image before promotion. Pass: exit code 0 — no fixable critical vulnerabilities. Fail: block promotion; patch or rebase the image. Recorded in: progress.md.
- **G-DO-033 — Deploy reference is pinned.** Verifies: DO-062, DO-068. Check: scripted grep over deploy specs — `grep -rnE 'image:\s*\S+:(latest)?\s*$' docker-compose*.yml deploy/ k8s/` must return nothing, and the recorded deploy reference contains a version tag or `@sha256:` digest. Pass: no floating reference found; staging and production records show the identical digest. Fail: block the deploy. Recorded in: progress.md.
- **G-DO-034 — No secret in the built image.** Verifies: DO-063, DO-066. Check: `docker inspect --format '{{json .Config.Env}}' <image-ref>` contains no credential values, and `docker history --no-trunc <image-ref>` shows no `ENV`/`ARG`/`COPY` step carrying a secret; `.dockerignore` exists in the build context. Pass: both inspections clean. Fail: block promotion and rotate any exposed credential. Recorded in: progress.md.
- **G-DO-035 — Runtime smoke test.** Verifies: DO-064, DO-067, DO-070. Check: start the image; `docker exec <id> whoami` must not print `root`; `docker stop` must exit the container within the stop grace period (clean SIGTERM handling); the health check reports healthy. Pass: all three hold. Fail: block release. Recorded in: progress.md.

## Anti-patterns

- **The everything container.** App server, database, and a cron job run side by side in one container under a shell script. Catch it: more than one long-lived process in `docker top`; split into one container per process instead.
- **Rebuild-per-environment.** Staging and production each build their own image from the same commit, so the tested artifact is not the shipped one. Catch it: compare the image digests recorded per environment — they must be identical; promote, never rebuild.
- **Cache-busting copy order.** `COPY . .` lands before the dependency install, so a one-line source change rebuilds the world and CI crawls. Catch it: read the Dockerfile top to bottom; manifests and lockfile must be copied and installed first.
- **Debugging inside the image.** The final image quietly keeps a shell, package manager, and dev dependencies "just in case". Catch it: check the final stage's package list against the runtime's real needs; debug with an ephemeral debug container, not a fat production image.

## Examples

- [Example 1 — Floating single-stage Dockerfile vs pinned multi-stage](examples/example-1.md) — violates/corrects DO-061, DO-062.
- [Example 2 — Secret in `ENV` vs runtime injection](examples/example-2.md) — violates/corrects DO-063.
- [Example 3 — Root, shell-form start with install-at-start vs non-root exec form](examples/example-3.md) — violates/corrects DO-064, DO-067.

## Recall anchors

- Build once, pin the digest, promote the same image everywhere.
- Secrets ride at runtime or in BuildKit mounts — never in a layer.
- Final stage: slim, non-root, one process, exec form.
- Dependencies before source; installs happen at build time, never at start.
- If it is not scanned and rebuilt on a cadence, the pin is a time capsule.

## Checklist

- [ ] One multi-stage Dockerfile per service; final stage holds no compiler or SDK (DO-061).
- [ ] Every base image pinned to a version tag; production pinned by digest (DO-062).
- [ ] No secret in any `ENV`, `ARG`, or copied file; build secrets use BuildKit mounts (DO-063).
- [ ] Final stage sets a non-root `USER` (DO-064).
- [ ] Dependencies installed from the lockfile before source is copied (DO-065).
- [ ] `.dockerignore` committed and excludes `.git`, `.env*`, and local artifacts (DO-066).
- [ ] Exec-form entrypoint, one process per container, health check declared (DO-067, DO-070).
- [ ] Deploy specs reference a version tag or digest — never `latest` — and the reference is recorded per deploy (DO-068).
- [ ] CI scan passes with no fixable criticals; resource limits set on every container (DO-069, DO-071).
