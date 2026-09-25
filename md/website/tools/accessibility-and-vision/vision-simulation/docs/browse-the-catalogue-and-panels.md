---
title: Vision Lab — Browse the Catalogue and panels
description: Find conditions in the Catalogue, open them as floating panels, arrange panels with Vision Control, and feed them an image.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Browse the Catalogue and panels

The **Catalogue** shows every condition as a card. Each card runs the same ten reference swatches, so the differences between two cards are real differences between two conditions. Selecting a card opens that condition as a floating panel, where you can run your own image through it and use every advanced control.

## The Catalogue bar

| Control | What it does |
| --- | --- |
| **Search simulations…** | Filters cards by name. `/` jumps to it; `Esc` clears it. **Clear** empties it. |
| Scope button | Shows the current category and its count, for example "All conditions 17"; opens a menu of categories |
| **Filter** | Opens the **Kind** and **Level** filters, with **Done**; a badge counts active filters |
| Count | How many conditions are showing, for example "17 of 78" |
| **About this catalogue** | Explains how the cards are built |
| **Copy link** | Copies a link to the whole current workspace (see [Links, saving and exports](links-saving-and-exports.md)) |
| Daily tally | On the free plan, how many simulations you have opened today out of 25 |

**Kind** offers **All**, **Per-colour** and **Field**; **Level** offers **All**, **Basic** and **Advanced**.

### Why do I see 17 of 78?

The **Level** filter follows the site-wide Simple and Advanced preference. **Basic** shows the 17 per-colour conditions, **Advanced** shows the 61 field conditions, and **All** shows all 78. On a first visit the Catalogue usually opens at the basic level. Select **Filter**, then **Level** › **All**, to see everything.

### Categories

A row of tabs narrows the cards: **All conditions**, **Favourites**, the 11 categories, **Source image** and **Open panels**. Each shows its count at the current filter. The lab remembers the last category you browsed.

If nothing matches, the grid says "Nothing matches that. No condition matches every filter you have on." Select **Clear the filters**.

## The cards

Each card shows:

- the severity score (1 to 10), an estimated visual-impact score, not a clinical grade;
- the category and the condition's name;
- a short description, such as "Green-cone absent";
- its kind (**Per-colour** or **Field**) and level (**Basic** or **Advanced**);
- its prevalence, such as "~1% males" or "Educational";
- the ten reference swatches as the condition affects them;
- a star to add it to **Favourites**.

Select a card, or focus it and press `Enter` or `Space`, to open its panel. `Shift` + click or `Ctrl` + click opens a second copy of a panel that is already open.

## Daily limit on the free plan

On the free plan you can open 25 simulations a day from the Catalogue. The tally in the bar ("0 / 25", read as "0 of 25 simulations used today") counts them. After the 25th, opening another card shows an upgrade prompt: "You've run your 25 free simulations for today. Upgrade for unlimited runs — every simulation stays free, this just lifts the daily cap." Paid plans have no daily cap. The tally counts simulation cards you open from the Catalogue; working in the Workbench is not counted.

## Floating panels

A panel is a window over the page with the full simulation for one condition. You can move it and open up to five at once.

### Title bar

| Button | What it does |
| --- | --- |
| **Link panel** | Syncs controls with other linked panels |
| **Duplicate** | Opens another instance of this simulation |
| **Pin panel** | Prevents the panel being replaced when you go over the panel limit |
| **Minimize** | Sends the panel to the dock of minimised panels |
| **Maximize panel** | Maximises or restores the panel |
| **Close panel** | Closes it |

When five panels are open, opening a sixth replaces the oldest panel that is not pinned. If all five are pinned, nothing more opens until you close one.

### Panel controls (colour-vision panels)

Controls vary by condition. A colour-vision panel, such as Deuteranopia, has:

| Control | What it does | Range or options | Default |
| --- | --- | --- | --- |
| **Base color** | The colour to simulate: a picker, a hex field and **Random** | Any colour | `#D3AF37` |
| **Severity** | How strongly the condition is expressed | 0–100% | 100% |
| **Perceptual severity curve** | Applies a perceptual curve so mid severities feel natural | On, off | Off |
| **Multi-pass deep** | Runs two passes of the simulation, which exaggerates the effect | On, off | Off |
| **Model** | The simulation model | **Brettel (1997)**, **Viénot (1999)**, **Machado-like** | Brettel (1997) |
| Workflow preset | Applies recommended parameters and colour-appearance settings | Custom (no preset), Default, Beginner mode, Material testing, Color matching, Print proof, Photography (D65) | Custom |
| **Copy HEX** / **Copy CSS** | Copies the reference hex, or CSS variables for the reference and simulated colours | — | — |
| **Show advanced controls** | Reveals cone-weight controls and exporters | On, off | Off |
| Cone channel weights | Scale the L, M and S cone signals | 0 to 2 each | 1 |
| **Export all CVD** | Downloads a JSON file of the base colour under each colour-vision type, at several severities | — | — |
| Illuminant | The standard illuminant used for the chromaticity maths | Several | D65 |

The **Color appearance (CAM)** section models how the colour looks in context:

| Control | Options or range | Default |
| --- | --- | --- |
| CAM model | CAT16 adaptation, CAM16-UCS perceptual, CIECAM02 surround, Hunt-Stevens brightness | CAT16 adaptation |
| White point | D65, D50, A, F2, F7, F11, and warm, neutral and cool LED | D65 — Daylight (6500 K) |
| Correlated color temperature | 1,667–25,000 K | 6517 K |
| Perceived brightness | 5–400% | 100% |
| Observer | 2° (small or close field), 10° (large field) | 2° |
| Surround | Average (typical room), Dim (low-light), Dark (theatre) | Average |
| Viewing distance | Near (50 cm or less), Normal (50–80 cm), Far (80 cm or more) | Normal |

**Snapshots** save the panel's whole state under a name ("Name (e.g. Version A)", then **Save**), kept in this browser. **Recent changes** lists your edits, with **Undo last** and **Clear**.

### Panel readouts

- **Reference** and the simulated colour, each with HEX, RGB and CIE xy values, and the **ΔE2000** and **ΔE76** between them.
- Tabs:
  - **Chromaticity** — a CIE 1931 xy diagram with the reference, the simulation and the drift between them, plus figures for xy drift, saturation collapse, lightness change and angle.
  - **Metrics** — RGB drift, the LMS cone response, drift over time, and reference and simulated HSL.
  - **Image** — "Run your own image through it": **Choose image** and **Clear**, with **Original** and **Simulated** side by side. Every control applies to the image just as it does to the colour.
  - **Mindmap** — how the condition relates to others.
  - **Model audit** — the steps from input to output (linear-light conversion, disease transform, colour appearance, validation) and what each model covers.

Field-condition panels have their own controls for the condition's effect.

## Vision Control

When panels are open, a dock titled **Vision Control** appears. It has:

- arrangement buttons: **Tile in a grid**, **Split left and right**, **Split top and bottom**, **Cascade with an offset** and **Stack them centred**;
- one tab per open panel, to bring it forward;
- a **More panel actions** menu: **Sync all panels**, **Minimize all**, **Restore all**, **Export a comparison PNG**, **Open the verification panel**, and **Close all but pinned**.

Minimised panels wait in a separate dock ("Minimized panels"); select one to restore it, or its **×** to close it. Press `T` to tile all panels, and `1` to `5` to bring a panel forward.

## The source image

One image can feed every panel. Open the **Source image** tab (or the **Image** button in the category bar). The card is titled **Universal Source Image** and says "One image feeds every simulation. A default sample is loaded for you."

| Control | What it does | Options | Default |
| --- | --- | --- | --- |
| Drop area | Drop, paste, or click to upload an image | Any image file | A built-in reference chart |
| **Apply to all panels** | Sends the image to every open panel | — | — |
| **Quality** | The working size the image is processed at | Fast · 1024px, Balanced · 1600px, Full · 4096px | Fast · 1024px |
| **Auto-apply to new panels** | New panels receive the image automatically | On, off | On |
| **Pause auto** / **Clear** | Pause auto-apply, or remove the image | — | — |

**What this image loses** shows the image's size and working size, and ranks the conditions that change this image most, with **Open most-affected →**.

**Samples** offers 15 images: Forest scene, Skin tones, Eye, Farmers market, Coastal village, Rainy city, India · Himalayas, India · Kerala, India · Rajasthan, India · Tea hills, China · Guilin, China · Zhangjiajie, China · Yunnan, Thrown paint and Abstract drawing. **Test charts** offers Color bars, Spectrum, Red–Green and Chromatic grid.

Images you add are processed in your browser and are not uploaded.
