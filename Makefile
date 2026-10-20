.PHONY: all fetch probe llms facts reports test check check-full clean

all: fetch probe llms facts reports test

fetch:
	python3 scripts/fetch.py

probe:
	python3 scripts/probe.py

llms:
	python3 scripts/llms.py --fetch

facts:
	python3 scripts/facts.py

reports: facts
	python3 scripts/build_reports.py

test:
	python3 scripts/test_integrity.py

check:
	python3 scripts/check.py

check-full:
	python3 scripts/check.py --limit 0

clean:
	rm -rf data/snapshots data/probes.json data/facts.json data/llms.json reports providers
