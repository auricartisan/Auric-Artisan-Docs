---
title: Collage Maker — Build and edit a collage
description: Add pictures, set up the canvas, select and edit pictures, use the layers list, and undo or redo any step.
product: Website › Tools › Image and file tools › Collage Maker
updated: 2026-09-25
---

# Build and edit a collage

Everything in this guide happens on the **Studio** tab.

## Add pictures

1. Drop one or more image files onto the **Drop pictures** box in the left-hand panel. You can also drop them straight onto the canvas, or select the box (or press `Enter` or `Space` while it has focus) to open a file chooser that accepts several files at once.
2. Wait for the message at the bottom of the screen. It reads **Added** followed by the file name, or **Added 4 pictures** for a batch.

What happens to each picture:

- It is centred on the canvas.
- It keeps its own pixels. If it is larger than 42% of the canvas width or height, it is scaled down to fit inside that box; a smaller picture stays at 100%.
- It is added on top of the others and becomes the selected picture.
- It appears at the top of the **Layers · top first** list, with a thumbnail, its file name, its size in pixels and its current scale.

Any image type your browser can open is accepted; the box names JPG, PNG, WebP and GIF. Files that are not images are ignored. If a file cannot be decoded, a message reads **Could not read** followed by its name, and the other files in the batch are still added. Adding a batch is one history step.

## Set up the canvas

The controls under **The canvas** apply to the whole collage.

| Control | What it does | Range | Default |
|---|---|---|---|
| **Shape** | Sets the canvas size. Every shape is 1200 pixels wide | 4 : 3, 1 : 1, 3 : 2, 16 : 9, 9 : 16, 2 : 3 | 4 : 3 — 1200 × 900 |
| **Padding** | The margin between the canvas edge and the block of grid cells. Used only when arranging in a grid | 0 to 120 px | 24 px |
| **Gap** | The space between grid cells. Used only when arranging in a grid | 0 to 80 px | 8 px |
| **Corner radius** | Rounds the corners of the canvas. The export is clipped to the rounded shape | 0 to 80 px | 18 px |
| **Transparent background** | When ticked, empty areas are transparent. When cleared, the background is white | On or off | On |
| **Centre and rule-of-thirds guides** | Shows thirds lines on the canvas, and dashed lines through the centre of the selected picture | On or off | On |
| **Snap to a 10 px grid** | While dragging, the picture's centre lands on a multiple of 10 px | On or off | On |

Above these controls, **size** and **background** repeat the current canvas size and background (transparent, or the colour in use).

Changing the shape does not move or resize any picture. Pictures that were near the edge of a larger canvas can end up partly outside a smaller one; the **outside the canvas** card tells you when that happens.

The guides are drawn only on screen. They never appear in an export.

## Select a picture

- Click a picture on the canvas. Where pictures overlap, the click selects the one on top.
- Or select a row in the **Layers · top first** list. This is the only way to select a hidden picture, because hidden pictures cannot be clicked on the canvas.
- Click an empty part of the canvas to clear the selection.

The selected picture has a gold outline and four square corner handles. Its controls appear under **The selected picture**; when nothing is selected that area reads **nothing selected**.

## Move, resize and nudge

| Action | How |
|---|---|
| Move | Drag the picture. With snapping on, its centre lands on a multiple of 10 px |
| Resize | Drag a corner handle; the picture scales around its centre, keeping its proportions, from 2% to 800% |
| Nudge 1 px | Click the canvas so it has keyboard focus, then press an arrow key |
| Nudge 10 px | Hold `Shift` and press an arrow key |
| Remove | Press `Delete` or `Backspace` while the canvas has focus, or select **Remove** |

Each drag is one history step, recorded when you let go. Each arrow-key press is one step. Arrow-key nudges are exact and are not snapped to the grid.

## Change the selected picture

The controls under **The selected picture** change only the selected picture.

| Control | What it does | Range |
|---|---|---|
| **Scale** | Size relative to the picture's own pixels | 2% to 400% |
| **Rotation** | Turns the picture about its centre | −180° to 180° |
| **Opacity** | How see-through the picture is | 0% to 100% |
| **Bring to front** | Moves it to the top of the stack | — |
| **Send to back** | Moves it to the bottom of the stack | — |
| **Centre** | Moves its centre to the centre of the canvas | — |
| **Duplicate** | Adds a copy 24 px to the right and 24 px down, and selects the copy | — |
| **Flip across** | Mirrors it left to right; select again to undo the flip | — |
| **Flip down** | Mirrors it top to bottom | — |
| **Hide** | Hides it from the canvas, the measurements and the export. The button then reads **Show** | — |
| **Remove** | Takes it off the canvas. Undo brings it back | — |

Sliders show the value as you drag. The history step is recorded when you release the slider.

## The layers list

**Layers · top first** lists every picture in the order it is painted, with the top of the stack first. Each row shows:

- a thumbnail;
- the file name (hover to see the full name);
- the picture's own size and its current scale, for example `3024×4032 · 12%`;
- a dot, or **hidden** for a hidden picture.

Select a row to select that picture.

## Arrange in a grid, or start again

- **Arrange in a grid** tries every number of columns for the visible pictures, measures each arrangement, and applies the one that covers the most canvas. It uses the fitting choices on the **Layout** tab. A message reports the grid and its coverage, for example **Arranged 2 × 2 — 88.1% covered. Undo puts them back.** See [Arrange pictures in a grid](arrange-in-a-grid.md) to choose an arrangement yourself.
- **Clear the canvas** removes every picture. It is one history step, so **Undo** brings them all back.

## Undo and redo

The **History** group has **← Undo** and **Redo →**. The note under them says how many steps you can go back, for example **5 steps back, to the start.**

- Every change is recorded: adding pictures, moving, resizing, each slider release, every button, changing the shape, padding, gap, corner radius or background, arranging, clearing, removing and loading a session.
- A removed picture comes back with the step that removed it.
- The history holds up to 60 steps. Older steps are dropped once you pass that.
- Making a new change after undoing clears the redo steps.
- Keyboard: `Ctrl` + `Z` undoes; `Ctrl` + `Shift` + `Z` or `Ctrl` + `Y` redoes. On a Mac, `Cmd` works in place of `Ctrl`. The shortcuts do nothing while a slider, menu or text box has focus.

> **Tip:** When the canvas itself has keyboard focus, one press of the undo or redo shortcut can move two steps. If you want exactly one step, use the **Undo** and **Redo** buttons, or click outside the canvas before using the keyboard.

Switching **Centre and rule-of-thirds guides** and **Snap to a 10 px grid** is not recorded, because neither changes the collage.

## What you should see

After these steps your pictures sit where you want them, the layers list shows their order, and the **canvas covered**, **overlapping** and **outside the canvas** cards describe the collage exactly as it will export. To export it, see [Export, copy and save sessions](export-and-sessions.md).
