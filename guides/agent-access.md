# Read the collection from an agent

## Local checkout

Read [AGENTS.md](../AGENTS.md), then use Python 3.9+:

~~~sh
python3 scripts/query.py search --use-case fintech --component forms
python3 scripts/query.py show ramp --section actions
python3 scripts/query.py compare ramp stripe --section layout --json
~~~

The CLI reads local files. It makes no network requests. Search has a default limit of five; --limit accepts 1 through 40. Add --include-limited when inspecting all source records, and --json when another program will consume the result.

Search requires all supplied filters to match; text uses weighted word matches. An unknown filter or reference returns an error. A valid search with no matches returns an empty list in JSON mode. Compare accepts two to four distinct reference IDs and a section name.

## Remote reading

An agent with HTTPS access can start with the [compact catalog](https://raw.githubusercontent.com/MartinPuli/taste-library/main/catalog/search.json). Resolve its profile paths against this base:

~~~text
https://raw.githubusercontent.com/MartinPuli/taste-library/main/
~~~

Profiles link to per-section JSON. A section response contains the original data plus source URL, capture date, quality flags, and an evidence pointer. A has_data value of false means the stored section contains no observed values; a missing file or failed request is a retrieval error.

For reproducible citations, replace main in the URL with the commit SHA used for the decision. Read [the full catalog](../catalog/index.json) only when you need component evidence pointers or section coverage.

## Reusable skill

Copy the entire [skills/taste-library](../skills/taste-library) directory into a skills directory supported by your agent. The folder includes its own access reference and does not depend on neighboring repository files. A checkout enables local queries; otherwise it points to the public dataset.

Clients differ in where they discover skills. This repo supplies the standard SKILL.md package without changing your agent configuration. An agent that does not support skills can follow AGENTS.md directly.

## Citation format

Name the reference, captured date, file, and JSON pointer. For example:

~~~text
Linear, captured 2026-10-10:
data/sections/linear/actions.json
/data/button_list/0/specs
~~~

The section's source_pointer maps back to the full raw result. Visual observations cite data/reviews/<id>.json; editorial adaptations should be identified as your recommendation.
