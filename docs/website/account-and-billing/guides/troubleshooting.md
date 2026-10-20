---
title: Account and billing — troubleshooting
description: Fixes for problems with signing in, verification emails, passwords, two-step codes, payments, invoices, API keys and the Auric Artisan dashboard.
product: Website › Account and billing
updated: 2026-09-25
---

# Troubleshooting

Each entry gives the symptom, the likely cause and what to do. For problems with the website in general — browser support, cookies, offline use — see [Help: troubleshooting](../../../help/troubleshooting.md).

## I cannot sign in

| Symptom | Why | What to do |
| --- | --- | --- |
| "Enter a valid email address." although you typed a username | The field contains an **@**, so it is checked as an email address | Type the username without **@**, or your full email address |
| The sign-in is refused with a credentials message | Wrong email, username or password | Check for typing errors, then use **Forgot password?** |
| Refused after several attempts | Sign-in attempts are rate-limited; repeated failures can lock sign-in for a while | Wait, then try again, or reset your password |
| "Complete the Auric human check before continuing." | A human check is on screen and not finished | Repeat the three marks and select **Verify sequence**, then **Sign In** |
| The human check keeps expiring | Each check lasts a few minutes and is used once | Select **New sequence**, answer, and sign in straight away |
| "Enter your email or username before verifying the sequence." | The check is tied to the identifier in the form | Fill in **Email or username** first |
| You signed up with Google or GitHub and have no password | Provider accounts have no Auric Artisan password | Use the same provider button, or set a password with **Forgot password?** |
| "That sign-in request expired. Start again." | The 10-minute second-factor window ran out | Sign in again and enter the code promptly |
| You are signed in but keep being sent to the sign-in page | Your session ended (password change, revoked device, or it expired) | Sign in again |

## Google or GitHub sign-in errors

After returning from the provider, one of these may appear at the top of the sign-in page:

| Message | What to do |
| --- | --- |
| "OAuth response was incomplete." | Try again from the Auric Artisan sign-in page. |
| "OAuth session expired. Try signing in again." | You took too long, or opened the provider page in another tab. Start again. |
| "Could not complete sign-in with that provider." | Try again; if it persists, use email and password. |
| "Your provider account has no verified email address." | Verify your email with Google or GitHub, or sign up with email and password. |
| "This email already has an account. Sign in with the method already connected to it." | Sign in with email and password (or the other provider) you used first. |
| "Could not link that account. Try signing in again." | Try again. |
| "Signed in, but the session could not be started." | Check that your browser allows cookies for auricartisan.com, then try again. |
| "OAuth sign-in failed." | Try again, or use email and password. |

## The verification email did not arrive

1. Wait a minute and check your spam or junk folder.
2. Check the address shown (partly masked) on the **Confirm your inbox.** screen.
3. Select **Resend verification email** once the wait timer ends. Each new link replaces the old one; use the newest.
4. From the dashboard, use **Send it again** in the **Your account is nearly there** panel.
5. If the address is wrong, it cannot be changed from the dashboard; contact support.

If the link says **Verification link unavailable.**, it has expired (after 24 hours), been used, or been replaced. Request a fresh one.

## The reset email did not arrive

- The reset form never says whether an address has an account. If nothing arrives, check that you typed the email address on the account (not your username) and look in spam.
- Reset requests are rate-limited; wait a few minutes before asking again.
- Links last one hour and work once. Request a new one if yours has expired.
- Accounts created with Google or GitHub receive a reset link too; that is how you add a password.

## My authenticator code is refused

| Symptom | What to do |
| --- | --- |
| "Code is invalid. Try again." during setup | Enter the code currently on screen. Make sure your phone's date and time are set automatically. |
| "2FA setup expired — start again." | Select **Enable 2FA** again and scan the new QR code. |
| Codes are refused at sign-in | Check the device clock, and that you are using the Auric Artisan entry in your app. Use a backup code if needed. |
| No app and no backup codes | Contact support through the contact page (topic **Security**) from the account's email address. |

## The dashboard

| Symptom | Why | What to do |
| --- | --- | --- |
| "Could not load subscription details." | The plan could not be read | Refresh. If it persists, sign out and in again. |
| Panels stay empty or show "—" | Figures appear only when there is something true to show | This is expected for a new account; see [Overview section](dashboard-overview.md) |
| Usage meters differ between browsers | Meters include counts recorded in each browser | Expected; they converge as the account's own figures update |
| **Your work** shows nothing although you saved work | The library lives in the browser where you saved it | Open the dashboard in that browser |
| The **Change plan** cards show rupees | These cards show prices in rupees | Use the pricing page to see US dollars |
| "Changed here, but not saved to your account" on **Usage data** | The choice could not be saved | Try the switch again later |
| "This list does not say which device you are reading on…" | The device list could not mark your device | Be careful: every row, including yours, can be revoked |
| **Sign out everywhere** did nothing | It needs a second press within about six seconds | Press **Sign out every other device?** to confirm |

## The danger zone will not unlock

| Message | What to do |
| --- | --- |
| "Not yet — it has to match word for word." | Retype the sentence exactly as displayed. |
| "That password is not right." | Retype your password. |
| "Set an account password before using these actions." | Add a password first: [Passwords](passwords.md#add-a-password-to-a-google-or-github-account). |
| "This page has lost its session token, so it cannot send this safely. Reload the page and try again — your password is fine." | Reload. This happens if you signed out in another tab, or opened the site over an insecure address. |
| "This page could not prove it is still your session…" | Reload the page. |
| "The danger zone is not available on this server yet. Nothing is wrong with what you typed." | The zone shows **Unavailable**. Contact support to delete the account. |
| "Too many attempts. Try again in a few minutes." | Wait before trying again. |

## Payments and checkout

| Symptom | Why | What to do |
| --- | --- | --- |
| Selecting **Get Artisan** shows "Sign in first…" | An account is required before payment | Select **Sign in or create a free account**; you return to the pricing page |
| The payment is refused because the email is unverified | Billing is locked until you verify | Verify your email, then try again |
| A foreign card is declined at the last step | Non-Indian cards and American Express depend on permissions on Auric Artisan's payment account | Nothing is charged. Try UPI or another card, or tell Auric Artisan through the contact page so they can arrange it |
| "Checkout is briefly unavailable, so nothing was charged." | The checkout could not start | Try again in a moment, or contact support |
| "Checkout cancelled." | The checkout window was closed | Nothing was charged; start again if you meant to pay |
| The confirmation page stays on **Confirming your payment** | Razorpay's confirmation is delayed | Wait; do not pay again. Check **Billing history**; contact support with the order reference if it does not update |
| **Payment not completed** but money left your account | A bank hold or a delayed confirmation | Holds are released automatically. If the money does not return, contact support with the order reference |
| The plan does not show after paying | The page loaded before the update | Refresh the dashboard. Quote the order reference if it still does not show |
| You were charged twice | — | Contact support with both order references |
| **Current Plan** on the pricing page does not match | You are signed in to another account | Check the email in the header account menu |

## Invoices

| Symptom | What to do |
| --- | --- |
| **Invoice not found** | Sign in to the account that made the payment and open the invoice from **Invoices & Payment History**. |
| You need a GST tax invoice | Auric Artisan is not currently registered for GST; receipts are payment receipts. See [Invoices and receipts](invoices-and-receipts.md#receipts-and-gst). |

## API keys and credits

| Symptom | Why | What to do |
| --- | --- | --- |
| No create button in **Your API Keys** | Your plan does not include the API | API access starts at Specialist |
| "You can hold at most 10 active keys." | The account limit | Revoke a key you do not need |
| You lost a key | Keys are shown once | Create a new key and revoke the old one |
| Calls return 402 with `PLAN_UPGRADE_REQUIRED` | The account's plan does not include the API | Move to a plan with API access |
| Calls return 429 | The monthly allowance is used up, the rate limit was hit, or overage cannot continue (no prepaid balance, spend cap or ceiling reached) | Wait for the reset, slow down, add credits, or raise your cap |
| **Usage & cost** says "That key was refused." | The pasted key was revoked or mistyped | Paste another key |
| The pack picker has nothing to buy | Credits belong to plans with API access | See [API credits and spend controls](api-credits-and-spend.md) |
| "Enter a cap between $0 and $10,000." | The cap is out of range | Enter a value in range, or 0 for no cap of your own |

## Related

- [FAQ](faq.md)
- [Contact and support](../../../help/contact-and-support.md)
