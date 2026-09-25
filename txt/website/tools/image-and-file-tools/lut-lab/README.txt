==============================================================================
LUT LAB
==============================================================================
What LUT Lab does, who it is for, where to find it and how to try a first look
and write a .cube file.
Area: Website › Tools › Image and file tools › LUT Lab   Updated: 2026-09-25

LUT Lab reads, applies and writes colour lookup tables. A lookup table, or
LUT, is a file that says what colour each input colour should become;
colourists use LUTs to carry a grade or a conversion from one program to
another. LUT Lab works with the `.cube` format, in its one-dimensional (1D)
and three-dimensional (3D) forms.

The Lab tab shows a scene before and after a transform, side by side. The
transform is either one of six built-in looks, such as Teal and orange or a
Reinhard tone-map, or a `.cube` file you load. Under the pair, the tool
measures what the transform moved: the average and largest colour difference
in CIEDE2000, the share of pixels it clipped to pure white or black, and, on a
ring of test colours, how far it turned hue and changed lightness and chroma.
You can test on four drawn scenes or on your own picture.

The Export tab writes the transform in force as a `.cube`, at any size from 2
to 65, as a 3D cube or a 1D curve. The file's header states plainly that the
tool works in 8 bits and that the sample order is red fastest, as the format
requires. Everything runs in your browser; nothing is uploaded.

WHO IT IS FOR
=============

  - Colourists and editors checking what a `.cube` does before using it in a
    grading or editing program.
  - Designers and developers who want a simple look as a `.cube` file.
  - Anyone who needs to resample a `.cube` to a different size, or turn it
    into a 1D curve.
  - Students learning how LUTs, interpolation and clipping work.

WHERE TO FIND IT
================

Open https://auricartisan.com/tool/general/tools/lut-lab/ in a current
browser. It is listed as LUT Lab on the Collections page at
https://auricartisan.com/collections/. Nothing needs installing.

QUICK START
===========

  1. Open the tool. The Lab tab shows the Neutral wedge scene with the Teal
     and orange look applied.
  2. Select another scene, for example Colour patches, or drop your own
     picture on Drop an image.
  3. Choose a look from the menu under The look, and move Strength to set how
     much of it to apply.
  4. Read the cards under What it moved and the hue circle under Where it
     moved things to.
  5. To test a file instead, drop a `.cube` on Drop a .cube.
  6. Open the Export tab, choose Kind and Size, and select Save the .cube.

WHAT YOU CAN DO
===============

  - Apply six built-in looks: Teal and orange, Bleach bypass, Film soft, Mono
    contrast, Log-ish lift and Reinhard tone-map, with a strength control and,
    for the tone-map, an exposure control.
  - Load any 1D or 3D `.cube` file, see its size, domain and any problems with
    it, and apply it.
  - Test on four drawn scenes or on your own picture, scaled to fit 480 × 270.
  - See the pixels a transform drove to white or black, highlighted on the
    result.
  - Measure mean, 95th-percentile and largest CIEDE2000 difference, and the
    share of clipped pixels.
  - See hue, lightness and chroma shifts on a 72-point ring of constant
    lightness in CIELAB.
  - Write a 3D `.cube` (2³ to 65³) or a 1D `.cube` (2 to 65 entries) of the
    transform in force, and copy it to the clipboard.
  - Save the hue sweep as CSV and a full report as JSON, and copy a link that
    restores your settings.

IN THIS FOLDER
==============

  - docs/ [docs/README.txt] — how to use the tool.
    - Getting started [docs/getting-started.txt] — open it, the screen tour, a
      first look.
    - LUT concepts [docs/lut-concepts.txt] — 1D and 3D LUTs, sizes, domains,
      interpolation, clipping and bit depth.
    - Apply a look [docs/apply-a-look.txt] — scenes, your own picture, the six
      looks, strength and exposure.
    - Load a .cube file [docs/load-a-cube-file.txt] — what the reader accepts
      and what it reports.
    - Read what a transform moved [docs/read-what-it-moved.txt] — the clip
      overlay, the difference cards and the hue circle.
    - Write a .cube file [docs/write-a-cube-file.txt] — kinds, sizes, the
      header, round trips and the other exports.
    - Reference [docs/reference.txt] — every control, readout, format and
      message.
    - Troubleshooting [docs/troubleshooting.txt] — symptoms, causes and fixes.
    - FAQ [docs/faq.txt] — short answers to common questions.
  - others/ [others/README.txt] — background material.
    - Glossary [others/glossary.txt] — terms used in this tool.
    - Limits and accuracy [others/limits-and-accuracy.txt] — the 8-bit path,
      what is measured and what is not held.
    - Related [others/related.txt] — related tools and Learn articles.
    - Release notes [others/release-notes.txt] — user-facing history.
    - Privacy [others/privacy.txt] — what stays in your browser.
