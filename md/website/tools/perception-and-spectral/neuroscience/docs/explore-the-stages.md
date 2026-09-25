---
title: Neuroscience (Visual Pathway) — Explore the five stages
description: Set up the stimulus and viewing geometry, then read what the retina, LGN, V1, V2 and V4 stages do to it, map by map.
product: Website › Tools › Perception and spectral › Neuroscience
updated: 2026-09-25
---

# Explore the five stages

This guide covers the stimulus, the viewing geometry, each stage of the pathway, the nine maps and the Cells tab. All controls named here are on the **Lab** tab unless stated.

## 1. Choose a stimulus

Under **Stimulus**, choose one of two sources.

- **Grating** — stripes whose brightness or colour varies as a sine wave across the frame. It is the only source with a defined spatial frequency, so it is the one the stages can be read against. Its controls are a colour picker (**Base colour**, default `#3A8CFF`) and a **Carrier** menu:
  - **Chromatic** — the stripes swing between the base colour's hue and its opposite, around a grey with the same L + M cone signal. Both phases have the same L + M, so the pattern changes colour with little change in lightness.
  - **Luminance** — grey stripes that swing lighter and darker around a grey with the base colour's relative luminance. The pattern changes lightness only.
- **Test card** — six colour bars (`#E03131`, `#2F9E44`, `#1971C2`, `#F59F00`, `#C2255C`, `#0CA678`) across the top half, a nine-step grey ramp below them, and a red-to-green gradient along the bottom. The base colour, carrier, frequency and contrast do not apply to it, and the grating controls are hidden.

**Contrast** (0 to 100%, default 25%) sets how far the grating swings either side of its mean. A saturated base colour's opposite is often outside the sRGB range a screen can show. When the swing you ask for does not fit, the page shrinks it to the largest swing both phases can survive, shows the note **The contrast you asked for does not fit in sRGB**, and reports what it drew under **Contrast achieved**. It does not clip one phase, because that would quietly change the contrast.

## 2. State the viewing geometry

A spatial frequency in **cycles per degree** (c/deg) counts how many light-dark cycles fit into one degree of your field of view. It is not a property of an image alone; it depends on how far away the image is and how large its pixels are. So the page asks for both:

- **Viewing distance** — 20 to 200 cm, default 57 cm. At 57 cm one degree covers very nearly one centimetre, which is why vision laboratories use it.
- **Pixel pitch** — 0.05 to 0.6 mm, default 0.248 mm. Your screen's value is its visible width in millimetres divided by its width in pixels.

From these the page works out the degrees per pixel (shown above the canvases; 0.0249° at the defaults) and the **Nyquist limit of the grid**, the finest frequency the pixel grid can carry: half a cycle per pixel, 20.1 c/deg at the defaults. If **Spatial frequency** (0.2 to 30 c/deg, default 4.0) is above that limit, the note **Above the pixel grid's Nyquist limit** appears: the screen cannot draw the frequency you asked for, and what you see is an alias, a coarser false pattern. Ask for a lower frequency, or check your geometry: the limit rises as the viewing distance grows and as the pixel pitch shrinks. (The warning's own text suggests moving closer, which in fact lowers the limit.)

**Pupil** (2 to 8 mm, default 3.0 mm) is shown on the rail but, in the current version, does not change any map or readout. The sensitivity curve peaks at 4 c/deg whatever the pupil size; the **Pipeline** tab explains why.

## 3. Switch stages on and off

Under **Stages** there is one checkbox per stage, all ticked by default:

- **Retina — centre-surround**
- **LGN — opponent channels**
- **V1 — Gabor bank**
- **V2 — boundary signal**
- **V4 — colour cell**

Each one really switches its stage. When a stage is off, its settings group is hidden, and a map that belongs to it is drawn black with **— stage off** after its name. **V2** is computed from the V1 energy map, so it needs **V1** on as well.

## 4. What each stage computes

All five are standard forms from the vision literature, implemented with constants chosen by this tool. They show the shape of what each area does; they are not measurements of real neurons.

### Retina: centre-surround

A retinal ganglion cell with a centre-surround receptive field responds to a spot that differs from its surroundings. The tool models this as a **difference of Gaussians**: the stimulus's relative luminance blurred by a small Gaussian (the centre), minus a weight times the same image blurred by a larger Gaussian (the surround). Positive responses form the **on-centre** map and negative ones the **off-centre** map.

| Control | Range | Default |
|---|---|---|
| **Centre σ** | 0.5 to 6, in pixels | 1.5 |
| **Surround σ** | 1 to 14, in pixels | 4.0 |
| **Surround weight** | 0 to 1.5 | 0.75 |

The sigmas are in pixels, not degrees. With a surround weight below 1 the centre and surround do not cancel over a uniform area, so the response carries a constant proportional to the mean luminance. That is why the off-centre map can be empty while the on-centre one is not. Raise the weight towards 1 to balance them.

### LGN: opponent channels

The lateral geniculate nucleus carries colour as differences between cone signals. The tool computes, for every pixel, three channels from the cone signals L, M and S:

- **L − M** — the red-green channel.
- **S − (L+M)/2** — the blue-yellow channel.
- **L + M** — the tool's luminance channel.

A neutral grey sits at zero on both chromatic channels. [Cones, opponent channels and the cone table](cones-and-opponent-channels.md) explains how the cone signals are obtained and how these axes differ from the published DKL space.

### V1: Gabor bank

Simple cells in primary visual cortex respond to stripes of a particular orientation and spacing. The tool filters the stimulus's luminance with a bank of **Gabor** filters — a sine-wave stripe pattern inside a Gaussian envelope — at evenly spaced orientations from 0° to 180°. For each orientation it uses a pair of filters a quarter-cycle apart and takes the length of the pair's response, which is the classic **complex-cell energy** model: it responds to a stripe pattern wherever the stripes' phase falls. The energies of all orientations are summed into one map. The bank runs at half the image resolution and the result is enlarged back to 256 × 256.

| Control | Range | Default |
|---|---|---|
| **Gabor frequency** | 0.2 to 30 c/deg | 4.0 c/deg |
| **Orientations** | 2 to 16 | 8 |
| **Kernel size** | 9 to 51 pixels, odd | 31 |
| **Envelope σ** | 1 to 16 | 6.0 |

Gabor frequency is in cycles per degree, the same unit as the stimulus, so a filter set to the grating's frequency is tuned to it.

The **preferred orientation** map (the hypercolumn view) shows, for every pixel, which orientation in the bank responded most. It is drawn as a colour wheel: hue runs through the orientations from 0° to 180°, and saturation shows how selective the pixel is (the winning energy as a share of the total). Grey or pale pixels have no clear preference.

### V2: boundary signal

The tool's V2 stage takes the V1 energy map, measures how steeply it changes from pixel to pixel, and divides the result by a blurred copy of itself (divisive normalisation). It marks where texture regions meet. Real V2 does more than this, and the Data tab says so.

### V4: colour cell

A V4 colour cell prefers a direction in colour space. The tool projects each pixel's two chromatic values onto the direction you pick under **V4 preferred direction**, keeps only positive responses, and normalises. The directions are **Red** (default), **Green**, **Blue**, **Yellow**, **Orange** and **Purple**. Red points along +L − M, Green along −(L − M), Blue along +S − (L+M)/2, Yellow along its negative, and Orange and Purple between them. V4 reads the same cone signals and opponent axes as the LGN stage.

### Colour vision

**Colour vision** changes the stimulus before any stage sees it: **Typical** (default), **Protanopia**, **Deuteranopia** or **Tritanopia**. The simulation uses the Viénot, Brettel and Mollon (1999) projection at full strength: the missing cone type's signal is replaced by a combination of the other two, so colours that differed only along the lost axis become the same. The stimulus canvas shows the simulated frame. The same setting applies to the colour list on the **Export** tab.

## 5. Choose and read a map

Under **Show**, the first menu picks the map for the right-hand canvas:

| Map | Stage | What bright means |
|---|---|---|
| **Retina, on-centre** | Retina | Brighter than the surround |
| **Retina, off-centre** | Retina | Darker than the surround |
| **LGN, L − M** | LGN | More L than M signal |
| **LGN, S − (L+M)/2** | LGN | More S than the L and M average |
| **LGN, L + M** | LGN | More combined L and M signal |
| **V1, complex-cell energy** | V1 | Strong oriented stripe energy at the Gabor frequency |
| **V1, preferred orientation** | V1 | Colour wheel of the winning orientation |
| **V2, boundary signal** | V2 | A change in V1 energy |
| **V4, colour cell** | V4 | Colour close to the preferred direction |

The second menu picks the colourmap: **Viridis** (default), **Inferno** or **Grayscale**. Grayscale is the one to use for printing.

**Show the scale** (ticked by default) shows the scale bar. Every map is stretched between its own minimum and maximum, so the numbers at the ends are the only thing that says what a bright pixel means: without them a bright pixel could be 0.2 or 20. The unit label reads **response, this map's own range**. For the orientation map the ends read 0° and 180°, the bar shows the hue wheel and the label reads **preferred orientation**. When a map has no variation at all, the label reads **flat — this stage found no variation in this stimulus**; for example, the off-centre cells find little to answer to in a chromatic grating.

Double-click either canvas to enlarge it; see [Shortcuts](../others/shortcuts.md).

## 6. Read the readouts

| Readout | Meaning |
|---|---|
| **L − M peak gap** | How far apart the L and M curves peak in the cone table the page holds; highlighted when under 5 nm |
| **Published gap** | 25 nm, the gap in the published cone fundamentals |
| **Neutral off-axis** | The largest distance from zero that a nine-step grey ramp reaches on either chromatic channel |
| **Contrast achieved** | The contrast actually drawn, after any cap |
| **Sensitivity at this frequency** | The tool's bandpass weighting curve at the stimulus frequency, from 0 to 1 |
| **The curve's peak** | Where that curve peaks: 4.0 c/deg |
| **Frame RMS contrast** | The root-mean-square spread of relative luminance across the stimulus frame |
| **Nyquist limit of the grid** | The finest frequency your stated screen can draw |

**Neutral off-axis** reads about 2.2 × 10⁻⁴ rather than zero because the published cone matrix is given to four decimals. The sensitivity reading is a weighting, not a probability of seeing the grating: the page gives no detection figure, because that would need a threshold criterion and a calibrated model it does not hold.

## 7. See every stage at once on the Cells tab

The **Cells** tab draws small (96 × 96) previews of every stage over the same grating, each with a name, what it computes, a short explanation and a tag.

- **Show**: **Everything** adds two cards for panels that were withdrawn from the page (**Spike raster** and **Detection %**); **The five that run** shows only the working stages.
- **Contrast**: **10%**, **25%** (default) or **100%**. At 100% each stage is at full drive, where a stage that does nothing is easy to spot.

The previews use your base colour, carrier, frequency, geometry, retinal settings, Gabor frequency and V4 direction, with a fixed V1 bank of 8 orientations, and the Viridis colourmap. They are drawn when you first open the tab and redrawn when you press one of its buttons, so after changing the Lab, press a **Show** or **Contrast** button to refresh them.

Below the grid, **Controls that were read and never used** lists six controls from an earlier version of the page and whether each was removed or connected up.

You should now be able to predict which maps a given stimulus will drive, and read their scale bars.
