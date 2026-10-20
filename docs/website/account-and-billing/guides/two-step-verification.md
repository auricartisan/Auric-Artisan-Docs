---
title: Two-step verification
description: Protect your Auric Artisan account with authenticator-app codes and single-use backup codes, sign in with them, and turn them off.
product: Website › Account and billing
updated: 2026-09-25
---

# Two-step verification

Two-step verification (the dashboard calls it **Two-factor** or **2FA**) adds a second check after your password: a six-digit code from an authenticator app on your phone or computer. The codes use the standard TOTP method (time-based one-time passwords, which change every 30 seconds), so any common authenticator app works. Two-step verification is free on every plan.

## Turn it on

1. Install an authenticator app if you do not have one.
2. Open the dashboard and select **Security & Privacy**.
3. The **Two-factor** cell in the readout strip reads "Off — nothing but your password" and is highlighted while it is off. Select **Enable 2FA**.
4. The form below the strip says "Setting up… fetching your secret." and then "Scan this with your authenticator app, then enter the 6-digit code it shows."
5. Scan the QR code with the app. If you cannot scan, use the text under "Can't scan? Enter this secret manually:", or select **Open in authenticator** on a device that has the app.
6. Type the 6-digit code the app shows into the box (placeholder `123456`).
7. Select **Verify & enable**.

Result: "Two-factor authentication is ON. Store these one-time backup codes somewhere safe:" followed by ten backup codes.

8. Select **Download backup codes** to save them as a text file named `auric-artisan-backup-codes.txt`, or copy them somewhere safe and offline.

The **Two-factor** cell now reads "On — 10 backup codes left", and the button changes to **Disable 2FA**.

> **Important:** The backup codes are shown once. There is no screen to view them again. Keep them where you can reach them if you lose your phone.

## Sign in with two-step verification

1. Sign in with your email or username and password as usual.
2. The **Second factor.** panel appears with a 10-minute countdown.
3. Type the current code from your authenticator app in **Verification Code** and select **Verify**.

If you do not have the app with you, select **Use a backup code**, type one backup code (format `XXXX-XXXX-XXXX-XXXX`) and select **Verify**. Each backup code works once; it is used up only after it is accepted. The **Two-factor** cell shows how many are left.

Full sign-in details: [Sign in and sign out](sign-in.md#sign-in-with-a-second-factor).

## Turn it off

1. Open **Security & Privacy** and select **Disable 2FA**.
2. The form says "Confirm your password and a current authenticator code to turn 2FA off."
3. Type your **Account password** and a current code from your authenticator app.
4. Select **Disable 2FA**.

Result: "Two-factor authentication disabled." The cell returns to "Off — nothing but your password".

## Get new backup codes

The dashboard has no separate control for new backup codes. If you are running low, turn two-step verification off and on again: completing setup replaces any old backup codes with a new set of ten, and you scan a new QR code into your app.

## Setup messages

| Message | What to do |
| --- | --- |
| "Code is invalid. Try again." | Type the code currently shown in the app. Check that your device's clock is set automatically. |
| "2FA setup expired — start again." | The setup took too long. Select **Enable 2FA** again and scan the new code. |
| "Code is invalid." (when turning off) | Use a current code from the app. |
| "Password is incorrect." (when turning off) | Retype your account password. |

## How it is protected

The Security page (https://auricartisan.com/security/) states that two-factor secrets are encrypted before they are stored, under a key held separately, so a copy of the database alone cannot generate anyone's codes. The QR code is drawn by Auric Artisan itself, so the secret is never sent to an outside image service.

## Reminders on the dashboard

While two-step verification is off, the Overview shows it as **Not set up** with a **Set it up** button, and its **Next** list leads with **Turn on two-factor**. You can dismiss that suggestion with its × button.

## If you lose your authenticator

- Use a backup code to sign in, then turn two-step verification off and on again with your new device.
- If you have neither the app nor a backup code, contact support through https://auricartisan.com/company/contact/ (topic **Security**) from the email address on the account. See [Contact and support](../../../help/contact-and-support.md).

## Related

- [Security & Privacy section](security-and-privacy.md)
- [Passwords](passwords.md)
- [Troubleshooting](troubleshooting.md#my-authenticator-code-is-refused)
