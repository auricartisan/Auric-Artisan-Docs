---
title: Auric Artisan Icon Hub — Privacy
description: What Icon Hub stores, exactly what uses the network, and what is never sent.
product: VS Code extensions › Auric Artisan Icon Hub
updated: 2026-09-25
---

# Privacy

No account, telemetry or search upload is required.

## What uses the network

| Feature | What is contacted | When |
| --- | --- | --- |
| Metadata checks | Five public JSON files under https://icons.auricartisan.com/data/ | On activation (at most once per interval) and when you select **Refresh**. Can be turned off. |
| **Open Auric Icon Tool** and **Website ↗** | https://icons.auricartisan.com in your browser | Only when you select them. |
| Pages using CDN output | The CDN script, catalog and fonts | When a visitor loads your page, not from VS Code. |

Metadata requests send no credentials and include none of your source code, search terms, favorites or usage history. Like any web request, they reveal ordinary connection information such as your IP address to the host.

To stop all catalog network checks, set `auricIconLib.remoteRefresh.enabled` to `false`.

## What is stored

| Data | Where |
| --- | --- |
| Favorites and recent icons | VS Code's extension storage on this machine. |
| Downloaded metadata | The extension's private storage folder; cleared by **Clear Downloaded Icon Catalog**. |
| Search, filters, selection and colour history | The Hub's saved view state. |
| Settings | Your VS Code settings under `auricIconLib.*`. |

## What is written to your project

Only the CDN bridge file, and only on an explicit Insert into a supported file in a trusted workspace. Copy, Save and browsing never create project files.

## Security

The Hub's webview uses a content security policy with per-session nonces, validates every message, sanitises SVG before preview and export, and never runs the CDN loader inside VS Code.
