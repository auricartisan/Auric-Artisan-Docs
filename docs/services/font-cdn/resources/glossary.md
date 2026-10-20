---
title: Font CDN — Glossary
description: Definitions of the type and web-font terms used in the Font CDN documentation.
product: Services › Font CDN
updated: 2026-09-25
---

# Glossary

**Axis.** One dimension a variable font can vary along, such as weight (`wght`), width (`wdth`), slant (`slnt`) or optical size (`opsz`).

**CDN (content delivery network).** A service that serves files, here fonts and stylesheets, to web pages.

**Fallback.** A font the browser uses when the one you asked for is not available yet or lacks a character.

**Family.** A set of related fonts sharing a name, such as Alegreya in regular, italic and several weights.

**Family id.** The lower-case, hyphenated form of a family name used in its stylesheet URL, such as `roboto-slab`.

**`@font-face`.** The CSS rule that tells the browser where to find a font file and which family, weight and style it provides.

**`font-display: swap`.** A setting that shows text in a fallback font straight away and swaps to the web font when it arrives.

**Font stack.** A `font-family` list with fallbacks in order of preference.

**Glyph.** A single drawn character shape in a font.

**Installed.** A family listed in the catalogue but not served, because it is a system font whose licence does not allow redistribution.

**Kit.** A ZIP file from the Font Library with a family's font files, stylesheet, demo page, notes and licence, for self-hosting.

**Loader.** The `font-cdn.js` script that adds stylesheets and offers the `AuricFonts` JavaScript API.

**OpenType features.** Optional behaviours built into a font, such as ligatures, small capitals or tabular figures, switched on with CSS `font-feature-settings`.

**SIL Open Font License (OFL).** The most common open licence for fonts. It allows use, embedding, modification and redistribution, but not selling the font file on its own.

**Self-hosting.** Serving font files from your own site instead of a CDN.

**Static font.** A font file with one fixed weight and style.

**Variable font.** A font file that contains a continuous range along one or more axes, such as every weight from 100 to 900.

**Weight.** How heavy the strokes are, from 100 (Thin) to 900 (Black); 400 is Regular and 700 is Bold.
