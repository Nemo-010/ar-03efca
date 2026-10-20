# Academic and archival APIs: documented free allowances

An inventory of **117 academic and archival services that expose an HTTP API** — web archives, national archive catalogues, library and museum aggregators, scholarly graphs, bibliographic indexes, research-data repositories, life-science data services and publisher TDM endpoints. Compiled 2026-10-20.

Each provider gets a page with its documented rate, the verbatim sentence that states it, a link to the captured snapshot, and the result of one live unauthenticated request against its API.

| Metric | Value |
|---|---|
| Providers catalogued | 117 |
| With a documented call figure | 20 |
| Documented volume, 1 account each | 812,188,000 calls/month |
| Documented volume, 5 accounts each | 4,060,940,000 calls/month |
| Answered an unauthenticated probe | 87 of 117 |
| Serve a verified llms.txt | 7 |
| Require a payment card for the free tier | 0 |

The two volume figures are **ceilings**: only three providers publish a quota (monthly, daily, or a daily dollar budget with a price list); for the rest the monthly number is the published rate times the seconds in a 30-day month. `reports/03-post-analysis.md` splits the three published quotas from the rate ceilings and shows that two rows account for 89% of the total.

## Reports

| File | Contents |
|---|---|
| `reports/00-methodology.md` | how every number was produced, and what it does not mean |
| `reports/01-inventory.md` | the ranked table plus a per-category catalogue of all providers |
| `reports/02-deep-reviews.md` | eight providers reviewed in depth |
| `reports/03-post-analysis.md` | totals, friction, probe results, coverage, a verified stack |
| `reports/04-probes.md` | what each endpoint answered, with its rate-limit headers |
| `providers/<slug>.md` | one page per provider |

## Data

| File | Contents |
|---|---|
| `data/candidates.json` | the working set: slug, name, category, home, docs, probe URL |
| `data/facts.json` | the curated table: figure, derivation, quote, URL, snapshot, probe |
| `data/probes.json` | one live request per endpoint: status, latency, headers, body head |
| `data/llms.json` | per-provider llms.txt verdict, with the rejection reason |
| `data/snapshots/<slug>/` | gzip + plain text + `meta.json` (URL, status, sha256) |

## Reproduce

```sh
make all       # fetch, probe, llms, facts, reports, test
make test      # integrity: quotes verbatim, figures recompute, reports consistent
make check     # re-fetch every recorded source and compare sha256
```

`make test` is the guarantee: it fails if any quote in `data/facts.json` is not present verbatim in the snapshot it cites, or if any derived monthly figure does not reproduce from the rate named in its derivation.

## Limits

- A rate is not a quota. Ceilings are labelled as ceilings wherever they appear.
- Shared pools (Semantic Scholar) and CPU-time limits (Wikidata) are deliberately not converted to call counts.
- `low` confidence means this run could not verify the allowance — a bot interstitial, an application shell, a login wall or a dead host — not that the service is bad. 53 providers are in that state and each page says why.
- One probe per endpoint from one IP is evidence that an endpoint answers, not a load test.
- Free tiers change without notice; every number is as of its snapshot.
- No terms-of-service analysis. This is a technical inventory of documented allowances and makes no claim that any particular use is permitted.

Licence: 0BSD (see `LICENSE`).
