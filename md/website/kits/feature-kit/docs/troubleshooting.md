---
title: Feature Kit — Troubleshooting
description: Fixes for Feature Kit problems, and what every calculator error message means.
product: Website › Kits › Feature Kit
updated: 2026-09-25
---

# Feature Kit troubleshooting

For problems shared by every kit, such as a missing launcher or a panel in the wrong place, see [Troubleshooting kits](../../docs/troubleshooting.md).

## The page goes dark and I cannot click it

**Why:** With Focus mode off, the Feature Kit dims the page and keeps keyboard focus inside the kit.

**What to do:** Click the dimmed page to close the kit, or select **Focus mode** in the kit's title bar to keep it open without dimming.

## The Feature launcher does not close the kit

**Why:** With Focus mode on, the launcher and `Ctrl` + `Shift` + `K` move focus into the kit instead of closing it.

**What to do:** Select **Close** in the title bar, or press `Esc` twice (once to leave a tool, once to close).

## Typing numbers does nothing on the calculator

**Why:** Keyboard typing reaches the keypad only while the Scientific Calculator is open and the cursor is not in a text box. If the cursor is in the expression bar, the **y =** box or a page field, your keys go there instead.

**What to do:** Click an empty part of the calculator, or the display, then type. Or type into the expression bar and press `Enter`.

## The Scientific or Programmer tab is missing

**Why:** The site's tool visibility mode is **Basic**, which shows only the **Basic** keypad. In **Advanced** mode, the **Basic** keypad is hidden instead.

**What to do:** Open the [Advanced Kit](../../advanced-kit/README.md) and choose **Everything** to see all three tabs.

## My variables and functions disappeared

**Why:** Variables, your own functions and the memory value last only while the page is open. Moving to another page or reloading clears them.

**What to do:** Keep definitions you reuse in [Notes](notes.md) and paste them into the expression bar. Calculations themselves stay in the history.

## The result of 2+3×2 is 8, not 10

**Why:** After a result, typing an operator adds to the end of the previous expression rather than to the result, and multiplication comes before addition.

**What to do:** Start the next step with **Ans**: `Ans×2`.

## % does not give a percentage

**Why:** `%` is the remainder operator: `10 % 3` is `1`.

**What to do:** Work out percentages with multiplication and division: `80*15/100`.

## A derivative shows 12.0000000001 instead of 12

**Why:** `diff` and `diff2` estimate derivatives numerically. The last digits can carry tiny rounding noise.

**What to do:** Round the result with `roundto(diff(x^3, 2), 6)`. See [Limits and accuracy](../others/limits-and-accuracy.md).

## Calculator error messages

| Message | Cause | Fix |
|---|---|---|
| `Division by zero` | You divided by 0 | Change the divisor |
| `Unknown variable: name` | The name is not a variable or constant. Also happens for `sin 30` (read as `sin30`) | Define it with `name = value`, check the spelling and case, or add brackets: `sin(30)` |
| `Unknown function: name` | No built-in or defined function has that name | Check spelling and case, or define it: `name(x) = ...` |
| `Unexpected token after expression` | Two values sit next to each other with no operator, such as `2pi` | Add the operator: `2*pi` |
| `Unexpected character: =` | An `=` where it cannot go, such as `pi = 3` | Choose a name that is not a constant |
| `Unexpected character: ...` | A character the calculator does not understand | Remove it |
| `Unexpected end of expression` | The expression stops too early, for example `2+` | Finish the expression |
| `Expected )` | A bracket is not closed | Add the `)` |
| `Invalid numeric literal` | A malformed number, such as `2e` or `1.2.3` | Fix the number; write `2*e` for two times e |
| `Invalid hexadecimal literal`, `Invalid binary literal` | `0x` or `0b` with no digits after it | Add digits |
| `sin expects 1 argument` (and similar) | Wrong number of values in a function call | Check the function in [Calculator functions](calculator-functions.md) |
| `Cannot redefine sin` (and similar) | You tried to define a function with a built-in name | Use another name |
| `Recursion too deep` | One of your functions calls itself without end | Rewrite the function |
| `Expression too complex` | The expression needs too many steps, for example huge nested sums | Simplify it or use smaller ranges |
| `solve: no convergence (try lo, hi bounds)` | No root was found near your guess | Try another guess, or give a range: `solve(expr, low, high)` |
| `sum: too many terms`, `product: too many terms` | The range spans more than 1,000,000 steps | Use a smaller range |
| `diff(expr, [var,] at)` and similar | A calculus function has the wrong number of arguments | See [Calculator functions](calculator-functions.md) |
| `Unclosed diff(...)` and similar | A calculus function's bracket is not closed | Add the `)` |
| `Need more values` | A sample statistic was given too few values | Give at least 2 values |
| `Factorial of negative`, `fib of negative` | A negative number where it is not allowed | Use zero or a positive number |
| `nextprime: too large` | The number is beyond the range the calculator can check | Use a smaller number |
| `NaN` | The answer is undefined, for example `sqrt(-1)` or `7 % 0` | Check the inputs |
| `∞` | The answer is too large or infinite, for example `1e400` or `fact(171)` | See [Limits and accuracy](../others/limits-and-accuracy.md) |

## The graph is empty

**Why:** The **y =** expression has a mistake, uses something other than `x` as its variable, or is undefined across the visible range.

**What to do:** Test the expression in the expression bar first, with a value for `x`, for example `x = 2` then your expression. Select the graph's reset button to return to the starting view.

## The Unit Converter says "Units could not be loaded"

**Why:** The unit list is downloaded the first time you open the converter on a page, and the download failed.

**What to do:** Check your connection and select **Try again**.

## A conversion shows a strange number

**Why:** The value box reads a number from the start of what you type. A comma is not a decimal separator, so `1,5` is read as `1`.

**What to do:** Use a dot for decimals: `1.5`.

## I cannot find a unit in the search results

**Why:** The search narrows the category pills; it does not pick the unit.

**What to do:** Select the category pill it shows, then choose the unit from the **From** or **To** list.

## A note disappeared

**Why:** **Delete** removes a note immediately, without asking. Notes are also lost if you clear the site's data in your browser, and they do not move between browsers or devices.

**What to do:** There is no undo. Use **Export** regularly for notes you want to keep.

## Copy does not work

**Why:** Your browser blocked clipboard access, which can happen outside a secure connection or with strict permissions.

**What to do:** Allow clipboard access for the site, or select the text and copy it with `Ctrl` + `C`.

## A tool card shows "failed to load"

**Why:** Notes, Date & Time and Developer Tools download the first time you open them on a page. The download failed.

**What to do:** Check your connection and reload the page.

## The feedback form keeps saying "Could not send yet"

See the message table in [Feedback](feedback.md). Your feedback is usually saved on your device and sent automatically once the connection is back.
