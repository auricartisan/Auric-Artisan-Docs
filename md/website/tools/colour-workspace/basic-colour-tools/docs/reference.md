---
title: Basic Color Tools — Reference
description: Every control, option, range, default and output of the Basic Color Tools page, its views and its seven panel tools, with pointers to the Colour Tools references.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Basic Color Tools reference

This page lists every control on the Basic Color Tools page. Defaults are given only where the page sets one. For the fourteen Colour Tools, each tool's guide ends with its own full controls table; see [Colour Tools](#colour-tools) at the end.

## Page

| Item | Value |
| --- | --- |
| Address | https://auricartisan.com/tool/basic-tools/ (also https://auricartisan.com/basic-tools) |
| Tools | 7, in 4 categories |
| Maximum open panels | 5 |
| Sign-in | Not needed to use the tools |
| Works offline | The tools compute everything in the browser once the page has loaded |

## View buttons

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Workspace** | Launcher, capacity meter and stage | — | Shown on first visit |
| **Catalogue** | Card grid with filters | — | — |
| **Panels** | List of open panels and a title-bar legend | — | — |
| Last view | Reopens on the view you used last | Stored in your browser | — |

## Workspace view

| Control | What it does |
| --- | --- |
| **Open a tool** rows | Open a tool, or bring its open panel forward (restoring it if docked). Rows show **Advanced** and **open** labels. |
| **Panels** meter | Shows **N of 5 open**, a bar, and **Room for N more.** or the ceiling message. |
| **Panels** entries | One per panel with **Floating**, **Docked** or **Maximised**. Select to bring it forward. |
| Stage | Holds the panels in this view. Shows **Nothing open yet.** when empty. |

## Catalogue view

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Basic Tools** link | Reloads the page | — | — |
| Search box | Filters cards by name, summary and tags; all words must match | Free text | Empty |
| **Clear** | Empties the search | — | — |
| Category list | Shows one category | All Tools, Generate, Pick, Compose, Convert, Favorites, Open Panels | All Tools (then remembered) |
| **Level** | Filters by depth | Basic, Advanced, Both | Both (then remembered) |
| Count | Visible cards out of the total | For example **7 of 7** | — |
| **Copy link** | Copies the page address | — | — |
| Quick start button | Shows or hides the quick start note | On or off | Off |
| Quick start **×** | Hides the note permanently | — | — |
| Tool card | Opens the tool or focuses its panel | — | — |
| `Shift`, `Ctrl` or `Cmd` + select a card | Opens another instance | — | — |
| Card star | Adds or removes a favourite | On or off | Off |
| Open Panels card | Restores and focuses a panel | — | — |

## Panels view

| Item | What it shows |
| --- | --- |
| **Open panels** | Each panel's name, category and state, and **N of 5** |
| **What the bar does** | Duplicate, Minimise, Maximise and Close explained |

## Panel window

| Control | What it does | Values or range |
| --- | --- | --- |
| Title bar drag | Moves the panel | Stays within the stage or window |
| Title bar double-click | Maximises or restores | — |
| **Open another instance** | Opens a copy with separate state | — |
| **Minimize** | Hides and docks the panel, keeping its work | — |
| **Maximize or restore** | Fills the stage or window, and back | — |
| **Close** | Closes the panel and discards its work | — |
| Resize handle | Resizes | Minimum 480 × 380 pixels, or the available space |
| `Escape` (focus inside a panel) | Restores a maximised panel; otherwise closes the panel | — |
| Select a panel | Brings it to the front (focus) | — |

## Palette Studio

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Harmony** | Generation mode; regenerates on change | Random, Analogous, Complementary, Triadic, Monochromatic, Split complementary, Tetradic, Compound, Shades, Tints, WCAG AA palette, WCAG AAA palette, Accessibility palette | Random |
| **Generate** | Replaces unlocked colours | — | — |
| `Space` | Generate (panel focused, not typing) | — | — |
| **+ Add** | Adds a random colour | Up to 9 colours | — |
| **From Image** | Extracts dominant colours from an image | As many colours as the palette has | — |
| **WCAG AA** / **WCAG AAA** / **Accessibility** | Switch mode and generate | — | — |
| **CVD Preview** | Simulates colour-vision deficiency on the strips | Normal vision, Deuteranopia, Protanopia, Tritanopia, Achromatopsia | Normal vision |
| Strip **Lock** | Keeps the colour on Generate | On or off | Off |
| Strip **Copy hex** | Copies the HEX code | — | — |
| Strip **Adjust** | OKLCH sliders with **Apply** and **Cancel** | L 0–1, C 0–0.4, H 0–360 | Current colour |
| Strip **Remove** | Removes the colour | At least 2 remain | — |
| Strip HEX label | Opens the site colour picker | — | — |
| Drag a strip | Reorders | — | — |
| Tabs | Palette, Contrast Matrix, WCAG Pairs, Curves, CVD Comparison, Color Info | — | Palette |
| **Share** | Copies a `#palette=` link | — | — |
| **CSS**, **SCSS**, **TW**, **JSON**, **ASE** | Copy | — | — |
| **SVG**, **PNG** | Download 1200 × 240 image | — | — |

## Palette Remix

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Seed colors** | Colours to remix; applied when you leave the box | HEX, rgb(), rgba(), hsl(), hsla(), hsv(), oklch() | #D3AF37, #1A1A2E, #F5DEB3, #0F172A, #FFFFFF |
| **Remix style** | Recipe family | Editorial kit, Analog drift, Complement battle, Tonal system | Editorial kit |
| **Colors per palette** | Colours per set | 3–9 | 5 |
| **Remix energy** | Random variation | 0–100 | 30 |
| **Remix** | Re-rolls variation | — | — |
| **New seed** | Random seeds | — | — |
| Card **Copy** / **Use as seed** | Copy one set / move it into the seeds | — | — |
| **CSS**, **JSON**, **All HEX** | Copy all sets | — | — |

## Gradient Maker

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Type** | Shape | Linear, Radial, Conic | Linear |
| **Angle** | Direction or start angle (hidden for Radial) | 0–360 | 90 |
| **Interpolation** | Blend space | sRGB (native CSS), OKLCh (perceptual), HSL, CIE Lab | sRGB (native CSS) |
| **Easing** | Blend pace | Linear, Ease in, Ease out, Ease in-out, Sine | Linear |
| **Reverse**, **+ Stop**, **Even**, **Random** | Edit stops | — | — |
| Track | Add a stop / highlight a marker | — | — |
| Stop row | Colour well, HEX box, position slider, **✕** | Position 0–100, step 0.5; at least 2 stops | #D3AF37 at 0, #1D2A3E at 100 |
| Tabs | Design, Curves, Presets, Export | — | Design |
| Presets | Sunset, Ocean, Aurora, Coral, Mint, Royal, Auric, Spectrum, Mono dark | — | — |
| **Copy CSS**, **JSON**, **Tailwind** | Copy | — | — |
| **SVG**, **1600px**, **4K** | Download | 800 × 400; 1600 × 800; 3840 × 1920 | — |

## Color Picker

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| Colour well, HEX box | Set the colour | HEX | — |
| **Pick** | System eyedropper | Needs browser support | — |
| **Random** | Random colour | — | — |
| Saturation-value plane | Saturation (x) and value (y) | 0–100 % | — |
| Hue slider | Hue | 0–360° | — |
| Tabs | Formats, Harmonies, CVD, Chromaticity, Info | — | Formats |
| Format copy buttons | HEX, RGB, HSL, HSV, OKLCH, Lab, XYZ, CMYK | — | — |
| Harmony rows | Complementary, Analogous, Triadic, Tetradic, Split-comp., Square, Shades (L ramp), Tints (C ramp) | Select a swatch to apply | — |
| Contrast tiles | White, Off-white, Black, Near-black, Dark slate, Auric gold | AAA, AA, Fail | — |

## Color Battle

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Team A**, **Team B** | Palettes to compare | Up to 9 colours each | Five colours each |
| Dice buttons | Random team of five | — | — |
| **Battle**, **Swap** | Score; exchange and score | — | Scores on opening |
| **Copy winner**, **Copy report** | Copy | — | — |
| Score weights | Avg contrast 35, AA pairs 30, Avg ΔE2000 20, CVD ΔE avg 15 | 0–100 total | — |

## Collage Maker

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Layout** | Arrangement | 29 layouts | Grid |
| **Cols**, **Rows** | Grid size for grid-based layouts | 1–6 each | 3, 2 |
| **Gap**, **Radius** | Spacing and rounding (px) | 0–40 each | 6, 8 |
| **Background** | Grid colour | Any | #101010 |
| **Border width / color** | Inner border | 0–20 px; any colour | 0; #FFFFFF |
| **Drop shadow** | Preview shadow | On or off | On |
| **Global filter** | Filter for all images | None, Grayscale, Sepia, Invert, Blur, Warm, Cool, Contrast, Vintage | None |
| **Title overlay** + colour | Title in the export | Text; any colour | Empty; #FFFFFF |
| **+ Add Images**, cell, shuffle, clear | Manage images | Image files | — |
| `Shift` + right-click a filled cell | Cycle that cell's filter | Filter list | — |
| **Export PNG (4K)** | Download `collage.png` | — | — |

## Quick Converter

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| Input box | Sets the colour | HEX, rgb(), rgba(), hsl(), hsla(), hsv(), oklch() | #D3AF37 |
| Colour well, dice | Set or randomise | — | — |
| **Convert** rows | HEX, RGB, RGB %, HSL, HSV, OKLCH, OKLab, Lab (D65), XYZ (D65), CIE xyY, CMYK, CSS oklch(), CSS oklab(), CSS lab() | Copy each | — |
| **Compare ΔE** | Color A and Color B with ΔE 76, ΔE 2000, WCAG ratio, ΔL, ΔC, ΔH, Same hue? | HEX | A #D3AF37, B #1F2A3E |
| **Wide Gamut** | Linear sRGB, Display P3, Rec.2020, Adobe RGB with In gamut or Out | — | — |
| **Visualize** | CIE 1931, hue wheel, shade strip, hue strip | — | — |
| **Quick Info** | Luminance, Nearest name | — | — |

## Save to Library

| Control | What it does |
| --- | --- |
| **Save to Library** (floating button) | Captures the focused panel and opens the save window |
| **Name**, **Description** | Per item |
| **Shared description**, **Collection**, **Tags (comma-separated)** | For all items being saved |
| **Save to Library** (in the window) or `Ctrl` + `Enter` | Saves |
| **Cancel** | Closes without saving |

## Colour Tools

The fourteen site-wide Colour Tools each have their own controls table at the end of their guide:

| Tool | Group | Guide |
| --- | --- | --- |
| Color Inspector | Essentials | [colour-inspector.md](colour-tools/colour-inspector.md) |
| Accessibility Lab | Essentials | [accessibility-lab.md](colour-tools/accessibility-lab.md) |
| Contrast System | Essentials | [contrast-system.md](colour-tools/contrast-system.md) |
| Color Name Finder | Essentials | [colour-name-finder.md](colour-tools/colour-name-finder.md) |
| Animation Contrast | Essentials | [animation-contrast.md](colour-tools/animation-contrast.md) |
| Type Readability Sim | Essentials | [type-readability-sim.md](colour-tools/type-readability-sim.md) |
| Color Library | Explore | [colour-library.md](colour-tools/colour-library.md) |
| Color Psychology | Explore | [colour-psychology.md](colour-tools/colour-psychology.md) |
| Pantone & Named Lookup | Explore | [pantone-and-named-lookup.md](colour-tools/pantone-and-named-lookup.md) |
| Harmony Studio | Design | [harmony-studio.md](colour-tools/harmony-studio.md) |
| Gradient Library | Design | [gradient-library.md](colour-tools/gradient-library.md) |
| CMYK Soft-Proof | Design | [cmyk-soft-proof.md](colour-tools/cmyk-soft-proof.md) |
| Color Formulation | Deep dive | [colour-formulation.md](colour-tools/colour-formulation.md) |
| Color Space Converter | Deep dive | [colour-space-converter.md](colour-tools/colour-space-converter.md) |

The launcher, the shared panel window and the `?color=` address parameters are covered in [launcher-and-panels.md](colour-tools/launcher-and-panels.md).

## Related

- [Basic Color Tools overview](../README.md)
- [Shortcuts](../others/shortcuts.md)
- [Glossary](../others/glossary.md)
