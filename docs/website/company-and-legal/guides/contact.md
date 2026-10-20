---
title: Contact page — summary
description: A plain-language summary of Auric Artisan's Contact page — the three inboxes, the seven topics, reply times and what happens after you send a message.
product: Website › Company and legal
updated: 2026-09-25
---

# Contact page

Official page: https://auricartisan.com/company/contact/. This summary explains how the page is organised; the step-by-step guide is [Contact and support](../../../help/contact-and-support.md).

## What the page is

A single form that routes your message to one of three inboxes, depending on the topic you pick. The page says every message "is read and answered by a person — there is no ticket queue and no bot in front of it", and that replies can be late at weekends or during a release. It links **Check the FAQ first** at the top.

## The three inboxes and seven topics

| Inbox | What it is for | Topics |
| --- | --- | --- |
| hello@auricartisan.com | "Everything that is not a bug, an integration, or a security matter." | **Using a tool**, **Billing**, **Something else** |
| developer@auricartisan.com | Bugs and the API — "Send the request, the response, and what you expected instead." | **A bug**, **API or integration** |
| security@auricartisan.com | Vulnerabilities and data requests, "Handled under the disclosure process on the security page, ahead of everything else." | **Security**, **Privacy or data** |

The address shown on the page is what you are told; the site decides the destination from the topic you choose.

## Reply times by topic

| Topic | Reply time shown |
| --- | --- |
| Using a tool | 2–3 days |
| Billing | 1–2 days |
| A bug | 2–4 days |
| API or integration | 2–4 days |
| Security | Within 48 hours |
| Privacy or data | Within 30 days |
| Something else | Up to a week |

The page's description and the FAQ also give a general figure of 1–3 business days.

## The form

- **Name**, **Email** and a reference field whose label changes with the topic (for example **Order or invoice ID** for Billing, **URL where it happened** for a bug, **Affected URL or endpoint** for Security).
- A message editor with bold, italic, inline code, bulleted list, code block and link, sent as plain text; up to 2,000 characters.
- Up to four images (PNG, JPEG, GIF or WebP, up to 12 MB each before they are shrunk), which you can mark up with a pen, highlighter or box.
- Each topic shows links that might answer the question faster.
- The **Security** topic shows a notice: do not put a working exploit in the form; send the location and impact, and a way to send the rest will follow.

## What happens next

The page lists three steps: you get a confirmation at the address you gave; the reply comes from the inbox, in that thread; and if the message leads to a change, you get the link when it ships.

## Deep links

Adding `?topic=` and a topic name opens the form with that topic chosen, for example https://auricartisan.com/company/contact/?topic=security, which the Security page uses.

## Related

- [Contact and support](../../../help/contact-and-support.md)
- [Security page](security-page.md) — responsible disclosure
