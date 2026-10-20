# Methodology and verification

Compiled 2026-10-20. Scope: academic and archival services that expose a documented HTTP API — web archives, national archive catalogues, library and museum aggregators, scholarly graphs, bibliographic indexes, research-data repositories, life-science data services, and publisher/patent text-and-data-mining endpoints. 117 providers are catalogued.

One provider is one API surface. Where a service publishes two distinct APIs (bioRxiv/medRxiv share a host but serve different corpora; OAPEN's library REST search and its api host were tried and are reported as one row) the row names the surface that was probed, so the count is of endpoints, not of companies.

## Where the method comes from

The discipline is adopted from two earlier inventories, and both debts are specific:

| Borrowed | From | Applied here |
|---|---|---|
| snapshot → facts → reports pipeline, with gzip + text + `meta.json` per page and sha256 on every capture | `Nemo-010/w-search-3f9a2c` | `scripts/fetch.py`, `scripts/facts.py`, `scripts/build_reports.py` |
| integrity test that re-checks every quote verbatim and every figure against its source, and refuses to generate a report citing a provider it does not have | `Nemo-010/w-search-3f9a2c` | `scripts/test_integrity.py` |
| `llms.txt` verification that rejects an HTML soft-404, an empty body, and a file belonging to another site | `Nemo-010/w-search-3f9a2c` | `scripts/llms.py` |
| per-row evidence index (url, http code, bytes, sha256, capture time) so one number can be traced to one artefact | `talaria0101/w-search-7b668b35` | `meta.json` per provider, plus `data/probes.json` |
| keeping two independent passes and saying when they disagree instead of reconciling them silently | `talaria0101/w-search-7b668b35` | documentation snapshot vs live probe, reported separately everywhere |

What is different here: this inventory is academic and archival, so the commercial-API apparatus (signup bonuses, credit-card requirements, anti-bot rankings) mostly does not apply. Three of 117 providers publish a quota; 0 ask for a card; 0 offer a trial credit. The work that mattered instead was distinguishing a published rate from a quota, a missing credential from a bot wall, and a live page from a dead host.

## Two evidence classes, never mixed

| class | what it proves | where it lives |
|---|---|---|
| **Documentation snapshot** | what the provider *says* the allowance is | `data/snapshots/<slug>/*.txt` + `meta.json` |
| **Live probe** | what the endpoint *did* for one unauthenticated caller today | `data/probes.json` |

A provider can have a generous documented allowance and still refuse this caller (Semantic Scholar documents 1,000 req/s and answered a 429 on the first probe run). A provider can answer happily and publish no number at all (Wayback CDX). The reports keep the two apart and never infer one from the other.

Two endpoints even changed their answer between attempts, and both results are kept in the probe history rather than the last one winning: Gallica answered XML on the first run and a Cloudflare challenge on the second; Perma.cc did the reverse. That is the honest state of a public API reached from a datacentre IP, and collapsing it to a single verdict would misrepresent it.

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
- **medium** (36) — an official statement that access is free or needs a key, without a number that can be converted to a call count.
- **low** (53) — nothing usable survived capture: a login wall, a JavaScript shell, a 403 challenge, a bot check, a dead host, or a documentation page that documents endpoints but never states an allowance.

`low` is not a verdict that the provider is bad. It means this run could not verify the allowance, and the report says so rather than guessing. Of the 117 providers, 87 answered an unauthenticated call during the probe, which is a different and independent fact.

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
