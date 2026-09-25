---
title: Icon Library — FAQ
description: Short answers to common questions about the Icon Library.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Frequently asked questions

## Do I need an account?

No. Browsing, copying and downloading all work without signing in.

## Can I use these icons in commercial projects?

Each set keeps its own open licence: MIT (Phosphor, Tabler, Heroicons, Feather), ISC (Lucide), the Remix Icon licence (Remix) and Apache 2.0 (Material). The panel shows each icon's licence and author, and links to the set's website where the full terms are. See also [Icon CDN licences](../../../../../services/icon-cdn/others/licences.md).

## Why do icons change colour with my text?

The icons are drawn in `currentColor`, which means "the colour of the surrounding text". Pick a colour in the panel before copying to fix it, or set `color` in your CSS.

## Which format should I copy?

- **SVG** to paste into HTML or a design tool.
- **JSX** for a React component.
- **data-URI** for an `<img>` tag or a CSS background without a separate file.
- **CDN tag** to let the Icon CDN script insert the icon for you.

## Can I mix icons from different sets?

Yes, but sets differ in line weight, corner style and grid size. For a consistent look, keep to one set, or compare the same idea across sets by searching its name with **All** chosen.

## Can I upload my own icons?

No. The library shows the seven bundled sets only.

## Is my kit shared between devices?

No. It is kept in the browser on the device where you made it.

## Related

- [Troubleshooting](troubleshooting.md)
- [Getting started](getting-started.md)
- [Icon CDN FAQ](../../../../../services/icon-cdn/docs/faq.md)
