---
title: Auric Artisan Icon Studio — Related extensions and comparison
description: How Icon Studio compares with Icon Hub, the Auric icon collections, File Icons, Emoji and the Icon Pack, and which to install for each job.
product: VS Code extensions › Auric Artisan Icon Studio
updated: 2026-09-25
---

# Related extensions and comparison

Auric Artisan publishes several icon extensions for VS Code. They overlap on purpose, so this page explains which one does what.

## At a glance

| Extension | Main job | Explorer file icon theme | Artwork | Network |
| --- | --- | --- | --- | --- |
| [Icon Studio](../README.md) | One offline studio to search and insert every Auric collection, emoji and seven open-source sets. | No | 17,234 entries in 11 collections | None |
| [Icon Hub](../../auric-artisan-icon-hub/README.md) | Seven open-source sets with size, colour and stroke controls, sprite and ZIP export, and CDN insertion. | No | 12,895 icons | Optional catalog metadata checks; CDN output loads from the web |
| [Auric Icons: Modern](../../auric-icons-modern/README.md) | Modern icon library plus the Modern file and folder icon theme. | Yes: **Auric Icons: Modern** | 720 library icons; 408 theme icons | None |
| [Auric Icons: Drawn](../../auric-icons-drawn/README.md) | Warm Drawn icon library. | No | 480 icons | None |
| [Auric Icons: Playful](../../auric-icons-playful/README.md) | Emoji-style icon library. | No | 1,225 icons | None |
| [File Icons](../../auric-artisan-file-icons/README.md) | Explorer file and folder icons, plus a File Icon Studio to insert that artwork. | Yes: Facet, Playful and Modern | 1,464 SVG assets | None |
| [Emoji](../../auric-artisan-emoji/README.md) | Emoji Studio with shortcodes, sequences, completions and six copy formats. | No | 1,914 emoji | None |
| [Icon Pack](../../auric-artisan-icon-pack/README.md) | Installs Modern, Playful, Drawn and Emoji together. | Through Modern | None of its own | Needs the Marketplace to install |

## Which should I install?

- **I want icons and emoji in my code, offline, in one place:** Icon Studio.
- **I want to recolour, restroke and export open-source icons, or load them from a CDN on my site:** Icon Hub.
- **I want my Explorer's file and folder icons to change:** File Icons (or Modern's own file theme).
- **I only want one Auric artwork style with its own interface:** Modern, Drawn or Playful.
- **I want the full emoji workflow (sequences, shortcode completion, replace in selection):** Emoji.
- **I want the four creative libraries installed together in one step:** Icon Pack.

## How the three collections merge

Modern, Drawn and Playful are built on the same library core and know about each other.

- **Without Icon Studio:** when two or three are installed, one becomes the host automatically and shows a single merged Icon Library. It adds a **Library** filter and a badge on each card showing which collection it comes from, and offers every collection's variants in one switcher. The other extensions hide their views and forward their commands to the host. This re-runs when you install or remove one, without a reload.
- **With Icon Studio:** by default Icon Studio hosts all three, so their separate views and shortcuts are hidden and you use Icon Studio instead. Set `auricIconStudio.hostFamilyLibraries` to `false` to get their own interfaces back.
- **Personalisation stays with its owner.** Likes and recent icons belong to the extension that owns the icon, so uninstalling one extension never removes another's history. Icon Studio keeps its own separate likes and recents.

See [Work with the Auric collection extensions](../docs/auric-collections.md) for the settings.

## Name clashes to be aware of

- **"Playful"** means two different things. In File Icons it is an Explorer file icon style with 500 file and folder SVGs. In **Auric Icons: Playful** it is a 1,225-icon emoji-style library. They are different artwork.
- **"Modern"** file icons exist in both File Icons and Auric Icons: Modern, under the same theme ID. See [File Icons](../../auric-artisan-file-icons/docs/modern-and-legacy.md) for how to avoid duplicates.
- **"Icon Studio"** is the name of this extension and also the heading of the merged library view inside the Modern, Drawn and Playful extensions.

## Other related products

- [Install and set up](../../install-and-setup/README.md) — installing and managing Auric extensions.
- [Icon Library on the website](../../../website/tools/colour-workspace/icon-library/README.md) — browse open-source icons in the browser.
- [Icon CDN](../../../services/icon-cdn/README.md) — the icon delivery service used by Icon Hub's CDN output.
