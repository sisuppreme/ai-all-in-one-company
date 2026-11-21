# Example 2 — Pinning the loader instead of shipping "latest"

## Before

The integration guide tells every host to paste a snippet that always
pulls the newest build:

```html
<script src="https://cdn.example.com/widget/latest.js" async></script>
<div data-acme-widget data-plan="pro"></div>
```

A breaking change ships on a Friday and silently rewrites the checkout
widget on hundreds of host sites at once. Hosts cannot roll back —
there is no version to roll back to — and support cannot reproduce a
bug report because no two reporters are running the same code.

## After

The loader is an immutable, semantically versioned artifact; the
documented snippet pins it, and each release carries a changelog entry
and a supported-versions policy:

```html
<script src="https://cdn.example.com/widget/loader@1.4.0.js" async></script>
<div data-acme-widget data-plan="pro"></div>
```

```text
Release 1.4.0 → loader@1.4.0.js is immutable once published; fixes
                ship as 1.4.1, never as an overwrite.
Docs          → the install snippet, the examples, and the loader
                header all carry the same version string (checked by
                the version-pin gate).
Policy        → versions 1.3.x and 1.4.x are supported; hosts on
                older pins get an upgrade notice, not a surprise.
```

Hosts upgrade on their own schedule, a bad release is rolled back by
changing one version string, and every bug report names the exact code
that produced it.

Note: corrects IN-225 — the loader is versioned and immutable per version; "latest" URLs are development-only and never the documented production integration.
