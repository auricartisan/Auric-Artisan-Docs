---
title: Image Picker — Chart the palette
description: Read the four charts on the Analysis tab and open any of them full screen.
product: Website › Tools › Image and file tools › Image Picker
updated: 2026-09-25
---

# Chart the palette

The **Analysis** tab draws the current palette four ways. Every chart is drawn in the palette's own colours, so a bar and a swatch of the same colour are the same cluster.

## Open the charts

1. Extract a palette on the **Workbench** tab.
2. Select the **Analysis** tab.
3. The left-hand panel, **Charting**, names the picture and its working size and pixel count, for example `667 × 500 · 333,500 px`.

Until a picture is loaded, the tab reads **Nothing charted yet**.

## The four charts

| Chart | Subtitle | What it shows |
|---|---|---|
| **Cluster population** | share of the samples | One bar per cluster, largest first, with the share of the largest and smallest at the top |
| **Colour distribution** | every cluster | A ring divided by share, with the leading share, its hex value and the cluster count in the middle |
| **Hue vs saturation** | HSL scatter | Each cluster placed by hue (0° to 360° across) and saturation (0% to 100% up); larger dots are larger shares |
| **Relative luminance** | WCAG, 0 → 1 | One bar per cluster, sorted from darkest to lightest, height set by relative luminance |

Details:

- **Cluster population** labels each bar with its share when there is room; with many clusters the labels are left off, and the share is still on the swatch.
- **Colour distribution** labels slices larger than 8% with their share.
- **Hue vs saturation** has a faint rainbow behind it to show where each hue sits.
- **Relative luminance** labels each bar with its value when there is room, and marks **darkest** and **lightest** at the ends.

## Full screen

To see a chart larger, double-click it, or select the **⛶** button in its corner. The chart opens over the page with its title, such as **Cluster Population Histogram**. Close it with the **×** button, the `Escape` key, or by clicking the dark area around it.

## When the charts update

The charts redraw whenever the palette changes and the **Analysis** tab is open, and when you resize the window. Extractions you run while on the **Workbench** tab are charted the next time you open **Analysis**.
