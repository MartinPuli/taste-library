# taste-library

Design references from the **top 40 companies in [Cosign’s High Taste Companies ranking](https://cosign.co/questions/highest-taste-companies)**, extracted with TasteLabs and organized for AI agents.

Give an agent a brief. It can search by style or project type, compare references, and read the colors, typography, layout, or interactions it needs to make a design decision.

## Start here

Read [AGENTS.md](AGENTS.md), then browse the [reference index](catalog/INDEX.md) or search locally:

```sh
python3 scripts/query.py search 'warm editorial' --limit 5
python3 scripts/query.py search --use-case developer-tools --style dark-technical
python3 scripts/query.py show linear
python3 scripts/query.py show linear --section typography
```

Python’s standard library is enough. Search runs locally and matches words and tags, so reading the collection requires no API calls. Add `--json` to `search` for structured results.

The [selection guide](guides/selection.md) helps an agent compare references against the brief. The [decision template](guides/decision-template.md) records what to borrow, what to adapt, and why.

## What agents can read

| Path | Contents |
|---|---|
| [catalog/index.json](catalog/index.json) | Searchable catalog with use cases, styles, evidence metadata, and file paths |
| [catalog/INDEX.md](catalog/INDEX.md) | All 40 companies in one table |
| [catalog/by-use-case.md](catalog/by-use-case.md) | References grouped by project type |
| [catalog/by-style.md](catalog/by-style.md) | References grouped by visual approach |
| `profiles/<id>.md` | Short profiles for comparing candidates |
| `data/tokens/<id>.json` | Extracted colors, type styles, grids, and breakpoints |
| `data/raw/<id>.json` | Full design-system results and links to captured artifacts |
| [data/manifest.json](data/manifest.json) | Capture dates, sources, and file hashes |

Read a profile first, then open the specific section needed for the task. Stable IDs such as `linear` and `teenage-engineering` keep paths independent of ranking changes. [llms.txt](llms.txt) lists the entry points for tools that support it.

## Source

**Cosign supplies the ranking. TasteLabs supplies the website extractions.** This repository adds the indexes, short profiles, and guidance for choosing references.

The collection follows Cosign’s ranking as checked on October 14, 2026. Each record preserves its own capture date and source URL. Use-case tags and selection notes are editorial interpretations of the extracted pages; the files describe observed website design rather than official brand manuals.

## Maintain the collection

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

See the [maintenance guide](guides/maintenance.md) to add a reference while preserving its source. [RIGHTS.md](RIGHTS.md) covers third-party materials.
