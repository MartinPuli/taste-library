# Worked reference choices

These are example briefs and editorial decisions, not client projects or measured design outcomes.

## A developer tool with a warm, readable presentation

**Brief:** A desktop code-review tool needs a landing page for small engineering teams. The team has real editor screenshots but no custom photography. The existing identity uses a light background.

~~~sh
python3 scripts/query.py search --use-case developer-tools --component buttons --limit 10
python3 scripts/query.py compare cursor linear --section layout --json
python3 scripts/query.py compare cursor linear --section typography --json
~~~

**Choice:** Cursor is the primary reference because its saved page places an editor demonstration on a warm light surface. Linear remains a useful comparison for dense interface presentation; adopting its dark page would require changing the brief's established direction.

**Evidence and adaptation:** Cursor's [layout](../data/sections/cursor/layout.json) records a 24-column grid and a 1300px maximum width at /data/grid. Its [typography](../data/sections/cursor/typography.json) records a 4.5rem display heading with 1.1 line height at /data/titles/variants/0/specs. Use the hierarchy as a reference, then fit the project's existing typeface and screenshot proportions. Do not assume the extracted font is available to reuse.

The [capture observation](../data/reviews/cursor.json) supports the light composition and large editor demonstration. It does not verify a mobile layout. Test the implemented page at its actual breakpoints.

## A research publication with substantial reading

**Brief:** A research group publishes long reports for policy readers. It has strong writing and a few illustrations. Reading reports is the primary action; an email signup is secondary.

~~~sh
python3 scripts/query.py search --use-case editorial-research --style warm-editorial --limit 10
python3 scripts/query.py compare anthropic pangram --section typography --json
python3 scripts/query.py compare anthropic pangram --section actions --json
~~~

**Choice:** Anthropic is the primary reference for its restrained research presentation and distinction between the headline and introduction. Pangram offers a useful contrast: its prominent product trial action is less suited to a reading-first brief.

**Evidence and adaptation:** Anthropic's [typography](../data/sections/anthropic/typography.json) records a responsive display size at /data/titles/variants/0/specs/size. Its [layout](../data/sections/anthropic/layout.json) retains a variable gutter at /data/grid/gutter. Keep those expressions intact as evidence; choose project-specific values during implementation.

The [saved capture](../data/reviews/anthropic.json) supports the warm surface and contrasting headline/introduction treatment. Use the group's own illustrations and a licensed font pairing. The [actions section](../data/sections/anthropic/actions.json) documents a product CTA at /data/button_list/0; adapt that position to “Read the latest report” rather than inheriting the original conversion goal.
