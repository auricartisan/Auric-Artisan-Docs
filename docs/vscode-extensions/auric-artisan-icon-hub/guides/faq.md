---
title: Auric Artisan Icon Hub — FAQ
description: Short answers to common questions about Auric Artisan Icon Hub.
product: VS Code extensions › Auric Artisan Icon Hub
updated: 2026-09-25
---

# Frequently asked questions

## Why is the extension ID "icon-lib" when it is called Icon Hub?

The extension keeps its original ID, `auric-artisan.auric-artisan-icon-lib`, so existing `auricIconLib.*` settings, favorites and recent items carry over. Its display name is **Auric Artisan Icon Hub**.

## Does Icon Hub work offline?

Yes, for browsing, searching, previewing, copying, saving and exporting. The optional metadata checks and pages that use the CDN need a network connection.

## Does it upload my code or searches?

No. Metadata checks request five public JSON files and include no source code, search terms, favorites or usage.

## Why does Insert create a file in my project?

In HTML and web-framework files, Insert connects the Auric icon CDN through a small loader file, `icons.auricartisan.com.js`. It is only created on an explicit Insert. Copy and Save never create files. See [Connect the icon CDN](cdn-insertion.md).

## How do I get self-contained SVG instead?

Use **Copy** or **Save** with the SVG format, export a ZIP, or insert into a CSS, SVG or other non-web file.

## Does it include Auric artwork or emoji?

No. Icon Hub covers the seven open-source collections. Auric Artisan Icon Studio adds the Auric Modern, Drawn and Playful artwork and emoji.

## Can I use exported icons commercially?

Each collection keeps its own licence: MIT (Phosphor, Tabler, Heroicons, Feather), ISC (Lucide), Remix v1.0 (Remix) and Apache-2.0 (Material). The ZIP export includes the licence notices.
