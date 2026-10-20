# Methodology and verification

Compiled 2026-10-20. Scope: academic and archival services that expose a documented HTTP API — web archives, national archive catalogues, library and museum aggregators, scholarly graphs, bibliographic indexes, research-data repositories, life-science data services, and publisher/patent text-and-data-mining endpoints. 120 providers are catalogued.

## Two evidence classes, never mixed

| class | what it proves | where it lives |
|---|---|---|
| **Documentation snapshot** | what the provider *says* the allowance is | `data/snapshots/<slug>/*.txt` + `meta.json` |
| **Live probe** | what the endpoint *did* for one unauthenticated caller today | `data/probes.json` |

A provider can have a generous documented allowance and still refuse this caller (Semantic Scholar: 1,000 req/s documented, 429 on the probe). A provider can answer happily and publish no number at all (Wayback CDX). The reports keep the two apart and never infer one from the other.

## Pipeline

```sh
make fetch     # snapshot home/docs/policy pages per provider (gzip + text + sha256)
make probe     # one live unauthenticated request per API endpoint
make llms      # verify which providers really serve a markdown llms.txt
make facts     # build data/facts.json from the curated table + probe results
make reports   # rebuild every report from data/facts.json
make test      # integrity: every quote verbatim, every figure recomputes
make check     # re-fetch every recorded source, compare sha256 (non-destructive)
```

## How a number gets into the inventory

1. The provider publishes a rate or a monthly figure on a page that was captured.
2. The exact sentence is copied into `scripts/facts.py` as `quote`, with the page's URL and snapshot path.
3. If the figure is derived from a rate, `derivation` states the arithmetic: `rate × seconds in a 30-day month` (2,592,000) for per-second rates, `rate × 1,440 × 30` for per-minute rates.
4. `scripts/test_integrity.py` re-checks that the quote is verbatim in the snapshot and that the arithmetic reproduces the published number.

A derived number is a **ceiling**: it is what the published rate permits if you call continuously for a month. It is not a quota the provider promises to serve, and no real workload calls at the ceiling. The ranking therefore shows both the rate and the derived monthly ceiling, and says which is which.

## What the confidence column means

- **high** (28 providers) — an explicit number, or an explicit statement that access is free and keyless, in official documentation that was captured.
- **medium** (37) — an official statement that access is free or needs a key, without a number that can be converted to a call count.
- **low** (55) — nothing usable survived capture: a login wall, a JavaScript shell, a 403 challenge, a bot check, a dead host, or a documentation page that documents endpoints but never states an allowance.

`low` is not a verdict that the provider is bad. It means this run could not verify the allowance, and the report says so rather than guessing. Of the 120 providers, 89 answered an unauthenticated call during the probe, which is a different and independent fact.

## Why some well-known services are marked low

The failure modes are worth naming, because they are the reason the number is missing and not a judgement about the service:

- **Cloudflare / bot interstitial.** `europepmc.org`, `dblp.org`, `base-search.net`, `cds.cern.ch` and `pubchem.ncbi.nlm.nih.gov` serve a JavaScript challenge to a plain HTTP client. The API hosts themselves (`www.ebi.ac.uk/europepmc/webservices`, `dblp.org/search/publ/api`) do answer, so the API works even when the docs site does not.
- **Application shell.** `patentsview.org`, `uspto` developer pages and `clinicaltrials.gov/data-api` return a single-page app that renders text only in a browser. Status 200, no readable words.
- **Dead or moved documentation.** `europeana`'s Confluence page is a 404, `info.orcid.org` returns 404 for every reference path tried, `chroniclingamerica`'s legacy API is retired in favour of the loc.gov API.
- **Host does not resolve.** `api.fatcat.wiki`, `api.lareferencia.info`, `api.dimensions.ai`, `search.patentsview.org`, `timetravel.mementoweb.org`, `api.isidore.science` and `api.constellate.org` did not resolve from this machine. That is a fact about this network, not about the provider.

## Limits of this inventory

- Free tiers change without notice. Every number is as of the capture date in the snapshot's `meta.json`.
- A rate is not a quota. Converting `5 requests/second` into `12,960,000/month` is arithmetic, not a promise; it is labelled a ceiling everywhere it appears.
- Where a provider publishes several rates (guest vs authenticated, per endpoint), the lowest published rate is the one converted, because it is the one a caller without an account can rely on.
- Where a rate is shared among all callers (Semantic Scholar), or is CPU time rather than calls (Wikidata), it is deliberately **not** converted, and the report says why.
- One probe per endpoint, from one IP, at one moment. It is evidence that the endpoint answers unauthenticated callers at all; it is not a load test.
- No terms-of-service analysis is included. This is a technical inventory of documented allowances; it makes no claim that any particular use is permitted.
- Licences are noted where a page states one, but licence of the *data* and the terms of the *API* are different things and only the captured text is reported.

## Re-verifying one number

```sh
python3 -c "import json;d={r['slug']:r for r in json.load(open('data/facts.json'))};print(json.dumps(d['crossref'],indent=1))"
```

That prints the quote, the URL and the snapshot path. Open the snapshot and read the sentence; `make check` re-fetches the URL and reports whether the bytes changed.

Licence: 0BSD (see `LICENSE`).
