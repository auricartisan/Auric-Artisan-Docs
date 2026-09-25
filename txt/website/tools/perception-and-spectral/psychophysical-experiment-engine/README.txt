==============================================================================
PSYCHOPHYSICAL EXPERIMENT ENGINE
==============================================================================
What the Psychophysics Bench does, who it is for, where to find it and how to
measure a first contrast threshold.
Area: Website › Tools › Perception and spectral › Psychophysical Experiment Engine   Updated: 2026-09-25

The Psychophysical Experiment Engine, whose page is titled Psychophysics
bench, measures a contrast detection threshold: the faintest pattern you can
reliably see. It shows a Gabor patch (a soft-edged patch of stripes) or a
grating in a circular aperture, asks you to say where or whether you saw it,
and uses an adaptive staircase to move the contrast up after errors and down
after correct answers, so that most trials fall near your threshold. At the
end it reports the threshold as a Michelson contrast, together with the
percentage correct that the threshold belongs to.

The bench states its units. Contrast is Michelson contrast in relative
luminance, about a background grey you choose, passed through the sRGB
transfer curve; spatial frequency is in cycles per degree of visual angle,
worked out from a viewing distance and pixel pitch you enter. When your screen
cannot show the contrast or the frequency you asked for, the page says so
instead of silently drawing something else.

It is an educational instrument that runs in your browser, not a calibrated
laboratory display. It assumes your screen follows the sRGB standard rather
than measuring it. Two of the five staircase procedures are published methods
(Levitt 1971); the other three are the tool's own and are named as such.

  | Important: At the time of writing (25 September 2026), only the Lab tab of
  | this page opens: selecting Method, Paradigms, Data, Export or Reference does
  | not change the view. You can design and run experiments and read the results
  | on the Lab tab, but the download and link buttons, which are on the Export
  | tab, cannot be reached. These pages document every tab so they remain useful
  | when the tabs work; see Troubleshooting [docs/troubleshooting.txt] for
  | workarounds.

WHO IT IS FOR
=============

  - Students and teachers of psychophysics and vision science who want to run
    a real staircase and see how it converges.
  - Designers and developers curious about how faint a pattern people can
    actually see on a screen.
  - Anyone who wants to understand what a threshold "at 70.7% correct" means.

WHERE TO FIND IT
================

Open
https://auricartisan.com/tool/general/perception-and-neuroscience/psychophysical-experiment-engine/
on a desktop or laptop with a keyboard. It is listed as Psychophysics Engine
on the Collections page (https://auricartisan.com/collections/) and as
Psychophysical Experiment Engine in the site menu.

QUICK START
===========

  1. Open the tool. The Lab tab shows a Gabor patch at the starting contrast.
  2. Under Geometry, set Viewing distance to your eye-to-screen distance and
     Pixel pitch to your screen's pixel size.
  3. Leave Task at Two-interval forced choice and Staircase at 1-up / 2-down —
     70.7%.
  4. Dim the room, sit at the stated distance and look at the centre of the
     stage.
  5. Select Practice and answer a few trials: press `←` if the patch was in
     the first interval and `→` if it was in the second. Guess when unsure.
  6. Select Run and answer until the run stops by itself (after 12 reversals
     or 120 trials by default).
  7. Read Threshold, Michelson and At what percentage, and look at the
     staircase trace.

WHAT YOU CAN DO
===============

  - Choose between two tasks: two-interval forced choice and yes/no detection.
  - Set the stimulus: Gabor or grating, spatial frequency, orientation,
    envelope size and background grey.
  - State the viewing geometry and read the degrees per pixel and your
    screen's Nyquist limit.
  - Choose one of five procedures: two transformed up-down staircases, a
    Bayesian tracker, an accelerated staircase or constant stimuli, and set
    the step, starting contrast, stopping rule and trial ceiling.
  - Set stimulus duration and the pause between trials.
  - Run practice and measured sessions with the keyboard or on-screen buttons,
    and stop at any time.
  - Read the threshold, its target percentage, the reversals used, the
    delivered contrast, trials run and proportion correct, with a live
    staircase trace.
  - Export every trial as CSV, the session as JSON, or a link to the setup
    (from the Export tab, when it opens).

IN THIS FOLDER
==============

  - docs/ [docs/README.txt] — how to use the tool.
    - Getting started [docs/getting-started.txt] — open it, the screen tour, a
      first threshold.
    - Design an experiment [docs/design-an-experiment.txt] — tasks, stimulus,
      geometry, staircases and timing.
    - Run a session [docs/run-a-session.txt] — practice, the trial sequence,
      responding and stopping.
    - Read the results [docs/read-the-results.txt] — the threshold, the
      readouts, the trace and the explanation tabs.
    - Export your data [docs/export-your-data.txt] — the trials CSV, the
      session JSON and setup links.
    - Reference [docs/reference.txt] — every control, readout, tab and file
      format.
    - Troubleshooting [docs/troubleshooting.txt] — symptoms, causes, fixes and
      workarounds.
    - FAQ [docs/faq.txt] — short answers to common questions.
  - others/ [others/README.txt] — background material.
    - Glossary [others/glossary.txt] — psychophysics terms used in this tool.
    - Shortcuts [others/shortcuts.txt] — the response keys and other actions.
    - Limits and accuracy [others/limits-and-accuracy.txt] — what is
      published, what is the tool's own, what is not shown.
    - Related [others/related.txt] — related tools and Learn articles.
    - Release notes [others/release-notes.txt] — user-facing history.
    - Privacy [others/privacy.txt] — what stays in your browser.
