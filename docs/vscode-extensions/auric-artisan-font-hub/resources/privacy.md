---
title: Auric Artisan Font Hub — privacy
description: What Auric Artisan Font Hub keeps on your machine and what it sends over the network.
product: VS Code extensions › Auric Artisan Font Hub
updated: 2026-09-25
---

# Privacy

## What stays on your machine

- Search queries, your source code, favourites, recents, selection and usage history. Recommendations that use "local use" are calculated on your computer.
- The cache of previews, font files and refreshed metadata, in VS Code's extension storage.
- No account, no analytics integration and no telemetry.

## What uses the network

Font Hub contacts one address, `https://fonts.auricartisan.com`, and only for:

- refreshing the catalogue (on the `auricFontLib.catalogRefresh` schedule, or when you ask);
- fetching fonts for previews that are not cached;
- loading full licence texts;
- downloading self-hosting kits;
- the CDN check you run.

Requests go through VS Code, not through the Font Hub panels, and every address is validated first. The CDN receives the ordinary information any web request carries, such as your IP address.

Switch all of this off with `auricFontLib.network.enabled` set to `false`.

## Your website

Embeds that Font Hub adds make your visitors' browsers load fonts from `fonts.auricartisan.com`. If you would rather your site made no requests to it, use a self-hosting kit instead.

## Links

**Explore Fonts on AuricArtisan.com** and the **auricartisan.com ↗** links open your browser.
