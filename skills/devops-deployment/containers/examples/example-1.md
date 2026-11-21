# Example 1 — Floating single-stage Dockerfile vs pinned multi-stage

## Before

```dockerfile
FROM node
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "server.js"]
```

One stage ships the full Node SDK and dev dependencies to production, the base image floats on whatever `node` means today, and `COPY . .` before the install busts the dependency layer cache on every source change.

## After

```dockerfile
FROM node:22.11-alpine@sha256:1d9a5a3c6f0e8b7d4a2c5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:22.11-alpine@sha256:1d9a5a3c6f0e8b7d4a2c5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
CMD ["node", "dist/server.js"]
```

Note: corrects DO-061 (multi-stage, slim runtime) and DO-062 (base image pinned by version tag and digest).
