---
title: Auric Code Health — Secrets and redaction
description: How Auric Code Health finds hardcoded secrets, avoids placeholders, scores confidence, supports your own patterns, and makes sure a secret is never stored.
product: VS Code extensions › Auric Artisan Studio › Auric Code Health
updated: 2026-09-25
---

# Secrets and redaction

A **hardcoded secret** is a credential, such as an API key, token, password or private key, written directly into source code or configuration. Anyone who can read the repository can use it. Auric Code Health looks for secrets in every supported file, including comments, and treats them as its most serious category.

## What it finds

- **Provider credentials** with a recognisable shape: AWS access and temporary keys, GitHub and GitLab tokens, Slack tokens and webhooks, Discord webhooks, Google API keys and OAuth client secrets, Stripe secret and restricted keys, OpenAI and Anthropic API keys, npm, SendGrid and DigitalOcean tokens.
- **Private keys**: PEM blocks such as `-----BEGIN RSA PRIVATE KEY-----` followed by key data.
- **JSON Web Tokens**.
- **Credentials in URLs** (`postgres://user:password@host`) and **connection strings** (`Password=…;`, `AccountKey=…`).
- **Authorization headers** with a literal `Bearer` or `Basic` token.
- **Credential assignments**: a key named like a credential (`DB_PASSWORD`, `apiKey`, `client_secret`) given a literal value, in code, JSON, YAML, INI, `.env`, properties, TOML, shell and XML.
- **Your own patterns** from `codeHealth.customSecretPatterns`.

The full list with IDs is in [Categories and signatures](categories-and-signatures.md#possible-secrets). When several detectors match the same text, only the most specific one is reported, so one credential is one finding.

## What it deliberately ignores

To keep false positives rare, a value is not reported as a secret when it is clearly not one:

- placeholders such as `xxxxxx`, `****`, `<your-key>`, `CHANGE_ME`, `changeme`, `your_api_key`, `replace-me`, `example…`, `test…`, `dummy`, `fake`, `redacted`, `not-a-real…`;
- references to where the secret really lives: `process.env`, `import.meta`, `os.environ`, `getenv`, `${VAR}`, `$VAR`, `{{API_KEY}}`, `%VAR%`, SOPS `ENC[…]`, `vault:`, `op://`, Azure Key Vault references and ARNs;
- values that are labels, autocomplete tokens (`current-password`), validation rules, file paths to key files, or translation keys such as `auth.password`;
- sentences with spaces, and values shorter than 8 characters for name-based assignments;
- dynamic strings such as Python f-strings or C# interpolated strings with `{…}`.

Provider-shaped tokens only need to pass the obvious-placeholder check, because their shape is already specific.

## Confidence

Each secret finding has a confidence:

- **high**: a provider token, or a value that looks random (high entropy, a measure of how unpredictable the characters are) or is a long unbroken token of 24 characters or more;
- **medium**: the default for name-based assignments, JWTs and custom patterns;
- **low**: a value shorter than 12 characters.

Confidence scales the score penalty (high × 1, medium × 0.75, low × 0.4) and can be filtered in the Code Health Studio. In the remediation plan, secrets are critical tasks unless their confidence is low.

## Add your own patterns

For token formats specific to your organisation, add regular expressions (as strings) to `auricCodeHealth.codeHealth.customSecretPatterns`:

```json
{
  "auricCodeHealth.codeHealth.customSecretPatterns": [
    "INTERNAL_[A-Z0-9]{20,}",
    "corp-tok-[a-f0-9]{32}"
  ]
}
```

- Matches are reported as `ch-secret-custom` at medium confidence, with the message **Matches a custom secret pattern.**
- Invalid regular expressions are ignored.
- Matches that look like placeholders are skipped.
- The patterns apply in the editor and in project scans. The command-line scanner does not read VS Code settings, so it does not use them.

## Redaction

A detected secret is **never** stored or shown. Everywhere a finding's evidence would appear, the secret is replaced by a note giving only its length:

```text
[redacted secret; 40 characters]
```

This applies to the editor hover, the Problems message, the Project Issues view, the Code Health Studio (which shows **Secret evidence redacted**), the scan cache, `health.json`, SARIF (marked `evidenceRedacted`), the history, the project health report and the remediation plan. Secret bytes are also scrubbed from other findings on the same text, such as a task marker or security finding next to the key, so they cannot leak through another category.

The underline still covers the secret's real position in the file, so you can find and remove it.

## What to do about a secret

1. Remove the value from the source and load it at runtime from an environment variable or a secret manager.
2. **Rotate** the credential with its provider: a secret that was ever committed must be treated as exposed, even after you delete it.
3. Clean it from your repository's history if your policy requires it.

The knowledge database's article **Treat a committed secret as an incident, not a text-edit task** and the policy **Never persist a detected secret value** expand on this. Open them with **Open Rulebook & Knowledge Database**.

If a match is a false positive (for example a published test key), silence it with `auric-disable-line secret` or `auric-disable-next-line ch-secret-jwt` in a comment. See [Suppression and branding](../../docs/suppression-and-branding.md).

## Limits

Auric Code Health reads the current files only. It does not scan Git history, does not verify whether a credential is live, and is not a replacement for a dedicated secret scanner. On the labelled test set used in development, secret detection found 96% of the planted secrets with no false positives.

## Related

- [Categories and signatures](categories-and-signatures.md)
- [Privacy](../others/privacy.md)
