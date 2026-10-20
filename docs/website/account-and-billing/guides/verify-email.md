---
title: Verify your email address
description: Confirm the email address on your Auric Artisan account, resend the link, and understand what stays locked until you do.
product: Website › Account and billing
updated: 2026-09-25
---

# Verify your email

When you sign up with an email address and password, Auric Artisan sends a one-time link to prove the address is yours. Accounts created with Google or GitHub are already verified and skip this page.

## What stays locked until you verify

You can sign in and use the dashboard straight away — the sign-up screen calls this the "limited workspace". The sign-in page lists what stays locked until the address is verified:

- billing (buying a plan),
- promotions,
- API keys,
- device approval (signing in the command-line tool).

## Verify from the email

1. Open the verification email from Auric Artisan and select its link.
2. The page https://auricartisan.com/auth/verify-email/ opens with the heading **One click confirms it is really you.** It removes the link's code from your address bar straight away.
3. Check that you asked for this account. The panel reads **Ready to verify.** "Confirm this address only if you requested the account."
4. Select **Confirm email ownership**.

Result: the heading changes to **Email verified.** with "Ownership is confirmed and protected account features are now unlocked." and the message "Verification complete. This link cannot be used again." Select **Open workspace** to go to the dashboard. A welcome email follows.

> **Note:** The page asks you to press a button on purpose. Email security scanners and link previews open links automatically; the extra step means a preview can never verify an account on your behalf.

## Time limits

- A verification link works for 24 hours. The page shows the time left as **Maximum link window**, and says "Server time is authoritative".
- On the sign-up screen, **Verification window** counts down the same 24 hours. If it reaches zero you see "The verification window expired. Request a new email."
- Each new link replaces the previous one. Always use the newest email.

## Get a new link

There are three places to ask for a new link. Each has a short wait between requests (60 seconds by default).

| Where | Control | Confirmation |
| --- | --- | --- |
| The **Confirm your inbox.** screen after sign-up, or the sign-in page while unverified | **Resend verification email** (shows **Resend in 60s** while waiting) | "A fresh verification link has been sent." |
| The verification page, after a failed link | **Send a fresh link** (shows **Send again in** a number of seconds while waiting) | "A fresh one-time link was sent. Open the newest email to continue." |
| The dashboard's **Your account is nearly there** panel | **Send it again** | "Sent — check your inbox" |

You must be signed in to request a new link. If you are not, the verification page says "Sign in to request a fresh verification link."

## Messages on the verification page

| Heading | Meaning | What to do |
| --- | --- | --- |
| **Verification link missing.** | The address you opened has no verification code | Open the complete link from the email, or request a fresh one |
| **Verification link unavailable.** | "The link has expired, was already used, or has been replaced." | Request a fresh link and use the newest email |
| **Verification could not be completed.** | The link may have expired, been used or been replaced | Request a fresh link |
| **Verification link expired.** | The one-time window closed | Request a fresh verification email |
| **Verification status unavailable.** | The page could not check the link | Try again from the latest email |

If the service cannot be reached, the page says your link is still available and you can try again.

## Related

- [Sign up](sign-up.md)
- [Emails and messages](emails-and-messages.md)
- [Troubleshooting](troubleshooting.md#the-verification-email-did-not-arrive)
