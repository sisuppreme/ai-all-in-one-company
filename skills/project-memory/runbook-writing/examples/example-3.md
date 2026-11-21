# Example 3 — Placeholder commands and missing prerequisites made executable

## Before

Runbook: "Rotate the API signing key" — complete text:

> 1. SSH into the app server.
> 2. Run `kubectl -n <namespace> rollout restart deployment/<app>`.
> 3. Update the key in the config and restart again.

Which server, which namespace, which deployment, where the key lives, and
what access is needed are all left for the executor to discover — during
the incident the runbook was written for.

## After

> ## Prerequisites
>
> - Cluster access: `kubectl` configured for the `prod-eu` context; your
>   account must be in the `deployers` group (check: `kubectl auth can-i
>   patch deployment -n shop` returns `yes`).
> - The new signing key is in the team vault, entry `shop/api-signing-key`
>   (retrieve the value at step 2; never paste it into the runbook, a
>   ticket, or chat).
> - Open the dashboard "Shop API — error rate" before starting.
>
> ## Steps
>
> 1. Confirm the target:
>    `kubectl --context prod-eu -n shop get deployment shop-api`
>    Expected: `shop-api` listed with the expected replica count.
> 2. Store the new key from the vault entry above:
>    `kubectl --context prod-eu -n shop create secret generic api-signing
>    --from-literal=key='<value from vault>' --dry-run=client -o yaml |
>    kubectl --context prod-eu -n shop apply -f -`
>    Expected: `secret/api-signing configured`.
> 3. Restart and watch the rollout:
>    `kubectl --context prod-eu -n shop rollout restart deployment/shop-api`
>    then `kubectl --context prod-eu -n shop rollout status deployment/shop-api`
>    Expected: `deployment "shop-api" successfully rolled out`. If the
>    rollout does not complete in 5 minutes, stop and escalate to the
>    platform on-call role.

Everything the executor needs is stated before step 1, every value is real,
and the one secret is referenced by its vault location, never written down.

Note: corrects PM-066 — prerequisites (access, credential locations, tools, dashboards) are stated up front, never discovered mid-incident.
