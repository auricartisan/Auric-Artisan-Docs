---
title: Animation Contrast — Check text over animated backgrounds and video
description: Sample an animated background, from CSS keyframe colours or a video file, at 48 points, check text contrast at each one, find the worst frame and get a text colour that passes throughout.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Animation Contrast

Most contrast checks assume the background stays still. Hero sections with animated gradients, background videos and colour transitions do not: text that is readable at the start of a loop can become unreadable for part of it. Animation Contrast checks the whole timeline.

You give it a text colour and an animated background, either a list of keyframe colours or a video file. It takes 48 evenly spaced samples along the timeline, checks the text against each one with the standard you choose, shows a pass or fail strip, picks out the worst moment, and suggests a single text colour that would pass at every sample.

Animation Contrast is in the launcher's **Essentials** group.

## Open it

Open the launcher and select **Animation Contrast**. See [Open the Colour Tools](launcher-and-panels.md). The text colour starts as the colour you opened the tool with, or white (#FFFFFF).

## Screen tour

1. **Setup** (*Text + animated background*):
   - **Text color**: a colour field.
   - **Threshold**: the standard to test against.
   - **Source**: **CSS keyframes** or **Video frames**.
2. The background section:
   - For **CSS keyframes**: **Keyframe stops**, with a note such as *4 colors · interpolated in OKLab*, one numbered colour row per stop, and **+ Add stop**, **− Remove last** and **Reset**.
   - For **Video frames**: **Video source**, a drop area with **Choose file**, and once a video is loaded, a player, **Sample 48 frames** and **Clear video**.
3. The results:
   - **Timeline**: 48 ticks coloured with each sample's background, marked pass or fail, an axis from 0 % to 100 %, and two pills: *N / 48 pass (P%)* and *N fail*.
   - **Worst frame** (*Lowest contrast in timeline*): a preview of body text and an 11-pixel caption on the worst background, with its position (*At t = 62%*), its HEX code, the measured value, and its WCAG and APCA levels.
   - **Suggested safe text color**: a colour chip, the worst contrast it reaches, and **Use as text color**.

## Thresholds

| Option | Passes when |
| --- | --- |
| **WCAG 2.x (4.5:1)** | The contrast ratio is at least 4.5:1 (AA, normal text). |
| **WCAG 2.x large (3:1)** | The ratio is at least 3:1 (AA, large text). |
| **WCAG 2.x AAA (7:1)** | The ratio is at least 7:1. |
| **APCA Lc 75 (body)** | The APCA lightness contrast is at least 75 (either sign). |
| **APCA Lc 60 (large)** | The APCA lightness contrast is at least 60. |

## Tasks

### Check text over a CSS gradient animation

1. Set **Text color** to your heading or body text colour.
2. Keep **Source** on **CSS keyframes**.
3. Enter the colours your background passes through, in order, as keyframe stops. Use **+ Add stop** for more (up to eight) and **− Remove last** to remove (at least two remain). **Reset** restores the starting set: #0F172A, #1E3A8A, #9333EA, #F97316.
4. Choose a **Threshold**.
5. Read the **Timeline**. Hover over a tick to see its position, value and pass or fail.

The tool blends between neighbouring stops in OKLab and spaces the stops evenly across the timeline, like a CSS animation with evenly spaced keyframes and linear timing.

Result: you see what share of the animation keeps your text readable, and where it fails.

### Check text over a background video

1. Set **Source** to **Video frames**.
2. Drop a video file on the drop area, or select **Choose file**. The video appears with player controls, muted.
3. Wait until it has loaded, then select **Sample 48 frames**. A **Sampling frames…** message appears, then **Sampled 48 frames**.
4. Read the timeline. Select a tick to move the video to that moment.

For each sample the tool takes the average colour of the whole frame. Short clips (the drop area suggests about 30 seconds at most) sample fastest.

Result: a pass or fail reading across the whole video.

### Get a text colour that always passes

1. After any check, read **Suggested safe text color**. Its note says **Passes every sampled frame** or **Best available — still fails somewhere**.
2. Select **Use as text color** to apply it. **Applied #HEX** appears and the timeline updates.

The suggestion keeps your text colour's hue and chroma and moves its OKLCH lightness up and down in small steps until the worst sample passes, then picks whichever direction needed the smaller change. If neither direction passes, it offers the colour that did best.

Result: one static text colour you can use over the whole animation, or a clear sign that the background needs changing (for example an overlay or a darker range).

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Text color** | The text colour to test | HEX, colour well, dice | The colour you opened with, or #FFFFFF |
| **Threshold** | The pass standard | 5 options (see Thresholds) | WCAG 2.x (4.5:1) |
| **Source** | Where background colours come from | CSS keyframes, Video frames | CSS keyframes |
| Keyframe stop | One background colour | Colour well or HEX | 4 stops |
| **+ Add stop** | Adds a white stop at the end | Up to 8 stops | — |
| **− Remove last** | Removes the last stop | At least 2 stops | — |
| **Reset** | Restores the four default stops | — | — |
| Drop area / **Choose file** | Loads a video | Video files | — |
| **Sample 48 frames** | Samples the loaded video | 48 samples | — |
| **Clear video** | Removes the video | — | — |
| Timeline tick | Shows details; in video mode, seeks the video | 48 ticks | — |
| **Use as text color** | Applies the suggested colour | — | — |

## Outputs and exports

The tool has no file export. Copy the suggested colour's HEX code from the **Text color** field after applying it.

## Accuracy and limits

- 48 samples catch most problems in a loop, but a very brief flash between two samples can be missed.
- Keyframe mode assumes evenly spaced keyframes and linear timing in OKLab. Real CSS animations may use different timing, blend in sRGB, or overlap several layers.
- Video mode uses the average colour of each frame. Text over a small bright area in an otherwise dark frame can fail even when the average passes. Check the area behind your text separately if the video has strong local contrast.
- The video is read in your browser and is not uploaded. Some video formats may not play in every browser.
- APCA figures use a simplified form of a draft method; see [Contrast System](contrast-system.md).

## Related

- [Colour Tools documentation](README.md)
- [Contrast System](contrast-system.md)
- [Accessibility Lab](accessibility-lab.md)
- [Basic Color Tools](../../README.md)
