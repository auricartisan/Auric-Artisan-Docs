==============================================================================
TONE MAPPING
==============================================================================
What the Tone Mapping lab does, who it is for, where to find it and how to map
your first frame.
Area: Website › Tools › Colorimetry and rendering   Updated: 2026-09-25

A real scene can hold far more light than any display can show: a sunlit
window may be thousands of times brighter than the shadows in the room. Tone
mapping is the curve that squeezes that range into the display's range while
deciding what to keep — shadow detail, mid-tones, or colour in the highlights.

The Tone Mapping lab runs a frame through an eleven-step pipeline you control:
decode the source, convert it to a working space with white-point adaptation,
set exposure, apply an optional low-level operator, apply the tone curve,
grade it, convert to the target display space with gamut mapping, and encode
it for output. It offers seven working tone curves — clipping, Reinhard,
Uchimura (Gran Turismo), Hable filmic, the Narkowicz fit of the ACES look, a
soft log curve and your own three-point curve — and shows two retired
operators on the Operators tab for comparison.

You can work on built-in test scenes or your own image, read the result on a
histogram, waveform, vectorscope and false-colour map, compare two versions
side by side, and export the tone curve as a 1D `.cube` or CSV, or the whole
pipeline as a 3D `.cube` LUT.

WHO IT IS FOR
=============

  - Game, 3D and VFX artists choosing a tone curve for renders.
  - Colourists and video editors who want a LUT that matches a preview.
  - Developers implementing tone mapping in a renderer.
  - Students learning scene-referred and display-referred imaging.

WHERE TO FIND IT
================

  - Address:
    https://auricartisan.com/tool/general/gamut-and-rendering/tone-mapping/
  - In the tool collection (https://auricartisan.com/collections/) under Gamut
    & Rendering, as Tone Mapping.

QUICK START
===========

  1. Open
     https://auricartisan.com/tool/general/gamut-and-rendering/tone-mapping/.
     The HDR test scene is mapped with the Hable filmic curve.
  2. Move Exposure up and down to see which part of the curve the scene lands
     on.
  3. Under Tone curve, try Reinhard, Narkowicz fit and None (clip). Watch the
     highlights.
  4. Read the statistics: where mid-grey 0.18 lands, and the input at which
     the scene reaches display white.
  5. Open Scopes to read the histogram, waveform and vectorscope.
  6. Open Operators to compare every curve on one set of inputs.
  7. Open Export, choose The tone curve as .cube, and select the download
     button.

WHAT YOU CAN DO
===============

  - Tone-map three built-in test scenes or your own image.
  - Declare the source's encoding (linear, sRGB, PQ, HLG, gamma 2.2 or 2.4),
    primaries and white.
  - Set exposure in stops, choose one of seven tone curves or shape your own.
  - Apply a low-level operator and a grade (contrast, saturation, lift, gamma,
    gain, temperature, tint, hue, vibrance).
  - Choose working and target spaces, target white, gamut mapping and output
    encoding; mark out-of-gamut pixels; dither.
  - Compare operators numerically and on one chart.
  - Read histogram, waveform, vectorscope and a false-colour exposure map;
    store two frames and split the view.
  - Export a 1D `.cube` or CSV of the curve, a 3D `.cube` of the pipeline, or
    a link.
  - Map a list of HEX colours through the pipeline.

IN THIS FOLDER
==============

  - docs/ [docs/README.txt] — how to use the lab
    - Getting started [docs/getting-started.txt]
    - Map a frame [docs/map-a-frame.txt]
    - Compare operators [docs/compare-operators.txt]
    - Read the scopes [docs/read-the-scopes.txt]
    - Export a LUT [docs/export-a-lut.txt]
    - Reference [docs/reference.txt]
    - Troubleshooting [docs/troubleshooting.txt]
    - FAQ [docs/faq.txt]
  - others/ [others/README.txt] — background and supporting pages
    - Glossary [others/glossary.txt]
    - Shortcuts [others/shortcuts.txt]
    - Limits and accuracy [others/limits-and-accuracy.txt]
    - Related tools [others/related.txt]
    - Release notes [others/release-notes.txt]
    - Privacy [others/privacy.txt]
