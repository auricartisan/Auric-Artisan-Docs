---
title: Psychophysical Experiment Engine — Run a session
description: Practise, run a measured session, respond with keys or buttons, and understand when and how a run stops.
product: Website › Tools › Perception and spectral › Psychophysical Experiment Engine
updated: 2026-09-25
---

# Run a session

## Before you start

- Sit at the **Viewing distance** you entered and keep your head still.
- Dim the room and turn off automatic brightness, night-light or colour-shifting modes on your screen. Keep brightness fixed for the whole session.
- Look at the centre of the stage throughout.
- Close other busy windows; a slow computer can delay intervals.

## Practise

Select **Practice**. A practice run shows up to 12 trials (fewer if **Trial ceiling** is lower) and does not stop on reversals. Its answers appear in the readouts while you practise, and are cleared when you start a measured run. A message confirms **Practice — arrow keys respond, Esc stops**, and the run state reads **practice**.

## Run

Select **Run**. The message **Running — arrow keys respond, Esc stops** appears, the run state reads **running**, **Run** and **Practice** are disabled, and **Stop** appears.

### What one trial looks like

**Two-interval forced choice**

1. A fixation cross on the background grey, for 240 ms.
2. **Interval 1** lights and the stage shows either the patch or a blank patch of the background, for the **Stimulus** duration.
3. A 300 ms blank.
4. **Interval 2** lights and shows the other one.
5. The stage returns to the background and waits for your answer.

**Yes / no detection**

1. A fixation cross for 240 ms.
2. One interval: the patch on about half of trials, a blank on the rest, for the **Stimulus** duration.
3. The stage returns to the background and waits for your answer.

### Answering

| Task | Left | Right |
|---|---|---|
| Two-interval forced choice | `←` or **First interval** | `→` or **Second interval** |
| Yes / no detection | `←` or **Yes, I saw it** | `→` or **No, I did not** |

Answers count only after the intervals have finished. There is no time limit, but answer promptly: the page records your response time. When you are unsure in the two-interval task, guess. The method assumes you will be guessing near threshold, and waiting to be certain biases the result upwards.

After each answer the page scores the trial, updates the staircase and the readouts, waits for the **Between trials** pause, and starts the next trial.

## When a run stops

| Procedure | Stops at |
|---|---|
| **1-up / 2-down**, **3-down / 1-up**, **Accelerated** | The **Stop after** reversal count, or the **Trial ceiling**, whichever comes first |
| **Bayesian tracker**, **Constant stimuli** | The **Trial ceiling** |

The run state then reads **done — N trials** and the stage shows the background.

To stop early, press `Esc` while the page is waiting for your answer, or select **Stop**. **Stop** takes effect at the end of the current interval; if the page is already waiting for your answer, the run ends when you next press `Esc`, a response key or a response button, and that last answer is not recorded. The state then reads **stopped**, and the trials completed so far remain in the readouts.

A normal session is 60 to 120 trials. Starting a new run clears the previous one's trials.

## Good practice

- Run **Practice** once before every measured session.
- Measure more than once and compare; single runs vary.
- Keep the geometry, background and room lighting the same between runs you want to compare.
- If the trace climbs to the top and stays there, you could not see the patch at any contrast: check the frequency against the Nyquist limit, the background, and the **Delivered / asked** readout.

You should now have a completed run with a threshold on the Lab tab; [Read the results](read-the-results.md) explains it.
