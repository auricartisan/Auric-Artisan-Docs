---
title: Device sign-in — approve the Auric command-line tool
description: Approve the Auric command-line tool from your browser with a device code, so it can act as your account.
product: Website › Account and billing
updated: 2026-09-25
---

# Device sign-in

The Auric command-line tool (`auric`, listed as `@auric-artisan/cli` on the API documentation page) signs in without asking for your password in the terminal. Instead it shows a short code, and you approve that code in a browser where you are already signed in. This is called a device sign-in.

The approval page is https://auricartisan.com/auth/device/. Its heading is **Authorize Auric CLI**.

## Before you start

- You need an Auric Artisan account, signed in in your browser.
- Your email address must be verified. Device approval is one of the features locked until you verify (see [Verify your email](verify-email.md)).
- Install the command-line tool as described on the API documentation page: [Public API](../../../services/public-api/README.md).

## Approve a device

1. In your terminal, run:

   ```bash
   auric login
   ```

2. The tool prints a short code and an approval address.
3. Open the address in your browser. If you are not signed in, the page sends you to sign in and brings you back.
4. The page shows **Signed in as** and your email or name, so you can check it is the right account.
5. If the address included the code, it is already in **Device code**. Otherwise type it; it has the form `ABCD-EFGH` (letters and numbers; the dash is added for you).
6. Select **Authorize CLI**.

Result: "CLI authorized. You can return to your terminal." The form disappears and the command-line tool continues, signed in as you. Its requests then use your account's plan and quota.

Other commands the tool documents for this:

```bash
auric whoami
auric logout
```

## Messages

| Message | What to do |
| --- | --- |
| "Enter the device code shown in your terminal." | The **Device code** field is empty. |
| An error about an invalid or expired code | Run `auric login` again to get a new code, and approve it promptly. |
| A message about email verification | Verify your email first, then try again. |

## Only approve codes you started

Approving a code lets whoever is running that terminal act as your account. Only approve a code you just generated yourself, on a computer you trust. If you approve one by mistake, sign out of the tool with `auric logout` on that computer and review **Security & Privacy** in the dashboard.

## Related

- [API keys](api-keys.md), the other way to authenticate your own code
- [Public API](../../../services/public-api/README.md)
