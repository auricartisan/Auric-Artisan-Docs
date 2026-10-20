---
title: API keys
description: Create, view, copy and revoke Auric Artisan API keys in the dashboard, and understand key limits, plans and what happens after a downgrade.
product: Website › Account and billing
updated: 2026-09-25
---

# API keys

An API key lets your own code call the Auric Artisan REST API as your account. Keys are created and revoked in the dashboard, under **Plan & Usage** › **Your API Keys**. How to use a key in a request, and every endpoint, is documented in [Public API](../../../services/public-api/README.md) and on https://auricartisan.com/library/documentation/api/.

## Before you start

- **Plan.** API access is included from the **Specialist** plan upward. On Apprentice and Artisan the create button is withdrawn, because a key there would authenticate but be refused on every metered call. Specialist is marked **Coming soon** on the pricing page today.
- **Verified email.** API keys are locked until your email address is verified.
- **Limit.** An account can hold up to 10 active keys.
- **One meter per account.** Every key on the account draws on the same monthly credit allowance and the same prepaid balance. Credits are counted per account, not per key.

## Create a key

1. Open the dashboard and select **Plan & Usage**.
2. In **Your API Keys**, select **Create your first key** (or **Create key** if you already have some).
3. Type a name that says where the key is used, for example "CI pipeline". Names can be up to 64 characters.
4. Select **Create**. (Select **Cancel** to stop.)
5. A panel appears: '"CI pipeline" created — copy it now.' and "This is the only time the full key is shown. We store just a fingerprint."
6. Select **Copy** (it changes to **Copied!**), or select the text in the field and copy it yourself.
7. Store the key somewhere safe, such as a password manager or your deployment's secret settings.
8. Select **Done**.

Result: the key appears in the list. Keys begin with `aa_live_`.

> **Important:** The full key is never shown again. Auric Artisan keeps only a one-way hash of each key and a short prefix, so it cannot recover a lost key. If you lose one, create a new key and revoke the old one.

## The key list

Each row shows:

- the key's **name**;
- its **prefix** — the first characters followed by "…", so you can tell keys apart;
- when it was **created**, and when it was last **used**, or "never used";
- a **Revoke** button.

The number of keys also appears in the **Active Keys** figure and on the **Plan & Usage** tab badge.

## Revoke a key

1. Find the key in **Your API Keys**.
2. Select **Revoke**.

Result: the key is removed from the list and stops working. Any code still using it gets an authentication error. Revoking cannot be undone; create a new key if you need one.

Revoke a key straight away if it may have leaked — for example if it was committed to a public repository.

## After a downgrade

A key outlives the plan that created it. If your account moves to a plan without API access while it still has keys:

- **Plan & Usage** still shows the API console, so you can see and revoke those keys.
- A notice reads "The API is not included on" your plan, and explains: "Keys can still be viewed and revoked here, but calls to metered endpoints return 402 PLAN_UPGRADE_REQUIRED. Full API access is included from Specialist upward." It offers **Compare plans** and **Read the API docs**.
- You cannot create new keys until the account is on a plan with API access again.

## Keys and the live usage panel

The usage figures in the dashboard come from the API itself, which is reached with an API key. To see them, paste one of your keys into **Live usage** › **API key** and select **Watch traffic**. The key is kept in that browser tab only and is forgotten when the tab closes. See [API credits and spend controls](api-credits-and-spend.md#live-usage).

## Messages

| Message | What to do |
| --- | --- |
| "Give the key a name." | Type a name before selecting **Create**. |
| "You can hold at most 10 active keys." | Revoke a key you no longer use, then create the new one. |
| "No API keys yet. Key creation is available from the Specialist plan." | Your plan does not include the API. |
| "Could not load API keys." | Refresh the page. If it persists, sign in again. |
| "Could not revoke key." | Try again; check your connection. |

## Related

- [API credits and spend controls](api-credits-and-spend.md)
- [Plan & Usage section](plan-and-usage.md)
- [Device sign-in](device-sign-in.md) — the command-line tool signs in without a key
- [Public API](../../../services/public-api/README.md)
