<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/brand/trustlynx-logo-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="assets/brand/trustlynx-logo-light.png">
    <img src="assets/brand/trustlynx-logo-light.png" width="400" alt="TrustLynx">
  </picture>
</p>

<p align="center">
  <img src="assets/trustlynx-signbox-workflow.svg" width="1000" alt="TrustLynx SignBox workflow">
</p>

# SignBox User Manual (TrustLynx)

SignBox helps employees create document signing processes and helps recipients sign documents securely online.

## Who this guide is for
- Initiators (employees who create signing processes)
- Recipients/signers (people who receive and sign or decline)
- Testers and support staff

> [!NOTE]
> This repository contains user-focused documentation for the current TrustLynx SignBox UI.

## Personas
- **I am a new initiator**: start with [Initiator Quick Start](docs/initiator-quickstart.md), then [Initiator Deep Dive](docs/initiator-deep-dive.md)
- **I am a recipient**: go to [Recipient Guide](docs/recipient-guide.md)
- **I am support/QA**: use [History](docs/history.md), [Troubleshooting](docs/troubleshooting.md), [FAQ](docs/faq.md)

## Table of Contents
1. [Terminology](docs/terminology.md)
2. [Overview](docs/overview.md)
3. [Initiator Quick Start](docs/initiator-quickstart.md)
4. [Initiator Deep Dive](docs/initiator-deep-dive.md)
5. [Contacts and Templates](docs/contacts-and-templates.md)
6. [Recipient Guide](docs/recipient-guide.md)
7. [History](docs/history.md)
8. [Troubleshooting](docs/troubleshooting.md)
9. [FAQ](docs/faq.md)
10. [User and Access Management](docs/access-management.md)
11. [Glossary](docs/glossary.md)
12. [New User Simulation](docs/new-user-simulation.md)
13. [Coverage Report](docs/coverage-report.md)
14. [Screenshot Style Guide](docs/style-guide.md)

## Screenshot generation
To regenerate sanitized + annotated screenshots:

```bash
python scripts/sanitize_screenshots.py specs/redactions.yml
python scripts/annotate_screenshots.py specs/annotations.yml
```
