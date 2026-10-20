---
title: Animation Contrast — Text on moving backgrounds
description: Check text over an animated background at 48 moments, from keyframe stops, pasted @keyframes CSS or a video, find where and how long it fails, and fix it with a text colour, a scrim or a shadow.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Animation Contrast

Animation Contrast checks text that sits on a moving background: a hero whose colour shifts, an animated gradient, or a video behind a caption. It samples the background at 48 moments across the loop, measures your text colour against each one, and shows where the text fails, for how long and how badly. Then it offers three ways to fix it: a different text colour, a scrim behind the text, or a text shadow, with the CSS for each.

The background can come from keyframe stops you set, a real `@keyframes` block you paste, or a video file, of which only the region behind the text is measured.

Animation Contrast is one of the six **Essentials** in the Colour Tools. It opens in a floating panel; for the panel, its footer and its links, see [Open the Colour Tools and work in their panels](launcher-and-panels.md).

## Open it

- **Launcher:** press `Ctrl` + `Shift` + `C`, then select **Animation Contrast**.
- **From another tool:** **Open in another tool** › **Animation Contrast** in Contrast System and Type Readability Sim.
- **A link:** `?ctool=anim`, for example `https://auricartisan.com/?ctool=anim&color=FFFFFF&stops=0F172A@0,9333EA@50,F97316@100`. See [Link keys](#link-keys).

The colour you open it with becomes the text colour; with no colour, the text is white. The starting animation runs over 6 seconds, `ease-in-out`, through four stops: `#0F172A` at 0%, `#1E3A8A` at 35%, `#9333EA` at 70% and `#F97316` at 100%.

## Screen tour

### The header band

The band shows the whole loop as a strip of 48 samples with six "Aa" in your text colour across it, and a marker at the worst moment with its value, for example "Worst · 100% · 2.80:1". The left of the band is painted in the worst moment's colour and says:

- "Worst moment · 100% · #F97316";
- the result: "Passes at every moment — lowest …", "Fails for 17% of the loop — worst at 100%", or "Fails for the whole loop — best …";
- the text colour, the threshold and the worst value, with "scrim on" when a scrim from **Fix** is applied.

Before there is anything to measure, it says "Drop a video to check it", "Sample the video to check it" or "Fix the CSS to check it".

### The controls rail

- **Text colour**: the colour field for the text.
- **Threshold**: the level every moment must reach: **WCAG AA · 4.5:1**, **WCAG large text · 3:1**, **WCAG AAA · 7:1**, **APCA Lc 75 · body** or **APCA Lc 60 · large**. APCA is read as |Lc|, whichever way round the text and background are.
- **Background source**: **Keyframes**, **Paste CSS** or **Video**. The rest of the rail follows the source.

**Keyframes**

- **Keyframe stops**, with a count such as "4 of 8". Each stop has a colour field and a position in percent, and a remove button (×) while there are more than two. Stops are placed by their percentage, not by list order.
- **Add stop** puts a new stop in the widest gap, coloured as the animation already is there. **Reset** puts the four starting stops back.
- A note under the list explains edge cases: two stops at the same percentage make a hard jump, and before the first stop (or after the last) that colour holds, as in CSS.
- **Easing**: `linear`, `ease`, `ease-in`, `ease-out`, `ease-in-out` or `steps(4)`, applied to every segment between two stops, as CSS does.
- **Duration**: 1 to 20 seconds, in half-seconds.
- **Colours blend in**: **sRGB**, which matches how browsers blend hex and `rgb()` keyframes, or **OKLab**, for keyframes written in `oklab()` or `oklch()`.

**Paste CSS**

- **Paste @keyframes**: a text box for a real `@keyframes` block with `background-color` (or `background`) in each keyframe, and optionally the `animation` line that uses it. The tool reads the keyframe positions (`from`, `to` and percentages), per-keyframe `animation-timing-function`, and the duration and easing from the `animation` line.
- A status line says **Parsed**, with the name, the number of stops, the duration and the easing, or **Error** with what went wrong, for example "No @keyframes block found. Paste one that starts “@keyframes name {”."
- Notes explain what the tool assumed: a missing 0% or 100% keyframe, ignored transparency, an unknown easing, or that `alternate` "plays the loop back and forth; one direction covers every colour, so that is what is checked."
- **Fill from stops** writes the current keyframe stops as `@keyframes`. **Edit as stops** loads the parsed keyframes into **Keyframes** (up to eight; per-keyframe easing stays only in **Paste CSS**).
- **Colours blend in**, as for **Keyframes**.

**Video**

- A drop area, "Drop a short video here", with **Choose file**. The video stays on your device; short loops sample fastest.
- Once a video is loaded: a preview with the text region outlined, its name and length, and **Text region** sliders, **Left**, **Top**, **Width** and **Height**, in percent of the frame. Only this region is averaged, so a bright sky above a dark caption does not skew the result.
- **Sample 48 frames** reads 48 evenly spaced frames and averages the text region of each. It shows its progress ("Sampling 12 of 48…") and then reads **Sample again**. If you move the region after sampling, a note asks you to sample again. **Clear** removes the video.

## The tabs

### Timeline

The opening sentences say how much of the loop fails and where, for example "#FFFFFF text falls below WCAG AA 4.5:1 at 8 of 48 samples (17%, about 1.0 s of every 6 s loop). It fails from 85% to 100%. The worst moment is 100% on #F97316, at 2.80:1." The next gives the range of the WCAG ratio and of APCA Lc across the loop. When the loop runs longer than 5 seconds, a note adds: "if it starts on its own, WCAG 2.2.2 also asks for a way to pause it."

- **The chart**: a bar for each of the 48 samples, painted in the background colour at that moment and as tall as the value (the WCAG ratio or APCA |Lc|, as the threshold decides), with the threshold drawn across it. Pills count the passes and fails, for example "40 / 48 pass" and "8 fail". Under the chart are the background colours, the failing stretches and a time axis.
- **Scrub to a moment**: a slider across the 48 samples. Its readout gives the moment, the time, the background, the value and pass or fail. Selecting a bar does the same.
- **Where it fails**: each failing stretch with its range, its length in samples and seconds, and its lowest value, with **Show moment**, which opens that moment on **Moment**.

### Moment

One moment of the loop: the one you picked on **Timeline**, or the worst if you have not picked one. The opening sentence gives the moment, the background and the result against the threshold, for example "At 100% (6.00 s) the background is #F97316. #FFFFFF text reaches 2.80:1, short of WCAG AA 4.5:1 by 1.70. This is the worst moment in the loop."

- **A sample card** at that moment's background: a heading ("Autumn launch"), body text at 16 px and small print at 12 px, in your text colour, with the pair, value and level and a pass or fail pill.
- For a video, the **frame** at that moment, with the averaged region outlined.
- **Values · tap to copy**: **Moment**, **Background**, the value at the threshold, **Needs**, **WCAG 2.x** and **APCA Lc**.
- **Previous moment**, **Next moment** and **Worst moment** step through the samples.

### Fix

The opening sentences name the smallest fix: "The smallest text change is" a colour, whether it is lighter or darker, how far it is from yours in ΔE2000, and that "it passes all 48 moments". The second sentence says whether a scrim also works. When no text colour can pass, they say why, for example "No lighter or darker version of #FFFFFF passes every moment: the background runs from #0F172A to #F97316, so text light enough for one end is too light for the other." When nothing fails, the tab says "Nothing to fix".

Three routes follow. Each has **Choose for export** (which becomes **Chosen for export**) to pick the CSS that the gold button and the export menu hand out. By default the text colour is chosen when one exists, otherwise the scrim, otherwise the shadow.

1. **Change the text colour.** Walks OKLCH lightness both ways from your text colour, keeping its hue and chroma, until all 48 moments pass. **Lighter** and **Darker** each show the colour found (or why none was), its ΔE from your colour and its worst value; the closer one is marked "closest". **Use #…** sets it as the text colour.
2. **Add a scrim.** Searches the opacity of a black and of a white layer under the text, in 2% steps, blended the way browsers composite. Each shows the opacity, the worst value and the colour value, marked **Smallest** or **Works**. The check box "Check the loop with the 24% black scrim on" applies the smallest scrim to the whole analysis. The CSS for it is shown underneath.
3. **Text shadow**, marked **Not counted by WCAG**. A preview of the worst moment with a halo round the letters, a note on why it helps legibility but "never turns a failing moment into a pass", and the CSS.

## Walkthroughs

### Check text over a CSS animation

1. Set **Background source** to **Paste CSS** and paste your `@keyframes` block with its `animation` line.
2. Check the status line says **Parsed**, and read the notes.
3. Set **Text colour** and **Threshold**.
4. Read **Timeline**: the sentence says how long the text fails and where.

### Check a caption over a video

1. Set **Background source** to **Video**, then drop the file or select **Choose file**.
2. Move **Left**, **Top**, **Width** and **Height** until the outline covers the area behind your text.
3. Select **Sample 48 frames**, and wait for it to finish.
4. Read **Timeline**, then open **Moment** on the worst frame to see it.

### Get a fix to paste

1. Open **Fix** and choose a route with **Choose for export**.
2. Select **Copy fix CSS**.

## Controls

| Control | Values or range | Default |
|---|---|---|
| **Text colour** | Any colour | The colour you opened with, or `#FFFFFF` |
| **Threshold** | 5 options | **WCAG AA · 4.5:1** |
| **Background source** | **Keyframes**, **Paste CSS**, **Video** | **Keyframes** |
| **Keyframe stops** | 2 to 8 stops, positions 0 to 100% | 4 stops |
| **Easing** | 6 options | `ease-in-out` |
| **Duration** | 1 to 20 s | 6 s |
| **Colours blend in** | **sRGB**, **OKLab** | **sRGB** |
| **Text region** (video) | Left and top 0 to 95%; width and height 5 to 100% | 8%, 30%, 60% × 40% |
| **Scrub to a moment** | 48 samples | The worst moment |

## Outputs and exports

| Output | Format | What it contains |
|---|---|---|
| **Copy fix CSS** (gold button) and **CSS for the chosen fix** | CSS | The chosen route: a `.hero-text` colour, a `.hero` scrim as a `linear-gradient` background image over the animated colour, or a `.hero-text` text shadow with a comment that WCAG does not count it. |
| **JSON report · all 48 samples** | JSON | The text colour, threshold, measure and target; the source (the name, duration, easing, blend and stops, or the video's name, length and text region); any scrim applied; a summary of passes, fails and the worst moment; the chosen fix and its CSS; and every sample with its time, background, ratio, APCA Lc and result. |
| **CSV of the samples** | CSV | One row per sample: index, percent, seconds, background, WCAG ratio, APCA Lc and pass or fail. |
| **@keyframes CSS** | CSS | The animation as a `@keyframes` block and an `animation` line. With **OKLab** blending, the stops are written as `oklab()` so browsers blend them the same way. Not available for a video. |
| **Markdown summary** | Markdown | The threshold, the source, the result, the worst moment and the fix. |
| **Save check** | A palette in your Library | Named "Animation check · #FFFFFF text", with the text colour, the stops and the best and worst backgrounds. |
| **Share link** | URL | `?ctool=anim` with the text colour, threshold, source and its settings. |

**Open in another tool** offers **Contrast System** and **Type Readability Sim** (your text on the worst moment), **Accessibility Lab** (the text and the keyframe colours as one set), **Gradient Library** (the keyframes as a gradient) and **Color Inspector** (the text colour).

## Link keys

| Key | What it sets | Values |
|---|---|---|
| `color` | The text colour. | A colour |
| `th` | The threshold. | `aa` (default), `large`, `aaa`, `lc75`, `lc60` |
| `src` | The background source. | `keyframes` (default), `css`, `video` |
| `stops` | The keyframe stops. | 2 to 8 of `hex@percent`, comma-separated, for example `0F172A@0,F97316@100`; without `@`, stops are spread evenly |
| `ease` | The easing. | `linear`, `ease`, `ease-in`, `ease-out`, `ease-in-out` (default), `steps(4)` |
| `dur` | The duration in seconds. | 1 to 20 |
| `blend` | The blending. | `srgb` (default), `oklab` |
| `region` | The video's text region, in percent. | `left,top,width,height`, for example `8,30,60,40` |
| `ctab` | The tab to open on. | `timeline` (default), `moment`, `fix` |

Older threshold ids still work: `wcag`, `wcagl`, `wcaga`, `apca` and `apcal`.

## Accuracy and limits

- **48 samples.** The loop is checked at 48 evenly spaced moments. A very brief flash between two samples can be missed.
- **Colours are blended as browsers render them.** Hex and `rgb()` keyframes blend in gamma-encoded sRGB; choose **OKLab** only if your CSS uses `oklab()` or `oklch()` stops.
- **Pasted CSS is read, not run.** The tool reads `background-color` keyframes, easing and duration. It ignores transparency (what shows through is unknown), and with `alternate` it checks one direction, which covers every colour.
- **Shared links carry stops, not CSS.** A link to a **Paste CSS** check brings back its stops, duration and easing as a simple `@keyframes` block; per-keyframe easing is not in the link.
- **Video stays on your device, and is not in the link.** A shared link to a video check brings the text region only; add the video again. Frames are averaged over the region, so fine detail inside it, such as a bright edge behind one letter, is averaged out. Some video formats cannot be decoded in the browser; the tool says so.
- **Text shadow is not a WCAG fix.** WCAG measures text against the background behind it, not against a halo. Keep a real fix as well.
- **Ratios are rounded down and Lc cut towards zero**, so a moment never shows a level it misses.

## Related

- [Colour Tools documentation](README.md)
- [Open the Colour Tools and work in their panels](launcher-and-panels.md)
- [Contrast System](contrast-system.md) — text on a still background
- [Gradient Library](gradient-library.md) — text contrast across a gradient
- [Accessibility Lab](accessibility-lab.md)
- [Basic Color Tools](../../README.md)
