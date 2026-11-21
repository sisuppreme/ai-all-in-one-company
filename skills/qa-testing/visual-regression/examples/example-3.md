# Example 3 — Desktop-only suite misses mobile overflow

## Before

The visual suite covers the marketing pages and pricing table at 1280px and 1440px widths, and it is green on every pull request. The project's support matrix includes phones, but no mobile viewport was ever added to the screenshot set. On a 390px phone the pricing table's third column is clipped and the page scrolls horizontally — a state no baseline exists to catch, reported eventually by a user.

## After

The screenshot set adds the 390px mobile viewport from the support matrix for every template in the inventory. The first mobile run of the pricing page fails with a diff showing the clipped column; the table is restyled to stack below the mobile breakpoint, a reviewed baseline PR accepts the new mobile screenshots, and later regressions at that width fail mechanically in CI.

Note: demonstrates QA-087 — screenshot viewports match the project's stated support matrix, including one mobile width.
