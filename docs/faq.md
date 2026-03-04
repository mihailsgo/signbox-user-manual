# FAQ

## Common questions

### I cannot find my process. What should I do?
Set `History` status to `Completed`, widen date range, and clear text filters.

### What is the difference between recipient and recipient group?
A recipient is one person. A recipient group is one workflow step that can contain multiple recipients.

### Why do I not see Management menu?
Management pages are role-gated (admin role required).

### Can I delete a process from UI?
Standard current flow is `Cancel` for active processes. Full delete behavior can be configuration-dependent.

## Anonymous checkbox (important)

### What does `Anonymous` mean?
`Anonymous` means recipient is created without personal code/phone in the process payload.

### How does this work internally?
- Frontend sends anonymous recipient with `signerPersonalCode = ''`.
- Process service marks signer as anonymous when personal code is null/empty.
- Matching logic:
  - Non-anonymous recipient: `personalCode + country`
  - Anonymous recipient: `signerId` fallback when personal code is empty

### When should I use it?
Use it only when your process policy allows identity flow without personal code.

### When should I avoid it?
Avoid for legally identity-bound signing where personal-code traceability is required.

> [!WARNING]
> Anonymous invitations should be treated as sensitive links. Do not forward them.

## New user simulation (Nina)
Persona: Nina, non-technical office employee, creating first process.

1. **Q**: Which portal do I use to create a process?  
   **A**: Internal portal (`signbox.<tenant>`).
2. **Q**: What is the first thing I do?  
   **A**: Upload a file on Home.
3. **Q**: Why is container name already filled?  
   **A**: It is auto-generated from filename and can be edited.
4. **Q**: Why is document type required?  
   **A**: It maps to configured process/document profile rules.
5. **Q**: What is a recipient group?  
   **A**: One workflow step; groups run step-by-step.
6. **Q**: What does `Anonymous` change?  
   **A**: Personal code is not used in primary matching path.
7. **Q**: Can anonymous recipient still sign?  
   **A**: Yes, using recipient-link/session context (signerId fallback).
8. **Q**: When should I avoid anonymous?  
   **A**: When legal/policy requires personal-code traceability.
9. **Q**: Where do I set due date?  
   **A**: Recipient group header.
10. **Q**: What is `Sign first`?  
    **A**: Initiator-first behavior (policy-dependent).
11. **Q**: How do I find old processes quickly?  
    **A**: History -> `Status = Completed`.
12. **Q**: Can I edit active process?  
    **A**: Yes, if status still allows updates.
13. **Q**: Recipient did not get email. What next?  
    **A**: Validate email, group step, notify settings, spam/quarantine.
14. **Q**: Why are some actions disabled?  
    **A**: Process is likely completed/canceled/read-only.
15. **Q**: What should I send to support?  
    **A**: Process ID, timestamp, role, exact error, screenshot.

Full simulation narrative: [new-user-simulation.md](new-user-simulation.md)  
Coverage mapping: [coverage-report.md](coverage-report.md)
