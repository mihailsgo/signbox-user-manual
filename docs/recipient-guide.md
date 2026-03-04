# Recipient Guide ✍️

This section is for recipients who receive a SignBox invitation link.

## External portal flow (end-to-end)

## Step 1 - Open your invitation link
- **Action**: Open the signing link from your email.
- **Expected result**: External SignBox portal opens and asks for authentication.
- **If not**: Ask initiator to resend the invitation.
- **Screenshot**: No screenshot needed, because email client UI is outside SignBox.

## Step 2 - Choose country and signing method
- **Action**: Select your country tab and one available method (`Smart-ID`, `ID card`, `SMS`, etc.).
- **Expected result**: Authentication request is started.
- **If not**: Check if your country/method is enabled for this recipient.
- **Screenshot**:

<p align="center">
  <img src="../assets/annotated/step-13-recipient-country-method.png" width="900" alt="External portal country and method selector">
  <br><em>Figure 1 — Authentication method selection in external portal.</em>
</p>

## Step 3 - Approve identity in provider app/device
- **Action**: Confirm the request in your identity provider app/device.
- **Expected result**: You are logged into the external portal.
- **If not**: Retry once, then verify phone/device network and provider status.
- **Screenshot**: No screenshot needed, because provider confirmation screens are outside SignBox.

## Step 4 - Open `My documents` list
- **Action**: Go to `My documents` in top navigation.
- **Expected result**: You see your assigned signing processes with filters and statuses.
- **If not**: Confirm you used the same invitation link from the assignment email.
- **Screenshot**:

<p align="center">
  <img src="../assets/external-portal-my-documents-blur.png" width="900" alt="External portal document list with blurred document names">
  <br><em>Figure 2 — `My documents` list view. Document names are intentionally blurred for privacy.</em>
</p>

## Step 5 - Filter and find your task
- **Action**: Use container search, status filter, and date range.
- **Expected result**: Required task row is visible.
- **If not**: Set status to `All` and widen date range.
- **Screenshot**:

<p align="center">
  <img src="../assets/external-portal-my-documents-blur.png" width="900" alt="External portal document list filters">
  <br><em>Figure 3 — Find your process using search and filters.</em>
</p>

## Step 6 - Open process details
- **Action**: Click the process row (document/container name).
- **Expected result**: Document detail view opens with signing controls.
- **If not**: Refresh page and open the row again.
- **Screenshot**:

<p align="center">
  <img src="../assets/external-portal-document-view.png" width="900" alt="External portal document detail view with Sign and Decline">
  <br><em>Figure 4 — Document detail view with `Sign` and `Decline` actions.</em>
</p>

## Step 7 - Review file before signing
- **Action**: Use view/download icons in `Content` area to inspect the file.
- **Expected result**: Document opens or downloads.
- **If not**: Retry download and check browser popup/download settings.
- **Screenshot**:

<p align="center">
  <img src="../assets/external-portal-document-view.png" width="900" alt="External portal content area and file actions">
  <br><em>Figure 5 — Content area with file preview/download controls.</em>
</p>

## Step 8 - Sign or decline
- **Action**: Click `Sign` to complete, or `Decline` to reject.
- **Expected result**: Status updates after confirmation.
- **If not**: Recheck authentication and due-date/status constraints.
- **Screenshot**:

<p align="center">
  <img src="../assets/external-portal-document-view.png" width="900" alt="External portal Sign and Decline buttons">
  <br><em>Figure 6 — Final recipient action buttons.</em>
</p>

## Important note about anonymous recipients
`Anonymous` does not make a process public. Only users with the correct invitation link can access and sign their assigned task.

> [!WARNING]
> Do not forward or share invitation links.
