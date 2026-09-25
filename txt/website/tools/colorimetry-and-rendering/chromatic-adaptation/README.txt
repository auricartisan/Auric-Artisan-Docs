==============================================================================
CHROMATIC ADAPTATION
==============================================================================
What the Chromatic Adaptation lab does, who it is for, where to find it and
how to adapt your first image.
Area: Website › Tools › Colorimetry and rendering   Updated: 2026-09-25

When you walk from daylight into a room lit by a tungsten lamp, white paper
looks orange for a moment and then white again. Your eyes have rebalanced to
the new light. This is chromatic adaptation, and colour science models it with
chromatic adaptation transforms (CATs) that convert a colour seen under one
white point into the colour that would look the same under another.

The Chromatic Adaptation lab applies eight published transforms (Bradford, Von
Kries, CAT02, CAT16, Sharp, CMCCAT2000, HPE and plain XYZ scaling) to a
photograph of your own or to a built-in test sweep, between any two of 12
standard illuminants. It also models the time the eye takes to adapt, using
the two-phase time course measured by Fairchild and Reniff (1995): about half
the adaptation happens within a second and the rest over tens of seconds. You
can scrub or animate that timeline, and set how complete the adaptation
becomes.

Supporting views show the matrices behind each transform (with copy-ready
code), compare all eight on your illuminant pair, list every dataset the lab
uses and its status, and export the result as an image, JSON or a shareable
link. Everything runs on your device; images are never uploaded.

WHO IT IS FOR
=============

  - Photographers and designers who want to see how a white-balance change
    affects colours.
  - Developers implementing colour management who need a CAT matrix in NumPy,
    JSON, CSS or GLSL form.
  - Students of colour science learning von Kries adaptation and the
    differences between transforms.
  - Researchers who want a quick visual demonstration of the adaptation time
    course.

WHERE TO FIND IT
================

  - Address:
    https://auricartisan.com/tool/general/colorimetry/chromatic-adaptation-dynamic/
  - In the tool collection (https://auricartisan.com/collections/) under
    Colorimetry, as Chromatic Adaptation.
  - No account is needed. It works in current desktop and mobile browsers.

QUICK START
===========

  1. Open
     https://auricartisan.com/tool/general/colorimetry/chromatic-adaptation-dynamic/.
  2. Select Generate the sample sweep (or Choose an image to use your own
     photo).
  3. Leave Source illuminant on D65 and set Destination illuminant to CIE A
     (2856 K) — tungsten.
  4. Keep CAT Method on Bradford (Lam 1985).
  5. Drag Time (scrubber) from 0 to 5 s and watch the adapted image warm up as
     adaptation progresses.
  6. Select Animate to play the five seconds in real time.
  7. Open the Matrix tab to see the adaptation matrix, then Export and select
     Export Frame (PNG).

WHAT YOU CAN DO
===============

  - Adapt an image between 12 illuminants: D65, D50, D55, D60, D75, A, B, C,
    E, F2, F7 and F11.
  - Choose among eight chromatic adaptation transforms.
  - Set the final degree of adaptation D from 0 (none) to 1 (complete).
  - Scrub or animate a five-second adaptation timeline, and explore the full
    two-minute time course on the Dynamics tab.
  - Inspect the RGB histogram, the adaptation curve, cone (LMS) channel
    scaling and the two illuminant spectra.
  - View and copy the adaptation matrix in NumPy, JSON, CSS matrix3d or GLSL
    form, with a round-trip check.
  - Compare what all eight transforms do to your illuminant pair.
  - Adapt a list of up to 50 HEX colours and read their ΔE₀₀ and LCh°.
  - Export JSON, a PNG frame, or a share link.

IN THIS FOLDER
==============

  - docs/ [docs/README.txt] — how to use the lab
    - Getting started [docs/getting-started.txt]
    - Adapt an image to a new light [docs/adapt-an-image.txt]
    - Explore the adaptation time course [docs/explore-the-time-course.txt]
    - Compare transforms and copy a matrix
      [docs/compare-transforms-and-copy-matrices.txt]
    - Adapt a list of colours [docs/adapt-a-colour-list.txt]
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
