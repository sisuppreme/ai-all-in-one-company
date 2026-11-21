# Example 2 — The font folder with its license deleted

## Before

```text
assets/fonts/inter/
  Inter-Regular.woff2
  Inter-Bold.woff2
  README.md   ("Fonts copied in for the redesign — source folder tidied, extra files removed")
```

The font files were copied in and their license file was deleted as clutter. The shipped product now contains the font with no terms, no attribution, and no record of where it came from — the vendored-file integrity scan (G-LG-054) fails.

## After

```text
assets/fonts/inter/
  Inter-Regular.woff2
  Inter-Bold.woff2
  LICENSE.txt   (SIL Open Font License 1.1, as distributed upstream)

## Component inventory (excerpt)

| Component | Version | Origin | SPDX license | Tier (hosted) | Adopted |
|---|---|---|---|---|---|
| Inter (font, 2 weights) | 4.0 | Upstream release archive | OFL-1.1 | Allowed | 2026-11-21 |
```

The upstream license file ships with the font, and the inventory row records the origin and SPDX identifier the scan checks.

## Note

Corrected under LG-107: vendored code and assets keep their license and copyright files intact — stripping them is a defect, not cleanup.
