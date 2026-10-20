---
title: Auric Artisan Formatter — options reference
description: All 391 Auric Artisan Formatter formatting options in 17 categories, with type, default, allowed values and effect.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Options reference

Auric Artisan Formatter has 391 formatting options in 17 categories. This page lists every one. The eleven settings that control how the extension works in VS Code (preset, format on save, the workspace scan and so on) are in the [reference](reference.md).

## How to use this page

Each option can be set in four places. The same name works in all of them:

| Where | How it is written |
| --- | --- |
| VS Code settings | `"auricFormatter.printWidth": 100` |
| A configuration file such as `.auricformatrc` | `"printWidth": 100` (no prefix) |
| The command line | `--print-width 100` (the name in kebab case; booleans also take a `--no-` form) |
| An inline directive in a file | `// @auric printWidth=100` |

The defaults shown are the extension's own defaults. A preset changes many of them; `"preset": "prettier"`, for example, switches every Auric-only enhancement off. Anything you set yourself wins over the preset. See [Configuration](configuration.md) and [Presets](presets.md).

Options that only apply to some languages only affect files in those languages. Formatter Studio's **Affects this file** filter shows which options change the file you are looking at.

Options marked "Experimental" are still settling; Formatter Studio hides them unless you tick **Experimental**.

## Global

21 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.byteOrderMark` | string | `preserve` | `preserve`, `add`, `remove` | Decide what happens to a UTF-8 byte order mark at the start of the file. |
| `auricFormatter.cursorOffset` | integer | `-1` | -1–no maximum | Track this character offset through the reformat and report where it lands. |
| `auricFormatter.editorconfig` | boolean | `true` |  | Read .editorconfig and translate indent_style, indent_size, end_of_line, max_line_length and the final-newline keys. |
| `auricFormatter.embeddedLanguageFormatting` | string | `auto` | `auto`, `off` | Decide whether code embedded inside another language is formatted. |
| `auricFormatter.endOfLine` | string | `lf` | `lf`, `crlf`, `cr`, `auto`, `preserve` | Choose the line ending written to disk. |
| `auricFormatter.filepath` | string | empty |  | Supply the path the text came from so language inference and glob overrides can work on stdin. |
| `auricFormatter.formatEmbeddedUnknown` | boolean | `false` |  | Attempt the universal engine on embedded fragments whose language has no native printer. |
| `auricFormatter.insertFinalNewline` | boolean | `true` |  | Guarantee the file ends with exactly one line ending. |
| `auricFormatter.insertPragma` | boolean | `false` |  | Insert an @format pragma into the leading comment of files that were formatted. |
| `auricFormatter.parser` | string | empty |  | Force a specific parser instead of inferring one from the file path or language id. |
| `auricFormatter.plugins` | array | `[]` |  | List additional printer plugins to load, by module path or by registered plugin name. |
| `auricFormatter.pragmaKeyword` | string | `format` |  | Set the bare word an opt-in pragma comment must contain, without the leading at sign. |
| `auricFormatter.printWidth` | integer | `80` | 0–1000 | Wrap lines that would otherwise exceed this many columns wherever the syntax allows a break. |
| `auricFormatter.rangeEnd` | integer | end of file | 0–no maximum | Format only the text before this character offset. |
| `auricFormatter.rangeStart` | integer | `0` | 0–no maximum | Format only the text at or after this character offset. |
| `auricFormatter.requirePragma` | boolean | `false` |  | Format only files whose leading comment carries an @format or @auric-format pragma. |
| `auricFormatter.respectIgnoreComments` | boolean | `true` |  | Honour auric-ignore, auric-ignore-start and auric-ignore-end comments and leave those regions untouched. |
| `auricFormatter.tabWidth` | integer | `2` | 0–24 | Set how many columns one level of indentation occupies. |
| `auricFormatter.tabWidthByLanguage` | array | `[]` |  | Override `tabWidth` for individual languages with `languageId=width` entries such as `python=4`. |
| `auricFormatter.trimTrailingWhitespace` | boolean | `true` |  | Strip whitespace at the end of every line outside of strings and preserved blocks. |
| `auricFormatter.useTabs` | boolean | `false` |  | Indent with hard tab characters instead of spaces. |

Notes and language-specific defaults:

- `auricFormatter.printWidth`: `120` for java, kotlin, scala, csharp, swift.
- `auricFormatter.tabWidth`: `4` for python, php, java, kotlin, csharp, c, cpp, objective-c, objective-cpp, rust, swift, groovy, solidity, apex; `4` for go, gomod, gowork, makefile, gotmpl.
- `auricFormatter.useTabs`: `true` for go, gomod, gowork, makefile, gotmpl.

## Common

15 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.arrowParens` | string | `always` | `always`, `avoid` | Choose whether a single arrow function parameter is parenthesised. |
| `auricFormatter.bracketSameLine` | boolean | `false` |  | Put the closing angle bracket of a multi-line opening tag on the last attribute line. |
| `auricFormatter.bracketSpacing` | boolean | `true` |  | Print spaces just inside object literal braces, as in `{ foo: 1 }`. |
| `auricFormatter.curlyBraces` | string | `preserve` | `preserve`, `all`, `multi-line` | Decide whether single-statement control-flow bodies get braces. |
| `auricFormatter.hexCase` | string | `lower` | `preserve`, `lower`, `upper` | Choose the letter case of hexadecimal digits in numeric literals and colour values. |
| `auricFormatter.htmlWhitespaceSensitivity` | string | `css` | `css`, `strict`, `ignore` | Choose how strictly whitespace around HTML elements is preserved. |
| `auricFormatter.jsxSingleQuote` | boolean | `false` |  | Prefer single quotes over double quotes inside JSX attributes. |
| `auricFormatter.objectWrap` | string | `preserve` | `preserve`, `collapse` | Decide whether the author's first newline inside an object forces it to stay expanded. |
| `auricFormatter.proseWrap` | string | `preserve` | `preserve`, `always`, `never` | Choose how prose paragraphs are wrapped. |
| `auricFormatter.quoteProps` | string | `as-needed` | `as-needed`, `consistent`, `preserve`, `consistent-as-needed` | Choose when object property keys are quoted. |
| `auricFormatter.semi` | boolean | `true` |  | Print a semicolon at the end of every statement. |
| `auricFormatter.singleAttributePerLine` | boolean | `false` |  | Put every attribute on its own line as soon as a tag has to break. |
| `auricFormatter.singleQuote` | boolean | `false` |  | Prefer single quotes over double quotes for strings. |
| `auricFormatter.trailingComma` | string | `all` | `all`, `es5`, `none` | Choose where trailing commas are added in multi-line constructs. |
| `auricFormatter.vueIndentScriptAndStyle` | boolean | `false` |  | Indent the contents of the top-level `<script>` and `<style>` blocks in a single file component. |

## JavaScript

60 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.arrayBracketSpacing` | boolean | `false` |  | Print spaces just inside array brackets, as in `[ 1, 2 ]`. |
| `auricFormatter.arrayElementsPerLine` | integer | `0` | 0–100 | Print at most this many array elements per line, or 0 to fit as many as the print width allows. |
| `auricFormatter.arrowBodyStyle` | string | `preserve` | `preserve`, `as-needed`, `always` | Choose whether arrow functions keep braced bodies or collapse to expressions. |
| `auricFormatter.arrowChainBreak` | string | `as-needed` | `as-needed`, `always`, `never` | Choose how chains of curried arrow functions are broken. |
| `auricFormatter.assignmentLayout` | string | `auto` | `auto`, `break-after-operator`, `break-lhs`, `chain`, `never-break-after-operator` | Choose how the two sides of an assignment are split when the line is too long. |
| `auricFormatter.awaitParens` | string | `as-needed` | `as-needed`, `always` | Choose when the operand of `await` is wrapped in parentheses. |
| `auricFormatter.breakBeforeBinaryOperators` | boolean | `false` |  | Start the new line with the operator when a binary expression breaks. |
| `auricFormatter.breakLongStrings` | boolean | `false` |  | Split a string literal that overflows the print width into concatenated parts. |
| `auricFormatter.catchPosition` | string | `same-line` | `same-line`, `new-line` | Choose where `catch` and `finally` sit relative to the preceding closing brace. |
| `auricFormatter.chainedCallIndent` | string | `indent` | `indent`, `align`, `preserve` | Choose how a broken member chain is indented. |
| `auricFormatter.chainedCallKeepFirstCall` | boolean | `true` |  | Keep the first call of a member chain attached to its receiver, as in `expect(x)\n .toBe(y)`. |
| `auricFormatter.directivePrologueQuotes` | string | `preserve` | `preserve`, `follow`, `double`, `single` | Choose how the quotes around directive prologues are printed. |
| `auricFormatter.doWhilePosition` | string | `same-line` | `same-line`, `new-line` | Choose where the trailing `while` of a do-while loop sits. |
| `auricFormatter.elsePosition` | string | `same-line` | `same-line`, `new-line` | Choose where the `else` keyword sits relative to the preceding closing brace. |
| `auricFormatter.emptyBlockStyle` | string | `collapse` | `collapse`, `preserve`, `expand` | Choose how blocks with no statements are printed. |
| `auricFormatter.firstArgumentHugging` | boolean | `true` |  | Let a leading function argument expand in place for call shapes like `describe(function () {}, opts)`. |
| `auricFormatter.functionParameterNewline` | string | `multiline` | `preserve`, `always`, `never`, `multiline` | Choose how function parameter lists are broken across lines. |
| `auricFormatter.generatorStarPosition` | string | `after-function` | `after-function`, `before-name`, `spaced` | Choose where the star of a generator function sits. |
| `auricFormatter.jsxBracketSameLine` | boolean | `false` |  | Put the closing angle bracket of a multi-line JSX opening tag on the last attribute line. |
| `auricFormatter.jsxEmptyExpressionComment` | boolean | `true` |  | Keep a comment that is the sole contents of a JSX expression container on its own line. |
| `auricFormatter.jsxSelfCloseSpace` | boolean | `true` |  | Print a space before the slash of a self-closing JSX element. |
| `auricFormatter.jsxSingleAttributeSameLine` | boolean | `true` |  | Keep an element with exactly one short attribute on a single line. |
| `auricFormatter.jsxSortProps` | boolean | `false` |  | Sort JSX attributes, keeping `key` and `ref` first and spreads pinned in place. |
| `auricFormatter.jsxSpaceBraces` | boolean | `false` |  | Print spaces just inside JSX expression braces, as in `{ value }`. |
| `auricFormatter.jsxWrapMultiline` | string | `parens` | `parens`, `preserve`, `never` | Choose whether multi-line JSX expressions are wrapped in parentheses. |
| `auricFormatter.labelIndent` | string | `preserve` | `preserve`, `dedent`, `flush` | Choose how statement labels are indented. |
| `auricFormatter.lastArgumentHugging` | boolean | `true` |  | Let a trailing function or object argument expand in place instead of breaking the whole call. |
| `auricFormatter.memberChainBreakThreshold` | integer | `3` | 0–32 | Break a member chain across lines once it contains at least this many member accesses. |
| `auricFormatter.methodChainCallThreshold` | integer | `3` | 0–32 | Break a member chain across lines once it contains at least this many call expressions. |
| `auricFormatter.newExpressionParens` | string | `always` | `always`, `preserve` | Choose whether a `new` expression with no arguments keeps its parentheses. |
| `auricFormatter.normalizeNumericLiterals` | boolean | `true` |  | Normalise numeric literals by trimming a trailing dot, adding a leading zero and dropping a redundant exponent sign. |
| `auricFormatter.numericLiteralCase` | string | `lower` | `preserve`, `lower`, `upper` | Choose the letter case of the non-digit parts of numeric literals. |
| `auricFormatter.numericSeparators` | string | `preserve` | `preserve`, `remove`, `thousands` | Choose how underscore separators inside numeric literals are handled. |
| `auricFormatter.objectDestructuringNewline` | string | `multiline` | `preserve`, `always`, `never`, `multiline` | Choose how object destructuring patterns are broken across lines. |
| `auricFormatter.objectExpandThreshold` | integer | `0` | 0–100 | Force an object with at least this many properties onto multiple lines, or 0 to decide by width alone. |
| `auricFormatter.objectPropertyNewline` | string | `preserve` | `preserve`, `always`, `never` | Choose whether every object property gets its own line. |
| `auricFormatter.preserveArrayFormatting` | boolean | `false` |  | Keep the author's line breaks in arrays of numbers and short literals so hand-laid tables survive. |
| `auricFormatter.preserveObjectShape` | boolean | `true` |  | Keep an object expanded when the author already broke it after the opening brace. |
| `auricFormatter.preserveParens` | boolean | `false` |  | Keep every parenthesis the author wrote, even where precedence makes it redundant. |
| `auricFormatter.quoteStyleForJSXText` | string | `preserve` | `preserve`, `entities`, `curly` | Choose how quotation marks inside JSX text are printed. |
| `auricFormatter.removeRedundantParens` | boolean | `true` |  | Drop parentheses that precedence and readability rules make unnecessary. |
| `auricFormatter.semiColonBeforeIIFE` | boolean | `true` |  | Start a line with a defensive semicolon when omitting semicolons would let it join the statement above. |
| `auricFormatter.shortArrayThreshold` | integer | `0` | 0–100 | Collapse an array onto one line when it holds at most this many short elements, or 0 to decide by width alone. |
| `auricFormatter.singleLineArrowBody` | boolean | `true` |  | Keep a short arrow function body on the same line as the arrow. |
| `auricFormatter.singleLineIfStatement` | string | `fit` | `fit`, `preserve`, `never` | Decide whether a braceless `if` may share a line with its body. |
| `auricFormatter.spaceAfterKeyword` | boolean | `true` |  | Print a space between a control-flow keyword and its opening parenthesis, as in `if (x)`. |
| `auricFormatter.spaceAroundOperators` | boolean | `true` |  | Print a single space on each side of binary and assignment operators. |
| `auricFormatter.spaceBeforeBlocks` | boolean | `true` |  | Print a space between a closing parenthesis or keyword and an opening block brace. |
| `auricFormatter.spaceBeforeColon` | boolean | `false` |  | Print a space before the colon in object properties and labels. |
| `auricFormatter.spaceBeforeFunctionParen` | string | `anonymous` | `never`, `always`, `named`, `anonymous`, `asyncArrow` | Choose which functions get a space between the name and the parameter list. |
| `auricFormatter.spaceInParens` | boolean | `false` |  | Print spaces just inside parentheses, as in `foo( a, b )`. |
| `auricFormatter.spreadSpacing` | boolean | `false` |  | Print a space between a spread or rest operator and its argument, as in `... rest`. |
| `auricFormatter.switchCaseBlankLine` | string | `preserve` | `preserve`, `always`, `never` | Choose whether consecutive switch cases are separated by a blank line. |
| `auricFormatter.switchCaseBraceSameLine` | boolean | `true` |  | Keep the opening brace of a braced case body on the case line. |
| `auricFormatter.switchCaseIndent` | boolean | `true` |  | Indent `case` clauses one level inside the switch block. |
| `auricFormatter.taggedTemplateFormat` | string | `auto` | `auto`, `preserve`, `always` | Choose whether the contents of tagged template literals are formatted. |
| `auricFormatter.templateExpressionSpacing` | boolean | `false` |  | Print spaces just inside template literal interpolations, as in `${ value }`. |
| `auricFormatter.templateLiteralIndent` | string | `preserve` | `preserve`, `indent`, `dedent` | Choose whether the interior of a template literal is re-indented. |
| `auricFormatter.ternaryFormat` | string | `indented` | `inline`, `indented`, `aligned`, `nested-flat` | Choose how conditional expressions are laid out when they break. |
| `auricFormatter.yieldParens` | string | `as-needed` | `as-needed`, `always` | Choose when the operand of `yield` is wrapped in parentheses. |

## TypeScript

23 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.abstractMemberBlankLine` | boolean | `false` |  | Separate abstract members from concrete ones with a blank line. |
| `auricFormatter.arrowReturnTypeSpacing` | boolean | `true` |  | Print a space after the colon that introduces a function return type. |
| `auricFormatter.conditionalTypeFormat` | string | `indented` | `indented`, `aligned`, `chain`, `inline` | Choose how conditional types are laid out when they break. |
| `auricFormatter.decoratorPosition` | string | `preserve` | `preserve`, `above`, `inline` | Choose where decorators sit relative to the declaration they decorate. |
| `auricFormatter.decoratorsBeforeExport` | string | `preserve` | `preserve`, `before`, `after` | Choose where decorators sit relative to the `export` keyword. |
| `auricFormatter.enumMemberTrailing` | string | `follow` | `follow`, `all`, `none` | Choose whether a trailing comma follows the last member of an enum. |
| `auricFormatter.genericSpacing` | boolean | `false` |  | Print spaces just inside type argument angle brackets, as in `Array< string >`. |
| `auricFormatter.importTypeStyle` | string | `preserve` | `preserve`, `separate`, `inline` | Choose how type-only import specifiers are grouped. |
| `auricFormatter.indexSignatureSpacing` | string | `none` | `none`, `inside` | Choose the spacing inside index signature brackets. |
| `auricFormatter.intersectionFormat` | string | `auto` | `auto`, `inline`, `expanded` | Choose how intersection types are laid out. |
| `auricFormatter.mappedTypeFormat` | string | `auto` | `auto`, `expanded`, `inline` | Choose how mapped types are laid out. |
| `auricFormatter.parameterDecoratorInline` | boolean | `true` |  | Keep parameter decorators on the same line as the parameter they decorate. |
| `auricFormatter.preserveEnumOneLine` | boolean | `false` |  | Keep a short enum on a single line when the author wrote it that way. |
| `auricFormatter.preserveTypeParens` | boolean | `false` |  | Keep redundant parentheses inside type expressions where the author wrote them. |
| `auricFormatter.readonlyArrayShorthand` | boolean | `false` |  | Print `readonly T[]` in place of `ReadonlyArray<T>` where the two are interchangeable. |
| `auricFormatter.satisfiesOperatorBreak` | string | `auto` | `auto`, `never`, `always` | Choose how a `satisfies` expression breaks when the line is too long. |
| `auricFormatter.typeAnnotationSpacing` | string | `after` | `after`, `before`, `both`, `none` | Choose the spacing around the colon of a type annotation. |
| `auricFormatter.typeCastParens` | boolean | `false` |  | Parenthesise an `as` expression whose position would otherwise make the cast ambiguous to a reader. |
| `auricFormatter.typeLiteralTrailingSeparator` | boolean | `true` |  | Print a trailing separator after the last member of a multi-line object type. |
| `auricFormatter.typeMemberSeparator` | string | `semi` | `semi`, `comma`, `none`, `preserve` | Choose the separator printed between members of an object type. |
| `auricFormatter.typeParameterNewline` | string | `multiline` | `multiline`, `preserve`, `always`, `never` | Choose how type parameter lists are broken across lines. |
| `auricFormatter.unionFormat` | string | `auto` | `auto`, `inline`, `expanded`, `leading-pipe` | Choose how union types are laid out. |
| `auricFormatter.unionLeadingPipeWhenBroken` | boolean | `true` |  | Print a leading pipe on the first member of a union that has been broken across lines. |

## CSS

39 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.atRuleBlankLine` | boolean | `false` |  | Print a blank line before a block at-rule such as @media or @supports. |
| `auricFormatter.atRuleCase` | string | `preserve` | `preserve`, `lower`, `upper` | Choose the letter case of at-rule names. |
| `auricFormatter.blankLineBetweenRules` | integer | `0` | 0–4 | Print exactly this many blank lines between sibling rules, or 0 to leave the author's spacing. |
| `auricFormatter.colorNotation` | string | `preserve` | `preserve`, `hex`, `rgb`, `hsl`, `oklch` | Choose the notation colour values are rewritten into. |
| `auricFormatter.cssTrailingSemicolon` | string | `always` | `always`, `never`, `preserve` | Choose whether the last declaration in a block ends with a semicolon. |
| `auricFormatter.declarationColonSpace` | boolean | `true` |  | Print a space after the colon that separates a property from its value. |
| `auricFormatter.declarationOrder` | string | `preserve` | `preserve`, `alphabetical`, `concentric`, `smacss`, `idiomatic`, `grouped` | Choose the order declarations are printed in inside a rule. |
| `auricFormatter.emptyLineBeforeNested` | boolean | `false` |  | Print a blank line before the first nested rule inside a block. |
| `auricFormatter.emptyRuleStyle` | string | `preserve` | `preserve`, `collapse`, `remove` | Choose what happens to rules with no declarations. |
| `auricFormatter.functionArgSpacing` | boolean | `false` |  | Print spaces just inside the parentheses of CSS functions, as in `rgb( 1, 2, 3 )`. |
| `auricFormatter.gridTemplateAlign` | boolean | `true` |  | Keep each row of a multi-line grid-template-areas value on its own line and align the columns. |
| `auricFormatter.hexShorthand` | string | `preserve` | `preserve`, `short`, `long` | Choose whether hex colours are written in their short or long form. |
| `auricFormatter.importantSpacing` | string | `before` | `before`, `none`, `both` | Choose the spacing around an !important flag. |
| `auricFormatter.keyframeSelectorCase` | string | `preserve` | `preserve`, `lower`, `upper` | Choose the letter case of keyframe selectors. |
| `auricFormatter.leadingZero` | string | `always` | `always`, `never`, `preserve` | Choose whether decimals below one carry a leading zero. |
| `auricFormatter.lessGuardFormat` | string | `preserve` | `preserve`, `expanded`, `compact` | Choose how Less mixin guard clauses are laid out. |
| `auricFormatter.lessMixinSeparator` | string | `preserve` | `preserve`, `semicolon`, `comma` | Choose the separator printed between Less mixin arguments. |
| `auricFormatter.mathOperatorSpacing` | boolean | `true` |  | Print spaces around the operators inside calc() and preprocessor arithmetic. |
| `auricFormatter.mediaQueryFormat` | string | `preserve` | `preserve`, `compact`, `expanded` | Choose how media query feature lists are laid out. |
| `auricFormatter.nestedRuleBlankLine` | boolean | `false` |  | Print a blank line before a nested rule that follows a declaration. |
| `auricFormatter.preserveCustomPropertyValues` | boolean | `true` |  | Print the value of a custom property exactly as written, since it may be an arbitrary token stream. |
| `auricFormatter.propertyCase` | string | `preserve` | `preserve`, `lower`, `upper` | Choose the letter case of property names. |
| `auricFormatter.propertyValueAlign` | boolean | `false` |  | Align the values of consecutive declarations into a column. |
| `auricFormatter.quotesInUrl` | string | `preserve` | `preserve`, `always`, `never` | Choose whether url() arguments are quoted. |
| `auricFormatter.scssIncludeParens` | string | `preserve` | `preserve`, `always`, `never` | Choose whether an argument-free @include keeps its parentheses. |
| `auricFormatter.scssMapFormat` | string | `preserve` | `preserve`, `expanded`, `compact` | Choose how SCSS maps are laid out. |
| `auricFormatter.scssOperatorSpacing` | boolean | `true` |  | Print spaces around SCSS comparison and arithmetic operators inside @if and @while. |
| `auricFormatter.selectorAttributeQuotes` | string | `always` | `always`, `preserve`, `never` | Choose whether attribute selector values are quoted. |
| `auricFormatter.selectorCase` | string | `preserve` | `preserve`, `lower`, `upper` | Choose the letter case of type selectors and pseudo-class names. |
| `auricFormatter.selectorCombinatorSpacing` | string | `spaced` | `spaced`, `tight`, `preserve` | Choose the spacing around child, sibling and descendant combinators. |
| `auricFormatter.selectorSeparator` | string | `newline` | `newline`, `space`, `preserve` | Choose how the selectors of a selector list are separated. |
| `auricFormatter.shorthandExpansion` | string | `preserve` | `preserve`, `collapse`, `expand` | Choose whether shorthand properties are expanded or collapsed. |
| `auricFormatter.singleLineRuleThreshold` | integer | `0` | 0–32 | Print a rule on one line when it holds at most this many declarations, or 0 to always break. |
| `auricFormatter.singleQuoteCss` | boolean | `false` |  | Prefer single quotes over double quotes in stylesheets. |
| `auricFormatter.trailingZero` | string | `never` | `never`, `preserve` | Choose whether trailing zeros in numbers are trimmed. |
| `auricFormatter.unitCase` | string | `preserve` | `preserve`, `lower`, `upper` | Choose the letter case of units. |
| `auricFormatter.valueKeywordCase` | string | `preserve` | `preserve`, `lower`, `upper` | Choose the letter case of keyword values. |
| `auricFormatter.vendorPrefixAlign` | boolean | `false` |  | Align a run of vendor-prefixed variants of the same property into a column. |
| `auricFormatter.zeroUnits` | string | `preserve` | `preserve`, `strip`, `keep` | Choose whether zero values keep their unit. |

## HTML

29 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.htmlAttributeCase` | string | `preserve` | `preserve`, `lower`, `upper` | Choose the letter case of attribute names. |
| `auricFormatter.htmlAttributeOrder` | array | `[]` |  | List attribute names or glob patterns in the order they should be printed when sorting is on. |
| `auricFormatter.htmlAttributeWrap` | string | `auto` | `auto`, `preserve`, `always`, `never` | Choose when a tag's attribute list is broken across lines. |
| `auricFormatter.htmlBlankLineBetweenBlocks` | integer | `0` | 0–4 | Print exactly this many blank lines between sibling block elements, or 0 to leave the author's spacing. |
| `auricFormatter.htmlBooleanAttributeStyle` | string | `preserve` | `preserve`, `bare`, `explicit` | Choose how boolean attributes are printed. |
| `auricFormatter.htmlClassAttributeWrap` | boolean | `false` |  | Break a long class attribute into one class name per line. |
| `auricFormatter.htmlDoctypeCase` | string | `lower` | `lower`, `upper`, `preserve` | Choose the letter case of the doctype declaration. |
| `auricFormatter.htmlEntityStyle` | string | `preserve` | `preserve`, `named`, `numeric`, `minimal` | Choose how character entities are printed. |
| `auricFormatter.htmlIndentInlineElements` | boolean | `false` |  | Indent the children of inline elements the way block elements are indented. |
| `auricFormatter.htmlMinifyWhitespace` | boolean | `false` |  | Collapse every run of insignificant whitespace between elements to nothing. |
| `auricFormatter.htmlPreserveTags` | array | `["pre","textarea","listing","plaintext"]` |  | List tags whose contents are copied through untouched because their whitespace is significant. |
| `auricFormatter.htmlQuoteAttributes` | string | `double` | `double`, `single`, `preserve`, `as-needed` | Choose how attribute values are quoted. |
| `auricFormatter.htmlScriptIndent` | string | `indent` | `indent`, `flush`, `preserve` | Choose how the contents of a `<script>` block are indented. |
| `auricFormatter.htmlSelfClosing` | string | `preserve` | `preserve`, `always`, `never` | Choose whether childless elements are printed self-closed. |
| `auricFormatter.htmlSortAttributes` | boolean | `false` |  | Sort attributes using htmlAttributeOrder, then alphabetically for anything left over. |
| `auricFormatter.htmlSrcsetWrap` | boolean | `true` |  | Break a long srcset or sizes attribute after each comma. |
| `auricFormatter.htmlStyleIndent` | string | `indent` | `indent`, `flush`, `preserve` | Choose how the contents of a `<style>` block are indented. |
| `auricFormatter.htmlTagCase` | string | `lower` | `preserve`, `lower`, `upper` | Choose the letter case of tag names. |
| `auricFormatter.htmlVoidElementSlash` | boolean | `true` |  | Print the trailing slash on void elements, as in `<br />`. |
| `auricFormatter.htmlWrapText` | boolean | `true` |  | Reflow text nodes so that they fit within the print width. |
| `auricFormatter.svgAttributeOrder` | array | `[]` |  | List SVG attribute names in the order they should be printed when attribute sorting is on. |
| `auricFormatter.svgPathPrecision` | integer | `0` | 0–12 | Round the numbers inside an SVG path to this many decimal places, or 0 to leave them untouched. |
| `auricFormatter.svgPathWrap` | string | `preserve` | `preserve`, `command`, `never` | Choose how SVG path data is wrapped. |
| `auricFormatter.xmlDeclarationQuotes` | string | `double` | `double`, `single`, `preserve` | Choose how the values in the XML declaration are quoted. |
| `auricFormatter.xmlIndentAttributes` | boolean | `true` |  | Indent a broken attribute list one level under its tag name. |
| `auricFormatter.xmlPreserveCdata` | boolean | `true` |  | Copy CDATA sections through byte for byte. |
| `auricFormatter.xmlSelfClosingSpace` | boolean | `true` |  | Print a space before the slash of a self-closing XML tag. |
| `auricFormatter.xmlSortAttributes` | boolean | `false` |  | Sort XML attributes alphabetically, leaving namespace declarations first. |
| `auricFormatter.xmlWhitespaceSensitivity` | string | `strict` | `strict`, `ignore`, `preserve-mixed` | Choose how strictly whitespace inside XML elements is preserved. |

## Markdown

32 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.mdBlockquoteBlankLineMarker` | boolean | `true` |  | Print a lone marker on the blank lines inside a blockquote so the quote stays visually joined. |
| `auricFormatter.mdBlockquoteMarker` | string | `spaced` | `spaced`, `tight`, `preserve` | Choose the spacing after a blockquote marker. |
| `auricFormatter.mdBulletAlternate` | boolean | `false` |  | Alternate the bullet character at each nesting level so that levels are visually distinct. |
| `auricFormatter.mdBulletMarker` | string | `dash` | `dash`, `asterisk`, `plus`, `preserve` | Choose the character used for unordered list bullets. |
| `auricFormatter.mdCodeFence` | string | `backtick` | `backtick`, `tilde`, `preserve` | Choose the character used to fence code blocks. |
| `auricFormatter.mdCodeFenceLength` | integer | `3` | 3–10 | Print code fences with at least this many characters, lengthening them further when the content demands it. |
| `auricFormatter.mdEmphasisMarker` | string | `underscore` | `asterisk`, `underscore`, `preserve` | Choose the character used for emphasis. |
| `auricFormatter.mdEscapeSpecial` | boolean | `true` |  | Escape characters in text that would otherwise be read as markup. |
| `auricFormatter.mdFormatCodeBlocks` | boolean | `true` |  | Format the contents of fenced code blocks whose info string names a language Auric supports. |
| `auricFormatter.mdFrontmatterFormat` | string | `format` | `format`, `preserve` | Choose whether document frontmatter is formatted. |
| `auricFormatter.mdHeadingBlankLines` | integer | `1` | 0–3 | Print exactly this many blank lines before a heading that follows other content. |
| `auricFormatter.mdHeadingClosingHashes` | boolean | `false` |  | Print a matching run of hashes at the end of an ATX heading. |
| `auricFormatter.mdHeadingStyle` | string | `atx` | `atx`, `setext`, `preserve` | Choose the heading style. |
| `auricFormatter.mdHtmlBlockFormat` | string | `preserve` | `preserve`, `format` | Choose whether raw HTML blocks inside Markdown are formatted. |
| `auricFormatter.mdLineBreakStyle` | string | `preserve` | `preserve`, `backslash`, `spaces` | Choose how hard line breaks inside a paragraph are written. |
| `auricFormatter.mdLinkStyle` | string | `preserve` | `preserve`, `inline`, `reference` | Choose whether links are printed inline or as references. |
| `auricFormatter.mdListIndent` | string | `aligned` | `aligned`, `one`, `tab`, `preserve` | Choose how the continuation lines of a list item are indented. |
| `auricFormatter.mdListItemBlankLine` | string | `preserve` | `preserve`, `loose`, `tight` | Choose whether list items are separated by blank lines. |
| `auricFormatter.mdMaxHeadingLevel` | integer | `0` | 0–6 | Warn when a heading is nested deeper than this level, or 0 to allow any depth. |
| `auricFormatter.mdNumberedListAlign` | boolean | `true` |  | Right-align the numbers of an ordered list that reaches double digits. |
| `auricFormatter.mdOrderedMarker` | string | `period` | `period`, `paren`, `preserve` | Choose the delimiter that follows an ordered list number. |
| `auricFormatter.mdOrderedNumbering` | string | `preserve` | `preserve`, `one`, `ordinal` | Choose how ordered list items are numbered. |
| `auricFormatter.mdReferencePlacement` | string | `preserve` | `preserve`, `end`, `section` | Choose where link reference definitions are placed. |
| `auricFormatter.mdSetextUnderlineFull` | boolean | `true` |  | Extend a setext heading underline to the full width of the heading text. |
| `auricFormatter.mdStrongMarker` | string | `asterisk` | `asterisk`, `underscore`, `preserve` | Choose the character used for strong emphasis. |
| `auricFormatter.mdTableAlign` | boolean | `true` |  | Pad table cells so that every pipe lines up into a column. |
| `auricFormatter.mdTableCompact` | boolean | `false` |  | Collapse table alignment when the table would otherwise exceed the print width. |
| `auricFormatter.mdTableMinCellWidth` | integer | `3` | 1–40 | Pad every aligned table cell to at least this many characters. |
| `auricFormatter.mdTablePadding` | boolean | `true` |  | Print one space of padding inside each table cell's pipes. |
| `auricFormatter.mdThematicBreak` | string | `dashes` | `dashes`, `asterisks`, `underscores`, `preserve` | Choose how thematic breaks are printed. |
| `auricFormatter.mdTocGenerate` | boolean | `false` |  | Rebuild the table of contents between the auric-toc markers from the document's headings. |
| `auricFormatter.mdTocMaxDepth` | integer | `3` | 1–6 | Include headings down to this level when rebuilding a table of contents. |

## YAML

15 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.yamlAlignValues` | boolean | `false` |  | Align the values of consecutive mapping entries into a column. |
| `auricFormatter.yamlAnchorFormat` | string | `preserve` | `preserve`, `inline`, `above` | Choose where anchors are printed relative to the value they name. |
| `auricFormatter.yamlBlankLineBetweenTopLevelKeys` | integer | `0` | 0–4 | Print exactly this many blank lines between top-level keys, or 0 to leave the author's spacing. |
| `auricFormatter.yamlBooleanStyle` | string | `preserve` | `preserve`, `true-false`, `yes-no`, `on-off` | Choose how boolean values are written. |
| `auricFormatter.yamlBracketSpacing` | boolean | `true` |  | Print spaces just inside the braces of flow mappings, as in `{ a: 1 }`. |
| `auricFormatter.yamlCommentIndent` | string | `align` | `align`, `preserve`, `flush` | Choose how standalone comments are indented. |
| `auricFormatter.yamlDocumentSeparator` | string | `preserve` | `preserve`, `always`, `never` | Choose whether documents are introduced by a triple-dash separator. |
| `auricFormatter.yamlExplicitKeys` | boolean | `false` |  | Write complex mapping keys with the explicit question-mark form. |
| `auricFormatter.yamlFlowCollectionWidth` | integer | `0` | 0–1000 | Break a flow collection into block form once it would exceed this many columns, or 0 to follow the print width. |
| `auricFormatter.yamlIndent` | integer | `2` | 1–12 | Indent each nested mapping level by this many spaces. |
| `auricFormatter.yamlKeySort` | boolean | `false` |  | Sort mapping keys alphabetically, which is safe because YAML mappings are unordered. |
| `auricFormatter.yamlNullStyle` | string | `preserve` | `preserve`, `empty`, `tilde`, `null` | Choose how null values are written. |
| `auricFormatter.yamlPreserveBlockScalars` | boolean | `true` |  | Copy the body of a literal or folded block scalar through byte for byte. |
| `auricFormatter.yamlQuoteStyle` | string | `preserve` | `preserve`, `single`, `double`, `minimal` | Choose how scalar values are quoted. |
| `auricFormatter.yamlSequenceIndent` | string | `indented` | `indented`, `flush`, `preserve` | Choose how sequence items are indented under their parent key. |

## JSON

22 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.iniAlignValues` | boolean | `false` |  | Align the values of consecutive properties into a column. |
| `auricFormatter.iniKeyCase` | string | `preserve` | `preserve`, `lower`, `upper` | Choose the letter case of property names. |
| `auricFormatter.iniSectionBlankLine` | integer | `1` | 0–4 | Print exactly this many blank lines before a section header, or 0 to leave the author's spacing. |
| `auricFormatter.iniSpaceAroundEquals` | boolean | `true` |  | Print a space on each side of the equals sign. |
| `auricFormatter.jsonBracketSpacing` | boolean | `true` |  | Print spaces just inside the braces of a single-line object. |
| `auricFormatter.jsonEmptyCollectionStyle` | string | `collapse` | `collapse`, `preserve` | Choose how empty objects and arrays are printed. |
| `auricFormatter.jsonEscapeUnicode` | boolean | `false` |  | Escape every non-ASCII character in strings as a \u sequence. |
| `auricFormatter.jsonExpandArrayThreshold` | integer | `0` | 0–100 | Break an array onto multiple lines once it holds at least this many elements, or 0 to decide by width alone. |
| `auricFormatter.jsonNormalizeNumbers` | boolean | `false` |  | Rewrite numbers into their shortest round-trip form. |
| `auricFormatter.jsonPackageJsonOrder` | boolean | `false` |  | Print the well-known top-level keys of a package.json in their conventional order. |
| `auricFormatter.jsonPreserveComments` | boolean | `true` |  | Keep comments in JSON dialects that permit them and refuse to format the file if they cannot be placed. |
| `auricFormatter.jsonQuoteKeys` | string | `preserve` | `preserve`, `always`, `as-needed` | Choose whether object keys are quoted. |
| `auricFormatter.jsonSingleLineArrays` | boolean | `false` |  | Keep arrays of primitives on one line whenever they fit. |
| `auricFormatter.jsonSortKeys` | boolean | `false` |  | Sort object keys alphabetically throughout the document. |
| `auricFormatter.jsonTrailingComma` | string | `none` | `none`, `all`, `preserve` | Choose whether broken arrays and objects end with a trailing comma. |
| `auricFormatter.tomlAlignValues` | boolean | `false` |  | Align the values of consecutive key-value pairs into a column. |
| `auricFormatter.tomlArrayWrap` | string | `auto` | `auto`, `always`, `never`, `preserve` | Choose how TOML arrays are wrapped. |
| `auricFormatter.tomlIndentTables` | boolean | `false` |  | Indent the body of a table one level under its header. |
| `auricFormatter.tomlInlineTableSpacing` | boolean | `true` |  | Print spaces just inside the braces of an inline table. |
| `auricFormatter.tomlKeyQuoting` | string | `as-needed` | `as-needed`, `always`, `preserve` | Choose whether TOML keys are quoted. |
| `auricFormatter.tomlSortKeys` | boolean | `false` |  | Sort the keys inside each table alphabetically. |
| `auricFormatter.tomlTableBlankLine` | integer | `1` | 0–4 | Print exactly this many blank lines before a table header, or 0 to leave the author's spacing. |

## GraphQL

8 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.graphqlArgumentWrap` | string | `auto` | `auto`, `always`, `never` | Choose how field and directive argument lists are wrapped. |
| `auricFormatter.graphqlBracketSpacing` | boolean | `true` |  | Print spaces just inside the braces of an inline object value. |
| `auricFormatter.graphqlCommaSeparators` | string | `remove` | `remove`, `preserve` | Choose whether GraphQL's optional commas are printed. |
| `auricFormatter.graphqlDescriptionStyle` | string | `preserve` | `preserve`, `block`, `inline` | Choose how schema descriptions are quoted. |
| `auricFormatter.graphqlFieldAlign` | boolean | `false` |  | Align the types of consecutive field definitions into a column. |
| `auricFormatter.graphqlSeparateOperations` | integer | `1` | 0–4 | Print exactly this many blank lines between top-level definitions. |
| `auricFormatter.graphqlSortDefinitions` | boolean | `false` |  | Sort top-level definitions by kind and then by name. |
| `auricFormatter.graphqlSortFields` | boolean | `false` |  | Sort the fields of a type definition alphabetically. |

## Universal

39 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.cPointerAlignment` | string | `preserve` | `preserve`, `left`, `right`, `middle` | Choose where the star of a pointer declaration sits. |
| `auricFormatter.dockerfileInstructionCase` | string | `upper` | `preserve`, `lower`, `upper` | Choose the letter case of Dockerfile instructions. |
| `auricFormatter.goAlignComments` | boolean | `true` |  | Align the trailing comments of a const or var block into a column, the way gofmt does. |
| `auricFormatter.goAlignStructTags` | boolean | `true` |  | Align the field names, types and struct tags of a struct definition into columns. |
| `auricFormatter.javaAnnotationPosition` | string | `above` | `above`, `inline`, `preserve` | Choose where Java-family annotations are printed. |
| `auricFormatter.makefileTabGuard` | boolean | `true` |  | Refuse to convert the leading tab of a recipe line to spaces, because make requires it. |
| `auricFormatter.pythonAlignDictValues` | boolean | `false` |  | Align the values of a multi-line dictionary literal into a column. |
| `auricFormatter.pythonBlankLinesNested` | integer | `1` | 0–4 | Separate methods and nested functions with exactly this many blank lines. |
| `auricFormatter.pythonBlankLinesTopLevel` | integer | `2` | 0–4 | Separate top-level classes and functions with exactly this many blank lines. |
| `auricFormatter.rustAlignMatchArms` | boolean | `false` |  | Align the fat arrows of a match block into a column. |
| `auricFormatter.rustAlignStructFields` | boolean | `false` |  | Align the types of consecutive struct fields into a column. |
| `auricFormatter.shellFunctionKeyword` | boolean | `false` |  | Print the optional `function` keyword before shell function definitions. |
| `auricFormatter.shellIndentCase` | boolean | `true` |  | Indent the patterns of a case statement one level inside the case block. |
| `auricFormatter.shellRedirectSpacing` | boolean | `false` |  | Print a space between a redirection operator and its target. |
| `auricFormatter.sqlAlignSelectColumns` | boolean | `false` |  | Align the aliases of a select list into a column. |
| `auricFormatter.sqlCommaPosition` | string | `trailing` | `trailing`, `leading`, `preserve` | Choose whether the commas of a broken list lead or trail. |
| `auricFormatter.sqlIdentifierCase` | string | `preserve` | `preserve`, `lower`, `upper` | Choose the letter case of unquoted identifiers. |
| `auricFormatter.sqlIndentJoins` | boolean | `true` |  | Indent join clauses one level under the FROM clause they belong to. |
| `auricFormatter.sqlIndentSubqueries` | boolean | `true` |  | Indent the body of a subquery one level inside its parentheses. |
| `auricFormatter.sqlKeywordCase` | string | `upper` | `preserve`, `lower`, `upper` | Choose the letter case of SQL keywords. |
| `auricFormatter.universalAlignAssignments` | boolean | `false` |  | Align the equals signs of a consecutive run of assignments into a column. |
| `auricFormatter.universalAlignConsecutive` | boolean | `false` |  | Align consecutive declarations, struct fields and case arms that share a shape. |
| `auricFormatter.universalAlignTrailingComments` | boolean | `false` |  | Align the trailing comments of a consecutive run of lines into a column. |
| `auricFormatter.universalAttributeIndent` | string | `preserve` | `preserve`, `above`, `inline` | Choose where attributes and annotations are printed relative to their target. |
| `auricFormatter.universalBraceStyle` | string | `preserve` | `preserve`, `same-line`, `next-line`, `next-line-indented` | Choose where the opening brace of a block is placed. |
| `auricFormatter.universalCaseIndent` | boolean | `true` |  | Indent case labels one level inside the switch or match block that owns them. |
| `auricFormatter.universalContinuationIndent` | integer | `0` | 0–24 | Indent the continuation lines of a wrapped statement by this many columns, or 0 to use one full level. |
| `auricFormatter.universalHangingIndent` | boolean | `true` |  | Align a wrapped argument list under the opening bracket that introduced it. |
| `auricFormatter.universalIndentSize` | integer | `0` | 0–24 | Indent universal-engine languages by this many columns, or 0 to follow tabWidth. |
| `auricFormatter.universalKeywordCase` | string | `preserve` | `preserve`, `lower`, `upper` | Choose the letter case of language keywords. |
| `auricFormatter.universalLabelIndent` | string | `preserve` | `preserve`, `dedent`, `flush` | Choose how goto labels and their equivalents are indented. |
| `auricFormatter.universalMaxBlankLines` | integer | `0` | 0–8 | Collapse runs of blank lines to this many, or 0 to follow maxBlankLines. |
| `auricFormatter.universalNormalizeCommaSpacing` | boolean | `true` |  | Print no space before a comma and exactly one after it. |
| `auricFormatter.universalNormalizeOperatorSpacing` | boolean | `true` |  | Print exactly one space on each side of a binary operator. |
| `auricFormatter.universalNormalizeParenSpacing` | boolean | `true` |  | Remove the padding just inside parentheses and brackets. |
| `auricFormatter.universalNormalizeSemicolonSpacing` | boolean | `true` |  | Print no space before a semicolon and exactly one after it when it separates rather than terminates. |
| `auricFormatter.universalPreserveAlignmentBlocks` | boolean | `true` |  | Keep a hand-aligned run of lines intact when its columns already line up. |
| `auricFormatter.universalPreserveShebang` | boolean | `true` |  | Keep a shebang line flush with the left margin and free of reformatting. |
| `auricFormatter.universalTrimBlockEdges` | boolean | `true` |  | Remove blank lines immediately inside an opening or closing brace. |

## Alignment

15 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.alignAssignments` | string | `off` | `off`, `consecutive`, `block` | Choose how the equals signs of neighbouring assignments are aligned. |
| `auricFormatter.alignConsecutiveDeclarations` | boolean | `false` |  | Align the names of consecutive variable declarations into a column. |
| `auricFormatter.alignEnumValues` | boolean | `false` |  | Align the initialisers of consecutive enum members into a column. |
| `auricFormatter.alignImportSpecifiers` | boolean | `false` |  | Align the `from` keyword of consecutive import statements into a column. |
| `auricFormatter.alignObjectValues` | boolean | `false` |  | Align the values of consecutive object properties into a column. |
| `auricFormatter.alignTernaryBranches` | boolean | `false` |  | Align the question mark and colon of a broken conditional expression into a column. |
| `auricFormatter.alignTrailingComments` | boolean | `false` |  | Align the trailing comments of consecutive lines into a column. |
| `auricFormatter.alignTrailingCommentsMaxColumn` | integer | `0` | 0–1000 | Give up aligning a trailing comment that would start past this column, or 0 to use the print width. |
| `auricFormatter.alignTrailingCommentsMinSpaces` | integer | `1` | 1–8 | Leave at least this many spaces between code and an aligned trailing comment. |
| `auricFormatter.alignTypeMembers` | boolean | `false` |  | Align the types of consecutive members of an object type into a column. |
| `auricFormatter.alignmentBreakOnBlankLine` | boolean | `true` |  | End an alignment group at a blank line, so that separate paragraphs align separately. |
| `auricFormatter.alignmentBreakOnComment` | boolean | `false` |  | End an alignment group at a standalone comment. |
| `auricFormatter.alignmentMaxPadding` | integer | `24` | 1–200 | Abandon an alignment that would need more than this many spaces of padding on any line. |
| `auricFormatter.alignmentMinGroupSize` | integer | `2` | 2–20 | Align a group only once it contains at least this many lines. |
| `auricFormatter.alignmentUseSpacesOnly` | boolean | `true` |  | Pad alignment with spaces even when the file is indented with tabs, so columns survive any tab width. |

## Sorting

19 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.classMemberOrder` | array | see note |  | List the class member kinds in the order they should be printed when class sorting is on. |
| `auricFormatter.exportOrder` | string | `preserve` | `preserve`, `alphabetical`, `grouped` | Choose the order of export declarations. |
| `auricFormatter.importOrder` | array | `[]` |  | List regular expressions describing the import groups, in the order those groups should appear. |
| `auricFormatter.importOrderCaseInsensitive` | boolean | `false` |  | Ignore letter case when sorting import paths. |
| `auricFormatter.importOrderGroupNamespaceSpecifiers` | boolean | `false` |  | Put namespace imports at the top of their group. |
| `auricFormatter.importOrderSeparation` | boolean | `false` |  | Separate the import groups with a blank line. |
| `auricFormatter.importOrderSideEffectsFirst` | boolean | `true` |  | Keep side-effect-only imports at the top and never move them past another import. |
| `auricFormatter.importOrderSortSpecifiers` | boolean | `false` |  | Sort the named specifiers inside each import statement. |
| `auricFormatter.importOrderTypeImports` | string | `preserve` | `preserve`, `first`, `last`, `separate` | Choose where type-only imports are sorted. |
| `auricFormatter.sortCaseSensitivity` | string | `insensitive` | `insensitive`, `sensitive` | Choose how letter case is treated when sorting names. |
| `auricFormatter.sortClassMembers` | boolean | `false` |  | Sort class members into the groups named by classMemberOrder. |
| `auricFormatter.sortIgnorePrefix` | string | empty |  | Strip this leading prefix from a name before comparing it, so decorated names sort with their plain neighbours. |
| `auricFormatter.sortImports` | boolean | `false` |  | Sort import declarations into the groups named by importOrder. |
| `auricFormatter.sortInterfaceMembers` | boolean | `false` |  | Sort the members of an interface or object type alphabetically. |
| `auricFormatter.sortNaturalNumeric` | boolean | `true` |  | Compare digit runs inside names numerically so that item2 sorts before item10. |
| `auricFormatter.sortObjectKeys` | boolean | `false` |  | Sort the keys of object literals that carry a sort-keys comment directive. |
| `auricFormatter.sortPreserveComments` | boolean | `true` |  | Carry each entry's leading and trailing comments with it when it moves. |
| `auricFormatter.sortRespectBlankLineGroups` | boolean | `true` |  | Treat a blank line as a group boundary and sort only inside each group. |
| `auricFormatter.sortUnionMembers` | boolean | `false` |  | Sort the members of a union type, keeping null and undefined last. |

Notes and language-specific defaults:

- `auricFormatter.classMemberOrder` default: `["static-field","field","constructor","static-method","method","getter","setter"]`

## Comments

18 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.bannerComment` | string | empty |  | Ensure the file starts with this comment text, inserting it when it is missing. |
| `auricFormatter.blankLineAfterComment` | string | `preserve` | `preserve`, `always`, `never` | Choose whether standalone comment blocks are followed by a blank line. |
| `auricFormatter.blankLineBeforeComment` | string | `preserve` | `preserve`, `always`, `never` | Choose whether standalone comments are preceded by a blank line. |
| `auricFormatter.blockCommentStarAlign` | boolean | `true` |  | Align the leading stars of a block comment one column in from the opening slash. |
| `auricFormatter.blockCommentStarPad` | boolean | `false` |  | Print a space after each leading star of a block comment. |
| `auricFormatter.commentAttachment` | string | `smart` | `smart`, `preserve` | Choose how comments are attached to the syntax around them. |
| `auricFormatter.commentIgnorePattern` | string | empty |  | Copy through untouched any comment whose text matches this regular expression. |
| `auricFormatter.commentSpacing` | string | `preserve` | `preserve`, `always`, `never` | Choose the spacing between a line comment marker and its text. |
| `auricFormatter.commentWrap` | string | `preserve` | `preserve`, `always`, `never` | Choose whether comment text is reflowed. |
| `auricFormatter.commentWrapWidth` | integer | `0` | 0–1000 | Wrap comment text at this column, or 0 to use the print width. |
| `auricFormatter.footerComment` | string | empty |  | Ensure the file ends with this comment text, inserting it when it is missing. |
| `auricFormatter.jsdocAlign` | boolean | `false` |  | Align the type, name and description columns of a documentation block's tags. |
| `auricFormatter.jsdocBlankLineAfterDescription` | boolean | `false` |  | Separate a documentation block's description from its first tag with a blank line. |
| `auricFormatter.jsdocDescriptionIndent` | integer | `0` | 0–24 | Indent the wrapped continuation of a tag description by this many extra columns. |
| `auricFormatter.jsdocNormalizeTags` | boolean | `false` |  | Rewrite documentation tag aliases to their canonical spelling, turning @return into @returns. |
| `auricFormatter.jsdocTagOrder` | array | `[]` |  | List documentation tags in the order they should be printed, with unlisted tags keeping their relative order at the end. |
| `auricFormatter.jsdocWrap` | string | `preserve` | `preserve`, `always`, `never` | Choose whether documentation block descriptions are reflowed. |
| `auricFormatter.preserveBannerComment` | boolean | `true` |  | Keep the leading comment block of a file flush with the top and free of reflowing, so licence headers survive. |

## Blank Lines

15 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.blankLineAfterDirectives` | boolean | `false` |  | Print a blank line after the directive prologue of a file or function. |
| `auricFormatter.blankLineAfterImports` | string | `preserve` | `preserve`, `always`, `never` | Choose whether a blank line follows the import block. |
| `auricFormatter.blankLineBeforeControlFlow` | string | `preserve` | `preserve`, `always`, `never` | Choose whether if, for, while and switch statements are preceded by a blank line. |
| `auricFormatter.blankLineBeforeExport` | string | `preserve` | `preserve`, `always`, `never` | Choose whether an export declaration is preceded by a blank line. |
| `auricFormatter.blankLineBeforeReturn` | string | `preserve` | `preserve`, `always`, `never` | Choose whether a return statement is preceded by a blank line. |
| `auricFormatter.blankLineBetweenMethods` | string | `preserve` | `preserve`, `always`, `never` | Choose whether class members are separated by a blank line. |
| `auricFormatter.blankLineBetweenTopLevel` | string | `preserve` | `preserve`, `always`, `never` | Choose whether top-level declarations are separated by a blank line. |
| `auricFormatter.collapseEmptyBlockBlankLines` | boolean | `true` |  | Remove the blank lines from a block that contains nothing else. |
| `auricFormatter.maxBlankLines` | integer | `1` | 0–8 | Collapse any run of blank lines to at most this many. |
| `auricFormatter.maxBlankLinesAtEnd` | integer | `0` | 0–8 | Allow at most this many blank lines at the very end of a file. |
| `auricFormatter.maxBlankLinesAtStart` | integer | `0` | 0–8 | Allow at most this many blank lines at the very top of a file. |
| `auricFormatter.maxBlankLinesInsideBlocks` | integer | `1` | 0–8 | Collapse any run of blank lines inside a block or function body to at most this many. |
| `auricFormatter.padBlocks` | boolean | `false` |  | Print a blank line just inside the braces of every block. |
| `auricFormatter.padClassBody` | boolean | `false` |  | Print a blank line just inside the opening and closing braces of a class body. |
| `auricFormatter.padFunctionBody` | boolean | `false` |  | Print a blank line just inside the opening and closing braces of a function body. |

Notes and language-specific defaults:

- `auricFormatter.maxBlankLines`: `2` for python.

## Safety

12 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.formatMinified` | boolean | `false` |  | Format files that look minified, instead of leaving them alone. |
| `auricFormatter.maxFileSizeKb` | integer | `4096` | 0–1048576 | Refuse to format a file larger than this many kilobytes, or 0 to lift the limit. |
| `auricFormatter.parseTimeoutMs` | integer | `5000` | 0–600000 | Abandon a parse that has run for this many milliseconds, or 0 to wait indefinitely. |
| `auricFormatter.safetyCommentPreservation` | boolean | `true` |  | Require every comment body in the input to appear in the output. |
| `auricFormatter.safetyIdempotency` | boolean | `false` |  | Format the output a second time and require the two results to be identical. |
| `auricFormatter.safetyIdempotencyPasses` | integer | `1` | 1–8 | Run this many extra formatting passes when the idempotency check is on. |
| `auricFormatter.safetyNumericLiterals` | boolean | `true` |  | Require every numeric literal to keep its value through any rewriting of its spelling. |
| `auricFormatter.safetyOnFailure` | string | `preserve` | `preserve`, `warn`, `throw` | Choose what happens when a safety check fails. |
| `auricFormatter.safetyReparse` | boolean | `true` |  | Re-parse the output with the same parser and require it to succeed. |
| `auricFormatter.safetyStringLiterals` | boolean | `true` |  | Require the multiset of string and template literal contents to be identical before and after. |
| `auricFormatter.safetyTokenCheck` | boolean | `true` |  | Re-lex the output and require the significant token stream to match the input exactly. |
| `auricFormatter.safetyTokenCheckComments` | boolean | `true` |  | Include comment tokens in the token comparison. |

## Experimental

9 options.

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.experimentalCommentReflow` | boolean | `false` |  | Experimental. Reflow comment prose with the Markdown paragraph engine, preserving lists and code spans. |
| `auricFormatter.experimentalDiffMinimization` | boolean | `false` |  | Experimental. Prefer the layout closest to the input whenever two layouts are equally valid. |
| `auricFormatter.experimentalIncrementalCache` | boolean | `false` |  | Experimental. Reuse printed fragments for subtrees whose text has not changed since the previous run. |
| `auricFormatter.experimentalJsxTextFill` | boolean | `false` |  | Experimental. Fill JSX text as prose so that words repack rather than each child taking a line. |
| `auricFormatter.experimentalMarkdownTableWrap` | boolean | `false` |  | Experimental. Wrap the contents of an over-wide Markdown table cell instead of letting the row overflow. |
| `auricFormatter.experimentalOperatorPosition` | string | `end` | `end`, `start` | Experimental. Choose which side of a line break a binary operator lands on. |
| `auricFormatter.experimentalPreserveSemanticBlocks` | boolean | `false` |  | Experimental. Treat a blank-line separated run of statements as a paragraph and keep it intact when breaking. |
| `auricFormatter.experimentalTernaries` | boolean | `false` |  | Experimental. Use the indented case-and-result layout for nested conditional expressions. |
| `auricFormatter.experimentalWidthAwareChains` | boolean | `false` |  | Experimental. Choose member chain layout by measuring every candidate rather than by counting links. |
