# Example 1 — Platform-built release

Note: demonstrates SE-121 and SE-122 — releases are built by the platform from a named commit, with platform-generated provenance (BAN-SE-061, DET-INF-004).

## Before

```bash
# Release 1.4.0, built on the developer's workstation and pushed by hand.
# Nothing records which commit, dependencies, or machine produced it.
docker build -t registry.example.com/app:1.4.0 .
docker push registry.example.com/app:1.4.0
kubectl set image deploy/app app=registry.example.com/app:1.4.0
```

## After

```yaml
# .github/workflows/release.yml — the platform builds from the tagged
# commit, generates and signs provenance, and pushes by digest.
on:
  push:
    tags: ["v*"]
jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      id-token: write        # lets the platform sign provenance
      contents: read
    steps:
      - uses: actions/checkout@<40-char-sha> # v4
      - name: Build, attest, and push
        run: |
          docker build -t registry.example.com/app:${{ github.ref_name }} .
          # platform step: generates SLSA provenance for the pushed digest
          # and records it in the release record before deploy is allowed
```

Only the digest this job produced may be deployed; a workstation build has no provenance and fails G-SE-061.
