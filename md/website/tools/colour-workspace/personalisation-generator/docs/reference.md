---
title: Personalization Generator — Reference
description: Every control, setting, range, default and list in the Personalization Generator in one place.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Personalization Generator reference

## Address

- https://auricartisan.com/tool/personalization-gen/
- https://auricartisan.com/personalization opens the same page.

## The brief column

| Control | Type | Notes |
| --- | --- | --- |
| Brief box | text | Same setting as **Preference note** in Tune. `Enter` starts a sweep. |
| **Generate** | button | Starts a sweep. Reads **Generating…** while one runs. |
| **Stop** | button | Stops the running sweep and keeps what it found. Also ends **Endless**. |
| **Endless** | toggle | Keeps sweeping and merging results until stopped. Reads **Endless ✓** when on. |
| **Simple**, **Advanced** | switch | Advanced shows the search settings below. Default **Simple**. |
| **Depth** | number, 40 to 4,000 | Advanced only. Same as **Search depth**. |
| **Pool** | number, 5 to 240 | Advanced only. Same as **Pool target**. |
| **Size** | number, 5 to 12 | Advanced only. Same as **Palette size**. |
| **Keep** | number, 6 to 120 | Advanced only. Values above 96 act as 96. |
| **CVD-safe**, **Contrast**, **Unique** | check boxes | Advanced only. All on by default. |
| **This run** | summary | Depth, pool target, palette size, top kept and the filters. |

## Tabs

| Tab | Purpose |
| --- | --- |
| **Overview** | Summary tiles, the leader with its score breakdown, sweep diagnostics, recent palettes. |
| **Pool** | Add, remove, build, randomise and nudge pool colours; pool statistics; quick seeds. |
| **Tune** | Style chips, use case, preference note, engine settings, weights, filters. |
| **Palettes** | Kept palettes, ranked. |
| **Gradients** | One gradient per top palette, twelve styles. |
| **Typography** | Type systems paired with palettes. |
| **UI Pairs** | Background, text, surface and accent sets with contrast checks. |
| **Posters** | Poster layouts in the palettes' colours. |
| **Tokens** | Roles, themes, ramps, contrast audit and chart scales from the leader. |
| **Studio** | Sixteen mockups of one palette. |
| **Presets** | Seventeen starting points. |
| **Export** | CSS and JSON. |

## Pool

| Item | Value |
| --- | --- |
| Maximum pool | 240 colours |
| Starting pool | #D3AF37, #161616, #F8F7F1, #7D8A75, #2D6CDF, #C97B84, #0F172A, #14B8A6 |
| Accepted input | HEX with 3, 4, 6 or 8 digits, with or without `#` |
| **Build** | Fills or trims the pool to the pool target |
| **+24 random** | Adds 24 variations |
| **Jitter** | Nudges every colour by up to about 6° hue, 0.02 chroma and 0.03 lightness (OKLCH) |
| Quick seeds | **+ 4 UI**, **+ 4 Earthy**, **+ 4 Neon**, **+ 4 Pop**, **+ Grayscale** (7 greys) |

## Tune settings

| Setting | Range | Default |
| --- | --- | --- |
| Style chips | 18, at least one on | Calm, Editorial |
| **Use case** | Ui, Brand, Poster, Editorial, Dashboard | Ui |
| **Preference note** | text | empty |
| **Pool target** | 5 to 240 | 64 |
| **Palette size** | 5 to 12 | 6 |
| **Search depth** | 40 to 4,000, steps of 20 | 320 |
| **Keep top** | 6 to 96 | 24 |
| **Diversity** | 0 to 100 | 68 |
| **Accessibility** | 0 to 100 | 72 |
| **Warmth** | 0 to 100 | 52 |
| **CVD-safe penalty** | on or off | on |
| **UI contrast bonus (4.5:1)** | on or off | on |
| **Strict perceptual dedupe** | on or off | on |

**Reset defaults** restores the last ten rows. It leaves the pool, style chips, use case and note alone.

## Style chips

Calm, Luxe, Playful, Tech, Earthy, Editorial, Neon, Minimal, Heritage, Pastel, Cyber, Sun, Monochrome, Botanical, Nordic, Sunset, Midnight, Coastal.

## Colour relationships

Palettes are built on one of nineteen hue relationships: Analogous, Split complement, Triadic, Tetradic, Mono accent, Editorial pop, UI system, Poster clash, Natural, Aurora, Duo (warm/cool), Monochrome tonal, Complementary, Square, Hexadic, Nature spectrum, Sunset burn, Compound, Brand trio.

The **Ui** and **Dashboard** use cases favour UI system; **Poster** favours Poster clash; **Editorial** favours Editorial pop.

## Palette names

A mood word and the relationship, for example *Deep Triadic*:

| Mood | When |
| --- | --- |
| Vivid | average saturation above 70% |
| Deep | average lightness under 38% |
| Soft | average lightness above 72% |
| Balanced | anything else |

## Score parts

| Part | Base weight | Grows with |
| --- | --- | --- |
| Preference | 26% | fixed |
| Harmony | 20% | fixed |
| Style | 16% | fixed |
| Diversity | 11% | **Diversity**, up to a further 13% |
| Contrast | 10% | **Accessibility**, up to a further 10% |
| CVD / UI | 5% | **Accessibility**, up to a further 12% |

The total is scaled to 0 to 100 and capped at 100.

## Gradient styles

linear, radial, conic, mesh, layered, sharp, soft-mesh, diagonal, spot, duotone, prism, halo. Assigned in turn down the ranked palettes.

## Type systems

Product Grotesk, Editorial Serif, Quiet Humanist, Poster Condensed, Luxury Contrast, Data Mono, Pastel Round, Solar Slab, Modern Sans, Magazine Serif, Geometric Sans, Console Stack, Workshop Slab, Botanic Type, Nordic Sans, Vapor Display, Coast Casual.

## Poster layouts

bauhaus, type-dominant, asymmetric, magazine, minimal-centered, brutalist, festival, swiss, collage, kinetic, archive, gradient-poster. Assigned in turn down the ranked palettes.

## Studio

| Control | Options | Default |
| --- | --- | --- |
| Theme | Auto, Light, Dark | Auto |
| Density | Cozy, Compact | Cozy |
| **Test** | on or off | off |
| **Inspect** | on or off | off |
| Palette switcher | up to 24 palettes | the leader |

Mockups: Brand identity card, Product · Dashboard, Marketing · Landing, Component library, Type scale, Charts, Pricing, Auth · Sign in, Messages, Mobile · App, Calendar, Music · Player, Editorial · Magazine spread, Marketing banner, Transactional · Email, Commerce · Product card.

## Tokens

| Item | Value |
| --- | --- |
| Roles | primary, secondary, accent, neutral, success, warning, danger, info |
| Ramp steps | 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950 (88 tones in all) |
| Themes | light, dark, high contrast (14 values each) |
| Audit pairs | Body text, Muted text, Text on surface, Primary button, Accent on bg, Primary on bg |
| Chart scales | Categorical (8), Sequential (7), Diverging (9) |
| CSS prefix | `--aa-` |

## Result limits

| Result | Most |
| --- | --- |
| Palettes kept | 96 |
| Gradients, UI pairs, posters | 28 |
| Typography cards | 24 |
| Studio palette switcher | 24 |

## Messages

| Message | Meaning |
| --- | --- |
| **Idle.** | No sweep has run since the page opened. |
| **Generating (320)…** | A sweep of 320 candidates is running. |
| **Done · 24 kept · 812ms** | The sweep finished. |
| **Cancelled after 192/320 (140ms).** | The sweep was stopped; results so far are kept. |
| **Use a valid HEX color** | The HEX box could not be read. |
| **Pool is empty** | **Jitter** was selected with no pool colours. |
| **Defaults restored** | **Reset defaults** was selected. |
| **Nothing to save yet** | **Save brand system** was selected with no palettes. |
| **Already saved “…”** | That item from this sweep is already in your Library. |
| **Save failed** | The Library could not store the item. |

## Related

- [Tune the sweep](tune-the-sweep.md)
- [Glossary](../others/glossary.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
