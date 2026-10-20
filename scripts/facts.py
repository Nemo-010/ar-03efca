#!/usr/bin/env python3
"""Build data/facts.json from the curated table below plus probe results.

Every number in FACTS is tied to a verbatim quote captured in
data/snapshots/<slug>/. scripts/test_integrity.py re-checks each quote
against the snapshot, so a quote that is not present fails the build.

Field meanings
--------------
monthly_calls   documented recurring free monthly call volume, computed ONLY
                where the provider states a rate or a monthly figure. When it
                is derived from a rate, `derivation` says so and the number is
                a ceiling (rate x 2,592,000 s/month), not a published quota.
rate            the documented rate as published, verbatim-ish, for the report.
one_time        a first-month or signup grant, kept out of monthly totals.
card            True/False/None — is a payment card demanded for the free tier.
key             "none" (works with no key), "free" (free key/account),
                "apply" (key granted after an application or approval),
                "paid" (key only with a paid plan), None (not established).
confidence      high   explicit number or explicit free statement in official docs
                medium official statement without a number
                low    nothing usable survived capture
                none   no free tier found in the captured pages
quote, url, snapshot  the evidence, verbatim, with its source.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

H, M, L, N = "high", "medium", "low", "none"

# slug: dict(...)
FACTS = {
 # ---------------------------------------------------------------- web archives
 "wayback-cdx": dict(
   monthly=None, rate="no published call quota; the CDX endpoint answers unauthenticated callers",
   derivation=None, one_time=None, card=False, key="none", confidence=M,
   note="The CDX server is the Wayback index API: one call returns capture rows for a URL, "
        "filterable and pageable, so a caller controls its own volume. No rate or quota is "
        "stated on the captured pages.",
   quote="However, the cdx server is freely available with the rest of the open-source wayback machine software in this repository.",
   url="https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server",
   snap="wayback-cdx/docs.txt"),
 "wayback-availability": dict(
   monthly=None, rate="no published quota", derivation=None, one_time=None, card=False,
   key="none", confidence=M,
   note="Single-URL availability check: returns the closest capture and its URL. Answered 200 "
        "in the live probe with no key.",
   quote="Internet Archive: Digital Library of Free & Borrowable Texts, Movies, Music & Wayback Machine",
   url="https://archive.org/", snap="wayback-availability/home.txt"),
 "wayback-save": dict(
   monthly=None, rate="Save Page Now is rate-limited per account in practice; no number captured",
   derivation=None, one_time=None, card=False, key=None, confidence=L,
   note="Write endpoint. The status endpoint answered 200 unauthenticated in the probe, but no "
        "documented allowance survived capture.",
   quote="All of these are in digital form and freely available to anyone with an internet connection.",
   url="https://archive.org/developers/", snap="wayback-save/docs.txt"),
 "ia-metadata": dict(
   monthly=None, rate="no published quota", derivation=None, one_time=None, card=False,
   key="none", confidence=M,
   note="Item metadata read API. Answers a bare GET per identifier and is the cheapest way to "
        "turn an archive.org identifier into structured metadata.",
   quote="An item’s metadata may be fetched by making an HTTP GET request to",
   url="https://archive.org/developers/md-read.html", snap="ia-metadata/docs.txt"),
 "ia-fulltext": dict(
   monthly=None, rate="no published quota", derivation=None, one_time=None, card=False,
   key=None, confidence=L,
   note="Full-text search inside archived books. The endpoint refused connections from this "
        "machine during the probe, so nothing is claimed about it.",
   quote="Internet Archive: Digital Library of Free & Borrowable Texts, Movies, Music & Wayback Machine",
   url="https://archive.org/search", snap="ia-fulltext/home.txt"),
 "fatcat": dict(
   monthly=None, rate="no published quota", derivation=None, one_time=None, card=False,
   key="none", confidence=L,
   note="IA Scholar's bibliographic API. DNS for api.fatcat.wiki did not resolve from this "
        "machine during the probe, so the endpoint could not be exercised.",
   quote="This service provides fulltext searching for research publications archived in Internet Archive's various collections.",
   url="https://scholar.archive.org/help", snap="fatcat/policy2.txt"),
 "commoncrawl": dict(
   monthly=None, rate="no published call quota; the index is a static file service",
   derivation=None, one_time=None, card=False, key="none", confidence=H,
   note="Crawl corpora and the CDXJ index are free to read. There is no account and no per-call "
        "price; volume is bounded by the index's own throughput.",
   quote="Common Crawl is a 501(c)(3) non-profit organization dedicated to providing a copy of the Internet to Internet researchers, companies and individuals at no cost for the purpose of research and analysis.",
   url="https://commoncrawl.org/faq", snap="commoncrawl/limits.txt"),
 "arquivo": dict(
   monthly=10800000, rate="250 requests/60s (full-text & URL search); 400 requests/60s (image, Memento)",
   derivation="250/60s x 2,592,000 s/month = 10,800,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="Portuguese web archive. Publishes per-endpoint limits and the 429 it returns above them.",
   quote="If a client exceeds the following maximum usage limits, it will receive an error \"HTTP 429 Too many requests\" and must decrease its access rate:",
   url="https://arquivo.pt/api", snap="arquivo/limits.txt"),
 "ukwa": dict(
   monthly=None, rate="not established", derivation=None, one_time=None, card=False,
   key=None, confidence=L,
   note="UK Web Archive. Neither the documentation page nor its archived copy could be fetched "
        "from this machine; no allowance is claimed.",
   quote="", url="", snap=""),
 "archive-today": dict(
   monthly=None, rate="no published quota; the site throttles bursty callers with 429",
   derivation=None, one_time=None, card=False, key="none", confidence=L,
   note="Readable via its timemap and newest endpoints. The probe got a 200 on the timemap and a "
        "429 on the newest lookup, which is the site's own throttle rather than a documented tier.",
   quote="Archive.today is a time capsule for web pages!",
   url="https://archive.ph/", snap="archive-today/docs.txt"),
 "memento": dict(
   monthly=None, rate="not established", derivation=None, one_time=None, card=False,
   key=None, confidence=L,
   note="Aggregator over many archives' Memento endpoints. The host did not resolve from this "
        "machine during the probe.",
   quote="", url="", snap=""),
 "perma": dict(
   monthly=None, rate="public-archive endpoints need no key; the rest need an API key",
   derivation=None, one_time=None, card=False, key="apply", confidence=M,
   note="Library-run link permanence service. The public-archives listing is readable without a "
        "key; creating links needs an account.",
   quote="You do not need an API Key to use this portion of the API.",
   url="https://perma.cc/docs/developer", snap="perma/docs.txt"),
 "conifer": dict(
   monthly=None, rate="free accounts get 5GB of storage; no call quota published",
   derivation=None, one_time=None, card=False, key="free", confidence=M,
   note="Rhizome's web-archiving service. The free tier is measured in stored bytes, not calls.",
   quote="Free accounts with 5GB of storage.",
   url="https://conifer.rhizome.org/", snap="conifer/home.txt"),
 "softwareheritage": dict(
   monthly=None, rate="no published quota; the API documents only its routes",
   derivation=None, one_time=None, card=False, key="none", confidence=M,
   note="Source-code archive. The API root answered 200 unauthenticated in the probe; the "
        "captured documentation is a machine-readable route list with no rate statement.",
   quote='Get information about a content (aka a \\"blob\\") object',
   url="https://archive.softwareheritage.org/api/1/", snap="softwareheritage/limits.txt"),
 "nara": dict(
   monthly=10000, rate="10,000 queries/month per API key (default); higher tiers to 1.5M/month",
   derivation="published monthly figure, not a rate conversion",
   one_time=None, card=False, key="apply", confidence=H,
   note="US National Archives Catalog API. The only provider here that publishes a plain monthly "
        "call quota with named higher tiers. A keyless call gets the single-page application "
        "shell rather than JSON, which is what the probe recorded — the quota is real, but the "
        "endpoint is not open.",
   quote="NARA limits the number of Catalog API requests to a default rate of 10,000 queries per month per API key.",
   url="https://www.archives.gov/research/catalog/help/api", snap="nara/docs.txt"),
 "tna-discovery": dict(
   monthly=None, rate="not established", derivation=None, one_time=None, card=False,
   key=None, confidence=L,
   note="UK National Archives Discovery API answered 200 in the probe, but its help page was not "
        "captured and no allowance is claimed.",
   quote="It provides brief descriptions of documents and details of their locations in public and private hands.",
   url="https://discovery.nationalarchives.gov.uk/", snap="tna-discovery/home.txt"),
 "archives-portal-europe": dict(
   monthly=None, rate="OAI-PMH endpoint answered 404 at the documented path", derivation=None,
   one_time=None, card=False, key=None, confidence=L,
   note="Aggregates European archive catalogues. The OAI-PMH path in the probe returned 404, so "
        "the endpoint recorded here is unverified.",
   quote="This object is made available under the Creative Commons CC0 1.0 Public Domain Dedication .",
   url="https://www.archivesportaleurope.net/", snap="archives-portal-europe/home.txt"),
 "snac": dict(
   monthly=None, rate="not established", derivation=None, one_time=None, card=False,
   key=None, confidence=L,
   note="Social Networks and Archival Context, the archival-authority cooperative. Its API root "
        "answers 400 to a bare GET because it wants a query, so the probe proves the host answers "
        "but not the allowance.",
   quote="", url="", snap=""),

 # ------------------------------------------------------------ library aggregators
 "europeana": dict(
   monthly=None, rate="no published call quota; a demo key (`wskey=api2demo`) works on the record API",
   derivation=None, one_time=None, card=False, key="free", confidence=M,
   note="Europeana's search API answers with the public demo key. The documented documentation "
        "URL moved; the captured page is a Confluence 'page not found', so nothing about quotas is claimed.",
   quote="You‘re viewing this with anonymous access, so some content might be blocked.",
   url="https://europeana.atlassian.net/wiki/spaces/EF/pages/2477260801/API+documentation",
   snap="europeana/docs.txt"),
 "dpla": dict(
   monthly=None, rate="not established (API key required; docs are behind a 403 for this client)",
   derivation=None, one_time=None, card=False, key="free", confidence=L,
   note="Digital Public Library of America. Every documentation URL tried returned 403 to this "
        "client, so the free tier is recorded as unverified rather than guessed.",
   quote="", url="", snap=""),
 "digitalnz": dict(
   monthly=None, rate="not established (key required; docs served a 202 challenge)", derivation=None,
   one_time=None, card=False, key="free", confidence=L,
   note="The records endpoint answered 200 with a key-less call in the probe, but the "
        "documentation pages returned a 202 interstitial and no allowance was captured.",
   quote="", url="", snap=""),
 "trove": dict(
   monthly=None, rate="call rate is set per application level; the table lists 200m for each level",
   derivation=None, one_time=None, card=False, key="apply", confidence=M,
   note="National Library of Australia. Access needs an approved key and the published table "
        "lists a call rate per review level; the unit of '200m' is not spelled out, so it is not "
        "converted into a monthly figure here.",
   quote="Access and Terms of Use On-going use of the Trove API will require an active API key.",
   url="https://trove.nla.gov.au/about/create-something/using-api", snap="trove/docs.txt"),
 "smithsonian": dict(
   monthly=None, rate="api_key required; no call quota captured", derivation=None, one_time=None,
   card=False, key="free", confidence=M,
   note="Open Access collection metadata and images. The content itself is released for reuse "
        "without asking; the API wants a key.",
   quote="Welcome to Smithsonian Open Access, where you can download, share, and reuse millions of the Smithsonian’s images—right now, without asking.",
   url="https://www.si.edu/openaccess", snap="smithsonian/home.txt"),
 "loc": dict(
   monthly=864000, rate="20 requests/minute for the JSON/YAML API; 150/min for text and image services",
   derivation="20/min x 1,440 min/day x 30 = 864,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="Library of Congress. Publishes a per-service rate table and the block duration for "
        "exceeding it, which is unusually precise for a public API.",
   quote="The API is accessible to the public with no API key or authentication required.",
   url="https://www.loc.gov/apis/json-and-yaml/working-within-limits/", snap="loc/loclimits.txt"),
 "chroniclingamerica": dict(
   monthly=None, rate="the legacy dedicated API is retired; the collection is served by the loc.gov API",
   derivation=None, one_time=None, card=False, key="none", confidence=M,
   note="Historic US newspapers. The legacy endpoint now 404s; use the loc.gov API, whose limits "
        "are recorded on the Library of Congress row.",
   quote="Beginning in 2025, the Chronicling America collection is accessible exclusively via the loc.gov API.",
   url="https://www.loc.gov/apis/additional-apis/chronicling-america-api/",
   snap="chroniclingamerica/policy.txt"),
 "gallica": dict(
   monthly=None, rate="SRU service; no call quota published in the captured pages",
   derivation=None, one_time=None, card=False, key="none", confidence=M,
   note="BnF's digital library. Exposes an SRU endpoint with the standard maximumRecords paging "
        "parameter; the documentation is in French and states no rate.",
   quote="maximumRecords : il s'agit du nombre de résultats retournés par le service SRU.",
   url="https://api.bnf.fr/api-gallica-de-recherche", snap="gallica/docs.txt"),
 "hathitrust": dict(
   monthly=None, rate="no published call quota; bulk work is steered to OAI and the hathifiles",
   derivation=None, one_time=None, card=False, key="none", confidence=M,
   note="Bibliographic lookups by identifier only — it is explicitly not a keyword search API.",
   quote="The HathiTrust Bibliographic API is not a search API (e.g., where you use a keyword to search across the collection).",
   url="https://www.hathitrust.org/bib_api", snap="hathitrust/limits.txt"),
 "openlibrary": dict(
   monthly=2592000, rate="1 request/second unidentified; 3 requests/second with a User-Agent carrying an email",
   derivation="1/s x 2,592,000 s/month = 2,592,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="Internet Archive's book catalogue. Identifies callers by User-Agent and gives them 3x.",
   quote="Default (non-identified requests): 1 request per second",
   url="https://openlibrary.org/developers/api", snap="openlibrary/docs.txt"),
 "gutenberg": dict(
   monthly=None, rate="no fees and no registration; the mirror is a static file service",
   derivation=None, one_time=None, card=False, key="none", confidence=H,
   note="Project Gutenberg's catalogue, reached here through the Gutendex JSON wrapper. The "
        "wrapper is a third-party service, so its own uptime is not Gutenberg's.",
   quote="✓ 100% Free - No fees, no registration, completely free",
   url="https://www.gutenberg.org/", snap="gutenberg/home.txt"),
 "wikidata": dict(
   monthly=None, rate="60 seconds of processing time per 60 seconds, per client; 30 error queries/minute",
   derivation=None, one_time=None, card=False, key="none", confidence=H,
   note="SPARQL endpoint. The limit is CPU time, not calls, so it cannot be converted to a call "
        "count — a cheap query and an expensive one cost the same one call but very different time.",
   quote="One client (user agent + IP) is allowed 60 seconds of processing time each 60 seconds",
   url="https://query.wikidata.org/", snap="wikidata/docs.txt"),
 "wikipedia-api": dict(
   monthly=None, rate="no hard speed limit on reads; write and state-changing calls are limited",
   derivation=None, one_time=None, card=False, key="none", confidence=H,
   note="MediaWiki action API. Read traffic is governed by etiquette rather than a published quota.",
   quote="There is no hard speed limit on read requests, but be considerate and try not to take a site down.",
   url="https://www.mediawiki.org/wiki/API:Etiquette", snap="wikipedia-api/docs.txt"),

 # --------------------------------------------------------- scholarly graphs
 "openalex": dict(
   monthly=300000, rate="10 req/s without a key, 30 req/s with a free key; $0.10/day keyless, $1/day with a key",
   derivation="10,000 list+filter calls per $1 of daily budget x 30 = 300,000 calls/month; "
              "a search costs 10x a list call, so 1,000 searches/day = 30,000/month",
   one_time=None, card=False, key="free", confidence=H,
   note="The clearest published free budget in this set: a dollar a day, with a published price "
        "per operation, so the call count follows from the price list. Single-entity lookups are free.",
   quote="Every account gets **$1 of usage per day** for free.",
   url="https://help.openalex.org/access/example-costs.md", snap="openalex/costs.txt"),
 "crossref": dict(
   monthly=12960000, rate="5 requests/second (public pool), 10/s polite pool with a mailto, 150/s with a Plus key",
   derivation="5/s x 2,592,000 s/month = 12,960,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="DOI metadata. No account needed for the public pool; adding a mailto moves you to the "
        "polite pool with double the rate and a concurrency allowance.",
   quote="The following limits apply: Pool Rate limit Concurrency limit Public 5 1 Polite 10 3 Plus 150 None",
   url="https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/",
   snap="crossref/limits.txt"),
 "datacite": dict(
   monthly=4320000, rate="500 requests/5min unidentified, 1,000 identified (mailto), 3,000 authenticated",
   derivation="500 per 5 min = 100/min x 1,440 x 30 = 4,320,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="DOI metadata for research data. Three tiers keyed on how the caller identifies itself; "
        "the lowest tier needs nothing at all.",
   quote="| 500 requests per 5 minutes per IP address |",
   url="https://support.datacite.org/docs/rate-limit.md", snap="datacite/ratelimits.txt"),
 "semanticscholar": dict(
   monthly=None, rate="1,000 requests/second shared by ALL unauthenticated callers; 1 req/s per key",
   derivation=None, one_time=None, card=False, key="none", confidence=H,
   note="The headline rate is a shared pool, not a per-caller allowance, so it is deliberately "
        "not converted into a monthly figure. In practice the pool is often exhausted: the probe "
        "got a 429.",
   quote="Most Semantic Scholar endpoints are available to the public without authentication, but they are rate-limited to 1000 requests per second shared among all unauthenticated users.",
   url="https://www.semanticscholar.org/product/api", snap="semanticscholar/docs.txt"),
 "core": dict(
   monthly=1296000, rate="one batch request or five single requests per 10 seconds, without registration",
   derivation="5 per 10 s = 30/min x 1,440 x 30 = 1,296,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="Open-access aggregator. Free and keyless; registered organisations get a faster rate "
        "that is typically paid.",
   quote="CORE API is free and does not require registration, subject to our rate limits .",
   url="https://core.ac.uk/services/api", snap="core/docs.txt"),
 "openaire-graph": dict(
   monthly=None, rate="no call quota published; the graph is also downloadable in bulk",
   derivation=None, one_time=None, card=False, key="none", confidence=M,
   note="The Graph API answered 200 unauthenticated in the probe. Bulk download is the intended "
        "route for volume, and the licence is CC-BY or CC-0. The explore.openaire.eu web UI is a "
        "front end over this same API, so it is not counted as a separate provider.",
   quote="The Graph is freely available for download and re-use to all as CC-BY or CC-0.",
   url="https://graph.openaire.eu/", snap="openaire-graph/home.txt"),
 "openaire-search": dict(
   monthly=None, rate="no call quota published", derivation=None, one_time=None, card=False,
   key="none", confidence=M,
   note="The older publications search endpoint. Still answers unauthenticated; superseded by the "
        "Graph API for structured queries.",
   quote="Imagine a vast collection of research products all linked together, contextualised and openly available.",
   url="https://api.openaire.eu/", snap="openaire-search/docs.txt"),
 "base": dict(
   monthly=None, rate="API key granted on application; no call quota published",
   derivation=None, one_time=None, card=False, key="apply", confidence=M,
   note="Bielefeld Academic Search Engine. The key is free but must be applied for, which puts it "
        "out of reach of a gateway that wants to start today.",
   quote="Before you can start testing and using the interface, you need to apply for an API key via this form .",
   url="https://api.base-search.net/", snap="base/docs.txt"),
 "orcid": dict(
   monthly=None, rate="public API; the rate-limit page was not captured", derivation=None,
   one_time=None, card=False, key="free", confidence=L,
   note="Researcher identifiers. The public API answered 200 unauthenticated; the documentation "
        "site returned 404 for every path tried, so no number is claimed.",
   quote="", url="", snap=""),
 "ror": dict(
   monthly=17280000, rate="2,000 requests per 5 minutes per IP address; no registration",
   derivation="2,000 per 5 min = 400/min x 1,440 x 30 = 17,280,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="Research organisation registry. Publishes both the rate and the absence of registration.",
   quote="No registration is currently required to use the ROR API, but note that the rate limit is a maximum of 2000 requests in a 5-minute period per IP address",
   url="https://ror.readme.io/docs/rest-api", snap="ror/docs.txt"),
 "dblp": dict(
   monthly=None, rate="no published quota; the site answers a JS challenge to non-browser clients",
   derivation=None, one_time=None, card=False, key="none", confidence=L,
   note="Computer-science bibliography. The live probe returned 202 with an interstitial, so the "
        "JSON API is reachable only through a client that runs the challenge; the archived copy of "
        "the FAQ is what is quoted here.",
   quote="Part of the search API is still in flux.",
   url="https://web.archive.org/web/20260723200605/https://dblp.org/faq/How+to+use+the+dblp+search+API.html",
   snap="dblp/docs.txt"),
 "opencitations": dict(
   monthly=7776000, rate="180 requests/minute per IP address", derivation="180/min x 1,440 x 30 = 7,776,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="Citation index. CC0 data, no key, published rate.",
   quote="API calls are rate-limited to 180 requests/minute per IP address to ensure fair usage and service availability.",
   url="https://opencitations.net/index/api/v2", snap="opencitations/docs.txt"),
 "crossref-eventdata": dict(
   monthly=None, rate="not established — the host did not resolve from this machine", derivation=None,
   one_time=None, card=False, key=None, confidence=L,
   note="Event data (mentions, citations) over Crossref DOIs. Recorded as unverified.",
   quote="", url="", snap=""),
 "dimensions": dict(
   monthly=1296000, rate="30 requests/minute per IP; free access only for eligible research projects",
   derivation="30/min x 1,440 x 30 = 1,296,000 calls/month ceiling, but eligibility is restricted",
   one_time=None, card=False, key="apply", confidence=H,
   note="The rate is published, but free access is granted to eligible scientometric research "
        "projects rather than to anyone who signs up, so the ceiling is not generally available.",
   quote="The Analytics API and the CRIS API are limited to 30 requests per IP address per minute.",
   url="https://docs.dimensions.ai/dsl/api.html", snap="dimensions/docs.txt"),
 "lens": dict(
   monthly=None, rate="API key required; no free allowance published", derivation=None,
   one_time=None, card=None, key="paid", confidence=M,
   note="Scholarly and patent records. The API root answers 401 without a key; the site markets a "
        "publicly available database but not a free API tier.",
   quote="This is the world’s largest publicly available database with internal transparency metrics.",
   url="https://www.lens.org/", snap="lens/home.txt"),
 "scite": dict(
   monthly=None, rate="papers and tallies endpoints are public; everything else needs a key",
   derivation=None, one_time=None, card=False, key="free", confidence=H,
   note="Citation statements (supporting / contradicting). Two endpoints are explicitly public, "
        "which is enough for lookups by DOI without an account.",
   quote="Papers and Tallies are public and don't require an API key.",
   url="https://docs.scite.ai/authentication.md", snap="scite/auth.txt"),
 "altmetric": dict(
   monthly=None, rate="API key required; no free allowance captured", derivation=None,
   one_time=None, card=None, key="apply", confidence=L,
   note="Attention scores for research outputs. The details API answered 403 without a key.",
   quote="Altmetric does all the heavy lifting involved in extracting, disambiguating and",
   url="https://api.altmetric.com/", snap="altmetric/limits.txt"),
 "sherpa-romeo": dict(
   monthly=None, rate="API key required; the docs site returned 403 to this client", derivation=None,
   one_time=None, card=False, key="apply", confidence=L,
   note="Journal open-access policies. Recorded as unverified: every documentation fetch returned "
        "a 403 challenge page.",
   quote="", url="", snap=""),

 # ------------------------------------------------------- bibliographic indexes
 "pubmed": dict(
   monthly=7776000, rate="3 requests/second without a key; 10/s with an NCBI API key",
   derivation="3/s x 2,592,000 s/month = 7,776,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="NCBI E-utilities. The 3/s figure is stated in an NLM support article and confirmed by the "
        "live response headers, which reported x-ratelimit-limit: 3.",
   quote="NCBI E-Utilities API service limits the number of requests per second (rps) to 3.",
   url="https://support.nlm.nih.gov/kbArticle/?pn=KA-05317", snap="pubmed/limits2.txt"),
 "europepmc": dict(
   monthly=None, rate="no call quota captured; the REST service answers unauthenticated",
   derivation=None, one_time=None, card=False, key="none", confidence=L,
   note="Life-sciences literature, including full text for the open-access subset. The "
        "documentation site returned 403 to this client and the captured reference PDF is a binary "
        "that could not be read here, so no number is claimed.",
   quote="Comprehensive search Search life sciences literature from trusted sources around the globe, all in one search, accessible by anyone anywhere, for free.",
   url="https://europepmc.org/", snap="europepmc/home.txt"),
 "pmc-oa": dict(
   monthly=None, rate="OAI-PMH and the OA web service; no call quota published",
   derivation=None, one_time=None, card=False, key="none", confidence=M,
   note="Full text for the PMC open-access subset. NLM names the services that may be used for "
        "automated retrieval, which matters more than a rate for a gateway.",
   quote="The PMC Cloud Service , PMC OAI-PMH Service , E-Utilities and BioC API are the only services that may be used for automated retrieval of PMC content.",
   url="https://www.ncbi.nlm.nih.gov/pmc/tools/developers/", snap="pmc-oa/limits2.txt"),
 "pmc-idconv": dict(
   monthly=None, rate="up to 200 IDs per request; no call quota published",
   derivation=None, one_time=None, card=False, key="none", confidence=M,
   note="Batches identifier conversions, which is the cheap way to normalise a reading list.",
   quote="The API service allows for up to 200 IDs in a single request.",
   url="https://www.ncbi.nlm.nih.gov/pmc/tools/id-converter-api/", snap="pmc-idconv/docs.txt"),
 "doaj": dict(
   monthly=5184000, rate="2 requests/second on all API routes, with a 5-request burst queue",
   derivation="2/s x 2,592,000 s/month = 5,184,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="Directory of Open Access Journals. Publishes the rate and the burst behaviour.",
   quote="There is a rate limit of two requests per second on all API routes.",
   url="https://doaj.org/api/v4/docs", snap="doaj/docs.txt"),
 "unpaywall": dict(
   monthly=None, rate="legacy-compatible surface over the OpenAlex database; the OpenAlex $1/day "
                      "budget is the allowance that applies",
   derivation=None, one_time=None, card=False, key="free", confidence=M,
   note="Unpaywall no longer has its own allowance: its docs say it runs on the OpenAlex database "
        "and that there is no separate Unpaywall list. The old 100k/day figure is not in any "
        "captured page, so it is not claimed.",
   quote="Since then there has been one set of data. Unpaywall is a legacy-compatible format over it, kept stable for the thousands of tools built on it.",
   url="https://help.openalex.org/access/unpaywall.md", snap="unpaywall/docs.txt"),
 "arxiv": dict(
   monthly=864000, rate="no more than one request every three seconds, single connection",
   derivation="1 per 3 s = 1,200/hour x 24 x 30 = 864,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="Preprint server. The slowest published rate in this set, and deliberately so; metadata is "
        "CC0 and bulk access is meant to come from the OAI-PMH service or the bulk data. The probe "
        "shows the throttle working: three attempts in a row returned 429, then a read timeout, "
        "then 200 — all recorded in the probe history rather than only the last one.",
   quote="When using the legacy APIs (including OAI-PMH, RSS, and the arXiv API), make no more than one request every three seconds, and limit requests to a single connection at a time.",
   url="https://info.arxiv.org/help/api/tou.html", snap="arxiv/docs.txt"),
 "biorxiv": dict(
   monthly=None, rate="no published call quota; 100 results per page, cursor paging",
   derivation=None, one_time=None, card=False, key="none", confidence=M,
   note="Preprint metadata by DOI or date window. Keyless and unthrottled in the probe.",
   quote="Results are paginated with 100 articles served in a call.",
   url="https://api.biorxiv.org/", snap="biorxiv/docs.txt"),
 "medrxiv": dict(
   monthly=None, rate="same service as bioRxiv; no published quota", derivation=None,
   one_time=None, card=False, key="none", confidence=M,
   note="Health-sciences preprints, served by the same API host as bioRxiv.",
   quote="Results are paginated with 100 articles served in a call.",
   url="https://api.biorxiv.org/", snap="medrxiv/docs.txt"),
 "hal": dict(
   monthly=None, rate="no published call quota captured", derivation=None, one_time=None,
   card=False, key="none", confidence=L,
   note="French national open archive. The search endpoint answered 200 unauthenticated; the "
        "documentation captured is an index page with no rate statement.",
   quote="Cette page vous donne accès à la documentation des APIs de HAL v3.0.",
   url="https://api.archives-ouvertes.fr/docs", snap="hal/limits.txt"),
 "ads": dict(
   monthly=150000, rate="5,000 regular requests/day for most request types, with a token; higher "
                        "limits by email request",
   derivation="5,000/day x 30 = 150,000 calls/month (published daily quota)",
   one_time=None, card=False, key="free", confidence=H,
   note="NASA Astrophysics Data System. Publishes a daily figure and an explicit process for "
        "raising it; the token is generated from the user profile page.",
   quote="All users, including API users, are subject to the same rate limit (currently 5000 regular requests/day for most request types).",
   url="https://adsabs.github.io/help/policies/rate-limits", snap="ads/ratelimits.txt"),
 "inspirehep": dict(
   monthly=7776000, rate="15 requests per 5-second window per IP address",
   derivation="15 per 5 s = 180/min x 1,440 x 30 = 7,776,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="High-energy-physics literature. Blocked requests still count against the window, which "
        "the docs warn about explicitly.",
   quote="every IP address is allowed 15 requests in a 5s window.",
   url="https://github.com/inspirehep/rest-api-doc", snap="inspirehep/docs.txt"),
 "zbmath": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key="none", confidence=L,
   note="Mathematics bibliography. The structured-search endpoint answers keyless; the "
        "documentation page captured is a stub.",
   quote="", url="", snap=""),
 "clinicaltrials": dict(
   monthly=None, rate="no published call quota captured", derivation=None, one_time=None,
   card=False, key="none", confidence=L,
   note="Trial registry. The v2 API answers keyless with JSON; the captured 'about the API' page "
        "rendered as an application shell with no readable text.",
   quote="", url="", snap=""),
 "scielo": dict(
   monthly=None, rate="not established", derivation=None, one_time=None, card=False,
   key=None, confidence=L,
   note="Latin American open-access collection. The ArticleMeta endpoint answered 200 keyless; no "
        "documentation page could be captured.",
   quote="Read our Open Access Statement",
   url="https://scielo.org/", snap="scielo/home.txt"),
 "lareferencia": dict(
   monthly=None, rate="not established — the API host did not resolve", derivation=None,
   one_time=None, card=False, key=None, confidence=L,
   note="Regional aggregator. Recorded as unverified: DNS for api.lareferencia.info did not resolve.",
   quote="", url="", snap=""),
 "oapen": dict(
   monthly=None, rate="no published call quota captured", derivation=None, one_time=None,
   card=False, key="free", confidence=L,
   note="Open-access book library. Two surfaces were tried: the library's REST search answered "
        "403 to this client, and the api.oapen.org host returns an HTML page rather than JSON. "
        "Neither is a working gateway target as configured here, so nothing is claimed.",
   quote="OAPEN connects libraries , publishers , researchers , and funders with a global infrastructure for peer-reviewed open access books",
   url="https://www.oapen.org/", snap="oapen/home.txt"),
 "doab": dict(
   monthly=None, rate="all services free of charge; no call quota published", derivation=None,
   one_time=None, card=False, key="free", confidence=H,
   note="Directory of Open Access Books. The site says the services and the data are free; the "
        "REST endpoint needs a key in the probe.",
   quote="All DOAB services are free of charge and all data is freely available.",
   url="https://www.doabooks.org/", snap="doab/home.txt"),
 "ndltd": dict(
   monthly=None, rate="not established — the OAI endpoint returned 503", derivation=None,
   one_time=None, card=False, key=None, confidence=L,
   note="Theses and dissertations. Recorded as unverified: the OAI-PMH endpoint answered 503.",
   quote="", url="", snap=""),

 # ------------------------------------------------------------- repositories
 "zenodo": dict(
   monthly=2592000, rate="guest 60 requests/minute and 2,000/hour; authenticated 100/minute and 5,000/hour",
   derivation="60/min x 1,440 x 30 = 2,592,000 calls/month ceiling for guests",
   one_time=None, card=False, key="none", confidence=H,
   note="CERN's repository. The clearest guest-versus-authenticated rate table in this set, and it "
        "names the per-endpoint limits that bite first (search 30/min).",
   quote="Global limit for guest users 60 requests per minute, 2000 requests per hour",
   url="https://developers.zenodo.org/#rate-limiting", snap="zenodo/limits.txt"),
 "figshare": dict(
   monthly=None, rate="no automatic rate limiting in place for API requests",
   derivation=None, one_time=None, card=False, key="free", confidence=H,
   note="The strongest free statement here — and the least useful one: no rate limiting is "
        "published, so there is no ceiling to plan against, and no promise it stays that way.",
   quote="We do not have automatic rate limiting in place for API requests.",
   url="https://docs.figshare.com/", snap="figshare/docs.txt"),
 "dryad": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key=None, confidence=L,
   note="Research-data repository. The API docs URL captured returns a redirect stub.",
   quote="", url="", snap=""),
 "osf": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key=None, confidence=L,
   note="Open Science Framework. The API root answers with a JSON welcome document but the docs "
        "site captured is a stub.",
   quote="", url="", snap=""),
 "dataverse": dict(
   monthly=None, rate="no published call quota captured", derivation=None, one_time=None,
   card=False, key="none", confidence=L,
   note="Harvard Dataverse. The rate limit is a per-installation setting, not a hosted allowance: "
        "an operator sets calls-per-hour per tier, and if the setting is absent there is no limit. "
        "So there is no number to publish for dataverse.harvard.edu from the docs alone.",
   quote="Rate limiting can be configured on a tier level with tier 0 being reserved for guest users and tiers 1-any for authenticated users.",
   url="https://guides.dataverse.org/en/latest/installation/config.html",
   snap="dataverse/ratelimits.txt"),
 "dataverse-nl": dict(
   monthly=None, rate="no published call quota captured", derivation=None, one_time=None,
   card=False, key="none", confidence=L,
   note="Dutch Dataverse instance; same software, same per-installation rate limiting as the "
        "Harvard row, so its allowance is whatever that installation configured.",
   quote="Rate limiting can be configured on a tier level with tier 0 being reserved for guest users and tiers 1-any for authenticated users.",
   url="https://guides.dataverse.org/en/latest/installation/config.html",
   snap="dataverse-nl/ratelimits.txt"),
 "openml": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key=None, confidence=L,
   note="Machine-learning datasets and tasks. The API answers keyless and the documentation states "
        "that OpenML is accessible to a wide range of clients; no call rate is published.",
   quote="How to use OpenML ¶ OpenML is accessible to a wide range",
   url="https://docs.openml.org/", snap="openml/docs.txt"),
 "huggingface": dict(
   monthly=None,
   rate="limits are per request class and published through RateLimit headers, not as one table; "
        "the docs use '100 requests per 5 minutes' only as an example of the header format",
   derivation=None,
   one_time=None, card=False, key="free", confidence=M,
   note="Model and dataset hub. Deliberately not converted into a monthly figure: the only number "
        "on the page is an illustration of header syntax, and treating it as a quota would invent "
        "an allowance the docs do not state.",
   quote="All API calls are subject to the HF-wide Rate limits .",
   url="https://huggingface.co/docs/hub/rate-limits", snap="huggingface/docs.txt"),
 "paperswithcode": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key=None, confidence=L,
   note="Papers with code links. The API answers, but the captured docs page is a 1.4MB HTML shell.",
   quote="", url="", snap=""),
 "openreview": dict(
   monthly=None, rate="no published call quota captured", derivation=None, one_time=None,
   card=False, key=None, confidence=L,
   note="Peer-review platform. The v2 notes endpoint needs an invitation parameter and answers 403 "
        "to a bare call, so nothing is claimed about an allowance.",
   quote="API V2 | OpenReview",
   url="https://docs.openreview.net/reference/api-v2", snap="openreview/docs.txt"),
 "dataone": dict(
   monthly=None, rate="not established", derivation=None, one_time=None, card=False,
   key=None, confidence=L,
   note="Earth-observation data network. The Solr query endpoint answered 200 keyless; the "
        "documentation URL captured is an authorisation error page.",
   quote="", url="", snap=""),
 "re3data": dict(
   monthly=None, rate="no published quota; the API is a plain REST interface", derivation=None,
   one_time=None, card=False, key="none", confidence=M,
   note="Registry of research-data repositories — useful for finding a repository, not for content.",
   quote="re3data.org supports the retrievial of its content via API.",
   url="https://www.re3data.org/api/doc", snap="re3data/docs.txt"),
 "thoth": dict(
   monthly=None, rate="no published quota; GraphQL and export APIs", derivation=None,
   one_time=None, card=False, key="none", confidence=M,
   note="Open-metadata service for book publishers. Metadata is CC0.",
   quote="Stay open with open APIs, no lock-in, and CC0-licensed metadata.",
   url="https://thoth.pub/", snap="thoth/home.txt"),

 # -------------------------------------------------------- life/physical science
 "gbif": dict(
   monthly=None, rate="no fixed rate; the docs say the maximum changes with server load",
   derivation=None, one_time=None, card=False, key="none", confidence=M,
   note="Biodiversity occurrences. Most of the API needs no authentication, and the docs are "
        "explicit that the tolerated rate moves with load, so no number is quoted.",
   quote="Most use of the GBIF API does not require authentication.",
   url="https://techdocs.gbif.org/en/openapi/", snap="gbif/docs.txt"),
 "uniprot": dict(
   monthly=518400000, rate="200 requests/second/user", derivation="200/s x 2,592,000 s/month = 518,400,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="Protein knowledge base. The highest published rate in this set; the number comes from the "
        "Proteins API documentation page.",
   quote="We limit your requests to 200 requests/second/user.",
   url="https://www.ebi.ac.uk/proteins/api/doc/", snap="uniprot/r2.txt"),
 "pdb": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key="none", confidence=L,
   note="Protein structures. The data API answers keyless per entry; no rate page was captured.",
   quote="", url="", snap=""),
 "ensembl": dict(
   monthly=None, rate="no published quota captured; the REST root documents endpoints only",
   derivation=None, one_time=None, card=False, key="none", confidence=L,
   note="Genome browser REST. Answers keyless; the captured documentation lists endpoints without a "
        "rate statement.",
   quote="Ensembl Rest API - Ensembl REST API Endpoints",
   url="https://rest.ensembl.org/", snap="ensembl/docs.txt"),
 "chembl": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key="none", confidence=L,
   note="Bioactivity database. Answers keyless with JSON or XML; the captured pages document "
        "parameters rather than rates.",
   quote="Because there is a limitation of how long a URL can be it's often more convenient to use POST requests instead.",
   url="https://chembl.gitbook.io/chembl-interface-documentation/web-services", snap="chembl/r1.txt"),
 "pubchem": dict(
   monthly=None, rate="no published quota captured; the docs page returned a bot check to this client",
   derivation=None, one_time=None, card=False, key="none", confidence=L,
   note="Chemical compounds. The PUG REST endpoint answers keyless in the probe, but the captured "
        "documentation page is a reCAPTCHA interstitial, so no number is claimed.",
   quote="", url="", snap=""),
 "biostudies": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key="none", confidence=L,
   note="EBI study archive. Answers keyless; the captured help page is navigation chrome.",
   quote="", url="", snap=""),
 "ebisearch": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key="none", confidence=L,
   note="EBI-wide search. The REST endpoint returns a large JSON domain catalogue keyless.",
   quote="", url="", snap=""),
 "ols": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key="none", confidence=L,
   note="Ontology lookup. Answers keyless; the captured help page is a short landing page.",
   quote="", url="", snap=""),
 "biomodels": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key="none", confidence=M,
   note="Systems-biology models. The site states the mission is freely accessible models; the API "
        "answers keyless.",
   quote="Our mission is to provide the systems modelling community with reproducible, high-quality, freely accessible models published in the scientific literature.",
   url="https://www.ebi.ac.uk/biomodels/", snap="biomodels/home.txt"),
 "obis": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key="none", confidence=L,
   note="Ocean biodiversity. The v3 API answers keyless; the captured landing page is a stub.",
   quote="", url="", snap=""),
 "idigbio": dict(
   monthly=None, rate="anonymous calls allowed; authenticating raises the limit",
   derivation=None, one_time=None, card=False, key="none", confidence=M,
   note="Natural-history specimens. The wiki documents the v2 search API and asks users to join a "
        "mailing list so changes can be announced; no call rate is published, and the "
        "loading/limits page could not be captured as text.",
   quote="It uses technology and patterns common in other parts of iDigBio to build a wrapper around the full Elasticsearch API, exposing a minimal subset.",
   url="https://github.com/iDigBio/idigbio-search-api/wiki", snap="idigbio/docs.txt"),
 "inaturalist": dict(
   monthly=None, rate="no published quota captured; the recommendations page returned 403",
   derivation=None, one_time=None, card=False, key="none", confidence=L,
   note="Citizen-science observations. The API answers keyless; the recommended-practices page "
        "could not be captured from this client.",
   quote="All iNaturalist observations are open and freely available",
   url="https://www.inaturalist.org/", snap="inaturalist/home.txt"),
 "osti": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key="none", confidence=M,
   note="US DOE science and technical reports. The API documents its resources but no rate.",
   quote="The API is built on a REST architecture, providing predictable URLs that make writing applications easy.",
   url="https://www.osti.gov/api/v1/docs", snap="osti/docs.txt"),
 "ntrs": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key="none", confidence=M,
   note="NASA technical reports. The site states the content is publicly available; the API "
        "answers keyless.",
   quote="The NASA Technical Reports Server (NTRS) provides access to NASA metadata records, full-text online documents, images, and videos.",
   url="https://ntrs.nasa.gov/", snap="ntrs/home.txt"),
 "cds-cern": dict(
   monthly=None, rate="no published quota captured; the site now runs an Anubis proof-of-work check",
   derivation=None, one_time=None, card=False, key=None, confidence=L,
   note="CERN Document Server. The search endpoint answered after a delay, but the captured pages "
        "are the Anubis interstitial, so the practical route is the API rather than the HTML site.",
   quote="You are seeing this because the administrator of this website has set up Anubis to protect the server",
   url="https://cds.cern.ch/help/hacking", snap="cds-cern/docs.txt"),
 "jstage": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key="none", confidence=M,
   note="Japanese science and technology journals. WebAPI returns XML metadata keyless.",
   quote="J-STAGE WebAPI is an application programming interface (API) that enables users to retrieve metadata for J-STAGE content in XML format.",
   url="https://www.jstage.jst.go.jp/static/pages/JstageServices/TAB3/-char/en", snap="jstage/docs.txt"),
 "repec": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key=None, confidence=L,
   note="Economics bibliography. The IDEAS search page answers HTML, not JSON, so it is not a "
        "clean gateway target.",
   quote="IDEAS is the largest bibliographic database dedicated to Economics and available freely on the Internet.",
   url="https://ideas.repec.org/", snap="repec/docs.txt"),

 # ------------------------------------------------------- publishers and patents
 "elsevier": dict(
   monthly=None, rate="API key plus an entitlement per product; no free allowance published",
   derivation=None, one_time=None, card=None, key="paid", confidence=M,
   note="Scopus and ScienceDirect. The docs say plainly that holding a key does not grant access to "
        "content, which is the key distinction from the open APIs above.",
   quote="Registering for or holding an API key does not by itself grant access to Elsevier data or content.",
   url="https://dev.elsevier.com/", snap="elsevier/docs.txt"),
 "springer": dict(
   monthly=None, rate="API key required; higher rate limits are a paid feature", derivation=None,
   one_time=None, card=None, key="paid", confidence=M,
   note="Springer Nature. Has a separate Open Access API that is free for open-access content; the "
        "general metadata API needs a key.",
   quote="Open Access API Retrieve full-text content from our open access publications, empowering your research with unrestricted access to valuable insights.",
   url="https://dev.springernature.com/", snap="springer/docs.txt"),
 "wiley": dict(
   monthly=None, rate="TDM API token required; no free allowance captured", derivation=None,
   one_time=None, card=None, key="paid", confidence=L,
   note="Text and data mining endpoint. Answers 400 without a token; the captured pages are "
        "marketing copy.",
   quote="", url="", snap=""),
 "ieee": dict(
   monthly=None, rate="API key required; the docs page did not state a free quota",
   derivation=None, one_time=None, card=None, key="apply", confidence=M,
   note="IEEE Xplore metadata API. Answers 403 without a key. Up to 25 DOIs per metadata call.",
   quote="Digital Object Identifier (DOI) API Query up to 25 DOI (Digital Object Identifier) numbers and retrieve metadata records including abstracts.",
   url="https://developer.ieee.org/docs", snap="ieee/docs.txt"),
 "epo-ops": dict(
   monthly=None, rate="OAuth credentials required; published free quota is per-registered-user and "
                      "was not captured",
   derivation=None, one_time=None, card=False, key="apply", confidence=L,
   note="European Patent Office Open Patent Services. Answers 403 without credentials; the "
        "developer portal is free to register but no call quota survived capture.",
   quote="", url="", snap=""),
 "patentsview": dict(
   monthly=None, rate="API key required; the docs page rendered as an application shell",
   derivation=None, one_time=None, card=None, key="apply", confidence=L,
   note="US patent data. The endpoint answered HTML rather than JSON to the probe, so it is "
        "recorded as unverified.",
   quote="", url="", snap=""),
 "uspto-ibd": dict(
   monthly=None, rate="no published quota captured; the API answered HTML rather than JSON",
   derivation=None, one_time=None, card=None, key=None, confidence=L,
   note="USPTO Open Data Portal. Recorded as unverified: the endpoint returned a single-page "
        "application shell.",
   quote="", url="", snap=""),
 "jstor-constellate": dict(
   monthly=None, rate="not established; the API host did not resolve", derivation=None,
   one_time=None, card=None, key=None, confidence=L,
   note="JSTOR's text-analysis service. Recorded as unverified.",
   quote="", url="", snap=""),

 # --------------------------------------------------------- museums and images
 "openverse": dict(
   monthly=None, rate="anonymous calls allowed; the API publishes no quota in the captured pages",
   derivation=None, one_time=None, card=False, key="none", confidence=M,
   note="Openly licensed images and audio, aggregated across sources. Answers keyless.",
   quote="", url="https://api.openverse.org/v1/", snap=""),
 "met-museum": dict(
   monthly=207360000, rate="80 requests/second; no registration or API key",
   derivation="80/s x 2,592,000 s/month = 207,360,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="The Met's collection API. Publishes the highest per-second rate of any museum API here and "
        "explicitly needs no key.",
   quote="At this time, we do not require API users to register or obtain an API key to use the service.",
   url="https://metmuseum.github.io/", snap="met-museum/docs.txt"),
 "artic": dict(
   monthly=2592000, rate="anonymous callers throttled to 60 requests/minute; each IP is one user",
   derivation="60/min x 1,440 x 30 = 2,592,000 calls/month ceiling",
   one_time=None, card=False, key="none", confidence=H,
   note="Art Institute of Chicago. Says outright that the API works without authentication and "
        "publishes the anonymous throttle.",
   quote="You may access our API without authentication.",
   url="https://api.artic.edu/docs/", snap="artic/docs.txt"),
 "cleveland-art": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key="none", confidence=M,
   note="Cleveland Museum of Art open-access API. Answers keyless, and the whole dataset is also "
        "offered as a download, which sidesteps rate limits entirely.",
   quote="If you do not wish to use our API, you can obtain the complete and current dataset in JSON or CSV format from our GitHub repository .",
   url="https://openaccess-api.clevelandart.org/", snap="cleveland-art/docs.txt"),
 "id-loc": dict(
   monthly=None, rate="not established — the search endpoint returned 403", derivation=None,
   one_time=None, card=False, key=None, confidence=L,
   note="Library of Congress linked-data service. Recorded as unverified.",
   quote="", url="", snap=""),
 "dnb-sru": dict(
   monthly=None, rate="SRU service; data free of charge under CC0", derivation=None,
   one_time=None, card=False, key="none", confidence=M,
   note="German National Library. The data licence is explicit; no call rate is published.",
   quote="All bibliographic data from the German National Library and the authority data from the Integrated Authority File is available free of charge for general use",
   url="https://www.dnb.de/EN/Professionell/Metadatendienste/metadatendienste_node.html",
   snap="dnb-sru/docs.txt"),
 "k10plus-sru": dict(
   monthly=None, rate="SRU service; no published call quota", derivation=None, one_time=None,
   card=False, key="none", confidence=L,
   note="K10plus union catalogue. The SRU endpoint answers; the captured page is a short index.",
   quote="", url="", snap=""),
 "nb-no": dict(
   monthly=None, rate="no published quota captured", derivation=None, one_time=None, card=False,
   key=None, confidence=L,
   note="National Library of Norway. The catalogue API answers keyless; the captured root is a "
        "link stub.",
   quote="", url="", snap=""),
 "finna": dict(
   monthly=None, rate="not established — the API returned 403 to this client", derivation=None,
   one_time=None, card=False, key=None, confidence=L,
   note="Finnish library search. Recorded as unverified.",
   quote="", url="", snap=""),
 "viaf": dict(
   monthly=None, rate="not established; the data page returned 403", derivation=None,
   one_time=None, card=False, key=None, confidence=L,
   note="Virtual International Authority File. The AutoSuggest endpoint answered keyless; OCLC's "
        "developer page documents the API but states no rate in the captured text.",
   quote="With the VIAF API, you can: Search for authority data by keyword, local name, preferred name form, title, source, or control number of source records",
   url="https://www.oclc.org/developer/api/oclc-apis/viaf.en.html", snap="viaf/docs.txt"),
}


def basis_kind(f):
    """Classify how the monthly figure was obtained, so the reports can say it plainly."""
    if not f["monthly"]:
        return None
    d = f["derivation"] or ""
    if "published monthly figure" in d:
        return "published-monthly"
    if "published daily quota" in d:
        return "published-daily"
    if "daily budget" in d:
        return "daily-budget"
    return "rate-ceiling"


def main():
    def load(name):
        path = os.path.join(DATA, name)
        if not os.path.exists(path):
            return {}
        with open(path) as fh:
            return json.load(fh)

    cands = load("candidates.json")["providers"]
    probes = load("probes.json")
    llms = load("llms.json")
    out = []
    for p in cands:
        slug = p["slug"]
        f = FACTS.get(slug)
        if f is None:
            raise SystemExit(f"no facts entry for candidate {slug}")
        rec = {
            "slug": slug, "name": p["name"], "category": p["category"],
            "home": p.get("home") or "", "docs": p.get("docs") or "",
            "pricing": p.get("pricing") or "", "api": p.get("api") or "",
            "llms": (llms.get(slug) or {}).get("url"),
            "llms_reason": (llms.get(slug) or {}).get("reason"),
            "monthly_calls": f["monthly"], "basis_kind": basis_kind(f),
            "rate": f["rate"],
            "derivation": f["derivation"], "one_time": f["one_time"],
            "card": f["card"], "key": f["key"], "confidence": f["confidence"],
            "note": f["note"],
            "evidence": [{"quote": f["quote"], "url": f["url"],
                          "snapshot": ("data/snapshots/" + f["snap"]) if f["snap"] else ""}]
                        if f["quote"] else [],
            "probe": probes.get(slug, {}),
        }
        out.append(rec)
    with open(os.path.join(DATA, "facts.json"), "w") as fh:
        json.dump(out, fh, indent=1)
        fh.write("\n")
    nums = [r for r in out if r["monthly_calls"]]
    print(f"facts.json: {len(out)} providers, {len(nums)} with a documented call figure")
    print(f"  confidence: " + ", ".join(
        f"{c}={sum(1 for r in out if r['confidence']==c)}" for c in (H, M, L, N)))
    print(f"  total monthly, one account each: {sum(r['monthly_calls'] for r in nums):,}")


if __name__ == "__main__":
    main()
