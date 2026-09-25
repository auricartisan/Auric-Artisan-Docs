---
title: Font Library — Limits and accuracy
description: What the Font Library's catalogue, categories, scores, recommendations and previews can and cannot tell you.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Limits and accuracy

## The catalogue is read from the font files

Names, designers, foundries, versions, dates, weights, scripts and licences come from the data inside each font file. Where a file leaves something out, the page leaves it out too, or shows it as unknown. 191 families have no licence the catalogue could identify; they appear under **Unspecified**.

## Categories are detected automatically

Each family's category (serif, sans serif, display, handwriting or monospace) and its serif or sans-serif classification are worked out from the font's data and letter shapes, not assigned by hand. Some families are misclassified; rounded sans-serifs in particular can be listed as serif. If the category filter hides a family you expect, search for it by name.

## Scores are computed, not judged

The suitability scores and style fingerprints are calculated from measurements of each font: x-height, how distinct look-alike characters are, proportions, weight range, stroke contrast and how it renders on screen. They are useful for sorting and comparing, but:

- they do not know how a font was designed to be used, so a display face can score well in a category it was not made for;
- a high accessibility score is a good sign, not a guarantee. Test your text at real sizes with real readers, and check colour contrast separately.

This is why the collections and the recommender draw on curated lists rather than the raw top scores.

## Recommendations and pairings use a shortlist

The recommender and the pairings rank within about 130 well-known, versatile families. Other families never appear there, however well they would fit. Pairings leave out handwriting faces.

## Installed families

190 families marked **Installed** are listed from installed system fonts and are not served. Their cards and specimens use your own copy of the font if you have one; otherwise you see a stand-in. They cannot be downloaded, and their embed code only works on devices with the font installed.

## Previews are your browser's rendering

Specimens are drawn by your browser from the served font files. Rendering differs a little between operating systems and browsers, and bold or italic buttons in the specimen editor are imitated by the browser if the family lacks those styles.

## Page limits

| Limit | Value |
| --- | --- |
| Card specimen size | 22 to 48 pixels, whatever the slider shows |
| Script filter chips | The 18 most common scripts and blocks |
| Glyphs shown in the Glyphs tab | Up to 8,000 |
| Unicode ranges listed in the Charset tab | The first 40 |
| Families compared at once | 4 (the first four in your kit) |
| Collection rows | Up to 14 families each |
| Recently viewed | The last 12 families |
| Recommender results | 12 |
| Pairing suggestions | 8 |

## Known issues

At the time of writing:

- sorting by **Accessibility score** or **Readability score** leaves the grid in alphabetical order;
- the `F` and `R` keys appear to do nothing;
- the **Selected weights** chips in **Use & Embed** do not change the code;
- the search box mentions foundries, but foundry names are not searched.

See [Troubleshooting](../docs/troubleshooting.md) for workarounds.

## Related

- [Font CDN limits and accuracy](../../../../../services/font-cdn/others/limits-and-accuracy.md)
- [Family details](../docs/family-details.md)
- [Supporting material](README.md)
