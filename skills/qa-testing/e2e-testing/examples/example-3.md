# Example 3 — Replace the sleep with an assertion

## Before

```ts
test('document shows as synced after save', async ({ page }) => {
  await page.getByRole('button', { name: 'Save' }).click();
  await page.waitForTimeout(5000);
  await expect(page.locator('.sync-badge')).toHaveText('Synced');
});
```

The fixed wait hides the real behavior: the test passes on fast machines even
when sync is broken, and flakes on slow ones when sync works. The CSS selector
also breaks the moment the badge is restyled.

## After

```ts
test('document shows as synced after save', async ({ page }) => {
  const saved = page.waitForResponse(
    (r) => r.url().includes('/api/documents') && r.request().method() === 'PUT',
  );
  await page.getByRole('button', { name: 'Save' }).click();
  await saved;
  await expect(page.getByRole('status', { name: 'Sync status' })).toHaveText('Synced');
});
```

The web-first assertion auto-waits for the actual state: it fails the moment
sync stops working, and it waits exactly as long as the app needs — no more.

Note: corrects QA-042 and BAN-QA-024 — never sleep; wait on the response and assert the visible state by role.
