# Example 3 — Optimistic delete with rollback

## Before

```jsx
const deleteOrder = useMutation({
  mutationFn: (id) => fetch(`/api/orders/${id}`, { method: 'DELETE' }),
  onMutate: (id) => {
    // Row vanishes instantly — and if the request fails, it stays vanished
    // on screen while still existing on the server, until a manual reload.
    queryClient.setQueryData(['orders'], (old) =>
      old.filter(o => o.id !== id));
  },
});
```

The user is told, in effect, that the delete succeeded. When it did not, the
interface is lying — a delete that only hides.

## After

```jsx
const deleteOrder = useMutation({
  mutationFn: (id) =>
    fetch(`/api/orders/${id}`, { method: 'DELETE' }).then(r => {
      if (!r.ok) throw new Error('delete failed');
    }),
  onMutate: async (id) => {
    await queryClient.cancelQueries({ queryKey: ['orders'] });
    const previous = queryClient.getQueryData(['orders']);  // snapshot
    queryClient.setQueryData(['orders'], (old) =>
      old.filter(o => o.id !== id));
    return { previous };                                    // rollback data
  },
  onError: (_err, _id, context) => {
    queryClient.setQueryData(['orders'], context.previous); // restore
    showErrorState('That order could not be deleted. It has been restored.');
  },
  onSettled: () => {
    queryClient.invalidateQueries({ queryKey: ['orders'] }); // reconcile
  },
});
```

The optimistic removal is instant as before, but a failure restores the exact
pre-mutation data and surfaces the error state — the interface never claims a
result the server did not confirm.

Note: corrects FE-207 — optimistic updates always carry a rollback path on mutation failure.
