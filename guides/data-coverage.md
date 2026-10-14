# What the library preserves

The collection contains the 40 selected stored extractions from Cosign's top 40. Default discovery includes 38 references. It does not include every extraction in the owner's TasteLabs account.

The file data/sections/a24/profile.json contains only A24's extracted profile section. Read [data/raw/a24.json](../data/raw/a24.json) for its complete result, or use [A24's profile](../profiles/a24.md) to navigate its sections and original captured files.

## Export fidelity

On October 14, 2026, we retrieved all 40 existing results again with get_brand_extraction_result and no section filter. We compared each entire result object against its raw record, including the design system and artifact metadata. No new extraction ran.

All 40 results matched exactly. All 600 section files matched the corresponding source values. Of those sections, 568 contain data and 32 have no observed values in the stored result; the export preserves those empty values. A match establishes that the export retained the source data, not that every source interpretation is accurate.

The [audit report](../data/audits/tastelabs-2026-10-14.json) records per-reference hashes, equality checks, and availability checks for the 191 non-null original artifact links. The 40 results each have five artifact slots; nine slots are null and remain null.

## Files and links

Full raw results preserve every field under result. Files under data/sections/ contain one original section plus provenance. Profiles and token summaries are access aids; they do not replace the raw result.

Original HTML, CSS, viewport captures, full-page captures, and element-layout JSON stay hosted by TasteLabs. The repo preserves their URLs, paths, and content types; its WebP previews are derived crops. External files are not an offline archive. The availability check requests headers, so a successful response confirms reachability at the recorded time, not a byte-for-byte audit of each remote file.

Account identifiers, credit records, and other service bookkeeping are outside the public design dataset. Capture dates and source URLs are retained.

## Repeat the check

Retrieve each selected stored extraction without a section filter. Save the structured response as <id>.json in a private snapshot directory; retain source_url, completed_at, status, sections, and result. The script accepts that response or a sanitized snapshot and never starts an extraction.

~~~sh
python3 scripts/audit_tastelabs.py --snapshot-dir /path/to/snapshots \
  --check-artifacts --output data/audits/tastelabs-2026-10-14.json
~~~

The completeness test in [Tester Army](../tests/e2e/completeness.e2e.ts) fetches every published raw record and all 600 section files. It compares raw-file hashes with this audit, then verifies section content and provenance. Set TASTE_LIBRARY_BASE_URL as described in [validation](validation.md). A later source update requires a new audit of the affected records before these checks can pass.
