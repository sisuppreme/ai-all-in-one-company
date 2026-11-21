# Example 2 — Console instance nobody owns

## Before

Billing shows a large instance that appears in no Terraform state, no stack, and no diagram. It was launched from the provider console for a "quick test" a year ago, carries no tags, and has been running a side project ever since. In the allocation report its cost lands in "unallocated," where nobody is responsible for questioning it.

## After

The instance is terminated, and the test it served is recreated through IaC: the module applies the mandatory tags (service, team, environment) by default, so the resource is allocated from its first hour and appears in the tag-coverage gate. The monthly review's allocation figure rises above 90%, and any future resource created outside IaC shows up in G-DO-163 as an untagged offender with a named bypass to fix.

Note: corrects DO-324 — tags are enforced at creation by IaC defaults; untagged console resources are banned under BAN-DO-162.
