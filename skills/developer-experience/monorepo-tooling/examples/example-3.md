# Example 3 — Hand-ordered build script replaced by a task graph with honest caching

## Before

```jsonc
// package.json
{
  "scripts": {
    "build": "cd packages/utils && npm run build && cd ../ui && npm run build && cd ../../apps/web && npm run build"
  }
}
```

```text
# turbo.json — present, but the cache key covers source files only
cache inputs: src/**   (lockfile and env vars not included)
```

The build order is a hand-written chain: add a package or change who depends
on whom and someone must remember to edit the chain. Worse, the cache key
ignores the lockfile, so after a dependency update the runner restores the
old build output and reports a "hit" — the shipped bundle was built against
dependencies that are no longer installed.

## After

```jsonc
// turbo.json (excerpt)
{
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "inputs": ["src/**", "$TURBO_DEFAULT$", "../../pnpm-lock.yaml"],
      "env": ["NODE_ENV", "API_BASE_URL"],
      "outputs": ["dist/**"]
    }
  }
}
```

```jsonc
// package.json — the only build entry point
{
  "scripts": {
    "build": "turbo run build"
  }
}
```

Order comes from the manifests: `dependsOn: ["^build"]` builds each
package's declared dependencies first, so the graph stays correct when
packages are added or edges change. The lockfile and the environment
variables the build reads are declared inputs, and outputs are declared, so
a cache hit means the inputs genuinely did not change — verified by the
double-run check (G-DX-011) before the pipeline is trusted.

Note: corrects DX-023, DX-026, and DX-027 — the task graph is derived from declared dependencies, every task declares its outputs, and cache keys include the lockfile and relevant env vars.
