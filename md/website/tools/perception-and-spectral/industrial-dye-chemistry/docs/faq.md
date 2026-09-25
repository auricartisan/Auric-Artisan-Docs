---
title: Industrial Dye Chemistry (Dye in Solution) — FAQ
description: Short answers to common questions about Dye in Solution.
product: Website › Tools › Perception and spectral › Industrial Dye Chemistry
updated: 2026-09-25
---

# Dye in Solution FAQ

## Are the preset dyes real products?

No. Each stands for a class of dye, such as "the methyl-orange family", with constants chosen by the tool to be plausible. None is a named commercial substance, and every preset is marked **Stand-in**.

## Can I use it to formulate a real recipe?

Not as it stands. The model (two forms, Beer–Lambert, a stated light and observer) is sound, but the dye data are the tool's own and the bands are Gaussian. With measured spectra for both forms of your dyes it becomes much closer, but it still models dye in solution, not on cloth.

## Does it model dye on fabric?

No. There is no substrate or reflectance mode in the current interface. The Data register describes a Kubelka–Munk model for opaque substrates as a stand-in, and the Reference tab explains why it is not offered.

## Why is there no F11 or other fluorescent light?

Fluorescent illuminants are measured spectra with narrow emission lines, published as tables, and the page does not hold them. It will not substitute a smooth imitation under that name.

## Is the "ΔE₀₀" in the lights row a metamerism index?

No. It is colour inconstancy: one bath under two lights. Metamerism concerns two baths that match under one light and not under another. See [Compare lights](compare-lights.md).

## Which colour difference formula does it use?

CIEDE2000 (CIE 142-2001), the full formula including its rotation term, checked against published test pairs.

## Why do the swatch and the L\*a\*b\* disagree when I change the light?

On purpose. The swatch shows the light leaving the bath without adaptation, so a bath under tungsten looks warm. L\*a\*b\* is taken against the chosen light's own white, so it measures the dye's colour relative to that light.

## Can the tool tell me if a dye is hazardous?

No. The page holds no toxicological data. Hazard classification belongs to each substance and is on its supplier's safety data sheet (section 2; section 8 covers exposure controls and protective equipment). See the **Safety** tab.

## Does it do lightfastness or wash-fastness tests?

No. ISO 105-B02, ISO 105-C06, AATCC TM 61 and ISO 14184-1 are laboratory procedures on physical cloth and cannot be performed in a browser.

## Is my data uploaded?

No. Everything, including loaded spectra, stays in the page. See [Privacy](../others/privacy.md).
