# Example 1 — The decline card is a journey, not an afterthought

## Before

```ts
test('checkout succeeds', async ({ page }) => {
  await page.getByRole('button', { name: 'Pay' }).click();
  await page.getByLabel('Card number').fill('4242 4242 4242 4242');
  await page.getByRole('button', { name: 'Confirm payment' }).click();
  await expect(page.getByText('Order confirmed')).toBeVisible();
});
```

The only card ever used is the always-approve test card. A build whose decline
path shows "Success" for a declined card passes this suite untouched.

## After

```ts
test('checkout charges and persists the order', async ({ page }) => {
  // ... provision a fresh account and cart inside this test (QA-043)
  await page.getByLabel('Card number').fill('4242 4242 4242 4242');
  await page.getByRole('button', { name: 'Confirm payment' }).click();
  await expect(page.getByText('Order confirmed')).toBeVisible();
  await page.reload();
  await expect(page.getByText('Order #')).toBeVisible(); // persisted, QA-046
});

test('decline card declines visibly and creates no order', async ({ page }) => {
  // ... provision a fresh account and cart inside this test (QA-043)
  const ordersBefore = await countOrders(page);
  await page.getByLabel('Card number').fill('4000 0000 0000 0002'); // generic decline
  await page.getByRole('button', { name: 'Confirm payment' }).click();
  await expect(page.getByText('Your card was declined')).toBeVisible();
  expect(await countOrders(page)).toBe(ordersBefore);
});
```

Note: corrects QA-047 and BAN-QA-021 — failure paths are journeys; a payment suite that never declines cannot detect a checkout that accepts everything.
