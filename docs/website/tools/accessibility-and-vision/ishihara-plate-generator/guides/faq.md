---
title: Ishihara Plate Generator — FAQ
description: Short answers to common questions about the Ishihara Plate Generator.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Ishihara Plate Generator FAQ

## Can I use these plates to test someone's colour vision?

No. The page says: "Not a colour-vision test. These plates are illustrative. A screen is not colour-calibrated and a real Ishihara examination is printed, lit and administered under controlled conditions. For diagnosis, see an eye-care professional."

## Is it free? Do I need an account?

It is free and needs no account. Plates are generated in your browser. Generating plates from code through the REST API costs 3 API credits per call.

## What does the quality score mean?

It combines four measurements: dot density, figure ratio, separation for typical vision, and concealment through the simulated deficiencies. A plate passes when it is visible to typical vision and hidden from the deficiency it targets. See [Read the diagnostics](read-the-diagnostics.md).

## Which colour-vision deficiencies are simulated?

Protanopia, deuteranopia and tritanopia, using the Brettel, Viénot and Mollon (1997) model.

## Why can I not keep my plates after closing the page?

Plates are not stored between visits. Export them, or keep their seeds.

## Can I make a plate with my own number or word?

Use **Custom** and type a number, a letter, or one of the listed symbol or shape names. See [Generate plates](generate-plates.md).

## What is a seed?

A number that fixes every random choice in a plate. The same seed with the same settings produces the same plate, dot for dot, on any machine.

## Which format should I export?

PNG for slides and documents; SVG for printing at any size, since every dot is a separate circle; the ZIP for everything at once, with a JSON description of each plate.

## What is the standard 38?

A fixed set of 38 plates (24 numbers, 6 letters, 4 symbols, 2 shapes and 2 paths), built from seed 42 so it is the same every time. See [Build the standard 38](build-the-standard-38.md).
