---
title: Font Library — Reference
description: Every view, control, option, file and message in the Font Library in one place.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Font Library reference

## Address

https://auricartisan.com/tool/font/

## Catalogue

| Figure | Value |
| --- | --- |
| Families | 2,213 |
| Font files | 4,883 |
| Variable families | 550 |
| Families with italics | 401 |
| Served (Library) | 2,023 |
| Listed only (System, marked Installed) | 190 |
| Scripts and Unicode blocks | 60 |
| Licences | Open Font License 1,929; Unspecified 191; Apache 2.0 45; Creative Commons 40; MIT 7; Custom 1 |

## Views

| View | Contents |
| --- | --- |
| **Specimens** | Rail and grid; the count of matching families |
| **Collections** | Six curated rows |
| **Selected** | Your kit as cards; the count |

## Rail

| Control | Values | Default |
| --- | --- | --- |
| Search | Family name, designer or category | empty |
| Sort | Alphabetical, Accessibility score, UI score, Readability score, Most weights, Most glyphs, Variable first, Surprise me | Alphabetical |
| **Filters** | Shows or hides the chip groups | shown |
| **Recommend** | Opens Find your font | closed |
| Category | All, Serif, Sans Serif, Handwriting, Monospace, Display | All |
| **Filter these options** | Text | empty |
| Properties | ⚡ Variable, 𝘐 Italic, ⌗ Monospace | off |
| Weights available | 100, 200, 300, 400, 500, 600, 700, 800, 900 | off |
| Features | Ligatures, Small Caps, Oldstyle Figures, Tabular Figures, Fractions, Slashed Zero, Stylistic Sets, Swashes | off |
| Scripts | The 18 most common | off |
| Licence | Six licence types | off |
| Source | Library, System | off |
| **Reset all filters** | Clears chips, category and search | button |
| **Download selected** | Downloads your kit | shown when the kit has families |

## Stage

| Control | Values | Default |
| --- | --- | --- |
| Preview text | Any text | the family name |
| **Shuffle** | Random order | button |
| **Grid**, **List** | Layout | Grid |
| **Size** | 12 to 120 px, − and + in 2 px steps, **Reset to 40**; cards use 22 to 48 px | 40 |

## Family panel

| Item | Values |
| --- | --- |
| Width (wide screens) | 380 to 720 px, 460 at first, remembered |
| Height (narrow screens) | 62% at rest, 94% open |
| Header buttons | **＋ Select** / **✓ Selected**, **Download kit** / **Installed only**, **✕** |
| Tabs | Specimen, Suitability, Pairings, Glyphs, Features, Styles, About, License, Charset, Develop, Use & Embed |

## Specimen tab

| Control | Values | Default |
| --- | --- | --- |
| Size | 8 to 400 px | 64 |
| Line height | 0.6 to 3 | 1.2 |
| Letter spacing | −10 to 40 px | 0 |
| Weight | The family's weights | 400, or the nearest available |
| Text colour | Any colour | dark ink |
| Presets | Pangram, Paragraph, Alphabet, Uppercase, Numbers, Symbols, Code | the preview text |

## Scores

| Score | Range |
| --- | --- |
| Accessibility, Readability, UI / Product, Developer / Code, Editorial | 0 to 100 |
| Style fingerprint: Modern, Classic, Elegant, Playful, Technical, Friendly, Bold, Minimal | 0 to 100 |
| Pairing score | 60 to 99 |
| Recommender match | 40 to 99 |

## Develop tab

| Item | Values |
| --- | --- |
| Exports | CSS variables, Tailwind, SCSS, Design tokens, CSS @import |
| Type scale steps | xs, sm, base, md, lg, xl, 2xl, 3xl, 4xl |
| Base | 10 to 24 px, 16 at first |
| Ratio | 1.125, 1.200, 1.250, 1.333, 1.414, 1.500, 1.618; 1.200 at first |

## Use & Embed tab

Link, Import, Script, JS, @font-face, Usage.

## Recommender

| Control | Values | Default |
| --- | --- | --- |
| Industry | Any / not sure and 13 industries | Any |
| Brand style | Modern, Classic, Elegant, Playful, Bold, Minimal, Technical, Friendly | none |
| Accessibility priority | Essential, Balanced, Any | Balanced |
| Colour palette | HEX colours | empty |
| Results | 12 cards | always 12 |

## Files

| File | From |
| --- | --- |
| *Family-name*-font-kit.zip | **Download kit**, or a kit of one family |
| auric-font-selection-kit.zip | **Download** or **Download selected** with several families |
| Single font file | **Download** in the Styles tab's file table |

## Messages

| Message | Meaning |
| --- | --- |
| **No fonts match these filters.** | Nothing fits the search and filters. |
| **No option matches that.** | No filter chip matches the text in Filter these options. |
| **Copied** … | Code, a stack, a glyph or a feature was copied. |
| **Added both to selection** | ＋ Select both worked. |
| **Select some families first** | Embed or Download with an empty kit. |
| **Select at least 2 families to compare** | Compare needs two. |
| **Preparing download kit...** | A ZIP is being built. |
| **Downloaded** … | The ZIP is ready. |
| **Only bundled library fonts can be downloaded** | Every family asked for is Installed only. |
| **Could not prepare this download** | The family's details could not be loaded. |
| **Font library is temporarily unavailable** | The catalogue could not be reached. |
| **The live font engine didn’t load** | The page's font engine did not start; **Retry** reloads. |

## Related

- [Shortcuts](../others/shortcuts.md)
- [Glossary](../others/glossary.md)
- [Browse, search and filter](browse-and-filter.md)
