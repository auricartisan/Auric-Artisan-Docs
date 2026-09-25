---
title: Settings panel — Change the appearance
description: Recolour the site with an accent, keep saved colours, and choose the theme, language and text size.
product: Website › Site features › Settings panel
updated: 2026-09-25
---

# Change the appearance

The **Appearance** section controls the site's accent colour, theme, language and text size. It opens first whenever you open the panel.

The **accent** is the site's highlight colour: the gold of links, active tabs, buttons, focus rings, kit launchers and tooltip borders. Changing it recolours all of those at once.

## Read the preview and the contrast readout

At the top of the section are two live readouts.

- **Preview** (live appearance) shows a heading, an **Accent** chip, **A link**, a sample sentence and a **Primary button** drawn in your current accent, theme and text size.
- **Accent accessibility** (live WCAG contrast) shows two rows:
  - **Accent on background** — the contrast between your accent and the page background of the current theme.
  - **Text on accent** — the contrast between the accent and the text colour the site places on it. The site picks a dark or a light text colour automatically, whichever reads better.

Each row shows a ratio such as `4.87:1` and a badge. **Contrast ratio** is the WCAG measure of how far apart two colours are in lightness, from 1:1 (identical) to 21:1 (black on white).

| Badge | Ratio | Meaning |
|---|---|---|
| **AAA** | 7:1 or more | Meets the strictest WCAG level for body text |
| **AA** | 4.5:1 or more | Meets the standard WCAG level for body text |
| **AA Large** | 3:1 or more | Meets WCAG only for large text and interface parts |
| **Fail** | below 3:1 | Too little contrast for text |

Below the rows is a strip of seven **shades** of your accent, from darker to lighter. Select any shade to use it as your accent.

## Choose a preset accent

1. Open the panel (`Ctrl` + `,`). **Appearance** is selected.
2. Under **Accent color** (gold + 12 premium tones), select a swatch. Hover a swatch to see its name.

The page recolours at once. The presets are:

| Swatch | Hex |
|---|---|
| Gold (default) | `#D3AF37` |
| Champagne | `#DEC68A` |
| Rose Gold | `#B76E79` |
| Silver | `#C4C7CE` |
| Platinum Grey | `#8A8F99` |
| Bronze | `#B08D57` |
| Copper | `#B87333` |
| Brown | `#8B5A2B` |
| Maroon | `#800020` |
| Pink | `#E75480` |
| Emerald | `#3EA882` |
| Sapphire | `#2F5EAA` |
| Amethyst | `#9966CC` |

> **Note:** In the light theme, the default Gold accent is drawn as a slightly darker gold so that it stays readable on a light page. A colour you choose yourself, including Gold picked from a saved colour, is used exactly as chosen.

## Use any colour you like

1. Under **Custom color** (any color you like), select the round colour chip. Your browser's colour picker opens.
2. Choose a colour. While you drag, the panel previews the colour; when you let go, the whole site takes it.
3. The hex value appears next to the chip, for example `#2E8B57`.

If your browser supports it, an **Eyedropper** button appears next to the chip. Select it, then click any pixel on your screen to make that colour your accent. Press `Esc` to cancel. Browsers without an eyedropper do not show the button.

You can also select any shade in the **Accent accessibility** shade strip to use it as a custom accent.

## Keep colours in Saved colors

**Saved colors** is a palette of accents you want to come back to. Nothing is added to it unless you ask.

1. Set a custom colour as above.
2. Select the **+** button (**Save this color**) next to the hex value.
3. The colour appears at the front of **Saved colors**, and the hint reads, for example, "3 of 18 kept".

To use a saved colour, select its swatch. To remove one, select the small X on its corner.

- The palette holds up to **18** colours. When it is full, the **+** button is disabled; remove a colour first.
- The **+** shows as done (**Already saved**) when the current colour is already in the palette.
- **Restore section defaults** and **Reset all** keep your saved colours. Only the X removes them.

## Choose a theme

Under **Theme**, select **Light**, **Dark** or **System**. **System** follows your device's light or dark setting and changes with it. The full story, including the header button and shortcuts, is in [Theme](../../theme/README.md).

## Choose a language

Under **Language** (भाषा — interface and articles), select **English** or **हिन्दी**. Choosing Hindi translates the page in place; choosing English reloads the page in English. See [Language](../../language/README.md) for what is translated.

## Change the text size

Under **Text size** (scales type across the site), select one of the four **A** buttons, from smallest to largest:

| Button | Size |
|---|---|
| **Small** | 90% of the default |
| **Default** | 100% |
| **Large** | 112% |
| **X-Large** | 125% |

You can also use the keyboard anywhere on the site (not while typing in a field):

- `Alt` + `+` makes text larger by one step.
- `Alt` + `-` makes text smaller by one step.
- `Alt` + `0` returns to the default size.

A short message such as "Text size: Large" confirms each change.

## Restore the section

Select **Restore section defaults** at the bottom of Appearance to return the accent, theme and text size to their defaults (Gold, System, Default). Your language and your saved colours are not changed. A message confirms "Appearance restored to defaults".
