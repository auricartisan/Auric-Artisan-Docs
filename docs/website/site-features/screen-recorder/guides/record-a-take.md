---
title: Screen recorder — Record a take
description: Choose a source and capture settings, add audio, draw a region, and control the recording with the recording bar.
product: Website › Site features › Screen recorder
updated: 2026-09-25
---

# Record a take

## Choose a source

| Source | Description on screen | Good for |
|---|---|---|
| **Screen or window** | Pick any screen, window, or tab. Controls stay out of the video unless you share this tab. | Showing several apps or windows |
| **This tab** | Records this page. The recording bar is part of the page, so collapse it to keep it small. | Walking through a page or tool |
| **Region of this page** | Drag a rectangle or click an element. Everything outside it is cropped away. | A tidy clip of one panel or control |
| **Tool canvas** | Records a tool's drawing surface directly — pixel-exact, and nothing on screen can spoil the take. | Animated or drawn output from a tool |

When a source is not possible, it is greyed out with the reason:

- "No recordable canvas on this page." — the page has no canvas large enough to record;
- "This browser cannot capture the screen." — the browser does not let pages capture the screen (the **Tool canvas** source may still work).

> **Note:** When you record this tab, anything shown on the page is in the video, including the recording bar. Collapse the bar to a dot, or record a region or a canvas, to keep it out.

## Choose capture settings

| Setting | Options | Default |
|---|---|---|
| **Frame rate** | 15 fps — smallest, 24 fps — cinematic, 30 fps — standard, 60 fps — smoothest | 30 fps |
| **Quality** | Low — smallest file, Balanced, High — sharpest text | Balanced |
| **Resolution cap** | Native, 1080p, 720p, 480p | Native |
| **Countdown** | None, 3 seconds, 5 seconds | 3 seconds |

**Resolution cap** scales down recordings wider than the chosen size (1080p is 1,920 pixels wide, 720p is 1,280, 480p is 854). **Native** keeps the source's own size. Higher quality and frame rate make larger files.

## Add audio and a pointer highlight

| Switch | Description on screen | Default |
|---|---|---|
| **Microphone** | Narrate while you record. | Off |
| **Tab audio** | Include sound the page itself makes. | On |
| **Highlight the cursor** | Draws an accent ring around the pointer. | Off |

- The browser asks for microphone permission the first time. If the microphone cannot be used, recording continues without it and the message reads "Microphone unavailable — recording without it."
- **Tab audio** is recorded only when the shared screen, window or tab offers sound; your browser's sharing dialog may have its own "share audio" option.
- If the browser has no microphone support, the switch is greyed out with "Not available in this browser."

## Record a region

1. Choose **Region of this page** and select **Start recording**.
2. The page dims with the hint "**Drag** to draw a region, or **click** an element to snap to it. **Esc** cancels."
3. Either drag a rectangle, or move over the page (a box outlines the element under the pointer) and click to use that element.
4. Your browser asks to share this tab. Allow it.

Only the region is recorded; the rest of the tab is cropped away. A click or a very small drag (under 12 pixels) counts as choosing the element under the pointer.

## Record a tool canvas

Choose **Tool canvas** and select **Start recording**. The recorder uses the canvas a tool offers for recording, or else the largest visible canvas on the page. No sharing dialog is needed.

## The countdown

With a countdown set, a large number counts down on the page before recording starts.

## The recording bar

While recording, a small bar floats on the page:

| Part | What it does |
|---|---|
| Grip | Drag to move the bar |
| Red dot and timer | Shows elapsed time |
| Size | File size so far |
| **Pause recording** / **Resume recording** | Pauses or resumes (`Alt` + `Shift` + `P`) |
| **Stop and save** | Ends the recording and saves it (`Alt` + `Shift` + `R`) |
| **Discard recording** | Ends and throws the recording away ("Recording discarded.") |
| **Collapse to a dot** / **Expand controls** | Shrinks the bar to a small dot, or restores it; remembered |

Click a collapsed dot to expand it again.

## When a recording stops by itself

- Your browser's own **Stop sharing** button ends the recording and saves it.
- A recording stops at **30 minutes**: "Time limit reached — recording stopped."
- If you try to leave or reload the page during a recording, the browser asks you to confirm.

## After you stop

- The recording is saved to **My recordings**, titled "Recording" with the date and time, and the list opens with it highlighted.
- If there is little browser storage left (under about 50 MB), the recorder warns before you start: "Storage is nearly full — this recording may not save. Delete some clips first."
- If the browser refuses to store it, the file is downloaded straight away instead: "Saved to your downloads (browser storage was unavailable)."
- If nothing was captured, the message reads "Nothing was recorded."

## Reset your setup

Select **Reset setup**, then **Confirm reset** within four seconds. The source and every setting return to their defaults: "Recorder setup reset to defaults." Press `Esc` while it says **Confirm reset** to cancel.
