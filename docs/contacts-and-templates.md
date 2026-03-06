# Contacts and Templates

Use contacts and templates to reduce repeated manual work when the same people or the same signing structure are used often.

## Why These Features Matter

Contacts help you reuse recipient details safely. Templates help you reuse process structure.

Use contacts when:
- the same signer is added often
- you want less typing and fewer input mistakes
- you want default role and scope behavior ready in advance

Use templates when:
- the same workflow repeats regularly
- the same recipient structure is used across many documents
- you want to standardize process setup

## Contacts

### Add a saved contact to a process

In the process form, click `Select contact`.

<p align="center">
  <img src="../assets/annotated/step-15-select-contact-open.png" width="900" alt="Select contact modal highlighted">
  <br><em>Figure 1 - Open the contact selector from the recipient area.</em>
</p>

What you can do in the selector:
- search by name
- search by email
- choose an existing row and insert it into the current recipient group

Expected result:
- the selected contact is added to the recipient group and can still be adjusted before launch

### Create a new contact

Contacts can usually also be created from the dedicated contacts page.

Typical contact fields:
- name
- email
- country
- role
- scope
- personal code, if used in non-anonymous flows

Why these fields matter:
- `Country` supports the correct identity/signing context
- `Role` pre-fills the intended participant role
- `Scope` controls who can reuse the contact

### Edit and delete contacts

Existing contacts can typically be:
- edited when recipient details change
- deleted when no longer needed

Before deleting a contact:
- confirm it is not a frequently reused entry for other users
- confirm the correct item is selected, especially in group-shared lists

## Scope Rules for Contacts

### Scope meaning

- `Personal`: visible only to the creator
- `Group`: visible to users in the same group
- `Global`: visible tenant-wide, depending on permissions
- `All`: filter value only, not a stored ownership scope

### Practical scope guidance

Use:
- `Personal` for your own private shortcuts
- `Group` for department or team reuse
- `Global` only when the contact is intended for broad organizational reuse

## Templates

Templates save a process setup for reuse.

Typical template content:
- selected document type
- recipient and group structure
- roles
- comments
- due date logic, depending on the implementation

### Open template selector

Click `Select template` in the process form.

<p align="center">
  <img src="../assets/annotated/step-16-template-open.png" width="900" alt="Template modal highlighted">
  <br><em>Figure 2 - Open the template selector from the create-process page.</em>
</p>

Expected result:
- the template modal opens
- you can search or select an existing template

### Load a template

Choose the template and apply it to the process.

What happens next:
- the process form is prefilled
- you can still review and adjust recipients, comments, or other fields before launch

Best practice:
- always confirm recipient list and due date before starting a templated process

### Save a template

After preparing a process structure, click `Save template`.

Expected result:
- the current setup is stored for future reuse

What to define when saving:
- template name
- template scope

Use naming that helps people understand when to use the template, for example:
- `HR contract - one signer`
- `Board approval - sequential`
- `Vendor agreement - two-stage`

## Contacts vs Templates

| Feature | Best used for | Example |
|---|---|---|
| Contact | one reusable person or participant entry | CFO signer, HR manager, legal approver |
| Template | one reusable workflow setup | one-signer contract, two-stage approval, board signing flow |

## Common Mistakes

### Using a template without reviewing the loaded data

Templates accelerate setup, but they should not replace review. Always confirm:
- recipient names
- group order
- role assignments
- comments
- due date

### Saving too many nearly identical templates

If too many templates exist, users stop trusting the list. Prefer:
- fewer templates
- clear names
- stable scope policy

### Wrong scope choice

If a useful contact or template cannot be found, the problem is often scope, not deletion.

Check:
- whether it was saved as `Personal` instead of `Group`
- whether the current user belongs to the right group
- whether tenant configuration restricts visible scopes

## Recommended Working Model

For most organizations:
- maintain shared contacts for recurring signers
- maintain a small, curated set of templates for the most common workflows
- avoid turning templates into copies of every one-off scenario

This keeps the manual process simple and makes SignBox easier to operate consistently.
