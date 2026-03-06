# Overview

SignBox is a document workflow solution for preparing, sending, signing, and tracking electronic signing processes. It is designed for business scenarios where multiple people interact with the same document and the process must remain structured, traceable, and secure.

The product is split into two user-facing surfaces:
- **Internal portal**: used by initiators and operational users to create and manage signing processes
- **External portal**: used by recipients to review documents and complete signing actions

## The Core Product Journey

Every SignBox process follows the same operational model:

1. An initiator creates a process in the internal portal.
2. The initiator uploads one or more documents and selects the right document type.
3. The initiator adds recipients, roles, comments, due dates, and signing order rules.
4. SignBox sends secure invitations to recipients.
5. Recipients open the external portal, review the document, and sign, approve, or decline.
6. The initiator tracks progress and opens the completed result from history.

This is the core mental model for the whole manual. If a page feels detailed, return to this sequence first.

## What Makes SignBox Different

SignBox is not just a file upload page with a signature option. It also gives users control over process structure:
- **Document type selection** to route a process correctly
- **Role-based participation** such as signer, viewer, or approver
- **Recipient groups** for sequential signing
- **Due dates and comments** for communication and deadline control
- **Templates and contacts** for recurring business flows
- **History and process detail views** for operational follow-up

## Who Uses SignBox

### Initiators

Initiators are internal users who create processes and define how documents move through the signing flow.

Typical initiator tasks:
- upload documents
- choose document type
- add recipients and roles
- set due dates
- start the process
- monitor completion status

### Recipients

Recipients are external or internal participants who receive a signing invitation.

Typical recipient tasks:
- open the invitation
- authenticate if required
- review the document
- sign, approve, or decline

### Support and QA

Support-oriented users usually work with process history, troubleshooting, and controlled test flows.

Typical support tasks:
- locate a process in history
- verify its current state
- inspect process details
- reproduce a user-reported issue

### Administrators

Administrator-visible controls depend on tenant configuration and assigned role. In some environments, admins can see broader management options than standard users.

## Common Business Scenarios

Typical use cases include:
- employee and HR document signing
- internal approval workflows
- multi-recipient agreement signing
- signing flows that require a strict order of participants
- recurring document processes that benefit from templates

## Internal Portal vs External Portal

| Portal | Main user | Main purpose | Typical actions |
|---|---|---|---|
| Internal portal | Initiator | Build and manage processes | Upload, configure, launch, track |
| External portal | Recipient | Complete assigned action | Review, sign, approve, decline |

This distinction matters because many questions come from mixing the two experiences. If you are trying to understand what a recipient sees, use the recipient guide, not the initiator pages.

## Security and Process Discipline

> [!WARNING]
> Treat invitation links, process links, and signing access as sensitive. Do not forward them to unauthorized people.

Good operational practice in SignBox means:
- choosing the correct document type
- adding the right recipients and roles
- using anonymous mode only when appropriate for the process
- checking due dates before launch
- reviewing history instead of guessing process state

## Recommended Reading Order

If you are new to SignBox, read in this order:

1. [Terminology](terminology.md)
2. [Initiator Quick Start](initiator-quickstart.md)
3. [Initiator Deep Dive](initiator-deep-dive.md)
4. [Recipient Guide](recipient-guide.md)
5. [History](history.md)

If you are supporting users, start here instead:

1. [History](history.md)
2. [Troubleshooting](troubleshooting.md)
3. [FAQ](faq.md)

## What This Manual Covers

This repository focuses on the current SignBox user experience:
- practical user flows
- UI-based guidance
- common operational scenarios
- role-oriented navigation

It does not try to replace internal configuration, infrastructure, or API documentation.
