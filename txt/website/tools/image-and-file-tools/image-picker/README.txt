==============================================================================
IMAGE PICKER
==============================================================================
What the Image Picker does, who it is for, where to find it and how to take a
first palette from a picture.
Area: Website › Tools › Image and file tools › Image Picker   Updated: 2026-09-25

The Image Picker (the page is titled Image Color Picker & Palette Tool) turns
a picture into a palette. Drop a photograph, a screenshot or a scan and the
tool samples its pixels, groups them into clusters with the k-means++ method,
and shows the resulting colours with the share of the picture each one takes
up. For flat artwork such as logos and icons, where the picture has no more
distinct colours than you asked for, it keeps the exact colours instead of
averages.

Alongside the palette it sorts the colours into shadows, midtones and
highlights, lists the pairs with the most contrast for text by the WCAG 2
ratio, and spots harmony relationships between the colours. A live eyedropper
reads any pixel under the pointer, and a click pins it, so you can keep exact
colours the clustering merged away. The Analysis tab charts the same palette
four ways.

You can copy the palette as hex values, CSS custom properties or JSON,
download it as SVG, JSON or CSV, and analyse a list of hex colours without any
picture at all. Pictures are read in the page; nothing is uploaded.

WHO IT IS FOR
=============

  - Designers building a palette from a photograph, moodboard or product shot.
  - Brand and editorial teams auditing the colours in a set of images.
  - Developers who want an image's colours as CSS custom properties or JSON.
  - Anyone who needs the exact colour of one pixel.

WHERE TO FIND IT
================

Open https://auricartisan.com/tool/general/tools/image-picker/ in a current
browser. It is listed as Image Picker on the Collections page at
https://auricartisan.com/collections/. Nothing needs installing.

QUICK START
===========

  1. Open the tool. The Workbench tab is selected.
  2. Drop an image anywhere on the large panel in the middle, or select the
     panel to choose a file (PNG, JPEG, WEBP, GIF or BMP).
  3. The palette appears under Extracted palette, largest share first.
  4. Move the Clusters slider to ask for more or fewer colours; the palette
     updates when you release it.
  5. Hover the preview to read any pixel, and click to pin one under Pinned.
  6. Select Hex, CSS or JSON under Take it with you to copy the palette, or
     SVG to download it.

WHAT YOU CAN DO
===============

  - Extract 2 to 12 colour clusters (16 when the page first opens), at five
    sampling qualities, with optional merging of near-identical clusters.
  - Leave out near-black or near-white pixels.
  - Read any pixel as hex, RGB, HSL, relative luminance and position, and pin
    up to 24 exact colours.
  - See each colour's share of the picture, its tone band, the eight strongest
    contrast pairs with WCAG ratings, and detected harmonies.
  - Chart population, distribution, hue against saturation, and luminance,
    each viewable full screen.
  - Copy hex, CSS custom properties or JSON; download SVG, JSON or CSV.
  - Analyse a typed list of hex colours in RGB, HSL, CIELAB, LCH, luminance
    and tone band.
  - Load a picture from a web address, where the server allows it.

IN THIS FOLDER
==============

  - docs/ [docs/README.txt] — how to use the tool.
    - Getting started [docs/getting-started.txt] — open it, the screen tour,
      the first palette.
    - Extract a palette [docs/extract-a-palette.txt] — loading pictures and
      every extraction setting.
    - Pick exact colours [docs/pick-exact-colours.txt] — the eyedropper and
      pins.
    - Read contrast pairs, tone bands and harmony
      [docs/read-contrast-and-harmony.txt] — what each readout means.
    - Chart the palette [docs/chart-the-palette.txt] — the four charts on the
      Analysis tab.
    - Export and share [docs/export-and-share.txt] — every copy and download
      format.
    - Analyse a list of hex colours [docs/batch-analysis.txt] — batch colour
      analysis.
    - Reference [docs/reference.txt] — every control, output and format.
    - Troubleshooting [docs/troubleshooting.txt] — symptoms, causes and fixes.
    - FAQ [docs/faq.txt] — short answers to common questions.
  - others/ [others/README.txt] — background material.
    - Glossary [others/glossary.txt] — terms used in this tool.
    - Shortcuts [others/shortcuts.txt] — keyboard shortcuts.
    - Limits and accuracy [others/limits-and-accuracy.txt] — how the palette
      is made and what it is not.
    - Related [others/related.txt] — related tools, the API and Learn
      articles.
    - Release notes [others/release-notes.txt] — user-facing history.
    - Privacy [others/privacy.txt] — what stays in your browser and what uses
      the network.
