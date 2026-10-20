---
title: Chromatic Adaptation — Reference
description: Every control, readout, option and export in the Chromatic Adaptation lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Chromatic Adaptation reference

Address: https://auricartisan.com/tool/general/colorimetry/chromatic-adaptation-dynamic/

## Lab tab

### Image Source

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Choose image** | Opens a file picker for an image | Any image type the browser can decode | — |
| File name | Shows the chosen file | — | "No file chosen" |
| **Sample** | Generates a synthetic HSL sweep (a test target, not a photograph) | 360 × 240 pixels | — |
| **Generate the sample sweep**, **Choose an image** | The same two actions, offered in the empty state before any image is loaded | — | — |

Loaded images are scaled to fit within 480 × 320 pixels (never enlarged).

### Illuminants and transform

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Source illuminant** | The original viewing white point | 12 illuminants, below | CIE D65 (6504 K) — sRGB daylight |
| **Swap** | Exchanges source and destination | Button | — |
| **Destination illuminant** | The target white point | 12 illuminants | CIE D50 (5003 K) — ICC PCS / printing |
| **CAT Method** | The chromatic adaptation transform | Bradford (Lam 1985); Von Kries (Hunt–Pointer–Estévez); CAT02 (CIE 159:2004); CAT16 (Li et al. 2017); Sharp (Finlayson & Süsstrunk 2000); CMCCAT2000 (Li et al. 2002); HPE (Hunt–Pointer–Estévez); XYZ scaling (null case) | Bradford |

The 12 illuminants and their white points (CIE xy):

| Choice | x | y | Spectrum drawn? |
| --- | --- | --- | --- |
| CIE D65 (6504 K) — sRGB daylight | 0.3127 | 0.3290 | Yes, reconstructed from the daylight basis |
| CIE D50 (5003 K) — ICC PCS / printing | 0.3457 | 0.3585 | Yes |
| CIE D55 (5503 K) | 0.3324 | 0.3474 | Yes |
| CIE D60 (6000 K) — ACES | 0.32168 | 0.33767 | Yes |
| CIE D75 (7504 K) — north sky | 0.2990 | 0.3149 | Yes |
| CIE A (2856 K) — tungsten | 0.4476 | 0.4074 | Yes, Planck at 2848 K with the 1931 constant |
| CIE B (4874 K) — noon sun | 0.3484 | 0.3516 | No, table not held |
| CIE C (6774 K) — average daylight | 0.3101 | 0.3162 | No, table not held |
| Equal-energy E | 0.3333 | 0.3333 | Yes, flat |
| FL F2 (4230 K) — cool white | 0.3721 | 0.3751 | No, table not held |
| FL F7 (6500 K) — broadband | 0.3129 | 0.3292 | No, table not held |
| FL F11 (4000 K) — narrow tri | 0.3805 | 0.3769 | No, table not held |

Adaptation needs only the white point, so all 12 adapt correctly whether or not a spectrum is drawn.

### Adaptation and timing controls

| Control | What it does | Range | Default |
| --- | --- | --- | --- |
| **Degree of adaptation D** | The final degree of adaptation the timeline moves towards | 0 to 1, step 0.01 | 1.00 |
| **Time (scrubber)** | The moment after the light changes | 0 to 5 s, step 0.01 | 0 s |
| **Run** | Re-renders the image now | Button | — |
| **Animate** | Plays the timeline from 0 to 5 s in real time, then stops | Button | — |
| **Pause** | Stops the animation at the current time | Button | — |
| **Reset** | Stops and returns to 0 s | Button | — |
| **Live** | Re-renders after every change | On or off | On |
| **HDR Tonemap** | Compresses values above white with a Reinhard curve before clipping | On or off | Off |

The adaptation applied at time t is 0.1 + (D − 0.1) × fraction(t), where fraction(t) follows the two-phase time course with the published defaults (see [Explore the adaptation time course](explore-the-time-course.md)). The starting value 0.1 can only be changed through the `init` value of a share link.

### Controls with no visible effect in the current version

These controls are on the page and their values are recorded in the JSON export, but they do not change the rendered result:

| Control | Range | Default | Current behaviour |
| --- | --- | --- | --- |
| **Display Gamma** | 1.8 to 2.6 | 2.2 | The image is always decoded and encoded with the sRGB transfer function |
| **τ luminance scale** | 0 to 1 | 0.0 | Intended to slow adaptation in dark pixels; the current time course does not use it |
| **Delay luminance scale** | 0 to 1 | 0.0 | As above |
| **Local radius** | 0 to 256 px | 64 px | Not applied |
| **Local strength** | 0 to 1 | 0.60 | Not applied |
| **Mix (global ↔ local)** | 0 to 1 | 0.50 | Has no effect while the per-pixel scales have none |
| **Tile factor** | 1× to 8× | 2× | Not applied |
| **Target FPS** | 8 to 120 | 60 | The animation runs at the browser's frame rate |
| **GPU** | On or off | Off | Processing always runs on the CPU |

Because the per-pixel settings have no effect, the **Per-Pixel Adaptation State Map** is a uniform grey whose brightness is the adaptation in use.

### Readouts

| Readout | What it shows |
| --- | --- |
| Status chip | Ready, Image loaded (size), Sample loaded (360×240), Animating..., Paused at t = …, Reset |
| Model chip | "two components · t = … s · D = …", the adaptation in use |
| **Original Image** | The loaded or generated image |
| **Adapted Image** | The result at the current time |
| **RGB Histogram (Adapted)** | Red, green and blue distributions of the result |
| **Adaptation Curve A(t)** | The applied adaptation over 0 to 5 s, with the current point labelled |
| **Per-Pixel Adaptation State Map** | Adaptation per pixel as grey (white = adapted) |
| **LMS Cone-Channel Analysis** | Source white (light bars) and destination white (dark bars) in L, M and S, with each channel's scale factor |
| **SPD Spectral Overlay (Source vs Dest)** | The two spectra from 380 to 780 nm with a line naming how each was obtained, or a message when a spectrum is not held |

Every chart can be opened full screen with its **Fullscreen** button or by double-clicking it.

## Dynamics tab

| Control | What it does | Range | Default |
| --- | --- | --- | --- |
| **Model** | **Two components** (measured) or **Single exponential** (the page's former curve) | — | Two components |
| **τ1** | Fast-phase time constant | 0.2 to 4 s, step 0.1 | 1.0 s |
| **w1** | Share of adaptation in the fast phase | 0 to 1, step 0.05 | 0.50 |
| **t½** | Slow-phase half-life | 5 to 120 s, step 1 | 30 s |
| **Playhead** | Time to read | 0 to 120 s, step 0.5 | 12.0 s |

Readouts: the chart (both curves, 0–120 s), **D at t = …**, **Half-adapted at**, **90% at**, **Legacy 90% at**, and a note explaining the two curves. These settings do not change the Lab tab.

## Matrix tab

| Control or readout | What it does | Values | Default |
| --- | --- | --- | --- |
| **Decimals** | Precision of the matrices shown | 4, 6, 9 | 6 |
| **Copy as** | Copies the transform's M matrix | NumPy, JSON, CSS matrix3d, GLSL mat3 | — |
| **Round trip** | Largest error of M⁻¹ × M against the identity | — | — |
| Matrices | **M — XYZ to cone-like**, **diag(d)**, **Full adaptation matrix**, at the D set on the Lab tab | — | — |
| **All eight on this pair** | Transform, ΔE vs Bradford, cond(M), Source, Status | — | — |

## Data tab

| Control | What it does |
| --- | --- |
| **Status** chips | Filter the register: **All**, **Verbatim**, **Computed**, **Absent** (a **Stand-in** chip appears only when a stand-in exists) |
| Rows | Expand to read the note and, for absent data, **What it would take** |
| **Install a table** | A drop area labelled "Drop a CSV or JSON here". It does not load files in the current version |

| Dataset | Status |
| --- | --- |
| Illuminant white points, CIE xy | Verbatim |
| Chromatic adaptation matrices, 8 | Verbatim |
| sRGB primaries and transfer function | Verbatim |
| Daylight eigenvectors S0 S1 S2 | Computed |
| Planckian radiators | Computed |
| Adaptation time constants | Computed |
| CIEDE2000 colour difference | Computed |
| Illuminants B and C spectra | Absent |
| Fluorescent F2 F7 F11 spectra | Absent |
| Corresponding-colour data sets | Absent |
| Colour matching functions, 10° | Absent |

## Export tab

| Control | What it does | Output |
| --- | --- | --- |
| **Export JSON** | Downloads the settings and the adaptation at the current time | `cad-<method>-<source>-<destination>.json` |
| **Export Frame (PNG)** | Downloads the adapted image | `cad-frame-t<time>.png` |
| **Copy Link** | Copies the page's current address | Text |
| **Share URL** field and **Generate** | Builds a link to the current settings, shows it and copies it | A URL |
| **Copy** | Copies the link in the field | Text |
| **Compare All Methods** | Runs all eight transforms on eight test colours at the current adaptation | Bar chart and table |
| **Batch Colour Analysis**, **Run Batch** | Adapts up to 50 HEX colours | Table |

The JSON file contains: `srcIllum`, `dstIllum`, `catMethod`, `gamma`, `delay`, `tau`, `strength` (the D setting), `initAdapt`, `tauLocal`, `delayLocal`, `radius`, `localStrength`, `mix`, `tile`, `time`, `fps`, `hdr`, `matrix` (the full 3 × 3 adaptation matrix as nine numbers, row by row), `srcLMS`, `dstLMS`, `scale` (the three cone gains) and `det` (its determinant). `delay` and `tau` belong to the former single-exponential model.

The share link carries `src`, `dst`, `cat`, `tau`, `delay`, `str` (D), `init` (initial adaptation) and `t` (time). It does not carry the image.

## Reference tab

| Control | What it does |
| --- | --- |
| **Standards**, **Formulas**, **Citations**, **Research notes** | Switch sections; each shows a count |
| **Filter** | Searches all four sections; `Esc` clears it |
| **Where it is used** chips (Citations) | **All**, **Runs here**, **Corrected**, **Context only** |

Standards covers CIE 160:2004, CIE 159:2004 (CIECAM02), CAM16/CAT16, ICC.1:2022, Fairchild and Reniff (1995), Brainard and Wandell (1992), Foster (2011) and CIE 15:2018. Formulas covers the adaptation models, von Kries diagonal adaptation, the eight matrices, sRGB conversion, CIELAB, ΔE, spectrum generation and the spatial model. Some background prose predates the current time-course model; the figures the lab uses are those on the Dynamics tab.

## Save to Library

The floating **Save to Library** button stores a preset of the current form settings in your Library.
