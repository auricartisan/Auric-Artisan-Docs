---
title: Auric Artisan Font Hub — FAQ
description: Short answers to common questions about Auric Artisan Font Hub.
product: VS Code extensions › Auric Artisan Font Hub
updated: 2026-09-25
---

# FAQ

## How many fonts are there?

2,023 library families, 547 of them variable. With `auricFontLib.includeSystemFonts` on, metadata for common system fonts is added.

## Does it work offline?

Browsing, searching, details and licences work offline from the bundled snapshot. Font previews and downloads need the network unless they are already cached.

## Does it use Google Fonts?

No. Embeds point to `https://fonts.auricartisan.com`. Font Hub does not substitute another font service.

## Will it change my existing CSS?

No. Automatic insertion only adds a stylesheet and a new class. It does not replace selected text, edit your rules or apply the font to the whole page. You can preview every change first, and one undo removes it.

## Why did it copy an embed instead of inserting?

For JSX, TSX, Vue, Svelte, Astro, data files and other languages, the right place for a font depends on your framework, so Font Hub copies the embed for you to place. It also copies when no editor is open.

## Does it create files in my project?

Opening Font Hub creates nothing. Files are only written when you insert into the active document, save a snippet, or save a kit.

## Can I use the fonts commercially?

It depends on each font's licence. Check the **License** tab. The extension's own licence does not grant rights to any font.

## Are the scores reliable?

They are catalogue estimates from measured traits, useful for shortlisting. Always test with your real text, languages, sizes and colours.

## Is anything I do uploaded?

No. Search queries, your code, favourites and history stay on your computer. The CDN sees the ordinary information of each request, such as your IP address. There is no analytics and no account.

## Why do settings start with `auricFontLib`?

The extension was previously called Font Library. The prefix is kept so existing settings and shortcuts keep working.

## Is the interface available in Hindi?

Not at present; the interface is in English.
