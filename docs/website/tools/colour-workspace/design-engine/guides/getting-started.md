---
title: Design System Generator — Getting started
description: Open the Design System Generator, learn the layout, and generate, check and export your first design system.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Getting started with the Design System Generator

This guide takes about ten minutes. By the end you will have a design system that meets a contrast target, and its tokens in a file.

## Open the tool

1. Go to https://auricartisan.com/tool/design-engine/ in a current desktop browser. The tool works on smaller screens, but the three-column layout is easiest on a wide one.
2. A system appears straight away. Which one depends on how you arrived:
   - from a shared link, the link's settings are applied first;
   - otherwise, on a return visit, the settings you used last in this browser;
   - otherwise the defaults: **Auto** industry, **Modern** style, **AAA** contrast.

## A tour of the screen

### The masthead

The top of the page reads *Three choices, one whole system.* with a short description, the number of tokens, **Targets 12** and *OKLCH · WCAG 2.1 · APCA*. On the right are five buttons and a link:

| Control | What it does |
| --- | --- |
| **Surprise** | Picks a random industry, style and contrast target, resets the seed to auto, and sets harmony to auto or a random harmony. |
| **Share** | Copies a link that rebuilds this system. |
| **Save** | Saves the system to your Library. |
| **Help** | Opens **How this works**: what the defaults assume and how the score is worked out. |
| **Workspace** | Opens your saved systems and the options for sending the palette to other tools. |
| **Read the API reference →** | Opens the public API documentation. |

Under the masthead a short note shows what the same job costs through the REST API (**Automate this — 4 API credits per call to POST /v1/tokens/generate**). You can dismiss it with its **×**.

### The tab row

Seven tabs: **Overview**, **Colour**, **Type**, **Icons**, **Scales**, **Components** and **Tokens**. The **Tokens** tab shows the token count. At the right end, **Expand** hides the two side rails so the tab you are reading gets the full width; select it again (**Collapse**) to bring them back. The page remembers this choice.

### The three columns

- **The brief** (left): every input. Changing any of them regenerates the system.
- **The stage** (middle): the tab you selected.
- **The audit** (right): the score, where the points went, and the twelve contrast pairings. It is always visible.

Below the columns a note reads *Generated, not designed.*

## Your first system

1. In **The brief**, open **Industry** and choose **Education**.
2. Open **Style** and choose **Playful**.
3. Under **Contrast target**, select **AA**.
4. Look at **The audit**. The large number is the score out of 100. Under it, a line says how it changed (*+3 on that change*) and a pill says whether all twelve pairings pass. A line below says how many tokens moved.
5. Open the **Colour** tab. Read the ramps, the semantic colours and the **Surfaces & roles** card. Select any colour to copy it.
6. Open **Components**. Try the buttons, tabs and switches, and switch **Theme** to **Dark**.
7. Open **Tokens**. Scroll to **Export tokens**, select the **CSS** pill, then select **Download**. The file `tokens.css` downloads.

Result: a complete token file for an education product with a playful style, whose text colours meet WCAG AA.

## Next steps

- Anchor the system to your own brand colour: [Set the brief](set-the-brief.md).
- Understand the score and the pairings: [Check contrast with the audit](contrast-audit.md).
- Choose the right export for your stack: [Export tokens](export-tokens.md).
- Keep the system: [Share, save and connect](share-save-and-connect.md).

## Related

- [Design System Generator overview](../README.md)
- [Reference](reference.md)
