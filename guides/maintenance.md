# Maintaining the data

Give each brand a short, stable ID. Its position in the Cosign ranking can change without changing file paths.

Save the TasteLabs result in `data/raw/<id>.json` with its source URL and capture date. Preserve `result.design_system` and artifact references; leave out account identifiers, credit records, keys, and session metadata. Public links must not contain credentials.

Update the profile, tokens, and catalog together. Label selection notes as editorial interpretations so agents can distinguish a suggested use from an extracted color rule. Use `limited` for records that need additional source checks and describe the reason in `warnings` in both the catalog and tokens.

The catalog uses tags defined in `catalog/taxonomy.json`. Define a new tag before adding it to records. Update the grouped indexes, main table, and `llms.txt` when an entry point changes.

`data/manifest.json` stores each raw JSON file’s SHA-256 hash. Recalculate it when that file changes and keep the revision in Git. Run `python3 scripts/validate.py` and the tests before publishing. The validator checks consistency and links; visual assessment still requires looking at the design.

Keep lookup local. Refreshing an extraction should be a separate decision, since it can consume credits and replace earlier evidence.
