---
title: Dashboard — Security & Privacy section
description: Check your password and two-step status, manage signed-in devices, review sign-ins, export your data and reach the danger zone in the Auric Artisan dashboard.
product: Website › Account and billing
updated: 2026-09-25
---

# Security & Privacy section

The **Security & Privacy** section (https://auricartisan.com/auth/dashboard/#security) answers two questions: who can get into the account, and what leaves it. Its heading counts what is signed in right now, for example "2 devices are holding this account open." The line beneath reads: "End anything you do not recognise — a device you revoke here is signed out immediately."

The older addresses `#settings` and `#sessions` open this section too.

## The readout strip

Four cells state the account's condition. The cell that needs attention is highlighted.

| Cell | What it says | Control |
| --- | --- | --- |
| **Password** | When the password was last set: "Set when you signed up", "Unchanged since you signed up", "Changed today", "Changed yesterday" or "Changed N days ago" | **Change** — see [Passwords](passwords.md#change-your-password) |
| **Two-factor** | "Off — nothing but your password" (highlighted), or "On — N backup codes left" | **Enable 2FA** or **Disable 2FA** — see [Two-step verification](two-step-verification.md) |
| **Usage data** | "On — anonymous usage only" or "Off — nothing is collected" | A switch that records your choice on your account |
| **Cookies** | Your cookie choice: "Not answered yet", "Necessary only", or "Necessary +" the optional categories you accepted | **Change** opens the Cookie Policy page, where you change it |

### The Usage data switch

Select the switch to turn it on or off. The choice is saved to your account at once. If it cannot be saved, the cell says "Changed here, but not saved to your account"; try again later.

This switch is separate from your cookie choice. On the website, analytics events are only sent when you have accepted the **Analytics** cookie category, and never when your browser sends Do Not Track or Global Privacy Control (see [Privacy overview](../../../help/privacy.md)).

## Signed-in devices

A sheet lists every browser or device where the account is signed in, with **Sign out everywhere** at the top.

| Column | Shows |
| --- | --- |
| **Device** | An icon (phone or computer), the browser and system — for example "Safari on iPhone" — and "Signed in 3 d ago" or **This device** |
| **Where** | The network address the sign-in came from |
| **Last active** | How long ago it was last used, for example "12 min ago" |
| (action) | **Revoke**, or the **This device** label on your own row |

Your own device is always the first row and has no **Revoke** button, so you cannot sign yourself out by accident here. If the list cannot tell which row is yours, it says "This list does not say which device you are reading on, so every row can be revoked — including this one."

### End one session

1. Find the row you do not recognise.
2. Select **Revoke**.

Result: that device is signed out immediately and the row disappears.

### Sign out everywhere else

1. Select **Sign out everywhere**. The button changes to **Sign out every other device?**
2. Select it again within about six seconds to confirm. If you wait, it resets.

Result: "Signing out…", then every other device is signed out. The device you are using stays signed in. To sign out this device too, use **Sign out** in the header account menu.

### Sign-in history

Under the sheet, a line summarises the last 30 days, for example "14 sign-ins in the last 30 days, none failed" or "…, and 2 failed attempts". Failed attempts are highlighted because they are worth a second look. If nothing is recorded: "No sign-ins recorded in the last 30 days".

Select **See all sign-ins** to open a list of recent successful sign-ins (up to six), each with the browser, system, network address and time. Select **Hide sign-ins** to close it.

If you see failed attempts you did not make, change your password and turn on two-step verification.

## Export everything

A single row: **Export everything** — "Your profile, portfolio, collections and receipts as one JSON file. Nothing secret is included — passwords, two-factor material and API keys stay out." Select **Export**. What the file contains is described in [Export your data](export-your-data.md).

## Danger zone

The last panel is the **Danger zone**, which holds the two actions that cannot be undone: **Erase this browser's workspace** and **Delete this account**. It starts **Locked**. To open it you type a confirmation sentence and your password, and it then stays open for five minutes. A list headed **Behind this door** names what it contains before you unlock it.

Everything reversible lives elsewhere: devices on the sheet above, keys under Plan & Usage, your public page in the Portfolio Builder.

Full walkthrough: [Delete your account](delete-your-account.md).

## Related

- [Sign in and sign out](sign-in.md)
- [Two-step verification](two-step-verification.md)
- [Export your data](export-your-data.md)
- [Reference](reference.md#security-and-privacy-section)
