# PubChem PUG REST

- Category: `data-api` — Life / physical science data APIs
- Home: https://pubchem.ncbi.nlm.nih.gov/
- Docs: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest
- Probe endpoint: `https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/aspirin/property/MolecularFormula/JSON`
- llms.txt: none verified — HTTP 404

## Free access

- Documented volume: **no call quota published** in the captured sources
- Published rate: no published quota captured; the docs page returned a bot check to this client
- Authentication: none
- Payment card for the free tier: no
- Evidence confidence: **low**

## Notes

Chemical compounds. The PUG REST endpoint answers keyless in the probe, but the captured documentation page is a reCAPTCHA interstitial, so no number is claimed.

## Live probe

- Request: `GET https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/aspirin/property/MolecularFormula/JSON`
- Result: HTTP 200 in 401 ms — **200 JSON**
- Body starts: `{ "PropertyTable": { "Properties": [ { "CID": 2244, "MolecularFormula": "C9H8O4" } ] } } `

## Measurement note

Generated from `data/facts.json` on 2026-10-20. The probe is one unauthenticated request from one machine: it shows whether the endpoint answers at all, not what the quota is. Re-run `make fetch probe` to refresh.
