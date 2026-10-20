---
title: Harmony Library — Identify your colours' harmony
description: Use "What harmony is this?" to find which of the 23 schemes your colours form, how closely, and which schemes it cannot tell apart.
product: Website › Library › Colour libraries › Harmony Library
updated: 2026-09-25
---

# Identify your colours' harmony

**What harmony is this?** compares the hue pattern of colours you give it against all 23 schemes in the collection.

## How the match works

- A harmony is a shape on the colour wheel, and a shape has no first colour. So the page tries each of your colours as the base in turn and keeps the best fit. The order you enter colours in does not change the answer.
- Only schemes with the same number of colours as yours are compared. Three colours are compared with the 3-colour schemes, five with the 5-colour schemes, and so on.
- For each scheme it measures how far, on average, your hues are from the scheme's ideal angles, in degrees. The **fit** runs from 1 (exact) down to 0 (60° or more off on average — a whole scheme's worth of wrong).
- Only hue is compared. Lightness and saturation are ignored.

## Steps

1. Scroll to **What harmony is this?**. It starts with three colours: `#E4572E`, `#2EE457` and `#572EE4`.
2. For each colour, click the swatch to pick one, or type into the field. Any CSS colour works: hex, `rgb()`, `hsl()`, `lab()`, `oklch()`, `color()` or a name.
3. Select **Add a colour** to add one (up to 12). The new colour is the opposite of the first colour. Select × to remove one; at least two always remain.
4. The answer updates as you type. **Identify it** runs the match again.

**Result:** the scheme your colours form, how closely, and which others were close.

## Reading the answer

### The verdict

| Fit | Verdict | Note |
| --- | --- | --- |
| 0.85 or more | The scheme's name, for example **a triadic** | **The hue offsets sit within N° of the canonical …°.** |
| 0.65 to below 0.85 | **Close to** and the scheme, for example **Close to an analogous 3** | **The closest scheme is off by N° on average. Near enough to read as intentional, far enough that it was probably not.** |
| Below 0.65 | **Not one of the 23** | **Nothing in the collection sits close to these hue offsets. That is not a fault — most palettes in the world are not one of 23 schemes.** |

Next to the verdict: **fit** and the score to three decimals.

### Schemes it cannot tell apart

Five schemes share a hue shape with another and differ only in lightness or saturation: **shades**, **tints** and **neutral** are all five colours at one hue (like **monochromatic 5**); **warm cool** has the shape of **complementary**; **triad shifted** has the shape of **triadic**. When your colours match one of these, the note says: **By hue alone this is indistinguishable from …** and lists the others, because a hue measurement cannot separate them.

### The rows

| Row | Meaning |
| --- | --- |
| **Family** | The best scheme's family: complementary, polyadic, analogous, monochromatic or compound. |
| **Base colour** | Which of your colours worked best as the scheme's base. |
| **Worst pair** | The lowest contrast ratio between any two of your colours. |
| **Best pair** | The highest, marked **(AA)** when it reaches 4.5:1 — at least one pair can then carry body text. |

### Also considered

Up to four runner-up schemes, each with its fit to two decimals.

## Special cases

- **No scheme uses N colours.** With 8 to 12 colours no scheme has as many members, so the page says so and explains that the 23 methods run from two members to seven. Remove colours until you have seven or fewer.
- **Colour N is not a colour yet.** A field holds text that is not a colour. The match uses that colour's last valid value; leaving the field puts that value back.
- If the list of schemes cannot be loaded, the section says **The scheme manifest did not load, so there is nothing to match against.**

## Example

Enter `#E4572E`, `#2EE457` and `#572EE4` (the defaults). The hues are 120° apart, so the verdict is **a triadic** with a fit close to 1, and the note names **triad shifted** as indistinguishable by hue alone.
