---
title: Account and billing — reference
description: Every screen, control, field, rule and status in the Auric Artisan account area, from the sign-in page to the dashboard, pricing, checkout and invoices.
product: Website › Account and billing
updated: 2026-09-25
---

# Reference

This page lists every control in the account area, screen by screen. Labels are as they appear on screen. For step-by-step instructions, follow the links to the task guides.

## Sign-in page

Address: https://auricartisan.com/auth/ (add `#register` to open **Create Account**, `#forgot` to open password recovery).

### Tabs

| Control | What it does |
| --- | --- |
| **Sign In** tab | Shows the sign-in form ("Welcome back.") |
| **Create Account** tab | Shows the sign-up form ("Create your identity.") |
| **Exit** | Returns to the home page |
| Arrow keys, `Home`, `End` | Move between the two tabs |

### Sign In form

| Control | What it does | Values or rules |
| --- | --- | --- |
| **Email or username** | Who you are | An email address (checked as an address if it contains **@**) or a username of 3–30 letters, numbers and underscores |
| **Password** | Your password | Required |
| Eye button ("Show password") | Shows or hides the password | Toggle |
| **Remember me** | Keeps you signed in on this browser | Up to 30 days; ends after seven days unused. Off: ends when the browser closes, 24 hours at most. |
| **Forgot password?** | Opens **Recover access.** | Copies an email address you typed |
| **Sign In** | Submits; shows the human check on first use | — |
| **Google**, **GitHub** | Sign in with that provider | — |

### Create Account form

| Control | Rules |
| --- | --- |
| **Display Name** | Required, 2–64 characters |
| **Username** | Required, 3–30 characters, letters, numbers and underscores; live availability tick or cross |
| **Email** | Required, valid address |
| **Password** | 12–128 characters; upper and lower case; a number; a symbol; no character four times in a row; not a common password. Strength label **Weak**, **Fair**, **Good** or **Strong**. |
| **Confirm Password** | Must match |
| **I agree to the Terms of Service and Privacy Policy** | Required |
| **Create Account** | Submits; shows the human check on first use |
| **Google**, **GitHub** | Sign up with that provider |

### Auric human check

| Control | What it does |
| --- | --- |
| Sequence and countdown | Three marks to repeat, and the time left |
| Choice buttons | Add a mark to the next answer slot |
| Answer slots | Select one to remove that mark |
| **Verify sequence** | Checks your answer (enabled when three are chosen) |
| **New sequence** | Loads a fresh sequence |

### Recover access

| Control | What it does |
| --- | --- |
| **Email** | The account's email address |
| **Send Reset Link** | Sends a one-hour link if the address has an account; the reply is the same either way |
| **← Back to Sign In** | Returns to the sign-in form |

### Second factor and backup code

| Control | What it does |
| --- | --- |
| **Verification Code** | Six digits from your authenticator app; the sign-in expires in 10 minutes |
| **Verify** | Checks the code |
| **Use a backup code** | Switches to **Backup Code** (`XXXX-XXXX-XXXX-XXXX`, single use) |
| **← Back to code entry** | Returns to the six-digit code |
| **Cancel sign-in** | Abandons this sign-in |

### Confirm your inbox

| Control | What it does |
| --- | --- |
| **Verification window** | Counts down 24 hours |
| **Resend verification email** | Sends a fresh link; shows **Resend in** seconds while waiting |
| **Continue to limited workspace** | Opens the dashboard before verifying (reads **Return to sign in** if the address already had an account) |

Full guides: [Sign up](sign-up.md), [Sign in and sign out](sign-in.md), [Passwords](passwords.md).

## Other account pages

| Page | Address | Controls |
| --- | --- | --- |
| Verify email | https://auricartisan.com/auth/verify-email/ | **Confirm email ownership**; afterwards **Open workspace**, **Return to sign in**, **Send a fresh link** |
| Reset password | https://auricartisan.com/auth/reset-password/ | **New Password**, **Confirm Password**, show-password button, **Reset password**, **← Back to Sign In** |
| Authorize Auric CLI | https://auricartisan.com/auth/device/ | **Device code** (`ABCD-EFGH`), **Authorize CLI** |
| Invoice | https://auricartisan.com/auth/billing/invoice/ | **← Back to billing**, **Print / Save as PDF**, **Copy invoice URL** |
| Payment confirmation | https://auricartisan.com/checkout/success/ | Copy buttons for **Payment** and **Order**; **Open your dashboard**, **Start using the tools**, **View invoice →**, **Billing history →**, **Try this payment again** |

## Header account menu

| Item | Description shown | Goes to |
| --- | --- | --- |
| **Sign in** / **Create account** | — | The sign-in page (shown when signed out) |
| Account chip | Your photo, first name and plan | Opens the menu |
| **Dashboard** | "Overview and recent activity" | Dashboard |
| **Profile** | "Identity and profile photo" | Profile section |
| **Billing & plan** | "Subscription and invoices" | Plan & Usage section |
| **API keys** | "Manage developer access" | Plan & Usage section |
| **Sign out** | "End this session securely" | Ends this session |

## Dashboard masthead

| Element | Values |
| --- | --- |
| Handle | **@yourhandle**, or **@unclaimed** with **Claim your handle** |
| Photo | Double-click to open the photo viewer |
| **Plan** | Apprentice, Artisan, Specialist or Industrial Pro, plus a status when not active: Trial, Past due, Paused, Cancelled, Expired, Incomplete |
| Email | The sign-in address |
| Join date | "Joined today" or "Member since" month and year |
| **Open Studio** | Opens your saved work |
| **Upgrade** / **Manage** | Pricing page, or Plan & Usage on a paid plan; hidden on Industrial Pro |

## Section rail

| Tab | Address | Badge |
| --- | --- | --- |
| **Overview** | `#overview` | — |
| **Profile** | `#identity` (also `#profile`, `#portfolio`) | — |
| **Plan & Usage** | `#plan` (also `#billing`, `#api-keys`) | API keys |
| **Security & Privacy** | `#security` (also `#settings`, `#sessions`) | Signed-in devices |

## Overview section

| Element | Contents |
| --- | --- |
| **Statement** | Month heading, summary line, ledger rows **Plan**, **Credits used**, **Credits left**, **Your work**, **Two-factor authentication** (**Set it up**), **Where the credits went** table, **Plan & usage in full** |
| Your work | Count heading, up to 12 tiles, **Open the library** or **Open the tools** |
| **Next** | Up to three of **Turn on two-factor**, **Group your work**, **Make an API key**, each with a dismiss **×** |
| **Start something** | **Colour tools**, **Palettes**, **Gradients**, **Shades**, **Contrast**, **Analyse a page**, **All tools** |
| **Finish setting up** | **Add your name**, **Choose a username**, **Verify your email**, **Add a profile photo**; buttons **Add**, **Pick**, **Verify** |
| **Tool tokens** | Balance, allowance, bar, note |
| **This device** | Browser and system, **Active now** |

Guide: [Overview section](dashboard-overview.md).

## Profile section

| Control | Rules |
| --- | --- |
| **Profile photo** | Double-click (or `Enter` / `Space`); PNG, JPG or GIF up to 2 MB; uploads on **Save changes** |
| **Display name** | Up to 64 characters |
| **Username** | 3–30 letters, numbers and underscores; once every 30 days; live availability line |
| **Bio** | Up to 500 characters |
| **Email address** | Read-only |
| **Website** | Up to 200 characters, `http://` or `https://` |
| **Location** | Up to 120 characters |
| **Save changes** | Saves all fields ("Profile saved.") |
| **How you appear** | Live preview card |
| **Public portfolio** card | **Portfolio builder**, **Live** or **Not published**; **View page**, **Open the builder** |

### Photo viewer

| Control | What it does |
| --- | --- |
| **Change photo** | Uploads a new photo at once |
| **Gallery** | Opens the Auric avatar gallery |
| **Remove** | Removes the photo at once |
| **×**, `Esc`, click outside | Closes the viewer |

### Avatar gallery

| Control | Values |
| --- | --- |
| Tabs | **Free** (120), **Paid** (420) |
| Filters | **All**, **Companions**, **Wildlife**, **Farm**, **Ocean**, **Fantasy**, **Future**, **Botanical**, **Cosmic**, **Signature**, **3D**, **Animated** |
| Featured | **Auric Muse** (Paid tab) |
| A design | Applies it at once; paid designs are locked on the free plan |

Guide: [Profile section](profile.md).

## Plan and Usage section

| Control | What it does |
| --- | --- |
| **Change Plan** | Opens the pricing page |
| **Request a refund** | On a paid pass; opens the contact page |
| **Cancel Subscription** | Only on a genuinely renewing subscription (not sold today) |
| **Manage Billing** | Only for a card-based subscription portal (not used today) |
| Usage meters | **Vision sims today**, **URL analyses this month**, **SVG recolors this month**, **Experiment runs**, **Projects**, **Team seats** |
| **Change plan** (folded) | Plan cards: **Current plan**, **Get this plan**, **Switch plan**, **Switch to Free**, **Coming soon**; **See the full comparison** |
| **Invoices & Payment History** | Table with **View**; **<- Newer**, **Older ->**; 25 per page |

### API console (plans with API access, or accounts that hold keys)

| Control | What it does | Values |
| --- | --- | --- |
| **Active Keys**, **Requests Today**, **Rate Limit / min**, **Monthly Usage** | Summary figures | — |
| **Connect a key** / **Try again** | Jumps to the key field / retries | — |
| **Show as table** / **Hide table** | Switches the daily chart to a table | — |
| **Create your first key** / **Create key** | Opens the key name field | Up to 10 keys |
| Key name, **Create**, **Cancel** | Names and creates a key | Name up to 64 characters |
| **Copy**, **Done** | Copy the new key; close the panel | Shown once |
| **Revoke** | Revokes a key | Immediate |
| **Add credits** | Opens the pack picker | 100,000 / 550,000 / 2,400,000 / 13,000,000 credits |
| **Paid overage** switch | Lets calls spend prepaid credits past the allowance | Off by default; turning on needs **Turn on paid overage** (or **Keep it off**) |
| **Monthly spend cap**, **Save** | Caps overage per month | $0–$10,000; 0 = no cap of your own |
| **API key**, **Watch traffic** | Connects the live feed | Kept in this tab only |
| **Errors only**, **Pause** / **Resume**, **Disconnect** | Live feed controls | — |
| **View API Docs**, **Endpoint Index** | Open the API documentation | — |

Guides: [Plan & Usage section](plan-and-usage.md), [API keys](api-keys.md), [API credits and spend controls](api-credits-and-spend.md).

## Security and Privacy section

| Control | What it does |
| --- | --- |
| **Password** › **Change** | Opens the change form: **Current password**, **New password (12+ chars, mixed)**, **Repeat new password**, **Update password**, **Cancel** |
| **Two-factor** › **Enable 2FA** | Setup: QR code, secret, **Open in authenticator**, code, **Verify & enable**, **Download backup codes** |
| **Two-factor** › **Disable 2FA** | **Account password**, code, **Disable 2FA** |
| **Usage data** switch | Saves your usage-data choice to the account |
| **Cookies** › **Change** | Opens the Cookie Policy page |
| **Sign out everywhere** | Press twice within about six seconds; signs out every other device |
| **Revoke** | Signs out one device |
| **See all sign-ins** / **Hide sign-ins** | Shows up to six recent successful sign-ins |
| **Export** | Downloads the JSON export |

### Danger zone

| Control | What it does |
| --- | --- |
| **First, type this sentence** | Must match the displayed sentence word for word |
| **Then your account password** | Your password |
| **Unlock for 5 minutes** | Opens the zone; **Lock now** closes it |
| **Erase** › **Type ERASE to confirm** › **Erase** / **Cancel** | Clears this browser's workspace |
| **Delete account…** › **Type DELETE to confirm**, **Confirm your password** › **Permanently delete account** / **Cancel** | Deletes the account |

Guides: [Security & Privacy section](security-and-privacy.md), [Delete your account](delete-your-account.md).

## Finish setting up panel

| Control | What it does |
| --- | --- |
| **Username** | Suggested handle, live **Available** check |
| **Your name** | Up to 64 characters |
| **Send it again** | Resends the verification link |
| **Save**, **Later**, **×**, `Esc` | Save, or dismiss for a week |

## Pricing page controls

Address: https://auricartisan.com/company/pricing/

| Control | What it does |
| --- | --- |
| **Monthly** / **Annual** switch | Shows monthly or annual prices; **Save 17%** badge |
| **USD $**, **INR ₹** | Chooses the currency (remembered in this browser) |
| **What's included** | Expands or collapses a plan card's feature list |
| **Get Started Free** | Opens the sign-in page |
| **Get Artisan** | Starts checkout (asks you to sign in first if needed) |
| **Coming soon** | Disabled; the tier is not on sale |
| **Current Plan** | Your own plan; disabled |
| Token estimator: number field, **−**, **+**, plan tiles | Recommends the plan whose allowance covers your usage |
| **Talk to us**, **Compare plans**, **Open the tools — free**, **Create an account** | Links |

## Upgrade dialog

Some paid conveniences open a dialog instead of a page. Its title is "Do more with" a plan, "You're on a roll" (when a free allowance is used up), or "Not available yet" (when the feature belongs only to a tier not on sale). It lists up to four perks and the monthly price, with **Upgrade to** the plan and **Not now** (or **See the roadmap** and **Close**). Its footer reads "Every tool stays free", "One-time — never auto-renews" and "7-day money-back". Close it with **×**, **Not now**, `Esc` or by clicking outside.

## Related

- [Troubleshooting](troubleshooting.md)
- [Limits](../others/limits-and-accuracy.md)
- [Keyboard shortcuts](../others/shortcuts.md)
