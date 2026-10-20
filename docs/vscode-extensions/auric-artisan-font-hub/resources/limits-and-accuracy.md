---
title: Auric Artisan Font Hub — limits and accuracy
description: What Font Hub's scores, recommendations, checks and insertion can and cannot guarantee, and its size limits.
product: VS Code extensions › Auric Artisan Font Hub
updated: 2026-09-25
---

# Limits and accuracy

## Scores and recommendations

- Suitability and accessibility scores are catalogue estimates built from measured traits of the fonts, such as x-height and how distinct similar characters are. They are guidance for shortlisting, not guarantees.
- Categories are assigned automatically and can occasionally be wrong for unusual designs.
- Recommendations blend the chosen intent, industry, palette and your local use. They are a starting point.
- Always check your real text, languages, sizes and colour contrast in the finished product.

## Previews

- Previews use the real font files, fetched through VS Code and cached. A family may show **Preview unavailable** when offline or when a file cannot be fetched.
- Variable-axis sliders and OpenType toggles only show what the preview font file supports.
- System-font previews depend on the font being installed on your computer.

## Automatic insertion

- Supports HTML files with a `<head>`, CSS, SCSS, Less, PostCSS, JavaScript and TypeScript. Other languages get a copied embed.
- Works on files up to 2 MiB.
- It is deliberately conservative, not a complete HTML, CSS or JavaScript parser. It skips `<head>` tags inside comments, scripts and styles, and it will not add a setup twice.
- Explicit formats insert at the cursor; they do not merge into framework configuration files.
- Up to 12 families can be inserted together.

## CDN check

- Checks one catalogue file, one stylesheet and one font file, with `HEAD` requests from the test address `http://localhost:5500`, with a 10-second timeout per request.
- It is a sample, not an audit of every family or of your production address.
- It reports what the CDN answers; it cannot change hosting settings or bypass browser security.

## Self-hosting kits

| Limit | Value |
| --- | --- |
| Families per kit | 6 by default, up to 12 (`auricFontLib.download.maxFamilies`) |
| One font file | 40 MB |
| Whole kit | 250 MB |

Kits are refused when redistribution permission or a required licence notice cannot be established. System fonts are never exported.

## Catalogue

- 2,023 library families, 547 variable, in the bundled snapshot.
- A refresh only accepts validated data; new families may need an extension update.
- The cache is limited to `auricFontLib.cache.maxMB` (512 MiB by default); the oldest items go first.
