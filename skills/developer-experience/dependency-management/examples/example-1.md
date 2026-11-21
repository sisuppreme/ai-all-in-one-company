# Example 1 — A second date library for one snippet

## Before

A change adds a "member since" label to the profile page. The manifest diff:

```diff
   "dependencies": {
     "dayjs": "1.11.13",
+    "moment": "2.30.1",
     "react": "18.3.1"
   }
```

The change description says only "add date formatting." The project already formats every date with `dayjs`; `moment` enters because a copied snippet used it, doubling the date-library weight and splitting future date work across two APIs.

## After

No manifest change. The label uses the library already in the tree:

```js
import dayjs from "dayjs";

export const memberSince = (isoDate) => dayjs(isoDate).format("MMMM YYYY");
```

Had `moment` been genuinely better, the correct change would migrate all date code to it and remove `dayjs` in the same change, with the justification written in the description.

## Note

Violates DX-063 (no justification against existing dependencies) and DX-069 / BAN-DX-034 (duplicate libraries for one job); corrected by using the dependency already in the tree.
