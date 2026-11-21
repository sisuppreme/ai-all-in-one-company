# Example 2 — Wildcard range and a regenerated lockfile

## Before

A feature change "fix login redirect" includes this manifest edit and a fully regenerated lockfile:

```diff
   "dependencies": {
-    "axios": "1.7.9",
+    "axios": "*",
     "react": "18.3.1"
   }
```

`package-lock.json` shows 40 changed transitive versions that nobody reviewed, and `"*"` means every future install resolves to whatever axios version exists that day — two machines, two different trees.

## After

The version is an exact pin, and the lockfile changes only in a dedicated update change:

```diff
   "dependencies": {
-    "axios": "1.7.9",
+    "axios": "1.8.4",
     "react": "18.3.1"
   }
```

The update change is produced by the update bot, its lockfile diff is the review, and CI proves reproducibility: `npm ci` exits 0 and `git status --porcelain` shows the lockfile untouched.

## Note

Violates DX-067 / BAN-DX-032 (wildcard range) and DX-061 / BAN-DX-031 (lockfile regenerated inside an unrelated change); corrected by an exact pin and a dedicated, reviewable update.
