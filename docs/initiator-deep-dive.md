# Initiator Deep Dive

This page explains the process creation form in detail and merges the practical field guidance that experienced users usually need after the first successful process.

## Upload Area and Document Container Logic

### Uploading one or more files

Use the upload area in `Home` to add the file or files that belong to the signing process.

<p align="center">
  <img src="../assets/annotated/step-02-upload.png" width="900" alt="Upload area highlighted">
  <br><em>Figure 1 - Upload area in process form.</em>
</p>

What happens next:
- one uploaded file usually creates one signing item
- multiple uploaded files are grouped into one container-based signing process
- output format and archive behavior depend on tenant configuration and selected document type

Practical note:
- If your organization uses document profiles heavily, always choose the document type before final validation.

## Document Type

The `Document type` field is more than a label. It usually defines how the process should be handled downstream.

Typical effects of document type:
- process profile selection
- archive mapping
- metadata routing
- available signing rules for the process

<p align="center">
  <img src="../assets/annotated/step-03-doctype-open.png" width="900" alt="Document type dropdown open">
  <br><em>Figure 2 - Document type dropdown in open state.</em>
</p>

What to do:
- select the document type that matches the business purpose of the file
- if there is only one configured type in your tenant, the field may be hidden

Common mistake:
- choosing a generic type when a contract-, approval-, or archive-specific profile exists

## Recipient Setup

Recipient setup defines who participates, how they participate, and in what order they are allowed to act.

<p align="center">
  <img src="../assets/annotated/step-04-recipient-fields.png" width="900" alt="Recipient fields highlighted">
  <br><em>Figure 3 - Recipient fields for signer setup.</em>
</p>

### Required recipient fields

Typical recipient fields:
- full name
- country
- personal code, if required by the selected identity model
- email
- role

### Country

The `Country` field influences available authentication/signing methods and, in non-anonymous flows, helps validate recipient identity together with personal code.

<p align="center">
  <img src="../assets/annotated/step-14-country-open.png" width="900" alt="Country dropdown open">
  <br><em>Figure 4 - Country dropdown opened with options.</em>
</p>

### Anonymous

Use `Anonymous` only when your process policy allows a recipient flow without personal-code-based matching.

<p align="center">
  <img src="../assets/annotated/step-05-anonymous-checkbox.png" width="900" alt="Anonymous checkbox highlighted">
  <br><em>Figure 5 - Anonymous checkbox location.</em>
</p>

Behavior:
- non-anonymous recipient matching normally relies on `personalCode + country`
- anonymous flow skips personal-code matching
- anonymous does not make the process public
- access still depends on the correct invitation link and valid process state

### Recipient roles

Typical role meanings:
- `Signer`: can sign the document and follow the process
- `Viewer`: can open and review the process without signing
- `Approver`: can approve without adding a signature, if this role is enabled in your tenant

Practical note:
- the exact role list may be tenant-specific
- all recipients are usually signers by default unless changed manually

## Recipient Groups and Signing Order

Recipient groups define workflow steps.

One recipient group:
- all recipients in that group can usually act in parallel

Multiple recipient groups:
- later groups wait until earlier groups are completed
- use this for sequential signing or staged approval

This is one of the most important concepts in SignBox. If a recipient is not receiving an invitation yet, the most common reason is that an earlier group is still active.

## Due Date

You can set a due date on a recipient group.

<p align="center">
  <img src="../assets/annotated/step-06-due-date.png" width="900" alt="Group due date control highlighted">
  <br><em>Figure 6 - Group due date control.</em>
</p>

What the due date is used for:
- giving recipients a deadline
- supporting reminder logic
- making overdue processes easier to identify operationally

Best practice:
- set due dates for externally facing workflows
- avoid unrealistically short deadlines for multi-recipient processes

## Comments

Comments can be used to guide recipients and reduce confusion.

Typical uses:
- explain what the document is
- tell a signer what to check before signing
- add process-level context for all participants

There are usually two comment scopes:
- comments for all recipients
- comments targeted to one recipient or one group

Use comments for business context, not for confidential notes that should not travel with the process.

## Sign First

Enable `Sign first` when the initiator must sign before recipients can continue.

<p align="center">
  <img src="../assets/annotated/step-07-sign-first.png" width="900" alt="Sign first checkbox highlighted">
  <br><em>Figure 7 - Sign first option.</em>
</p>

How the flow changes:
- without `Sign first`, recipients receive invitations immediately based on group order
- with `Sign first`, the initiator is redirected into the signing flow first
- recipient invitations follow after the initiator action is completed

Use it when:
- the initiator is also a formal signer
- the document must be pre-signed before it is sent out

## Start Process

When all required fields are complete, click `Start signing process`.

<p align="center">
  <img src="../assets/annotated/step-08-start-process.png" width="900" alt="Start signing process button highlighted">
  <br><em>Figure 8 - Start process action.</em>
</p>

Expected result:
- the process is created
- invitations are prepared for the active workflow step
- the process becomes visible in history

If the process does not start:
- review required fields marked with `*`
- verify document type
- verify recipient email format
- check whether country, personal code, or role settings conflict with your policy

## Templates and Repeated Flows

If you create similar processes often, do not rebuild them from scratch.

Use:
- contacts for frequently used recipients
- templates for repeated process structure

This is described in more detail in [Contacts and Templates](contacts-and-templates.md).

## Advanced Controls

### `Do not notify`

Use `Do not notify` only when you intentionally want to suppress the immediate recipient notification for that signer row.

Typical use cases:
- controlled manual communication
- staged rollout during a process update

### `Load by AI`

`Load by AI` can extract possible recipients from uploaded files when the feature is enabled in your tenant.

Use it as an accelerator, not as a source of truth. Always review the extracted data before starting the process.

## Best-Practice Checklist Before Launch

Before starting the process, verify:
- the correct document was uploaded
- document type matches business purpose
- recipient roles are correct
- group order matches intended workflow
- due date is realistic
- comments are clear
- anonymous mode is used only when appropriate
- `Sign first` is enabled only when needed
