# Example 2 — Secret in `ENV` vs runtime injection

## Before

```dockerfile
FROM node:22.11-alpine
WORKDIR /app
COPY . .
ENV DATABASE_URL=postgres://app:realpassword@db.internal:5432/app
ENV STRIPE_SECRET_KEY=sk_live_examplevalue
CMD ["node", "server.js"]
```

The credentials are baked into a layer: anyone who can pull the image can read them with `docker inspect`, and rotating them means rebuilding and redistributing the image.

## After

```dockerfile
FROM node:22.11-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev
COPY . .
CMD ["node", "server.js"]
```

```yaml
# docker-compose.yml — values come from the host/CI secret store at runtime, never from the image
services:
  app:
    image: myapp:1.4.2
    environment:
      DATABASE_URL: ${DATABASE_URL:?set in the platform secret store}
      STRIPE_SECRET_KEY: ${STRIPE_SECRET_KEY:?set in the platform secret store}
```

Note: corrects DO-063 (no secrets in any layer; runtime injection, BuildKit secret mounts for build-time needs).
