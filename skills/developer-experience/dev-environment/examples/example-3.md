# Example 3 — CI on a different Node

## Before

```yaml
# .github/workflows/ci.yml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: "lts/*"        # whatever is current on the day CI runs
  - run: npm install               # resolves fresh; lockfile may be rewritten
```

```markdown
<!-- README.md -->
You need Node 18 installed. (The last developer used 20; both "worked".)
```

Laptop, README, and CI each name a different Node version, and CI resolves dependencies fresh — so a build can pass locally, fail in CI, and pass again next week with no code change.

## After

```toml
# mise.toml — the single source of tool versions, used by laptops and CI
[tools]
node = "20.11.1"
pnpm = "9.1.0"
```

```yaml
# .github/workflows/ci.yml
steps:
  - uses: jdx/mise-action@v2       # installs exactly what mise.toml pins
  - run: pnpm install --frozen-lockfile
  - run: pnpm test
```

```markdown
<!-- README.md -->
Run `make setup`. Tool versions are pinned in `mise.toml`; do not install
Node or pnpm by hand.
```

One pin file is the only place a version is stated; CI and laptops install from it identically, and the frozen lockfile makes the dependency set reproducible.

## Note

Corrected under DX-009: CI installs from the same pin file and lockfile as a laptop; the Before also violates DX-003 (floating `lts/*`) and DX-002 (versions restated in three places instead of one pin file).
