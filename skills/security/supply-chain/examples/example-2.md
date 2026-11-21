# Example 2 — Deploy by digest

Note: demonstrates SE-124 and SE-125 — deploys reference the verified digest, never a mutable tag (BAN-SE-062, DET-INF-026).

## Before

```yaml
# deploy/production.yaml — "latest" can point at anything by tonight:
# a re-pushed tag silently changes what production runs on restart.
containers:
  - name: app
    image: registry.example.com/app:latest
```

## After

```yaml
# deploy/production.yaml — the exact artifact the build produced,
# signed provenance for, and recorded in build/digest.txt.
containers:
  - name: app
    image: registry.example.com/app@sha256:9f2c1e4b8a7d3f05c6e1a2b4d8f0e3c5a7b9d1f2e4a6c8b0d3f5a7c9e1b2d4f6a8
```

The deploy step verifies the signature and digest before applying (G-SE-062 diffs this digest against the build record); a tag change alone can never alter what runs.
