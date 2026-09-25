---
title: Auric Artisan Icon Studio — Work with the Auric collection extensions
description: How Icon Studio, Auric Icons: Modern, Drawn and Playful share one library interface, and how to keep their separate views if you prefer.
product: VS Code extensions › Auric Artisan Icon Studio
updated: 2026-09-25
---

# Work with the Auric collection extensions

The Auric artwork is also published as three separate extensions: **Auric Icons: Modern**, **Auric Icons: Drawn** and **Auric Icons: Playful**. Each has its own Icon Library view. Icon Studio already contains all three collections, so it is designed to avoid showing the same icons twice.

## Default: Icon Studio hosts the collections

With `auricIconStudio.hostFamilyLibraries` set to `true` (the default):

- The separate Icon Library views of Modern, Drawn and Playful are hidden, together with their Command Palette entries and their `Ctrl` + `Alt` + `I` and `Ctrl` + `Alt` + `R` shortcuts.
- Icon Studio's own view, commands and shortcuts are active.
- Modern's Explorer file icon theme is not affected. It keeps working.
- Hovering over an Auric icon ID is still answered by the collection extension that owns it, so you see one preview, not two.

## Keep the separate collection views

1. Open Settings and search for `auricIconStudio.hostFamilyLibraries`.
2. Turn it off (`false`).

The collection extensions show their own Icon Library views, commands and shortcuts again. Icon Studio's view and commands stay available, but its `Ctrl` + `Alt` + `I` and `Ctrl` + `Alt` + `R` shortcuts step aside so the shortcuts are not claimed twice. If none of the collection extensions are installed, Icon Studio's shortcuts stay active either way.

The change takes effect immediately. If Icon Studio is disabled or uninstalled, the collection views come back.

## When the collections are installed without Icon Studio

If two or three of Modern, Drawn and Playful are installed (and Icon Studio is not hosting them), they cooperate on their own: one of them automatically becomes the host and shows a single merged Icon Library. The others hide their views and forward their commands to it. See [Auric Icons: Modern](../../auric-icons-modern/docs/merged-icon-studio.md) for details.

## Likes and recent icons

- Icon Studio keeps its own likes, recent icons and learned recommendations.
- Each collection extension keeps its own likes and recents for its own icons.
- These are separate stores. Liking an icon in Icon Studio does not add it to the Modern extension's likes, and clearing one does not clear the other.

## Other Auric icon extensions

- **Auric Artisan Emoji** keeps its own Emoji Studio view and commands.
- **Auric Artisan Icon Hub** keeps its own view and settings.
- **Auric Artisan File Icons** remains the extension for Explorer file and folder themes. Installing Icon Studio does not replace it.

See the [comparison](../others/related.md) for which extension does what.

## Result

You see each Auric icon once, in the interface you prefer, and your shortcuts do not clash.
