---
title: Design System Generator — Read the system
description: What the Overview, Colour, Type, Icons and Scales tabs show, and how to copy any value from them.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Read the system

The first five tabs show the generated system from different angles. Every tab is made of cards; select a card's heading to fold or unfold it. Some cards start folded. Almost every colour, gradient and token can be selected to copy its value, and a short message confirms the copy.

## Overview

Four cards:

- **System summary**: a score ring (green at 85 and above, amber from 65, red below), the industry and style, the mood and target, the harmony, and badges for the seed, **All pairings pass** or **N to review**, the font pairing and the icon family. Under it, eight headline swatches: primary, secondary, accent, success, warning, danger, info and text. The primary swatch also shows its contrast against white.
- **At a glance**: **Color ramps** (4 × 11), **Type sizes**, **Base size**, **Scale ratio**, **Spacing unit**, **Radius**, **Shadows** (6 levels) and **Total tokens**.
- **Generation recipe**: every input written out, including the resolved primary hue and the secondary and accent hue angles, the colour mode, the font pairing and the icon family with its stroke width. Use it to explain how a system was made.
- **Jump to**: shortcuts to **Color**, **Type**, **Components** and **Export**.

## Colour

- **Color ramps**: primary, secondary and accent at eleven steps (50, 100, 200 … 900, 950), and a neutral ramp at thirteen steps (0, 50, 100 … 950, 1000). The card's note lists the three hues. Steps sit on even perceptual lightness in OKLCH, with chroma highest in the middle steps and lower at the ends. Neutral step 0 is pure white; the other neutral steps carry a trace of the brand hue.
- **Semantic colors**: success, warning, danger and info at fixed hues (green, amber, red and blue), each shown as a solid with a label and four small chips for the background wash, border, text and solid colours. Select a chip to copy it.
- **Surfaces & roles**: **Light surfaces & roles** and, unless the colour mode is Light, **Dark surfaces & roles**. These are the tokens you build with: `bg`, `bg-subtle`, `bg-muted`, `surface`, `elevated`, `border`, `border-strong`, `text`, `text-muted`, `text-subtle`, `primary`, `primary-hover`, `primary-active`, `primary-subtle`, `on-primary` and `ring`.
- **Gradients** (folded): five gradients named **brand**, **brand-soft**, **sunrise**, **mesh** and **subtle**. Select one to copy its CSS.

How roles are chosen:

- Light text tiers are the lightest neutral steps that still meet their requirement: your target for `text`, 4.5:1 for `text-muted` and 3:1 for `text-subtle`. This gives three visibly different tiers rather than three near-blacks.
- The primary fill is the first of steps 600, 700, 500, 800, 400, 900, 300, 950 and 200 that reaches 3:1 against the background and takes a black or white label at your target (at least 4.5:1).
- The dark set is built on neutral step 950, a tinted near-black. Its text colour is chosen against the lightest dark surface, so it passes on cards as well as on the page. Dark borders are translucent white.

Colours that would fall outside sRGB have their chroma reduced until they fit, so a very vivid seed can come back calmer: what you see is what a screen can show.

## Type

- **Font pairing**: specimens of the heading, body and mono families, the pairing's note, *Served from fonts.auricartisan.com*, and **Browse in Font Library ↗**, which opens the Font Library searching for the heading family.
- **Type scale**: thirteen sizes named `2xs`, `xs`, `sm`, `base`, `md`, `lg`, `xl`, `2xl`, `3xl`, `4xl`, `5xl`, `6xl` and `7xl`, largest first, each with pixels, rem and a specimen. The note shows the ratio and base size.
- **Roles**: twelve text styles (**display**, **h1** to **h5**, **body-lg**, **body**, **small**, **caption**, **overline** and **code**), each drawn at its size, weight, line height and letter spacing, with the family it uses.
- **Available weights** (folded): the weights of the heading family.

The pairing is chosen from sixteen curated pairings by how many tags it shares with your industry and style. The families include Inter, Space Grotesk, Sora, Manrope, Plus Jakarta Sans, Outfit, DM Serif Display, Fraunces, Playfair Display with Source Sans 3, Cormorant Garamond with Jost, Bricolage Grotesque, Lexend, Epilogue, Archivo Expanded with Archivo, Spline Sans, and IBM Plex Sans with IBM Plex Mono; the mono family is JetBrains Mono unless the pairing has its own.

Each size also has its own line height, tighter for large sizes; the Tailwind v3 export carries it with each font size.

## Icons

- **Recommended icon family**: **Recommended set**, **Why**, **Stroke width**, **Grid size** (24 px), **Corner join**, **Suggested sizes** (16 · 20 · 24 · 32 px), **Source** (icons.auricartisan.com) and a button to browse the set in the Icon Library.
- **Preview set**: twenty common icons at the recommended stroke.
- **On brand color** (folded): eight icons in the primary colour.
- **Size ramp** (folded): one icon at 16, 20, 24, 32 and 40 pixels.

The family is one of seven: **Feather**, **Lucide**, **Heroicons**, **Phosphor**, **Tabler**, **Remix Icon** and **Material Symbols**, chosen by tag overlap. The stroke is made slightly thinner for Minimal and Elegant and slightly thicker for Bold and Brutalist. When the Auric icon CDN is reachable, the previews show the real family; otherwise they show built-in line icons of the same weight.

## Scales

Four columns in one tab:

- **Spacing scale**: nineteen steps (`0`, `px`, `0.5`, `1`, `1.5`, `2`, `2.5`, `3`, `4`, `5`, `6`, `8`, `10`, `12`, `16`, `20`, `24`, `32`, `40`), each drawn as a bar. `0` is 0 px and `px` is 1 px; every other step is its number × the base unit × the density multiplier.
- **Border radius scale**: `none`, `sm`, `md`, `lg`, `xl`, `2xl`, `3xl` and `pill`, each drawn as a box, with the corner style named.
- **Elevation / shadow scale**: six levels (`xs` to `2xl`) plus `primary` and `inner`, drawn on a surface, with the brand-tinted shadow colour. **Shadow values** (folded) lists the CSS for each. The **Hard** preset (Brutalist) gives offset shadows with no blur; the **Glow** preset (Futuristic) adds a brand-coloured glow to the two largest levels.
- **Durations** (fast, base, slow) and **Easing curves** (standard, spring, linear): hover a row to replay the movement.

Z-index (`base` 0, `dropdown` 1000, `sticky` 1100, `banner` 1200, `overlay` 1300, `modal` 1400, `popover` 1500, `toast` 1600, `tooltip` 1700) and breakpoints (`sm` 640, `md` 768, `lg` 1024, `xl` 1280, `2xl` 1536 px) have no tab; they are in the Tokens list and the exports.

## Copying values

- Select a ramp cell, swatch, gradient or token to copy its value. The item flashes and a message such as **Copied #1f6feb** appears.
- Changing any input rebuilds every tab, so folded or unfolded cards return to their starting state.

## Related

- [Set the brief](set-the-brief.md)
- [Export tokens](export-tokens.md)
- [Reference](reference.md)
