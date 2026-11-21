# Example 3 — State moved to a remote locked backend

## Before

Terraform runs from one developer's laptop against a local `terraform.tfstate` file that gets committed to the repo "so everyone has it." The file contains plaintext database passwords. Two people running applies in the same week overwrite each other's state, resources are double-created, and the recovery plan for a lost laptop is unclear — the state file is the only map from code to real resources.

## After

State lives in a remote backend with locking and access control, so concurrent applies are serialized and the state survives any single laptop. State files are added to `.gitignore`, the repository history copy is treated as a secret exposure — every credential it contained is rotated — and the remote state is itself backed up. CI runs plan and apply against the shared backend, so the whole team works from one locked, current map.

Note: demonstrates DO-103 — state is remote, locked, and access-controlled, never a local file passed around the team.
