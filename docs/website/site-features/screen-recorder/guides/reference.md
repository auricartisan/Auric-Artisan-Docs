---
title: Screen recorder — Reference
description: Every recorder option, default, output format, limit and message.
product: Website › Site features › Screen recorder
updated: 2026-09-25
---

# Screen recorder reference

## Setup dialog (Your Recorder)

| Control | Options | Default |
|---|---|---|
| **Recording source** | Screen or window, This tab, Region of this page, Tool canvas | Screen or window |
| **Frame rate** | 15, 24, 30, 60 fps | 30 fps |
| **Quality** | Low — smallest file, Balanced, High — sharpest text | Balanced |
| **Resolution cap** | Native, 1080p, 720p, 480p | Native |
| **Countdown** | None, 3 seconds, 5 seconds | 3 seconds |
| **Microphone** | On, off | Off |
| **Tab audio** | On, off | On |
| **Highlight the cursor** | On, off | Off |
| **My recordings** | Opens the recordings list | — |
| **Reset setup** / **Confirm reset** | Two-step reset of all the above | — |
| **Start recording** | Starts with the chosen source | — |
| **Reset dialog position** | Centres the dialog | — |
| **Close** | Closes the dialog | — |

All choices are remembered in this browser, as is whether the recording bar is collapsed.

## Recording bar

| Control | Action |
|---|---|
| Grip | Move the bar |
| Timer and size | Elapsed time and file size |
| **Pause recording** / **Resume recording** | Pause or resume |
| **Stop and save** | Stop and keep |
| **Discard recording** | Stop and throw away |
| **Collapse to a dot** / **Expand controls** | Shrink or restore the bar |

## Recordings list

| Action | Output |
|---|---|
| Thumbnail (Play) | Opens the player |
| Title | Editable name |
| **Download video** | MP4 or WebM file |
| **GIF** | Animated GIF: 10 fps, up to 640 px wide, up to 300 frames, loops |
| **Frames** | ZIP of PNGs: 5 per second, up to 1,280 px wide, up to 120 frames |
| **Still** | One PNG at 1 second (or half the length), up to 1,280 px wide |
| **Trim** | New MP4 or WebM of the chosen span, re-encoded in real time |
| **Delete** | Removes the recording (select twice within 4 seconds) |

## Formats

| Output | Format |
|---|---|
| Video | MP4 (H.264 video, AAC audio) where the browser can record it; otherwise WebM (VP9 or VP8 video, Opus audio) |
| Animated image | GIF, up to 255 colours |
| Frames | ZIP containing `frame-0001.png` and onward |
| Still | PNG |

## Limits

| Limit | Value |
|---|---|
| Longest recording | 30 minutes |
| Storage warning | Below about 50 MB of free browser storage |
| Region pick threshold | A drag under 12 pixels selects the element instead |

## Keyboard

| Keys | Action |
|---|---|
| `Alt` + `Shift` + `R` | Open the setup dialog; while recording, stop and save |
| `Alt` + `Shift` + `P` | Pause or resume while recording |
| `Esc` | Close the dialog, the list, the player or the region picker; cancel **Confirm reset** |
| Arrow keys on the dialog grip | Move the dialog (`Shift` for finer steps) |

## Messages

| Message | Meaning |
|---|---|
| A recording is already running. | You opened the setup during a recording |
| No recordable canvas on this page. | **Tool canvas** cannot be used here |
| This browser cannot capture the screen. | Screen sources are unavailable |
| Microphone unavailable — recording without it. | The microphone was refused or missing |
| Storage is nearly full — this recording may not save. Delete some clips first. | Less than about 50 MB free |
| Time limit reached — recording stopped. | 30 minutes reached |
| Recording discarded. | **Discard recording** was selected |
| Recording saved — time, size. | The recording was kept |
| Saved to your downloads (browser storage was unavailable). | Storage refused; file downloaded instead |
| Nothing was recorded. | The recording was empty |
| Recording failed. / Could not start recording. / Recording cancelled. | Starting failed or was cancelled |
| Recorder returned to the center. | The dialog position was reset |
| Recorder setup reset to defaults. | **Confirm reset** was selected |
| GIF exported — size. | A GIF was downloaded |
| Trimmed clip exported. / End must be after start. / Trimming failed. | Trim results |
| That recording could not be read. | The stored recording is unreadable |
