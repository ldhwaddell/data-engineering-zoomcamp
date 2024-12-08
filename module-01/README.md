# 01-docker-terraform

*.env is intentionally committed*

### Terraform

- Infrastructure as Code
- Enables us to provision resources based on config files.
- Terraform enables:
  - Easy to keep track of resources
  - Reproducibility
  - Guaranteed resource cleanup.
  - Bypass vendor GUIs.
- Terraform does not:
  - Update/manage code on the infra
  - Let you change immutable resources.
  - Manage anything defined outside of the terraform files.
- Key commands:
  - `init`: Get relevant providers
  - `plan`: Explain what is going to happen
  - `apply`: Make changes defined in tf files
  - `destroy`: Remove everything defined in tf files.

### GCP

- test
