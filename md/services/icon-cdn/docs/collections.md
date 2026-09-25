---
title: Icon CDN — Collections
description: The seven icon sets on the Icon CDN — their styles, icon counts, grids, whether they are stroke-based, and their licences.
product: Services › Icon CDN
updated: 2026-09-25
---

# Collections

The CDN serves seven sets: 12,896 icons in 32,803 variants. An **icon** is one symbol, such as "heart"; a **variant** is one style of it, such as Phosphor's heart in bold or fill.

| Set | Icons | Variants | Styles | Default style | Licence |
|---|---|---|---|---|---|
| Lucide | 1,714 | 1,714 | `regular` | `regular` | ISC |
| Phosphor | 1,512 | 9,072 | `thin`, `light`, `regular`, `bold`, `fill`, `duotone` | `regular` | MIT |
| Tabler | 5,093 | 6,146 | `outline`, `filled` | `outline` | MIT |
| Remix | 1,690 | 3,229 | `line`, `fill` | `line` | Remix Icon License v1.0 |
| Heroicons | 324 | 1,288 | `24/outline`, `24/solid`, `20/solid`, `16/solid` | `24/outline` | MIT |
| Feather | 287 | 287 | `regular` | `regular` | MIT |
| Material | 2,276 | 11,067 | `outlined`, `round`, `sharp`, `regular`, `twotone` | `outlined` | Apache 2.0 |

## Grids and strokes

| Set | Grid (viewBox) | Drawn with |
|---|---|---|
| Lucide | 24 × 24 | Strokes |
| Phosphor | 256 × 256 | Fills |
| Tabler | 24 × 24 | Strokes |
| Remix | 24 × 24 | Fills |
| Heroicons | 24, 20 or 16, by style | Strokes (outline) and fills (solid) |
| Feather | 24 × 24 | Strokes |
| Material | Webfont | Glyphs of a font |

Stroke width (`data-stroke`) changes only icons drawn with strokes: Lucide, Tabler, Feather and Heroicons' outline style.

## Material is a webfont

Material icons are not SVG: the CDN serves them as five webfonts (Regular, Outlined, Round, Sharp and Two-Tone) with their code points. The loader renders a Material icon as a character in the matching font, so it behaves like text: its size follows `data-size` or the font size, and its colour follows `data-color` or the text colour.

## Remix categories

Remix icons are organised in twenty folders on the CDN, such as `Arrows`, `Buildings`, `Business`, `Communication`, `Design`, `Development`, `Device`, `Document`, `Editor`, `Finance`, `Food`, `Game & Sports`, `Health & Medical`, `Logos`, `Map`, `Media`, `Others`, `System`, `User & Faces` and `Weather`. Remix also ships its own webfont; see [Embed an icon](embed-an-icon.md#webfonts).

## Categories in the Icon Library

The Icon Library groups icons into categories such as Arrows, Brand, Design, Devices, Document, E-commerce, Map, Media, System and Weather, where the sets provide them. Many icons have no category.

## Upstream sources

| Set | Home | Credit |
|---|---|---|
| Lucide | https://lucide.dev | Lucide Contributors |
| Phosphor | https://phosphoricons.com | Phosphor Icons |
| Tabler | https://tabler.io/icons | Paweł Kuna |
| Remix | https://remixicon.com | Remix Design |
| Heroicons | https://heroicons.com | Tailwind Labs |
| Feather | https://feathericons.com | Cole Bemis |
| Material | https://fonts.google.com/icons | Google |

## Related pages

- [Licences](../others/licences.md)
- [Style, size and colour](style-size-and-colour.md)
