# Academic and archival APIs by documented free allowance

Compiled 2026-10-20. 117 providers, 20 with a documented call figure. Ranked by the documented recurring free volume, largest first; providers that publish no number follow, ordered by evidence confidence.

**Read the volume column as a ceiling, not a quota.** Where a provider publishes a rate (`5 requests/second`) and not a monthly figure, the monthly number is that rate multiplied by the seconds in a 30-day month. Nobody calls at that rate for a month; the column exists so that rates of different shapes can be compared at all. The `Basis` column always says which kind of number it is.

Columns: **Calls/mo** documented recurring free volume; **Basis** the published figure or the arithmetic; **Key** whether an API key or account is needed; **Card** whether a payment card is demanded; **Probe** what one unauthenticated request returned; **Conf** evidence confidence.

| # | Provider | Category | Calls/mo | Basis | Key | Card | Probe | Conf | Links |
|---|----------|----------|--------:|-------|-----|:----:|-------|:----:|-------|
| 1 | **UniProt** | data-api | 518,400,000 | 200/s x 2,592,000 s/month = 518,400,000 calls/month ceiling | none | no | 200 JSON | high | [home](https://www.uniprot.org/) · [docs](https://www.uniprot.org/help/api) · [report](../providers/uniprot.md) |
| 2 | **The Met Collection API** | aggregator | 207,360,000 | 80/s x 2,592,000 s/month = 207,360,000 calls/month ceiling | none | no | 200 JSON | high | [home](https://www.metmuseum.org/) · [docs](https://metmuseum.github.io/) · [report](../providers/met-museum.md) |
| 3 | **Research Organization Registry** | scholarly-graph | 17,280,000 | 2,000 per 5 min = 400/min x 1,440 x 30 = 17,280,000 calls/month ceiling | none | no | 200 JSON | high | [home](https://ror.org/) · [docs](https://ror.readme.io/docs/rest-api) · [llms](https://ror.readme.io/llms.txt) · [report](../providers/ror.md) |
| 4 | **Crossref REST API** | scholarly-graph | 12,960,000 | 5/s x 2,592,000 s/month = 12,960,000 calls/month ceiling | none | no | 200 JSON | high | [home](https://www.crossref.org/) · [docs](https://www.crossref.org/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/) · [report](../providers/crossref.md) |
| 5 | **Arquivo.pt** | web-archive | 10,800,000 | 250/60s x 2,592,000 s/month = 10,800,000 calls/month ceiling | none | no | 200 JSON | high | [home](https://arquivo.pt/) · [docs](https://arquivo.pt/api) · [report](../providers/arquivo.md) |
| 6 | **OpenCitations Index** | scholarly-graph | 7,776,000 | 180/min x 1,440 x 30 = 7,776,000 calls/month ceiling | none | no | 200 JSON | high | [home](https://opencitations.net/) · [docs](https://opencitations.net/index/api/v2) · [report](../providers/opencitations.md) |
| 7 | **PubMed E-utilities** | index | 7,776,000 | 3/s x 2,592,000 s/month = 7,776,000 calls/month ceiling | none | no | 200 JSON | high | [home](https://pubmed.ncbi.nlm.nih.gov/) · [docs](https://www.ncbi.nlm.nih.gov/books/NBK25497/) · [report](../providers/pubmed.md) |
| 8 | **INSPIRE-HEP** | index | 7,776,000 | 15 per 5 s = 180/min x 1,440 x 30 = 7,776,000 calls/month ceiling | none | no | 200 JSON | high | [home](https://inspirehep.net/) · [docs](https://github.com/inspirehep/rest-api-doc) · [report](../providers/inspirehep.md) |
| 9 | **DOAJ** | index | 5,184,000 | 2/s x 2,592,000 s/month = 5,184,000 calls/month ceiling | none | no | 200 JSON | high | [home](https://doaj.org/) · [docs](https://doaj.org/api/v4/docs) · [report](../providers/doaj.md) |
| 10 | **DataCite REST API** | scholarly-graph | 4,320,000 | 500 per 5 min = 100/min x 1,440 x 30 = 4,320,000 calls/month ceiling | none | no | 200 JSON | high | [home](https://datacite.org/) · [docs](https://support.datacite.org/docs/api) · [llms](https://support.datacite.org/llms.txt) · [report](../providers/datacite.md) |
| 11 | **Open Library** | aggregator | 2,592,000 | 1/s x 2,592,000 s/month = 2,592,000 calls/month ceiling | none | no | 200 JSON | high | [home](https://openlibrary.org/) · [docs](https://openlibrary.org/developers/api) · [llms](https://docs.openlibrary.org/llms.txt) · [report](../providers/openlibrary.md) |
| 12 | **Zenodo** | repository | 2,592,000 | 60/min x 1,440 x 30 = 2,592,000 calls/month ceiling for guests | none | no | 200 JSON | high | [home](https://zenodo.org/) · [docs](https://developers.zenodo.org/) · [report](../providers/zenodo.md) |
| 13 | **Art Institute of Chicago API** | aggregator | 2,592,000 | 60/min x 1,440 x 30 = 2,592,000 calls/month ceiling | none | no | 200 JSON | high | [home](https://api.artic.edu/docs/) · [docs](https://api.artic.edu/docs/) · [report](../providers/artic.md) |
| 14 | **CORE** | scholarly-graph | 1,296,000 | 5 per 10 s = 30/min x 1,440 x 30 = 1,296,000 calls/month ceiling | none | no | 200 JSON | high | [home](https://core.ac.uk/) · [docs](https://core.ac.uk/services/api) · [report](../providers/core.md) |
| 15 | **Dimensions** | scholarly-graph | 1,296,000 | 30/min x 1,440 x 30 = 1,296,000 calls/month ceiling, but eligibility is restricted | key on application | no | no answer | high | [home](https://www.dimensions.ai/) · [docs](https://docs.dimensions.ai/dsl/api.html) · [report](../providers/dimensions.md) |
| 16 | **Library of Congress JSON API** | aggregator | 864,000 | 20/min x 1,440 min/day x 30 = 864,000 calls/month ceiling | none | no | bot wall | high | [home](https://www.loc.gov/) · [docs](https://www.loc.gov/apis/) · [report](../providers/loc.md) |
| 17 | **arXiv API** | index | 864,000 | 1 per 3 s = 1,200/hour x 24 x 30 = 864,000 calls/month ceiling | none | no | 200 JSON | high | [home](https://arxiv.org/) · [docs](https://info.arxiv.org/help/api/tou.html) · [report](../providers/arxiv.md) |
| 18 | **OpenAlex** | scholarly-graph | 300,000 | 10,000 list+filter calls per $1 of daily budget x 30 = 300,000 calls/month; a search costs 10x a | free key | no | 200 JSON | high | [home](https://openalex.org/) · [docs](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication) · [llms](https://docs.openalex.org/llms.txt) · [report](../providers/openalex.md) |
| 19 | **NASA ADS** | index | 150,000 | 5,000/day x 30 = 150,000 calls/month (published daily quota) | free key | no | needs key | high | [home](https://ui.adsabs.harvard.edu/) · [docs](https://ui.adsabs.harvard.edu/help/api/) · [report](../providers/ads.md) |
| 20 | **US National Archives Catalog** | web-archive | 10,000 | published monthly figure, not a rate conversion | key on application | no | 200 HTML | high | [home](https://www.archives.gov/research/catalog) · [docs](https://www.archives.gov/research/catalog/help/api) · [report](../providers/nara.md) |
| 21 | **Common Crawl Index** | web-archive | — | no published call quota; the index is a static file service | none | no | 200 JSON | high | [home](https://commoncrawl.org/) · [docs](https://commoncrawl.org/cc-index-table) · [report](../providers/commoncrawl.md) |
| 22 | **DOAB** | index | — | all services free of charge; no call quota published | free key | no | needs key | high | [home](https://www.doabooks.org/) · [docs](https://directory.doabooks.org/rest/) · [report](../providers/doab.md) |
| 23 | **Figshare** | repository | — | no automatic rate limiting in place for API requests | free key | no | 200 JSON | high | [home](https://figshare.com/) · [docs](https://docs.figshare.com/) · [report](../providers/figshare.md) |
| 24 | **Project Gutenberg (Gutendex)** | aggregator | — | no fees and no registration; the mirror is a static file service | none | no | 200 JSON | high | [home](https://www.gutenberg.org/) · [docs](https://gutendex.com/) · [report](../providers/gutenberg.md) |
| 25 | **Scite** | scholarly-graph | — | papers and tallies endpoints are public; everything else needs a key | free key | no | 200 JSON | high | [home](https://scite.ai/) · [docs](https://api.scite.ai/) · [llms](https://scite.ai/llms.txt) · [report](../providers/scite.md) |
| 26 | **Semantic Scholar Graph API** | scholarly-graph | — | 1,000 requests/second shared by ALL unauthenticated callers; 1 req/s per key | none | no | 200 JSON | high | [home](https://www.semanticscholar.org/) · [docs](https://www.semanticscholar.org/product/api) · [report](../providers/semanticscholar.md) |
| 27 | **Wikidata Query Service** | aggregator | — | 60 seconds of processing time per 60 seconds, per client; 30 error queries/minute | none | no | 200 JSON | high | [home](https://query.wikidata.org/) · [docs](https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual) · [report](../providers/wikidata.md) |
| 28 | **Wikipedia / MediaWiki API** | aggregator | — | no hard speed limit on reads; write and state-changing calls are limited | none | no | 200 JSON | high | [home](https://www.mediawiki.org/wiki/API:Main_page) · [docs](https://www.mediawiki.org/wiki/API:Etiquette) · [report](../providers/wikipedia-api.md) |
| 29 | **BASE (Bielefeld)** | scholarly-graph | — | API key granted on application; no call quota published | key on application | no | 200 JSON | medium | [home](https://www.base-search.net/) · [docs](https://api.base-search.net/) · [report](../providers/base.md) |
| 30 | **BioModels** | data-api | — | no published quota captured | none | no | 200 JSON | medium | [home](https://www.ebi.ac.uk/biomodels/) · [docs](https://www.ebi.ac.uk/biomodels/docs/) · [report](../providers/biomodels.md) |
| 31 | **Chronicling America** | aggregator | — | the legacy dedicated API is retired; the collection is served by the loc.gov API | none | no | 404 | medium | [home](https://chroniclingamerica.loc.gov/) · [docs](https://chroniclingamerica.loc.gov/about/api/) · [report](../providers/chroniclingamerica.md) |
| 32 | **Cleveland Museum of Art Open Access API** | aggregator | — | no published quota captured | none | no | 200 JSON | medium | [home](https://www.clevelandart.org/) · [docs](https://openaccess-api.clevelandart.org/) · [report](../providers/cleveland-art.md) |
| 33 | **Conifer (Rhizome)** | web-archive | — | free accounts get 5GB of storage; no call quota published | free key | no | 200 JSON | medium | [home](https://conifer.rhizome.org/) · [docs](https://conifer.rhizome.org/api/docs) · [report](../providers/conifer.md) |
| 34 | **Deutsche Nationalbibliothek SRU** | aggregator | — | SRU service; data free of charge under CC0 | none | no | 200 JSON | medium | [home](https://www.dnb.de/) · [docs](https://www.dnb.de/EN/Professionell/Metadatendienste/metadatendienste_node.html) · [report](../providers/dnb-sru.md) |
| 35 | **Elsevier Scopus / ScienceDirect API** | publisher | — | API key plus an entitlement per product; no free allowance published | paid only | ? | needs key | medium | [home](https://www.elsevier.com/) · [docs](https://dev.elsevier.com/) · [report](../providers/elsevier.md) |
| 36 | **Europeana** | aggregator | — | no published call quota; a demo key (`wskey=api2demo`) works on the record API | free key | no | 200 JSON | medium | [home](https://www.europeana.eu/) · [docs](https://europeana.atlassian.net/wiki/spaces/EF/pages/2477260801/API+documentation) · [report](../providers/europeana.md) |
| 37 | **GBIF** | data-api | — | no fixed rate; the docs say the maximum changes with server load | none | no | 200 JSON | medium | [home](https://www.gbif.org/) · [docs](https://techdocs.gbif.org/en/openapi/) · [report](../providers/gbif.md) |
| 38 | **Gallica (BnF)** | aggregator | — | SRU service; no call quota published in the captured pages | none | no | bot wall | medium | [home](https://gallica.bnf.fr/) · [docs](https://api.bnf.fr/api-gallica-de-recherche) · [report](../providers/gallica.md) |
| 39 | **HathiTrust Bibliographic API** | aggregator | — | no published call quota; bulk work is steered to OAI and the hathifiles | none | no | 200 JSON | medium | [home](https://www.hathitrust.org/) · [docs](https://www.hathitrust.org/bib_api) · [report](../providers/hathitrust.md) |
| 40 | **Hugging Face Hub** | repository | — | limits are per request class and published through RateLimit headers, not as one table; the docs | free key | no | 200 JSON | medium | [home](https://huggingface.co/) · [docs](https://huggingface.co/docs/hub/api) · [report](../providers/huggingface.md) |
| 41 | **IEEE Xplore API** | publisher | — | API key required; the docs page did not state a free quota | key on application | ? | needs key | medium | [home](https://developer.ieee.org/) · [docs](https://developer.ieee.org/docs) · [report](../providers/ieee.md) |
| 42 | **Internet Archive Metadata API** | web-archive | — | no published quota | none | no | 200 JSON | medium | [home](https://archive.org/) · [docs](https://archive.org/developers/md-read.html) · [report](../providers/ia-metadata.md) |
| 43 | **J-STAGE** | index | — | no published quota captured | none | no | 200 JSON | medium | [home](https://www.jstage.jst.go.jp/) · [docs](https://www.jstage.jst.go.jp/static/pages/JstageServices/TAB3/-char/en) · [report](../providers/jstage.md) |
| 44 | **Lens.org Scholarly API** | scholarly-graph | — | API key required; no free allowance published | paid only | ? | needs key | medium | [home](https://www.lens.org/) · [docs](https://docs.api.lens.org/) · [report](../providers/lens.md) |
| 45 | **NASA NTRS** | index | — | no published quota captured | none | no | 200 JSON | medium | [home](https://ntrs.nasa.gov/) · [docs](https://sti.nasa.gov/ntrs-api/) · [report](../providers/ntrs.md) |
| 46 | **OSTI.gov** | index | — | no published quota captured | none | no | 200 JSON | medium | [home](https://www.osti.gov/) · [docs](https://www.osti.gov/api/v1/docs) · [report](../providers/osti.md) |
| 47 | **OpenAIRE Graph** | scholarly-graph | — | no call quota published; the graph is also downloadable in bulk | none | no | 200 JSON | medium | [home](https://graph.openaire.eu/) · [docs](https://graph.openaire.eu/docs/) · [report](../providers/openaire-graph.md) |
| 48 | **OpenAIRE Search API** | scholarly-graph | — | no call quota published | none | no | 200 JSON | medium | [home](https://www.openaire.eu/) · [docs](https://api.openaire.eu/) · [report](../providers/openaire-search.md) |
| 49 | **Openverse** | aggregator | — | anonymous calls allowed; the API publishes no quota in the captured pages | none | no | 200 JSON | medium | [home](https://openverse.org/) · [docs](https://api.openverse.org/v1/) · [report](../providers/openverse.md) |
| 50 | **PMC ID Converter** | index | — | up to 200 IDs per request; no call quota published | none | no | 200 JSON | medium | [home](https://www.ncbi.nlm.nih.gov/pmc/tools/id-converter-api/) · [docs](https://www.ncbi.nlm.nih.gov/pmc/tools/id-converter-api/) · [report](../providers/pmc-idconv.md) |
| 51 | **PMC Open Access Subset** | index | — | OAI-PMH and the OA web service; no call quota published | none | no | 200 JSON | medium | [home](https://www.ncbi.nlm.nih.gov/pmc/) · [docs](https://www.ncbi.nlm.nih.gov/pmc/tools/oa-service/) · [report](../providers/pmc-oa.md) |
| 52 | **Perma.cc** | web-archive | — | public-archive endpoints need no key; the rest need an API key | key on application | no | 200 JSON | medium | [home](https://perma.cc/) · [docs](https://perma.cc/docs/developer) · [report](../providers/perma.md) |
| 53 | **Smithsonian Open Access** | aggregator | — | api_key required; no call quota captured | free key | no | needs key | medium | [home](https://www.si.edu/openaccess) · [docs](https://edan.si.edu/openaccess/apidocs/) · [report](../providers/smithsonian.md) |
| 54 | **Software Heritage** | web-archive | — | no published quota; the API documents only its routes | none | no | 200 JSON | medium | [home](https://www.softwareheritage.org/) · [docs](https://archive.softwareheritage.org/api/) · [report](../providers/softwareheritage.md) |
| 55 | **Springer Nature API** | publisher | — | API key required; higher rate limits are a paid feature | paid only | ? | needs key | medium | [home](https://www.springernature.com/) · [docs](https://dev.springernature.com/) · [report](../providers/springer.md) |
| 56 | **Thoth Open Metadata** | repository | — | no published quota; GraphQL and export APIs | none | no | 200 JSON | medium | [home](https://thoth.pub/) · [docs](https://api.thoth.pub/graphql) · [report](../providers/thoth.md) |
| 57 | **Trove (National Library of Australia)** | aggregator | — | call rate is set per application level; the table lists 200m for each level | key on application | no | needs key | medium | [home](https://trove.nla.gov.au/) · [docs](https://trove.nla.gov.au/about/create-something/using-api) · [report](../providers/trove.md) |
| 58 | **Unpaywall** | index | — | legacy-compatible surface over the OpenAlex database; the OpenAlex $1/day budget is the allowanc | free key | no | 200 JSON | medium | [home](https://unpaywall.org/) · [docs](https://unpaywall.org/products/api) · [report](../providers/unpaywall.md) |
| 59 | **Wayback Availability API** | web-archive | — | no published quota | none | no | 200 JSON | medium | [home](https://archive.org/) · [docs](https://archive.org/developers/wayback-cdx-server.html) · [report](../providers/wayback-availability.md) |
| 60 | **Wayback Machine CDX** | web-archive | — | no published call quota; the CDX endpoint answers unauthenticated callers | none | no | 200 JSON | medium | [home](https://web.archive.org/) · [docs](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server) · [report](../providers/wayback-cdx.md) |
| 61 | **bioRxiv API** | index | — | no published call quota; 100 results per page, cursor paging | none | no | 200 JSON | medium | [home](https://www.biorxiv.org/) · [docs](https://api.biorxiv.org/) · [report](../providers/biorxiv.md) |
| 62 | **iDigBio** | data-api | — | anonymous calls allowed; authenticating raises the limit | none | no | 200 JSON | medium | [home](https://www.idigbio.org/) · [docs](https://github.com/iDigBio/idigbio-search-api/wiki) · [report](../providers/idigbio.md) |
| 63 | **medRxiv API** | index | — | same service as bioRxiv; no published quota | none | no | 200 JSON | medium | [home](https://www.medrxiv.org/) · [docs](https://api.biorxiv.org/) · [report](../providers/medrxiv.md) |
| 64 | **re3data** | repository | — | no published quota; the API is a plain REST interface | none | no | 200 JSON | medium | [home](https://www.re3data.org/) · [docs](https://www.re3data.org/api/doc) · [report](../providers/re3data.md) |
| 65 | **Altmetric** | scholarly-graph | — | API key required; no free allowance captured | key on application | ? | needs key | low | [home](https://www.altmetric.com/) · [docs](https://api.altmetric.com/) · [report](../providers/altmetric.md) |
| 66 | **Archives Portal Europe** | web-archive | — | OAI-PMH endpoint answered 404 at the documented path | ? | no | 404 | low | [home](https://www.archivesportaleurope.net/) · [docs](https://www.archivesportaleurope.net/information/api) · [report](../providers/archives-portal-europe.md) |
| 67 | **BioStudies (EBI)** | data-api | — | no published quota captured | none | no | 200 JSON | low | [home](https://www.ebi.ac.uk/biostudies/) · [docs](https://www.ebi.ac.uk/biostudies/api/v1/swagger-ui.html) · [report](../providers/biostudies.md) |
| 68 | **CERN Document Server** | index | — | no published quota captured; the site now runs an Anubis proof-of-work check | ? | no | 200 HTML | low | [home](https://cds.cern.ch/) · [docs](https://cds.cern.ch/help/hacking) · [report](../providers/cds-cern.md) |
| 69 | **ChEMBL** | data-api | — | no published quota captured | none | no | 200 JSON | low | [home](https://www.ebi.ac.uk/chembl/) · [docs](https://chembl.gitbook.io/chembl-interface-documentation/web-services) · [llms](https://chembl.gitbook.io/llms.txt) · [report](../providers/chembl.md) |
| 70 | **ClinicalTrials.gov** | index | — | no published call quota captured | none | no | 200 JSON | low | [home](https://clinicaltrials.gov/) · [docs](https://clinicaltrials.gov/data-api/api) · [report](../providers/clinicaltrials.md) |
| 71 | **Crossref Event Data** | scholarly-graph | — | not established — the host did not resolve from this machine | ? | no | no answer | low | [home](https://www.eventdata.crossref.org/) · [docs](https://www.eventdata.crossref.org/guide/) · [report](../providers/crossref-eventdata.md) |
| 72 | **DataONE** | repository | — | not established | ? | no | 200 JSON | low | [home](https://www.dataone.org/) · [docs](https://purl.dataone.org/architecture/apis/MN-API.html) · [report](../providers/dataone.md) |
| 73 | **DataverseNL** | repository | — | no published call quota captured | none | no | 200 JSON | low | [home](https://dataverse.nl/) · [docs](https://guides.dataverse.org/en/latest/api/) · [report](../providers/dataverse-nl.md) |
| 74 | **Digital Public Library of America** | aggregator | — | not established (API key required; docs are behind a 403 for this client) | free key | no | needs key | low | [home](https://dp.la/) · [docs](https://pro.dp.la/developers/api-codex) · [report](../providers/dpla.md) |
| 75 | **DigitalNZ** | aggregator | — | not established (key required; docs served a 202 challenge) | free key | no | 200 JSON | low | [home](https://digitalnz.org/) · [docs](https://digitalnz.org/developers/api) · [report](../providers/digitalnz.md) |
| 76 | **Dryad** | repository | — | no published quota captured | ? | no | 200 JSON | low | [home](https://datadryad.org/) · [docs](https://datadryad.org/api/v2/docs/) · [report](../providers/dryad.md) |
| 77 | **EBI Search** | data-api | — | no published quota captured | none | no | 200 JSON | low | [home](https://www.ebi.ac.uk/ebisearch/) · [docs](https://www.ebi.ac.uk/ebisearch/swagger.ebi) · [report](../providers/ebisearch.md) |
| 78 | **EMBL-EBI Ontology Lookup Service** | data-api | — | no published quota captured | none | no | 200 JSON | low | [home](https://www.ebi.ac.uk/ols4/) · [docs](https://www.ebi.ac.uk/ols4/help) · [report](../providers/ols.md) |
| 79 | **EPO Open Patent Services** | publisher | — | OAuth credentials required; published free quota is per-registered-user and was not captured | key on application | no | needs key | low | [home](https://www.epo.org/) · [docs](https://developers.epo.org/) · [report](../providers/epo-ops.md) |
| 80 | **Ensembl REST** | data-api | — | no published quota captured; the REST root documents endpoints only | none | no | 200 JSON | low | [home](https://www.ensembl.org/) · [docs](https://rest.ensembl.org/) · [report](../providers/ensembl.md) |
| 81 | **Europe PMC** | index | — | no call quota captured; the REST service answers unauthenticated | none | no | 200 JSON | low | [home](https://europepmc.org/) · [docs](https://europepmc.org/RestfulWebService) · [report](../providers/europepmc.md) |
| 82 | **Finna (Finnish libraries)** | aggregator | — | not established — the API returned 403 to this client | ? | no | bot wall | low | [home](https://www.finna.fi/) · [docs](https://api.finna.fi/) · [report](../providers/finna.md) |
| 83 | **HAL Open Archive** | index | — | no published call quota captured | none | no | 200 JSON | low | [home](https://hal.science/) · [docs](https://api.archives-ouvertes.fr/docs) · [report](../providers/hal.md) |
| 84 | **Harvard Dataverse** | repository | — | no published call quota captured | none | no | 200 JSON | low | [home](https://dataverse.harvard.edu/) · [docs](https://guides.dataverse.org/en/latest/api/) · [report](../providers/dataverse.md) |
| 85 | **Internet Archive Full-Text Search** | web-archive | — | no published quota | ? | no | no answer | low | [home](https://archive.org/search) · [docs](https://archive.org/developers/search_inside.html) · [report](../providers/ia-fulltext.md) |
| 86 | **Internet Archive Scholar / fatcat** | web-archive | — | no published quota | none | no | no answer | low | [home](https://scholar.archive.org/) · [docs](https://api.fatcat.wiki/) · [report](../providers/fatcat.md) |
| 87 | **JSTOR / Constellate** | publisher | — | not established; the API host did not resolve | ? | ? | no answer | low | [home](https://www.jstor.org/) · [docs](https://constellate.org/docs/) · [report](../providers/jstor-constellate.md) |
| 88 | **K10plus SRU** | aggregator | — | SRU service; no published call quota | none | no | 200 JSON | low | [home](https://k10plus.de/) · [docs](https://projekt.mvb10plus.de/) · [report](../providers/k10plus-sru.md) |
| 89 | **LA Referencia** | index | — | not established — the API host did not resolve | ? | no | no answer | low | [home](https://www.lareferencia.info/) · [docs](https://api.lareferencia.info/v1/) · [report](../providers/lareferencia.md) |
| 90 | **Memento TimeTravel aggregator** | web-archive | — | not established | ? | no | no answer | low | [home](http://timetravel.mementoweb.org/) · [docs](http://timetravel.mementoweb.org/guide/api/) · [report](../providers/memento.md) |
| 91 | **NDLTD Union Catalog** | index | — | not established — the OAI endpoint returned 503 | ? | no | 429/503 | low | [home](https://search.ndltd.org/) · [docs](https://union.ndltd.org/OAI-PMH) · [report](../providers/ndltd.md) |
| 92 | **National Library of Norway API** | aggregator | — | no published quota captured | ? | no | 200 JSON | low | [home](https://www.nb.no/) · [docs](https://api.nb.no/catalog/swagger-ui.html) · [report](../providers/nb-no.md) |
| 93 | **OAPEN Library** | index | — | no published call quota captured | free key | no | needs key | low | [home](https://www.oapen.org/) · [docs](https://library.oapen.org/rest/) · [report](../providers/oapen.md) |
| 94 | **OBIS** | data-api | — | no published quota captured | none | no | 200 JSON | low | [home](https://obis.org/) · [docs](https://api.obis.org/) · [report](../providers/obis.md) |
| 95 | **ORCID Public API** | scholarly-graph | — | public API; the rate-limit page was not captured | free key | no | 200 JSON | low | [home](https://orcid.org/) · [docs](https://info.orcid.org/documentation/api-reference/) · [report](../providers/orcid.md) |
| 96 | **OSF (Open Science Framework)** | repository | — | no published quota captured | ? | no | 200 JSON | low | [home](https://osf.io/) · [docs](https://developer.osf.io/) · [report](../providers/osf.md) |
| 97 | **OpenML** | repository | — | no published quota captured | ? | no | 200 JSON | low | [home](https://www.openml.org/) · [docs](https://www.openml.org/apis) · [report](../providers/openml.md) |
| 98 | **OpenReview** | repository | — | no published call quota captured | ? | no | 200 HTML | low | [home](https://openreview.net/) · [docs](https://docs.openreview.net/reference/api-v2) · [llms](https://docs.openreview.net/llms.txt) · [report](../providers/openreview.md) |
| 99 | **Papers with Code** | repository | — | no published quota captured | ? | no | 200 HTML | low | [home](https://paperswithcode.com/) · [docs](https://paperswithcode.com/api/v1/docs/) · [report](../providers/paperswithcode.md) |
| 100 | **PatentsView** | publisher | — | API key required; the docs page rendered as an application shell | key on application | ? | 200 HTML | low | [home](https://patentsview.org/) · [docs](https://patentsview.org/apis/api-endpoints) · [report](../providers/patentsview.md) |
| 101 | **PubChem PUG REST** | data-api | — | no published quota captured; the docs page returned a bot check to this client | none | no | 200 JSON | low | [home](https://pubchem.ncbi.nlm.nih.gov/) · [docs](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) · [report](../providers/pubchem.md) |
| 102 | **RCSB PDB Data API** | data-api | — | no published quota captured | none | no | 200 JSON | low | [home](https://www.rcsb.org/) · [docs](https://data.rcsb.org/redoc/) · [report](../providers/pdb.md) |
| 103 | **RePEc / IDEAS** | index | — | no published quota captured | ? | no | 200 HTML | low | [home](https://ideas.repec.org/) · [docs](https://ideas.repec.org/) · [report](../providers/repec.md) |
| 104 | **SNAC Cooperative** | web-archive | — | not established | ? | no | no answer | low | [home](https://snaccooperative.org/) · [docs](https://api.snaccooperative.org/) · [report](../providers/snac.md) |
| 105 | **SciELO ArticleMeta** | index | — | not established | ? | no | 200 JSON | low | [home](https://scielo.org/) · [docs](https://articlemeta.scielo.org/api/v1/) · [report](../providers/scielo.md) |
| 106 | **Sherpa Romeo** | scholarly-graph | — | API key required; the docs site returned 403 to this client | key on application | no | needs key | low | [home](https://v2.sherpa.ac.uk/) · [docs](https://v2.sherpa.ac.uk/api/) · [report](../providers/sherpa-romeo.md) |
| 107 | **UK National Archives Discovery** | web-archive | — | not established | ? | no | 200 JSON | low | [home](https://discovery.nationalarchives.gov.uk/) · [docs](https://discovery.nationalarchives.gov.uk/API/site/search) · [report](../providers/tna-discovery.md) |
| 108 | **UK Web Archive** | web-archive | — | not established | ? | no | no answer | low | [home](https://www.webarchive.org.uk/) · [docs](https://www.webarchive.org.uk/en/ukwa/info/api) · [report](../providers/ukwa.md) |
| 109 | **USPTO Open Data Portal (IBD)** | publisher | — | no published quota captured; the API answered HTML rather than JSON | ? | ? | 200 HTML | low | [home](https://developer.uspto.gov/) · [docs](https://developer.uspto.gov/api-catalog) · [report](../providers/uspto-ibd.md) |
| 110 | **VIAF** | aggregator | — | not established; the data page returned 403 | ? | no | 200 JSON | low | [home](https://viaf.org/) · [docs](https://viaf.org/viaf/data/) · [report](../providers/viaf.md) |
| 111 | **Wayback Save Page Now** | web-archive | — | Save Page Now is rate-limited per account in practice; no number captured | ? | no | 200 JSON | low | [home](https://web.archive.org/save) · [docs](https://archive.org/developers/) · [report](../providers/wayback-save.md) |
| 112 | **Wiley TDM API** | publisher | — | TDM API token required; no free allowance captured | paid only | ? | no answer | low | [home](https://www.wiley.com/) · [docs](https://onlinelibrary.wiley.com/library-info/resources/text-and-datamining) · [report](../providers/wiley.md) |
| 113 | **archive.today** | web-archive | — | no published quota; the site throttles bursty callers with 429 | none | no | 200 JSON | low | [home](https://archive.ph/) · [docs](https://archive.ph/) · [report](../providers/archive-today.md) |
| 114 | **dblp computer science bibliography** | scholarly-graph | — | no published quota; the site answers a JS challenge to non-browser clients | none | no | 200 HTML | low | [home](https://dblp.org/) · [docs](https://dblp.org/faq/How+to+use+the+dblp+search+API.html) · [report](../providers/dblp.md) |
| 115 | **iNaturalist** | data-api | — | no published quota captured; the recommendations page returned 403 | none | no | 200 JSON | low | [home](https://www.inaturalist.org/) · [docs](https://api.inaturalist.org/v1/docs/) · [report](../providers/inaturalist.md) |
| 116 | **id.loc.gov (LC Linked Data)** | aggregator | — | not established — the search endpoint returned 403 | ? | no | bot wall | low | [home](https://id.loc.gov/) · [docs](https://id.loc.gov/) · [report](../providers/id-loc.md) |
| 117 | **zbMATH Open** | index | — | no published quota captured | none | no | 200 JSON | low | [home](https://zbmath.org/) · [docs](https://api.zbmath.org/v1/) · [report](../providers/zbmath.md) |

## The ranking is not the dataset

Every one of the 117 providers has a full report under `providers/` and a row in the category catalogue below, including the ones with no published figure. A provider absent from the ranked top of the table is not absent from the work.

## Web archives & national archive catalogs

### Arquivo.pt

- Free access: 10,800,000 calls/mo — 250 requests/60s (full-text & URL search); 400 requests/60s (image, Memento)
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://arquivo.pt/ · docs https://arquivo.pt/api · llms.txt — · [full report](../providers/arquivo.md)

### US National Archives Catalog

- Free access: 10,000 calls/mo — 10,000 queries/month per API key (default); higher tiers to 1.5M/month
- Authentication: key on application · confidence high · probe 200 HTML
- Links: home https://www.archives.gov/research/catalog · docs https://www.archives.gov/research/catalog/help/api · llms.txt — · [full report](../providers/nara.md)

### Archives Portal Europe

- Free access: no published number — OAI-PMH endpoint answered 404 at the documented path
- Authentication: ? · confidence low · probe 404
- Links: home https://www.archivesportaleurope.net/ · docs https://www.archivesportaleurope.net/information/api · llms.txt — · [full report](../providers/archives-portal-europe.md)

### Common Crawl Index

- Free access: no published number — no published call quota; the index is a static file service
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://commoncrawl.org/ · docs https://commoncrawl.org/cc-index-table · llms.txt — · [full report](../providers/commoncrawl.md)

### Conifer (Rhizome)

- Free access: no published number — free accounts get 5GB of storage; no call quota published
- Authentication: free key · confidence medium · probe 200 JSON
- Links: home https://conifer.rhizome.org/ · docs https://conifer.rhizome.org/api/docs · llms.txt — · [full report](../providers/conifer.md)

### Internet Archive Full-Text Search

- Free access: no published number — no published quota
- Authentication: ? · confidence low · probe no answer
- Links: home https://archive.org/search · docs https://archive.org/developers/search_inside.html · llms.txt — · [full report](../providers/ia-fulltext.md)

### Internet Archive Metadata API

- Free access: no published number — no published quota
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://archive.org/ · docs https://archive.org/developers/md-read.html · llms.txt — · [full report](../providers/ia-metadata.md)

### Internet Archive Scholar / fatcat

- Free access: no published number — no published quota
- Authentication: none · confidence low · probe no answer
- Links: home https://scholar.archive.org/ · docs https://api.fatcat.wiki/ · llms.txt — · [full report](../providers/fatcat.md)

### Memento TimeTravel aggregator

- Free access: no published number — not established
- Authentication: ? · confidence low · probe no answer
- Links: home http://timetravel.mementoweb.org/ · docs http://timetravel.mementoweb.org/guide/api/ · llms.txt — · [full report](../providers/memento.md)

### Perma.cc

- Free access: no published number — public-archive endpoints need no key; the rest need an API key
- Authentication: key on application · confidence medium · probe 200 JSON
- Links: home https://perma.cc/ · docs https://perma.cc/docs/developer · llms.txt — · [full report](../providers/perma.md)

### SNAC Cooperative

- Free access: no published number — not established
- Authentication: ? · confidence low · probe no answer
- Links: home https://snaccooperative.org/ · docs https://api.snaccooperative.org/ · llms.txt — · [full report](../providers/snac.md)

### Software Heritage

- Free access: no published number — no published quota; the API documents only its routes
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.softwareheritage.org/ · docs https://archive.softwareheritage.org/api/ · llms.txt — · [full report](../providers/softwareheritage.md)

### UK National Archives Discovery

- Free access: no published number — not established
- Authentication: ? · confidence low · probe 200 JSON
- Links: home https://discovery.nationalarchives.gov.uk/ · docs https://discovery.nationalarchives.gov.uk/API/site/search · llms.txt — · [full report](../providers/tna-discovery.md)

### UK Web Archive

- Free access: no published number — not established
- Authentication: ? · confidence low · probe no answer
- Links: home https://www.webarchive.org.uk/ · docs https://www.webarchive.org.uk/en/ukwa/info/api · llms.txt — · [full report](../providers/ukwa.md)

### Wayback Availability API

- Free access: no published number — no published quota
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://archive.org/ · docs https://archive.org/developers/wayback-cdx-server.html · llms.txt — · [full report](../providers/wayback-availability.md)

### Wayback Machine CDX

- Free access: no published number — no published call quota; the CDX endpoint answers unauthenticated callers
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://web.archive.org/ · docs https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server · llms.txt — · [full report](../providers/wayback-cdx.md)

### Wayback Save Page Now

- Free access: no published number — Save Page Now is rate-limited per account in practice; no number captured
- Authentication: ? · confidence low · probe 200 JSON
- Links: home https://web.archive.org/save · docs https://archive.org/developers/ · llms.txt — · [full report](../providers/wayback-save.md)

### archive.today

- Free access: no published number — no published quota; the site throttles bursty callers with 429
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://archive.ph/ · docs https://archive.ph/ · llms.txt — · [full report](../providers/archive-today.md)

## Library / museum / newspaper aggregators

### The Met Collection API

- Free access: 207,360,000 calls/mo — 80 requests/second; no registration or API key
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://www.metmuseum.org/ · docs https://metmuseum.github.io/ · llms.txt — · [full report](../providers/met-museum.md)

### Art Institute of Chicago API

- Free access: 2,592,000 calls/mo — anonymous callers throttled to 60 requests/minute; each IP is one user
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://api.artic.edu/docs/ · docs https://api.artic.edu/docs/ · llms.txt — · [full report](../providers/artic.md)

### Open Library

- Free access: 2,592,000 calls/mo — 1 request/second unidentified; 3 requests/second with a User-Agent carrying an email
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://openlibrary.org/ · docs https://openlibrary.org/developers/api · llms.txt https://docs.openlibrary.org/llms.txt · [full report](../providers/openlibrary.md)

### Library of Congress JSON API

- Free access: 864,000 calls/mo — 20 requests/minute for the JSON/YAML API; 150/min for text and image services
- Authentication: none · confidence high · probe bot wall
- Links: home https://www.loc.gov/ · docs https://www.loc.gov/apis/ · llms.txt — · [full report](../providers/loc.md)

### Chronicling America

- Free access: no published number — the legacy dedicated API is retired; the collection is served by the loc.gov API
- Authentication: none · confidence medium · probe 404
- Links: home https://chroniclingamerica.loc.gov/ · docs https://chroniclingamerica.loc.gov/about/api/ · llms.txt — · [full report](../providers/chroniclingamerica.md)

### Cleveland Museum of Art Open Access API

- Free access: no published number — no published quota captured
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.clevelandart.org/ · docs https://openaccess-api.clevelandart.org/ · llms.txt — · [full report](../providers/cleveland-art.md)

### Deutsche Nationalbibliothek SRU

- Free access: no published number — SRU service; data free of charge under CC0
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.dnb.de/ · docs https://www.dnb.de/EN/Professionell/Metadatendienste/metadatendienste_node.html · llms.txt — · [full report](../providers/dnb-sru.md)

### Digital Public Library of America

- Free access: no published number — not established (API key required; docs are behind a 403 for this client)
- Authentication: free key · confidence low · probe needs key
- Links: home https://dp.la/ · docs https://pro.dp.la/developers/api-codex · llms.txt — · [full report](../providers/dpla.md)

### DigitalNZ

- Free access: no published number — not established (key required; docs served a 202 challenge)
- Authentication: free key · confidence low · probe 200 JSON
- Links: home https://digitalnz.org/ · docs https://digitalnz.org/developers/api · llms.txt — · [full report](../providers/digitalnz.md)

### Europeana

- Free access: no published number — no published call quota; a demo key (`wskey=api2demo`) works on the record API
- Authentication: free key · confidence medium · probe 200 JSON
- Links: home https://www.europeana.eu/ · docs https://europeana.atlassian.net/wiki/spaces/EF/pages/2477260801/API+documentation · llms.txt — · [full report](../providers/europeana.md)

### Finna (Finnish libraries)

- Free access: no published number — not established — the API returned 403 to this client
- Authentication: ? · confidence low · probe bot wall
- Links: home https://www.finna.fi/ · docs https://api.finna.fi/ · llms.txt — · [full report](../providers/finna.md)

### Gallica (BnF)

- Free access: no published number — SRU service; no call quota published in the captured pages
- Authentication: none · confidence medium · probe bot wall
- Links: home https://gallica.bnf.fr/ · docs https://api.bnf.fr/api-gallica-de-recherche · llms.txt — · [full report](../providers/gallica.md)

### HathiTrust Bibliographic API

- Free access: no published number — no published call quota; bulk work is steered to OAI and the hathifiles
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.hathitrust.org/ · docs https://www.hathitrust.org/bib_api · llms.txt — · [full report](../providers/hathitrust.md)

### K10plus SRU

- Free access: no published number — SRU service; no published call quota
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://k10plus.de/ · docs https://projekt.mvb10plus.de/ · llms.txt — · [full report](../providers/k10plus-sru.md)

### National Library of Norway API

- Free access: no published number — no published quota captured
- Authentication: ? · confidence low · probe 200 JSON
- Links: home https://www.nb.no/ · docs https://api.nb.no/catalog/swagger-ui.html · llms.txt — · [full report](../providers/nb-no.md)

### Openverse

- Free access: no published number — anonymous calls allowed; the API publishes no quota in the captured pages
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://openverse.org/ · docs https://api.openverse.org/v1/ · llms.txt — · [full report](../providers/openverse.md)

### Project Gutenberg (Gutendex)

- Free access: no published number — no fees and no registration; the mirror is a static file service
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://www.gutenberg.org/ · docs https://gutendex.com/ · llms.txt — · [full report](../providers/gutenberg.md)

### Smithsonian Open Access

- Free access: no published number — api_key required; no call quota captured
- Authentication: free key · confidence medium · probe needs key
- Links: home https://www.si.edu/openaccess · docs https://edan.si.edu/openaccess/apidocs/ · llms.txt — · [full report](../providers/smithsonian.md)

### Trove (National Library of Australia)

- Free access: no published number — call rate is set per application level; the table lists 200m for each level
- Authentication: key on application · confidence medium · probe needs key
- Links: home https://trove.nla.gov.au/ · docs https://trove.nla.gov.au/about/create-something/using-api · llms.txt — · [full report](../providers/trove.md)

### VIAF

- Free access: no published number — not established; the data page returned 403
- Authentication: ? · confidence low · probe 200 JSON
- Links: home https://viaf.org/ · docs https://viaf.org/viaf/data/ · llms.txt — · [full report](../providers/viaf.md)

### Wikidata Query Service

- Free access: no published number — 60 seconds of processing time per 60 seconds, per client; 30 error queries/minute
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://query.wikidata.org/ · docs https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual · llms.txt — · [full report](../providers/wikidata.md)

### Wikipedia / MediaWiki API

- Free access: no published number — no hard speed limit on reads; write and state-changing calls are limited
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://www.mediawiki.org/wiki/API:Main_page · docs https://www.mediawiki.org/wiki/API:Etiquette · llms.txt — · [full report](../providers/wikipedia-api.md)

### id.loc.gov (LC Linked Data)

- Free access: no published number — not established — the search endpoint returned 403
- Authentication: ? · confidence low · probe bot wall
- Links: home https://id.loc.gov/ · docs https://id.loc.gov/ · llms.txt — · [full report](../providers/id-loc.md)

## Scholarly graphs, metadata & citation APIs

### Research Organization Registry

- Free access: 17,280,000 calls/mo — 2,000 requests per 5 minutes per IP address; no registration
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://ror.org/ · docs https://ror.readme.io/docs/rest-api · llms.txt https://ror.readme.io/llms.txt · [full report](../providers/ror.md)

### Crossref REST API

- Free access: 12,960,000 calls/mo — 5 requests/second (public pool), 10/s polite pool with a mailto, 150/s with a Plus key
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://www.crossref.org/ · docs https://www.crossref.org/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/ · llms.txt — · [full report](../providers/crossref.md)

### OpenCitations Index

- Free access: 7,776,000 calls/mo — 180 requests/minute per IP address
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://opencitations.net/ · docs https://opencitations.net/index/api/v2 · llms.txt — · [full report](../providers/opencitations.md)

### DataCite REST API

- Free access: 4,320,000 calls/mo — 500 requests/5min unidentified, 1,000 identified (mailto), 3,000 authenticated
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://datacite.org/ · docs https://support.datacite.org/docs/api · llms.txt https://support.datacite.org/llms.txt · [full report](../providers/datacite.md)

### CORE

- Free access: 1,296,000 calls/mo — one batch request or five single requests per 10 seconds, without registration
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://core.ac.uk/ · docs https://core.ac.uk/services/api · llms.txt — · [full report](../providers/core.md)

### Dimensions

- Free access: 1,296,000 calls/mo — 30 requests/minute per IP; free access only for eligible research projects
- Authentication: key on application · confidence high · probe no answer
- Links: home https://www.dimensions.ai/ · docs https://docs.dimensions.ai/dsl/api.html · llms.txt — · [full report](../providers/dimensions.md)

### OpenAlex

- Free access: 300,000 calls/mo — 10 req/s without a key, 30 req/s with a free key; $0.10/day keyless, $1/day with a key
- Authentication: free key · confidence high · probe 200 JSON
- Links: home https://openalex.org/ · docs https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication · llms.txt https://docs.openalex.org/llms.txt · [full report](../providers/openalex.md)

### Altmetric

- Free access: no published number — API key required; no free allowance captured
- Authentication: key on application · confidence low · probe needs key
- Links: home https://www.altmetric.com/ · docs https://api.altmetric.com/ · llms.txt — · [full report](../providers/altmetric.md)

### BASE (Bielefeld)

- Free access: no published number — API key granted on application; no call quota published
- Authentication: key on application · confidence medium · probe 200 JSON
- Links: home https://www.base-search.net/ · docs https://api.base-search.net/ · llms.txt — · [full report](../providers/base.md)

### Crossref Event Data

- Free access: no published number — not established — the host did not resolve from this machine
- Authentication: ? · confidence low · probe no answer
- Links: home https://www.eventdata.crossref.org/ · docs https://www.eventdata.crossref.org/guide/ · llms.txt — · [full report](../providers/crossref-eventdata.md)

### Lens.org Scholarly API

- Free access: no published number — API key required; no free allowance published
- Authentication: paid only · confidence medium · probe needs key
- Links: home https://www.lens.org/ · docs https://docs.api.lens.org/ · llms.txt — · [full report](../providers/lens.md)

### ORCID Public API

- Free access: no published number — public API; the rate-limit page was not captured
- Authentication: free key · confidence low · probe 200 JSON
- Links: home https://orcid.org/ · docs https://info.orcid.org/documentation/api-reference/ · llms.txt — · [full report](../providers/orcid.md)

### OpenAIRE Graph

- Free access: no published number — no call quota published; the graph is also downloadable in bulk
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://graph.openaire.eu/ · docs https://graph.openaire.eu/docs/ · llms.txt — · [full report](../providers/openaire-graph.md)

### OpenAIRE Search API

- Free access: no published number — no call quota published
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.openaire.eu/ · docs https://api.openaire.eu/ · llms.txt — · [full report](../providers/openaire-search.md)

### Scite

- Free access: no published number — papers and tallies endpoints are public; everything else needs a key
- Authentication: free key · confidence high · probe 200 JSON
- Links: home https://scite.ai/ · docs https://api.scite.ai/ · llms.txt https://scite.ai/llms.txt · [full report](../providers/scite.md)

### Semantic Scholar Graph API

- Free access: no published number — 1,000 requests/second shared by ALL unauthenticated callers; 1 req/s per key
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://www.semanticscholar.org/ · docs https://www.semanticscholar.org/product/api · llms.txt — · [full report](../providers/semanticscholar.md)

### Sherpa Romeo

- Free access: no published number — API key required; the docs site returned 403 to this client
- Authentication: key on application · confidence low · probe needs key
- Links: home https://v2.sherpa.ac.uk/ · docs https://v2.sherpa.ac.uk/api/ · llms.txt — · [full report](../providers/sherpa-romeo.md)

### dblp computer science bibliography

- Free access: no published number — no published quota; the site answers a JS challenge to non-browser clients
- Authentication: none · confidence low · probe 200 HTML
- Links: home https://dblp.org/ · docs https://dblp.org/faq/How+to+use+the+dblp+search+API.html · llms.txt — · [full report](../providers/dblp.md)

## Bibliographic indexes & preprint servers

### INSPIRE-HEP

- Free access: 7,776,000 calls/mo — 15 requests per 5-second window per IP address
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://inspirehep.net/ · docs https://github.com/inspirehep/rest-api-doc · llms.txt — · [full report](../providers/inspirehep.md)

### PubMed E-utilities

- Free access: 7,776,000 calls/mo — 3 requests/second without a key; 10/s with an NCBI API key
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://pubmed.ncbi.nlm.nih.gov/ · docs https://www.ncbi.nlm.nih.gov/books/NBK25497/ · llms.txt — · [full report](../providers/pubmed.md)

### DOAJ

- Free access: 5,184,000 calls/mo — 2 requests/second on all API routes, with a 5-request burst queue
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://doaj.org/ · docs https://doaj.org/api/v4/docs · llms.txt — · [full report](../providers/doaj.md)

### arXiv API

- Free access: 864,000 calls/mo — no more than one request every three seconds, single connection
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://arxiv.org/ · docs https://info.arxiv.org/help/api/tou.html · llms.txt — · [full report](../providers/arxiv.md)

### NASA ADS

- Free access: 150,000 calls/mo — 5,000 regular requests/day for most request types, with a token; higher limits by email request
- Authentication: free key · confidence high · probe needs key
- Links: home https://ui.adsabs.harvard.edu/ · docs https://ui.adsabs.harvard.edu/help/api/ · llms.txt — · [full report](../providers/ads.md)

### CERN Document Server

- Free access: no published number — no published quota captured; the site now runs an Anubis proof-of-work check
- Authentication: ? · confidence low · probe 200 HTML
- Links: home https://cds.cern.ch/ · docs https://cds.cern.ch/help/hacking · llms.txt — · [full report](../providers/cds-cern.md)

### ClinicalTrials.gov

- Free access: no published number — no published call quota captured
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://clinicaltrials.gov/ · docs https://clinicaltrials.gov/data-api/api · llms.txt — · [full report](../providers/clinicaltrials.md)

### DOAB

- Free access: no published number — all services free of charge; no call quota published
- Authentication: free key · confidence high · probe needs key
- Links: home https://www.doabooks.org/ · docs https://directory.doabooks.org/rest/ · llms.txt — · [full report](../providers/doab.md)

### Europe PMC

- Free access: no published number — no call quota captured; the REST service answers unauthenticated
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://europepmc.org/ · docs https://europepmc.org/RestfulWebService · llms.txt — · [full report](../providers/europepmc.md)

### HAL Open Archive

- Free access: no published number — no published call quota captured
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://hal.science/ · docs https://api.archives-ouvertes.fr/docs · llms.txt — · [full report](../providers/hal.md)

### J-STAGE

- Free access: no published number — no published quota captured
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.jstage.jst.go.jp/ · docs https://www.jstage.jst.go.jp/static/pages/JstageServices/TAB3/-char/en · llms.txt — · [full report](../providers/jstage.md)

### LA Referencia

- Free access: no published number — not established — the API host did not resolve
- Authentication: ? · confidence low · probe no answer
- Links: home https://www.lareferencia.info/ · docs https://api.lareferencia.info/v1/ · llms.txt — · [full report](../providers/lareferencia.md)

### NASA NTRS

- Free access: no published number — no published quota captured
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://ntrs.nasa.gov/ · docs https://sti.nasa.gov/ntrs-api/ · llms.txt — · [full report](../providers/ntrs.md)

### NDLTD Union Catalog

- Free access: no published number — not established — the OAI endpoint returned 503
- Authentication: ? · confidence low · probe 429/503
- Links: home https://search.ndltd.org/ · docs https://union.ndltd.org/OAI-PMH · llms.txt — · [full report](../providers/ndltd.md)

### OAPEN Library

- Free access: no published number — no published call quota captured
- Authentication: free key · confidence low · probe needs key
- Links: home https://www.oapen.org/ · docs https://library.oapen.org/rest/ · llms.txt — · [full report](../providers/oapen.md)

### OSTI.gov

- Free access: no published number — no published quota captured
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.osti.gov/ · docs https://www.osti.gov/api/v1/docs · llms.txt — · [full report](../providers/osti.md)

### PMC ID Converter

- Free access: no published number — up to 200 IDs per request; no call quota published
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.ncbi.nlm.nih.gov/pmc/tools/id-converter-api/ · docs https://www.ncbi.nlm.nih.gov/pmc/tools/id-converter-api/ · llms.txt — · [full report](../providers/pmc-idconv.md)

### PMC Open Access Subset

- Free access: no published number — OAI-PMH and the OA web service; no call quota published
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.ncbi.nlm.nih.gov/pmc/ · docs https://www.ncbi.nlm.nih.gov/pmc/tools/oa-service/ · llms.txt — · [full report](../providers/pmc-oa.md)

### RePEc / IDEAS

- Free access: no published number — no published quota captured
- Authentication: ? · confidence low · probe 200 HTML
- Links: home https://ideas.repec.org/ · docs https://ideas.repec.org/ · llms.txt — · [full report](../providers/repec.md)

### SciELO ArticleMeta

- Free access: no published number — not established
- Authentication: ? · confidence low · probe 200 JSON
- Links: home https://scielo.org/ · docs https://articlemeta.scielo.org/api/v1/ · llms.txt — · [full report](../providers/scielo.md)

### Unpaywall

- Free access: no published number — legacy-compatible surface over the OpenAlex database; the OpenAlex $1/day budget is the allowance that applies
- Authentication: free key · confidence medium · probe 200 JSON
- Links: home https://unpaywall.org/ · docs https://unpaywall.org/products/api · llms.txt — · [full report](../providers/unpaywall.md)

### bioRxiv API

- Free access: no published number — no published call quota; 100 results per page, cursor paging
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.biorxiv.org/ · docs https://api.biorxiv.org/ · llms.txt — · [full report](../providers/biorxiv.md)

### medRxiv API

- Free access: no published number — same service as bioRxiv; no published quota
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.medrxiv.org/ · docs https://api.biorxiv.org/ · llms.txt — · [full report](../providers/medrxiv.md)

### zbMATH Open

- Free access: no published number — no published quota captured
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://zbmath.org/ · docs https://api.zbmath.org/v1/ · llms.txt — · [full report](../providers/zbmath.md)

## Repositories & research-data archives

### Zenodo

- Free access: 2,592,000 calls/mo — guest 60 requests/minute and 2,000/hour; authenticated 100/minute and 5,000/hour
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://zenodo.org/ · docs https://developers.zenodo.org/ · llms.txt — · [full report](../providers/zenodo.md)

### DataONE

- Free access: no published number — not established
- Authentication: ? · confidence low · probe 200 JSON
- Links: home https://www.dataone.org/ · docs https://purl.dataone.org/architecture/apis/MN-API.html · llms.txt — · [full report](../providers/dataone.md)

### DataverseNL

- Free access: no published number — no published call quota captured
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://dataverse.nl/ · docs https://guides.dataverse.org/en/latest/api/ · llms.txt — · [full report](../providers/dataverse-nl.md)

### Dryad

- Free access: no published number — no published quota captured
- Authentication: ? · confidence low · probe 200 JSON
- Links: home https://datadryad.org/ · docs https://datadryad.org/api/v2/docs/ · llms.txt — · [full report](../providers/dryad.md)

### Figshare

- Free access: no published number — no automatic rate limiting in place for API requests
- Authentication: free key · confidence high · probe 200 JSON
- Links: home https://figshare.com/ · docs https://docs.figshare.com/ · llms.txt — · [full report](../providers/figshare.md)

### Harvard Dataverse

- Free access: no published number — no published call quota captured
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://dataverse.harvard.edu/ · docs https://guides.dataverse.org/en/latest/api/ · llms.txt — · [full report](../providers/dataverse.md)

### Hugging Face Hub

- Free access: no published number — limits are per request class and published through RateLimit headers, not as one table; the docs use '100 requests per 5 minutes' only as an example of the header format
- Authentication: free key · confidence medium · probe 200 JSON
- Links: home https://huggingface.co/ · docs https://huggingface.co/docs/hub/api · llms.txt — · [full report](../providers/huggingface.md)

### OSF (Open Science Framework)

- Free access: no published number — no published quota captured
- Authentication: ? · confidence low · probe 200 JSON
- Links: home https://osf.io/ · docs https://developer.osf.io/ · llms.txt — · [full report](../providers/osf.md)

### OpenML

- Free access: no published number — no published quota captured
- Authentication: ? · confidence low · probe 200 JSON
- Links: home https://www.openml.org/ · docs https://www.openml.org/apis · llms.txt — · [full report](../providers/openml.md)

### OpenReview

- Free access: no published number — no published call quota captured
- Authentication: ? · confidence low · probe 200 HTML
- Links: home https://openreview.net/ · docs https://docs.openreview.net/reference/api-v2 · llms.txt https://docs.openreview.net/llms.txt · [full report](../providers/openreview.md)

### Papers with Code

- Free access: no published number — no published quota captured
- Authentication: ? · confidence low · probe 200 HTML
- Links: home https://paperswithcode.com/ · docs https://paperswithcode.com/api/v1/docs/ · llms.txt — · [full report](../providers/paperswithcode.md)

### Thoth Open Metadata

- Free access: no published number — no published quota; GraphQL and export APIs
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://thoth.pub/ · docs https://api.thoth.pub/graphql · llms.txt — · [full report](../providers/thoth.md)

### re3data

- Free access: no published number — no published quota; the API is a plain REST interface
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.re3data.org/ · docs https://www.re3data.org/api/doc · llms.txt — · [full report](../providers/re3data.md)

## Life / physical science data APIs

### UniProt

- Free access: 518,400,000 calls/mo — 200 requests/second/user
- Authentication: none · confidence high · probe 200 JSON
- Links: home https://www.uniprot.org/ · docs https://www.uniprot.org/help/api · llms.txt — · [full report](../providers/uniprot.md)

### BioModels

- Free access: no published number — no published quota captured
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.ebi.ac.uk/biomodels/ · docs https://www.ebi.ac.uk/biomodels/docs/ · llms.txt — · [full report](../providers/biomodels.md)

### BioStudies (EBI)

- Free access: no published number — no published quota captured
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://www.ebi.ac.uk/biostudies/ · docs https://www.ebi.ac.uk/biostudies/api/v1/swagger-ui.html · llms.txt — · [full report](../providers/biostudies.md)

### ChEMBL

- Free access: no published number — no published quota captured
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://www.ebi.ac.uk/chembl/ · docs https://chembl.gitbook.io/chembl-interface-documentation/web-services · llms.txt https://chembl.gitbook.io/llms.txt · [full report](../providers/chembl.md)

### EBI Search

- Free access: no published number — no published quota captured
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://www.ebi.ac.uk/ebisearch/ · docs https://www.ebi.ac.uk/ebisearch/swagger.ebi · llms.txt — · [full report](../providers/ebisearch.md)

### EMBL-EBI Ontology Lookup Service

- Free access: no published number — no published quota captured
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://www.ebi.ac.uk/ols4/ · docs https://www.ebi.ac.uk/ols4/help · llms.txt — · [full report](../providers/ols.md)

### Ensembl REST

- Free access: no published number — no published quota captured; the REST root documents endpoints only
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://www.ensembl.org/ · docs https://rest.ensembl.org/ · llms.txt — · [full report](../providers/ensembl.md)

### GBIF

- Free access: no published number — no fixed rate; the docs say the maximum changes with server load
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.gbif.org/ · docs https://techdocs.gbif.org/en/openapi/ · llms.txt — · [full report](../providers/gbif.md)

### OBIS

- Free access: no published number — no published quota captured
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://obis.org/ · docs https://api.obis.org/ · llms.txt — · [full report](../providers/obis.md)

### PubChem PUG REST

- Free access: no published number — no published quota captured; the docs page returned a bot check to this client
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://pubchem.ncbi.nlm.nih.gov/ · docs https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest · llms.txt — · [full report](../providers/pubchem.md)

### RCSB PDB Data API

- Free access: no published number — no published quota captured
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://www.rcsb.org/ · docs https://data.rcsb.org/redoc/ · llms.txt — · [full report](../providers/pdb.md)

### iDigBio

- Free access: no published number — anonymous calls allowed; authenticating raises the limit
- Authentication: none · confidence medium · probe 200 JSON
- Links: home https://www.idigbio.org/ · docs https://github.com/iDigBio/idigbio-search-api/wiki · llms.txt — · [full report](../providers/idigbio.md)

### iNaturalist

- Free access: no published number — no published quota captured; the recommendations page returned 403
- Authentication: none · confidence low · probe 200 JSON
- Links: home https://www.inaturalist.org/ · docs https://api.inaturalist.org/v1/docs/ · llms.txt — · [full report](../providers/inaturalist.md)

## Publisher & patent TDM endpoints

### EPO Open Patent Services

- Free access: no published number — OAuth credentials required; published free quota is per-registered-user and was not captured
- Authentication: key on application · confidence low · probe needs key
- Links: home https://www.epo.org/ · docs https://developers.epo.org/ · llms.txt — · [full report](../providers/epo-ops.md)

### Elsevier Scopus / ScienceDirect API

- Free access: no published number — API key plus an entitlement per product; no free allowance published
- Authentication: paid only · confidence medium · probe needs key
- Links: home https://www.elsevier.com/ · docs https://dev.elsevier.com/ · llms.txt — · [full report](../providers/elsevier.md)

### IEEE Xplore API

- Free access: no published number — API key required; the docs page did not state a free quota
- Authentication: key on application · confidence medium · probe needs key
- Links: home https://developer.ieee.org/ · docs https://developer.ieee.org/docs · llms.txt — · [full report](../providers/ieee.md)

### JSTOR / Constellate

- Free access: no published number — not established; the API host did not resolve
- Authentication: ? · confidence low · probe no answer
- Links: home https://www.jstor.org/ · docs https://constellate.org/docs/ · llms.txt — · [full report](../providers/jstor-constellate.md)

### PatentsView

- Free access: no published number — API key required; the docs page rendered as an application shell
- Authentication: key on application · confidence low · probe 200 HTML
- Links: home https://patentsview.org/ · docs https://patentsview.org/apis/api-endpoints · llms.txt — · [full report](../providers/patentsview.md)

### Springer Nature API

- Free access: no published number — API key required; higher rate limits are a paid feature
- Authentication: paid only · confidence medium · probe needs key
- Links: home https://www.springernature.com/ · docs https://dev.springernature.com/ · llms.txt — · [full report](../providers/springer.md)

### USPTO Open Data Portal (IBD)

- Free access: no published number — no published quota captured; the API answered HTML rather than JSON
- Authentication: ? · confidence low · probe 200 HTML
- Links: home https://developer.uspto.gov/ · docs https://developer.uspto.gov/api-catalog · llms.txt — · [full report](../providers/uspto-ibd.md)

### Wiley TDM API

- Free access: no published number — TDM API token required; no free allowance captured
- Authentication: paid only · confidence low · probe no answer
- Links: home https://www.wiley.com/ · docs https://onlinelibrary.wiley.com/library-info/resources/text-and-datamining · llms.txt — · [full report](../providers/wiley.md)

