---
title: Auric Code Health — Categories and signatures
description: The seven code-health categories and every signature Auric Code Health detects, with the languages it checks and its confidence.
product: VS Code extensions › Auric Artisan Studio › Auric Code Health
updated: 2026-09-25
---

# Categories and signatures

Auric Code Health groups its checks into seven **categories**. Within each, a **signature** is one specific detector with a stable ID, such as `ch-secret-github-token`. The ID stays the same when the wording of a message improves, so records, baselines and suppression comments keep working. Every finding also records the detector version (1.2.0 in the current package).

## The seven categories

| Category | ID | Problems severity | Hover severity | Score weight | Setting |
| --- | --- | --- | --- | --- | --- |
| Possible secrets | `secret` | Warning | Critical | 14 | `codeHealth.secret` |
| Security risks | `security` | Warning | Serious | 12 | `codeHealth.security` |
| Merge markers | `conflict` | Error | Critical | 10 | `codeHealth.conflict` |
| Risky APIs | `risk` | Warning | Serious | 4 | `codeHealth.risk` |
| Debug leftovers | `debug` | Information | Minor | 2 | `codeHealth.debug` |
| Task markers | `todo` | Hint | Minor | 0.25 | `codeHealth.todo` |
| Oversized | `size` | Hint | Minor | 0.5 | `codeHealth.size` |

Each setting is `auricCodeHealth.codeHealth.<category>` and is on by default. `auricCodeHealth.codeHealth.enabled` turns all of them off at once.

## How the checks read code

- A small per-language reader marks comments and strings. Task markers must be inside comments; debug, risk and security signatures ignore commented-out or quoted code. Secrets are found everywhere, including comments, because a key in a comment is still leaked.
- Signatures run only in the languages where they mean something. In a language the Studio does not know, the checks behave language-agnostically.
- **Argument-aware** signatures read the call's argument or assigned value: a dynamic value (a variable, concatenation or template with `${}`) gives **high** confidence; a constant gives **low** confidence (or is skipped where a constant is harmless); an argument that cannot be read gives **medium**.
- A file reports at most 300 code-health findings.

In the tables, *web languages* means JavaScript, TypeScript, JSX, TSX, Vue, Svelte, Astro, HTML, EJS, Handlebars, Twig, Razor, PHP and CoffeeScript.

## Possible secrets

All secret signatures map to CWE-798 (hard-coded credentials). Every match is redacted; see [Secrets and redaction](secrets-and-redaction.md).

| Signature | Title | Detects |
| --- | --- | --- |
| `ch-secret-aws-access` | AWS access key | An AWS access key ID (`AKIA` followed by 16 characters) |
| `ch-secret-aws-temporary` | AWS temporary access key | A temporary AWS key (`ASIA` followed by 16 characters) |
| `ch-secret-private-key` | Embedded private key | A PEM private key block (RSA, EC, DSA, OpenSSH, encrypted or PGP) |
| `ch-secret-github-token` | GitHub token | A GitHub token starting `ghp_`, `gho_`, `ghu_`, `ghs_` or `ghr_` |
| `ch-secret-github-pat` | GitHub fine-grained token | A token starting `github_pat_` |
| `ch-secret-gitlab-token` | GitLab access token | A GitLab personal access token (`glpat-`) |
| `ch-secret-slack-token` | Slack token | A Slack token (`xoxb-`, `xoxp-` and similar, or `xapp-`) |
| `ch-secret-google-api-key` | Google API key | A Google API key (`AIza` followed by 35 characters) |
| `ch-secret-google-oauth` | Google OAuth client secret | A Google OAuth client secret (`GOCSPX-`) |
| `ch-secret-stripe-live` | Stripe live secret | A live Stripe secret key (`sk_live_`) |
| `ch-secret-stripe-key` | Stripe secret or restricted key | A Stripe test secret or restricted key (`sk_test_`, `rk_test_`, `rk_live_`) |
| `ch-secret-anthropic-key` | Anthropic API key | An Anthropic API key (`sk-ant-`) |
| `ch-secret-openai-key` | OpenAI API key | An OpenAI key (`sk-proj-`, `sk-svcacct-`, `sk-admin-`, or `sk-` and 32+ characters) |
| `ch-secret-npm-token` | npm access token | An npm token (`npm_` and 36 characters) |
| `ch-secret-sendgrid-key` | SendGrid API key | A SendGrid key (`SG.` with two dotted parts) |
| `ch-secret-digitalocean-token` | DigitalOcean token | A DigitalOcean token (`dop_v1_` and 64 hex characters) |
| `ch-secret-slack-webhook` | Slack webhook secret | A Slack incoming-webhook URL with its secret path |
| `ch-secret-discord-webhook` | Discord webhook secret | A Discord webhook URL with its token |
| `ch-secret-jwt` | JSON Web Token | A three-part token starting `eyJ` (medium confidence) |
| `ch-secret-credential-url` | Credentials embedded in URL | `scheme://user:password@host` for HTTP(S), Postgres, MySQL, MongoDB, Redis, AMQP, FTP, SSH, SMTP |
| `ch-secret-connection-string` | Password in a connection string | `Password=`, `Pwd=`, `AccountKey=` or `SharedAccessKey=` in a connection string (Azure, ADO.NET) |
| `ch-secret-auth-header` | Hard-coded Authorization header | A `Bearer` or `Basic` token written into a string |
| `ch-secret-assignment` | Hardcoded credential assignment | A credential-named key assigned a literal value (medium confidence; see below) |
| `ch-secret-custom` | Workspace custom secret signature | A match of one of your `codeHealth.customSecretPatterns` (medium confidence) |

**Credential assignments** are keys whose name ends in a credential word, such as `password`, `passwd`, `pwd`, `passphrase`, `secret`, `token`, `bearer`, `api_key`, `api_secret`, `secret_key` or `private_key` (so `DB_PASSWORD` and `adminPassword` count, but `password_hint` does not), assigned a value of 8 to 500 characters. Quoted and typed keys, `=`, `:`, `:=` and `=>` are all understood, as are unquoted values in YAML, INI, properties, `.env`, shell and TOML files, and XML settings such as `<add key="ApiKey" value="…"/>` and `<password>…</password>`.

The message for each is short, for example **Looks like a GitHub token.**, and the fix is **Move secrets to env vars / a secret manager and rotate any that were committed.**

## Security risks

All security signatures map to OWASP Top 10:2025 A05 and have high confidence unless noted. The fix is **Harden or remove this — see the linked guidance.**

| Signature | Title | Detects | Languages |
| --- | --- | --- | --- |
| `ch-sec-tls-node-option` | Node TLS verification disabled | `rejectUnauthorized: false` | Any |
| `ch-sec-tls-node-env` | Process-wide Node TLS bypass | `NODE_TLS_REJECT_UNAUTHORIZED` set to `0` | Any |
| `ch-sec-tls-python` | Python TLS verification disabled | `verify=False`, `ssl._create_unverified_context()`, `check_hostname=False`, `CERT_NONE` | Any, outside strings |
| `ch-sec-tls-go` | Go TLS verification disabled | `InsecureSkipVerify: true` | Any, outside strings |
| `ch-sec-tls-php` | PHP cURL TLS verification disabled | `CURLOPT_SSL_VERIFYPEER` or `CURLOPT_SSL_VERIFYHOST` set to false or 0 | PHP |
| `ch-sec-weak-crypto-node` | Weak Node cryptographic hash | `createHash('md5')` or `createHash('sha1')` | Any, outside strings |
| `ch-sec-weak-crypto-python` | Weak Python cryptographic hash | `hashlib.md5`, `hashlib.sha1`, `hashlib.new('md5')`; not with `usedforsecurity=False` | Any, outside strings |
| `ch-sec-weak-crypto-java` | Weak Java / .NET cryptographic hash | `MessageDigest.getInstance("MD5")` or SHA-1, `DigestUtils.md5`, `MD5.Create()` | Java, Kotlin, Scala, Groovy, C#, F#, VB |
| `ch-sec-weak-crypto-php` | Weak PHP password hash | `md5()` or `sha1()` of a `$…pass`, `$…pwd` or `$…secret` variable | PHP |
| `ch-sec-deserialize-python` | Unsafe Python deserialization | `pickle`, `cPickle` or `marshal` `load` and `loads` | Any, outside strings |
| `ch-sec-yaml-load` | Unsafe YAML deserialization | `yaml.load`, `load_all`, `full_load`, `unsafe_load`; not with `SafeLoader`, not js-yaml | Any, outside strings |
| `ch-sec-php-unserialize` | Unsafe PHP deserialization | `unserialize()`, unless `allowed_classes` is false | PHP |
| `ch-sec-string-timer` | String-evaluated timer | `setTimeout` or `setInterval` given a string | Web languages |
| `ch-sec-vue-html` | Vue raw HTML sink | The `v-html` directive | Any |
| `ch-sec-insert-html` | insertAdjacentHTML sink | `insertAdjacentHTML` with dynamic, unsanitised markup | Web languages |
| `ch-sec-wildcard-cors` | Wildcard CORS policy | `Access-Control-Allow-Origin` set to `*` | Any |
| `ch-sec-command-injection` | Dynamic shell command | `child_process` `exec` with a dynamic command, or `spawn` and `execFile` with `shell: true` | JavaScript family |
| `ch-sec-sql-template` | Interpolated SQL query | SQL built by interpolation: JS templates, Python f-strings, C# `$""`, PHP `"$x"`, Ruby `#{}` | Any |
| `ch-sec-sql-concat` | Concatenated SQL query | SQL built with `+`, PHP `.`, Python `%` or `.format`, or `sprintf`-style formatting | Any |

Notes:

- **Command injection** follows how `child_process` was imported: `require`, `import`, aliases, destructuring and `promisify`. A constant command is not reported; an unreadable one is reported at medium confidence.
- **SQL** signatures look for upper-case SQL shapes (`SELECT … FROM`, `INSERT INTO`, `UPDATE … SET`, `DELETE FROM`, `DROP`, `CREATE` or `ALTER TABLE`, `UNION SELECT`, `MERGE INTO`), so ordinary prose is ignored. Tagged templates such as `` sql`…` `` are parameterised and not reported.
- **insertAdjacentHTML** is skipped when the markup is a constant or passes through a sanitiser (a function named like `sanitize…`, `escapeHtml`, `filterXSS`, `xss` or `purify`).

## Risky APIs

Signatures with **contextual** confidence are argument-aware. The fix is **Review this call for safer alternatives.**

| Signature | Title | Detects | Languages | Confidence |
| --- | --- | --- | --- | --- |
| `ch-risk-eval` | Dynamic eval | `eval(…)`, including `window.eval` and `globalThis.eval` | Any, outside strings | contextual |
| `ch-risk-function-constructor` | Function constructor | `new Function(…)` | Web languages | contextual |
| `ch-risk-innerhtml` | Dynamic innerHTML assignment | Assigning a dynamic value to `innerHTML` or `outerHTML`; constants and sanitised values are skipped | Web languages | contextual |
| `ch-risk-react-html` | React raw HTML sink | `dangerouslySetInnerHTML` | JSX, TSX | medium |
| `ch-risk-document-write` | document.write usage | `document.write()` or `writeln()` | Web languages | medium |
| `ch-risk-shell` | Shell execution | `os.system`, `os.popen`, `subprocess.getoutput`, or `subprocess` calls with `shell=True` | Python | contextual |

A constant argument adds **(constant argument — lower risk)** to the message and lowers the confidence.

## Debug leftovers

The message is **Leftover debug statement (…).** and the fix **Remove before committing, or route through a real logger.** Normal output such as `print`, `echo` and `fmt.Println` is deliberately not reported. Commented-out and quoted code is ignored. Confidence is medium.

| Signature | Title | Detects | Languages |
| --- | --- | --- | --- |
| `ch-debug-console` | Console debug output | `console.log`, `debug`, `trace`, `dir` or `table` | Web languages |
| `ch-debug-debugger` | Debugger statement | `debugger` | Web languages |
| `ch-debug-rust-dbg` | Rust dbg! output | `dbg!(…)` | Rust |
| `ch-debug-php-dump` | PHP diagnostic dump | `var_dump`, `print_r`, `var_export` | PHP |
| `ch-debug-ruby` | Ruby debugger hook | `binding.pry`, `binding.irb`, `byebug` | Ruby |
| `ch-debug-python` | Python debugger hook | `pdb.set_trace()`, `ipdb.set_trace()`, `pudb.set_trace()`, `breakpoint()` | Python |
| `ch-debug-nslog` | NSLog debug output | `NSLog(…)` | Objective-C, Objective-C++, Swift |
| `ch-debug-java-system-out` | Java System.out debug output | `System.out.print` and `println` | Java, Groovy, Scala, Kotlin |
| `ch-debug-go` | Go debug print | `fmt.Print`, `Println` or `Printf` whose text starts with `DEBUG` | Go |

## Task markers

| Signature | Marker |
| --- | --- |
| `ch-todo-todo` | TODO |
| `ch-todo-fixme` | FIXME |
| `ch-todo-hack` | HACK |
| `ch-todo-xxx` | XXX |
| `ch-todo-bug` | BUG |
| `ch-todo-optimize` | OPTIMIZE |
| `ch-todo-refactor` | REFACTOR |
| `ch-todo-deprecated` | DEPRECATED |

- In languages the Studio can lex, an upper-case marker counts only inside a comment. Lower-case `@todo`, `todo:` and `fixme:` count inside comments too. Rust's `todo!()` and Kotlin's `TODO()` count in code.
- In markup files, a marker counts inside a comment, and `TODO`, `FIXME` and `HACK` count anywhere.
- The message quotes the text after the marker, for example `TODO: remove the legacy header`. The fix is **Resolve or convert into a tracked issue.** Confidence is medium.

## Merge markers

| Signature | Title | Detects |
| --- | --- | --- |
| `ch-conflict` | Unresolved merge marker | A line starting with seven `<` or `>` characters, or seven equals signs or vertical bars inside a conflict |

A lone `=======` line outside a conflict, such as a Markdown heading underline, is not reported. The message is **Unresolved merge-conflict marker.** and the fix **Resolve the conflict and remove the marker.**

## Oversized

| Signature | Title | Detects | Where |
| --- | --- | --- | --- |
| `ch-longline` | Oversized source line | A line longer than 240 characters, except lines that start with a URL | Editor and scans |
| `ch-bigfile` | Large file | A file with more than 800 lines, reported on line 1 | Project scans and the command-line scanner |

Messages: **Very long line (312 chars) — hard to read and review.** and **Large file (1204 lines) — consider splitting.**

## Search the rulebook

Every signature, the seven categories, four policies (on confidence, redaction, stable identities and suppression review) and two articles are in the knowledge database. Run **Auric Artisan: Open Rulebook & Knowledge Database** and search for a signature ID or a word such as `secret`, or select **Rule details** in a finding's hover. The **Code-health balanced baseline** rulebook brings them together. See [Rulebook and knowledge database](../../docs/rulebook-and-knowledge.md).

## Related

- [Secrets and redaction](secrets-and-redaction.md)
- [Suppression and branding](../../docs/suppression-and-branding.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
