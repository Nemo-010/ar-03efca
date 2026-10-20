# Post-analysis

All figures derive from `data/facts.json` (captured 2026-10-20). Nothing here is an estimate unless the sentence says so.

## 1. Total documented volume, one account and five

Of the providers with a number, **three publish a quota** — one monthly, one daily, and one as a daily dollar budget with a published price list. The other 17 publish a *rate* (requests per second or minute), and their monthly figure is arithmetic on that rate, not a promise. The two groups are kept apart because they mean different things.

### 1a. Published quotas

| Provider | Per account /mo | ×5 | What the provider actually publishes |
|----------|---:|---:|-------|
| OpenAlex | 300,000 | **1,500,000** | 10,000 list+filter calls per $1 of daily budget x 30 = 300,000 calls/month; a search costs 10x a |
| NASA ADS | 150,000 | **750,000** | 5,000/day x 30 = 150,000 calls/month (published daily quota) |
| US National Archives Catalog | 10,000 | **50,000** | published monthly figure, not a rate conversion |
| **Subtotal** | **460,000** | **2,300,000** | |

These three are the only numbers in this inventory that a caller can plan against without assuming saturation. NARA and ADS state the quota outright; OpenAlex publishes a daily dollar budget and a price per operation, so the call count follows from two published facts.

### 1b. Rate ceilings

| Provider | Rate published | Ceiling /mo | ×5 |
|----------|----------------|---:|---:|
| UniProt | 200 requests/second/user | 518,400,000 | **2,592,000,000** |
| The Met Collection API | 80 requests/second; no registration or API key | 207,360,000 | **1,036,800,000** |
| Research Organization Registry | 2,000 requests per 5 minutes per IP address; no registration | 17,280,000 | **86,400,000** |
| Crossref REST API | 5 requests/second (public pool), 10/s polite pool with a mailto, 150/s with a Plus k | 12,960,000 | **64,800,000** |
| Arquivo.pt | 250 requests/60s (full-text & URL search); 400 requests/60s (image, Memento) | 10,800,000 | **54,000,000** |
| OpenCitations Index | 180 requests/minute per IP address | 7,776,000 | **38,880,000** |
| PubMed E-utilities | 3 requests/second without a key; 10/s with an NCBI API key | 7,776,000 | **38,880,000** |
| INSPIRE-HEP | 15 requests per 5-second window per IP address | 7,776,000 | **38,880,000** |
| DOAJ | 2 requests/second on all API routes, with a 5-request burst queue | 5,184,000 | **25,920,000** |
| DataCite REST API | 500 requests/5min unidentified, 1,000 identified (mailto), 3,000 authenticated | 4,320,000 | **21,600,000** |
| Open Library | 1 request/second unidentified; 3 requests/second with a User-Agent carrying an email | 2,592,000 | **12,960,000** |
| Zenodo | guest 60 requests/minute and 2,000/hour; authenticated 100/minute and 5,000/hour | 2,592,000 | **12,960,000** |
| Art Institute of Chicago API | anonymous callers throttled to 60 requests/minute; each IP is one user | 2,592,000 | **12,960,000** |
| CORE | one batch request or five single requests per 10 seconds, without registration | 1,296,000 | **6,480,000** |
| Dimensions | 30 requests/minute per IP; free access only for eligible research projects | 1,296,000 | **6,480,000** |
| Library of Congress JSON API | 20 requests/minute for the JSON/YAML API; 150/min for text and image services | 864,000 | **4,320,000** |
| arXiv API | no more than one request every three seconds, single connection | 864,000 | **4,320,000** |
| **Subtotal** | | **811,728,000** | **4,058,640,000** |

A ceiling is what the published rate permits if a client called continuously for 30 days. No real client does that, and several of these docs ask callers not to.

### 1c. The headline number, and why it is nearly meaningless

Adding the two groups gives **812,188,000 calls/month** for one account each and **4,060,940,000** for five. That total is dominated by two rows:

- UniProt: 518,400,000 (63.8% of the total) — 200/s x 2,592,000 s/month = 518,400,000 calls/month ceiling
- The Met Collection API: 207,360,000 (25.5% of the total) — 80/s x 2,592,000 s/month = 207,360,000 calls/month ceiling

Both are per-second rates on scientific data APIs. Dropping them leaves **86,428,000 calls/month**, and that figure is the one worth remembering. Three reasons the total overstates what a real pipeline gets:

1. **A rate is not a quota.** Nothing obliges a provider to serve a client that saturates its published rate for a month, and several of these docs say so.
2. **Shared pools.** Semantic Scholar's 1,000 requests/second is shared by every unauthenticated caller in the world, so it is excluded from the sum entirely rather than counted as one caller's allowance.
3. **Per-key gates.** NARA's quota and Dimensions' eligibility rule mean a second account needs a second approval, so the ×5 column is arithmetic rather than access.

### 1d. Ceiling by category

| Category | With a figure | Ceiling /mo, 1 account | ×5 |
|---|---:|---:|---:|
| web-archive | 2 | 10,810,000 | 54,050,000 |
| aggregator | 4 | 213,408,000 | 1,067,040,000 |
| scholarly-graph | 7 | 45,228,000 | 226,140,000 |
| index | 5 | 21,750,000 | 108,750,000 |
| repository | 1 | 2,592,000 | 12,960,000 |
| data-api | 1 | 518,400,000 | 2,592,000,000 |

### 1e. One-time grants

None of the captured pages in this set offer a one-time credit grant. That is a real difference from commercial scraping APIs: public and academic infrastructure publishes a standing rate instead of a trial.

## 2. Friction: what it takes to make the first call

| Friction | Count | Meaning | Examples |
|---|---:|---|---|
| keyless | 64 | works with no key at all | Wayback Machine CDX, Wayback Availability API, Internet Archive Metadata API, Internet Archive Scholar / fatcat, Common Crawl Index, Arquivo.pt |
| free key | 14 | sign-up, no payment | Conifer (Rhizome), Europeana, Digital Public Library of America, DigitalNZ, Smithsonian Open Access, OpenAlex |
| key on application | 10 | a human approves the key | Perma.cc, US National Archives Catalog, Trove (National Library of Australia), BASE (Bielefeld), Dimensions, Altmetric |
| paid only | 4 | no free API tier found | Lens.org Scholarly API, Elsevier Scopus / ScienceDirect API, Springer Nature API, Wiley TDM API |
| not established | 25 | capture did not settle it | Wayback Save Page Now, Internet Archive Full-Text Search, UK Web Archive, Memento TimeTravel aggregator, UK National Archives Discovery, Archives Portal Europe, SNAC Cooperative, Crossref Event Data |

**Payment cards demanded for the free tier: 0.** None of the captured pages requires a card to reach a free academic or archival API.

The gated ones matter more than the count suggests. Perma.cc, US National Archives Catalog, Trove (National Library of Australia), BASE (Bielefeld), Dimensions, Altmetric, Sherpa Romeo, IEEE Xplore API, EPO Open Patent Services, PatentsView all require an application or an institutional entitlement, which means they cannot be added to a pipeline by a script — a human has to ask. Two of them publish a call figure beyond the gate (US National Archives Catalog, Dimensions), which is what makes filing the application worthwhile; the rest publish none.

## 3. What the endpoints actually answered

| Verdict | Count | What it means |
|---|---:|---|
| ok | 79 | 200 with a machine-readable body |
| ok-html | 8 | 200 but an HTML page, not the API |
| auth | 13 | 401/403 with a JSON or plain refusal — a key is required |
| bot-wall | 4 | 403/503 carrying a Cloudflare/Anubis/reCAPTCHA challenge |
| blocked | 1 | 429/503 — refused at probe time |
| not-found | 2 | 404 — the documented path is gone |
| error | 10 | no answer: DNS, TLS or timeout |

87 of 117 endpoints answered an unauthenticated call. The most common failure is not a paywall: it is a bot interstitial or an application shell, which returns 200 with no usable body. That is why the probe records `ok-html` separately from `ok`.

Slowest endpoints in the probe (one request each, so this is a floor, not a benchmark):

| Provider | ms | Verdict |
|---|---:|---|
| Internet Archive Scholar / fatcat | 25,356 | no answer |
| Crossref Event Data | 25,058 | no answer |
| RePEc / IDEAS | 10,570 | 200 HTML |
| Internet Archive Metadata API | 3,299 | 200 JSON |
| re3data | 2,810 | 200 JSON |
| ChEMBL | 2,416 | 200 JSON |
| iDigBio | 2,357 | 200 JSON |
| Archives Portal Europe | 2,169 | 404 |

## 4. Where the free capacity actually is

Counting only providers with a published figure, by category:

| Category | With a figure | Total in category | Share |
|---|---:|---:|---:|
| web-archive | 2 | 18 | 11% |
| aggregator | 4 | 23 | 17% |
| scholarly-graph | 7 | 18 | 39% |
| index | 5 | 24 | 21% |
| repository | 1 | 13 | 8% |
| data-api | 1 | 13 | 8% |
| publisher | 0 | 8 | 0% |

Web archives are the least quantified category in this inventory: the Wayback CDX server, the single largest index of the web's past, publishes no call quota at all. The well-quantified categories are bibliographic indexes and life-science data, where the funder pays for the infrastructure and the API is the product.

llms.txt is barely used in this space: 7 of 117 providers serve a verified markdown index at a canonical path (Open Library, OpenAlex, DataCite REST API, Research Organization Registry, Scite, OpenReview, ChEMBL). Academic and archival infrastructure predates that convention, and several hosts that do return 200 at `/llms.txt` serve an HTML shell there, which the verifier rejects.

## 5. A stack built only from verified figures

If the requirement is 'documented allowance, no card, works today', the subset is small and specific:

| Need | Provider | Why this one |
|---|---|---|
| scholarly metadata and citation graph | OpenAlex | published price list, free single-entity lookups, $1/day budget |
| DOI metadata | Crossref REST API | 5/s public, 10/s with a mailto, no key needed |
| research-data DOIs | DataCite REST API | 500 per 5 min unidentified, keyless |
| historical page state | Wayback Machine CDX | the index of record; no quota to exceed |
| newspapers and print collections | Library of Congress JSON API | explicit 20/min rate table with the block duration — note the probe hit a Cloudflare wall, so expect to identify the client properly |
| book metadata | Open Library | 1/s unidentified, 3/s with a contact header |
| open-access journal articles | DOAJ | 2/s published, keyless |
| biomedical literature | PubMed E-utilities | 3/s keyless, 10/s with a free NCBI key |
| research data deposits | Zenodo | guest 60/min published per endpoint |
| museum objects and images | The Met Collection API | 80/s, no key, no registration |

The honest summary: **an archival pipeline can be built entirely from keyless, rate-published public APIs**, and the binding constraint is not quota but politeness — arXiv's one request every three seconds is the slowest published rate in the set, and it is slow on purpose.

Two caveats on that table, both measured: the Library of Congress API publishes the cleanest rate table here but answered the probe with a Cloudflare challenge, and OpenAlex's free tier is a dollar a day rather than an unlimited keyless pool. Both are still the right choice for their job; neither is frictionless.

What is *not* in the table is just as informative: none of the 120 providers needs a payment card, none offers a one-time trial credit, and the eight publisher and patent endpoints are the only group where no free call figure exists at all.
