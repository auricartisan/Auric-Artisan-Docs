---
title: Design System Generator — FAQ
description: Short answers to common questions about the Design System Generator.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Design System Generator FAQ

## Is it the same as "Design Engine"?

Yes. The page's title is the Design System Generator; its address and some labels use Design Engine.

## Do I need an account?

No, to generate, share and export. Saving systems uses your Auric Artisan Library; see the [Library Kit](../../../../kits/library-kit/README.md).

## Is anything generated on a server?

No. The system is calculated in your browser. The page downloads fonts and icons for the previews; see [Privacy](../others/privacy.md). The same job is also available through the public REST API, which is billed in API credits.

## Will the same inputs always give the same system?

Yes. That is why a share link reproduces a system. The only exceptions are the ramp shape and token naming, which links and saved systems do not carry; see [Share, save and connect](share-save-and-connect.md).

## Where is the Generate button?

There is none. Every change regenerates the system at once.

## Why is there no dark-theme score?

The score is calculated from the light roles. The dark roles are fully audited in the audit view under **Dark**.

## Which export should I use?

CSS or JSON if you want everything. Tailwind v4 for Tailwind projects with roles. Figma / W3C to import into Figma Variables or Tokens Studio (colours, type, spacing, radius and shadow only). The native formats for Android, iOS, Flutter or Compose (colours and dimensions). See [Export tokens](export-tokens.md).

## Can I use my own font or icon set?

The tool recommends from its own list. After export, replace the font families and icon set in your project as you like.

## Are the fonts free to use?

The recommended families are served through the Auric font CDN and Google Fonts. Check each family's licence in the [Font Library](../../font-library/README.md) before using it in a product.

## Does passing the audit make my product accessible?

No. It shows that the defined colour pairings meet their contrast requirements. Layout, font size, focus states and many other requirements are up to you.

## Related

- [Troubleshooting](troubleshooting.md)
- [Getting started](getting-started.md)
