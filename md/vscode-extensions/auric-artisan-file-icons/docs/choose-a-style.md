---
title: Auric Artisan File Icons — Choose a style
description: Compare the Facet, Playful and Modern Explorer styles and switch between them.
product: VS Code extensions › Auric Artisan File Icons
updated: 2026-09-25
---

# Choose a style

File Icons contains three complete Explorer styles. Each is a separate VS Code file icon theme, and only one can be active at a time.

| Style | Theme name in VS Code | Artwork | What you get |
| --- | --- | --- | --- |
| Facet | Auric Artisan File Icons: Facet | 500 SVGs | Faceted artwork: 200 file designs and 150 closed and open folder pairs. |
| Playful | Auric Artisan File Icons: Playful | 500 SVGs | A distinct playful palette and artwork covering the same file and folder catalog as Facet. |
| Modern | Auric Artisan File Icons: Modern | 464 SVGs | 219 file designs, 114 closed and open folder pairs, light alternatives and state overlays. |

The totals include open-folder states, framework artwork and alternatives; they are not counts of unique file types.

Facet and Playful share the same mappings: 270 file extensions, 453 exact filenames, 84 language IDs and 357 folder aliases. Modern uses its own mappings and supports four framework packs (Angular, NestJS, React, Vue).

## Switch style

### From File Icon Studio

1. Open the **Library** tab.
2. Choose a style in **Artwork style**. This only previews the artwork.
3. Select **Use Facet in Explorer**, **Use Playful in Explorer** or **Use Modern in Explorer**.

### From the Command Palette

| Command | Result |
| --- | --- |
| **Auric Artisan File Icons: Activate Facet Icon Theme** | Facet becomes the file icon theme. VS Code confirms "Auric Artisan File Icons: Facet is active." |
| **Auric Artisan File Icons: Activate Playful Icon Theme** | Playful becomes the file icon theme. |
| **Auric Artisan File Icons: Activate Modern Icon Theme** | Modern becomes the file icon theme. |

### From VS Code

Run **Preferences: File Icon Theme** and choose one of the three **Auric Artisan File Icons** entries.

## What carries across styles

- Appearance settings (colours, saturation, brightness, opacity, arrows) apply to all three styles at once.
- Your associations and smart detection work with all three.
- The Explorer right-click actions (**Set File or Folder Icon** and others) are available whenever any of the three is active.
- The Modern framework pack only affects Modern.

## Live filename previews

While you type a new file or folder name in the Explorer, VS Code already shows the icon the active theme maps to that name, before you press `Enter`. This is VS Code's own theme rendering: no temporary file is created and no keystrokes are intercepted.

## Result

Your Explorer uses the style you picked, with your appearance settings applied.
