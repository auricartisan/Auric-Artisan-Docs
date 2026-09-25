==============================================================================
M-GRADIENT PALETTE
==============================================================================
What the M-Gradient Palette does, who it is for, where to find it and how to
build a first ramp.
Area: Website › Tools › Image and file tools › M-Gradient Palette   Updated: 2026-09-25

The M-Gradient Palette (the page is titled Gradient Ramp) builds a colour
ramp: a row of evenly spaced steps between two colours, of the kind used for
data-visualisation scales, tint and shade series, and design tokens. You
choose the two ends, the number of steps, and the space the colours are
blended in: OKLCH, sRGB, linear RGB or HSL, with a short or long way round the
hue circle for the two polar spaces.

The tool then measures the ramp. It gives the CIEDE2000 colour difference
between every pair of neighbouring steps, their average, and how even they
are, and counts the steps whose colourfulness had to be reduced to fit sRGB. A
second tab builds all thirty combinations of route and easing between your two
colours and marks the evenest. A third checks every step as a background for a
text colour you choose, with both the WCAG 2.2 ratio and the APCA lightness
contrast, and the whole ramp can be viewed as people with protanopia,
deuteranopia or tritanopia see it.

You can copy the ramp as a CSS gradient, as CSS custom properties, as a list
of hex values or as SVG, and save a JSON reading of what was measured.
Everything runs in your browser.

WHO IT IS FOR
=============

  - Designers building tint and shade scales, and tokens for a design system.
  - Data-visualisation designers who need sequential scales with even, visible
    steps.
  - Front-end developers choosing between `linear-gradient` in sRGB and in
    OKLCH.
  - Accessibility specialists checking which steps of a scale can carry text.

WHERE TO FIND IT
================

Open https://auricartisan.com/tool/general/tools/m-gradient-palette/ in a
current browser. It is listed as M-Gradient Palette on the Collections page at
https://auricartisan.com/collections/. Nothing needs installing.

QUICK START
===========

  1. Open the tool. The Ramp tab shows a 12-step ramp from `#0B3D5C` to
     `#F2B134`, blended in OKLCH, short hue.
  2. Set the two ends with the swatches or the hex boxes under The two ends,
     or choose a pair from A starting point.
  3. Set Steps, and choose a route under Interpolate in.
  4. Read mean ΔE₀₀ and evenness under What the ramp measures; flatter bars
     mean more even steps.
  5. Open the Contrast tab, choose a Text colour, and see which steps can
     carry text.
  6. Open the Export tab and select Copy the custom properties to copy the
     steps as CSS.

WHAT YOU CAN DO
===============

  - Blend between two colours in four spaces by six routes, at 2 to 32 steps,
    with five easing curves.
  - Start from 25 named preset pairs, and swap the ends.
  - Measure the CIEDE2000 difference between every pair of neighbouring steps,
    their mean, spread and largest jump.
  - See which steps were brought inside sRGB, and where the ramp travels in
    OKLCH hue and chroma.
  - Compare all 30 route and easing combinations, built and measured, with the
    evenest marked.
  - Check every step against a text colour with WCAG 2.2 and APCA, side by
    side.
  - View the ramp as seen with protanopia, deuteranopia or tritanopia.
  - Copy a CSS gradient, custom properties, a hex list or SVG; save SVG and a
    JSON reading.

IN THIS FOLDER
==============

  - docs/ [docs/README.txt] — how to use the tool.
    - Getting started [docs/getting-started.txt] — open it, the screen tour, a
      first ramp.
    - Interpolation and gamut [docs/interpolation-and-gamut.txt] — OKLab,
      OKLCH, sRGB, linear RGB and HSL; hue routes; easing; gamut mapping.
    - Build a ramp [docs/build-a-ramp.txt] — ends, presets, routes, steps,
      easing and the measurements.
    - Compare routes and easings [docs/compare-routes.txt] — the Spaces tab.
    - Check contrast and colour vision
      [docs/check-contrast-and-colour-vision.txt] — WCAG 2.2, APCA and the
      colour-vision views.
    - Export a ramp [docs/export-a-ramp.txt] — every copy and save format.
    - Reference [docs/reference.txt] — every control, value, readout and
      format.
    - Troubleshooting [docs/troubleshooting.txt] — symptoms, causes and fixes.
    - FAQ [docs/faq.txt] — short answers to common questions.
  - others/ [others/README.txt] — background material.
    - Glossary [others/glossary.txt] — terms used in this tool.
    - Limits and accuracy [others/limits-and-accuracy.txt] — what is measured,
      how precisely, and what is not held.
    - Related [others/related.txt] — related tools and Learn articles.
    - Release notes [others/release-notes.txt] — user-facing history.
    - Privacy [others/privacy.txt] — what stays in your browser.
