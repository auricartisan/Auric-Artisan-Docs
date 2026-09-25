---
title: Troubleshooting
description: Fixes for general Auric Artisan problems — browser support, pages that look out of date, cookies and consent, sign-in, payments, offline use, language and theme, and clearing site data.
product: Help
updated: 2026-09-25
---

# Troubleshooting

Each entry gives the symptom, the likely cause and what to do. Problems specific to one tool are covered in that tool's own troubleshooting page; account and payment problems in detail are in [Account and billing troubleshooting](../website/account-and-billing/docs/troubleshooting.md).

## Browser support

The website is built for current, modern browsers. The download page says the same package runs on Windows, macOS, Linux, ChromeOS, Android, iOS and iPadOS, and that offline caching works "anywhere with a service worker and a secure origin".

| Symptom | Why | What to do |
| --- | --- | --- |
| A tool does not start, or a panel stays blank | An old browser version, or a browser feature the tool needs (such as canvas or WebGL graphics) is turned off | Update your browser; try another current browser |
| Copy buttons do nothing | The browser blocked clipboard access | Allow clipboard access for auricartisan.com, or select and copy the text yourself |
| The eyedropper in **Settings** is missing | Not every browser offers a screen eyedropper | Use the colour picker beside it |
| A download or export window does not open | A pop-up blocker stopped it | Allow pop-ups for auricartisan.com |
| The site behaves oddly in one browser only | An extension (ad blocker, script blocker) interferes | Try a private window with extensions off |

The download page's **Check local hardware** and **Check readiness** buttons report what your browser supports.

## A page looks out of date or broken

| Symptom | What to do |
| --- | --- |
| A page shows old content after an update | Reload the page. If you installed the app, open https://auricartisan.com/download/ and select **Update app** when it appears. |
| Layout or styling is broken | Reload; if it persists, open the download page and use **Audit cache**, then **Repair cache**. |
| Nothing helps | Use **Reset cache** on the download page, or see [Clear site data and start fresh](#clear-site-data-and-start-fresh). |

## Cookies and consent

| Symptom | Why | What to do |
| --- | --- | --- |
| The cookie bar appears on every visit | Your choice is stored in the browser; private windows and cleared site data forget it | Use a normal window, or allow site data for auricartisan.com |
| The cookie bar does not appear on the sign-in page | It is deliberately not shown over sign-in and verification pages | Choose later on any other page, or at https://auricartisan.com/legal/cookies/ |
| You want to change your choice | — | Open https://auricartisan.com/legal/cookies/ › **Manage Cookie Preferences**, change the switches and select **Save Preferences** |
| You want to start over | — | On the same page select **Withdraw Consent** or **Clear All Cookies** |

Essential cookies cannot be turned off; without them you cannot stay signed in. See [Cookie Policy summary](../website/company-and-legal/docs/cookie-policy.md).

## Sign-in problems

| Symptom | Why | What to do |
| --- | --- | --- |
| You sign in but appear signed out on the next page | The browser blocked cookies for auricartisan.com | Allow cookies for the site; its sign-in cookies are first-party |
| Actions fail with a message about the page's session token | You opened the site over an insecure address, or signed out in another tab | Use https://auricartisan.com and reload the page |
| You are signed out unexpectedly | Your session ended: a password change, a revoked device, seven days without use, or closing the browser without **Remember me** | Sign in again |
| Human check, verification, reset or two-step problems | — | See [Account and billing troubleshooting](../website/account-and-billing/docs/troubleshooting.md#i-cannot-sign-in) |

## Payments

| Symptom | What to do |
| --- | --- |
| Checkout will not open | Allow pop-ups and scripts for auricartisan.com and Razorpay, then try again |
| A foreign card is declined | Nothing is charged. Try another method, or tell Auric Artisan through the contact page |
| Paid but the plan is not showing | Refresh the dashboard; quote the order reference to support if it persists |
| Anything else | See [Payments and checkout](../website/account-and-billing/docs/troubleshooting.md#payments-and-checkout) |

Never pay anywhere other than the Razorpay checkout on auricartisan.com.

## Offline and the installed app

| Symptom | Why | What to do |
| --- | --- | --- |
| No **Install app** button | Whether to offer installation is the browser's decision | On iPhone and iPad use **Add to Home Screen** in Safari; on desktop try Chrome or Edge |
| A tool will not open offline | It was not cached, or the **Lite** profile keeps only core tools | Go online, open the tool once, or choose **Balanced** or **Full** and select **Prepare offline version** |
| The offline copy disappeared | The browser cleared the cache to free space | Grant persistent storage when asked, then prepare the offline version again |
| Sign-in, the dashboard or checkout fail offline | They always need a connection | Reconnect |
| Offline copy is out of date | — | Go online and select **Update app** on the download page |

See [Offline use](../getting-started/offline-use.md) and [Download and offline](../website/download-and-offline/README.md).

## Language and theme

| Symptom | What to do |
| --- | --- |
| A few words stay in English in Hindi | Technical names (colour spaces, models, fonts) and some third-party names stay in Latin script by design |
| Search finds nothing in Hindi | Search in English |
| Switching back to English reloads the page | Expected: the original text is loaded again |
| The theme keeps changing | You chose **System** or **Auto**, which follows your device; pick **Light** or **Dark** |
| Theme or language is not remembered | They are stored per browser; private windows and cleared site data reset them |

## Clear site data and start fresh

Clearing Auric Artisan's site data in your browser removes everything the site keeps in that browser:

- your library of saved palettes, gradients, collections and exports;
- your portfolio draft;
- your settings (theme, language, accent colour, text size and so on) and your cookie choice;
- the offline cache;
- your sign-in on that browser.

It does not touch your account, your plan, your published portfolio or anything on other devices.

> **Important:** Export anything you want to keep first — see [Export your data](../website/account-and-billing/docs/export-your-data.md) — because the library exists only in your browser.

### Gentler options first

- To clear only your saved work and preferences but stay signed in: dashboard **Security & Privacy** › danger zone › **Erase this browser's workspace**.
- To clear only the offline cache: https://auricartisan.com/download/ › **Reset cache**.
- To reset only settings: **Settings** › **Reset all**.

### Clear everything in your browser

The Cookie Policy lists where to find the controls:

| Browser | Where |
| --- | --- |
| Chrome | Settings › Privacy and security › Cookies and other site data |
| Firefox | Settings › Privacy & Security › Cookies and Site Data |
| Safari | Settings › Privacy › Manage Website Data |
| Edge | Settings › Cookies and site permissions › Manage and delete cookies |

Find auricartisan.com and remove its data, then reload the site.

## Still stuck

Report it through https://auricartisan.com/company/contact/ with the topic **A bug**. Include the page address, your browser and what you expected. See [Contact and support](contact-and-support.md).
