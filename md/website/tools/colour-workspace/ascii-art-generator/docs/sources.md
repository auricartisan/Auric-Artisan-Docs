---
title: ASCII Art Generator — Choose a source
description: Convert an image, a line of text or a webcam frame, and every way to get a picture into the ASCII Art Generator.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Choose a source

The **Source** group at the top of the rail has three buttons: **Image**, **Text** and **Webcam**. Switching source converts the new source at once if it has something to show, or returns to the empty stage if it has not.

## Image

Use a photo, screenshot, logo or drawing.

Ways to load one:

- select the drop area (*Drop an image, or click to browse*) or **Choose a file** on the empty stage, and pick a file;
- drag a file anywhere onto the tool; the stage highlights while you drag;
- copy an image and press `Ctrl` + `V` (`Cmd` + `V` on a Mac) anywhere on the page, as long as you are not typing in a field;
- select **Try an example** to load a built-in picture of a lit sphere on a dark gradient.

Accepted types are PNG, JPEG, GIF, WebP, BMP, SVG and TIFF, up to 20 MB. Whether TIFF opens depends on your browser.

After loading, the rail shows the picture's size, such as **1200 × 800 px**. Pictures larger than 4,000 pixels on a side, or larger than 12 megapixels, are scaled down first, and a note says so, for example **Downscaled from 6000×4000 to 4000×2667**. The art never needs that much detail, so you will not normally see a difference.

**Clear** removes the picture and returns the stage to its empty state.

An animated GIF is converted as a single still frame.

## Text

Select **Text** (or **Type some text** on the empty stage) to turn a word or short line into art.

| Control | What it does | Default |
| --- | --- | --- |
| Text box | The text to draw. | ASCII |
| Font | monospace, Courier New, Consolas, Monaco, Fira Code or Source Code Pro. | monospace |
| Size | 8 to 128 pixels. | 48 |
| Weight | **Normal**, **Bold** or **Black**. | Bold |
| **White on black** | Draws light letters on a dark ground instead of dark on light. | off |

The text is first drawn as a picture in the chosen font, then converted like an image. The font must be installed on your device; if it is not, your browser substitutes another. Bigger sizes give smoother letter shapes; set **Detail** wide enough to hold them.

If the box is empty, the stage returns to its empty state.

## Webcam

Select **Webcam** (or **Use the webcam** on the empty stage) to see the camera controls.

At the time of writing, the camera cannot be used on auricartisan.com. The site tells browsers not to give any of its pages camera access, so **Start** does not turn the camera on, and a message under the buttons says that camera permission was denied. Changing the camera permission in your browser does not help. To convert a picture of yourself, take a photo with your camera app and load it with **Image**.

For reference, the controls are:

| Control | What it is for |
| --- | --- |
| **Start** | Ask for the camera and show a small live preview. |
| **Capture** | Convert the current frame. |
| **Keep converting every frame** | Convert continuously, several times a second. |
| **Smooth between frames** | Blend each frame a little with the one before, to reduce flicker. |
| **Stop** | Turn the camera off. |

## Related

- [Looks, colour and detail](looks-colour-and-detail.md)
- [Troubleshooting](troubleshooting.md)
- [Privacy](../others/privacy.md)
