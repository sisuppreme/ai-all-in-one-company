# Example 3 — One default shadow becomes an elevation scale

## Before

```css
.card, .menu, .modal, .btn-primary, .toast {
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}
```

One soft shadow at one depth for everything: a modal floats no higher
than a card, a dropdown menu casts the same weight as a dialog, and the
light direction is implied nowhere. This is the default shadow stack
(DET-VIS-021) — a framework habit, not a decision.

## After

An elevation scale with named roles, one light direction (from above),
each step defined once as a token:

```json
{
  "elevation": {
    "flat":  { "$value": "none", "$type": "shadow",
      "$description": "Role: flat — inline surfaces, no lift" },
    "card":  { "$value": "0 1px 2px rgba(16,24,40,.06), 0 1px 3px rgba(16,24,40,.10)",
      "$type": "shadow", "$description": "Role: card — resting content surfaces" },
    "menu":  { "$value": "0 4px 8px rgba(16,24,40,.08), 0 8px 16px rgba(16,24,40,.10)",
      "$type": "shadow", "$description": "Role: menu — dropdowns, popovers" },
    "modal": { "$value": "0 12px 24px rgba(16,24,40,.12), 0 24px 48px rgba(16,24,40,.16)",
      "$type": "shadow", "$description": "Role: modal — dialogs and overlays" }
  }
}
```

Components pick by role: `box-shadow: var(--elevation-menu)`. Depth now
communicates layer order, and a reviewer can check a component's shadow
against its role instead of against taste.

Note: corrects FE-045 — elevation is a scale with named roles, applied by role, never one default everywhere.
