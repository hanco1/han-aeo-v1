# last30days integration (optional)

`last30days` is an independent third-party skill. Han AEO does not include it and will not install it automatically. Its upstream project is [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill).

Use it only when you want extra, recent-language research to supplement an AEO proposal. Han AEO works without it.

## Start without API keys

All API keys are optional. A base `last30days` installation can use its available base sources without a key; the exact sources depend on the installed version and environment. Use the third-party skill's own diagnostics, when available, to see what your installation can access.

## Minimal safe configuration

For `last30days` v3.3.2, the privacy-first setting below has been verified. When unset in that version, `FROM_BROWSER` may try Firefox or Safari cookies, so explicitly set it to `off`:

```dotenv
FROM_BROWSER=off
```

Do not use `FROM_BROWSER=false`. For other versions, follow the upstream documentation or setup wizard.

Add an API key only when you choose a source that requires one, and keep the configuration file out of version control.

## Bring findings into Han AEO

Research a concrete customer question rather than a broad keyword. Then pass the returned questions, objections, comparisons, and wording to Han AEO as supplementary research input.

Use those findings to strengthen a proposed FAQ, answer-first section, service-page subtopic, or proof gap. They supplement business facts, site evidence, Search Console data, and normal search research; they do not replace them.
