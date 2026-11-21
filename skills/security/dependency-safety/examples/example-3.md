# Example 3 — Unpinned base image

## Before

```dockerfile
FROM node:latest
WORKDIR /app
COPY . .
CMD ["node", "server.js"]
```

The base image is whatever `latest` points to on build day: unreviewed OS and runtime changes enter production silently, and the image is never rebuilt for OS patches.

## After

```dockerfile
FROM node:22-bookworm-slim@sha256:<digest-of-the-reviewed-image>
WORKDIR /app
COPY . .
CMD ["node", "server.js"]
```

The digest is pinned, update automation opens a PR when a newer digest is published, and the monthly rebuild is scanned before it replaces the running image.

Note: corrects SE-110; the "before" is BAN-SE-054.
