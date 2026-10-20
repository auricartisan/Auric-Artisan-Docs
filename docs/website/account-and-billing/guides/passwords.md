---
title: Passwords — reset, change and set
description: Reset a forgotten Auric Artisan password, change your password from the dashboard, and add a password to a Google or GitHub account.
product: Website › Account and billing
updated: 2026-09-25
---

# Passwords

This page covers three tasks: resetting a password you have forgotten, changing a password you know, and adding a password to an account that was created with Google or GitHub.

## Password rules

Every Auric Artisan password must have:

- 12 to 128 characters,
- both upper-case and lower-case letters,
- at least one number,
- at least one symbol,
- no single character repeated four or more times in a row,
- not be a common password such as "password123".

Passwords are stored only as a one-way hash (the Security page names PBKDF2-SHA256 at 600,000 iterations), so nobody at Auric Artisan can read or recover your password. A reset replaces it rather than revealing it.

## Reset a forgotten password

1. Open https://auricartisan.com/auth/ and select **Forgot password?** under the password field.
2. The **Recover access.** panel opens. If you had typed an email address in the sign-in form, it is copied into **Email**.
3. Type the email address on the account (not your username) and select **Send Reset Link**.
4. The page always answers "If that address belongs to an account, a one-hour reset link is on its way." It says the same whether or not the address has an account, so nobody can use the form to find out who is registered.
5. Open the email and select the reset link within one hour.
6. The page **Set a new password** opens. Type a new password in **New Password** and again in **Confirm Password**. Select the eye button to show what you typed.
7. Select **Reset password**.

Result: "Password updated. Redirecting to sign in…" and, a moment later, the sign-in page. Sign in with the new password. Resetting a password ends every existing sign-in on every device.

Select **← Back to Sign In** on either panel to return without resetting.

### Reset page messages

| Message | Meaning |
| --- | --- |
| "This reset link is missing a token." | The address is incomplete. Open the full link from the email. |
| "Password must be at least 12 characters." | Checked before sending. The full rule list above also applies. |
| "Passwords do not match." | The two fields differ. |
| An expired or used link message | Each link works once and for one hour. Request a new one. |

## Change your password

1. Open the dashboard and select **Security & Privacy**.
2. The **Password** cell in the readout strip says when the password was last set, for example "Set when you signed up", "Unchanged since you signed up", "Changed today", "Changed yesterday" or "Changed 42 days ago".
3. Select **Change** in that cell. A small form opens below the strip.
4. Type your **Current password**, a **New password (12+ chars, mixed)**, and **Repeat new password**.
5. Select **Update password**. Select **Cancel** to close the form without changing anything.

Result: "Password changed." Changing the password signs you out everywhere, including this browser, so the dashboard returns you to the sign-in page. Sign in with the new password.

| Message | What to do |
| --- | --- |
| "New passwords do not match." | Retype the new password in both fields. |
| "Current password is incorrect." | Check the current password, or reset it instead. |
| "Password changed in another session. Sign in again." | The password was changed somewhere else a moment ago. Sign in with the newest password. |

## Add a password to a Google or GitHub account

An account created with Google or GitHub has no Auric Artisan password. You need one to unlock the dashboard's danger zone (for example, to delete the account); without one the danger zone says "Set an account password before using these actions."

1. Sign out, or use a private window.
2. Follow [Reset a forgotten password](#reset-a-forgotten-password) with the email address of your Google or GitHub account.
3. Set a password from the emailed link.

Result: you can sign in with either the provider or the email address and password.

## Related

- [Sign in and sign out](sign-in.md)
- [Two-step verification](two-step-verification.md)
- [Security & Privacy section](security-and-privacy.md)
- [Troubleshooting](troubleshooting.md#the-reset-email-did-not-arrive)
