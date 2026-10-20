# Deutsche Nationalbibliothek SRU

- Category: `aggregator` — Library / museum / newspaper aggregators
- Home: https://www.dnb.de/
- Docs: https://www.dnb.de/EN/Professionell/Metadatendienste/metadatendienste_node.html
- Probe endpoint: `https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=openalex&recordSchema=oai_dc&maximumRecords=1`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: SRU service; data free of charge under CC0
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

German National Library. The data licence is explicit; no call rate is published.

## Evidence

> All bibliographic data from the German National Library and the authority data from the Integrated Authority File is available free of charge for general use

Source: https://www.dnb.de/EN/Professionell/Metadatendienste/metadatendienste_node.html  
Snapshot: `data/snapshots/dnb-sru/docs.txt`  

## Live probe

- Request: `GET https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=openalex&recordSchema=oai_dc&maximumRecords=1`
- Result: HTTP 200 in 965 ms — **200 JSON**
- Body starts: `<?xml version="1.0" encoding="UTF-8"?> <searchRetrieveResponse xmlns="http://www.loc.gov/zing/srw/"><version>1.1</version><numberOfRecords>19</numberOfRecords><records><record><rec`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
