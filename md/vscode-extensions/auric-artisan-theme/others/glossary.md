---
title: Auric Artisan Theme — Glossary
description: Definitions of the terms used in Auric Artisan Theme and Theme Studio.
product: VS Code extensions › Auric Artisan Theme
updated: 2026-09-25
---

# Glossary

| Term | Meaning |
| --- | --- |
| Accent | The single colour the whole theme is keyed to. Washes, borders, selections, the focus ring and the cursor are derived from it. |
| Alpha | Transparency. Alpha slots accept an opacity value, written as the last two digits of `#rrggbbaa`. |
| APCA Lc | A perceptual contrast value from the draft WCAG 3 work. It accounts for polarity; a negative value means light text on a dark background. |
| Audit | The contrast check of 81 foreground and background pairs in the active theme. |
| Canvas | The editor background, slot `bg.base`. |
| Chrome | The workbench bars and frames around the editor: status bar, activity bar, title bar, side bar and tabs. |
| Colour slot | One named colour the theme is built from, such as `syntax.keyword`. There are 107. |
| Contrast guard | The step that nudges colours along OKLCH lightness until they meet your minimum contrast. Controlled by **Enforce contrast**. |
| Contrast ratio | The WCAG measure of luminance difference, from 1:1 to 21:1. |
| Customisation JSON | The portable document holding your changed dials and colour overrides. |
| Dial | One theme setting, such as **Syntax palette** or **Depth**. There are 37, all under `auricTheme.*`. |
| Family | A set of variants sharing the same neutral surfaces, such as Obsidian or Porcelain. |
| High contrast | The two builds designed for VS Code's high-contrast modes, one dark and one light. |
| Look | A named combination of dial values, such as **Clarity**, that you apply in one click. |
| OKLCH | A colour model with Lightness, Chroma (colourfulness) and Hue that matches human perception closely, so changing hue keeps colours looking equally strong. |
| Override | A colour you set for a slot by hand. It wins over the dials and is stored per variant. |
| Polarity | Whether a theme is dark (light text on dark) or light (dark text on light). |
| Preset | A named, saved copy of your dials and overrides, kept on this machine. |
| Semantic highlighting | Colouring based on what a language server knows about a symbol, in addition to TextMate grammar colouring. |
| Shipped | The colour a slot has in the variant as published, before your changes. |
| TextMate token | A piece of code classified by a grammar, such as a string or keyword, and coloured by the theme. |
| Theme Studio | The editor-tab interface for customising the theme, with six tabs. |
| Variant | One of the 54 complete themes: a family plus an accent. |
| WCAG AA / AAA | Web Content Accessibility Guidelines levels. AA needs 4.5:1 for body text (3:1 for large text and control edges); AAA needs 7:1. |
