---
title: Psychophysical Experiment Engine — Reference
description: Every tab, control, readout, message, file format and link parameter in the Psychophysics Bench, with ranges and defaults.
product: Website › Tools › Perception and spectral › Psychophysical Experiment Engine
updated: 2026-09-25
---

# Psychophysics Bench reference

Address: https://auricartisan.com/tool/general/perception-and-neuroscience/psychophysical-experiment-engine/

## Tabs

| Tab | Contents | Opens at the time of writing |
|---|---|---|
| **Lab** | All experiment controls, the trial stage, response buttons, the staircase trace, readouts and warnings | Yes |
| **Method** | The contrast chain, the frequency axis, what each ladder estimates | No |
| **Paradigms** | Two scoring tasks and three withdrawn ones | No |
| **Data** | The register of 13 methods and constants; the tab label shows the count | No |
| **Export** | Trials CSV, session JSON, setup link | No |
| **Reference** | Eleven sources and their use | No |

## Lab tab — Task

| Control | Values | Default |
|---|---|---|
| **Task** | **Two-interval forced choice**, **Yes / no detection** | Two-interval forced choice |

## Lab tab — Stimulus

| Control | Range and step | Default |
|---|---|---|
| Stimulus type | **Gabor**, **Grating in an aperture** | Gabor |
| **Spatial frequency** | 0.25–20 c/deg, step 0.25 | 4.0 c/deg |
| **Orientation** | 0–179°, step 1 | 45° |
| **Envelope σ** | 0.10–2.00°, step 0.05 (Gabor only) | 0.50° |
| **Background** | Code 40–220, step 1 | Code 128 |

## Lab tab — Geometry

| Control | Range and step | Default |
|---|---|---|
| **Viewing distance** | 20–200 cm, step 1 | 57 cm |
| **Pixel pitch** | 0.05–0.6 mm, step 0.001 | 0.248 mm |

## Lab tab — Staircase

| Control | Values or range | Default |
|---|---|---|
| Procedure | **1-up / 2-down — 70.7%**, **3-down / 1-up — 79.4%**, **Bayesian tracker — this tool's own**, **Accelerated — this tool's own**, **Constant stimuli — no adaptation** | 1-up / 2-down |
| **Step** | 0.5–12 dB, step 0.5 | 2.0 dB |
| **Starting contrast** | 0.01–1, step 0.01 | 0.300 |
| **Stop after** | 4–24 reversals, step 2 | 12 reversals |
| **Trial ceiling** | 20–400, step 10 | 120 |

## Lab tab — Timing

| Control | Range and step | Default |
|---|---|---|
| **Stimulus** | 20–1000 ms, step 10 | 200 ms |
| **Between trials** | 100–2000 ms, step 50 | 600 ms |

Fixed timings: fixation cross 240 ms before each trial; 300 ms blank between the two intervals.

## Lab tab — Buttons

| Button | What it does |
|---|---|
| **Run** | Starts a measured run; disabled while a run is going |
| **Practice** | Starts a practice run of up to 12 trials with no reversal stop |
| **Stop** | Shown during a run; ends it (see [Run a session](run-a-session.md)) |
| **First interval** `←` / **Yes, I saw it** `←` | Answers first interval (two-interval) or yes (yes/no) |
| **Second interval** `→` / **No, I did not** `→` | Answers second interval or no |

## Lab tab — Stage and trace

| Element | Description |
|---|---|
| Run state | **not running**, **practice**, **running**, **stopped**, **done — N trials** |
| Stimulus stage | 256 × 256; shows the stimulus at the current contrast between runs |
| **Interval 1**, **Interval 2** | Light in turn during two-interval trials |
| **The staircase** | Contrast (log axis) against trial; grey warm-up reversals, red reversals used, gold dashed threshold; drawn for the up-down and accelerated staircases |

## Lab tab — Readouts

| Readout | Format |
|---|---|
| **Threshold, Michelson** | Four decimals, or **—** |
| **At what percentage** | 70.7%, 79.4%, 80.3% or 61.9%, or **not defined for this ladder** |
| **Reversals used** | **N of M**, **fewer than two reversals after the warm-up**, **N trials, posterior mean**, or **—** |
| **Delivered / asked** | Ratio, two decimals; highlighted when capped |
| **Trials run** | Count |
| **Proportion correct** | Three decimals |
| **Degrees per pixel** | Degrees, four decimals |
| **Nyquist limit of the grid** | c/deg, one decimal; highlighted when exceeded |

## Lab tab — Warnings

| Warning | When |
|---|---|
| **Above the pixel grid's Nyquist limit.** | Spatial frequency above the Nyquist limit |
| **The contrast asked for does not fit about this background.** | The contrast asked for exceeds what fits around the background |

## Method tab

| Control | Values |
|---|---|
| **Show** | **The contrast chain**, **The frequency axis**, **What each ladder estimates** |

## Data tab

| Control | What it does |
|---|---|
| **Status** | **All** (13), **Verbatim** (3), **Computed** (5), **Stand-in** (3), **Absent** (2) |
| Register row | Select, or press `Enter` or `Space`, to expand its note and **what it would take** |
| **Drop a measured gamma table** | Shown under **Calibrate the display**; not active in the current version |

Entries: **sRGB transfer and primaries**, **Transformed up-down rules**, **Extreme-proportion correction** (Verbatim); **Michelson contrast in luminance**, **Viewing geometry**, **Signal-detection formulae**, **Inverse normal CDF**, **Nonparametric bootstrap** (Computed); **Bayesian adaptive staircase**, **Psychometric function fit**, **Accelerated staircase** (Stand-in); **Weibull fit**, **ROC curve and its area** (Absent).

## Export tab

| Control | What it does |
|---|---|
| **What to take** | Preview **Every trial**, **The session** or **A link to this** |
| **Download the trials** | Saves `psychophysics-trials.csv` |
| **Download the session** | Saves `psychophysics-session.json` |
| **Copy a link to this setup** | Copies a link with every rail setting |

## Messages

| Message | Meaning |
|---|---|
| **Practice — arrow keys respond, Esc stops** | A practice run started |
| **Running — arrow keys respond, Esc stops** | A measured run started |
| **No trials yet — run the experiment first** | A download was requested with no trials |
| **Link copied** | The setup link is on the clipboard |
| **A trial could not be scored; the run stopped rather than record it** | A safety stop that should not occur with the two shipped tasks |

## File formats

| File | Format | Contents |
|---|---|---|
| `psychophysics-trials.csv` | CSV with `#` header lines | `trial,contrast,delivered,response,correct,rt_ms,interval,present,cpd` |
| `psychophysics-session.json` | JSON | Units, settings, procedure, threshold and its percentage, every trial |

Details are in [Export your data](export-your-data.md).

## Link parameters

`paradigm`, `stimType`, `cpd`, `orientation`, `sigmaDeg`, `meanCode`, `distanceCm`, `pitchMm`, `stair`, `stepDb`, `start`, `nReversals`, `trials`, `duration`, `iti`. Values are listed in [Export your data](export-your-data.md).
