# Example 3 — Two cart counts replaced by one owner

## Before

```jsx
function Header() {
  const [count, setCount] = useState(0); // copy #1: updated on "add" clicks
  return <span>Cart ({count})</span>;
}

function CartPage() {
  const [items, setItems] = useState([]); // copy #2: the actual items
  return <p>{items.length} items</p>;     // disagrees with the header
}
```

Adding an item updates the header's counter; removing one on the cart page
updates only the page's list. The two numbers diverge immediately, and a
reload resets them differently again.

## After

```js
// cartStore.js — the items array is the single owner of the cart fact.
export const cartStore = {
  items: [],
  add(item)    { this.items = [...this.items, item]; },
  remove(id)   { this.items = this.items.filter(i => i.id !== id); },
  count()      { return this.items.length; },  // derived, never stored
};
```

```jsx
function Header() {
  return <span>Cart ({cartStore.count()})</span>;
}

function CartPage() {
  return <p>{cartStore.count()} items</p>;
}
```

There is one list and one way to change it; the count is computed from that
list at read time, so the header and the page cannot disagree.

Note: corrects FE-182 — one fact, one owner, one update path; counts are derived, not stored twice (FE-187).
