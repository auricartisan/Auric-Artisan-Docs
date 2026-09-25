---
title: ASCII Art Generator — Troubleshooting
description: Fixes for common problems in the ASCII Art Generator, from files that will not load to downloads that do not match the art.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Troubleshooting

## Nothing happens when I open the page

That is expected: the stage waits for a source. Choose a file, drop or paste a picture, select **Try an example**, or switch to **Text**. There is no Render button; conversion starts by itself.

## My file will not load

- **Unsupported file type**: use PNG, JPEG, GIF, WebP, BMP, SVG or TIFF. Convert other formats, such as HEIC, first.
- **File too large**: the limit is 20 MB. Save a smaller copy or a JPEG.
- **Failed to load image**: the file may be damaged, or your browser cannot read that format. TIFF in particular opens only in some browsers.

## Pasting a picture does nothing

Click on an empty part of the page first, so you are not typing in a field, then press `Ctrl` + `V` (`Cmd` + `V` on a Mac). The clipboard must hold an image, not a link to one.

## The webcam will not start

At the time of writing, auricartisan.com tells browsers not to allow camera access on any of its pages. **Start** then shows a message that camera permission was denied. Changing permissions in your browser does not help. Take a photo with your camera app and load it with **Image** instead.

## The art looks stretched or squashed

- Leave **Match the output font** on in **Fine tuning › Shape**, so the cell shape matches the font.
- If you pasted the art somewhere else, use a monospaced font there too; a proportional font breaks the columns.
- If **Lock row count** is on, the row count no longer follows the picture. Turn it off.

## The art looks like a negative

The characters with the most ink should stand for the dark parts on light paper, and the light parts on dark paper. Check **Invert for dark paper**. Once you have changed it yourself, it no longer follows the paper colour automatically.

## The art is too dark, too light or flat

- Try **Gamma**: above 1 lightens the mid-tones, below 1 darkens them.
- Raise **Contrast**.
- Look at **Character frequency** in **Analysis**: a spike at one end means the tones are crushed.
- Try the **Line art** or **Bold** look for strong shapes, or **Fine** for subtle tones.

## Smooth areas show bands

Turn on **Floyd-Steinberg** or **Ordered (Bayer)** dithering, or choose a longer set such as **Detailed**. The **Compare** tab shows which sets are not ordered light to dark.

## Colour does not show

- Under **Colour**, choose **From image**. Colour shows in the **HTML**, **Canvas** and **SVG** renders, not in **Text**.
- With **Rotate 90°**, **Border**, **Frame** or **Thin out** on, the Canvas and SVG renders fall back to one colour. Turn those off for colour art.

## Filters do nothing

The **HTML** render shows the art before filters. Switch to **Text**, **Canvas** or **SVG**. **Brighten**, **Darken** and **Noise** work on Standard-set characters, so with other sets they change little or mix Standard characters in.

## The PNG, SVG or HTML download does not match the art

Those downloads can reuse an earlier render. Before downloading, select the matching render on the **Lab** tab: **Canvas** for PNG, **SVG** for SVG, **HTML** for HTML. Then download again.

## The ANSI download says to turn colour on

The ANSI file carries the picture's colours, so it needs **From image**. For plain characters, use the TXT download or **Copy**.

## Export all gave me five files, not six

That is how it works at present: **Export all six** downloads TXT, PNG, SVG, JSON and CSV. Download the HTML and ANSI files from their own cards. If only one file arrived, allow the page to download several files when your browser asks.

## Full screen shows no colour

Full screen shows the plain characters for every render except **Canvas**. Switch to **Canvas** first to see the colour art full screen. Close full screen with **×**.

## The Analysis charts are empty

Convert something first; the charts describe the last conversion. If they are still blank, switch to another tab and back.

## Conversion is slow or lags behind the sliders

Lower **Detail**, switch **Sampling** to **Bilinear** or **Point / Nearest**, turn off dithering, or use the **Text** render. The **Render timeline** chart and **Run benchmark** show the effect.

## Related

- [FAQ](faq.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
- [Help centre](../../../../../help/README.md)
