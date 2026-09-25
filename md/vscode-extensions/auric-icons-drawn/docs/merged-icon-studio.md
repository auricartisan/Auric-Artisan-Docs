---
title: Auric Icons: Drawn — Use Drawn with Modern and Playful
description: How Drawn merges with Auric Icons: Modern and Playful into one library, and how Auric Artisan Icon Studio takes over hosting.
product: VS Code extensions › Auric Icons: Drawn
updated: 2026-09-25
---

# Use Drawn with Modern and Playful

Drawn works by itself. When **Auric Icons: Modern** or **Auric Icons: Playful** is also installed, the extensions show one library instead of duplicate sidebars.

## What happens when they are co-installed

1. One extension becomes the **host** automatically. With the current versions, that is Modern when it is installed; with only Drawn and Playful, Drawn hosts.
2. The host's **Icon Library** view (headed "Icon Studio") contains every installed collection.
3. A **Library** filter appears, and each card shows a badge naming its collection.
4. The **Variant** buttons offer every collection's variants. If a collection lacks the selected variant (for example Drawn has no **Filled** or **Small**), its cards fall back to Color.
5. The other extensions hide their views, Command Palette entries and shortcuts, and forward their commands to the host.

This updates on its own when you install or remove a collection. No reload is needed.

## Likes and recents

Likes and recent icons are stored by the extension that owns each icon. The merged view shows them together. If you uninstall Drawn, its icons and their history leave the merged view; the other collections keep theirs.

## Hover previews

Drawn previews only Drawn icon IDs, so hovering always shows one preview.

## With Auric Artisan Icon Studio

[Auric Artisan Icon Studio](../../auric-artisan-icon-studio/README.md) already contains the Drawn collection. By default it hosts Drawn, Modern and Playful, so their separate views, palette entries and shortcuts are hidden. Set `auricIconStudio.hostFamilyLibraries` to `false` to bring the Drawn view back. Icon Studio keeps its own likes and recents.

See [The merged Icon Studio](../../auric-icons-modern/docs/merged-icon-studio.md) in the Modern documentation for more detail.

## A file icon theme for Drawn

Drawn has no Explorer file icon theme. Install Auric Icons: Modern for the family's file and folder theme; both libraries still merge.

## Result

With several Auric collections installed, you see Drawn alongside them in one library and can filter to Drawn with the **Library** filter.
