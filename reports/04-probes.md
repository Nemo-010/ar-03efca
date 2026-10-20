# Live probe results

One unauthenticated `GET` per documented endpoint, from one machine, on 2026-10-20. This is a different evidence class from the documentation snapshots: it shows whether the endpoint answers a caller with no key, not what the allowance is.

Verdicts: `ok` = 2xx with a machine-readable body; `ok-html` = 2xx but an HTML page rather than the API; `auth` = 401/403 with a plain refusal; `bot-wall` = 403/503 carrying a Cloudflare, Anubis or reCAPTCHA challenge; `blocked` = 429/503; `not-found` = 404; `error` = no answer (DNS, TLS, timeout). The `auth` / `bot-wall` split matters: the first needs a credential, the second needs a browser.

| Provider | Status | Verdict | ms | Rate-limit headers | URL |
|---|---:|---|---:|---|---|
| Altmetric | 403 | needs key | 88 | — | `https://api.altmetric.com/v1/doi/10.1038/nature12373` |
| archive.today | 200 | 200 JSON | 679 | — | `https://archive.ph/timemap/https://openalex.org` |
| Archives Portal Europe | 404 | 404 | 2169 | — | `https://www.archivesportaleurope.net/OAI-PMH/?verb=Identify` |
| Arquivo.pt | 200 | 200 JSON | 717 | `RateLimit-Limit: 250`, `RateLimit-Reset: 60`, `X-RateLimit-Limit: 250` | `https://arquivo.pt/wayback/cdx?url=openalex.org&output=json&limit=2` |
| Art Institute of Chicago API | 200 | 200 JSON | 318 | — | `https://api.artic.edu/api/v1/artworks?limit=1` |
| arXiv API | 200 | 200 JSON | 205 | — | `https://export.arxiv.org/api/query?search_query=all:openalex&max_results=1` |
| BASE (Bielefeld) | 200 | 200 JSON | 1910 | — | `https://api.base-search.net/cgi-bin/BaseHttpSearchInterface.fcgi?func=PerformSearch&quer` |
| BioModels | 200 | 200 JSON | 1456 | — | `https://www.ebi.ac.uk/biomodels/search?query=openalex&format=json` |
| bioRxiv API | 200 | 200 JSON | 692 | — | `https://api.biorxiv.org/details/biorxiv/10.1101/2020.09.09.20191205` |
| BioStudies (EBI) | 200 | 200 JSON | 601 | — | `https://www.ebi.ac.uk/biostudies/api/v1/search?query=openalex&pageSize=1` |
| CERN Document Server | 200 | 200 HTML | 514 | — | `https://cds.cern.ch/search?p=openalex&of=recjson&rg=1` |
| ChEMBL | 200 | 200 JSON | 2416 | — | `https://www.ebi.ac.uk/chembl/api/data/target.json?limit=1` |
| Chronicling America | 404 | 404 | 322 | — | `https://chroniclingamerica.loc.gov/search/pages/results/?andtext=openalex&format=json` |
| Cleveland Museum of Art Open Access API | 200 | 200 JSON | 212 | — | `https://openaccess-api.clevelandart.org/api/artworks/?q=openalex&limit=1` |
| ClinicalTrials.gov | 200 | 200 JSON | 461 | — | `https://clinicaltrials.gov/api/v2/studies?pageSize=1` |
| Common Crawl Index | 200 | 200 JSON | 286 | — | `https://index.commoncrawl.org/collinfo.json` |
| Conifer (Rhizome) | 200 | 200 JSON | 265 | — | `https://conifer.rhizome.org/api/v1/` |
| CORE | 200 | 200 JSON | 919 | `x-ratelimit-limit: 10`, `x-ratelimit-remaining: 9`, `x-ratelimit-retry-after: 2026-10-20T02:48:32+0000` | `https://api.core.ac.uk/v3/search/works/?q=openalex&limit=1` |
| Crossref Event Data | 0 | no answer | 25058 | — | `https://api.eventdata.crossref.org/v1/events?obj-id=10.1038/nature12373&rows=1` |
| Crossref REST API | 200 | 200 JSON | 224 | `x-rate-limit-interval: 1s`, `x-rate-limit-limit: 5` | `https://api.crossref.org/works/10.1038/nature12373` |
| DataCite REST API | 200 | 200 JSON | 1083 | — | `https://api.datacite.org/dois?query=openalex&page%5Bsize%5D=1` |
| DataONE | 200 | 200 JSON | 693 | — | `https://cn.dataone.org/cn/v2/query/solr/?q=openalex&rows=1&wt=json` |
| DataverseNL | 200 | 200 JSON | 831 | — | `https://dataverse.nl/api/search?q=openalex` |
| dblp computer science bibliography | 202 | 200 HTML | 519 | — | `https://dblp.org/search/publ/api?q=openalex&format=json&h=1` |
| Deutsche Nationalbibliothek SRU | 200 | 200 JSON | 965 | — | `https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=openalex&reco` |
| Digital Public Library of America | 403 | needs key | 446 | — | `https://api.dp.la/v2/items?q=openalex` |
| DigitalNZ | 200 | 200 JSON | 1314 | — | `https://api.digitalnz.org/v3/records.json?text=openalex` |
| Dimensions | 0 | no answer | 27 | — | `https://api.dimensions.ai/v2/publications?search_text=openalex` |
| DOAB | 403 | needs key | 509 | — | `https://directory.doabooks.org/rest/search?query=openalex` |
| DOAJ | 200 | 200 JSON | 369 | — | `https://doaj.org/api/search/articles/openalex?pageSize=1` |
| Dryad | 200 | 200 JSON | 455 | — | `https://datadryad.org/api/v2/search?q=openalex&per_page=1` |
| EBI Search | 200 | 200 JSON | 731 | — | `https://www.ebi.ac.uk/ebisearch/ws/rest?query=openalex&format=json` |
| Elsevier Scopus / ScienceDirect API | 401 | needs key | 331 | — | `https://api.elsevier.com/content/search/scopus?query=openalex` |
| EMBL-EBI Ontology Lookup Service | 200 | 200 JSON | 644 | — | `https://www.ebi.ac.uk/ols4/api/search?q=openalex&rows=1` |
| Ensembl REST | 200 | 200 JSON | 599 | `X-RateLimit-Limit: 55000`, `X-RateLimit-Period: 3600`, `X-RateLimit-Remaining: 54994` | `https://rest.ensembl.org/lookup/id/ENSG00000139618?content-type=application/json` |
| EPO Open Patent Services | 403 | needs key | 1096 | — | `https://ops.epo.org/3.2/rest-services/published-data/search?q=openalex` |
| Europe PMC | 200 | 200 JSON | 794 | — | `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=openalex&format=json&pageS` |
| Europeana | 200 | 200 JSON | 386 | `ratelimit: "project";r=993901;t=691`, `ratelimit-policy: "project";q=1000000;w=3600` | `https://api.europeana.eu/record/v2/search.json?query=openalex&wskey=api2demo&rows=1` |
| Figshare | 200 | 200 JSON | 737 | — | `https://api.figshare.com/v2/articles?page_size=1` |
| Finna (Finnish libraries) | 403 | bot wall | 79 | — | `https://api.finna.fi/v1/search?lookfor=openalex&limit=1` |
| Gallica (BnF) | 403 | bot wall | 368 | — | `https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&query=gallica%20all%20%2` |
| GBIF | 200 | 200 JSON | 1292 | — | `https://api.gbif.org/v1/occurrence/search?q=openalex&limit=1` |
| HAL Open Archive | 200 | 200 JSON | 540 | — | `https://api.archives-ouvertes.fr/search/?q=openalex&rows=1&wt=json` |
| Harvard Dataverse | 200 | 200 JSON | 388 | — | `https://dataverse.harvard.edu/api/search?q=openalex&per_page=1` |
| HathiTrust Bibliographic API | 200 | 200 JSON | 438 | — | `https://catalog.hathitrust.org/api/volumes/brief/json/oclc:424023` |
| Hugging Face Hub | 200 | 200 JSON | 186 | `RateLimit: "api";r=498;t=123`, `RateLimit-Policy: "fixed window";"api";q=500;w=300` | `https://huggingface.co/api/datasets?limit=1` |
| id.loc.gov (LC Linked Data) | 403 | bot wall | 76 | — | `https://id.loc.gov/search/?q=openalex&format=json` |
| iDigBio | 200 | 200 JSON | 2357 | — | `https://search.idigbio.org/v2/search/records/?q=openalex&limit=1&fields=uuid` |
| IEEE Xplore API | 403 | needs key | 357 | — | `https://ieeexploreapi.ieee.org/api/v1/search/articles?querytext=openalex` |
| iNaturalist | 200 | 200 JSON | 617 | — | `https://api.inaturalist.org/v1/observations?per_page=1` |
| INSPIRE-HEP | 200 | 200 JSON | 547 | — | `https://inspirehep.net/api/literature?q=openalex&size=1` |
| Internet Archive Full-Text Search | 0 | no answer | 165 | — | `https://ia-fts.archive.org/api/v1/search/hits?q=openalex&size=1` |
| Internet Archive Metadata API | 200 | 200 JSON | 3299 | — | `https://archive.org/metadata/wikipedia` |
| Internet Archive Scholar / fatcat | 0 | no answer | 25356 | — | `https://api.fatcat.wiki/v0/release/lookup?doi=10.1038/nature12373` |
| J-STAGE | 200 | 200 JSON | 968 | — | `https://api.jstage.jst.go.jp/searchapi/do?service=3&q=openalex&count=1` |
| JSTOR / Constellate | 0 | no answer | 126 | — | `https://api.constellate.org/` |
| K10plus SRU | 200 | 200 JSON | 834 | — | `https://sru.k10plus.de/gvk?version=1.1&operation=searchRetrieve&query=pica.all%3Dopenale` |
| LA Referencia | 0 | no answer | 27 | — | `https://api.lareferencia.info/v1/search?query=openalex` |
| Lens.org Scholarly API | 401 | needs key | 382 | — | `https://api.lens.org/scholarly/search` |
| Library of Congress JSON API | 403 | bot wall | 96 | — | `https://www.loc.gov/books/?q=openalex&fo=json` |
| medRxiv API | 200 | 200 JSON | 657 | — | `https://api.biorxiv.org/details/medrxiv/10.1101/2020.09.09.20191205` |
| Memento TimeTravel aggregator | 0 | no answer | 76 | — | `http://timetravel.mementoweb.org/api/json/2020/https://openalex.org` |
| NASA ADS | 401 | needs key | 339 | — | `https://api.adsabs.harvard.edu/v1/search/query?q=openalex` |
| NASA NTRS | 200 | 200 JSON | 708 | `X-RateLimit-Limit: 500`, `X-RateLimit-Remaining: 499`, `X-RateLimit-Reset: 1792464778` | `https://ntrs.nasa.gov/api/citations/search?q=openalex&page.size=1` |
| National Library of Norway API | 200 | 200 JSON | 1067 | — | `https://api.nb.no/catalog/v1/items?q=openalex&size=1` |
| NDLTD Union Catalog | 503 | 429/503 | 734 | `Retry-After: 86400` | `https://union.ndltd.org/OAI-PMH?verb=Identify` |
| OAPEN Library | 403 | needs key | 538 | — | `https://library.oapen.org/rest/search?query=openalex&expand=metadata&limit=1` |
| OAPEN REST API | 200 | 200 HTML | 864 | — | `https://api.oapen.org/search?query=openalex` |
| OBIS | 200 | 200 JSON | 885 | — | `https://api.obis.org/v3/occurrence?size=1` |
| Open Library | 200 | 200 JSON | 580 | — | `https://openlibrary.org/search.json?q=openalex&limit=1` |
| OpenAIRE Explore | 200 | 200 JSON | 707 | `x-ratelimit-limit: 7199`, `x-ratelimit-used: 18` | `https://api.openaire.eu/search/publications?keywords=openalex&size=1` |
| OpenAIRE Graph | 200 | 200 JSON | 678 | `x-ratelimit-limit: 7199`, `x-ratelimit-used: 16` | `https://api.openaire.eu/graph/v1/researchProducts?search=openalex&pageSize=1` |
| OpenAIRE Search API | 200 | 200 JSON | 830 | `x-ratelimit-limit: 7199`, `x-ratelimit-used: 17` | `https://api.openaire.eu/search/publications?title=openalex&size=1` |
| OpenAlex | 200 | 200 JSON | 595 | `X-RateLimit-Cost-USD: 0.0001`, `X-RateLimit-Credits-Used: 1`, `X-RateLimit-Limit: 1000` | `https://api.openalex.org/works?filter=doi:10.1038/nature12373` |
| OpenCitations Index | 200 | 200 JSON | 2149 | — | `https://opencitations.net/index/api/v2/citations/doi:10.1038/nature12373` |
| OpenML | 200 | 200 JSON | 1188 | — | `https://www.openml.org/api/v1/json/data/list/limit/1` |
| OpenReview | 200 | 200 HTML | 644 | — | `https://api2.openreview.net/notes?limit=1` |
| Openverse | 200 | 200 JSON | 97 | `x-ratelimit-available-anon_burst: 19`, `x-ratelimit-available-anon_sustained: 199`, `x-ratelimit-limit-anon_burst: 20/min` | `https://api.openverse.org/v1/images/?q=openalex&page_size=1` |
| ORCID Public API | 200 | 200 JSON | 251 | — | `https://pub.orcid.org/v3.0/expanded-search/?q=openalex&rows=1` |
| OSF (Open Science Framework) | 200 | 200 JSON | 761 | — | `https://api.osf.io/v2/nodes/?page%5Bsize%5D=1` |
| OSTI.gov | 200 | 200 JSON | 353 | — | `https://www.osti.gov/api/v1/records?q=openalex&rows=1` |
| Papers with Code | 200 | 200 HTML | 1130 | `RateLimit: "pages";r=98;t=122`, `RateLimit-Policy: "fixed window";"pages";q=100;w=300` | `https://paperswithcode.com/api/v1/papers/?items_per_page=1` |
| PatentsView | 200 | 200 HTML | 1208 | — | `https://api.patentsview.org/patents/query?q=%7B%22_gte%22%3A%7B%22patent_date%22%3A%2220` |
| Perma.cc | 200 | 200 JSON | 450 | — | `https://api.perma.cc/v1/public/archives/?limit=1` |
| PMC ID Converter | 200 | 200 JSON | 737 | — | `https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids=PMC13900&format=json` |
| PMC Open Access Subset | 200 | 200 JSON | 578 | — | `https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC13900/unicod` |
| Project Gutenberg (Gutendex) | 200 | 200 JSON | 312 | — | `https://gutendex.com/books/?search=openalex` |
| PubChem PUG REST | 200 | 200 JSON | 401 | — | `https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/aspirin/property/MolecularFormul` |
| PubMed E-utilities | 200 | 200 JSON | 497 | `X-Ratelimit-Limit: 3`, `X-Ratelimit-Remaining: 2` | `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=openalex&retmo` |
| RCSB PDB Data API | 200 | 200 JSON | 321 | — | `https://data.rcsb.org/rest/v1/core/entry/4HHB` |
| re3data | 200 | 200 JSON | 2810 | — | `https://www.re3data.org/api/v1/repositories?query=openalex` |
| RePEc / IDEAS | 200 | 200 HTML | 10570 | — | `https://ideas.repec.org/cgi-bin/htsearch?q=openalex` |
| Research Organization Registry | 200 | 200 JSON | 788 | — | `https://api.ror.org/v2/organizations?query=harvard` |
| SciELO ArticleMeta | 200 | 200 JSON | 1580 | — | `https://articlemeta.scielo.org/api/v1/article/identifiers/?limit=1` |
| Scite | 200 | 200 JSON | 228 | `RateLimit-Limit: 60`, `RateLimit-Remaining: 59`, `RateLimit-Reset: 12` | `https://api.scite.ai/tallies/10.1038/nature12373` |
| Semantic Scholar Graph API | 200 | 200 JSON | 266 | — | `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1038/nature12373?fields=title` |
| Sherpa Romeo | 403 | needs key | 583 | — | `https://v2.sherpa.ac.uk/cgi/retrieve?item-type=publication` |
| Smithsonian Open Access | 403 | needs key | 626 | — | `https://api.si.edu/openaccess/api/v1.0/search?q=openalex` |
| SNAC API | 400 | no answer | 328 | — | `https://api.snaccooperative.org/` |
| SNAC Cooperative | 400 | no answer | 263 | — | `https://api.snaccooperative.org/` |
| Software Heritage | 200 | 200 JSON | 785 | `X-Ratelimit-Limit: 10`, `X-Ratelimit-Remaining: 8`, `X-Ratelimit-Reset: 1792464519` | `https://archive.softwareheritage.org/api/1/origin/search/openalex/?limit=1` |
| Springer Nature API | 401 | needs key | 792 | — | `https://api.springernature.com/meta/v2/json?q=openalex` |
| The Met Collection API | 200 | 200 JSON | 691 | — | `https://collectionapi.metmuseum.org/public/collection/v1/objects/436535` |
| Thoth Open Metadata | 200 | 200 JSON | 967 | — | `https://api.thoth.pub/` |
| Trove (National Library of Australia) | 401 | needs key | 1074 | — | `https://api.trove.nla.gov.au/v3/result?q=openalex&category=book&n=1` |
| UK National Archives Discovery | 200 | 200 JSON | 942 | — | `https://discovery.nationalarchives.gov.uk/API/search/records?sps.searchQuery=openalex` |
| UK Web Archive | 0 | no answer | 353 | — | `https://www.webarchive.org.uk/wayback/archive/cdx?url=openalex.org&limit=2` |
| UniProt | 200 | 200 JSON | 1016 | — | `https://rest.uniprot.org/uniprotkb/search?query=openalex&size=1&format=json` |
| Unpaywall | 200 | 200 JSON | 360 | — | `https://api.unpaywall.org/v2/10.1038/nature12373?email=research@example.org` |
| US National Archives Catalog | 200 | 200 HTML | 293 | — | `https://catalog.archives.gov/api/v2/records/search?q=openalex` |
| USPTO Open Data Portal (IBD) | 200 | 200 HTML | 1733 | — | `https://developer.uspto.gov/ibd-api/v1/application/publications?publicationTitleText=eng` |
| VIAF | 200 | 200 JSON | 203 | `Ratelimit-Limit: 1003`, `Ratelimit-Remaining: 999`, `Ratelimit-Reset: 76279` | `https://viaf.org/viaf/AutoSuggest?query=openalex` |
| Wayback Availability API | 200 | 200 JSON | 464 | — | `https://archive.org/wayback/available?url=openalex.org` |
| Wayback Machine CDX | 200 | 200 JSON | 696 | — | `https://web.archive.org/cdx/search/cdx?url=openalex.org&limit=2&output=json` |
| Wayback Save Page Now | 200 | 200 JSON | 426 | — | `https://web.archive.org/save/status/https://example.com` |
| Wikidata Query Service | 200 | 200 JSON | 347 | — | `https://query.wikidata.org/sparql?format=json&query=SELECT%20%3Fitem%20WHERE%20%7B%3Fite` |
| Wikipedia / MediaWiki API | 200 | 200 JSON | 432 | — | `https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=openalex&format=jso` |
| Wiley TDM API | 400 | no answer | 339 | — | `https://api.wiley.com/onlinelibrary/tdm/v1/articles/10.1002%2Fadvs.201900001` |
| zbMATH Open | 200 | 200 JSON | 645 | — | `https://api.zbmath.org/v1/document/_structured_search_query?search_string=openalex&resul` |
| Zenodo | 200 | 200 JSON | 1266 | `retry-after: 11`, `x-ratelimit-limit: 30`, `x-ratelimit-remaining: 28` | `https://zenodo.org/api/records?q=openalex&size=1` |

## Endpoints that changed their answer between attempts

The probe keeps earlier results instead of overwriting them, so a throttle or a transient failure stays visible:

- **Perma.cc** — HTTP 403 → HTTP 200 (final: 200 JSON)
- **Gallica (BnF)** — HTTP 200 → HTTP 403 (final: bot wall)

## Rate-limit headers seen in the wild

These are the only endpoints that told the probe its budget in the response headers, which is what a gateway would use to pace itself automatically:

- **Arquivo.pt** — `RateLimit-Limit: 250`, `RateLimit-Reset: 60`, `X-RateLimit-Limit: 250`, `X-RateLimit-Policy: 250;w=60`, `X-RateLimit-Reset: t=1792464508520004`, `X-RateLimit-Scope: ip`
- **Software Heritage** — `X-Ratelimit-Limit: 10`, `X-Ratelimit-Remaining: 8`, `X-Ratelimit-Reset: 1792464519`
- **Europeana** — `ratelimit: "project";r=993901;t=691`, `ratelimit-policy: "project";q=1000000;w=3600`
- **OpenAlex** — `X-RateLimit-Cost-USD: 0.0001`, `X-RateLimit-Credits-Used: 1`, `X-RateLimit-Limit: 1000`, `X-RateLimit-Limit-USD: 0.1`, `X-RateLimit-Onetime-Remaining: 0`, `X-RateLimit-Prepaid-Remaining-USD: 0`, `X-RateLimit-Remaining: 942`, `X-RateLimit-Remaining-USD: 0.0942`, `X-RateLimit-Reset: 76289`
- **Crossref REST API** — `x-rate-limit-interval: 1s`, `x-rate-limit-limit: 5`
- **CORE** — `x-ratelimit-limit: 10`, `x-ratelimit-remaining: 9`, `x-ratelimit-retry-after: 2026-10-20T02:48:32+0000`
- **OpenAIRE Graph** — `x-ratelimit-limit: 7199`, `x-ratelimit-used: 16`
- **OpenAIRE Search API** — `x-ratelimit-limit: 7199`, `x-ratelimit-used: 17`
- **Scite** — `RateLimit-Limit: 60`, `RateLimit-Remaining: 59`, `RateLimit-Reset: 12`, `X-RateLimit-Limit-Minute: 60`, `X-RateLimit-Remaining-Minute: 59`
- **PubMed E-utilities** — `X-Ratelimit-Limit: 3`, `X-Ratelimit-Remaining: 2`
- **NDLTD Union Catalog** — `Retry-After: 86400`
- **OpenAIRE Explore** — `x-ratelimit-limit: 7199`, `x-ratelimit-used: 18`
- **Zenodo** — `retry-after: 11`, `x-ratelimit-limit: 30`, `x-ratelimit-remaining: 28`, `x-ratelimit-reset: 1792464529`
- **Hugging Face Hub** — `RateLimit: "api";r=498;t=123`, `RateLimit-Policy: "fixed window";"api";q=500;w=300`
- **Papers with Code** — `RateLimit: "pages";r=98;t=122`, `RateLimit-Policy: "fixed window";"pages";q=100;w=300`
- **Ensembl REST** — `X-RateLimit-Limit: 55000`, `X-RateLimit-Period: 3600`, `X-RateLimit-Remaining: 54994`, `X-RateLimit-Reset: 681`
- **Openverse** — `x-ratelimit-available-anon_burst: 19`, `x-ratelimit-available-anon_sustained: 199`, `x-ratelimit-limit-anon_burst: 20/min`, `x-ratelimit-limit-anon_sustained: 200/day`
- **VIAF** — `Ratelimit-Limit: 1003`, `Ratelimit-Remaining: 999`, `Ratelimit-Reset: 76279`, `X-Ratelimit-Limit-Day: 1003`, `X-Ratelimit-Remaining-Day: 999`
- **NASA NTRS** — `X-RateLimit-Limit: 500`, `X-RateLimit-Remaining: 499`, `X-RateLimit-Reset: 1792464778`

Everything else publishes its allowance in prose or not at all. That is the single biggest practical difference from the commercial scraping market, where rate-limit headers and per-call prices are standard.
