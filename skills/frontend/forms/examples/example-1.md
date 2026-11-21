# Example 1 — Placeholder-only input replaced by a labeled control

Corrects rule **FE-241** (every control has a visible, associated label).

## Before

```html
<!-- The placeholder is the only label. It vanishes on typing,
     and a screen reader announces an unnamed edit field. -->
<form>
  <input type="email" name="email" placeholder="Email address">
  <input type="password" name="password" placeholder="Password">
  <button type="submit">Sign in</button>
</form>
```

## After

```html
<!-- Visible labels tied with for/id; the hint is announced with
     the field via aria-describedby; placeholders show format only. -->
<form>
  <div>
    <label for="email">Email address</label>
    <input id="email" name="email" type="email" autocomplete="email"
           placeholder="you@example.com" required>
  </div>
  <div>
    <label for="password">Password</label>
    <input id="password" name="password" type="password"
           autocomplete="current-password" aria-describedby="pw-hint" required>
    <p id="pw-hint">Use the password you chose when you created your account.</p>
  </div>
  <button type="submit">Sign in</button>
</form>
```

Note: the before version is BAN-FE-121 — once the user types, no label remains. The after version keeps labels visible and gives forms-mode screen readers the label and hint together.
