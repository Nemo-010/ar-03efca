# Wikidata Query Service

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://query.wikidata.org/
- Docs: https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual
- Probe endpoint: `https://query.wikidata.org/sparql?format=json&query=SELECT%20%3Fitem%20WHERE%20%7B%3Fitem%20wdt%3AP31%20wd%3AQ5%7D%20LIMIT%201`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: 60 seconds of processing time per 60 seconds, per client; 30 error queries/minute
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **high**

## Notes

SPARQL endpoint. The limit is CPU time, not calls, so it cannot be converted to a call count — a cheap query and an expensive one cost the same one call but very different time.

## Evidence

> One client (user agent + IP) is allowed 60 seconds of processing time each 60 seconds

Source: https://query.wikidata.org/  
Snapshot: `data/snapshots/wikidata/docs.txt`  

## Live probe

- Request: `GET https://query.wikidata.org/sparql?format=json&query=SELECT%20%3Fitem%20WHERE%20%7B%3Fitem%20wdt%3AP31%20wd%3AQ5%7D%20LIMIT%201`
- Result: HTTP 200 in 347 ms — **200 JSON**
- Body starts: `{ "head" : { "vars" : [ "item" ] }, "results" : { "bindings" : [ { "item" : { "type" : "uri", "value" : "http://www.wikidata.org/entity/L1742768" } } ] } }`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
