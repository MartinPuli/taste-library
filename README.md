# taste-library

<!-- count:default -->38<!-- /count --> website design references for coding agents, selected from the top 40 in [Cosign’s High Taste Companies ranking](https://cosign.co/questions/highest-taste-companies) and extracted with [TasteLabs](https://www.tastelabs.com/).

Give your agent a brief and this repo. It can find relevant references, compare documented patterns, and cite the typography, layout, or controls behind its decisions.

## Give this to your agent

> Read [AGENTS.md](AGENTS.md). Use this library to choose a design reference for my project before building the UI. Compare candidates against my audience, content, and primary task; explain the choice and cite the sections you use.

For a reusable workflow, copy [skills/taste-library](skills/taste-library) into your agent’s supported skills directory. Its instructions work with a local checkout or the public files on GitHub. See [agent access](guides/agent-access.md).

## Find a reference

Python 3.9+ and its standard library are enough; local queries need no account or API key.

~~~sh
python3 scripts/query.py search --use-case developer-tools --component buttons
python3 scripts/query.py search 'warm editorial' --limit 5
python3 scripts/query.py show linear
python3 scripts/query.py show linear --section typography
python3 scripts/query.py compare linear cursor --section actions --json
~~~

Search supports project type, style, and documented component filters. Word matches and Cosign rank help order candidates; they do not decide which reference fits your brief.

## Read only what the task needs

| Entry point | Use it for |
|---|---|
| [Compact catalog](catalog/search.json) | Find candidates without loading their extractions |
| [Reference index](catalog/INDEX.md) | Browse names, project types, styles, and components |
| [Component index](catalog/by-component.md) | Find forms, navigation, cards, or other documented patterns |
| [Profiles](profiles) | Read selection advice, content requirements, and capture observations |
| [Section files](data/sections) | Retrieve one section with its source, date, and evidence pointer |
| [Tokens](data/tokens) | Read extracted palettes, type variants, grids, and breakpoints |
| [Capture reviews](data/reviews) | See exactly what the screenshot and CSS checks covered |
| [Full results](data/raw) | Inspect the original extraction when more context is needed |

The repo preserves 40 source records. Default search excludes limited records; use --include-limited to inspect the full collection. Small [image previews](data/previews) help agents with vision inspect the saved composition. Profiles also link to the original full captures.

The [worked examples](guides/worked-examples.md) show how to turn a brief into a documented choice. Use the [decision template](guides/decision-template.md) to record the result.

## Where the information comes from

Cosign supplies the ranking. TasteLabs supplies the website extractions. This repo adds retrieval, editorial guidance, and review records.

Each raw record preserves the complete stored TasteLabs result, including artifact metadata. The section files split that result without summarizing it. Original HTML, CSS, screenshots, and element-layout files remain hosted by TasteLabs; profiles link to them. The repository stores their URLs and small derived image previews, not an offline copy of every artifact. See the [completeness audit](guides/data-coverage.md).

The collection follows the ranking checked on October 14, 2026. Every reference keeps its own capture date. These are observations of particular web pages, not official brand manuals. Capture reviews cover visible composition and literal CSS checks; they do not certify interaction behavior or responsive layouts.

## Maintain the library

~~~sh
python3 scripts/build.py
python3 scripts/validate.py
python3 -m unittest discover -s tests
~~~

End-to-end checks use [Tester Army e2e](https://tester.army/e2e) as a development dependency. See [validation](guides/validation.md) for commands and coverage; ordinary library queries still need only Python.

See [maintenance](guides/maintenance.md) for data updates and [agent packaging decisions](guides/agent-packaging.md) for the official specifications consulted in October 2026. [RIGHTS.md](RIGHTS.md) describes the third-party material.
