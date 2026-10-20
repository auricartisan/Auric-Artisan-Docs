---
title: Pantone & Named Lookup — The nearest chip in five named systems
description: Find the nearest CSS, Pantone Solid Coated, RAL Classic, NCS and Crayola chip to a colour by ΔE2000, compare any chip with your colour term by term, and copy names, codes and every notation.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Pantone & Named Lookup

Pantone & Named Lookup finds the chips nearest to your colour in five named colour systems at once: CSS named colours, Pantone Solid Coated, RAL Classic, NCS and Crayola. Every match carries its ΔE2000 distance and a word that says how close it is. You can select any match to compare it with your colour, see whether the chip is lighter, more saturated or a different hue, and copy its name or code.

Use it to find a starting reference to talk to a printer, a paint supplier or a manufacturer, for example "which Pantone is nearest to our brand blue?", before you check a physical swatch book. The chip values are approximate screen renderings, not licensed library data, and the tool says so on every tab.

Pantone & Named Lookup is in the launcher's **Explore** group. It opens in a floating panel over the page you are on; for moving, docking and closing panels, see [Open the Colour Tools and work in their panels](launcher-and-panels.md).

## How to open it

- **Launcher:** press `Ctrl` + `Shift` + `C` (or right-click the page and choose **Colour tools** › **All colour tools…**), then select **Pantone & Named Lookup**.
- **From another Colour Tool:** it is in the **Open in another tool** menu of CMYK Soft-Proof, Color Formulation and Color Space Converter, which pass their colour in.
- **A link:** add `?ctool=named` to any page address, with the keys under [Links](#links).

Opened from the launcher or the [Colour Tools dashboard](colour-tools-dashboard.md), it looks up the [working colour](launcher-and-panels.md#the-working-colour). With no colour at all, it looks up `#0F4C81`.

The chips download the first time you open the tool. Until they arrive, the header says "loading 561 chips…".

## Screen tour

This is a narrow tool: the colour fills the top of the panel, three tabs sit below it, and a row of actions runs along the bottom. [Open the Colour Tools and work in their panels](launcher-and-panels.md) describes the parts every tool shares, including the title bar, **Open in another tool**, **Dock** and the bottom sheet on phones.

### The header

The top of the panel is filled with your colour.

- A tag names the system of the nearest chip overall, for example **Nearest overall · Pantone Solid Coated**.
- The chip's name in large type, for example **PANTONE Classic Blue (2020)**.
- A line with your hex, the distance and the closeness word, for example "#0F4C81 · ΔE 0.0 · exact match".
- **The colour field**, with a picker button that takes a colour from anywhere on your screen (only in browsers that support it) and a dice button that tries a random colour.

The field accepts a hex code (with or without `#`), a CSS colour name or a CSS colour function. The tool follows as you type whenever the text is a complete colour; press `Enter` to also accept a fragment of a hex code. If you press `Enter` on something that is not a colour, the field is outlined in red and a message says "That isn't a colour yet".

On **Compare** and **Formats**, the header folds to a slimmer strip, without the tag, so the tab has room.

### Closeness words

Every match has a ΔE2000 value and a word:

| ΔE2000 | Word | What it means side by side |
|---|---|---|
| 0, same sRGB value | **Exact** | The chip has the same value as your colour. |
| Under 1 | **Imperceptible** | Nobody could tell them apart. |
| 1 to 2 | **Very close** | Only a trained eye sees it. |
| 2 to 5 | **Close match** | The difference shows. |
| 5 to 10 | **Noticeable** | Related, but clearly not the same colour. |
| 10 and above | **Distinct** | The nearest chip there is, but not a match. |

**ΔE2000** is the CIE's standard measure of how different two colours look. These are the same words every Colour Tool uses.

## Matches

**Matches** is the tab that opens first.

- **The verdict.** Two sentences and a note:
  - the nearest chip overall, its system, its distance and what that means, for example "Nearest overall: RAL 1032 Broom yellow in RAL Classic, ΔE 3.0 — close, the difference shows side by side." An exact match says so instead;
  - how many of the five systems have a close match (under ΔE 5) and which system is farthest. When none does, it says to treat every match as a starting point, not a substitute;
  - "Tap a match to compare it with your colour", and that your colour stays as it is.
- **System buttons.** **All**, **CSS**, **Pantone Solid Coated**, **RAL Classic**, **NCS** and **Crayola**, each with its number of chips. **All** shows five matches per system; a single system shows its eighteen nearest.
- **Selected for Compare.** A card with your colour and the selected chip side by side, the chip's name, hex, distance and word, and a **Compare** button that opens **Compare**. Until you select one, it is the nearest chip overall.
- **One section per system**, headed with its name and, for example, "141 chips · nearest 5":
  - the best match as a wide split button, **Your colour** on the left and **Best in** the system on the right, with its distance, its word and a copy button;
  - the next matches as rows with a swatch, name, hex, distance and word, each with its own copy button.

Select a match, or its split button, to select it for **Compare**. A message confirms it, for example "RAL 5019 Capri blue is selected for Compare. Your colour stays #0F4C81." Selecting a match never changes the colour you are looking up.

Copy buttons say **Copy name** for CSS and Crayola chips, and **Copy code** for Pantone, RAL and NCS chips. They copy the chip's full name, for example `RAL 5019 Capri blue`.

## The systems

| System | Chips | Example |
|---|---|---|
| **CSS named colours** | 141 | `aliceblue` |
| **Pantone Solid Coated** | 105 | `PANTONE Yellow C` |
| **RAL Classic** | 148 | `RAL 1000 Green beige` |
| **NCS** | 56 | `NCS S 0500-N` |
| **Crayola** | 111 | `Crayola Red` |

That is 561 chips in all. CSS named colours is the full CSS list. The Pantone, RAL, NCS and Crayola lists are curated subsets, not complete systems. Chips that share a value, such as two RAL greys, are both kept and rank side by side.

## Compare

**Compare** sets the selected chip against your colour.

- **The verdict** gives the chip's distance and what it means, then says in words how the chip differs, for example "The chip is slightly darker and much less saturated, and its hue turns well toward cyan. Most of the difference is chroma." An exact match says that lightness, chroma and hue all match, and that any difference in print comes from ink, paper and light.
- **Compare with · best in each system.** Five buttons, **CSS**, **Pantone**, **RAL**, **NCS** and **Crayola**, each with its best chip and distance. Select one to compare with it.
- **The pair.** Your colour, with its hex, family and OKLCH values, beside the chip, with its system, name, hex and family.
- **ΔE2000 in three parts · chip minus yours.** Rows for **Lightness** (ΔL′), **Chroma** (ΔC′) and **Hue** (ΔH′). Each has a signed value, a bar centred on no difference, a word such as "Slightly darker", "Much less saturated", "Turns well toward cyan" or "No visible difference", and its share of the whole difference, for example "55% of the difference". A note explains that these are the weighted terms inside CIEDE2000.
- **Values side by side.** **Hex**, **RGB**, **OKLCH**, **CIELAB · D65**, **CMYK · naive**, **Family**, **On white** and **On black** (the contrast ratio and grade), for your colour and for the chip.
- **Look up the chip instead** makes the chip the colour you are looking up. It is unavailable when the chip is an exact match. This is the only control that changes your colour, and it keeps a way back: a bar at the top of each tab says "You were looking up #… before this." with **Back to #…**.
- **Copy code and hex** (or **Copy name and hex**) copies the chip's name and hex, for example `RAL 5019 Capri blue #1B5583`.

## Formats

**Formats** lists the nearest chip per system and your colour in every notation.

- **The verdict** counts the notations, says how many paste straight into CSS, and names the nearest CSS keyword with its distance. A second sentence reminds you that the CMYK here is a naive split with no press profile, and points to CMYK Soft-Proof.
- **Nearest in each system · tap to copy.** One row per system with the chip's name, hex, distance and word. Select a row to copy the chip's name.
- **Your colour · every notation · tap to copy.** Eighteen or nineteen rows, each marked **CSS** or **Notation**: **HEX**, **HEX · 3 digit** (only when the colour has a short form), **RGB**, **RGB %**, **RGBA**, **HSL**, **HSLA**, **HWB**, **HSV / HSB**, **CMYK**, **XYZ**, **CIELAB**, **CIELCh**, **lab()**, **lch()**, **OKLab**, **OKLCH**, **Linear sRGB** and **CSS keyword**. Select a row to copy exactly what it shows.

**CSS** means the value pastes into a stylesheet as it is. **Notation** means a standard way of writing the values that is not a CSS function: HSV, CMYK and the D65 CIELAB and CIELCh rows. CSS `lab()` and `lch()` are defined on a D50 white, so their numbers differ from the D65 CIELAB rows; both are correct for their white.

## Walkthroughs

### Find the nearest Pantone to a brand colour

1. Type your brand colour into the field, for example `D3AF37`.
2. Select **Pantone Solid Coated**. The section now lists its eighteen nearest chips.
3. Read the best match: for `#D3AF37` it is **PANTONE 123 C**, ΔE 8.7, **Noticeable**.
4. Select it and then **Compare** to see how it differs, term by term.

The verdict on **Matches** tells you that RAL 1032 Broom yellow is the nearest chip overall, at ΔE 3.0. Take the Pantone reference to a physical guide before you specify it.

### Compare two systems for the same colour

1. Look up your colour and open **Compare**.
2. Under **Compare with · best in each system**, select **RAL**, then **NCS**.

Each time, the verdict, the three-part split and the side-by-side values change to the chip you chose. Your colour stays as it is.

### Look up a chip itself, and come back

1. On **Compare**, with a chip selected, select **Look up the chip instead**.
2. The chip becomes the colour you are looking up, and every tab shows its own nearest matches.
3. Select **Back to #…** in the bar at the top of the tab to return to your colour.

## Controls

| Control | What it does | Values or range | Default |
|---|---|---|---|
| Colour field | Sets the colour to look up. | Hex, CSS names, CSS colour functions; fragments on `Enter` | The colour you opened with, or `#0F4C81` |
| Picker button | Picks a colour from your screen. | Supported browsers only | — |
| Dice button | Tries a random colour. | — | — |
| System buttons | Show all systems or one. | **All**, **CSS**, **Pantone Solid Coated**, **RAL Classic**, **NCS**, **Crayola** | **All** |
| A match | Selects it for **Compare**. | Any chip shown | The nearest chip overall |
| **Compare** | Opens **Compare**. | — | — |
| **Compare with** buttons | Select the best chip of one system. | 5 systems | — |
| **Look up the chip instead** | Makes the selected chip your colour. | Unavailable for an exact match | — |
| **Back to #…** | Returns to the colour you were looking up before. | — | — |
| Copy buttons and rows | Copy a chip name, a chip and hex, or one notation. | — | — |
| Tabs | Switch the view. | **Matches**, **Compare**, **Formats** | **Matches** |

## Outputs and exports

The footer holds **Copy match**, **Share link**, **Save match** and **Export**. On a narrow panel or a phone, the last three show as icons.

| Output | Format | What it contains |
|---|---|---|
| **Copy match** | Text | The selected chip's name and hex, for example `PANTONE Classic Blue (2020) #0F4C81`. |
| **Share link** | A URL | This page with `?ctool=named`, your colour, the system filter, the selected chip and the tab. |
| **Save match** | A palette in your Library | Your colour and the chip, named for both, with the system, the ΔE2000 and the note that chip values are approximate. |
| **Selected chip · name and hex** | Text | The same as **Copy match**. |
| **Match report · Markdown** | Markdown table | One row per system: system, nearest chip, hex, ΔE2000 and match word, then your colour and the approximate-values note. |
| **CSV · every chip ranked** | CSV | All 561 chips, nearest first, with the columns `system`, `chip`, `hex` and `delta_e_2000`. |
| **JSON report** | JSON | Your colour, the nearest chip overall, the selected chip, the five nearest chips in each system, and the note. |
| **CSS custom properties** | CSS | `--match-css`, `--match-pantone`, `--match-ral`, `--match-ncs` and `--match-crayola`, each the nearest chip's hex with a comment naming the chip and its distance. |

The **Open in another tool** menu offers **Color Name Finder** (a name from the dictionary of named colours), **CMYK Soft-Proof** (proof the colour on coated and uncoated stock), **Color Inspector** and **Color Library** (the named colours nearest to it), all with your colour.

## Links

| Key | What it sets | Values |
|---|---|---|
| `ctool` | Opens this tool. | `named` |
| `color` | The colour to look up. | A hex code without `#` |
| `sys` | The system shown on **Matches**. | `css`, `pantone`, `ral`, `ncs`, `crayola` (or `all`) |
| `chip` | The chip selected for **Compare**. | The chip's name in lower case with hyphens, for example `ral-5019-capri-blue` |
| `ctab` | The tab to open on. | `matches`, `compare`, `formats` |

For example, `?ctool=named&color=D3AF37&sys=pantone&chip=pantone-123-c&ctab=compare` compares `#D3AF37` with PANTONE 123 C.

## Accuracy and limits

- **Approximate values, not licensed data.** The Pantone, RAL and NCS chips are widely published sRGB approximations of printed or painted colours. Real swatches vary with paper, ink, finish and lighting, and a screen cannot show some of them accurately at all. Always confirm with the official physical guide before you specify a colour.
- **Subsets.** The Pantone, RAL, NCS and Crayola lists are curated subsets. A closer official colour may exist that the tool does not know about.
- **ΔE2000 predicts a side-by-side difference on screen**, under good viewing. It does not say how a colour will print.
- **CMYK is naive.** The CMYK values on **Compare** and **Formats** use a simple formula with no press profile. Compare the two columns with each other, not with a press sheet. To see how a colour might print, use [CMYK Soft-Proof](cmyk-soft-proof.md).
- **Families** come from one OKLCH rule shared with the Color Name Finder and Color Library: Red, Orange, Yellow, Green, Cyan, Blue, Violet, Pink, Brown and Neutral.
- **Network.** The chips download from the site the first time you open the tool. If they cannot load, the header says "the chips could not be loaded".

## Related

- [Colour Tools documentation](README.md)
- [Open the Colour Tools and work in their panels](launcher-and-panels.md)
- [Colour Tools dashboard](colour-tools-dashboard.md)
- [Color Name Finder](colour-name-finder.md) — the nearest name from the dictionary of named colours
- [CMYK Soft-Proof](cmyk-soft-proof.md) — how the colour might shift in print
- [Color Inspector](colour-inspector.md) — its **About** section shows the nearest entry in each system too
- [Library Kit](../../../../../kits/library-kit/README.md) — where saved matches go
