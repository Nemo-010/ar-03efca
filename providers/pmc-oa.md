# PMC Open Access Subset

- Category: `index` — Bibliographic indexes & preprint servers
- Home: https://www.ncbi.nlm.nih.gov/pmc/
- Docs: https://www.ncbi.nlm.nih.gov/pmc/tools/oa-service/
- Probe endpoint: `https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC1000000`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: OAI-PMH and the OA web service; no call quota published
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **medium**

## Notes

Full text for the PMC open-access subset. NLM names the services that may be used for automated retrieval, which matters more than a rate for a gateway.

## Evidence

> The PMC Cloud Service , PMC OAI-PMH Service , E-Utilities and BioC API are the only services that may be used for automated retrieval of PMC content.

Source: https://www.ncbi.nlm.nih.gov/pmc/tools/developers/  
Snapshot: `data/snapshots/pmc-oa/limits2.txt`  

## Live probe

- Request: `GET https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC13900/unicode`
- Result: HTTP 200 in 578 ms — **200 JSON**
- Body starts: `[{"bioctype": "BioCCollection", "source": "PMC", "date": "20260127", "key": "pmc.key", "version": "1.0", "infons": {}, "documents": [{"bioctype": "BioCDocument", "id": "PMC13900", `

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
