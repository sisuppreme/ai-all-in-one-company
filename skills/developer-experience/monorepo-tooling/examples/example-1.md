# Example 1 — Reach-across import replaced by a declared dependency

## Before

```ts
// apps/web/src/lib/session.ts
import { getSession } from "../../../packages/api/src/internal/session";
```

`apps/web` reaches into the API package's source tree by relative path, and
`@repo/api` appears nowhere in the web app's manifest. The import resolves
only because the files happen to sit in those folders: moving `session.ts`
inside the API package breaks the web build, the task graph has no edge from
`web` to `api`, so CI does not rebuild `web` when the API package changes,
and the API package's internal layout has silently become a public contract.

## After

```jsonc
// apps/web/package.json
{
  "dependencies": {
    "@repo/api": "workspace:*"
  }
}
```

```ts
// apps/web/src/lib/session.ts
import { getSession } from "@repo/api";
```

The dependency is declared in the manifest, the import goes through the API
package's public entry point, and the task graph now carries the `web → api`
edge, so a change to the API package rebuilds and retests the web app.

Note: corrects DX-023 and DX-024 — internal dependencies are declared in the manifest, and packages are imported only through their entry points.
