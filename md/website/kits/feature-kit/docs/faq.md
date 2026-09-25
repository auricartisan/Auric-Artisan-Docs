---
title: Feature Kit — FAQ
description: Short answers to common questions about the Feature Kit's calculator, converter, notes, date tools, developer tools and feedback.
product: Website › Kits › Feature Kit
updated: 2026-09-25
---

# Feature Kit FAQ

## Does the Feature Kit work offline?

Mostly. Once the kit and its tools have loaded on a page, the calculator, graph, notes, date tools and developer tools work without a connection. The Unit Converter needs a connection the first time you open it on a page, to download its unit list. Feedback waits on your device until you are back online.

## Is my calculator history saved?

Yes. Your last 100 calculations are kept in your browser and appear in **History** on any page. Variables, functions you define and the memory value are not saved.

## Can I plot more than one function at once?

No. The graph shows one expression at a time. Define functions in the expression bar and switch between them in the **y =** box.

## Does the calculator handle complex numbers?

No. Results are real numbers. Expressions with no real answer, such as `sqrt(-1)`, show `NaN`.

## Is `%` a percentage?

No. It is the remainder after division: `10 % 3` is `1`.

## Can I solve an equation such as x² = 5?

Yes. Move everything to one side and use `solve`: `solve(x^2 - 5, 2)` returns `2.2360679775`.

## Does the calculator give exact answers?

It gives decimal answers rounded to 14 significant digits, shown to 12. In the expression bar it also shows an exact fraction when one with a denominator up to 10,000 matches, such as `0.875 = 7/8`. Calculus results are numerical estimates. See [Limits and accuracy](../others/limits-and-accuracy.md).

## Why can I not see the Scientific keypad?

The site is in **Basic** mode. Choose **Everything** in the [Advanced Kit](../../advanced-kit/README.md).

## Are my notes private?

Notes are kept only in your browser for auricartisan.com. They are not sent anywhere and not linked to your account.

## Can I move notes to another computer?

Export each note with **Export** and keep the `.md` files. There is no import button; paste the text into a new note on the other computer.

## Is it safe to paste a token or secret into Developer Tools?

The Developer Tools run entirely in your browser and do not send or store what you paste. As with any web page, clear the box when you are done, and prefer test tokens over live ones.

## Does the JWT tool check signatures?

No. It only decodes the header and payload and marks the signature "not verified — decoding only".

## Why does the Business days figure differ from my calendar?

It counts Monday to Friday only and does not know about public holidays.

## Who reads my feedback?

It is sent to the Auric Artisan team. See [Privacy](../others/privacy.md) for what is included.

## How do I stop feedback prompts?

Select **Later** on a prompt or **Not now** on the form. Prompts appear at most twice per visit and once an hour, and less often after you have dismissed several. They only appear inside the Feature Kit's menu, never over the page.
