# PubMed E-utilities

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://pubmed.ncbi.nlm.nih.gov/
- Docs: https://www.ncbi.nlm.nih.gov/books/NBK25497/
- Probe endpoint: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=openalex&retmode=json&retmax=1`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **7,776,000 calls/month**
- Derivation: 3/s x 2,592,000 s/month = 7,776,000 calls/month ceiling
- Published rate: 3 requests/second without a key; 10/s with an NCBI API key
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

NCBI E-utilities. The 3/s figure is stated in an NLM support article and confirmed by the live response headers, which reported x-ratelimit-limit: 3.

## Evidence

> NCBI E-Utilities API service limits the number of requests per second (rps) to 3.

Source: https://support.nlm.nih.gov/kbArticle/?pn=KA-05317  
Snapshot: `data/snapshots/pubmed/limits2.txt`  

## Live probe

- Request: `GET https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=openalex&retmode=json&retmax=1`
- Result: HTTP 200 in 497 ms — **200 JSON**
- Rate-limit headers: `{"X-Ratelimit-Limit": "3", "X-Ratelimit-Remaining": "2"}`
- Body starts: `{"header":{"type":"esearch","version":"0.3"},"esearchresult":{"count":"160","retmax":"1","retstart":"0","idlist":["42890311"],"translationset":[],"querytranslation":"\"openalex\"[A`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
