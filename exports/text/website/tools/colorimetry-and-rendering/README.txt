==============================================================================
COLORIMETRY AND RENDERING TOOLS
==============================================================================
What the colorimetry, gamut and rendering tools on auricartisan.com are for,
where to find them, and which one to open for your question.
Area: Website › Tools › Colorimetry and rendering   Updated: 2026-09-25

This area documents seven colour-science tools on auricartisan.com. They
answer questions that sit underneath everyday colour work: what "white" means
under a given light, how a colour changes when the light changes, which
colours a screen or file format can hold, what happens to a colour that does
not fit, and how a high-dynamic-range signal becomes light on a display.

The tools are split into two groups on the site:

  - Colorimetry — measuring and converting colour with the standard CIE
    methods: light sources (illuminants), white points, chromatic adaptation
    and gamut mapping.
  - Gamut and rendering — the limits of colour spaces and displays, HDR
    transfer curves, tone mapping, and ramps of tints and shades.

Every tool runs entirely in your browser. Each one has a Data tab that lists
the published tables and formulas it uses, with a status for each (verbatim,
computed, stand-in or absent), so you can see which figures are standard
values and which are illustrations. None of them is a certified measurement
instrument.

WHERE TO FIND THEM
==================

The tools are listed in the Colorimetry and Gamut & Rendering categories of
the site's tool collection at https://auricartisan.com/collections/.

The three hub addresses below are kept for old links. Each one now sends you
to the collection page:

  Address                                                    | Where it goes
  -----------------------------------------------------------+--------------------
  https://auricartisan.com/tool/general/                     | The tool collection
  https://auricartisan.com/tool/general/colorimetry/         | The tool collection
  https://auricartisan.com/tool/general/gamut-and-rendering/ | The tool collection

THE TOOLS
=========

  Tool:      Illuminants [illuminants/README.txt]
  Address:   https://auricartisan.com/tool/general/colorimetry/illuminants/
  Use it to: Inspect standard light sources: spectra, white points, CCT and
             Duv, chromaticity, adaptation and measurement uncertainty

  Tool:      Chromatic Adaptation [chromatic-adaptation/README.txt]
  Address:   https://auricartisan.com/tool/general/colorimetry/chromatic-adaptation-dynamic/
  Use it to: Apply eight adaptation transforms to an image and study how the
             eye adapts over time

  Tool:      Gamut Mapping [gamut-map/README.txt]
  Address:   https://auricartisan.com/tool/general/colorimetry/gamut-map/
  Use it to: See what a colour becomes when the target colour space cannot
             hold it

  Tool:      Gamut Lab [gamut-lab/README.txt]
  Address:   https://auricartisan.com/tool/general/gamut-and-rendering/gamut/
  Use it to: Draw and measure 13 RGB colour spaces (or your own) and their
             transfer curves

  Tool:      HDR Gamut Plot [hdr-gamut-plot/README.txt]
  Address:   https://auricartisan.com/tool/general/gamut-and-rendering/hdr-gamut-plot/
  Use it to: Compare Rec.709, Display P3 and Rec.2020 and explore PQ, HLG,
             ICtCp and Jzazbz

  Tool:      Tonal Steps [tonal-steps/README.txt]
  Address:   https://auricartisan.com/tool/general/gamut-and-rendering/tonal-steps-tints-shades/
  Use it to: Build a lightness ramp, tints, shades and tones from one colour
             and check contrast

  Tool:      Tone Mapping [tone-mapping/README.txt]
  Address:   https://auricartisan.com/tool/general/gamut-and-rendering/tone-mapping/
  Use it to: Compare tone-mapping operators that turn HDR values into
             displayable ones

WHICH TOOL DO I NEED?
=====================

  - "What colour is this light, and is it close to daylight?" — Illuminants.
  - "My photo was lit by tungsten; what does it look like adapted to
    daylight?" — Chromatic Adaptation.
  - "This brand colour is outside sRGB. What will it look like after
    conversion?" — Gamut Mapping.
  - "How much bigger is Display P3 than sRGB, and what curve does Rec.2020
    use?" — Gamut Lab.
  - "What does a PQ signal of 0.5 mean in nits?" — HDR Gamut Plot.
  - "I need an 11-step ramp with known contrast against white." — Tonal Steps.
  - "Which tone curve keeps my highlights?" — Tone Mapping.

CONCEPTS IN ONE PAGE
====================

  - Illuminant — a light source defined by its spectral power distribution
    (how much power it emits at each wavelength). CIE D65 stands for average
    daylight; CIE A for a tungsten lamp.
  - White point — the colour of an illuminant, usually written as chromaticity
    coordinates x, y. A colour space is defined against one (D65 for sRGB, D50
    for ProPhoto RGB).
  - Chromaticity diagram — a flat map of colour without brightness. The CIE
    1931 xy diagram is the classic one; the CIE 1976 u′v′ diagram spaces
    colours more evenly.
  - Gamut — the set of colours a device or colour space can represent. On a
    chromaticity diagram an RGB gamut is a triangle.
  - Chromatic adaptation — the eye's adjustment to the colour of the light. A
    chromatic adaptation transform (CAT) predicts it numerically.
  - Transfer function — the curve that converts between stored code values and
    light (for example the sRGB curve, PQ or HLG).
  - Tone mapping — compressing a wide range of scene brightness into what a
    display can show.

Each tool folder has its own glossary with fuller definitions.

IN THIS FOLDER
==============

  Folder                                                  | What it covers
  --------------------------------------------------------+------------------------------
  illuminants/ [illuminants/README.txt]                   | The Standard Illuminants lab
  chromatic-adaptation/ [chromatic-adaptation/README.txt] | The Chromatic Adaptation lab
  gamut-map/ [gamut-map/README.txt]                       | The Gamut Mapping lab
  gamut-lab/ [gamut-lab/README.txt]                       | The Gamut Lab
  hdr-gamut-plot/ [hdr-gamut-plot/README.txt]             | The HDR Gamut Plot
  tonal-steps/ [tonal-steps/README.txt]                   | Tonal Steps, Tints and Shades
  tone-mapping/ [tone-mapping/README.txt]                 | The Tone Mapping lab
