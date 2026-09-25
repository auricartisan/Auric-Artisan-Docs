---
title: Font Library — Family details
description: The Suitability, Pairings, Glyphs, Features, Styles, About, License and Charset tabs of the family panel.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Family details

These eight tabs in the family panel tell you what a family is good for, what goes with it, what it contains and what you may do with it.

## Suitability

The page explains: *Scores are computed from this font's own outlines and metrics — x-height, character distinction, proportions, weight range and screen rendering — not editorial opinion.*

Five scores from 0 to 100, sorted best first:

| Score | Meaning on the page |
| --- | --- |
| **Accessibility** | Legibility & character distinction for the widest audience |
| **Readability** | Comfort for long-form body text |
| **UI / Product** | Clarity at small sizes in interfaces |
| **Developer / Code** | Monospacing & glyph disambiguation for code |
| **Editorial** | Headlines & long-form print character |

**Why these scores** shows the measurements behind them, each 0 to 100:

- **x-height**, with the measured value in em;
- **Character distinction (I l 1 · 0 O)**, noting *distinct zero* where the zero differs from the letter O;
- **Proportion / width**;
- **Weight flexibility**, with the number of weights;
- **Screen rendering**;
- **Low stroke-contrast**.

**Best for** lists uses the family qualifies for: *UI & product* (UI 78 or more), *Body text* (readability 78 or more), *Code* (developer 75 or more), *Headlines* (editorial 78 or more) and *Accessibility-critical* (accessibility 85 or more). A family that reaches none shows *Display & accents*.

**Style fingerprint** rates eight traits from 0 to 100: Modern, Classic, Elegant, Playful, Technical, Friendly, Bold and Minimal. The recommender and the pairings use these.

Colours on scores run from low to great. For what the scores can and cannot tell you, see [Limits and accuracy](../others/limits-and-accuracy.md).

## Pairings

Pairings suggest a partner that contrasts in role but matches in proportion. The page says whether the open family is treated as the **heading** or the **body**: serif and display families, and any family with an editorial score of 72 or more, are headings; others are bodies.

- A preview sets *Designing with type* in the heading face and a paragraph in the body face, each labelled with its family.
- **Best body partners** (or **Best heading partners**) lists eight partners with a score from 60 to 99. A **Super-family** badge marks a partner from the same family of designs, such as a sans and a serif sharing a name.
- Select a partner to preview it. **＋ Select both** adds both families to **Your kit**; **Open** *family* opens the partner in the panel.

The score blends how well the two categories pair, how close their x-heights are, how strong the partner is in its role, and its accessibility and UI quality. Partners come from the same shortlist of about 130 well-known families the recommender uses, without handwriting faces.

## Glyphs

Every character the family maps, in its own face, with the total at the top (a **+** after it means the count stopped at the limit). Hover a glyph to see its code point, such as *U+0041*.

- Select a glyph to copy the character; the message reads, for example, **Copied U+00E9**.
- **Size** (18 to 80 pixels) sets the glyph size.
- Glyphs appear 600 at a time; **Show more glyphs** adds the next batch. Up to 8,000 are shown.

## Features

Each OpenType feature the family supports, shown *default → enabled* on a sample chosen for it, for example fractions on *1/2 3/4 5/8 11/16* or tabular figures on *1111 2222 3333*. Each row shows the feature's name and four-letter tag.

Select a row to copy its CSS, for example `font-feature-settings: "tnum" 1;`. The message reads **Copied "tnum" CSS**.

If the family has none, the tab reads *This family exposes no toggleable OpenType features.*

## Styles

- **All weights & styles**: a line of your preview text (or the family name) in every weight, and every italic if the family has them.
- A download card: **Download self-hosting kit**, with the number of font files, and **Download kit**. For a family that is listed but not served, it reads **Installed system family** and the button is disabled.
- **Font files**: a table of every file with **Style**, **Weight**, **Width**, **Format** (or **⚡ Variable**), **Size**, **Glyphs**, and a **Download** link for that single file (or an **Installed** badge).

## About

The family's description, if it has one, then **Details**: **Designer**, **Foundry / Publisher**, **Category**, **Classification** (serif or sans-serif, detected from the letter shapes), **Version**, **Released / Created**, **Last modified**, **Outline format** (TrueType or PostScript/CFF), **Styles**, **Weights**, **Variable axes**, **Glyph count**, **Embedding** and **Source**. Designer and foundry names link to their websites where the font gives one. **Copyright** and **Trademark** notices follow when present.

Everything here is read from the font files themselves, so it is only as complete as the files.

## License

- A badge with the licence name, and buttons for the **License URL ↗** and the **Original file** the licence came from, when known.
- Six permissions: **Commercial use**, **Modification**, **Redistribution**, **Private / personal use**, **Web embedding** and **Sell font on its own**. Each shows a tick, a cross, or *Not stated in this file* when the licence could not be read for that point. Unknowns are listed last.
- **Copyright**, then **Full license**: the complete licence text, or *No bundled license text was found for this family. Refer to the foundry or the license URL above.*

The permissions summarise the licence for convenience. The full licence text is what applies. See also [Font CDN licences](../../../../../services/font-cdn/others/licences.md).

## Charset

- **Supported scripts**, as chips.
- **Character coverage**: **Characters mapped**, **Glyphs in font** and **First / last codepoint**.
- **Unicode ranges (first 40)**.
- **Sample**: a sample sentence in the family's face.

Use this tab to check a language before choosing a family; the **Scripts** filter only offers the 18 most common scripts and blocks.

## Related

- [The specimen panel](specimen-panel.md)
- [Develop and embed](develop-and-embed.md)
- [Glossary](../others/glossary.md)
