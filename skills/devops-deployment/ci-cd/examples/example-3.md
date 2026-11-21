# Example 3 — Lockfile install, CI only

## Before

```yaml
# CI installs whatever the registry resolves today
steps:
  - uses: actions/checkout@v4
  - run: npm install
  - run: npm run build
```

```dockerfile
# And the container installs again at start, so restarts change the code
CMD ["sh", "-c", "npm install && node server.js"]
```

Neither install reads the lockfile as authoritative, and every container restart can silently pull different dependency versions than the ones tested.

## After

```yaml
# CI installs exactly the locked dependency set
steps:
  - uses: actions/checkout@v4
  - run: npm ci
  - run: npm run build
```

```dockerfile
# Dependencies are installed at image build time from the lockfile;
# the running container installs nothing
COPY package.json package-lock.json ./
RUN npm ci --omit=dev
COPY . .
CMD ["node", "server.js"]
```

One locked install, in the build, is the only install; the artifact that ships is the artifact that was tested.

Note: Demonstrates DO-007 — dependencies install from the lockfile in CI, never at container start or deploy time.
