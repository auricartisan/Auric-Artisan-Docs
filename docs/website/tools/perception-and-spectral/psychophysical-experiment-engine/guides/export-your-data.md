---
title: Psychophysical Experiment Engine — Export your data
description: The trials CSV, the session JSON and setup links on the Export tab, their exact contents, and what to do while the Export tab does not open.
product: Website › Tools › Perception and spectral › Psychophysical Experiment Engine
updated: 2026-09-25
---

# Export your data

> **Important:** At the time of writing, the **Export** tab does not open, so the three buttons below cannot be reached. The last section of this page describes what you can do meanwhile.

## The Export tab

**What to take** switches the preview on the right between **Every trial** (the CSV), **The session** (the JSON, first part) and **A link to this**. The note above the preview gives the number of rows. Nothing leaves the page until you press a button:

| Button | Result |
|---|---|
| **Download the trials** | Saves `psychophysics-trials.csv` |
| **Download the session** | Saves `psychophysics-session.json` |
| **Copy a link to this setup** | Copies a link with every rail setting; shows **Link copied**, or the link itself if the clipboard is unavailable |

With no trials yet, the download buttons show **No trials yet — run the experiment first**.

## The trials CSV

The file starts with header lines that record what the numbers mean, then one row per trial:

```text
# Auric Artisan · psychophysics bench · 2026-09-25T10:00:00.000Z
# contrast_unit    = michelson, relative luminance, sRGB EOTF
# mean_luminance   = 0.2159 (code 128)
# frequency_unit   = cycles per degree
# viewing_distance = 570 mm ; pixel_pitch = 0.248 mm ; deg_per_px = 0.0249
# display_gamma    = sRGB standard curve, not a measurement of this screen
# paradigm         = Two-interval forced choice
# staircase        = 1-up / 2-down, 2.0 dB step, target 70.7%
# reportable       = false   (the fit is this tool's own; see the Data register)
trial,contrast,delivered,response,correct,rt_ms,interval,present,cpd
```

| Column | Meaning |
|---|---|
| `trial` | Trial number |
| `contrast` | The Michelson contrast the procedure asked for |
| `delivered` | The contrast the screen could show; lower than `contrast` when capped |
| `response` | `0` (first interval) or `1` (second) in two-interval; `yes` or `no` in yes/no |
| `correct` | `1` or `0` |
| `rt_ms` | Response time from the end of the stimulus, in milliseconds |
| `interval` | The interval that held the patch (`0` or `1`); `-1` in yes/no |
| `present` | `1` if the patch was shown, `0` if not (always `1` in two-interval) |
| `cpd` | Spatial frequency in cycles per degree |

The header carries the background luminance and the geometry because a Michelson contrast cannot be reconstructed without its mean, and a frequency in cycles per degree means nothing without a viewing distance.

## The session JSON

`psychophysics-session.json` contains:

| Field | Meaning |
|---|---|
| `tool`, `version`, `recorded` | `psychophysics-bench`, `2` and the time of export |
| `units` | Contrast unit, `mean_luminance`, `mean_code`, frequency unit and `deg_per_px` |
| `display_gamma` | "sRGB standard curve, not a measurement of this screen" |
| `settings` | Every rail setting |
| `paradigm`, `staircase` | The task and a description of the procedure and step |
| `threshold`, `threshold_at` | The current threshold and its proportion correct, or `null` |
| `reversals_used` | The same text as the readout |
| `trials` | Number of trials |
| `reportable` | Whether the result may be reported as a published quantity (currently `false`) |
| `data` | Every trial, with the fields of the CSV |

## Setup links

A setup link opens the bench with the same rail settings. It uses these parameters:

| Parameter | Control | Values |
|---|---|---|
| `paradigm` | Task | `2afc`, `yesno` |
| `stimType` | Stimulus type | `gabor`, `grating` |
| `cpd` | Spatial frequency | 0.25–20 |
| `orientation` | Orientation | 0–179 |
| `sigmaDeg` | Envelope σ | 0.1–2 |
| `meanCode` | Background | 40–220 |
| `distanceCm` | Viewing distance | 20–200 |
| `pitchMm` | Pixel pitch | 0.05–0.6 |
| `stair` | Staircase | `1u2d`, `3d1u`, `bayes`, `accel`, `constant` |
| `stepDb` | Step | 0.5–12 |
| `start` | Starting contrast | 0.01–1 |
| `nReversals` | Stop after | 4–24 |
| `trials` | Trial ceiling | 20–400 |
| `duration` | Stimulus (ms) | 20–1000 |
| `iti` | Between trials (ms) | 100–2000 |

A link carries settings, not results.

## While the Export tab does not open

- **Share or save a setup:** build the link by hand. Start from the tool address and add the parameters you want to set, for example:

  ```text
  https://auricartisan.com/tool/general/perception-and-neuroscience/psychophysical-experiment-engine/?paradigm=yesno&cpd=2&stair=3d1u&trials=160
  ```

  Parameters you leave out keep their defaults.
- **Keep a result:** write down **Threshold, Michelson**, **At what percentage**, **Reversals used**, **Delivered / asked**, **Trials run** and **Proportion correct**, together with your settings, before starting another run. A screenshot of the Lab tab records the trace as well. Double-clicking the trace enlarges it first.
- **Per-trial data** cannot be taken away until the tab opens.
