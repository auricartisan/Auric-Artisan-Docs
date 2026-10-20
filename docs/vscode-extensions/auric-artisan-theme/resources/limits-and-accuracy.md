---
title: Auric Artisan Theme — Limits and accuracy
description: What the contrast audit measures, how precise it is, and what Auric Artisan Theme does not do.
product: VS Code extensions › Auric Artisan Theme
updated: 2026-09-25
---

# Limits and accuracy

## What the contrast audit measures

- The audit covers 81 defined foreground and background pairs per theme: editor text, 26 syntax roles, 14 text-bearing ANSI colours, source control decorations, and text and borders of common controls.
- Ratios use the WCAG 2 relative-luminance formula on sRGB colours. Transparent colours are composited onto the surface they sit on before measuring.
- APCA Lc values are shown for guidance. APCA is part of draft WCAG 3 work and is not yet a conformance requirement.
- Each pair has its own minimum. Text is held to your **Minimum contrast** setting; control borders are held to 3:1; decorative washes are held to less than text.

## What the audit does not tell you

- It does not check every colour VS Code can draw, or colours added by other extensions.
- It does not check your font, font size, font weight or display.
- It does not replace testing with real users. Contrast checks are guidance, not a guarantee that every possible customisation meets accessibility requirements.
- A pair marked **Missing** could not be measured because a colour it depends on is missing.

## How the contrast guard changes colours

The guard moves a colour along its OKLCH lightness until the pair clears the minimum, keeping hue and chroma. Very saturated or unusual colours may shift visibly. The guard applies to text and syntax colours, not decorative washes.

## What the extension does not do

- Theme edits apply live. There is no dry-run or "apply later" mode, and the Preview tab is an illustrative specimen, not a full editor.
- There is no undo history, cloud preset gallery or multi-device preset service.
- It does not extract palettes from images.
- Recent colours in the picker last only for the current panel session.
- Settings change colours only. They cannot change VS Code's layout.
- Customisations apply only while an Auric Artisan theme is active.
- Colour overrides are per variant and are not shared between variants automatically.
