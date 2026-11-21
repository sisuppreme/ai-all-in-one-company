# Example 1 — Permanent flag and dead branch removed at rollout completion

## Before

```ts
// Registry: new_checkout — release flag, created 8 months ago, expiry extended 3 times
if (flags.isOn("new_checkout", user)) {
  return renderNewCheckout(cart);
}
return renderLegacyCheckout(cart); // unmaintained, but still "supported"
```

The rollout finished months ago: the flag is at 100% and the legacy branch
is dead weight that every checkout change must still tiptoe around. The
registry entry's expiry has been extended three times instead of triggering
removal.

## After

```ts
return renderNewCheckout(cart);
```

…and in the same change: the legacy renderer and its tests are deleted, the
`new_checkout` key is removed from the registry (the audit log keeps its
history), and the registry-vs-codebase diff confirms no reference remains.
One checkout exists, one path is maintained, and the flag system is back to
holding only switches that can still move.

Note: corrects BE-067 — expiry is enforced and removal of the flag, registry entry, and dead branch is part of the feature's definition of done.
