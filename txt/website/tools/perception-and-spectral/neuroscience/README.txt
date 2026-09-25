==============================================================================
NEUROSCIENCE (VISUAL PATHWAY)
==============================================================================
What the Visual Pathway tool does, who it is for, where to find it and how to
follow a first grating from the cones to V4.
Area: Website › Tools › Perception and spectral › Neuroscience   Updated: 2026-09-25

The Neuroscience tool, whose page is titled Visual Pathway, follows one
stimulus through five stages of the early visual system, one stage at a time.
It starts with a colour on your screen, turns it into the signals of the three
cone types, combines those into opponent channels, and then shows what a
retinal centre-surround cell, a bank of V1 orientation filters, a V2 boundary
signal and a V4 colour cell would each respond to. Every stage produces a map
you can view beside the stimulus, with a scale bar that says what a bright
pixel means.

The stimulus is a grating, a pattern of stripes whose spatial frequency you
set in cycles per degree of visual angle. Because cycles per degree depends on
how far you sit from the screen and how large its pixels are, the page asks
for both and derives every frequency from them. It also warns you when the
frequency you ask for is finer than your pixel grid can draw.

The tool is an educational approximation, not a physiological measurement. The
page says so, and its Data tab lists which of its numbers come from published
sources and which are its own. In particular, the cone curves drawn in the
figure are the tool's own and put the L and M cones at the same wavelength,
while the cone signals that drive the stages come from a published transform.
Everything runs in your browser.

WHO IT IS FOR
=============

  - Students and teachers of colour vision and visual neuroscience who want to
    see what each stage computes.
  - Designers and developers curious about why some colour pairs are hard to
    see as patterns, and what "opponent colour" means.
  - Anyone who wants a worked, traceable example of cone signals and opponent
    channels for a list of colours.

WHERE TO FIND IT
================

Open
https://auricartisan.com/tool/general/perception-and-neuroscience/neuroscience/
in a current desktop browser. It is listed as Neuroscience on the Collections
page (https://auricartisan.com/collections/) and as Neuroscience of Color in
the site menu. No installation or account is needed.

QUICK START
===========

  1. Open the tool. The Lab tab is selected and a blue grating is shown at 4.0
     c/deg and 25% contrast.
  2. Under Geometry, set Viewing distance to how far your eyes are from the
     screen and Pixel pitch to your screen's pixel size (screen width in
     millimetres divided by its width in pixels).
  3. Under Show, choose Retina, on-centre. The right-hand canvas shows the
     retinal map and the scale bar under it gives its range.
  4. Switch Show to LGN, L − M, then LGN, S − (L+M)/2, and watch the chromatic
     channels respond to the grating.
  5. Choose V1, preferred orientation to see the orientation map as a colour
     wheel.
  6. Change the Carrier from Chromatic to Luminance and compare the maps
     again.
  7. Open the Export tab, paste your own hex colours into Colours and select
     Download the CSV to take away their cone signals and opponent values.

WHAT YOU CAN DO
===============

  - Show a chromatic or luminance grating, or a built-in test card, and set
    its base colour, frequency and contrast.
  - State your viewing distance and pixel pitch, and read the degrees per
    pixel and the Nyquist limit of your screen.
  - Switch each of the five stages on or off, and view any of nine maps in one
    of three colourmaps.
  - Tune the retinal centre-surround, the V1 Gabor bank and the V4 preferred
    direction.
  - Simulate protanopia, deuteranopia or tritanopia before the stages see the
    stimulus.
  - Compare the cone-curve figure with the published peak wavelengths, and
    install a cone table of your own.
  - See every stage side by side on the Cells tab, and the colour chain step
    by step on the Pipeline tab.
  - Export a colour list as CSV or to the clipboard, the active map as PNG,
    the settings as JSON, or a link to the view.

IN THIS FOLDER
==============

  - docs/ [docs/README.txt] — how to use the tool.
    - Getting started [docs/getting-started.txt] — open it, the screen tour,
      the first grating.
    - Explore the five stages [docs/explore-the-stages.txt] — the stimulus,
      the stages, the maps and how to read them.
    - Cones, opponent channels and the cone table
      [docs/cones-and-opponent-channels.txt] — the Pipeline tab, the cone
      figure and installing your own table.
    - Export and share [docs/export-and-share.txt] — the colour list, the map,
      the settings file and links.
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
