---
title: Collage Maker — Troubleshooting
description: Symptoms you may meet in the Collage Maker, why they happen, and what to do.
product: Website › Tools › Image and file tools › Collage Maker
updated: 2026-09-25
---

# Troubleshooting the Collage Maker

## Pictures will not load

| Symptom | Why | What to do |
|---|---|---|
| Nothing happens after dropping a file | The file is not an image type, so it is ignored | Convert it to JPG, PNG, WebP or GIF and try again |
| **Could not read** followed by a file name | Your browser could not decode that file | Save it again as JPG or PNG in another program; HEIC and camera RAW files are not opened by every browser |
| The page slows down with many pictures | Every change is measured from pixels, once per picture for the overlap figure | Use fewer or smaller pictures, or resize very large photographs before adding them |

## A picture is in the wrong place or missing

| Symptom | Why | What to do |
|---|---|---|
| A picture cannot be clicked | It is hidden, or another picture is on top of it | Select it in the **Layers · top first** list; use **Show** or **Bring to front** |
| A picture moved partly off the canvas after changing **Shape** | Changing the shape does not move pictures | Use **Arrange in a grid**, **Centre**, or drag it back; watch the **outside the canvas** card |
| Dragging jumps in steps | **Snap to a 10 px grid** is on | Clear the switch, or use the arrow keys for 1 px nudges |
| Arrow keys scroll the page instead of nudging | The canvas does not have keyboard focus | Click the canvas once, then use the arrow keys |

## Grid arrangements

| Symptom | Why | What to do |
|---|---|---|
| **No arrangement fits at this padding and gap.** | Padding and gap leave no room for any grid | Reduce **Padding** or **Gap** on the **Studio** tab |
| A row in the **Layout** table reads **refused** | That grid's cells come out at zero or less | Reduce padding or gap, or choose a grid with fewer columns or rows |
| Every row shows the same **Covered** figure | No picture is larger than its cell, so each keeps its own size | Switch on **Enlarge a small picture to fill its cell**, or use larger pictures |
| Pictures overlap after applying a grid | **Fill the cell, crop** scales pictures past their cells without trimming them | Use **Fit inside the cell**, or check the **Overlap** column first |
| Rotated pictures became straight | Applying an arrangement sets every picture's rotation to 0° | Rotate again afterwards, or undo |

## Undo and redo

| Symptom | Why | What to do |
|---|---|---|
| One key press undid two steps | With the canvas focused, the shortcut can be handled twice | Use the **Undo** and **Redo** buttons, or click outside the canvas before pressing the shortcut |
| `Ctrl` + `Z` does nothing | A slider, menu or text box has focus | Click an empty part of the page, or use the **Undo** button |
| Early steps can no longer be undone | The history keeps 60 steps | Save a session file at points you may want to return to |
| **A picture in that step is no longer loaded.** | The step refers to a picture whose image the page no longer holds | Add the picture again |

## Exports

| Symptom | Why | What to do |
|---|---|---|
| The JPEG has dark or unexpected empty areas or corners | JPEG cannot store transparency | Clear **Transparent background** before saving a JPEG, or save a PNG |
| Part of a picture is missing from the export | It lies outside the canvas, or the rounded corners clip it | Check **outside the canvas**; reduce **Corner radius** |
| A picture looks soft in a large export | It was scaled above its own size, or the export scale enlarges it | Use a larger original, or a lower **Scale** |
| **The browser could not encode that.** | The image was too large for the browser, or encoding failed | Lower **Scale** and try again |
| **Nothing on the canvas yet.** | There are no pictures | Add pictures first |
| **This browser will not take an image from the clipboard.** | The browser cannot copy images | Use **Save the PNG** instead |
| **The browser refused the clipboard.** | Clipboard permission was blocked | Allow clipboard access for the site, or save the file |

## Sessions

| Symptom | Why | What to do |
|---|---|---|
| **That is not a session file this page wrote.** | The file is not JSON, or lacks the canvas and picture lists | Choose a `collage-session.json` saved by this tool |
| Loading a session changed only the canvas | No pictures were loaded when the session was read | Add the pictures, then load the session again |
| Pictures took each other's positions | They were added in a different order from the original | Clear the canvas, add the pictures in their original order, and load the session again |
| The session reopened without the pictures | A session never contains image data | Keep the original picture files with the session |

## Still stuck

Reload the page to start fresh; nothing you loaded was stored, so reloading clears the canvas and history. For help with the site in general, see the help pages at [Help](../../../../../help/README.md).
