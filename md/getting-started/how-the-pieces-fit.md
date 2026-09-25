---
title: How the pieces of Auric Artisan fit together
description: What runs in your browser, what runs on a server, what the account connects, and how the website, extensions and services relate.
product: Getting started
updated: 2026-09-25
---

# How the pieces fit

Auric Artisan is several products built on one colour engine and one design system. This page explains how they relate, so you know what you need to install, what needs an account, and what needs a network connection.

## One engine, several places

The same colour-science code powers the website tools, the Learn library's interactive figures, the REST API, the browser extension and the colour-related VS Code extensions. The author page describes it this way: where an article states a formula or threshold, it is the formula the code uses. In practice this means a contrast ratio or a colour conversion should agree whether you get it from a website tool, the extension or the API.

The products do not depend on each other. You can use the browser extension without ever visiting the website, or the VS Code extensions without an account.

## What runs where

| Product | Where it runs | Needs an account? | Needs a network? |
| --- | --- | --- | --- |
| Website tools (most) | In your browser tab | No | Only to load the page, unless you prepared it for offline use |
| Website Analyzer, basic analysis | In your browser | No | Yes, to fetch the page you analyse |
| Website Analyzer, server-backed runs (rendered analyses, whole-site crawls) | On Auric Artisan's servers | Yes, and uses tokens | Yes |
| Libraries and Learn | In your browser | No | Only to load, unless cached for offline use |
| Portfolio Builder, drafting | In your browser | No for drafting | Publishing needs an account and a connection |
| Dashboard, plans, API keys | On Auric Artisan's servers | Yes | Yes |
| Browser extension | Entirely in your browser | No | No (it makes no network calls) |
| VS Code extensions | On your computer, inside VS Code | No | Only for extensions that fetch fonts or icons |
| REST API | On Auric Artisan's servers | Yes (an API key) and a plan with API access | Yes |

## What the account connects

An account is optional for the tools. When you have one, it connects:

- **Your identity** — a display name, a username (your public handle), a profile photo and a verified email address.
- **Your plan** — the Apprentice (free) plan by default, or a paid plan pass you have bought. A pass belongs to the account, not to one browser, so it follows you to other devices.
- **Tokens** — the balance that pays for server-backed tool work such as whole-site accessibility crawls. See [Tokens](../website/account-and-billing/docs/tokens.md).
- **API keys and API credits** — for the REST API, on plans that include it. See [API keys](../website/account-and-billing/docs/api-keys.md).
- **Your public portfolio** — publishing a portfolio page at your own address.
- **Security** — two-step verification, signed-in devices and a data export.

Most of your saved work (palettes, gradients, collections, drafts and preferences) is stored in your browser, not in the account. The pricing page says so directly: "today the platform syncs account settings and saves your work locally." Cloud sync across devices is listed as coming soon. See [Privacy basics](privacy-basics.md).

## Two separate meters: tokens and API credits

The site uses two units that are easy to confuse:

- **Tokens** pay for work you start in a website tool that runs on Auric Artisan's servers — for example a rendered page analysis or a whole-site crawl. Everything that runs in your browser is free and unmetered.
- **API credits** pay for requests your own code makes to the REST API.

They are separate balances with separate allowances. Neither pays for the other and nothing converts between them. If you only use the website tools you can ignore API credits; if you only use the API you can ignore tokens. Details: [Tokens](../website/account-and-billing/docs/tokens.md) and [API credits and spend controls](../website/account-and-billing/docs/api-credits-and-spend.md).

## Site-wide features

Every website page shares the same header, search, settings and floating kits:

- **Search** — `Ctrl` + `K`, or the **Search** button in the header.
- **Guide** — tours and quick paths; press `?` when you are not typing.
- **Settings** — theme, language, text size, motion and comfort options; `Ctrl` + `,`.
- **Kits** — floating panels such as the Library Kit that open over any page.

See [Site features](../website/site-features/README.md) and [Kits](../website/kits/README.md).

## Related

- [What Auric Artisan is](what-is-auric-artisan.md)
- [Choose where to start](choose-where-to-start.md)
- [Create an account (optional)](create-an-account.md)
