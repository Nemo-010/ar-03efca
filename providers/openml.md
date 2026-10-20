# OpenML

- Category: `repository` — Repositories & research-data archives
- Home: https://www.openml.org/
- Docs: https://www.openml.org/apis
- Probe endpoint: `https://www.openml.org/api/v1/json/data/list/limit/1`
- llms.txt: none verified — not a markdown index (no heading near the top)

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured
- Authentication: ?
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Machine-learning datasets and tasks. The API answers keyless and the documentation states that OpenML is accessible to a wide range of clients; no call rate is published.

## Evidence

> How to use OpenML ¶ OpenML is accessible to a wide range

Source: https://docs.openml.org/  
Snapshot: `data/snapshots/openml/docs.txt`  

## Live probe

- Request: `GET https://www.openml.org/api/v1/json/data/list/limit/1`
- Result: HTTP 200 in 1188 ms — **200 JSON**
- Body starts: `{"data":{"dataset":[ {"did":2, "name":"anneal", "version":1, "status":"active", "format":"ARFF", "md5_checksum":"", "file_id": 1666876, "quality":[ {"name":"MajorityClassSize", "va`

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
