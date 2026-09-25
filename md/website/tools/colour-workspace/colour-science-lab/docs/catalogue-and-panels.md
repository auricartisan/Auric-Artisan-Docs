---
title: Color Science Lab — The Catalogue and its panels
description: Find tools in the Catalogue, and use every control and tab of a Color Science Lab tool panel.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# The Catalogue and its panels

The **Catalogue** view lists the lab's 45 tools as cards. Selecting a card opens that tool as a floating panel over the page. All 45 panels share one layout, so once you know one, you know them all; the tool you choose sets the defaults (model, colour space and theory) and what the canvas draws.

## The filter bar

| Control | What it does |
| --- | --- |
| **Color Lab** | Reloads the page. |
| Search box | *Search tools, models, spaces, illuminants...*. Matches tool names, summaries, tags, domains, default models and spaces, and, for colour-space and theory tools, the names and details of every space and theory. Results update a moment after you stop typing. |
| **Clear** | Empties the search. |
| Domain list | **All**, the eight domains, **Favorites**, **Compare**, **Analytics** and **Open Panels**. |
| **Level** | **Basic** (20 Foundation tools), **Advanced** (25 Research tools) or **Both** (all 45, the default). |
| Count | Cards shown out of the total, for example **20 of 45**. |
| **Copy link** | Copies the page address. |
| Quick start button | Shows or hides the quick start note. |

The **Level** setting is shared with the site-wide complexity mode (the Advanced Kit), so changing it in one place changes it in the other.

The domains are **Colorimetry**, **Chromatic Adaptation**, **Spectral Analysis**, **Appearance Models**, **Perceptual Spaces**, **Color Spaces**, **Theory and History** and **Gamut and Rendering**. **Compare** and **Analytics** are described in [Catalogue Compare and Analytics](catalogue-compare-and-analytics.md); **Open Panels** in [Arrange, link, save and export](arrange-link-save-export.md).

## Tool cards

Each card shows the domain, the tool name, a strip of colours computed for that domain, a summary, and tags: the domain, **Basic / Foundation** or **Advanced / Research**, up to three topic tags, and **● Open** when it has a panel.

- Select a card to open the tool, or to bring its panel forward.
- Hold `Shift`, `Ctrl` or `Cmd` while selecting to open another copy.
- Select the star to add or remove a favourite.

The full list is in [The 45 tools](tool-list.md).

## The panel

### Controls (left column)

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Sample color** | The colour under study: colour well, HEX box, **Random**. | Any sRGB colour | #D3AF37 |
| **Compare color** | A second colour for difference metrics. | Any sRGB colour | #2FA7D8 |
| **Model** | The model for the tool's domain. | Depends on the domain (see below) | The tool's default |
| **Color space / standard** | The space used for coordinate readouts and the dossier. | 63 colour spaces | The tool's default |
| **Theory / observer** | The theory or observer framework. | 24 theories and models | The tool's default |
| **White points: Source** | Reference white for the sample. | A, B, C, D50, D55, D60 / ACES, D65, D75, DCI, E, F2, F7, F11 | D65 |
| **White points: Target** | Reference white for the result. | Same list | D50 |
| **Experiment strength** | How strongly the model is applied to the result preview. | 0 to 100 % | 72 % |
| **Color temperature** | A light temperature used by spectral tools and the temperature metric. | 1800 to 12000 K, step 100 | 6500 K |
| **Show reference guides** | Draws guides on the canvases. | On or off | On |
| **Apply adaptation preview** | Turns the result preview on or off (off shows the sample unchanged). | On or off | On |

The HEX boxes accept a partial value while you type and apply it when it is complete, when you press `Enter`, or when you leave the box.

### Models by domain

| Domain | Models |
| --- | --- |
| Colorimetry | XYZ + Lab, xyY, u'v'Y, Delta E, CIE 1931 observer, CIE 1964 observer |
| Chromatic adaptation | XYZ scaling, Von Kries, Bradford, CAT02, CAT16, CMCCAT97, CMCCAT2000, Sharp CAT, Hunt-Pointer-Estevez, Bianco-Schettini, Bianco-Schettini PC |
| Spectral | Visible spectrum, Blackbody, Emission lines, Metamerism, CIE daylight locus, Planckian locus, Standard observer |
| Appearance | Fairchild appearance, Hunt, Nayatani, RLAB, LLAB, CIECAM02, CIECAM16, CAM16, CAM02-UCS, HDR appearance, Surround study, iCAM image appearance |
| Perceptual | CIELAB, CIELCh(ab), CIELUV, DIN99, Jzazbz, Oklab, Oklch, IPT, ICtCp, CAM02-UCS, CAM16-UCS |
| Color spaces | Full space atlas, RGB matrix profiles, Wide gamut RGB, Video component spaces, CIE family, Perceptual family, Print/process family, HDR family |
| Theory | Newton prism and wheel, Goethe, Young-Helmholtz, Hering opponent, Maxwell triangle, Munsell, Ostwald, Von Kries, Retinex, Fairchild, CIECAM02, CAM16 |
| Rendering | sRGB, Display P3, Rec.2020, ACES, ICC rendering intent, Gamut mapping, Tone map, PQ HDR, HLG HDR |

### Tabs (right column)

| Tab | What it shows |
| --- | --- |
| **Experiment** | The tool's main canvas, and three swatches: **Reference** (the sample), **Result** (the model's output) and **Compare**, each with HEX, RGB, xy and its white point. |
| **Metrics** | Twelve cards: **dE76 to compare**, **dE76 after model**, **Luma drift**, **Chroma drift**, **Lab result**, **CCT color dE**, **Source Lab**, **Active space**, **Sample coordinates** (with an in-gamut or out-of-gamut note), **Result coordinates**, **Theory model** and **Target white**. |
| **Chart** | A channel and Lab chart for the sample, result, compare and temperature colours. |
| **Graph** | A response graph for the domain, such as an adaptation response, spectral sweep, appearance curve, uniformity check, space preview, theory transform or rendering compression. |
| **Diagram** | The model path: input sample, reference white, and the domain's steps through to the output. |
| **Audit** | The tool summary; a dossier of the selected colour space; the current model, space, theory, whites and catalogue size; and tables of related spaces and theories. |

### The colour-space dossier

On the **Audit** tab, the dossier describes the space chosen in **Color space / standard** for the current sample: its family and category, a summary, the sample's coordinates in that space, an **In gamut** or **Out of … gamut** pill, key facts (primaries, white, transfer function, and for many spaces the year, standard, typical encoding and gamut area relative to sRGB), the **Conversion chain**, typical uses and notes. **This sample across 21 spaces** expands to a table of the sample's coordinates in 21 representative spaces.

## Tasks

### Adapt a colour from D65 to D50

1. Open **Bradford Adaptation** (Chromatic Adaptation).
2. Set **Sample color**. Leave **Source** on D65 and set **Target** to D50.
3. Set **Experiment strength** to 100 %.
4. Read the **Result** swatch and, on **Metrics**, **Lab result** and **dE76 after model**.

Result: the adapted colour and how far it moved.

### Read a colour in an unfamiliar space

1. Open **40+ Color Space Atlas** (Color Spaces).
2. Set **Color space / standard**, for example to *ICtCp* or *Munsell HVC*.
3. Open **Audit** and read the dossier and the conversion chain.

Result: the sample's coordinates in that space, with what the space is for.

## Related

- [The 45 tools](tool-list.md)
- [Arrange, link, save and export panels](arrange-link-save-export.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
