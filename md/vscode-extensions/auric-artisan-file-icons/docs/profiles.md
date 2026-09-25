---
title: Auric Artisan File Icons — Profiles
description: Apply a built-in icon profile, save your own, and move profiles between machines as JSON.
product: VS Code extensions › Auric Artisan File Icons
updated: 2026-09-25
---

# Profiles

A **profile** is a named, portable set of appearance settings, associations and smart detection settings.

## Apply a profile

1. Run **Auric Artisan File Icons: Apply Icon Profile**, or **Apply profile…** on the **Workspace** tab.
2. Choose a profile. Built-in profiles are marked **Built-in**; your saved profiles follow.
3. Select **Reload** when asked.

| Built-in profile | Description | Key values |
| --- | --- | --- |
| Classic Facet | Balanced original colours and full smart decorations. | Default colours, 1 / 1 / 1, badge and colour |
| Vivid Studio | Brighter, richer colour for large project explorers. | Saturation 1.35, brightness 1.08 |
| Focused Explorer | Blue folders, softer files, hidden arrows and badge-only smart matches. | Files `#718096`, folders `#4AA3DF`, opacity 0.88 |
| Graphite Mono | Near-monochrome files and folders with semantic smart colours. | `#7B8796`, saturation 0.18, colour only |
| High Visibility | Maximum opacity, extra brightness and propagated badges. | Folders `#E0A82E`, saturation 1.2, brightness 1.18 |
| Minimal | Muted monochrome artwork with tooltip-only smart explanations. | `#8993A1`, saturation 0, opacity 0.72, arrows hidden |

Built-in profiles keep your custom associations and smart rules. Applying a saved or imported profile replaces them with the profile's own.

## Save your current set-up

1. Run **Save Current Icon Profile**, or **Save current…** on the Workspace tab.
2. Enter a name (up to 80 characters).
3. VS Code confirms "Saved icon profile "…"."

The Workspace tab's **Profiles** panel shows how many profiles are available and their names.

## Delete a saved profile

Run **Delete Saved Icon Profile** (or **Delete saved…**), choose the profile and confirm with **Delete**. Built-in profiles cannot be deleted.

## Export and import

- **Export Icon Profile to Clipboard** (or **Export**) copies your current settings as profile JSON. VS Code confirms "Current icon profile copied to the clipboard."
- **Import Icon Profile from Clipboard** (or **Import…**) reads profile JSON from the clipboard, then asks "Import "…"?" with **Apply** or **Apply and Save**.

Imports are checked first:

| Message | Meaning |
| --- | --- |
| The clipboard does not contain an icon profile. | The clipboard is empty. |
| The clipboard profile is larger than the 256 KiB safety limit. | Profiles must be under 256 KiB. |
| The clipboard does not contain valid JSON. | The text is not JSON. |
| Unsupported icon profile schema: … | The profile came from an unknown source. |
| Invalid icon profile: … | A value failed validation. |

Profiles exported from the older standalone Playful extension can be imported. Values are bounded and sanitised before they are written, and icon IDs that do not exist are dropped.

## Result

You can switch between complete Explorer looks in two steps and carry them to other machines.
