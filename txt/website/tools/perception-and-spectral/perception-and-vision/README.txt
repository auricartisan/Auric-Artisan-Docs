==============================================================================
PERCEPTION AND VISION
==============================================================================
What the Perception Vision tool does, who it is for, where to find it and how
to run a first colour vision simulation over your own image.
Area: Website › Tools › Perception and spectral › Perception and Vision   Updated: 2026-09-25

Perception and Vision (the page is titled Perception Vision) runs eight
simulations of how a scene reaches a different visual system: colour vision
deficiency (protan, deutan and tritan), rod-only night vision, twilight
vision, a yellowing lens, cataract, loss of central vision, light adaptation
and reduced acuity. You run them over a built-in test card, a grey ramp, a
Snellen chart or an image of your own, and compare the result with the
original in a split view.

The colour vision simulation follows the published method of Viénot, Brettel
and Mollon (1999): each colour goes from sRGB through CIE XYZ into cone
signals, the missing cone type is projected away, and the result comes back to
sRGB. The page checks itself as it goes. A grey ramp shows whether the
simulation tints neutrals (a correct dichromacy simulation never does), a
counter reports how many of the frame's colours merged into one, and the
graphics-card and processor renderers are compared on 216 colours after every
change.

The tool is an educational and design-review aid. Only the colour vision
projection comes from a publication; the other seven simulations use the
tool's own constants and show that an effect exists rather than how strong it
is for any person. It is not a clinical instrument, and everything runs in
your browser.

WHO IT IS FOR
=============

  - Designers and front-end developers checking whether a screen, chart or
    palette still works for people with colour vision deficiency, in dim light
    or with ageing eyes.
  - Accessibility specialists who want a traceable simulation with a stated
    method.
  - Students learning what dichromacy, rod vision and lens yellowing do to
    colour.

WHERE TO FIND IT
================

Open
https://auricartisan.com/tool/general/perception-and-neuroscience/perception-vision/
in a current desktop browser. It is listed as Perception & Vision on the
Collections page (https://auricartisan.com/collections/) and as Perception and
Vision in the site menu. WebGL2 is used when available; without it the page
runs the same simulations on the processor.

QUICK START
===========

  1. Open the tool. The Lab tab shows the test card, split down the middle:
     original on the left, protanopia on the right.
  2. Under Source, choose Uploaded image, select Choose a file and pick a
     screenshot or picture.
  3. Under Simulation, keep Colour vision and try Protan, Deutan and Tritan
     under Type.
  4. Drag on the image to move the divider, or set Divider on the rail.
  5. Read Colours merged and Distinct colours left to see how many of your
     image's colours became indistinguishable.
  6. Try Scotopic, Lens yellowing or Acuity, or pick a Presets entry.
  7. Select Save the frame to download the view as a PNG, or open Export to
     check a list of hex colours.

WHAT YOU CAN DO
===============

  - Simulate eight visual conditions over a test card, a grey ramp, a Snellen
    chart or your own image.
  - Set severity, adaptation level, age, scotoma radius, cataract level and
    Snellen acuity.
  - Daltonise instead of simulate, to see a colour correction for dichromats.
  - Relight the scene with illuminant D50 or A before it reaches the simulated
    eye.
  - Add contrast, gamma, blur, glare and noise adjustments to both halves of
    the comparison.
  - Compare as a split view, simulated only, or an amplified difference image.
  - Read neutral drift, merged colours, out-of-gamut share, renderer agreement
    and frame luminance.
  - Run a list of hex colours through the simulation and export CSV, clipboard
    text, settings JSON, a PNG of the frame or a link.

IN THIS FOLDER
==============

  - docs/ [docs/README.txt] — how to use the tool.
    - Getting started [docs/getting-started.txt] — open it, the screen tour,
      the first simulation.
    - Simulate a design or image [docs/simulate-a-design.txt] — sources, the
      eight simulations, their controls, presets and comparison views.
    - Read the checks [docs/read-the-checks.txt] — the grey ramp, the
      readouts, the Simulation and Modes tabs.
    - Check a palette and export [docs/check-a-palette-and-export.txt] — the
      colour list, CSV, clipboard, frame PNG, settings and links.
    - Reference [docs/reference.txt] — every control, readout, tab and file
      format.
    - Troubleshooting [docs/troubleshooting.txt] — symptoms, causes and fixes.
    - FAQ [docs/faq.txt] — short answers to common questions.
  - others/ [others/README.txt] — background material.
    - Glossary [others/glossary.txt] — terms used in this tool.
    - Shortcuts [others/shortcuts.txt] — keyboard and pointer actions.
    - Limits and accuracy [others/limits-and-accuracy.txt] — what is
      published, what is the tool's own, what is not held.
    - Related [others/related.txt] — related tools and Learn articles.
    - Release notes [others/release-notes.txt] — user-facing history.
    - Privacy [others/privacy.txt] — what stays in your browser.
