# Ensembl REST

- Category: `data-api` — Life / physical science data APIs
- Home: https://www.ensembl.org/
- Docs: https://rest.ensembl.org/
- Probe endpoint: `https://rest.ensembl.org/lookup/id/ENSG00000139618?content-type=application/json`
- llms.txt: none verified — empty body

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured; the REST root documents endpoints only
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Genome browser REST. Answers keyless; the captured documentation lists endpoints without a rate statement.

## Evidence

> Ensembl Rest API - Ensembl REST API Endpoints

Source: https://rest.ensembl.org/  
Snapshot: `data/snapshots/ensembl/docs.txt`  

## Live probe

- Request: `GET https://rest.ensembl.org/lookup/id/ENSG00000139618?content-type=application/json`
- Result: HTTP 200 in 599 ms — **200 JSON**
- Rate-limit headers: `{"X-RateLimit-Limit": "55000", "X-RateLimit-Period": "3600", "X-RateLimit-Remaining": "54994", "X-RateLimit-Reset": "681"}`
- Body starts: `{"canonical_transcript":"ENST00000380152.8","logic_name":"ensembl_havana_gene_homo_sapiens","biotype":"protein_coding","db_type":"core","source":"ensembl_havana","seq_region_name":`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
