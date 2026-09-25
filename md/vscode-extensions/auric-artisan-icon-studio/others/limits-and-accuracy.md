---
title: Auric Artisan Icon Studio — Limits and accuracy
description: What Icon Studio's search, recommendations and smart insert can and cannot do.
product: VS Code extensions › Auric Artisan Icon Studio
updated: 2026-09-25
---

# Limits and accuracy

## Catalog

- The catalog is fixed at the version you installed: 17,234 entries in 11 collections. New icons arrive with extension updates.
- Counts are catalog entries, not the number of style or tone variants.
- Emoji are drawn by your operating system's emoji font, so their look varies and very new emoji may not display on older systems.
- Material icons are font glyphs and cannot be exported as SVG.

## Search and recommendations

- Search matches names, concepts, tags and synonyms, and uses Hindi aliases where available. It is not a full translation of the catalog.
- **For you** and Quick Pick recommendations are ranked locally from the text around your cursor (about 60 lines either side), the file type, and your likes and use. They are suggestions, not an AI service.

## Smart insert

- Smart insert picks a format by language. It does not look at the exact cursor position, so it cannot tell whether you are inside a string, a tag or a comment.
- It does not add imports, fonts or build configuration to your project.
- Inserted SVG includes an accessible name based on the icon name when the artwork has none. Decide whether each icon is decorative or meaningful and adjust the label.

## Hover previews

- Only Auric icon IDs (a hyphenated name ending in a four-digit number) are previewed. Open-source icon IDs are not.
- When the owning collection extension is installed, it shows the preview instead of Icon Studio.

## Licences

Auric artwork is covered by the Auric Artisan Free Use Licence, which is not an unrestricted asset licence. Open-source sets keep their own licences, shown in the credit line when you choose a single collection.
