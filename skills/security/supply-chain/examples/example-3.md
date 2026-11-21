# Example 3 — SHA-pinned CI actions

Note: demonstrates SE-126 — third-party CI actions are pinned by full commit SHA, not by a mutable tag (BAN-SE-063, DET-INF-026).

## Before

```yaml
# Tags are movable: whoever controls the action repo can re-point
# v4 or main at new code, and the next run executes it with the
# pipeline's credentials.
steps:
  - uses: actions/checkout@v4
  - uses: some-org/deploy-action@main
```

## After

```yaml
# Full commit SHAs are immutable references; the trailing comment
# records the human-readable version for the update bot and reviewers.
steps:
  - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
  - uses: some-org/deploy-action@3fa9c1e72b4d8a05f6c19e2b7d04a8c5e6f1a2b3 # v2.7.0
```

Dependabot/Renovate proposes SHA bumps as reviewed pull requests, so pinning stays current instead of freezing (SE-129); G-SE-063 lints every workflow for unpinned references.
