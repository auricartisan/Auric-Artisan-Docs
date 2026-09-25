---
title: Auric Icons: Modern — Related extensions and comparison
description: How Auric Icons: Modern compares with Drawn, Playful, Icon Studio, Icon Hub, File Icons, Emoji and the Icon Pack.
product: VS Code extensions › Auric Icons: Modern
updated: 2026-09-25
---

# Related extensions and comparison

## At a glance

| Extension | Main job | Explorer file icon theme | Artwork | Network |
| --- | --- | --- | --- | --- |
| [Auric Icons: Modern](../README.md) | Modern icon library plus the Modern file and folder icon theme. | Yes: **Auric Icons: Modern** | 720 library icons; 408 theme icons | None |
| [Auric Icons: Drawn](../../auric-icons-drawn/README.md) | Warm Drawn icon library. | No | 480 icons | None |
| [Auric Icons: Playful](../../auric-icons-playful/README.md) | Emoji-style icon library. | No | 1,225 icons | None |
| [Icon Studio](../../auric-artisan-icon-studio/README.md) | One offline studio for every Auric collection, emoji and seven open-source sets. | No | 17,234 entries in 11 collections | None |
| [Icon Hub](../../auric-artisan-icon-hub/README.md) | Seven open-source sets with colour and stroke controls, sprite and ZIP export, and CDN insertion. | No | 12,895 icons | Optional metadata checks; CDN output loads from the web |
| [File Icons](../../auric-artisan-file-icons/README.md) | Explorer file and folder icons in three styles, plus File Icon Studio. | Yes: Facet, Playful and Modern | 1,464 SVG assets | None |
| [Emoji](../../auric-artisan-emoji/README.md) | Emoji Studio. | No | 1,914 emoji | None |
| [Icon Pack](../../auric-artisan-icon-pack/README.md) | Installs Modern, Playful, Drawn and Emoji together. | Through Modern | None of its own | Needs the Marketplace to install |

## How the three collections merge

- Install Modern with Drawn and/or Playful and one of them becomes the host of a single merged library, with a **Library** filter, collection badges on cards and every collection's variants in one switcher. The others hide their views and forward their commands. See [The merged Icon Studio](../docs/merged-icon-studio.md).
- Install Auric Artisan Icon Studio and, by default, it hosts all three instead. Modern's file icon theme keeps working.
- Likes and recent icons stay with the extension that owns each icon.

## Modern in File Icons

Auric Artisan File Icons also includes a Modern Explorer style, with 464 SVG assets (219 file designs, 114 folder pairs, light alternatives and state overlays) and the same four framework packs. It uses the same theme ID as this extension's file icon theme and its own `auricFileIcons.*` settings. If you install both, see [Troubleshooting](../docs/troubleshooting.md#file-icon-theme). The File Icons documentation describes importing Modern's file settings in [Modern and older Playful settings](../../auric-artisan-file-icons/docs/modern-and-legacy.md).

## Retired extensions

Modern supersedes two unpublished preview extensions, "Auric Artisan Drawing Icon" and "Auric Artisan Icons". If either is installed, uninstall it: they share keybindings and command IDs with Modern.

## Other related pages

- [Install and set up](../../install-and-setup/README.md)
- [Icon Library on the website](../../../website/tools/colour-workspace/icon-library/README.md)
