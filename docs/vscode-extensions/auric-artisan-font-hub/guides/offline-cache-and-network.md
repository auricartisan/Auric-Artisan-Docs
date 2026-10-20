---
title: Auric Artisan Font Hub — offline use, cache and network
description: What Font Hub can do offline, how it refreshes and caches catalogue data and fonts, and how to switch its network use off.
product: VS Code extensions › Auric Artisan Font Hub
updated: 2026-09-25
---

# Offline use, cache and network

## What works offline

The extension includes a snapshot of the catalogue: every family's details and the licence notices. Without a network connection you can:

- search, filter, sort and browse every family;
- open details, including styles, charset, about and licence information;
- use favourites, recents, selection and the recommender;
- copy and insert embeds (the page that uses them still needs the CDN when it loads).

Font previews and self-hosting downloads need the font files. Previews you have already seen stay available from the cache where possible; others need the network.

## What uses the network

Only one address is ever contacted: `https://fonts.auricartisan.com`. Font Hub validates every address before requesting it, and the Font Hub panels themselves cannot make network requests; all fetching goes through VS Code.

| Activity | When |
| --- | --- |
| Catalogue refresh | On the schedule in `auricFontLib.catalogRefresh`, or when you run **Refresh Font Catalog from Auric CDN** |
| Font previews | When a card or detail panel needs a font that is not cached |
| Licence text | When you select **Load full license text** or build a kit |
| Self-hosting downloads | When you download a kit |
| CDN check | When you run **Check Font CDN and Browser CORS** |

Search queries, your source code, favourites and usage history are not sent. The CDN still receives the ordinary information any web request carries, including your IP address.

## Switch the network off

Set `auricFontLib.network.enabled` to `false`. Font Hub then works from the bundled snapshot and the cache only. Previews that are not cached are unavailable, the CDN check is refused, and kits cannot be downloaded.

## Catalogue refresh

| `auricFontLib.catalogRefresh` | Behaviour |
| --- | --- |
| `manual` | Only when you run **Refresh Font Catalog from Auric CDN** (or select **↻**) |
| `daily` (default) | Automatically, once the last refresh is older than `auricFontLib.cache.maxAgeHours` (24 hours by default) |
| `always` | Automatically every time Font Hub checks, without waiting for the cache to age |

After a refresh: **Auric Font Hub refreshed *N* families.** If the refresh fails or is rejected, Font Hub keeps what it had: **Auric Font Hub kept cached data: *reason*.** The bundled snapshot always remains available. Refreshed identities and licence data are validated; a family the extension does not recognise may need an extension update.

The status bar **Fonts** item's tooltip shows the number of families and whether the **CDN catalog**, a **Cached catalog** or the **Bundled catalog** is in use. Turn the item off with `auricFontLib.statusBar.enabled`.

## Cache

| Setting | Default | Range | Meaning |
| --- | --- | --- | --- |
| `auricFontLib.cache.maxAgeHours` | 24 | 1–720 | How long cached CDN metadata counts as fresh |
| `auricFontLib.cache.maxMB` | 512 | 64–4096 | Disk space for previews, font files and refreshed metadata; the oldest items are removed first |

The cache lives in VS Code's storage for the extension, not in your project. **Auric Artisan Font Hub: Clear Downloaded Font Cache** empties it: **Auric Font Hub cache cleared. Bundled catalog data remains available offline.**

## System fonts

With `auricFontLib.includeSystemFonts` on, metadata for common system fonts captured when the catalogue was built appears in the list. Their previews depend on the font being installed on your computer.
