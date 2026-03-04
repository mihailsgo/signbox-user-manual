# New User Simulation

Persona:
- Name: Nina
- Background: non-technical office employee
- Goal: prepare a process up to right before `Start signing process`

## Q&A walkthrough
1. **Q**: Which portal do I use to create a process?
   **A**: Use internal portal (`signbox.<tenant>`).
2. **Q**: What is the first thing I click?
   **A**: Upload a file on Home.
3. **Q**: Why did container name change automatically?
   **A**: It is generated from file name and can be edited.
4. **Q**: Why is document type mandatory?
   **A**: It maps process to configured profile/rules.
5. **Q**: What is a recipient group?
   **A**: One workflow step; groups run sequentially.
6. **Q**: What does `Anonymous` mean?
   **A**: Recipient is created without personal code in payload.
7. **Q**: Can anonymous recipient still sign?
   **A**: Yes, via recipient-link/session context.
8. **Q**: When should I avoid anonymous?
   **A**: When legal/policy requires personal-code identity matching.
9. **Q**: Where do I set due date?
   **A**: In recipient group header.
10. **Q**: What does `Sign first` do?
    **A**: Enables initiator-first signing behavior.
11. **Q**: Where do I check old processes?
    **A**: In `History`, set status to `Completed`.
12. **Q**: Can I update active process?
    **A**: Yes, if status allows edits.
13. **Q**: What if recipient got no email?
    **A**: Check email, group step, notify settings, spam.
14. **Q**: Why is action disabled?
    **A**: Process may be completed/canceled/read-only.
15. **Q**: How do I escalate issue?
    **A**: Send process ID, timestamp, role, and screenshot.

See coverage mapping in [coverage-report.md](coverage-report.md).
