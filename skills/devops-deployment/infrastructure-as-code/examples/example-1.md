# Example 1 — Console-built network declared and imported

## Before

The production VPC, its subnets, and its security groups were created by clicking through the cloud console during launch week. The repo contains no network configuration at all. When the security group needs a new rule, someone logs in, adds it, and tells the team in chat. Nobody can say what the full rule set is without opening the console, and a second environment cannot be built because the "configuration" is one person's memory.

## After

The network is declared in a versioned Terraform module in the repo. The existing VPC, subnets, and security groups are imported into state so the code describes the real resources, the generated configuration is reviewed and cleaned up, and `terraform plan` converges to no changes. From then on, a new security group rule is a pull request: plan output shows the exact rule being added, a reviewer approves it, and CI applies it.

Note: demonstrates DO-101 — everything durable is declared in code, not held in a console session.
