---
title: Collage Maker (panel) — Arrange images and export a 4K PNG
description: Put your own images into one of 29 collage layouts, style the grid, apply filters, add a title and export a 4K PNG, all inside a Basic Color Tools panel.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Collage Maker (panel)

The Collage Maker panel arranges images from your device into a layout: a plain grid, an editorial magazine page, a filmstrip, a pinboard and 25 more. You can set spacing, corner radius, background, borders and a drop shadow, apply a colour filter to all images or to single cells, add a title, and export the result as a large PNG. It is useful for mood boards, palette boards and quick visual references.

This is the compact collage tool inside Basic Color Tools. The site also has a separate, fuller Collage Maker page; see [Image and file tools](../../../../image-and-file-tools/README.md).

The panel's Collage Maker is in the **Compose** category at the **Advanced** level.

## Open it

In the Workspace view, select **Collage Maker** in **Open a tool**. It opens with an empty three-by-two grid.

## Screen tour

### Sidebar

- **Layout**: 29 layouts.
- **Cols**, **Rows**, **Gap** and **Radius** number boxes.
- **Background** colour.
- **Border width / color**: a number and a colour.
- **Drop shadow** check box.
- **Global filter**.
- **Title overlay**: text and colour.
- **+ Add Images**, a shuffle button and a clear (bin) button.
- **Export PNG (4K)**.

### Main area: Preview

A 4:3 preview of the collage. Empty cells read **+ Add**. Under it: *Click any cell to assign an image. Drag from desktop to drop multiple at once. Right-click a cell to apply a per-cell filter.* Dropping files is not supported in the current version, and a plain right-click opens the site's own menu; use the methods in the tasks below.

## Layouts

**Cols** and **Rows** shape the layouts marked "your grid". The others have a fixed number of cells.

| Layout | Cells | Notes |
| --- | --- | --- |
| **Grid** | your grid | Equal cells, Cols by Rows. |
| **Brick** | your grid | Cols by Rows. |
| **Mosaic** | your grid | A finer grid with a repeating pattern of large and small cells. |
| **Hero** | your grid (at least 2) | The first cell is large, the rest fill around it. |
| **Split** | 2 | Two large halves. |
| **Two-up** | 2 | Two side by side. |
| **Triptych** | 3 | Three side by side. |
| **Sidebar** | 4 | One large image and three small ones. |
| **Magazine** | 5 | Editorial page with one large image. |
| **Feature** | 4 | A wide feature image above smaller ones. |
| **Panorama** | 5 | A wide image above four small ones. |
| **Banner** | 4 | One large image beside three tall, narrow ones. |
| **Golden** | 4 | One dominant image and diminishing ones. |
| **Story** | 4 | A tall format with a wide top image. |
| **Poster** | 4 | A large image above three small ones. |
| **Frame** | 5 | Images framing a centre image. |
| **Quilt** | 10 | Mixed sizes. |
| **Tiles** | 9 | Mixed sizes. |
| **Checkerboard** | 16 | Four by four; alternate cells are slightly faded. |
| **Diagonal** | 7 | Cells stepping diagonally. |
| **Staircase** | 5 | Rows that grow wider, like steps. |
| **Masonry** | 12 | Four columns of varied heights. |
| **Columns** | 4 | Four tall columns. |
| **Rows** | 3 | Three wide rows. |
| **Contact sheet** | 20 | Five by four small frames. |
| **Pinboard** | 12 | Four by three, each image slightly tilted. |
| **Polaroid** | Cols (at least 3) | One row, images tilted like prints. |
| **Strip** | Cols (at least 3) | One row. |
| **Filmstrip** | 5 | Five frames in a row. |

## Tasks

### Make a mood board

1. Choose a **Layout**, for example **Magazine**.
2. Select **+ Add Images** and choose several images at once. They fill the empty cells in order. Images beyond the layout's number of cells are ignored.
3. To place or replace a single image, select that cell and choose one file.
4. Select the shuffle button to mix the order of the images.
5. Adjust **Gap**, **Radius**, **Background**, border and **Drop shadow** until it looks right.

Result: your images arranged in the chosen layout in the preview.

### Apply filters

1. Choose a **Global filter** to apply one look to every image: **None**, **Grayscale**, **Sepia**, **Invert**, **Blur**, **Warm**, **Cool**, **Contrast** or **Vintage**.
2. To give one cell its own filter, hold `Shift` and right-click that cell. Each `Shift` + right-click moves the cell to the next filter in the list above, and a message such as **Filter: sepia** appears. A cell's own filter overrides the global filter.

If you have set the site's right-click menu to use the browser's menu, a plain right-click cycles the filter instead. See [Site features](../../../../../site-features/README.md).

Result: every image carries the look you chose, with individual exceptions.

### Add a title and export

1. Type a **Title overlay** and choose its colour.
2. Select **Export PNG (4K)**.

The title does not appear in the preview. It is drawn only in the exported image: bold, centred near the top, with a soft shadow.

Result: `collage.png` downloads, with the preview's proportions, the background colour, rounded corners, borders, filters and title. When the preview is at least 800 pixels wide, the image is 3,840 pixels wide. When the preview is narrower, the image is 4.8 times the preview's size and so less than 3,840 pixels wide; widen or maximise the panel before exporting to get the full size.

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Layout** | Chooses the arrangement. | 29 layouts | Grid |
| **Cols** | Columns for grid-based layouts; images per row for Polaroid and Strip. | 1 to 6 | 3 |
| **Rows** | Rows for grid-based layouts. | 1 to 6 | 2 |
| **Gap** | Space between cells, in pixels. | 0 to 40 | 6 |
| **Radius** | Corner rounding of cells, in pixels. | 0 to 40 | 8 |
| **Background** | Colour behind the cells. | Any colour | #101010 |
| **Border width** | Inner border on each cell, in pixels. | 0 to 20 | 0 |
| Border colour | Colour of that border. | Any colour | #FFFFFF |
| **Drop shadow** | Shadow under each cell in the preview. | On or off | On |
| **Global filter** | Filter for every image. | None, Grayscale, Sepia, Invert, Blur, Warm, Cool, Contrast, Vintage | None |
| **Title overlay** | Text drawn at the top of the export. | Any text | Empty |
| Title colour | Colour of the title. | Any colour | #FFFFFF |
| **+ Add Images** | Adds several images to empty cells. | Image files | — |
| Cell | Select to place one image in that cell. | One image file | — |
| `Shift` + right-click a filled cell | Cycles that cell's filter. | Same list as Global filter | — |
| Shuffle | Randomises the image order. | — | — |
| Clear (bin) | Removes all images. | — | — |
| **Export PNG (4K)** | Downloads the collage as `collage.png`. | 3,840 pixels wide when the preview is 800 pixels wide or more | — |

## Accuracy and limits

- Images are read from your device in the browser and are not uploaded. Very large images or many images make the export slower.
- The export redraws the collage at high resolution from the preview's layout. The drop shadow and the slight fade of alternate **Checkerboard** cells appear only in the preview; the pinboard and polaroid tilts are not drawn in the export either.
- Images are cropped to fill their cells, keeping their centre.
- Open panels are not saved when you reload the page. Export before you leave.

## Related

- [Panel tools](README.md)
- [Collage Maker page and other image tools](../../../../image-and-file-tools/README.md)
- [Troubleshooting](../troubleshooting.md)
