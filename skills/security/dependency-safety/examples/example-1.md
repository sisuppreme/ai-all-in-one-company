# Example 1 — Floating range, no lockfile

## Before

```json
{
  "dependencies": {
    "express": "*",
    "lodash": "latest"
  }
}
```

CI runs plain `npm install`; no lockfile is committed, so every build resolves whatever versions are current that day.

## After

```json
{
  "dependencies": {
    "express": "4.21.2",
    "lodash": "4.17.21"
  }
}
```

`package-lock.json` is committed, and CI installs with `npm ci`, so the reviewed lockfile — not the registry's current state — is the build input.

Note: corrects SE-101 and SE-111; the "before" is BAN-SE-051.
