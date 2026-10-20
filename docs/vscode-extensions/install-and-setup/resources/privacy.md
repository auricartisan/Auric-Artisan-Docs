---
title: Privacy — what the Auric Artisan VS Code extensions keep local and what uses the network
description: A summary of which Auric Artisan extensions use the network, what they send, and where their data is stored.
product: VS Code extensions › Install and setup
updated: 2026-09-25
---

# Privacy

## Installing

Installing, updating and searching for extensions happens between VS Code and the Visual Studio Marketplace. That is VS Code's own traffic, covered by Microsoft's terms, and it is the same for every extension.

## Once installed

The Auric Artisan VS Code page states that none of the extensions contains telemetry. Most work entirely on your machine. Three use the network as part of their job:

### Auric Artisan Live

- Runs a development server on your machine. With the default host `0.0.0.0`, other devices on your local network can reach it, subject to your firewall.
- Proxy routes you configure forward requests to the targets you name.
- The phone QR code is generated locally; no address goes to a QR service.

### Auric Artisan Font Hub

- Refreshes its catalogue, fetches preview fonts and downloads self-hosting files from `fonts.auricartisan.com`. Switch this off with `auricFontLib.network.enabled`.
- Search queries, source code, favourites and usage history are not uploaded. The CDN still receives ordinary request information, such as your IP address.

### Auric Artisan Icon Hub

- Checks `icons.auricartisan.com` for catalogue updates, and can be switched off in its settings.
- Your code, searches and favourites are not sent.

Everything else ships inside the extension. Opening a website link from a panel (for example **auricartisan.com ↗**) opens your browser and needs a network connection.

## Where data is kept

- **Settings** live in your user or workspace `settings.json`, like any VS Code setting.
- **Favourites, recents, likes, tags, groups, history and similar** are kept in VS Code's extension storage on your machine. They are not copied by Settings Sync.
- **Project files** you create (such as `auric.live.json`, `.auricformatrc` or File System's `.auric/trash`) stay in your project and travel wherever you copy or commit it.

The privacy page in each extension's own folder describes that extension in detail.
