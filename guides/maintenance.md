# Maintaining the data

Give each brand a short, stable ID. Its position in the Cosign ranking can change without changing file paths.

Save the TasteLabs result in `data/raw/<id>.json` with its source URL and capture date. Preserve `result.design_system` and artifact references; leave out account identifiers, credit records, keys, and session metadata. Public links must not contain credentials.

Update the profile, tokens, and catalog together. Label selection notes as editorial interpretations so agents can distinguish a suggested use from an extracted color rule. Use `limited` for records that need additional source checks and describe the reason in `warnings` in both the catalog and tokens.

The catalog uses tags defined in `catalog/taxonomy.json`. Define a new tag before adding it to records. Update the grouped indexes, main table, and `llms.txt` when an entry point changes.

`data/manifest.json` stores each raw JSON file’s SHA-256 hash. Recalculate it when that file changes and keep the revision in Git. Run `python3 scripts/validate.py` and the tests before publishing. The validator checks consistency and links; visual assessment still requires looking at the design.

## Regenerate and validate

After updating evidence, run:

~~~sh
python3 scripts/build.py
python3 scripts/validate.py
python3 -m unittest discover -s tests
~~~

The builder generates per-section files, component pointers, profiles, the compact catalog, and grouped indexes. Edit selection notes and tags in catalog/index.json; edit review observations in data/reviews/. Keep metadata derived from sources out of manual edits.

Review records store the raw-file hash, capture URL and hash, the literal CSS checks performed, and what was not tested. A visual review of a saved image is not a live behavior test. Previews are resized crops of the saved capture's top area; keep a link to the original capture in the profile.

When syncing a stored TasteLabs result, compare every section first. Archive a changed raw record under data/history/<id>/ before replacing it, update its manifest hash, and record recovered sections in the review. Update warnings when their supporting condition changes. The Wander record demonstrates this procedure.

Public counts come from catalog entries and quality flags. The builder updates count markers in the README and launch draft. Do not promote a record's quality solely because an extraction finished or a CSS string matched.

When raw evidence changes, repeat the [stored-result audit](data-coverage.md) and update its report before publishing. The validator and full-collection HTTP test compare raw-file hashes against that audit, so an old report cannot silently certify a changed export.

Keep lookup local. Refreshing an extraction should be a separate decision, since it can consume credits and replace earlier evidence.
