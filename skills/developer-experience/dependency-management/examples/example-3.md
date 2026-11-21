# Example 3 — One giant "update everything" change

## Before

After four months without updates, a single change titled "bump deps" raises 14 packages at once, including three majors:

```text
react-router 6.x -> 7.x   (major)
eslint       8.x -> 9.x   (major)
zod          3.x -> 4.x   (major)
+ 11 minor/patch bumps
```

The description says "tests pass." When CI fails, nobody can tell which of the 14 bumps broke the build, and none of the three majors' breaking changes were read.

## After

The same work lands as a sequence of small changes:

```text
Change 1: grouped minor/patch batch (11 packages) — suite green.
Change 2: eslint 8 -> 9 alone. Description names the breaking change
          (flat config replaces .eslintrc) and the config migration.
Change 3: zod 3 -> 4 alone. Description names the breaking changes
          and the two schema call sites updated.
Change 4: react-router 6 -> 7 alone, after 2 and 3 are merged.
```

Each change is reviewable, bisectable, and revertible on its own; each major's changelog was read before its change was written.

## Note

Violates DX-065 (updates in small batches; majors individually) and DX-066 (changelog read before a major update); corrected by splitting the majors and naming their breaking changes.
