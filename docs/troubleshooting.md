# Troubleshooting

Use this page when a process does not start, a recipient cannot act, or history does not show the expected result.

## Session and Data Issues

### Data disappeared during process creation

Possible reason:
- the session expired while the form was open for too long

What to do:
- sign in again
- reopen `Home`
- rebuild the process
- if available, save as draft earlier for long or complex workflows

## Email Not Received

Check:
- recipient email address
- spam, junk, or quarantine folder
- whether the recipient group is currently active
- whether notifications were intentionally suppressed

## Login Problems

Check:
- correct portal URL
- active user account
- browser session state
- correct invitation link for recipient-side access

If needed:
- retry in a clean browser session
- confirm method and country configuration with your administrator

## Smart-ID, eID, or Other Signing Method Problems

Check:
- recipient country
- enabled method for that country
- provider readiness or device readiness
- personal data format in non-anonymous flows

If the issue is method-specific, treat it as a signing-readiness problem first, not only as a SignBox UI issue.

## Process Actions Are Disabled

Typical reasons:
- process is already completed
- process is canceled
- the current user is not in the active workflow step
- the view is read-only due to status progression

## I Cannot Find the Process in History

Try this order:
- widen date range
- broaden status filter
- search by container or document name
- verify initiator identity

## Recipient Cannot Open or Sign the Document

Possible reasons:
- wrong invitation link
- non-anonymous identity mismatch
- process is no longer active
- another recipient group must finish first

## What to Send to Support

Send:
- process ID
- timestamp and timezone
- your role in the process
- exact action that failed
- exact error text
- screenshot with sensitive data redacted

> [!WARNING]
> If the issue persists, send structured support data instead of a general description. That shortens diagnosis time significantly.
