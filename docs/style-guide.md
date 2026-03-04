# Screenshot Style Guide 🖼️

Use this guide for all SignBox documentation screenshots.

## Rendering standard

Use this exact centered pattern for every user-facing image:

```html
<p align="center">
  <img src="<path-to-annotated-image>" width="900" alt="Short alt text">
  <br><em>Figure X — Clear caption describing the exact action.</em>
</p>
```

Rules:
- Keep width at `900` for consistency.
- Add a caption for every figure.
- Match caption wording to the step text.

## Annotation standard

Every annotated screenshot must include:
- Tight highlight around the exact control (not full page sections).
- One arrow pointing to the highlighted control.
- Step badge number near the control.
- Short label such as `Step 3: Open Document type`.

## Dropdown rule

If the step references a dropdown, the screenshot must show the dropdown open with visible options.

Examples in this repo:
- `Document type` open.
- `Status` filter open.
- `Country` dropdown open.

## Sanitization and privacy

Before annotation, sanitize screenshots with:

```bash
python scripts/sanitize_screenshots.py specs/redactions.yml
```

Redact:
- Real document names.
- Personal emails/identifiers.
- Any personal data visible in tables, metadata, or recipient rows.

Approved replacement names:
- `Sample-Contract-01.pdf`
- `NDA_Test.pdf`
- `Invoice_Test_2026-01.pdf`
- `initiator@example.com`
- `signer@example.com`

## Git history warning

If sensitive screenshots were committed to a public repository, replacing files in a new commit may not fully remove exposure.

Recommended remediation:
1. Rewrite repository history to purge sensitive files.
2. Force-push cleaned history.
3. Rotate any exposed credentials/links.
4. Invalidate old screenshot URLs where possible.
