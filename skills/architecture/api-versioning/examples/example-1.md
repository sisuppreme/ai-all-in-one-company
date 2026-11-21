# Example 1 — A field rename shipped as v2, not as a quiet v1 break

## Before

A developer renames the order field `total_price` to `grand_total` for clarity and ships it in `/v1/` as a minor release. Renaming a field is on the breaking list, but nobody checks. Every v1 client that reads `total_price` starts failing the same morning.

## After

The rename is classified against the compatibility list first: rename = breaking. The change ships in `/v2/orders` with `grand_total`; `/v1/` keeps `total_price` unchanged and enters its deprecation window. The `oasdiff breaking` gate compares the new v1 spec against the shipped baseline and would have failed the original change automatically.

## Note

Corrects AR-084 (a breaking change shipped under the same major version is a release-blocking defect).
