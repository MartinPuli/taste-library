# Access paths

The public repository is [MartinPuli/taste-library](https://github.com/MartinPuli/taste-library).

For a local checkout, resolve paths relative to its root. For remote reads, prepend:

~~~text
https://raw.githubusercontent.com/MartinPuli/taste-library/main/
~~~

Read catalog/search.json first. Its profile field points to a concise profile. Profiles link directly to evidence sections. Read catalog/taxonomy.json when selecting filters, and catalog/index.json when you need exact component pointers or section coverage.

| Path | Content |
|---|---|
| profiles/<id>.md | Suggested fit, content requirements, capture notes |
| data/sections/<id>/<section>.json | One extracted section with provenance |
| data/reviews/<id>.json | What was checked and what remains untested |
| data/previews/<id>.webp | A resized top-of-capture preview for visual inspection |

For reproducible decisions, replace main in the URL with the commit SHA of the checkout used. A reference ID remains stable when a ranking changes.

~~~sh
python3 scripts/query.py search --use-case hardware --component buttons
python3 scripts/query.py search --style warm-editorial
python3 scripts/query.py search --component forms --json
python3 scripts/query.py show paper --section layout
python3 scripts/query.py compare paper figma --section actions --json
~~~

Supported section names: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, brand_assets, sections.

The repository runs without extra dependencies on Python 3.9+. An agent without a terminal can read the same files over HTTPS; an agent without web access needs a local checkout. Report unavailable access rather than inventing the contents.
