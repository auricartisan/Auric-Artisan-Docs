---
title: Psychophysical Experiment Engine — Design an experiment
description: Choose a task, build the stimulus, state the viewing geometry, pick a staircase procedure and set its parameters and the timing.
product: Website › Tools › Perception and spectral › Psychophysical Experiment Engine
updated: 2026-09-25
---

# Design an experiment

Every setting in this guide is on the **Lab** rail. Settings take effect at the next **Run** or **Practice**; the stage preview updates as you change them.

## What a threshold is

**Psychophysics** measures the relationship between a physical stimulus and what a person reports. A **detection threshold** is the stimulus strength at which an observer reports the stimulus a stated proportion of the time. The proportion matters: "your threshold is 0.01" means nothing until it says "at 70.7% correct" or "at 79.4% correct", because the chance of a correct answer rises smoothly with contrast. That rising curve is the **psychometric function**. This bench always reports a threshold together with the percentage it belongs to, and says when a procedure has no stated percentage.

## 1. Choose the task

| Task | What happens on a trial | Chance level |
|---|---|---|
| **Two-interval forced choice** (default) | Two intervals are shown one after the other, marked **Interval 1** and **Interval 2**. The patch is in exactly one, chosen at random. You say which. | 50% |
| **Yes / no detection** | One interval. The patch is present on a random half of trials and absent on the rest. You say whether you saw it. | No guess rate of this kind; your answers depend on how willing you are to say yes |

**Forced choice** is the usual method for thresholds because guessing is built in: you must answer, and the known chance level (50%) lets the analysis separate seeing from guessing. **Yes/no** is the task that has stimulus-absent trials, so it is the only one that can separate sensitivity from willingness to say yes (signal detection theory). In yes/no, a correct "no" on a blank trial counts as correct and moves the staircase just as a correct "yes" does.

Three more tasks from an earlier version (m-alternative forced choice, same/different and odd-one-out) are withdrawn because they could never score a trial correct; the **Paradigms** tab explains each.

## 2. Build the stimulus

| Control | Range | Default | What it sets |
|---|---|---|---|
| Stimulus type | **Gabor**, **Grating in an aperture** | Gabor | A **Gabor** is a sine-wave grating that fades out under a Gaussian envelope; a grating in an aperture has the same stripes inside a hard-edged circle |
| **Spatial frequency** | 0.25–20 c/deg, step 0.25 | 4.0 c/deg | How fine the stripes are |
| **Orientation** | 0–179°, step 1 | 45° | The angle of the stripes |
| **Envelope σ** | 0.10–2.00°, step 0.05 | 0.50° | The size of the Gabor's Gaussian envelope, in degrees of visual angle (used by the Gabor only) |
| **Background** | Code 40–220, step 1 | Code 128 | The grey the contrast swings about, as an 8-bit screen value |

Human contrast sensitivity is highest at a few cycles per degree, so thresholds are lowest near the default 4 c/deg.

### How contrast is defined

**Michelson contrast** is (Lmax − Lmin) ÷ (Lmax + Lmin), where L is luminance. The bench converts the **Background** code value to relative luminance through the sRGB transfer curve, places the stripes' peaks and troughs symmetrically around that luminance, and only then converts back to code values. So a contrast of 0.02 on this page is 0.02 in light, not in screen numbers.

The background limits how much contrast fits. A trough cannot be darker than black and a peak cannot be brighter than white, so the largest contrast possible about a background of relative luminance L is 1 ÷ L − 1, capped at 1. Around the default code 128 (relative luminance about 0.216) the full range up to 1.0 fits; around code 200 (about 0.578) the most is about 0.73, and around code 220 (about 0.716) about 0.40. When a staircase asks for more than fits, the bench shows the largest contrast that fits, reports **Delivered / asked** below 1.00, and shows the note **The contrast asked for does not fit about this background.** It never clips one side of the stripes, because that would be a different stimulus.

## 3. State the viewing geometry

| Control | Range | Default |
|---|---|---|
| **Viewing distance** | 20–200 cm, step 1 | 57 cm |
| **Pixel pitch** | 0.05–0.6 mm, step 0.001 | 0.248 mm |

Cycles per degree and an envelope in degrees are undefined without these. At 57 cm one degree covers very nearly 1 cm of screen. Your pixel pitch is your screen's visible width in millimetres divided by its horizontal resolution.

The readouts **Degrees per pixel** (0.0249° at the defaults) and **Nyquist limit of the grid** (20.1 c/deg at the defaults) update as you change them. The Nyquist limit is the finest frequency the pixel grid can show: half a cycle per pixel. Above it the note **Above the pixel grid's Nyquist limit** appears, because what reaches your eye would be an alias at a different frequency and contrast. Lower the frequency, or check the geometry: the limit rises as you sit further away and as pixels get smaller.

## 4. Choose the procedure

An **adaptive staircase** chooses each trial's contrast from your previous answers, lowering it after correct answers and raising it after errors, so trials cluster near your threshold instead of being wasted where the patch is obviously visible or invisible. A **reversal** is a trial where the staircase changes direction.

| Procedure | How it moves | Converges at | Source |
|---|---|---|---|
| **1-up / 2-down — 70.7%** (default) | Down one step after two correct in a row, up one step after any error | 70.7% correct (the p at which p² = 0.5) | Levitt 1971 |
| **3-down / 1-up — 79.4%** | Down after three correct in a row, up after any error | 79.4% correct (p³ = 0.5) | Levitt 1971 |
| **Bayesian tracker — this tool's own** | Updates a probability distribution over the threshold after every trial and tests at its mean | About 80.3% correct in two-interval, 61.9% in yes/no | The tool's own |
| **Accelerated — this tool's own** | Moves every trial; halves the step at each reversal and doubles it after three moves in the same direction | No stated percentage | The tool's own |
| **Constant stimuli — no adaptation** | Every trial at the starting contrast | Not a threshold procedure here | — |

### Staircase parameters

| Control | Range | Default | Applies to |
|---|---|---|---|
| **Step** | 0.5–12 dB, step 0.5 | 2.0 dB | 1-up / 2-down, 3-down / 1-up, Accelerated |
| **Starting contrast** | 0.01–1, step 0.01 | 0.300 | All |
| **Stop after** | 4–24 reversals, step 2 | 12 reversals | 1-up / 2-down, 3-down / 1-up, Accelerated |
| **Trial ceiling** | 20–400 trials, step 10 | 120 | All |

**Step** is a ratio in decibels of contrast: each step multiplies or divides the contrast by 10^(dB ÷ 20), so 2 dB is a factor of about 1.26 at any contrast. A ratio step resolves a threshold of 0.005 as finely as one of 0.5, which a fixed step cannot. For the two up-down staircases the step halves after the second reversal and halves again after the fourth. The accelerated staircase starts at the set step, halves it at each reversal (down to one eighth) and doubles it after three moves in one direction (up to four times the set step). Contrast is kept between 0.0001 and 1.

**The Bayesian tracker** keeps a probability for 240 candidate thresholds spread evenly on a logarithmic scale from 0.0001 to 1. It starts from a Gaussian prior centred on a quarter of the starting contrast with a width of one decade (1 dex), assumes a Weibull psychometric function with a slope of 3.5, a lapse rate of 0.02 and the task's guess rate, and after each answer tests at the mean of the updated distribution. Its slope, lapse rate and prior are the tool's choices, not estimated from your data, which is why it is not called QUEST.

**Constant stimuli** here shows every trial at the starting contrast, so it measures your proportion correct at one contrast. The classical method of constant stimuli uses several fixed levels in random order; the bench does not do that.

## 5. Set the timing

| Control | Range | Default | What it sets |
|---|---|---|---|
| **Stimulus** | 20–1000 ms, step 10 | 200 ms | How long each interval shows the patch or blank |
| **Between trials** | 100–2000 ms, step 50 | 600 ms | The pause after your answer before the next trial |

A fixation cross shows for 240 ms before each trial, and in the two-interval task the intervals are separated by a 300 ms blank. There is no time limit on answering. Browser timing follows your screen's refresh, so very short durations are rounded to whole frames by the display.

## 6. Save your design

When the **Export** tab opens, **Copy a link to this setup** copies every rail setting as a link. Until then, see [Export your data](export-your-data.md) for how to build that link by hand.

You should now have a stimulus, geometry and procedure that match the question you want to answer.
