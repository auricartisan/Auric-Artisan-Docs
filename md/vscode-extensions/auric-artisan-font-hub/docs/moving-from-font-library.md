---
title: Auric Artisan Font Hub — moving from Font Library
description: Replace the earlier Auric Artisan Font Library extension with Font Hub without duplicate commands, and know what carries over.
product: VS Code extensions › Auric Artisan Font Hub
updated: 2026-09-25
---

# Moving from Font Library

Font Hub 0.1.0 is the renamed and redesigned successor of an earlier extension called **Font Library**. Font Hub has a new extension ID, `auric-artisan.auric-artisan-font-hub`, so VS Code treats them as two different extensions.

## Switch over

1. Open the Extensions view (`Ctrl` + `Shift` + `X`) and find **Font Library**.
2. Select **Disable** or **Uninstall**.
3. Install Font Hub: search for `@id:auric-artisan.auric-artisan-font-hub` and select **Install**.
4. Reload the window if VS Code asks.

If both are enabled at the same time, you see duplicate commands and views.

## What carries over

| Item | Carries over? |
| --- | --- |
| Settings (`auricFontLib.*`) | Yes. Font Hub uses the same setting names |
| Command IDs (`auricFontLib.*`) | Yes, so your custom keyboard shortcuts keep working |
| Favourites, recents and selection | No. They were stored with the old extension |
| Cached previews and font files | No. Font Hub builds its own cache |

After switching, the Activity Bar shows **Auric Font Hub** and the Command Palette lists commands under **Auric Artisan Font Hub**.
