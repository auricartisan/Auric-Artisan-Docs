---
title: Collage Maker — Reference
description: Every tab, control, button, readout, message and file format in the Collage Maker, with ranges and defaults.
product: Website › Tools › Image and file tools › Collage Maker
updated: 2026-09-25
---

# Collage Maker reference

Address: https://auricartisan.com/tool/general/tools/collage-maker/

## Tabs

| Tab | Contents |
|---|---|
| **Studio** | Pictures, canvas settings, history, selected-picture controls, the canvas, the layers list, the readout cards |
| **Layout** | Fitting options, apply buttons, the arrangement table and drawings of the three best arrangements |
| **Measure** | Worked examples of how coverage, overlap and off-canvas area are measured |
| **Data** | The list of every figure and its source, filterable by status; the tab label shows the count (12) |
| **Export** | Export scale, JPEG quality, save, copy and session buttons, file sizes, the reading |
| **Reference** | Sources, each marked **Runs** or **Withdrawn**, and the arithmetic table |

Links in the page text (for example **Measure** or **Data** in a note) switch to that tab.

## Studio tab — Pictures

| Control | What it does | Accepts |
|---|---|---|
| **Drop pictures** box | Adds pictures by drag and drop, or opens a file chooser when selected or when `Enter` or `Space` is pressed | Any image type the browser opens; JPG, PNG, WebP, GIF named |
| The canvas | Also accepts dropped image files | As above |

Several files can be added at once. New pictures are centred, scaled down to fit within 42% of the canvas width and height (never enlarged), placed on top and selected.

## Studio tab — The canvas

| Control | Values or range | Default |
|---|---|---|
| **Shape** | 4 : 3 — 1200 × 900; 1 : 1 — 1200 × 1200; 3 : 2 — 1200 × 800; 16 : 9 — 1200 × 675; 9 : 16 — 1200 × 2133; 2 : 3 — 1200 × 1800 | 4 : 3 |
| **Padding** | 0 to 120 px, step 1 | 24 px |
| **Gap** | 0 to 80 px, step 1 | 8 px |
| **Corner radius** | 0 to 80 px, step 1 | 18 px |
| **Transparent background** | On (transparent) or off (white) | On |
| **Centre and rule-of-thirds guides** | On or off; screen only | On |
| **Snap to a 10 px grid** | On or off; applies to dragging | On |
| **size** (readout) | Current canvas size | 1200 × 900 |
| **background** (readout) | transparent, or the colour in use | transparent |

Padding and gap affect only grid arrangements. The corner radius clips the canvas and every export.

## Studio tab — History

| Control | What it does |
|---|---|
| **← Undo** | Steps back one change; disabled when there is nothing to undo |
| **Redo →** | Steps forward one undone change; disabled when there is nothing to redo |
| Note | **Nothing to undo yet**, or the number of steps back to the start |

Up to 60 steps are kept. A new change clears the redo steps.

## Studio tab — The selected picture

Shown when a picture is selected; otherwise the area reads **nothing selected**.

| Control | Range or effect | Default for a new picture |
|---|---|---|
| **Scale** | 2% to 400%, step 1% | Whatever fits 42% of the canvas, at most 100% |
| **Rotation** | −180° to 180°, step 1° | 0° |
| **Opacity** | 0% to 100%, step 1% | 100% |
| **Bring to front** | Moves the picture to the top of the stack | — |
| **Send to back** | Moves the picture to the bottom | — |
| **Centre** | Centres the picture on the canvas | — |
| **Duplicate** | Adds a copy offset 24 px right and 24 px down, and selects it | — |
| **Flip across** | Mirrors left to right (toggles) | Not flipped |
| **Flip down** | Mirrors top to bottom (toggles) | Not flipped |
| **Hide** / **Show** | Hides or shows the picture | Shown |
| **Remove** | Removes the picture | — |

## Studio tab — Other buttons

| Button | What it does |
|---|---|
| **Arrange in a grid** | Applies the arrangement with the highest measured coverage, using the **Layout** tab's fitting choices |
| **Clear the canvas** | Removes every picture; undoable |

## Studio tab — Canvas and layers

| Element | What it shows or does |
|---|---|
| Canvas heading | **Canvas ·** width × height, and **measured at full size** or **measured at** the reduced size |
| Note beside **The canvas** | **no pictures**, or the number of pictures and the canvas size |
| Canvas | Click to select, drag to move, drag a corner handle to resize, click empty space to deselect |
| **Layers · top first** | One row per picture, top of the stack first: thumbnail, file name, own size and scale, visibility |

Pointer resizing by a corner handle ranges from 2% to 800%.

## Studio tab — Readout cards

| Card | Meaning |
|---|---|
| **canvas covered** | Share of canvas pixels painted by pictures (measured from pixels) |
| **overlapping** | Share of canvas pixels painted by two or more pictures |
| **outside the canvas** | Share of picture area beyond the edges; warns above 0.1% |
| **history** | Undo steps available |
| **the old readout said** | Sum of picture areas divided by canvas area; for comparison only |

Percentages are shown to one decimal place.

## Layout tab

| Control | What it does | Default |
|---|---|---|
| **Fit inside the cell** | Scales pictures so all of each is inside its cell | Selected |
| **Fill the cell, crop** | Scales pictures to cover their cells; the excess is not trimmed | — |
| **Enlarge a small picture to fill its cell** | Allows scaling above 100% of a picture's own pixels | Off |
| **Apply** buttons | One per valid arrangement, labelled columns × rows | — |

Arrangement table columns: **Arrangement**, **Cell**, **Covered**, **Overlap**, **Off-canvas**, **What happened**. One row per column count from 1 to the number of visible pictures. The three highest-covering arrangements are drawn under **The grid, and what it leaves**, each with **covered** and **cells used**.

Applying an arrangement moves each visible picture to the centre of its cell, sets its scale, and sets its rotation to 0°. It is one history step.

## Measure tab

| Element | Contents |
|---|---|
| **What is measured** | covered: pixels; overlapping: pixels; off-canvas: geometry; arrangements: laid out |
| **Withdrawn** buttons | **Bootstrap CI** and **Batch coverage** scroll to the notes on two withdrawn features |
| **One number for three different collages** | Three live panels, **Stacked**, **Spread out**, **Dragged off the canvas**, with **it said** and **really** |
| Further panels | How undo records history, what an export contains, withdrawn features, and what stayed unchanged |

## Data tab

Status filter buttons: **All**, **Measured**, **Computed**, **This tool's choice**, **Absent**, each with a count. Each entry expands to an explanation; stand-in and absent entries add **what it would take**.

## Export tab

| Control | Range or effect | Default |
|---|---|---|
| **Scale** | 0.25× to 4×, step 0.25 | 1.00× |
| **JPEG quality** | 0.10 to 1.00, step 0.01 | 0.92 |
| **size** (readout) | Export size in pixels | 1200 × 900 |
| **background** (readout) | transparent or the colour in use | transparent |
| **Save the PNG** | Downloads `collage.png` | — |
| **Save a JPEG** | Downloads `collage.jpg` at the chosen quality | — |
| **Copy to the clipboard** | Copies a PNG at the export scale | — |
| **Save the session** | Downloads `collage-session.json` | — |
| **Load a session** | Opens a chooser for a `.json` session file | — |
| **Save the reading** | Downloads `collage-reading.json` | — |

The table under **What leaves this page** lists **PNG**, **JPEG** and **Session JSON** with what each carries, its measured size for your collage, and what it is good for.

## File formats

### collage.png and collage.jpg

| Property | Value |
|---|---|
| Size | Canvas size × **Scale**, rounded to whole pixels |
| Colour | 8 bits per channel, as the browser draws the canvas |
| Transparency | PNG keeps it; JPEG cannot store it |
| Contents | Visible pictures, background, rounded corners; no guides, outlines or handles |

### collage-session.json

```json
{
  "tool": "Auric Artisan — collage",
  "canvas": {
    "w": 1200, "h": 900, "aspect": "4:3",
    "pad": 24, "gap": 8, "radius": 18,
    "background": "transparent"
  },
  "pictures": [
    {
      "name": "harbour.jpg", "cx": 300, "cy": 225, "bw": 4032, "bh": 3024,
      "scale": 0.1339, "rot": 0, "opa": 1,
      "flipX": false, "flipY": false, "visible": true
    }
  ]
}
```

| Field | Meaning |
|---|---|
| `canvas.w`, `canvas.h` | Canvas size in pixels |
| `canvas.aspect` | Shape preset, for example `4:3` |
| `canvas.pad`, `canvas.gap`, `canvas.radius` | Padding, gap and corner radius in pixels |
| `canvas.background` | `transparent`, or a colour |
| `pictures[].name` | The file name the picture had |
| `pictures[].cx`, `cy` | Position of the picture's centre on the canvas, in pixels |
| `pictures[].bw`, `bh` | The picture's own width and height in pixels |
| `pictures[].scale` | Scale factor (1 is 100%) |
| `pictures[].rot` | Rotation in degrees |
| `pictures[].opa` | Opacity from 0 to 1 |
| `pictures[].flipX`, `flipY` | Mirrored across or down |
| `pictures[].visible` | Shown or hidden |

The file holds no image data. On loading, stored pictures are matched to loaded pictures by order in the stack, bottom first. The values in the example are illustrative.

### collage-reading.json

Fields: `tool`, `canvas` (`w`, `h`, `background`), `pictures` (a count), `measured` (`covered`, `overlapping`, `outsideCanvas` as fractions to four decimals, and `at`), `choices` (`neverEnlargeBeyond`, `snapStep`, `jpegQuality`), and `notHeld`. See [Export, copy and save sessions](export-and-sessions.md) for an example.

## Messages

| Message | When it appears |
|---|---|
| **Added** name / **Added N pictures** | Pictures were added |
| **Could not read** name | A file could not be decoded as an image |
| **Removed. Undo brings it back.** | A picture was removed |
| **Cleared. Undo brings every picture back.** | The canvas was cleared |
| **Arranged. Undo puts every picture back.** | An arrangement was applied from the **Layout** tab |
| **Arranged** C × R **—** N% **covered. Undo puts them back.** | **Arrange in a grid** was used |
| **No arrangement fits at this padding and gap.** | Every arrangement was refused |
| **Nothing on the canvas yet.** | Export, copy or arrange with no pictures |
| **Saved PNG** or **Saved JPG**, with a size | An image was saved |
| **The browser could not encode that.** | The browser failed to produce the image file |
| **Copied** with a size | The PNG was copied to the clipboard |
| **This browser will not take an image from the clipboard.** | The browser does not support copying images |
| **The browser refused the clipboard.** | Clipboard permission was refused |
| **Session saved. It describes the layout, not the pictures.** | A session file was saved |
| **Session applied to the** N **pictures you have loaded.** | A session was loaded onto loaded pictures |
| **Session read. Load the same pictures and it will be applied to them.** | A session was loaded with no pictures on the canvas |
| **That is not a session file this page wrote.** | The chosen file is not a valid session |
| **Reading saved.** | The reading was saved |
| **A picture in that step is no longer loaded.** | An undo or redo step refers to a picture the page no longer holds |
