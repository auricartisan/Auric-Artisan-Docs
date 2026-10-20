---
title: Psychophysical Experiment Engine — Getting started
description: Open the Psychophysics Bench, learn the Lab tab and measure a first contrast threshold with the default two-interval task.
product: Website › Tools › Perception and spectral › Psychophysical Experiment Engine
updated: 2026-09-25
---

# Getting started with the Psychophysics Bench

## Open the tool

Go to https://auricartisan.com/tool/general/perception-and-neuroscience/psychophysical-experiment-engine/ on a computer with a keyboard. The page opens on the **Lab** tab. A note strip above the tabs, which cannot be closed, says what the numbers are of: contrast in light, not in screen code values, and frequency in cycles per degree.

## The six tabs

| Tab | What it is for |
|---|---|
| **Lab** | Design and run an experiment and read the results |
| **Method** | What a contrast is on this page, how the frequency axis is built, and what each staircase estimates |
| **Paradigms** | The two tasks that can be scored and three that were withdrawn |
| **Data** | The register of every method and constant a threshold rests on (13 entries) |
| **Export** | Downloads of the trials and the session, and a link to the setup |
| **Reference** | Eleven sources and what each is used for |

> **Note:** At the time of writing, only the **Lab** tab opens. See [Troubleshooting](troubleshooting.md).

## A tour of the Lab tab

**The rail (left)**, from top to bottom:

- **Task** — **Two-interval forced choice** or **Yes / no detection**.
- **Stimulus** — **Gabor** or **Grating in an aperture**, then **Spatial frequency**, **Orientation**, **Envelope σ** and **Background**.
- **Geometry** — **Viewing distance** and **Pixel pitch**.
- **Staircase** — the procedure, then **Step**, **Starting contrast**, **Stop after** (reversals) and **Trial ceiling**.
- **Timing** — **Stimulus** duration and the pause **Between trials**.
- **Run**, **Practice** and, while a run is going, **Stop**.

**The stage (right)**:

- **The trial**, with the run state on the right (**not running**, **practice**, **running**, **stopped** or **done — N trials**). Between runs the square stage shows the stimulus at its current contrast, so you can see what you are about to measure.
- **Interval 1** and **Interval 2** markers, lit in turn during a two-interval trial.
- Two response buttons: **First interval** `←` and **Second interval** `→`, which become **Yes, I saw it** `←` and **No, I did not** `→` for the yes/no task.
- **The staircase**: a plot of contrast against trial number, with a key for **reversals used**, **warm-up, discarded** and **threshold**.
- Two rows of readouts: **Threshold, Michelson**, **At what percentage**, **Reversals used**, **Delivered / asked**, then **Trials run**, **Proportion correct**, **Degrees per pixel** and **Nyquist limit of the grid**.
- Warnings, when needed, about the Nyquist limit and about contrast that does not fit around the background.

## Measure your first threshold

1. Set **Viewing distance** to the distance from your eyes to the screen, and **Pixel pitch** to your screen's width in millimetres divided by its width in pixels. The defaults are 57 cm and 0.248 mm.
2. Keep the defaults for the rest: a Gabor at 4.0 c/deg, 45°, envelope 0.50°, background code 128; **1-up / 2-down — 70.7%** with a 2.0 dB step from a starting contrast of 0.300; 12 reversals or 120 trials; 200 ms stimulus and 600 ms between trials.
3. Dim the room, keep the screen brightness fixed, and sit at the distance you entered.
4. Select **Practice**. A fixation cross appears, then **Interval 1** lights with a patch or a blank, then **Interval 2**. The patch is in exactly one of them. Press `←` for the first or `→` for the second. If you did not see it, guess: chance is 50%.
5. After a few practice trials, select **Stop** or let practice finish (it ends after 12 trials).
6. Select **Run** and keep answering. The patch will get fainter as you answer correctly and stronger after mistakes. The run stops by itself at 12 reversals or 120 trials, whichever comes first, and the state reads **done — N trials**.
7. Read **Threshold, Michelson**: the contrast at which you were right 70.7% of the time, as **At what percentage** says. **Reversals used** shows how many turning points went into it.

You should see a staircase trace that drops from 0.3, zig-zags, and settles in a band, with a dashed gold line at your threshold.

## Next steps

- [Design an experiment](design-an-experiment.md) explains every setting.
- [Run a session](run-a-session.md) covers stopping rules and good practice.
- [Read the results](read-the-results.md) explains the numbers and the trace.
