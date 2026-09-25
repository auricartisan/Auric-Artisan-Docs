==============================================================================
SVG RECOLOUR
==============================================================================
What SVG Recolour does, who it is for, where to find it and how to recolour a
first SVG.
Area: Website › Tools › Image and file tools › SVG Recolour   Updated: 2026-09-25

SVG Recolour (listed as SVG Recolor in Collections) changes the colours of an
SVG file. It finds every colour in the file, wherever and however it is
written, lists each distinct colour once with the number of places it is used,
and lets you choose what each should become. The new file is written from your
original in one pass, so two colours can trade places, a colour written as a
name such as `red` is changed like any other, and the count beside each colour
is the number of places actually rewritten.

Before and after previews sit side by side on a chequerboard. You can recolour
by hand, one colour at a time, or from a harmony built on the file's main
colour: complementary, analogous, triadic, tetradic or split complementary.
The Check tab measures every colour as a background for a text colour of your
choice, with both WCAG 2.2 and APCA, and finds the two colours in the file
that are hardest to tell apart, with normal vision and with each of three
colour-vision deficiencies.

You can save the recoloured SVG, copy its markup, copy the new palette as CSS
custom properties, and save a JSON report of every change. The file is parsed
in the page and never uploaded, and scripts and other active content are
removed from the previews.

WHO IT IS FOR
=============

  - Designers adapting icons and illustrations to a new brand palette.
  - Developers who need an SVG's colours to match CSS tokens.
  - Accessibility specialists checking whether the colours in an icon set can
    be told apart.
  - Anyone who has been sent an SVG and wants to change its colours without a
    drawing program.

WHERE TO FIND IT
================

Open https://auricartisan.com/tool/general/tools/svg-recolor/ in a current
browser. It is listed as SVG Recolor on the Collections page at
https://auricartisan.com/collections/. Nothing needs installing.

QUICK START
===========

  1. Open the tool. A small sample SVG is already loaded on the Recolour tab.
  2. Drop your own SVG on the Drop an SVG box, or paste its markup and select
     Read the markup.
  3. Under Every colour in the file, select the right-hand swatch in a row and
     choose the new colour.
  4. Watch the After preview change, and the row report how many places were
     written.
  5. Open the Check tab to see contrast and the closest pair of colours.
  6. Open the Export tab and select Save the recoloured SVG. Your browser
     downloads `recoloured.svg`.

WHAT YOU CAN DO
===============

  - Load an SVG by dropping it, choosing it, or pasting its markup; or load
    the built-in sample.
  - Find colours in eight paint properties, in attributes, style attributes
    and style sheets, written as hex, `rgb()`, `hsl()` or any of the 148 CSS
    colour names.
  - Remap each distinct colour, and swap colours with each other.
  - Write new colours as hex, or keep the form each colour was written in.
  - Recolour from five harmonies built in OKLCH, and put every colour back in
    one step.
  - Preview before and after, also as seen with protanopia, deuteranopia or
    tritanopia.
  - Check every colour as a background for text with WCAG 2.2 and APCA, and
    find the closest pair under four kinds of vision.
  - Save or copy the recoloured SVG, copy the palette as custom properties,
    and save a JSON report.

IN THIS FOLDER
==============

  - docs/ [docs/README.txt] — how to use the tool.
    - Getting started [docs/getting-started.txt] — open it, the screen tour, a
      first recolour.
    - Recolour an SVG [docs/recolour-an-svg.txt] — loading, what is found,
      mapping colours, swaps and write styles.
    - Recolour from a harmony [docs/use-a-harmony.txt] — the five harmonies
      and how they are built.
    - Check contrast and colour vision
      [docs/check-contrast-and-colour-vision.txt] — the Check tab and the
      vision previews.
    - Export the result [docs/export-the-result.txt] — the SVG, the markup,
      custom properties and the report.
    - Reference [docs/reference.txt] — every control, readout, format and
      message.
    - Troubleshooting [docs/troubleshooting.txt] — symptoms, causes and fixes.
    - FAQ [docs/faq.txt] — short answers to common questions.
  - others/ [others/README.txt] — background material.
    - Glossary [others/glossary.txt] — terms used in this tool.
    - Limits and accuracy [others/limits-and-accuracy.txt] — what is found,
      what is not, and how precise it is.
    - Related [others/related.txt] — related tools and Learn articles.
    - Release notes [others/release-notes.txt] — user-facing history.
    - Privacy [others/privacy.txt] — what stays in your browser, and active
      content.
