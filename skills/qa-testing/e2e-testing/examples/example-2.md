# Example 2 — Reload before you believe the toast

## Before

```ts
test('user can update their display name', async ({ page }) => {
  await page.getByLabel('Display name').fill('Ada Lovelace');
  await page.getByRole('button', { name: 'Save' }).click();
  await expect(page.getByText('Profile updated')).toBeVisible();
});
```

The toast renders from local state. The save request can fail, post nowhere, or
write a value that never comes back — this test passes in all three cases.

## After

```ts
test('display name persists across reload and re-login', async ({ page }) => {
  const name = `Ada ${uniqueSuffix()}`;
  await page.getByLabel('Display name').fill(name);
  const writeRequest = page.waitForRequest(
    (r) => r.method() === 'PATCH' && r.url().includes('/api/profile'),
  );
  await page.getByRole('button', { name: 'Save' }).click();
  await writeRequest; // the write actually left the browser (QA-048)
  await page.reload();
  await expect(page.getByLabel('Display name')).toHaveValue(name);
  await signOut(page);
  await signIn(page);
  await expect(page.getByLabel('Display name')).toHaveValue(name);
});
```

Note: corrects QA-046 and BAN-QA-022 — a mutation is proven by reload and re-read, never by the success toast alone.
