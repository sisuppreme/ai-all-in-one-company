# Example 3 — Root, shell-form start with install-at-start vs non-root exec form

## Before

```dockerfile
FROM node:22.11-alpine
WORKDIR /app
COPY . .
CMD sh -c "npm install && node server.js"
```

The process runs as root, the shell is PID 1 so the app never receives `SIGTERM` and is hard-killed on every stop, and each restart reinstalls dependencies — an untested upgrade on every boot.

## After

```dockerfile
FROM node:22.11-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev
COPY . .
RUN addgroup -S app && adduser -S app -G app && chown -R app:app /app
USER app
HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://127.0.0.1:3000/health || exit 1
CMD ["node", "server.js"]
```

Dependencies are installed once at build time from the lockfile, the app runs as the unprivileged `app` user, and exec-form `CMD` makes the app PID 1 so it shuts down cleanly on `SIGTERM`.

Note: corrects DO-064 (final stage runs non-root) and DO-067 (one process, exec form, PID 1 signal handling).
