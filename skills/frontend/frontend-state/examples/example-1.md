# Example 1 — Server mirror replaced by the query cache

## Before

```js
// store.js — the orders list is fetched once, copied into the store,
// and then patched by hand after every mutation.
const store = {
  orders: [],
  async loadOrders() {
    const res = await fetch('/api/orders');
    this.orders = await res.json();          // mirror copy #1
  },
  async cancelOrder(id) {
    await fetch(`/api/orders/${id}`, { method: 'DELETE' });
    this.orders = this.orders.filter(o => o.id !== id);  // hand sync
  },
};
```

Every new mutation needs its own hand-written patch, and any patch that is
missed — or a change made by another session — leaves the dashboard showing
numbers the API no longer agrees with.

## After

```js
// Server data is never stored here. The store holds UI state only.
const uiStore = {
  state: { selectedOrderId: null, sidebarOpen: false },
  selectOrder(id) { this.state.selectedOrderId = id; },
};

// Orders live in the query cache (data-fetching). Components read them
// through the query layer, and mutations invalidate instead of patching:
//   useQuery({ queryKey: ['orders'], queryFn: fetchOrders })
//   useMutation({ mutationFn: cancelOrder,
//                 onSuccess: () => queryClient.invalidateQueries({ queryKey: ['orders'] }) })
```

There is exactly one copy of the orders data — the server's, viewed through
the cache — so it cannot drift from the truth, and a mutation needs no
synchronization code at all.

Note: corrects FE-184 — server data is never copied into the client store and hand-synchronized.
