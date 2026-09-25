---
title: Perception and spectral tools — Overview
description: What the three perception and neuroscience tools and the two spectral tools on auricartisan.com are for, where to find them, and which one to open for each job.
product: Website › Tools › Perception and spectral
updated: 2026-09-25
---

# Perception and spectral tools

This group holds five workbenches for questions that sit behind a colour value rather than in it. Three of them are about the observer: how a colour travels through the early visual system, how a scene looks to a different visual system, and how to measure the faintest contrast a person can see. Two of them are about light and matter: what colour a dye bath makes under a named light, and how a material looks under a light source at a given angle.

All five are teaching and exploration tools that show their working. Each page says, in a strip at the top that cannot be closed, what its pictures and numbers rest on. Each has a **Data** tab that lists every table, formula and model the tool uses and marks it **Verbatim** (taken unchanged from a publication or standard), **Computed** (derived from verbatim data by stated arithmetic), **Stand-in** (this tool's own values, chosen to be plausible) or **Absent** (not held, with a note on what it would take). A figure that rests on a stand-in or an absent entry is never presented as a published value. None of the five is a clinical, physiological or laboratory instrument.

Everything runs in your browser. Nothing you load, type or measure is uploaded, and nothing leaves the page until you press an export or copy button.

## Where to find them

The group has two hub addresses:

- https://auricartisan.com/tool/general/perception-and-neuroscience/ (the site menu calls it **Perception and Neuroscience Hub**)
- https://auricartisan.com/tool/general/spectral-tools/ (the site menu calls it **Spectral Tools Hub**)

Both addresses currently forward you to the Collections page at https://auricartisan.com/collections/, which lists every tool on the site. Find the tools there, or open them directly from the table below. The Collections page is described in [Collections](../../library/collections/README.md).

## The tools

| Tool | Page title | Address | Use it to |
|---|---|---|---|
| [Neuroscience](neuroscience/README.md) | Visual Pathway | https://auricartisan.com/tool/general/perception-and-neuroscience/neuroscience/ | Follow a grating from cone signals through opponent channels, retina, V1, V2 and V4 |
| [Perception and Vision](perception-and-vision/README.md) | Perception Vision | https://auricartisan.com/tool/general/perception-and-neuroscience/perception-vision/ | Simulate colour vision deficiency, night vision, lens ageing, cataract, central loss and acuity over an image |
| [Psychophysical Experiment Engine](psychophysical-experiment-engine/README.md) | Psychophysics Bench | https://auricartisan.com/tool/general/perception-and-neuroscience/psychophysical-experiment-engine/ | Measure a contrast detection threshold with an adaptive staircase |
| [Industrial Dye Chemistry](industrial-dye-chemistry/README.md) | Dye in Solution | https://auricartisan.com/tool/general/spectral-tools/industrial-dye-chemistry/ | Model a dye bath with pH, concentration and path length, and see its colour under four lights |
| [Material Lighting](material-lighting/README.md) | Material Under Light | https://auricartisan.com/tool/general/spectral-tools/material-lighting/ | Render a material's reflectance under an illuminant and a surface model, and compare it with its reference light |

The names differ between places. The Collections page lists the tools as **Neuroscience**, **Perception & Vision**, **Psychophysics Engine**, **Industrial Dye Chemistry** and **Material Lighting**; the site menu uses **Neuroscience of Color**, **Perception and Vision**, **Psychophysical Experiment Engine**, **Industrial Dye Chemistry** and **Material Lighting**.

> **Important:** On the Psychophysical Experiment Engine, at the time of writing, only the **Lab** tab opens. Its other tabs, including **Export**, do not respond. See [its troubleshooting page](psychophysical-experiment-engine/docs/troubleshooting.md).

## Which tool for which job

- You want to see what each stage of the early visual system does to a colour or a pattern: use [Neuroscience](neuroscience/README.md).
- You want to check a design, a screenshot or a palette for colour vision deficiency, low light or an ageing eye: use [Perception and Vision](perception-and-vision/README.md).
- You want to measure your own contrast threshold for a Gabor patch, or learn how staircase procedures work: use the [Psychophysical Experiment Engine](psychophysical-experiment-engine/README.md).
- You want to see how a pH indicator changes colour, what an isosbestic point is, or how far a bath's colour moves between daylight and tungsten light: use [Industrial Dye Chemistry](industrial-dye-chemistry/README.md).
- You want to see why the same material looks different under two light sources, or how a surface's roughness and metalness change its colour: use [Material Lighting](material-lighting/README.md).

## What the five share

- **Six tabs.** A working tab (**Lab**) followed by explanation tabs, a **Data** tab (the register described above), an **Export** tab and a **Reference** tab of sources. Links inside the page text, such as **Data** or **Method** in a note, jump to that tab.
- **Stated inputs.** Where a number depends on a condition, the condition is a control: viewing distance and pixel pitch for anything in cycles per degree, the illuminant for anything that is a colour of a physical sample.
- **Files that carry their caveats.** Every CSV and JSON the tools write begins with a header (or contains fields) that name the method, the units, the light, the data sources and whether the result may be reported as a published value.
- **Links that reproduce a setup.** Each tool can copy a link that restores its main controls when opened.

All five tools are free to use, like every tool on the site.

## In this folder

| Folder | What it covers |
|---|---|
| [neuroscience/](neuroscience/README.md) | The Visual Pathway: stimulus, viewing geometry, the five stages and their maps, the cone table, the colour list export |
| [perception-and-vision/](perception-and-vision/README.md) | The eight simulations, sources, comparison views, the grey-ramp check, presets, the colour list export |
| [psychophysical-experiment-engine/](psychophysical-experiment-engine/README.md) | The two tasks, the stimulus, the five staircases, running a session, the threshold readouts and the exports |
| [industrial-dye-chemistry/](industrial-dye-chemistry/README.md) | The bath, the two-form dye model, pH and titration, Beer–Lambert, lights and colour inconstancy, the tolerance sweep, measured spectra |
| [material-lighting/](material-lighting/README.md) | Illuminants, the twenty materials, the five lobes, geometry, the reference comparison, the sensitivity sweep, measured reflectance |
