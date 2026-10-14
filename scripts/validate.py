#!/usr/bin/env python3
"""Check catalog consistency, evidence hashes, warnings and local links."""
import hashlib
import json
from pathlib import Path
import re
import sys
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    errors = []
    catalog = json.loads((root / 'catalog/index.json').read_text())
    manifest = json.loads((root / 'data/manifest.json').read_text())
    taxonomy = json.loads((root / 'catalog/taxonomy.json').read_text())
    entries = catalog['entries']
    ids = [e['id'] for e in entries]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate catalog IDs')
    ranks = [e['rank'] for e in entries]
    if len(ranks) != len(set(ranks)):
        errors.append('Duplicate source ranks')
    if sorted(ranks) != list(range(1, 41)):
        errors.append('Collection must preserve exactly the Cosign top 40')
    if set(ids) != {e['id'] for e in manifest['records']}:
        errors.append('Manifest and catalog IDs differ')
    if catalog['schema_version'] != '1.1':
        errors.append('Unsupported catalog version')
    expected_counts = {
        'records': len(entries),
        'default_references': sum(e['quality'] != 'limited' for e in entries),
        'saved_capture_reviews': sum((root / e['paths']['review']).is_file() for e in entries),
    }
    if catalog['counts'] != expected_counts:
        errors.append('Catalog counts differ from records')
    compact = json.loads((root / 'catalog/search.json').read_text())
    if compact['counts'] != expected_counts or {e['id'] for e in compact['entries']} != set(ids):
        errors.append('Compact catalog differs')
    records = {e['id']: e for e in manifest['records']}
    required = {'id','name','rank','source_url','captured_at','page_type','use_cases',
                'styles','quality','warnings','selection_note','note_basis','paths'}
    for e in entries:
        id = e['id']
        if not required <= e.keys():
            errors.append(f'{id}: missing catalog fields')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', id):
            errors.append(f'{id}: invalid ID')
        for key in ['use_cases','styles']:
            if not e[key] or not set(e[key]) <= set(taxonomy[key]):
                errors.append(f'{id}: invalid {key}')
        if e['quality'] not in taxonomy['quality']:
            errors.append(f'{id}: invalid quality')
        if e['quality'] == 'limited' and not e['warnings']:
            errors.append(f'{id}: limited record has no warning')
        if not e['source_url'].startswith('https://'):
            errors.append(f'{id}: source must be HTTPS')
        try:
            datetime.fromisoformat(e['captured_at'].replace('Z', '+00:00'))
        except (ValueError, AttributeError):
            errors.append(f'{id}: invalid capture date')
        for path in e['paths'].values():
            dest = (root / path).resolve()
            if root.resolve() not in dest.parents or not dest.is_file():
                errors.append(f'{id}: missing or external path {path}')
        if any(not (root / p).is_file() for p in e['paths'].values()):
            continue
        raw_path = root / e['paths']['raw']
        raw = json.loads(raw_path.read_text())
        tokens = json.loads((root / e['paths']['tokens']).read_text())
        for key in ['quality','warnings','source_url','captured_at']:
            if tokens[key] != e[key]:
                errors.append(f'{id}: token {key} differs')
        if raw['source_url'] != e['source_url'] or raw['completed_at'] != e['captured_at']:
            errors.append(f'{id}: raw provenance differs')
        if raw['status'] != 'completed':
            errors.append(f'{id}: incomplete extraction')
        if hashlib.sha256(raw_path.read_bytes()).hexdigest() != records.get(id,{}).get('sha256'):
            errors.append(f'{id}: evidence hash mismatch')
        if not tokens['colors'] and e['quality'] != 'limited':
            errors.append(f'{id}: empty palette must be marked limited')
        if any(key in raw for key in ['user_id','api_key','api_key_name','credit_ref_id','submission_id']):
            errors.append(f'{id}: account metadata in public export')
        system = raw['result']['design_system']
        if set(e['sections']) != set(system):
            errors.append(f'{id}: section inventory differs')
        for name, section in e['sections'].items():
            path = root / section['path']
            if not path.is_file():
                errors.append(f'{id}: missing section {name}')
                continue
            value = json.loads(path.read_text())
            if value['data'] != system.get(name):
                errors.append(f'{id}: section content differs: {name}')
            for key in ['quality','warnings','source_url','captured_at']:
                if value[key] != e[key]:
                    errors.append(f'{id}: section {name} provenance differs: {key}')
            if value['source_pointer'] != '/result/design_system/' + name or value['source_file'] != e['paths']['raw']:
                errors.append(f'{id}: invalid section source pointer: {name}')
        if not set(e['components']) <= set(taxonomy['components']) or set(e['components']) != set(e['component_evidence']):
            errors.append(f'{id}: component inventory differs')
        for component, pointers in e['component_evidence'].items():
            for pointer in pointers:
                try:
                    target = system[pointer['section']]
                    for part in pointer['pointer'].strip('/').split('/'):
                        target = target[int(part)] if isinstance(target,list) else target[part]
                    if not target:
                        raise ValueError('empty evidence')
                except (KeyError, IndexError, ValueError, TypeError):
                    errors.append(f'{id}: broken component pointer for {component}')
        review = json.loads((root / e['paths']['review']).read_text())
        if review['raw_sha256'] != hashlib.sha256(raw_path.read_bytes()).hexdigest():
            errors.append(f'{id}: review refers to a different raw version')
        if not (root / e['preview']).is_file():
            errors.append(f'{id}: missing preview')
        c = next((x for x in compact['entries'] if x['id'] == id), None)
        if c is None or any(c[k] != e[k] for k in c if k != 'profile') or c['profile'] != e['paths']['profile']:
            errors.append(f'{id}: compact entry differs')
    audit_path = root / 'data/audits/tastelabs-2026-10-14.json'
    if audit_path.is_file():
        audit = json.loads(audit_path.read_text())
        if {r['id'] for r in audit['records']} != set(ids):
            errors.append('TasteLabs audit and catalog IDs differ')
        for record in audit['records']:
            path = root / record['raw_file']
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != record['raw_sha256']:
                errors.append(f"{record['id']}: TasteLabs audit refers to a different raw version")
            if not (record['full_result_matches'] and record['provenance_matches']
                    and record['section_inventory_matches'] and all(record['section_matches'].values())):
                errors.append(f"{record['id']}: TasteLabs audit found an export difference")
    else:
        errors.append('Missing TasteLabs completeness audit')
    for path in root.rglob('*.md'):
        if any(part in {'.git', 'node_modules', '.e2e'} for part in path.relative_to(root).parts):
            continue
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if '://' in target or target.startswith('#'):
                continue
            if not (path.parent / target.split('#')[0]).exists():
                errors.append(f'{path.relative_to(root)}: broken link {target}')
    return errors


if __name__ == '__main__':
    errors = validate()
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(1)
    count = len(json.loads((ROOT / 'catalog/index.json').read_text())['entries'])
    print(f'Validated {count} references: paths, hashes, provenance, quality flags and links.')
