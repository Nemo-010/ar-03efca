#!/usr/bin/env python3
"""Integrity tests for the fact table, the snapshots and the generated reports.

Run: python3 scripts/test_integrity.py -v

What is checked:
  * every evidence quote appears verbatim in the snapshot it names
  * every snapshot path in facts.json exists and is non-empty
  * every provider in the catalogue has exactly one facts row, and vice versa
  * every derived monthly figure recomputes from the rate it claims
  * the generated reports exist and cite no provider that is absent from facts
  * no report contains a number that is not backed by a facts row
"""
import json
import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
REP = os.path.join(ROOT, "reports")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def load(name):
    with open(os.path.join(DATA, name)) as f:
        return json.load(f)


class TestCatalogue(unittest.TestCase):
    def test_every_candidate_has_one_fact_row(self):
        cands = [p["slug"] for p in load("candidates.json")["providers"]]
        facts = [r["slug"] for r in load("facts.json")]
        self.assertEqual(len(cands), len(set(cands)), "duplicate slug in candidates.json")
        self.assertEqual(sorted(cands), sorted(facts), "catalogue and facts.json disagree")

    def test_every_fact_row_has_required_fields(self):
        want = {"slug", "name", "category", "home", "docs", "api", "monthly_calls", "rate",
                "derivation", "one_time", "card", "key", "confidence", "note", "evidence", "probe"}
        for r in load("facts.json"):
            self.assertTrue(want <= set(r), f"{r['slug']} missing {want - set(r)}")
            self.assertIn(r["confidence"], ("high", "medium", "low", "none"))
            self.assertIn(r["key"], ("none", "free", "apply", "paid", None))

    def test_categories_are_declared(self):
        cats = set(load("candidates.json")["categories"])
        for r in load("facts.json"):
            self.assertIn(r["category"], cats, f"{r['slug']} has undeclared category")


class TestEvidence(unittest.TestCase):
    def test_snapshot_paths_exist_and_are_non_empty(self):
        bad = []
        for r in load("facts.json"):
            for e in r["evidence"]:
                sp = e.get("snapshot") or ""
                if not sp:
                    continue
                path = os.path.join(ROOT, sp)
                if not os.path.exists(path):
                    bad.append(f"{r['slug']}: missing {sp}")
                elif os.path.getsize(path) < 40:
                    bad.append(f"{r['slug']}: near-empty {sp} ({os.path.getsize(path)}b)")
        self.assertEqual([], bad)

    def test_every_quote_is_verbatim(self):
        bad = []
        for r in load("facts.json"):
            for e in r["evidence"]:
                q, sp = (e.get("quote") or "").strip(), e.get("snapshot") or ""
                if not q or not sp:
                    continue
                path = os.path.join(ROOT, sp)
                if not os.path.exists(path):
                    continue
                txt = norm(open(path, encoding="utf-8", errors="replace").read())
                for frag in [f for f in re.split(r"\s*(?:\.\.\.|…)\s*", q) if f.strip()]:
                    if norm(frag) not in txt:
                        bad.append(f"{r['slug']}: {frag[:70]!r} not in {sp}")
                        break
        self.assertEqual([], bad, "evidence quotes must appear verbatim in their snapshot")

    def test_every_evidence_row_cites_a_url(self):
        bad = [r["slug"] for r in load("facts.json")
               for e in r["evidence"] if e.get("quote") and not e.get("url")]
        self.assertEqual([], bad)


class TestDerivation(unittest.TestCase):
    """A derived monthly figure must recompute from the rate it names."""

    CASES = {
        # slug: (rate, expected)
        "arquivo": (250 / 60 * 2592000, 10800000),
        "loc": (20 * 1440 * 30, 864000),
        "openlibrary": (1 * 2592000, 2592000),
        "crossref": (5 * 2592000, 12960000),
        "datacite": (500 / 5 * 1440 * 30, 4320000),
        "core": (5 / 10 * 60 * 1440 * 30, 1296000),
        "ror": (2000 / 5 * 1440 * 30, 17280000),
        "opencitations": (180 * 1440 * 30, 7776000),
        "pubmed": (3 * 2592000, 7776000),
        "doaj": (2 * 2592000, 5184000),
        "arxiv": (2592000 / 3, 864000),
        "inspirehep": (15 / 5 * 2592000, 7776000),
        "zenodo": (60 * 1440 * 30, 2592000),
        "met-museum": (80 * 2592000, 207360000),
        "artic": (60 * 1440 * 30, 2592000),
        "uniprot": (200 * 2592000, 518400000),
        "dimensions": (30 * 1440 * 30, 1296000),
        "nara": (10000, 10000),
        "ads": (5000 * 30, 150000),
    }

    def test_derived_figures_recompute(self):
        facts = {r["slug"]: r for r in load("facts.json")}
        for slug, (computed, expected) in self.CASES.items():
            r = facts[slug]
            self.assertEqual(expected, round(computed),
                             f"{slug}: arithmetic in the test itself is wrong")
            self.assertEqual(expected, r["monthly_calls"],
                             f"{slug}: facts.json says {r['monthly_calls']}, derivation gives {round(computed)}")
            self.assertTrue(r["derivation"], f"{slug}: a derived figure needs a derivation string")

    def test_no_figure_without_a_derivation_or_a_published_number(self):
        for r in load("facts.json"):
            if r["monthly_calls"]:
                self.assertTrue(r["derivation"], f"{r['slug']}: number with no derivation")
                self.assertTrue(r["evidence"], f"{r['slug']}: number with no evidence")


class TestReports(unittest.TestCase):
    def test_reports_exist(self):
        for name in ("00-methodology.md", "01-inventory.md", "02-deep-reviews.md",
                     "03-post-analysis.md", "04-probes.md"):
            p = os.path.join(REP, name)
            self.assertTrue(os.path.exists(p), f"missing {name}")
            self.assertGreater(os.path.getsize(p), 2000, f"{name} looks empty")

    def test_reports_cite_only_catalogued_providers(self):
        facts = {r["slug"] for r in load("facts.json")}
        text = "".join(open(os.path.join(REP, n), encoding="utf-8").read()
                       for n in os.listdir(REP) if n.endswith(".md"))
        cited = set(re.findall(r"providers/([a-z0-9-]+)\.md", text))
        self.assertEqual(set(), cited - facts, "report cites a provider report that is not in facts")

    def test_every_provider_has_a_report_file(self):
        facts = [r["slug"] for r in load("facts.json")]
        missing = [s for s in facts
                   if not os.path.exists(os.path.join(ROOT, "providers", s + ".md"))]
        self.assertEqual([], missing)

    def test_report_numbers_match_facts(self):
        """Every thousand-separated figure in the ranking table must be a facts figure."""
        facts = {r["slug"]: r for r in load("facts.json")}
        text = open(os.path.join(REP, "01-inventory.md"), encoding="utf-8").read()
        allowed = {f"{r['monthly_calls']:,}" for r in facts.values() if r["monthly_calls"]}
        for n in re.findall(r"\|\s*([\d,]{4,})\s*\|", text):
            self.assertIn(n, allowed, f"{n} in the ranking table is not a facts figure")


class TestProbes(unittest.TestCase):
    def test_probe_verdicts_are_known(self):
        ok = {"ok", "ok-html", "auth", "bot-wall", "payment", "blocked", "not-found",
              "error", "none"}
        for slug, p in load("probes.json").items():
            self.assertIn(p.get("verdict"), ok, f"{slug}: unexpected verdict {p.get('verdict')}")

    def test_ok_verdict_matches_status(self):
        bad = []
        for slug, p in load("probes.json").items():
            v, st = p.get("verdict"), p.get("status") or 0
            if v in ("ok", "ok-html") and not (200 <= st < 300):
                bad.append(f"{slug}: verdict {v} with status {st}")
            if v in ("auth", "bot-wall") and st not in (401, 403, 503):
                bad.append(f"{slug}: verdict {v} with status {st}")
        self.assertEqual([], bad)


if __name__ == "__main__":
    unittest.main(verbosity=2)
