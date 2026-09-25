---
title: Material Lighting (Material Under Light) — Set up a scene
description: Choose the light, the material, the surface model and the viewing geometry, and understand what each does to the spectrum and the colour.
product: Website › Tools › Perception and spectral › Material Lighting
updated: 2026-09-25
---

# Set up a scene

## How the colour is made

At each of 81 wavelengths, 380 to 780 nm in 5 nm steps, the tool multiplies:

1. **The illuminant's spectral power** — how much light the source emits at that wavelength (its **spectral power distribution**, SPD).
2. **The material's reflectance** — the fraction of that light the material sends back, from 0 to 1.
3. **The lobe's weight** — how much of the reflected light travels towards your eye at the angles you set.

The products are summed against the CIE 1931 2° observer's colour-matching functions to give CIE XYZ, and converted to sRGB for the screen. The **Method** tab's **From spectrum to colour** view shows these steps. The published observer table is at 10 nm; the tool interpolates it to 5 nm, and says so in its exports.

## 1. Choose the light

| Option | What it is |
|---|---|
| **D65 — daylight, 6504 K** (default) | CIE average daylight |
| **D50 — daylight, 5003 K** | Warmer daylight, the graphic arts reference |
| **D55 — daylight, 5503 K** | Mid-morning or mid-afternoon daylight |
| **D75 — daylight, 7504 K** | Cool north-sky daylight |
| **A — a blackbody at 2856 K** | Incandescent (tungsten) light |
| **E — equal energy** | Equal power at every wavelength |
| **Blackbody at a temperature you choose** | Planck's law at **Temperature** |
| **Daylight at a temperature you choose** | The CIE daylight model at **Temperature** |

The daylights are reconstructed from the CIE D-series basis, which is published and lands on the published chromaticities. A **blackbody** (Planckian radiator) is an ideal hot object whose light depends only on its temperature; daylight has a slightly different, greener-or-bluer balance at the same temperature.

**Temperature** (1800–10000 K in steps of 50, default 2700 K) is used only by the last two options, and is disabled otherwise; its hint says which. The CIE daylight model is defined from 4000 K, so **Daylight at a temperature you choose** raises lower values to 4000 K and says so in the exports.

## 2. Choose the material

The menu offers twenty materials: **White**, **Gray**, **Black**, **Red**, **Green**, **Blue**, **Yellow**, **Cyan**, **Magenta**, **Skin**, **Leaf**, **Ocean**, **Concrete**, **Wood**, **Sky**, **Gold** (default), **Copper**, **Silver**, **Ceramic** and **Rubber**.

Every one is a curve the tool invented to look right: a flat level plus one or two bell-shaped bumps. For example, silver is a flat 0.75 across the spectrum and gold is a low level plus bumps near 590 and 620 nm. None is a measurement, and **Reflectance** reads **synthesised**. This matters most for metals, whose reflectance spectrum is their colour. To use real data, load a measured file; see [Use a measured reflectance](use-a-measured-reflectance.md).

## 3. Set the surface

**Dielectric** or **Conductor** (default Dielectric):

- A **dielectric** (paint, plastic, ceramic, skin) reflects a small, nearly colourless highlight from its surface and gets its colour from light that enters and scatters back out (the diffuse term). **Refractive index** (1.00–3.00, step 0.01, default 1.50) sets how strong the surface highlight is: the reflectance straight on, F0, is ((n − 1) ÷ (n + 1))², 4% at 1.50.
- A **conductor** (metal) has no diffuse term: all its colour comes from the specular reflection, tinted by its reflectance spectrum. **Refractive index** is disabled.

**Roughness** (0.02–1.00, step 0.01, default 0.40) sets how spread out the reflection is: low values give a tight, bright highlight; high values a broad, dim one.

## 4. Choose a lobe

A **lobe** (a bidirectional reflectance distribution function, BRDF) describes how a surface spreads reflected light over directions. Most here are **microfacet** models, which treat the surface as tiny mirror facets whose tilts are spread according to the roughness. Select a card under the sample:

| Lobe | Description on the card | Source |
|---|---|---|
| **GGX** (default) | Trowbridge-Reitz, with Smith height-correlated masking | Walter et al. 2007 |
| **Beckmann** | A Gaussian slope distribution; narrower tails than GGX | Beckmann & Spizzichino 1963 |
| **Ward** | Fitted to measured gonioreflectometer data | Ward 1992 |
| **Ashikhmin-Shirley** | An anisotropic Phong lobe with a coupled diffuse term (used here in its isotropic form) | Ashikhmin & Shirley 2000 |
| **Oren-Nayar** | Rough diffuse, no specular: a surface of Lambertian facets | Oren & Nayar 1994 |

The **Method** tab's **The five lobes** view gives each lobe's specular and diffuse values at your current geometry and roughness.

**Oren-Nayar** has no specular term, and a **Conductor** has no diffuse term, so together they reflect nothing: the sphere and swatch go black. Use a specular lobe for metals.

## 5. Set the geometry

| Control | Range | Default | Meaning |
|---|---|---|---|
| **Light from** | 0–89° | 30° | Angle of the light from the surface normal (straight up) |
| **Seen from** | 0–89° | 20° | Angle of your eye from the normal |
| **Between them** | 0–180° | 0° | Azimuth between the light and the eye around the normal |

At 0° and 0° the eye is in the mirror direction and the highlight is strongest.

The three angles set the geometry for the readouts, the swatches and the spectrum's product curve: they describe one point on a flat surface. The **sphere** is always drawn seen head-on, lit from the **Light from** angle, so it shows the whole range of surface angles at once; **Seen from** and **Between them** do not change it.

## 6. Read the sample

- The sphere and swatch are scaled so that a perfect white diffuser in the same light and at the same angles would read Y = 1 (the note **scaled so a white card here would read Y = 1**). This makes brightness comparable between scenes.
- The swatch and **sRGB** are not adapted to the light: under a 2700 K lamp even a white card looks warm, as it would to a camera.
- **CIE L\***, **a\*, b\*** are taken against the light's own white, so they describe the material relative to the light; see [Compare with the reference light](compare-with-the-reference.md).
- **Jz** is the lightness of JzAzBz (Safdar et al. 2017), a colour space designed for high dynamic range, given as a second opinion on lightness.
- **Inside sRGB** reads **yes**, **no**, or **the highlight is not** when only the sphere's highlight had to be clipped. **clipped to sRGB** appears on the sphere in the last two cases.

**Save the spectrum** downloads the CSV; **Reset the scene** returns to the defaults.

You should now be able to build a scene of any preset material under any of the eight light options.
