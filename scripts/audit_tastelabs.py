#!/usr/bin/env python3
"""Compare complete stored TasteLabs responses with this collection; never extract."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(',', ':')).encode('utf-8')).hexdigest()


def check_link(item):
    id, kind, url = item
    result = {'id': id, 'artifact': kind, 'url': url}
    try:
        request = urllib.request.Request(url, method='HEAD')
        try:
            response = urllib.request.urlopen(request, timeout=25)
        except urllib.error.HTTPError as error:
            if error.code != 405:
                raise
            response = urllib.request.urlopen(urllib.request.Request(
                url, headers={'Range': 'bytes=0-0'}), timeout=25)
        with response:
            result.update(status=response.status,
                          content_type=response.headers.get('Content-Type'),
                          content_length=response.headers.get('Content-Length'))
    except (OSError, urllib.error.URLError) as error:
        result['error'] = str(error)
    return result


def audit(snapshot_dir, check_artifacts=False):
    catalog = json.loads((ROOT/'catalog/index.json').read_text())
    records, links = [], []
    for entry in catalog['entries']:
        id = entry['id']
        raw_path = ROOT/entry['paths']['raw']
        raw = json.loads(raw_path.read_text())
        # Accept a full tool structuredContent response or a sanitized snapshot.
        fresh = json.loads((snapshot_dir/(id+'.json')).read_text())
        system = fresh['result']['design_system']
        section_matches = {}
        for name, value in system.items():
            section_path = entry['sections'].get(name, {}).get('path')
            section_matches[name] = bool(section_path) and json.loads(
                (ROOT/section_path).read_text())['data'] == value
        record = {
            'id': id, 'source_url': fresh['source_url'],
            'captured_at': fresh['completed_at'],
            'source_selection': fresh.get('sections'),
            'raw_file': entry['paths']['raw'],
            'raw_sha256': hashlib.sha256(raw_path.read_bytes()).hexdigest(),
            'remote_result_sha256': digest(fresh['result']),
            'local_result_sha256': digest(raw['result']),
            'full_result_matches': raw['result'] == fresh['result'],
            'provenance_matches': all(raw[k] == fresh[k] for k in ['source_url','completed_at','status']),
            'section_inventory_matches': set(entry['sections']) == set(system),
            'section_matches': section_matches,
        }
        records.append(record)
        for kind, artifact in fresh['result']['artifacts'].items():
            if artifact:
                links.append((id, kind, artifact['url']))
    if check_artifacts:
        with ThreadPoolExecutor(max_workers=8) as pool:
            checked_links = list(pool.map(check_link, links))
    else:
        checked_links = []
    return {
        'checked_at': datetime.now(timezone.utc).isoformat(),
        'method': 'Fresh get_brand_extraction_result responses with no section filter; exact JSON equality for the entire result, including artifact metadata, arrays, and null values.',
        'result_hash_method': 'SHA-256 of UTF-8 JSON with sorted keys, no ASCII escaping, and compact separators.',
        'scope': 'All 40 selected stored extractions. This checks export fidelity and link availability, not the accuracy of TasteLabs interpretations or the completeness of the source websites.',
        'artifact_storage': 'Original files stay at the TasteLabs URLs; the repository stores their metadata and links, plus derived image previews.',
        'counts': {
            'records': len(records),
            'matching_results': sum(r['full_result_matches'] for r in records),
            'sections': sum(len(r['section_matches']) for r in records),
            'matching_sections': sum(sum(r['section_matches'].values()) for r in records),
            'available_artifact_links': len(links),
            'checked_artifact_links': len(checked_links),
            'reachable_artifact_links': sum(200 <= r.get('status', 0) < 300 for r in checked_links),
        },
        'records': records,
        'artifact_checks': checked_links,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--snapshot-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--check-artifacts', action='store_true')
    args = parser.parse_args()
    report = audit(args.snapshot_dir, args.check_artifacts)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(report['counts'], indent=2))
    okay = all(r['full_result_matches'] and r['provenance_matches']
               and r['section_inventory_matches'] and all(r['section_matches'].values())
               for r in report['records'])
    if args.check_artifacts:
        okay = okay and report['counts']['reachable_artifact_links'] == report['counts']['available_artifact_links']
    raise SystemExit(0 if okay else 1)
