# Validation

The repository checks evidence consistency and the retrieval paths an agent uses. They do not measure subjective design quality or certify the source websites' behavior.

## Data and local queries

Python 3.9+ is enough for these checks:

~~~sh
python3 scripts/build.py
python3 scripts/validate.py
python3 -m unittest discover -s tests
~~~

The validator checks the top-40 inventory, raw hashes, capture dates, component pointers, generated sections, compact catalog, previews, and local Markdown links. The Python tests also check absent values, invalid queries, and detection of altered evidence.

## Tester Army

[Tester Army e2e](https://tester.army/e2e) is pinned to 0.20.0 in the development lockfile. The tests use its [value assertions and engine-free target](https://e2e.tester.army/docs/api-testing) for subprocess and HTTP checks. They make no model calls and need no account or API key. Node 24.8+ is required on the Node 24 line; Node 22.22.3+ and newer supported releases also work.

~~~sh
npm ci --ignore-scripts
E2E_TELEMETRY_DISABLED=1 npm run test:e2e -- tests/e2e/local.e2e.ts
~~~

The five CLI journeys cover:

- A developer-tool brief: discovery, profile reading, comparison, and source tracing.
- A research-publication brief: editorial filters and preservation of CSS expressions.
- Default counts, limited-record opt-in, and absent evidence.
- Empty searches and invalid requests, including repeated comparison IDs.
- Component evidence lookup and comparison of four references.

To check public reading, set the base to a raw GitHub URL ending in a branch or commit and run the three HTTP journeys:

~~~sh
TASTE_LIBRARY_BASE_URL=https://raw.githubusercontent.com/MartinPuli/taste-library/main/ \
E2E_TELEMETRY_DISABLED=1 npm run test:e2e -- tests/e2e/remote.e2e.ts
~~~

For reproducible results, replace main with the commit being checked. Without the environment variable, the HTTP tests are explicitly skipped. A local file-server base can test unpublished changes. The CI workflow starts a temporary file server and runs all nine journeys, then stops it.

HTTP tests open the agent guide, compact catalog, standalone skill, and access reference. For both example briefs they follow actual profile links to section files, read the original evidence, and compare content and capture metadata.

The ninth test checks the entire collection: all 40 raw files against the fresh TasteLabs audit and all 600 section files against the original values. Run it with the same environment variables and tests/e2e/completeness.e2e.ts, or omit the file argument to run every journey. See [data coverage](data-coverage.md) for the audit method and original-file availability checks.

## Recorded check

On October 14, 2026, all 12 Python tests and all eight Tester Army journeys passed against the local checkout and its temporary file server. The skill passed the skill-creator metadata validator. The original Wander result was confirmed byte-for-byte against its archived copy before the recovered evidence was published.

The three HTTP journeys also passed against [published commit 026d80c](https://github.com/MartinPuli/taste-library/commit/026d80c10b91535c1a9e6cbfefcef1b52a90406b), using its immutable raw GitHub URLs. The checks covered public discovery and source tracing for both example briefs.

A subsequent full-data audit on the same day retrieved all 40 stored TasteLabs responses again and confirmed exact equality. The new completeness test fetched all 40 raw files and 600 sections from the published main branch at commit 9d21fe24571d7d4a2937bdc6cd86ed7ac791f3f2; it passed. All 191 original artifact URLs returned HTTP 200, and the expanded Python suite passed all 14 tests.

Tester Army writes a Markdown report to .e2e/summary.md. Run artifacts remain local and are ignored by Git.
