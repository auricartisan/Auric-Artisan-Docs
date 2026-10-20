---
title: Auric Artisan File Icons — Customise the Explorer
description: Set file and folder colours, saturation, brightness, opacity, Explorer arrows and the Modern framework pack.
product: VS Code extensions › Auric Artisan File Icons
updated: 2026-09-25
---

# Customise the Explorer

Appearance settings recolour the Explorer artwork while keeping each icon's faceted light and dark structure. They apply to Facet, Playful and Modern together. They do not change the artwork you insert into code.

## Use the Appearance tab

1. Open File Icon Studio and select **Appearance**.
2. Set any of these:

| Control | What it does | Range |
| --- | --- | --- |
| **File color** | Recolours every file icon. Use the swatch, type a hex value, or **Reset** to `default`. | `default`, `#rgb` or `#rrggbb` |
| **Folder color** | Recolours every folder pair. | `default`, `#rgb` or `#rrggbb` |
| **Saturation** | Colour intensity. 0 is greyscale. | 0 to 2, steps of 0.05 |
| **Brightness** | Overall lightness. | 0.5 to 1.5, steps of 0.05 |
| **Opacity** | Transparency. | 0.2 to 1, steps of 0.05 |
| **Hide Explorer arrows** | Hides the expand and collapse chevrons. | On or off |

3. Select **Apply appearance**.
4. If the artwork changed, VS Code shows "Auric file icons updated. Reload the window to apply every icon change." Select **Reload**. If nothing needed rebuilding, it says "No theme reload is needed."

**Restore defaults…** runs **Restore Icon Defaults** (see below).

## Use the Configure menu

Run **Auric Artisan File Icons: Open File Icon Studio Settings**. A menu titled **Configure Auric Artisan File Icons** lists:

| Item | What it does |
| --- | --- |
| **File color** | Choose from presets or a custom hex colour. |
| **Folder color** | Same, for folders. |
| **Saturation** | Choose 0, 0.5, 0.75, 1, 1.25, 1.5 or 2. |
| **Brightness** | Choose 0.6, 0.75, 0.9, 1, 1.1, 1.25 or 1.4. |
| **Opacity** | Choose 0.4, 0.55, 0.7, 0.85 or 1. |
| **Explorer arrows** | Toggle between visible and hidden. |
| **Smart detection** | Opens the smart detection menu. |
| **Icon profiles** | Opens **Apply Icon Profile**. |
| **Scan workspace folders** | Runs the workspace folder scan. |
| **Diagnostics** | Shows diagnostics. |
| **Open all settings** | Opens Settings filtered to this extension. |
| **Restore defaults** | Runs **Restore Icon Defaults**. |

### Colour presets

**Auric Artisan File Icons: Choose Folder Color** (and the colour items above) offer: **Default gold** (`default`), **Amber** `#D8A33C`, **Ocean** `#4AA3DF`, **Mint** `#43BFA5`, **Violet** `#8D73D8`, **Rose** `#D56782`, **Slate** `#718096`, and **Custom hex color…** for any three- or six-digit value.

## Modern framework pack

On **Appearance**, choose **Modern framework pack**: **No framework pack**, **Angular**, **NestJS**, **React** or **Vue**. The setting is `auricFileIcons.modernPack`.

A pack changes Modern's automatic Explorer associations only. All framework artwork stays searchable in the Library whatever you choose.

## Toggle arrows quickly

Run **Auric Artisan File Icons: Toggle Explorer Arrows**.

## Restore defaults

Run **Auric Artisan File Icons: Restore Icon Defaults**, or select **Restore defaults…** on **Appearance**. After you confirm with **Restore**, it clears:

- the appearance settings (file and folder colour, saturation, brightness, opacity, arrows and Modern pack) in your user settings;
- the file, folder and root associations and the smart detection settings in the current workspace.

## Settings files

The Studio writes appearance settings for you. You can also set them in `settings.json`:

```json
{
  "auricFileIcons.folderColor": "#D8A33C",
  "auricFileIcons.fileColor": "default",
  "auricFileIcons.saturation": 1.15,
  "auricFileIcons.brightness": 1.05,
  "auricFileIcons.opacity": 0.9,
  "auricFileIcons.hidesExplorerArrows": false,
  "auricFileIcons.modernPack": "none"
}
```

Workspace or folder settings override user settings. If a change seems to have no effect, check for a workspace value.

## Result

After a reload, the Explorer shows your colours and settings in whichever Auric style is active.
