---
title: Collections — Reference
description: Every control, filter, sort order and menu item on the Collections page, and the full catalogue of 30 tools.
product: Website › Library › Collections
updated: 2026-09-25
---

# Collections reference

This page lists every control on https://auricartisan.com/collections/ and every tool in the catalogue. For step-by-step help, see the task guides in this folder.

## Page sections

| Section | What it contains |
| --- | --- |
| Hero | The page heading, three counters (**Tools**, **Categories**, **Topics**) and three quick links (**Tools**, **Learn**, **Pricing**). |
| **Start here** | A slider of three featured tools, with previous and next buttons, dots and a slide counter. |
| **All tools** | The full catalogue with the **Filter and sort** panel, search box, view switch and cards. |
| **Featured Highlights** | Two short notes: **Accessibility & Analysis** and **Creative Generation**. |
| Plans | "Every tool here is free. Upgrade for superpowers." The four plans with billing and currency switches. |
| **Explore All Collections** | Closing banner with **Browse All Collections** and **See full pricing & FAQ**. |

## Hero counters

| Counter | What it counts |
| --- | --- |
| **Tools** | Tools the catalogue is showing under your tool-visibility setting. |
| **Categories** | Different categories among those tools. |
| **Topics** | Different topic tags among those tools. |

## Start here slider

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| Previous button | Shows the previous featured tool. | — | — |
| Next button | Shows the next featured tool. | — | — |
| Dots | Jump to a featured tool. Each dot's label is "Show" and the tool's name. | One dot per tool | — |
| Slide counter | Shows the current slide and the total. | `01 / 03` style | — |
| Progress bar | Fills while the current slide is shown, then the slider moves on. | — | 7 seconds per slide |
| `Left` / `Right` arrow keys | Previous or next slide, while the slider has focus. | — | — |
| Autoplay pause | Autoplay pauses while the pointer is over the slider or it has focus. | — | — |
| Reduced motion | With your system's reduced-motion setting on, the slider does not move by itself. | — | — |

The shortlist holds three tools. Pinned tools come first; the rest follow in catalogue order.

## Filter and sort panel

The panel is headed **Filter and sort** and has three sections you can open or close.

| Section | Control | What it does | Default |
| --- | --- | --- | --- |
| **Sort by** | **Sort** list | Chooses the order of the grid. See the sort table below. | — |
| **Category** | Tick boxes with counts | Shows only tools in the ticked categories. None ticked means all. | Open, none ticked |
| **Topics** | Tick boxes with counts | Shows only tools with any ticked topic. Up to 14 of the most common topics are listed. | Closed, none ticked |

A **Pinned** tick box appears first under **Category** once you have pinned at least one tool.

### Categories

| Category | Tools in it |
| --- | --- |
| Accessibility | 2 |
| Color Science | 1 |
| Colorimetry | 3 |
| Design Systems | 1 |
| Gamut & Rendering | 4 |
| Generators | 5 |
| Iconography | 1 |
| Perception | 3 |
| Publish | 1 |
| Spectral | 2 |
| Typography | 1 |
| Utilities | 6 |

The counts above are for the full catalogue (**Everything**). The page shows counts for the tools currently in view.

### Sort orders

| Option | Card-menu button | Order |
| --- | --- | --- |
| **Title A to Z** | **Title** | Alphabetical by tool name. First in the list, and the order **Reset** returns to. |
| **Category A to Z** | **Category** | Alphabetical by category. |
| **Newest first** | **Newest** | By date, newest first. Tools have no dates, so this keeps catalogue order. |
| **Oldest first** | **Oldest** | By date, oldest first. Tools have no dates, so this keeps catalogue order. |
| **Recommended** | **Recommended** | By a score built from your pins, your opens, core subjects and description depth. |
| **Most used** | **Most** | By how often and how recently you opened each tool from this page. |
| **Pinned first** | **Pinned** | Pinned tools first, then the rest. |
| **Most metadata** | **Most metadata** | Tools with the fullest descriptions and most tags first. |

When the page first opens, the grid is in catalogue order (the order of the tool catalogue below), even though the **Sort** list shows **Title A to Z**. Choose any order to apply it.

## Results bar

| Control | What it does | Default |
| --- | --- | --- |
| **Search tools...** | Filters as you type. Every word must match the tool's name, description, category, address or tags. Case does not matter; part-words match. | Empty |
| **Grid** | Shows cards side by side. | On |
| **List** | Shows one tool per row. | Off |
| Result count | Shows `N tools`, or `N of M tools` while filtering. | — |

## Cards

| Part | What it shows or does |
| --- | --- |
| Artwork | An illustration for the tool. |
| Category line | The tool's category, above its name. |
| Name and description | The tool's name and one-sentence summary. |
| **Free to use** | Shown on every card: every tool is free on every plan. |
| Pin button | Pins or unpins the tool. Its label reads "Pin" or "Unpin" followed by the tool's name. |
| Tooltip | On hover: **Category**, **Mode** (Basic, Advanced or Both), **Route** (the tool's address) and topic tags. |
| Selecting the card | Opens the tool and counts one open towards **Most used**. |

## Loading

| Behaviour | Detail |
| --- | --- |
| First view | 12 tools. |
| Scrolling to the end of the grid | Loads the next 12 automatically. |
| Status line | `Showing 12 of 14 tools`, then `All 14 tools shown` (numbers vary). |
| Fallback button | **Load N more tools**, shown only if automatic loading is unavailable. |
| No results | **No matching tools** — "Try a shorter search, clear the topic chip, or switch the category back to all tools." |
| Load failure | The count reads **Unable to load** and the grid shows "Unable to load tools." |

## Floating search button

Appears on the right-hand side of the screen once the main controls have scrolled out of view. Its label is "Search and sort tools".

| Control | What it does |
| --- | --- |
| **Search tools...** | Same search as the main box; the two stay in step. |
| **Sort** | Same list as the main **Sort** list. |
| **Category** | Same tick boxes as the main panel (open by default). |
| **Topics** | Same tick boxes as the main panel (closed by default). |
| `Escape` or selecting outside | Closes the panel. |

## Card menu (right-click)

Right-click a card, or focus it and press the context-menu key or `Shift` + `F10`.

| Group | Control | What it does | Values | Default |
| --- | --- | --- | --- | --- |
| Header | Title | Shows the card's title, with a pin mark if pinned. | — | — |
| **Card** | **Pin** / **Unpin** | Pins or unpins the tool. | — | — |
| **Card** | **Open** | Opens the tool in this tab. | — | — |
| **Card** | **New tab** | Opens the tool in a new tab. | — | — |
| **Card** | **Copy link** | Copies the tool's full address. | — | — |
| **View** | **Grid** / **List** | Switches the layout. | Grid, List | Grid |
| **Density** | **Cozy** / **Compact** | Changes the space between cards. | Cozy, Compact | Cozy |
| **Columns** | **Auto** / **2** / **3** / **4** | Sets the number of columns in grid view. | Auto, 2, 3, 4 | Auto |
| **Sort** | Sort buttons | Chooses the sort order. | See the sort table | — |
| **System** | **Theme** | Switches the site theme; highlighted while dark. | On, Off | — |
| **System** | **Reading** | Turns reading mode on or off. | On, Off | — |
| Footer | **Reset** | Grid view, Cozy, Auto columns, first sort order. Pins and usage are kept. | — | — |
| Footer | **All settings →** | Opens the site settings panel. | — | — |

## Plans section

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| Billing switch | Shows monthly or annual prices. The **Save 22%** badge sits beside it. | **Monthly**, **Annual** | Monthly |
| Currency buttons | Shows prices in US dollars or Indian rupees. The page picks one for your region on your first visit; your own choice is remembered. | **USD $**, **INR ₹** | Set by region |

The plans are **Apprentice**, **Artisan**, **Specialist** and **Industrial Pro**. The section lists "No credit card to start", "Every tool free on every plan" and "Cancel anytime · 7-day money-back". For plan details, see [Account and billing](../../../account-and-billing/README.md).

## What is remembered

| Item | Where | Scope |
| --- | --- | --- |
| Pinned tools | This browser | The Collections catalogue |
| Opens (for **Most used** and **Recommended**) | This browser | The Collections catalogue |
| Grid or list view | This browser | The Collections page |
| Density and columns | This browser | The Collections page |
| Tool-visibility setting | This browser | The whole site |

## Tool catalogue

All 30 tools, in catalogue order.

| Tool | Category | Mode | Address | What it does |
| --- | --- | --- | --- | --- |
| Analyze URLs | Accessibility | Both | /tool/analyzer/ | Accessibility audit, contrast checking, colour vision simulation, palette extraction and reports. |
| Vision Simulation | Accessibility | Advanced | /tool/vision-simulation/ | Simulates colour vision deficiencies, cone isolation and ocular conditions. |
| Design System Generator | Design Systems | Basic | /tool/design-engine/ | OKLCH colour ramps, font pairing, icons, spacing and motion scales, with token exports. |
| Color Science Lab | Color Science | Advanced | /tool/color-science-lab/ | Chromatic adaptation, appearance models, spectral analysis and perceptual spaces. |
| Basic Tools | Generators | Basic | /tool/basic-tools/ | Palettes, gradients, conversions and quick colour utilities. |
| Personalization Generator | Generators | Basic | /tool/personalization-gen/ | Preference-based palettes, gradients, typography, UI pairs and posters. |
| Image Picker | Utilities | Basic | /tool/general/tools/image-picker/ | Samples images and extracts palettes. |
| Font Library | Typography | Basic | /tool/font/ | Browse, preview, download and embed self-hosted fonts. |
| Icon Library | Iconography | Basic | /tool/icon/ | Browse, recolour and self-host about 12,900 open-source icons. |
| Generate ASCII Art | Generators | Basic | /tool/ascii/ | Turns images, webcam captures and text into ASCII art. |
| Generate Ishihara Plates | Generators | Basic | /tool/ishihara-plate-generation/ | Generates Ishihara-style colour vision test plates. |
| Illuminants | Colorimetry | Advanced | /tool/general/colorimetry/illuminants/ | Reference spectra for standard illuminants. |
| Chromatic Adaptation | Colorimetry | Advanced | /tool/general/colorimetry/chromatic-adaptation-dynamic/ | Adaptation transforms and viewing-condition demos. |
| Gamut Mapping | Colorimetry | Advanced | /tool/general/colorimetry/gamut-map/ | Maps colours between gamuts while preserving appearance. |
| Gamut Explorer | Gamut & Rendering | Advanced | /tool/general/gamut-and-rendering/gamut/ | Inspects gamuts in chromaticity and 3D views. |
| HDR Gamut Plot | Gamut & Rendering | Advanced | /tool/general/gamut-and-rendering/hdr-gamut-plot/ | Plots HDR gamuts and exposure effects. |
| Tonal Steps, Tints & Shades | Gamut & Rendering | Advanced | /tool/general/gamut-and-rendering/tonal-steps-tints-shades/ | Builds tonal step-charts. |
| Tone Mapping | Gamut & Rendering | Advanced | /tool/general/gamut-and-rendering/tone-mapping/ | Tone mapping operators for HDR to LDR rendering. |
| Perception & Vision | Perception | Advanced | /tool/general/perception-and-neuroscience/perception-vision/ | Visual phenomena, illusions and appearance models. |
| Neuroscience | Perception | Advanced | /tool/general/perception-and-neuroscience/neuroscience/ | Visual cortex and neural colour processing. |
| Psychophysics Engine | Perception | Advanced | /tool/general/perception-and-neuroscience/psychophysical-experiment-engine/ | Sets up, runs and analyses psychophysical experiments. |
| Material Lighting | Spectral | Advanced | /tool/general/spectral-tools/material-lighting/ | Material reflectance under different illuminants. |
| Industrial Dye Chemistry | Spectral | Advanced | /tool/general/spectral-tools/industrial-dye-chemistry/ | Dye mixture and spectral prediction tools. |
| LUT Lab | Utilities | Advanced | /tool/general/tools/lut-lab/ | Creates and previews lookup tables. |
| ICC Parser | Utilities | Advanced | /tool/general/tools/icc-profile-parser/ | Inspects ICC profiles. |
| Collage Maker | Utilities | Basic | /tool/general/tools/collage-maker/ | Composes image collages and applies palettes. |
| M-Gradient Palette | Generators | Basic | /tool/general/tools/m-gradient-palette/ | Multigradient palette generator and presets. |
| SVG Recolor | Utilities | Basic | /tool/general/tools/svg-recolor/ | Recolours and batch-updates SVG files. |
| Convert & Export | Utilities | Basic | /tool/general/tools/ | Small converters and helper utilities. |
| Portfolio Builder | Publish | Both | /portfolio/ | Builds and publishes a public portfolio page. |

All addresses are on https://auricartisan.com.
