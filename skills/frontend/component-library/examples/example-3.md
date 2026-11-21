# Example 3 — A button with two states becomes a full state matrix

## Before

The library's `Button` ships with a default style and a `:hover` darkening.
Nothing else was ever built:

- No `:focus-visible` style — keyboard users tab onto an invisible target.
- `disabled` renders at 40% opacity but still fires click handlers.
- The "Saving…" state is improvised per page: one form swaps the label,
  another shows a spinner, a third does nothing.
- A failed submit gives the button no error state at all; the failure is
  silent (DET-VIS-032).

## After

The state matrix is specified, built once in the component, and storied:

| State | Treatment | Story |
|---|---|---|
| default | token colors by variant (primary/secondary/destructive/text) | ✅ |
| hover | surface shift via token, no layout change | ✅ |
| focus-visible | 2px outline token at 3:1 contrast, offset 2px | ✅ |
| active | pressed shift, immediate | ✅ |
| disabled | muted tokens, `disabled` attribute set, no events fire | ✅ |
| loading | label replaced by spinner + action name ("Saving…"), width locked, `aria-busy="true"` | ✅ |
| error | not a button state: the form's error summary owns failure (ui-states); the button returns to default with the field errors linked | ✅ (documented exception) |

Every page now inherits the same focus ring, the same disabled semantics,
and the same loading treatment, because the behavior lives in the
component (FE-063) instead of being re-invented per form.

Note: corrects FE-062 — every component ships its full applicable state set, or the matrix states why a state does not apply.
