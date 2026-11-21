# preview-environments

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://docs.Netlify.com/site-deploys/create-deploys ; https://vercel.com/docs/v1/features/repositories/
- **Depends on:** ci-cd
- **Feeds into:** deployment-strategies

## When to use / Do NOT use

- **Use when:** A project has pull requests that need reviewable, running builds — platform-native previews (Vercel/Netlify Deploy Previews) or a pipeline-spun namespace/stack per PR.
- **Do NOT use when:** The change is production release mechanics (use deployment-strategies) or the pipeline itself is missing (build ci-cd first); a preview is never a substitute for staging-for-approval.

## Rules

1. **DO-021 — One preview per pull request, created automatically.** Opening or updating a PR creates or refreshes exactly one preview environment and posts its URL on the PR; no preview is created by hand.
2. **DO-022 — Previews never touch production data.** Each preview uses its own database (or schema/namespace) seeded with non-production data; the preview's database host must differ from the production host.
3. **DO-023 — Previews never hold production credentials.** Preview environments receive a separate, least-privilege secret set; no production API key, token, or password is present in the preview's environment variables.
4. **DO-024 — Same artifact path as production.** The preview is built by the same pipeline and artifact path that produces staging and production builds; previews are never built by a local script or a divergent build command.
5. **DO-025 — Config differs by values, never by code path.** Preview and production run the same code; every behavioral difference comes from environment variable values, with no preview-only branches, flags hardcoded on, or conditional build steps.
6. **DO-026 — Teardown is automatic.** Merging or closing the PR destroys its preview — app, database, and DNS/subdomain — within the documented teardown window recorded in the project config.
7. **DO-027 — Preview count and age are capped and visible.** A maximum number of live previews and a maximum age (TTL) are set in config; a scheduled sweep lists live previews and tears down any that exceed either limit.
8. **DO-028 — The preview serves the PR's commit.** The preview response identifies the commit it serves (build metadata endpoint, header, or footer injected at build time) and that SHA equals the PR head SHA.
9. **DO-029 — Previews are not publicly discoverable.** Every preview response carries `X-Robots-Tag: noindex` (or access control); no preview URL is linked from production pages or sitemaps.
10. **DO-030 — Debug surfaces stay off in previews.** Debug mode, verbose error pages, and admin/test endpoints are disabled in preview config exactly as in production config.
11. **DO-031 — The preview URL is the unit of review.** Reviewers verify the change on the preview URL, and the PR records which preview URL and commit SHA were reviewed before merge.
12. **DO-032 — Preview failures block like CI failures.** A failed preview build or a preview serving the wrong commit is a red status on the PR, treated as a stop, not background noise.

## BAN list

- **BAN-DO-011 — Preview wired to the production database.** Banned: a preview environment whose `DATABASE_URL` (or equivalent) resolves to the production database host. Defeats: DET-INF-003. Bad: the PR preview for a billing change reads and writes the live `orders` table during review. Instead: provision a per-preview database seeded with synthetic data and point the preview at it. Severity: BLOCK.
- **BAN-DO-012 — Production secrets copied into preview config.** Banned: reusing production API keys, tokens, or passwords as preview environment values "to make it work." Defeats: DET-INF-003. Bad: the preview deploy carries the live payment provider secret key, so a test checkout charges real cards. Instead: issue separate sandbox/test-mode credentials scoped to the preview only. Severity: BLOCK.
- **BAN-DO-013 — Preview built outside the pipeline.** Banned: building or updating a preview by hand — local build, FTP upload, or SSH rebuild — instead of the CI artifact path. Defeats: DET-INF-004. Bad: a developer runs a deploy script from a laptop so the preview shows code that exists in no commit. Instead: let the pipeline build the PR's commit and deploy that artifact to the preview. Severity: BLOCK.
- **BAN-DO-014 — The immortal preview.** Banned: a preview left running indefinitely after its PR merged or closed, kept "just in case" as an unofficial second site. Defeats: DET-INF-027. Bad: forty stale preview subdomains from closed PRs still serve old builds on the shared quota. Instead: tear the preview down automatically on merge/close and sweep for orphans past the TTL. Severity: WARN.

## Gates

- **G-DO-011 — Preview serves the PR commit (automated).** Verifies: DO-021, DO-028. Check: open a test PR, wait for the preview comment, then run `curl -s <preview-url>/.well-known/build-info.json` (or the project's build-metadata path) and compare its `commit` field to the PR head SHA. Pass: HTTP 200 and the SHAs match exactly. Fail: block merge until the preview rebuilds. Recorded in: progress.md.
- **G-DO-012 — Preview isolation audit (automated).** Verifies: DO-022, DO-023. Check: script reads the preview environment's resolved config and asserts its database host differs from the production host and none of the production secret values appear in the preview value set. Pass: zero matches on both assertions. Fail: block the preview, rotate any exposed production secret. Recorded in: progress.md.
- **G-DO-013 — Teardown on close (automated).** Verifies: DO-026, DO-027. Check: close the test PR, then poll the preview URL every 60 seconds; it must return 404/410 (or fail DNS) within the documented teardown window. Pass: preview unreachable inside the window. Fail: raise a teardown defect and run the orphan sweep. Recorded in: progress.md.
- **G-DO-014 — Review evidence on the PR.** Verifies: DO-029, DO-031. Check: before merge, confirm the PR thread contains the preview URL, the reviewed commit SHA, and a reviewer note; fetch the preview URL and confirm the `X-Robots-Tag: noindex` header is present. Pass: all three items present and the header is set. Fail: hold the merge. Recorded in: progress.md.

## Anti-patterns

- **Preview theater.** A preview URL is posted on every PR but nobody opens it; review happens from screenshots in chat. Catch it: the PR has no recorded preview URL/SHA review note (G-DO-014 fails).
- **The golden preview.** One long-lived "preview" branch environment is hand-tuned until it no longer matches what the pipeline would build. Catch it: its build predates the current pipeline config or its env values were edited in a console.
- **Seed-data cosplay.** The preview database is a copied production snapshot with names lightly renamed — real user data in disguise. Catch it: row counts and email domains match production patterns instead of the synthetic seed set.
- **Quota blindness.** Previews multiply silently until the platform's build minutes or preview cap stop all deploys, including production. Catch it: no dashboard or sweep output shows live preview count and age.

## Examples

- [Example 1 — Preview database isolation](examples/example-1.md) — violates/corrects DO-022.
- [Example 2 — Pipeline-built preview](examples/example-2.md) — violates/corrects DO-024.
- [Example 3 — Automatic teardown](examples/example-3.md) — violates/corrects DO-026.

## Recall anchors

- One PR, one preview, posted automatically.
- Never production data, never production secrets.
- Same artifact path as production — values differ, code does not.
- Merge or close means teardown.
- The preview URL and its SHA are the unit of review.

## Checklist

- [ ] Opening a test PR produced a preview URL on the PR (DO-021).
- [ ] Preview database host differs from production and holds only synthetic seed data (DO-022).
- [ ] No production secret value appears in the preview environment (DO-023, G-DO-012).
- [ ] Preview was built by the pipeline from the PR head commit, and its build metadata shows that SHA (DO-024, DO-028, G-DO-011).
- [ ] Preview responses carry `X-Robots-Tag: noindex` and debug surfaces are off (DO-029, DO-030).
- [ ] Closing the test PR removed the preview within the documented window (DO-026, G-DO-013).
- [ ] Live preview count and oldest age are within the configured caps (DO-027).
- [ ] The PR records the preview URL and commit SHA that were reviewed (DO-031, G-DO-014).
