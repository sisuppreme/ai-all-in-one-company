# Example 1 — A gate that actually gates

## Before

```yaml
# .github/workflows/test.yml — runs after merge, and cannot fail the build
on:
  push:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install
      - run: npm test
        continue-on-error: true # suite is flaky, revisit later
```

The workflow runs only after code is already on `main`, and `continue-on-error` turns every failure green. Nothing blocks a bad merge.

## After

```yaml
# .github/workflows/test.yml — required check on the protected branch
on:
  push:
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test
```

Branch protection lists the `test` check as required, so a red run blocks merge; the flaky test is fixed or quarantined in the open instead of silenced.

Note: Demonstrates DO-003 and DO-006 — required status checks, and no `continue-on-error` on a gating job.
