# FAQ

## I cannot find my process. What should I do?

Open `History` and start with the broadest reasonable filters.

<p align="center">
  <img src="../assets/annotated/faq-history-find-process.png" width="900" alt="History filters highlighted">
  <br><em>Figure 1 - Use history filters to locate a process.</em>
</p>

Recommended order:
- widen date range
- set status to a broader value
- search by container or document name
- verify initiator identity

## Why is `Document type` important?

`Document type` is usually tied to process rules and archive behavior. If the wrong type is selected, the process may be routed incorrectly or fail business validation.

## What does `Anonymous` mean?

`Anonymous` means recipient matching does not rely on personal code.

<p align="center">
  <img src="../assets/annotated/faq-anonymous-checkbox.png" width="900" alt="Anonymous checkbox highlighted">
  <br><em>Figure 2 - Anonymous checkbox in the recipient row.</em>
</p>

What it does not mean:
- it does not make the process public
- it does not allow open access without the invitation link

What it changes:
- personal-code-based recipient matching is skipped
- access still depends on the correct invitation link and valid process state

## Why did my entered data disappear during process creation?

The old manual highlighted this correctly: long idle time during creation can cause the page or session to expire, depending on tenant security policy.

What to do:
- restart the process setup
- avoid leaving the form idle for too long
- save as draft if the workflow is complex and your tenant supports it

## A recipient says they did not receive any email. What should I check?

Check the following first:
- correct email address
- spam or junk folder
- whether the recipient group is already active
- whether `Do not notify` was used intentionally
- whether the process was updated after launch and notifications were suppressed

## I cannot log in to SignBox. What should I do?

Verify:
- correct portal URL
- your account is active
- your country and configured authentication/signing methods are supported
- you are using the correct invitation link if entering as a recipient

## Smart-ID does not allow signing. Why?

One common cause is that the Smart-ID account is not qualified for signing. Another is that the configured country or signing method does not match the intended recipient configuration.

Check:
- Smart-ID qualification level
- recipient country
- provider availability

## eID card does not work. Why?

This is usually an environment readiness issue rather than a SignBox content issue.

Check:
- browser compatibility
- local middleware/readiness for your national eID
- whether the eID works in other browser-based signing flows

## What is the difference between `Cancel` and `Delete`?

Typical meaning:
- `Cancel`: stop an active process
- `Delete`: remove a finished process record or related UI/archival reference, depending on configuration

`Delete` is usually more restricted and should be used more carefully.

## Why do I not see management or admin controls?

Management functions are role-based.

<p align="center">
  <img src="../assets/annotated/faq-management-menu.png" width="900" alt="Top menu highlighted">
  <br><em>Figure 3 - Top navigation area where role-based menu items can appear.</em>
</p>

If you do not see a menu entry:
- your assigned role may not include that permission
- the function may not be enabled for your tenant

## Will end users pay for signing in SignBox?

The old manual stated that end-user usage is free of charge. In practice, commercial and service ownership terms depend on the organization operating the SignBox environment, not on the recipient using the invitation flow.

## How are documents and data managed?

Documents processed through SignBox are controlled by the organization operating the environment. Retention, archive destination, and access policy are organization-specific.

If you need:
- storage location
- retention duration
- archive deletion policy

ask your administrator or service owner.

## Who can access a shared document?

Normally only:
- the intended recipients in the process
- authorized internal users who manage the process

Access is limited by role, process state, and invitation/security model.

## What support information should I send when reporting an issue?

Send:
- process ID, if visible
- exact timestamp and timezone
- your role in the process
- exact action that failed
- error text, if shown
- screenshot with sensitive data redacted
