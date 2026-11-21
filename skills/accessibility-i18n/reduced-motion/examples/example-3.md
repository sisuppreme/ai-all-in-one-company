# Example 3 — State change carried by animation alone

## Before

Clicking "Add to cart" animates a thumbnail flying from the button to the cart icon. That animation is the entire confirmation:

```js
addBtn.addEventListener('click', () => {
  flyToCart(productThumb); // 600ms flight, then nothing persists
  addItemToCart(id);
});
```

With reduced motion on, the flight is (correctly) removed — and now the click produces no visible result at all. Users click again and add the item twice.

## After

The animation becomes decoration on top of a persistent, non-animated signal: the cart count updates as text and a polite live region announces the change, whether or not the flight plays:

```html
<button id="cart-btn">Cart (<span id="cart-count">0</span>)</button>
<p class="visually-hidden" role="status" id="cart-status"></p>
```

```js
addBtn.addEventListener('click', () => {
  addItemToCart(id);
  cartCount.textContent = String(cart.items.length);
  cartStatus.textContent = `${productName} added to cart.`;
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    flyToCart(productThumb);
  }
});
```

With animation off, the count changes and the announcement fires; the state change survives the removal of the motion that used to carry it.

Note: demonstrates AC-107 — animation is never the only carrier of meaning; every animated state change also changes text, icon, or ARIA state.
