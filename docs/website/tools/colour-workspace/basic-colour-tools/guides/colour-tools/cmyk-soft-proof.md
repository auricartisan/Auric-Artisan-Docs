---
title: CMYK Soft-Proof — How a colour may shift on press
description: Simulate a screen colour or an image on six print conditions with a choice of black generation, see the separation as sent and on press against the ink limit, test the colours around it, and copy device-cmyk() values. A model, not ICC colour management.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# CMYK Soft-Proof

Screens mix light; printing presses lay ink on paper. Many bright screen colours cannot be printed, paper is never pure white, printed black is never pure black, and ink spreads as it soaks in. CMYK Soft-Proof gives you a feel for these effects before you send a file. It takes a colour, or an image you drop in, and shows how it might look on one of six print conditions, the CMYK ink amounts involved, whether they run over the press's ink limit, and which colours nearby shift the most.

**Soft-proofing** means previewing on screen how something will print. **CMYK** is four-ink printing with cyan, magenta, yellow and black. **Dot gain** is the darkening of tints as ink spreads on paper. **TAC** (total area coverage) is the most combined ink a press allows, as C + M + Y + K in percent, up to 400%. **Black generation** decides how much of a colour's grey component is printed with black ink instead of the three colours.

This tool is a model for intuition, not ICC colour management. It shows the direction and rough size of a print shift; proof against your printer's real profile before you sign anything off.

CMYK Soft-Proof is in the launcher's **Design** group. It opens in a floating panel over the page you are on; for moving, docking and closing panels, see [Open the Colour Tools and work in their panels](launcher-and-panels.md).

## How to open it

- **Launcher:** press `Ctrl` + `Shift` + `C` (or right-click the page and choose **Colour tools** › **All colour tools…**), then select **CMYK Soft-Proof**.
- **From another Colour Tool:** it is in the **Open in another tool** menu of Pantone & Named Lookup, Color Formulation and Color Space Converter, and in the Color Inspector's **Open in another tool** list.
- **A link:** add `?ctool=softproof` to any page address, with the keys under [Links](#links).

Opened from the launcher or the [Colour Tools dashboard](colour-tools-dashboard.md), it proofs the [working colour](launcher-and-panels.md#the-working-colour). With no colour at all, it proofs process blue, `#0085CA`, on **FOGRA39 coated** with **Medium** black generation and dot-gain compensation on.

## Screen tour

The panel has the shared Colour Tools layout: the screen and press colours painted across the top, four tabs, a controls rail on the left, the selected tab on the right and a row of actions at the bottom. [Open the Colour Tools and work in their panels](launcher-and-panels.md) describes the parts every tool shares, including the title bar, **Open in another tool**, **Dock** and the bottom sheet on phones.

### The screen and press band

- **The left half** is your colour as the screen shows it. It is headed **Screen · sRGB** with the hex, gives the size of the shift, for example "ΔE 5.4 — a noticeable shift", and a line with a plain-language name and the RGB values.
- **The right half** is the press simulation, framed by the condition's paper colour. It is headed with the condition, the black generation and "compensated" when compensation is on, names the shift, for example "Slightly darker and duller on FOGRA39 coated paper", and gives the simulated hex and the separation as sent, for example "#2581AC · C100 M34 Y12 K4 sent".

### The controls rail

- **Colour.** A colour field, with a picker button in browsers that support it. Under it, six colours to start from: Process blue `#0085CA`, Auric gold `#D3AF37`, House navy `#1D2A3E`, Gold ink `#765A0B`, Paper `#F5F0E6` and Black `#000000`.
- **Press condition.** The paper and press to simulate.
- **Constants · approximate.** The chosen condition's **Paper white**, **Black point**, **Dot gain** (the rise at a 50% tint) and **Ink limit**, and a note describing the condition, ending "Hand-set stand-ins, not the condition's characterisation data."
- **Black generation.** **UCR**, **Light**, **Medium** or **Heavy**, with a note on what the choice does.
- **Compensate for dot gain, as a profile would.** When ticked, the separation is thinned before sending so that, after dot gain, the press lands on the intended tint.

The colour field accepts a hex code (with or without `#`), a CSS colour name or a CSS colour function. The tool follows as you type whenever the text is a complete colour. If you press `Enter` on something that is not a colour, the field is outlined in red and a message says "That isn't a colour yet".

On a narrow panel or a phone, the rail moves above the results.

## Press conditions

| Condition (as listed) | Full name | Paper white | Black point | Dot gain at 50% | Ink limit |
|---|---|---|---|---|---|
| **FOGRA39 coated** | ISO Coated v2 (FOGRA39) | `#F4F2E8` | `#1B1814` | 12% | 330% |
| **GRACoL 2013 coated · new** | GRACoL 2013 (CRPC6) | `#EFF0F8` | `#1A1A1D` | 13% | 320% |
| **SWOP web coated** | SWOP (US Web Coated) | `#F1EFE3` | `#1F1B16` | 16% | 300% |
| **FOGRA52 uncoated** | ISO Uncoated (FOGRA52) | `#EFEBD8` | `#252118` | 20% | 320% |
| **Newsprint** | ISO Newsprint 26v5 | `#EAE3CE` | `#2B2719` | 28% | 240% |
| **Fine-art rag** | Fine art · cotton rag inkjet | `#F8F3DF` | `#1C1610` | 8% | 360% |

FOGRA39 is European offset on coated stock, the most common commercial specification. GRACoL 2013 is US sheet-fed coated, the G7 reference, with a bluish paper from optical brighteners. SWOP is US web offset with a lower ink limit. FOGRA52 is premium uncoated stock, with higher dot gain and warmer paper. Newsprint has heavy dot gain and a low ink limit. Fine-art rag is inkjet on cotton rag, closer to what a screen can show than offset.

## Black generation

| Setting | What it does (as the tool says) |
|---|---|
| **None (UCR)** | Black only in deep neutral shadows; C, M and Y carry the rest. The highest ink totals. |
| **Light GCR** | Black starts in the three-quarter tones and takes over part of the grey. |
| **Medium GCR** | Black carries most of the grey from the midtones down. A common default. |
| **Heavy GCR** | Black carries the whole grey component: the lowest ink totals and the steadiest greys. |

Every setting describes the same colour; what changes is how much ink it takes. In the simulation the press colour still moves a little between settings, because the inks absorb slightly differently, and more when a setting runs over the ink limit and C, M and Y are cut. For house navy `#1D2A3E` on FOGRA39, for example, the shift is ΔE 9.0 with **UCR** and ΔE 7.9 with **Heavy**.

## How the simulation works

The **Notes** tab explains the model in four steps:

1. **Separation.** The screen colour becomes C, M, Y from its RGB values, and black generation moves part of the shared grey into K.
2. **Ink limit.** If C + M + Y + K is above the condition's limit, C, M and Y are scaled down together and K is kept, as a profile does.
3. **Press.** Dot gain raises each tint. With compensation on, the separation is thinned beforehand so the press lands on the intended tint.
4. **Paper and inks.** The inks are combined, with small unwanted absorptions, between the paper white and the black point, so full coverage reaches the black point exactly.

The difference between the screen colour and the simulation is measured with ΔE2000:

| ΔE2000 | Reading |
|---|---|
| Under 1 | **Imperceptible**: no visible shift |
| 1 to 2 | **Very close** |
| 2 to 5 | **Close match** |
| 5 to 10 | **Noticeable** |
| 10 and above | **Distinct** |

## Proof

**Proof** is the tab that opens first.

- **The verdict.** The size of the shift and what changes, for example "ΔE 5.4 — a noticeable shift on FOGRA39 coated paper: the press version is slightly darker and duller, and the hue turns 14° toward cyan." The second sentence gives the lightness, chroma and hue differences and names the paper white and black point as the lightest and darkest the condition prints. It adds when your colour is lighter than the paper, and when the separation runs over the ink limit.
- **Side by side.** Two cards: **Screen · sRGB** and the press simulation inside a paper frame, each with "Aa", its hex and its CIELAB values.
- **The shift · tap to copy.** Six tiles: **ΔE 2000** (with its reading), **ΔL\***, **ΔC\***, **Δh**, **Simulated hex** and **As sent**. Select a tile to copy its value; **As sent** copies the `device-cmyk()` value.
- **Your colour under every condition.** A table of all six conditions, with the simulated colour on its paper, the **ΔE 2000**, the **Reading** and the **Ink total** against that condition's limit, for example "150 / 330%". Select a row to switch to that condition.

## Separation

- **The verdict.** What is sent and whether it fits the limit, for example "Sent to FOGRA39 coated as C 100 M 34 Y 12 K 4 — 150% ink, inside the 330% limit. Heavy GCR would need 141%." When it runs over, it says how much C, M and Y are cut and that the deepest tones print lighter than intended. The second sentence gives the largest dot gain and whether compensation handles it.
- **As sent · the file values.** Bars for **Cyan**, **Magenta**, **Yellow** and **Black**.
- **On press · after dot gain.** The same bars after dot gain, each with a dashed tick at the value as sent and the rise in points, for example "+11".
- **Total area coverage · 0–400%.** A bar with the ink total against the limit, a reading of **Within limit** or **Over by** a number of points, and a sentence. When the colour runs over, the bar shows the total before the cut as a dashed outline and suggests more GCR or accepting lighter shadows.
- **Every black generation for** your colour. A table with the separation, total and **Within** or **Over by** for each of the four settings. Select a row to use that setting.

## Test chart

**Test chart** proofs 24 colours around yours, and any image you give it.

- **The verdict** counts the patches that shift more than the threshold on this condition and names the row with the most. The second sentence names the worst patch, with its screen and press colours, and the closest.
- **Drop or paste an image here.** Drop an image on the area, paste one while the panel has focus, or select **Choose file**. **Clear** removes it. Images of up to 2 megapixels are proofed at full size; larger ones are scaled down first. Nothing leaves your device.
- **Flag shifts above.** The threshold, from ΔE 1 to 20 in steps of 0.5.
- **Show.** **Screen / press** shows each patch as the screen colour on top and the press simulation below; **Shift map** shows each patch's ΔE instead.
- **Four rows of six patches:**
  - **Lighter and darker**: OKLCH lightness −24, −16, −8, +8, +16 and +24 (in hundredths);
  - **Less and more saturated**: chroma × 0.25, 0.5, 0.75, 1.15, 1.3 and 1.5;
  - **Hue either side**: −30°, −20°, −10°, +10°, +20° and +30°;
  - **Mixed**: lighter and softer, lighter and richer, darker and softer, darker and richer, **Yours**, and a grey at the same lightness.

  Each row heading counts its patches over the threshold. Patches over the threshold are marked **Over**. Select a patch to proof it on its own.

### Proofing an image

When you add an image, the tab switches to **Test chart** and shows three versions side by side:

- **Original**;
- **Press ·** the condition, the image as it might print;
- **Shift map · ΔE >** the threshold, where pixels that shift more than the threshold are pink over a dimmed grey copy.

While it works, the tool shows "Proofing…" with a percentage. A line underneath gives the file name, its size, the size it was proofed at and the share of pixels that shift more than the threshold. Changing the press condition, black generation or compensation proofs the image again; changing the colour does not. Moving the threshold redraws only the shift map.

## Notes

**Notes** repeats that this is a model for intuition, not ICC colour management, explains the four steps of the model (see [How the simulation works](#how-the-simulation-works)) with the chosen condition's numbers, and lists the **Condition constants · approximate** for all six conditions, with the chosen one marked.

## Walkthroughs

### Check a brand colour before print

1. Type your colour into **Colour**.
2. Choose the **Press condition** your printer uses. Ask them; FOGRA39 is common in Europe, GRACoL and SWOP in the US.
3. Read the verdict on **Proof** and compare the two cards.
4. Read the table under the cards to see which conditions shift it least.

For the starting blue, `#0085CA`, FOGRA39 shows a **Noticeable** shift (ΔE 5.4), while GRACoL 2013 coated is a **Close match** (ΔE 2.2).

### Bring a rich black inside the ink limit

1. Type `000000` into **Colour**, or select the black swatch.
2. Set **Black generation** to **UCR** and open **Separation**.
3. The verdict says the separation totals 384%, over FOGRA39's 330% limit, so C, M and Y are cut by 18%, and that Heavy GCR would need 100% and stay inside it.
4. Select **Heavy GCR** in **Every black generation**. The reading becomes **Within limit**.

### See which parts of a photo will shift

1. Open **Test chart** and drop your image on the drop area.
2. Wait for "Proofing…" to finish, then compare **Original** with the press version.
3. Read the **Shift map**: pink marks the pixels that shift more than the threshold. Typically these are bright blues, greens and saturated oranges.
4. Change **Press condition** to compare conditions, or move **Flag shifts above** to change what counts.
5. To keep the result, choose **Export** › **Proofed image · PNG**.

## Controls

| Control | What it does | Values or range | Default |
|---|---|---|---|
| **Colour** | The colour to proof. | Hex, CSS names, CSS colour functions | The colour you opened with, or `#0085CA` |
| Starting swatches | Proof a house colour. | 6 swatches | — |
| **Press condition** | Paper, black point, dot gain and ink limit. | 6 conditions | **FOGRA39 coated** |
| **Black generation** | How much grey goes to K. | **UCR**, **Light**, **Medium**, **Heavy** | **Medium** |
| **Compensate for dot gain, as a profile would** | Thins the separation before sending. | On or off | On |
| Condition rows (**Proof**) | Switch the condition. | 6 rows | — |
| Setting rows (**Separation**) | Switch the black generation. | 4 rows | — |
| **Flag shifts above** | The threshold for the chart and the shift map. | ΔE 1 to 20, steps of 0.5 | ΔE 5 |
| **Show** | Patches as colours or as ΔE. | **Screen / press**, **Shift map** | **Screen / press** |
| Patches | Proof that colour on its own. | 24 patches | — |
| Drop area, paste, **Choose file** | Loads an image. | Image files | — |
| **Clear** | Removes the image. | — | — |
| Tabs | Switch the view. | **Proof**, **Separation**, **Test chart**, **Notes** | **Proof** |

## Outputs and exports

The footer holds **Copy device-cmyk()**, **Share link**, **Save proof** and **Export**.

| Output | Format | What it contains |
|---|---|---|
| **Copy device-cmyk()** / **CSS · device-cmyk() with hex fallback** | CSS | A comment naming the condition, black generation and compensation, then a `.brand` rule with the hex and, below it, `device-cmyk()` with the values as sent. Browsers that do not support `device-cmyk()` keep the hex line. |
| **Channel values as sent** | Text | For example `C100 M34 Y12 K4`. |
| **Simulated hex** | Text | The press simulation, for example `#2581AC`. |
| **JSON** | JSON | The colour; the condition with its paper white, black point, dot gain, ink limit and `approximate: true`; the black generation; whether compensation is on; the separation intended, as sent and on press, with the total, the total before the cut and the cut; the `device-cmyk()` value; the simulated hex; the ΔE2000 and its reading; the lightness, chroma and hue shift; and a note that this is not ICC colour management. |
| **Test chart CSV · 24 patches** | CSV | One row per patch with the columns `row`, `patch`, `screen`, `press`, `delta_e` and `over`. |
| **Proofed image · PNG** | PNG download | Only while an image is proofed: the press version, named after the image and condition, for example `photo-fogra39-proof.png`. |
| **Share link** | A URL | This page with `?ctool=softproof`, the colour, condition, black generation, compensation (when off) and the tab. |
| **Save proof** | An item in your Library | Named, for example, "Soft-proof · #0085CA on FOGRA39 coated paper", with the screen and simulated colours, the condition, black generation, values as sent and ΔE2000. |

The **Open in another tool** menu offers **Pantone & Named Lookup** (the nearest Pantone chip), **Color Inspector**, **Color Formulation** (a paint mix) and **Color Space Converter** (34 notations, CMYK included), all with your colour.

## Links

| Key | What it sets | Values |
|---|---|---|
| `ctool` | Opens this tool. | `softproof` |
| `color` | The colour to proof. | A hex code without `#` |
| `press` | The press condition. | `fogra39`, `gracol`, `swop`, `fogra52`, `news`, `rag` |
| `gcr` | The black generation. | `ucr`, `light`, `medium`, `heavy` |
| `comp` | Turns dot-gain compensation off. | `0` |
| `ctab` | The tab to open on. | `proof`, `separation`, `chart`, `notes` |

Links made for the earlier tool still work: `press=uncoated` opens **FOGRA52 uncoated**, `press=newsprint` opens **Newsprint** and `press=fineart` opens **Fine-art rag**.

## Accuracy and limits

- **A model, not ICC colour management.** The separation is a simple formula, and the conditions are hand-set approximations of paper colour, black point, dot gain and ink limit, named after common standards. They are not the standards' characterisation data and use no ICC profiles.
- **The CMYK values are a starting point.** Real separations depend on the printer's profile, rendering intent, black generation and more. Discuss them with your printer, and ask for a contract proof for colour-critical work.
- **`device-cmyk()` is not rendered by browsers yet.** The CSS export keeps the hex line for that reason.
- **Your screen matters.** The calibration of your own display changes what you see.
- **Images are proofed in your browser** at up to 2 megapixels and are not uploaded.

## Related

- [Colour Tools documentation](README.md)
- [Open the Colour Tools and work in their panels](launcher-and-panels.md)
- [Colour Tools dashboard](colour-tools-dashboard.md)
- [Pantone & Named Lookup](pantone-and-named-lookup.md) — the nearest printed chip
- [Color Formulation](colour-formulation.md) — how a colour might be mixed in paint
- [Color Space Converter](colour-space-converter.md)
- [Library Kit](../../../../../kits/library-kit/README.md) — where saved proofs go
