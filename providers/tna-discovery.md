# UK National Archives Discovery

- Category: `web-archive` — Web archives & national archive catalogs
- Home: https://discovery.nationalarchives.gov.uk/
- Docs: https://discovery.nationalarchives.gov.uk/API/site/search
- Probe endpoint: `https://discovery.nationalarchives.gov.uk/API/search/records?sps.searchQuery=openalex`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: not established
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

UK National Archives Discovery API answered 200 in the probe, but its help page was not captured and no allowance is claimed.

## Evidence

> It provides brief descriptions of documents and details of their locations in public and private hands.

Source: https://discovery.nationalarchives.gov.uk/  
Snapshot: `data/snapshots/tna-discovery/home.txt`  

## Live probe

- Request: `GET https://discovery.nationalarchives.gov.uk/API/search/records?sps.searchQuery=openalex`
- Result: HTTP 200 in 942 ms — **200 JSON**
- Body starts: `{"records":[],"taxonomySubjects":[],"timePeriods":[],"departments":[],"catalogueLevels":[],"closureStatuses":[],"sources":[],"repositories":[],"heldByReps":[],"referenceFirstLetter`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
