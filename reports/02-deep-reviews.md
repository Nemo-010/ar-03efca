# Deep reviews

Eight providers reviewed against the same questions: what is the documented allowance, what does the API actually do, what is the failure mode, and what is it good for in an archival or academic pipeline. Every figure here is also in `data/facts.json`; nothing is added in prose.

## OpenAlex

`scholarly-graph` · confidence **high** · key: free key · card: no

**Documented allowance.** 300,000 calls/month. 10,000 list+filter calls per $1 of daily budget x 30 = 300,000 calls/month; a search costs 10x a list call, so 1,000 searches/day = 30,000/month. 10 req/s without a key, 30 req/s with a free key; $0.10/day keyless, $1/day with a key.

**Live probe.** `GET https://api.openalex.org/works?filter=doi:10.1038/nature12373` returned HTTP 200 in 595 ms (200 JSON).

**What it is.** The clearest published free budget in this set: a dollar a day, with a published price per operation, so the call count follows from the price list. Single-entity lookups are free.

> Every account gets **$1 of usage per day** for free.

Source: https://help.openalex.org/access/example-costs.md · snapshot `data/snapshots/openalex/costs.txt`

**In a pipeline.** The best default for scholarly metadata because the price list is public: a DOI lookup is free, a filtered list costs a tenth of a cent per call, a full-text search costs a cent per call. That means a pipeline can budget in dollars instead of guessing at a quota. Use single-entity lookups for citation checking (free, unlimited) and reserve searches for discovery.

## Wayback Machine CDX

`web-archive` · confidence **medium** · key: none · card: no

**Documented allowance.** No call quota is published. no published call quota; the CDX endpoint answers unauthenticated callers.

**Live probe.** `GET https://web.archive.org/cdx/search/cdx?url=openalex.org&limit=2&output=json` returned HTTP 200 in 696 ms (200 JSON).

**What it is.** The CDX server is the Wayback index API: one call returns capture rows for a URL, filterable and pageable, so a caller controls its own volume. No rate or quota is stated on the captured pages.

> However, the cdx server is freely available with the rest of the open-source wayback machine software in this repository.

Source: https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server · snapshot `data/snapshots/wayback-cdx/docs.txt`

**In a pipeline.** The index of record for 'what did this page say in 2019'. One call per URL returns the capture list with status codes and digests; `collapse=digest` deduplicates, and `limit` bounds the response. There is no published quota, so pace yourself rather than relying on a header to tell you when to stop.

## Crossref REST API

`scholarly-graph` · confidence **high** · key: none · card: no

**Documented allowance.** 12,960,000 calls/month. 5/s x 2,592,000 s/month = 12,960,000 calls/month ceiling. 5 requests/second (public pool), 10/s polite pool with a mailto, 150/s with a Plus key.

**Live probe.** `GET https://api.crossref.org/works/10.1038/nature12373` returned HTTP 200 in 224 ms (200 JSON).

**What it is.** DOI metadata. No account needed for the public pool; adding a mailto moves you to the polite pool with double the rate and a concurrency allowance.

> The following limits apply: Pool Rate limit Concurrency limit Public 5 1 Polite 10 3 Plus 150 None

Source: https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/ · snapshot `data/snapshots/crossref/limits.txt`

**In a pipeline.** The cheapest way to turn a DOI into publisher-deposited metadata, and the only one here that publishes both a rate and a concurrency allowance. Add a `mailto` and you move from 5 to 10 requests/second for free, which is the single easiest performance win in this inventory.

## Library of Congress JSON API

`aggregator` · confidence **high** · key: none · card: no

**Documented allowance.** 864,000 calls/month. 20/min x 1,440 min/day x 30 = 864,000 calls/month ceiling. 20 requests/minute for the JSON/YAML API; 150/min for text and image services.

**Live probe.** `GET https://www.loc.gov/books/?q=openalex&fo=json` returned HTTP 403 in 96 ms (bot wall).

**What it is.** Library of Congress. Publishes a per-service rate table and the block duration for exceeding it, which is unusually precise for a public API.

> The API is accessible to the public with no API key or authentication required.

Source: https://www.loc.gov/apis/json-and-yaml/working-within-limits/ · snapshot `data/snapshots/loc/loclimits.txt`

**In a pipeline.** The Library of Congress API is the model public-sector API: a per-service rate table (20/minute for JSON, 150/minute for text and image), the block duration when you exceed it, and a 100,000-item paging ceiling. For newspaper and print collections it replaces the retired Chronicling America API. The caveat is the probe: a datacentre IP gets a Cloudflare challenge before the rate table ever applies, so budget for identifying your client properly rather than assuming the documented rate is reachable.

## Zenodo

`repository` · confidence **high** · key: none · card: no

**Documented allowance.** 2,592,000 calls/month. 60/min x 1,440 x 30 = 2,592,000 calls/month ceiling for guests. guest 60 requests/minute and 2,000/hour; authenticated 100/minute and 5,000/hour.

**Live probe.** `GET https://zenodo.org/api/records?q=openalex&size=1` returned HTTP 200 in 1266 ms (200 JSON).

**What it is.** CERN's repository. The clearest guest-versus-authenticated rate table in this set, and it names the per-endpoint limits that bite first (search 30/min).

> Global limit for guest users 60 requests per minute, 2000 requests per hour

Source: https://developers.zenodo.org/#rate-limiting · snapshot `data/snapshots/zenodo/limits.txt`

**In a pipeline.** CERN's repository is where a lot of European research data lands, and its rate table distinguishes guest from authenticated per endpoint — search is 30/minute, not the 60/minute headline. A DOI-to-record lookup is one call; do not walk the whole corpus.

## UniProt

`data-api` · confidence **high** · key: none · card: no

**Documented allowance.** 518,400,000 calls/month. 200/s x 2,592,000 s/month = 518,400,000 calls/month ceiling. 200 requests/second/user.

**Live probe.** `GET https://rest.uniprot.org/uniprotkb/search?query=openalex&size=1&format=json` returned HTTP 200 in 1016 ms (200 JSON).

**What it is.** Protein knowledge base. The highest published rate in this set; the number comes from the Proteins API documentation page.

> We limit your requests to 200 requests/second/user.

Source: https://www.ebi.ac.uk/proteins/api/doc/ · snapshot `data/snapshots/uniprot/r2.txt`

**In a pipeline.** The highest published rate in this inventory (200 requests/second/user) on a protein knowledge base. Realistic use is per-accession lookup during annotation, not bulk scanning; bulk belongs in the FTP download, not the API.

## The Met Collection API

`aggregator` · confidence **high** · key: none · card: no

**Documented allowance.** 207,360,000 calls/month. 80/s x 2,592,000 s/month = 207,360,000 calls/month ceiling. 80 requests/second; no registration or API key.

**Live probe.** `GET https://collectionapi.metmuseum.org/public/collection/v1/objects/436535` returned HTTP 200 in 691 ms (200 JSON).

**What it is.** The Met's collection API. Publishes the highest per-second rate of any museum API here and explicitly needs no key.

> At this time, we do not require API users to register or obtain an API key to use the service.

Source: https://metmuseum.github.io/ · snapshot `data/snapshots/met-museum/docs.txt`

**In a pipeline.** 80 requests/second with no key and no registration, over a collection whose images are openly licensed. For art and object metadata this is the least friction of any source here — and it also publishes the full dataset for download, which sidesteps the API entirely.

## US National Archives Catalog

`web-archive` · confidence **high** · key: key on application · card: no

**Documented allowance.** 10,000 calls/month. published monthly figure, not a rate conversion. 10,000 queries/month per API key (default); higher tiers to 1.5M/month.

**Live probe.** `GET https://catalog.archives.gov/api/v2/records/search?q=openalex` returned HTTP 200 in 293 ms (200 HTML).

**What it is.** US National Archives Catalog API. Publishes a plain monthly call quota with named higher tiers to 1.5M/month for partners. A keyless call gets the single-page application shell rather than JSON, which is what the probe recorded — the quota is real, but the endpoint is not open.

> NARA limits the number of Catalog API requests to a default rate of 10,000 queries per month per API key.

Source: https://www.archives.gov/research/catalog/help/api · snapshot `data/snapshots/nara/docs.txt`

**In a pipeline.** The only provider in this set that publishes a plain monthly call quota: 10,000 queries/month per key by default, with named tiers to 1.5M for partners. That makes it easy to plan and hard to scale without an application — the key is free but gated, and a keyless call gets the single-page application shell rather than JSON.

