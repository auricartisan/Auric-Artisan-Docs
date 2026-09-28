---
title: Color Name Finder — Name any colour
description: Name any colour with the nearest of 1,055 named colours by ΔE2000, see how it differs in words, its hue family, the next names and the 18 nearest neighbours, and copy it in 20 notations.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Color Name Finder

Color Name Finder gives a colour a name. It measures your colour against a dictionary of 1,055 named colours, picks the nearest by ΔE2000, and says in words how close it is and how it differs: lighter or darker, more or less saturated, and which way the hue leans. It also files the colour in one of ten hue families, lists the next nearest names and the 18 nearest neighbours, and writes the colour in 20 notations.

Selecting a name copies it and leaves your colour alone. **Inspect** is the only thing that changes the colour being named, and it always offers a way back.

Color Name Finder is one of the six **Essentials** in the Colour Tools. It opens in a floating panel; for the panel, its footer and its links, see [Open the Colour Tools and work in their panels](launcher-and-panels.md).

## Open it

- **Launcher:** press `Ctrl` + `Shift` + `C`, then select **Color Name Finder**, or type a colour in the search and choose **Find the name of …**.
- **Right-click menu:** **Colour tools** › **Color Name Finder**, or right-click a colour value and choose **Find its name**.
- **Dashboard:** the **Color Name Finder** card, which already shows the nearest name. See [Colour Tools dashboard](colour-tools-dashboard.md).
- **From another tool:** the Color Library's card menu (**Find name**) and its **Open in another tool** menu.
- **A link:** `?ctool=name&color=1E40AF`. The colour can also be a name from the dictionary, for example `?ctool=name&color=goldenrod`. See [Link keys](#link-keys).

With no colour, it starts on the site's gold, `#D3AF37`. The dictionary downloads the first time you open the tool; until it arrives, the specimen says "loading 1,055 names…".

## Screen tour

### The specimen

The top of the panel is filled with your colour, and all its words are written in black or white, whichever reads better on it.

- **The family chip**, for example "Blue family · OKLCH 266°", or "Neutral · chroma 0.000" for a colour with no hue.
- **The colour field**, with a pen-shaped button that picks a colour from your screen (in browsers that support it) and a dice button for a random colour. It accepts a hex code, a CSS colour name or function, and any name from the dictionary, such as `Persian Blue` or `goldenrod`; spaces, hyphens and capitals do not matter.
- **The name**: the nearest name, in large type.
- **The line under it**: the hex code, the ΔE and how close that is, for example "#1E40AF · ΔE 2.9 · close to your colour", or "an exact match".

On **Neighbours** and **Formats** the specimen folds to a strip with the name and a shorter line.

### The tabs

**Names**, **Neighbours** and **Formats**. While you are looking at a name you reached with **Inspect**, each tab starts with "You were naming #… before this." and **Back to #…**.

## Names

The opening sentences give the match and the difference in words, for example:

- "Persian Blue is the nearest of 1,055 names, ΔE 2.9: close — the difference shows side by side."
- "Persian Blue is slightly darker and more saturated, and its hue leans toward violet. Most of the difference is hue."

For an exact match they say so ("#DAA520 is Goldenrod exactly, one of 1,055 names in the dictionary.") and give its family, OKLCH lightness, chroma and hue.

**Best match · ΔE2000** shows your colour and the named colour side by side, the ΔE, and a pill: **Exact**, **Imperceptible**, **Very close**, **Close match**, **Noticeable** or **Distinct**. **Copy name** copies the name; **Inspect** makes the named colour the one being named (it is greyed out for an exact match). When other names in the dictionary have exactly the same value, a line lists them: "Same value, other names in the dictionary: Steel Gray."

**Hue family · one OKLCH classification** gives the family in large type, the OKLCH lightness, chroma and hue, and a hue strip with the family bands (Red, Orange, Yellow, Green, Cyan, Blue, Violet, Pink) and a marker at your hue. A sentence says why the colour is in that family, for example "Hue 266° falls in the Blue band (225–285°), and chroma 0.181 clears the 0.035 neutral line." The same rule files every name in the Color Library, so a name's family agrees in both tools.

**Next 8 names · tap to copy** lists the next eight names, each with its swatch, hex code, a bar for its ΔE on a 0 to 20 scale, and its word. Select a row to copy the name, or **Inspect** to name that colour instead. Other spellings of the best match are left out of this list.

### How close is close

| ΔE2000 | Word | What it means side by side |
|---|---|---|
| 0 | **Exact** | The same value. |
| Under 1 | **Imperceptible** | Nobody could tell them apart. |
| 1 to 2 | **Very close** | Only a trained eye sees it. |
| 2 to 5 | **Close match** | The difference shows. |
| 5 to 10 | **Noticeable** | Related, but clearly not the same colour. |
| 10 or more | **Distinct** | The nearest name there is, but not a match. |

## Neighbours

The 18 names nearest your colour, placed by lightness.

The opening sentences count them and point the way lighter and darker, for example "Of the 18 names nearest #1E40AF, 6 are lighter, 5 sit at its lightness (within ±0.03 OKLCH L) and 7 are darker. For a lighter version, the closest name is Cerulean Blue (#2A52BE, ΔE 5.8); for a darker one, Egyptian Blue (#1034A6, ΔE 3.6)."

- **Where they sit** is a map with your colour as the ringed dot in the middle. Up is lighter and down is darker; sideways is OKLCH hue ("← toward cyan", "toward violet →"), or, for a colour with almost no hue, chroma ("← greyer", "more colourful →"). Each dot is painted in its own colour.
- **Lighter**, **Same lightness** and **Darker** list the neighbours as cards, each with its swatch, name, hex code, ΔE and lightness difference, for example "+0.040 L". Select a card to copy its name, or **Inspect** to name it instead.

## Formats

Your colour in 20 notations (21 when its hex code has a 3-digit short form). The opening sentence says how many paste straight into CSS and reminds you that CSS `lab()` and `lch()` use a D50 white, so they read differently from the D65 CIELAB rows; both are correct.

Filter the list with **All**, **CSS** or **Notation**, each with its count. Select a row to copy exactly what it shows.

| Row | Marked | Notes |
|---|---|---|
| **HEX**, **HEX · 3 digit** | CSS | The short form only when every channel repeats a digit. |
| **RGB**, **RGB %** | CSS | Modern space-separated `rgb()`. |
| **RGBA**, **HSLA** | CSS | Legacy comma form. |
| **HSL**, **HWB** | CSS | |
| **HSV / HSB** | Notation | No CSS function. |
| **CMYK** | Notation | A naive split with no press profile. |
| **XYZ** | CSS | `color(xyz-d65 …)`. |
| **CIELAB**, **CIELCh** | Notation | D65. |
| **lab()**, **lch()** | CSS | D50, as CSS defines it. |
| **OKLab**, **OKLCH** | CSS | |
| **Linear sRGB** | CSS | No transfer curve. |
| **CSS keyword** | CSS | The nearest real CSS colour name, "exact match" or with its ΔE. |
| **Custom property** | CSS | `--colour-persian-blue: #1e40af;`, named after the nearest name. |
| **Nearest name** | Notation | The name and its ΔE. |

## Walkthroughs

### Name a colour

1. Type or paste the colour into the specimen's field.
2. Read the name and the first sentence on **Names**.
3. Select **Copy name**.

### Find a lighter or darker named version

1. Open **Neighbours**.
2. Read the second sentence for the closest lighter and darker names, or look under **Lighter** and **Darker**.
3. Select **Inspect** on a card to name that colour instead. **Back to #…** returns to your colour.

### Give a colour a token name

1. Open **Export** and choose **CSS custom property**.
2. Paste it into your stylesheet: it keeps your exact colour and takes its name from the nearest name.

## Controls

| Control | What it does | Default |
|---|---|---|
| Colour field | Sets the colour to name. Accepts hex, CSS colours and dictionary names. | The colour you opened with, or `#D3AF37` |
| Pen button | Picks a colour from the screen (supported browsers only). | — |
| Dice button | Picks a random colour of medium lightness and chroma. | — |
| **Copy name** and name rows | Copy a name. | — |
| **Inspect** | Names that colour instead. | — |
| **Back to #…** | Returns to the colour you were naming. | — |
| **All** / **CSS** / **Notation** (Formats) | Filters the notations. | **All** |

## Outputs and exports

| Output | Format | What it contains |
|---|---|---|
| **Copy name** (gold button) | Text | The nearest name, for example `Persian Blue`. |
| **Name and hex** | Text | `Persian Blue #1C39BB (nearest name to #1E40AF, ΔE2000 2.87)`, or just the name and hex for an exact match. |
| **CSS custom property** | CSS | `--colour-persian-blue: #1e40af;` with a comment naming the nearest name, its hex and ΔE2000. |
| **Markdown table · 9 nearest** | Markdown | Name, Hex, ΔE2000 and Match for the best match and the next eight. |
| **CSV · 18 neighbours** | CSV | `name,hex,delta_e_2000,delta_l_oklch`, one row per neighbour. |
| **JSON report** | JSON | The colour, its family, its OKLCH values, the nine nearest names with ΔE2000 and match word, and the dictionary counts. |
| **Every format · plain text** | Text | All 20 notations, one per line. |
| **Save colour** | A colour in your Library | Named with the nearest name and your hex code. |
| **Share link** | URL | `?ctool=name&color=…`, with `ctab` unless you are on **Names**. |

**Open in another tool** offers **Color Library** (the colour's family, nearest first), **Pantone & Named Lookup** (the nearest Pantone, RAL, NCS and Crayola chips), **Color Inspector** and **Harmony Studio**.

## Link keys

| Key | What it sets | Values |
|---|---|---|
| `color` (or `colour`) | The colour to name. | A hex code, a CSS colour, or a name from the dictionary, for example `goldenrod` |
| `ctab` | The tab to open on. | `names` (default), `neighbours`, `formats` |

## Accuracy and limits

- **Terms.** *ΔE2000*: the CIEDE2000 colour difference, the standard measure of how different two colours look. *OKLCH*: a colour model whose lightness, chroma and hue change evenly to the eye.
- **The dictionary.** The names file has 1,058 entries. Three are listed twice with the same name and value and are counted once, leaving 1,055 names. Many values carry more than one name, which the tool lists as other names for the same value.
- **Names are names, not standards.** The dictionary gathers common colour names from several sources. For print and paint systems such as Pantone, RAL and NCS, use [Pantone & Named Lookup](pantone-and-named-lookup.md).
- **The difference in words** splits ΔE2000 into its lightness, chroma and hue parts. It describes the named colour relative to yours.
- **Families are one rule.** Chroma under 0.035 is **Neutral**; dark or dusty reds, oranges and yellows are **Brown**; pale, soft reds are **Pink**. A colour called "pink" in the dictionary can therefore sit in the **Red** family.
- **CMYK is a naive split**, not a press conversion. Soft-proof print colour in [CMYK Soft-Proof](cmyk-soft-proof.md).
- **Solid sRGB only.** Transparency is ignored.

## Related

- [Colour Tools documentation](README.md)
- [Open the Colour Tools and work in their panels](launcher-and-panels.md)
- [Color Library](colour-library.md) — browse the same 1,055 names by family
- [Pantone & Named Lookup](pantone-and-named-lookup.md) — Pantone, RAL, NCS, Crayola and CSS names
- [Color Inspector](colour-inspector.md) — everything about one colour
- [Basic Color Tools](../../README.md)
