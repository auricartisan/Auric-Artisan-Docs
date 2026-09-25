---
title: Perception and Vision — Troubleshooting
description: Symptoms, causes and fixes for the camera, WebGL2, uploads, readouts that say n/a, links and copying in Perception Vision.
product: Website › Tools › Perception and spectral › Perception and Vision
updated: 2026-09-25
---

# Troubleshooting Perception and Vision

## The camera does not start

**Symptom:** after choosing **Camera** or selecting **Start or stop**, a message beginning **Camera:** appears, the status reads **unavailable** and the source goes back to **Test card**.

**Why:** the camera needs permission, and auricartisan.com currently does not allow its pages to use the camera. Browsers also block cameras on pages that are not secure, and a camera already in use by another application may refuse.

**What to do:** take a screenshot or photo and load it with **Uploaded image**.

## The page says "No WebGL2 here."

**Why:** your browser or device does not provide WebGL2, or it is switched off.

**What to do:** nothing is required: every simulation runs on the processor (**CPU**) and gives the same colours, more slowly. The **GPU** button is disabled and **GPU and CPU agree** reads **not run**. To use the GPU, update the browser or enable hardware acceleration in its settings.

## My uploaded image looks smaller than the original

**Why:** images larger than 1200 × 900 pixels are scaled down to fit. Smaller images are shown at their own size.

**What to do:** nothing; to inspect detail, crop the image before loading it. Double-click the frame to enlarge the view.

## The grey ramp shows non-zero numbers

**Why:** under **Scotopic**, **Mesopic**, **Lens yellowing**, **Cataract** and **Light adaptation**, shifting greys is the effect being simulated. Under **Colour vision** the numbers should be zero; the strip shows them in red if not.

**What to do:** check which simulation is selected. Adjustments (contrast, gamma, glare, noise) and the illuminant do not affect the strip.

## Readouts show "n/a", "spatial mode" or "n/a — spatial"

**Why:** **Cataract**, **Central loss** and **Acuity** change pixels according to their neighbours or their position, so per-colour measurements do not apply.

**What to do:** use **Difference** under **Compare** to see where these simulations change the image.

## "GPU and CPU agree" shows a number followed by "off"

**Why:** the GPU's answer differs from the processor's by more than 2 code values on at least one of the 216 test colours. This can happen with unusual graphics drivers.

**What to do:** switch **Renderer** to **CPU** for figures you intend to rely on. The settings file records the check.

## The divider moves when I click the frame

**Why:** in **Split** mode, pressing anywhere on the frame moves the divider there.

**What to do:** use **Simulated only** if you do not want a split, or set **Divider** with its slider.

## The Install a table area on the Data tab does nothing

**Why:** the area is shown but not active in the current version.

**What to do:** nothing; the tool's tables cannot be replaced from a file at present.

## A preset did not reset my adjustments

**Why:** a preset only sets the values it lists. Earlier adjustments stay.

**What to do:** select **Reset** first, then the preset.

## A link or loaded settings file did not bring back my image

**Why:** links and settings files carry settings, not images.

**What to do:** after opening the link or loading the settings, choose **Uploaded image** and the file again. Links also omit the divider position, **Daltonise instead of simulate** and **Fixation cross**.

## Nothing is copied, or the page says "Copy blocked"

**Why:** the browser refused clipboard access.

**What to do:** click inside the page and try again, or use **Download the CSV** or **Download the settings**.

## Sliders are slow with a large image

**Why:** the readouts and the renderer check rerun after every change, and the CPU renderer processes every pixel.

**What to do:** use the **GPU** renderer if available, or load a smaller image.
