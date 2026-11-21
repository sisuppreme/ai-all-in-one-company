# Example 2 — Copy-pasted configs replaced by one config package

## Before

```text
packages/api/tsconfig.json        (copy 1 — strict: true)
packages/ui/tsconfig.json         (copy 2 — strict: true)
packages/utils/tsconfig.json      (copy 3 — strict missing)
apps/web/tsconfig.json            (copy 4 — strict: true, paths edited)
```

Each package carries its own near-identical copy of the base TypeScript
config. One copy was never updated, so `packages/utils` compiles without
strict checks while the rest of the repo believes strict mode is universal.
The same drift applies to the ESLint and test-preset copies sitting next to
them: five files to edit for one policy change, and no way to notice the one
that was missed.

## After

```text
packages/tsconfig/base.json       (the single base config)
packages/tsconfig/package.json    (published internally as @repo/tsconfig)
```

```jsonc
// packages/utils/tsconfig.json — the whole file
{
  "extends": "@repo/tsconfig/base.json",
  "include": ["src"]
}
```

The base config lives once, in an internal config package; every package
extends it and adds only its own `include` paths. A policy change is one
edit in one file, and a package that opts out does so visibly, in its own
`tsconfig.json`, where review can see it.

Note: corrects DX-028 — shared configs live in internal config packages and are extended, never copy-pasted per package.
