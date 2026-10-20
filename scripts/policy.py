#!/usr/bin/env python3
"""Fetch the pages that document each provider's allowance, rate limit or terms.

The home/docs pages captured by fetch.py rarely state a quota. This adds a
`policy` snapshot per provider pointing at the page that actually carries the
number (a rate-limit page, a terms page, a pricing page, an FAQ).

Run: python3 scripts/policy.py [slug ...]
"""
import concurrent.futures as cf
import gzip
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import fetch, to_text, SNAP  # noqa: E402

POLICY = {
 "wayback-cdx": [("policy", "https://archive.org/developers/wayback-cdx-server.html"),
                 ("policy2", "https://archive.org/about/terms.php")],
 "wayback-availability": [("policy", "https://archive.org/developers/wayback-cdx-server.html")],
 "wayback-save": [("policy", "https://archive.org/developers/wayback-save.html")],
 "ia-metadata": [("policy", "https://archive.org/developers/md-read.html")],
 "ia-fulltext": [("policy", "https://archive.org/developers/search_inside.html")],
 "fatcat": [("policy", "https://guide.fatcat.wiki/")],
 "commoncrawl": [("policy", "https://commoncrawl.org/terms-of-use")],
 "arquivo": [("policy", "https://arquivo.pt/api")],
 "ukwa": [("policy", "https://www.webarchive.org.uk/en/ukwa/info/api")],
 "archive-today": [("policy", "https://archive.ph/faq")],
 "memento": [("policy", "http://timetravel.mementoweb.org/guide/api/")],
 "perma": [("policy", "https://perma.cc/docs/developer")],
 "conifer": [("policy", "https://conifer.rhizome.org/api/docs")],
 "softwareheritage": [("policy", "https://archive.softwareheritage.org/api/")],
 "nara": [("policy", "https://www.archives.gov/research/catalog/help/api")],
 "tna-discovery": [("policy", "https://discovery.nationalarchives.gov.uk/API/site/help")],
 "snac": [("policy", "https://api.snaccooperative.org/")],
 "europeana": [("policy", "https://europeana.atlassian.net/wiki/spaces/EF/pages/2477260801/API+documentation"),
               ("policy2", "https://www.europeana.eu/en/rights/api-terms-of-use")],
 "dpla": [("policy", "https://pro.dp.la/developers/api-codex")],
 "digitalnz": [("policy", "https://digitalnz.org/developers/api")],
 "trove": [("policy", "https://trove.nla.gov.au/about/create-something/using-api")],
 "smithsonian": [("policy", "https://edan.si.edu/openaccess/apidocs/")],
 "loc": [("policy", "https://www.loc.gov/apis/")],
 "chroniclingamerica": [("policy", "https://www.loc.gov/apis/additional-apis/chronicling-america-api/")],
 "gallica": [("policy", "https://api.bnf.fr/fr/api-document-de-gallica")],
 "hathitrust": [("policy", "https://www.hathitrust.org/bib_api")],
 "openlibrary": [("policy", "https://openlibrary.org/developers/api")],
 "gutenberg": [("policy", "https://gutendex.com/")],
 "wikidata": [("policy", "https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual")],
 "wikipedia-api": [("policy", "https://www.mediawiki.org/wiki/API:Etiquette")],
 "openalex": [("policy", "https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication")],
 "crossref": [("policy", "https://www.crossref.org/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/")],
 "datacite": [("policy", "https://support.datacite.org/docs/api")],
 "semanticscholar": [("policy", "https://www.semanticscholar.org/product/api")],
 "core": [("policy", "https://core.ac.uk/services/api")],
 "openaire-graph": [("policy", "https://graph.openaire.eu/docs/")],
 "openaire-search": [("policy", "https://api.openaire.eu/")],
 "base": [("policy", "https://api.base-search.net/")],
 "orcid": [("policy", "https://info.orcid.org/documentation/api-reference/")],
 "ror": [("policy", "https://ror.readme.io/docs/rest-api")],
 "dblp": [("policy", "https://dblp.org/faq/How+to+use+the+dblp+search+API.html")],
 "opencitations": [("policy", "https://opencitations.net/index/api/v2")],
 "crossref-eventdata": [("policy", "https://www.eventdata.crossref.org/guide/")],
 "dimensions": [("policy", "https://docs.dimensions.ai/dsl/api.html")],
 "lens": [("policy", "https://docs.api.lens.org/")],
 "scite": [("policy", "https://api.scite.ai/")],
 "altmetric": [("policy", "https://api.altmetric.com/")],
 "sherpa-romeo": [("policy", "https://v2.sherpa.ac.uk/api/")],
 "pubmed": [("policy", "https://www.ncbi.nlm.nih.gov/books/NBK25497/")],
 "europepmc": [("policy", "https://europepmc.org/RestfulWebService")],
 "pmc-oa": [("policy", "https://www.ncbi.nlm.nih.gov/pmc/tools/oa-service/")],
 "pmc-idconv": [("policy", "https://www.ncbi.nlm.nih.gov/pmc/tools/id-converter-api/")],
 "doaj": [("policy", "https://doaj.org/api/v4/docs")],
 "unpaywall": [("policy", "https://unpaywall.org/products/api")],
 "arxiv": [("policy", "https://info.arxiv.org/help/api/tou.html")],
 "biorxiv": [("policy", "https://api.biorxiv.org/")],
 "hal": [("policy", "https://api.archives-ouvertes.fr/docs")],
 "ads": [("policy", "https://ui.adsabs.harvard.edu/help/api/")],
 "inspirehep": [("policy", "https://github.com/inspirehep/rest-api-doc")],
 "zbmath": [("policy", "https://api.zbmath.org/v1/")],
 "clinicaltrials": [("policy", "https://clinicaltrials.gov/data-api/api")],
 "scielo": [("policy", "https://articlemeta.scielo.org/api/v1/")],
 "lareferencia": [("policy", "https://api.lareferencia.info/v1/")],
 "oapen": [("policy", "https://library.oapen.org/rest/")],
 "oapen-api": [("policy", "https://api.oapen.org/")],
 "doab": [("policy", "https://directory.doabooks.org/rest/")],
 "ndltd": [("policy", "https://union.ndltd.org/OAI-PMH")],
 "zenodo": [("policy", "https://developers.zenodo.org/")],
 "figshare": [("policy", "https://docs.figshare.com/")],
 "dryad": [("policy", "https://datadryad.org/api/v2/docs/")],
 "osf": [("policy", "https://developer.osf.io/")],
 "dataverse": [("policy", "https://guides.dataverse.org/en/latest/api/")],
 "dataverse-nl": [("policy", "https://guides.dataverse.org/en/latest/api/")],
 "openml": [("policy", "https://www.openml.org/apis")],
 "huggingface": [("policy", "https://huggingface.co/docs/hub/api")],
 "paperswithcode": [("policy", "https://paperswithcode.com/api/v1/docs/")],
 "openreview": [("policy", "https://docs.openreview.net/reference/api-v2")],
 "dataone": [("policy", "https://purl.dataone.org/architecture/apis/MN-API.html")],
 "re3data": [("policy", "https://www.re3data.org/api/doc")],
 "thoth": [("policy", "https://api.thoth.pub/graphql")],
 "gbif": [("policy", "https://techdocs.gbif.org/en/openapi/")],
 "uniprot": [("policy", "https://www.uniprot.org/help/api")],
 "pdb": [("policy", "https://data.rcsb.org/redoc/")],
 "ensembl": [("policy", "https://rest.ensembl.org/")],
 "chembl": [("policy", "https://chembl.gitbook.io/chembl-interface-documentation/web-services")],
 "pubchem": [("policy", "https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest")],
 "biostudies": [("policy", "https://www.ebi.ac.uk/biostudies/api/v1/swagger-ui.html")],
 "ebisearch": [("policy", "https://www.ebi.ac.uk/ebisearch/swagger.ebi")],
 "ols": [("policy", "https://www.ebi.ac.uk/ols4/help")],
 "biomodels": [("policy", "https://www.ebi.ac.uk/biomodels/docs/")],
 "obis": [("policy", "https://api.obis.org/")],
 "idigbio": [("policy", "https://github.com/iDigBio/idigbio-search-api/wiki")],
 "inaturalist": [("policy", "https://api.inaturalist.org/v1/docs/")],
 "osti": [("policy", "https://www.osti.gov/api/v1/docs")],
 "ntrs": [("policy", "https://sti.nasa.gov/ntrs-api/")],
 "cds-cern": [("policy", "https://cds.cern.ch/help/hacking")],
 "jstage": [("policy", "https://www.jstage.jst.go.jp/static/pages/JstageServices/TAB3/-char/en")],
 "repec": [("policy", "https://ideas.repec.org/")],
 "elsevier": [("policy", "https://dev.elsevier.com/")],
 "springer": [("policy", "https://dev.springernature.com/")],
 "wiley": [("policy", "https://onlinelibrary.wiley.com/library-info/resources/text-and-datamining")],
 "ieee": [("policy", "https://developer.ieee.org/docs")],
 "epo-ops": [("policy", "https://developers.epo.org/")],
 "patentsview": [("policy", "https://patentsview.org/apis/api-endpoints")],
 "uspto-ibd": [("policy", "https://developer.uspto.gov/api-catalog")],
 "jstor-constellate": [("policy", "https://constellate.org/docs/")],
 "openverse": [("policy", "https://api.openverse.org/v1/")],
 "met-museum": [("policy", "https://metmuseum.github.io/")],
 "artic": [("policy", "https://api.artic.edu/docs/")],
 "cleveland-art": [("policy", "https://openaccess-api.clevelandart.org/")],
 "id-loc": [("policy", "https://id.loc.gov/")],
 "dnb-sru": [("policy", "https://www.dnb.de/EN/Professionell/Metadatendienste/metadatendienste_node.html")],
 "k10plus-sru": [("policy", "https://projekt.mvb10plus.de/")],
 "nb-no": [("policy", "https://api.nb.no/catalog/swagger-ui.html")],
 "finna": [("policy", "https://api.finna.fi/")],
 "viaf": [("policy", "https://viaf.org/viaf/data/")],
}


def one(slug: str) -> str:
    """Fetch the policy pages for one provider into its snapshot directory."""
    got = []
    for kind, url in POLICY.get(slug, []):
        res = fetch(url)
        raw = res.pop("raw")
        d = os.path.join(SNAP, slug)
        os.makedirs(d, exist_ok=True)
        if res["status"] == 200:
            with gzip.open(os.path.join(d, kind + ".gz"), "wb", compresslevel=9) as f:
                f.write(raw)
            txt = to_text(raw, res["content_type"])
            with open(os.path.join(d, kind + ".txt"), "w") as f:
                f.write(txt)
            res["text_bytes"] = len(txt)
        meta_path = os.path.join(d, "meta.json")
        meta = json.load(open(meta_path)) if os.path.exists(meta_path) else {
            "slug": slug, "sources": {}}
        meta.setdefault("sources", {})[kind] = res
        with open(meta_path, "w") as f:
            json.dump(meta, f, indent=1)
        got.append(f"{kind}:{res['status']}")
        time.sleep(0.05)
    return f"{slug:24s} " + " ".join(got)


def main():
    want = sys.argv[1:] or sorted(POLICY)
    with cf.ThreadPoolExecutor(6) as ex:
        for f in cf.as_completed([ex.submit(one, s) for s in want]):
            print(f.result(), flush=True)


if __name__ == "__main__":
    main()
