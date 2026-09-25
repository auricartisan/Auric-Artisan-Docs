---
title: Font CDN — FAQ
description: Short answers to common questions about the Auric Artisan Font CDN.
product: Services › Font CDN
updated: 2026-09-25
---

# FAQ

### Is the Font CDN free?

The CDN's stylesheets, files and loader are served publicly, and the Font Library page needs no sign-in to copy embed code or download kits. Each font keeps its own licence terms; see [Licences](../others/licences.md).

### Do I need an API key?

No.

### How is this different from Google Fonts?

It works the same way, with a stylesheet per family, but everything is served from fonts.auricartisan.com, including fonts that came from other open sources, and every family comes with its licence text and a downloadable self-hosting kit.

### Can I use these fonts in commercial projects?

Most families are under open licences that allow commercial use, such as the SIL Open Font License. Check each family's **License** tab: it shows the licence and a permissions summary.

### Can I choose only some weights to download less?

The stylesheet always declares the whole family. Browsers generally download a font file only when the page uses that style. To ship exactly the files you want, self-host and remove the rules you do not need.

### Can I use the fonts offline or behind a firewall?

Yes: download the kit and serve it from your own site. See [Self-host a family](self-host-a-family.md).

### What does "Installed" mean?

The family is a system font listed for reference. Its licence does not allow redistribution, so the CDN does not serve it and it cannot be downloaded.

### Are variable fonts supported?

Yes. 550 families are variable; their stylesheets declare a weight range, and width where the font has it.

### Can I use a font file that is not in the library?

Yes, with `AuricFonts.face({ family, url })`, which registers any font file you have the rights to.

### Where are the fonts' licences?

In each family's **License** tab, in the `LICENSE.txt` of each kit, in the stylesheet's header comment, and in the collection reference at https://fonts.auricartisan.com/LICENSE.md.
