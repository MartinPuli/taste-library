#!/usr/bin/env python3
"""Query local design references without dependencies or external services."""
import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
STOPWORDS = {'a', 'al', 'and', 'con', 'de', 'del', 'el', 'en', 'for', 'la', 'las',
             'lo', 'los', 'no', 'of', 'or', 'para', 'por', 'que', 'the', 'un',
             'una', 'unas', 'unos', 'with', 'y'}
ALIASES = {
    'calido': 'warm', 'calida': 'warm', 'calidos': 'warm', 'calidas': 'warm',
    'oscuro': 'dark', 'oscura': 'dark', 'oscuros': 'dark', 'oscuras': 'dark',
    'tecnico': 'technical', 'tecnica': 'technical', 'tecnicos': 'technical',
    'monocromo': 'monochrome', 'monocromatico': 'monochrome',
    'cinematografico': 'cinematic', 'cine': 'cinematic',
    'desarrolladores': 'developer', 'developers': 'developer',
}


def load_catalog():
    return json.loads((ROOT / 'catalog/index.json').read_text())['entries']


def normalize(value):
    return ''.join(c for c in unicodedata.normalize('NFKD', value.lower())
                   if not unicodedata.combining(c))


def words(value):
    return {ALIASES.get(term, term) for term in re.findall(r'[a-z0-9]+', normalize(value))}


def search(query='', use_case=None, style=None, include_limited=False, limit=5, component=None):
    taxonomy = json.loads((ROOT / 'catalog/taxonomy.json').read_text())
    for value, group in [(use_case,'use_cases'), (style,'styles'), (component,'components')]:
        if value and value not in taxonomy[group]:
            raise ValueError(f'Unknown {group}: {value}')
    if not 1 <= limit <= 40:
        raise ValueError('limit must be between 1 and 40')
    terms = words(query) - STOPWORDS
    if query.strip() and not terms:
        return []
    matches = []
    for entry in load_catalog():
        if entry['quality'] == 'limited' and not include_limited:
            continue
        if use_case and use_case not in entry['use_cases']:
            continue
        if style and style not in entry['styles']:
            continue
        if component and component not in entry.get('components', []):
            continue
        fields = [(entry['name'], 8),
                  (' '.join(entry['use_cases'] + entry['styles'] + entry.get('components', [])), 5),
                  (entry['selection_note'], 2)]
        matched = sorted(terms & set().union(*(words(v) for v, _ in fields)))
        score = sum(weight * len(terms & words(text)) for text, weight in fields)
        if terms and not matched:
            continue
        matches.append(dict(entry, match_score=score, matched_terms=matched))
    # Rank only makes ties reproducible. It does not measure design suitability.
    matches.sort(key=lambda e: (-e['match_score'], e['rank']))
    return matches[:limit]


def show(identifier, section=None):
    entry = next((e for e in load_catalog() if e['id'] == identifier), None)
    if entry is None:
        raise ValueError('Unknown reference: ' + identifier)
    if section is None:
        return (ROOT / entry['paths']['profile']).read_text()
    raw = json.loads((ROOT / entry['paths']['raw']).read_text())
    system = raw['result']['design_system']
    if section not in system:
        raise ValueError('Unknown section. Available: ' + ', '.join(system))
    return {
        'id': entry['id'], 'source_url': entry['source_url'],
        'captured_at': entry['captured_at'], 'quality': entry['quality'],
        'warnings': entry['warnings'], 'section': section, 'data': system[section],
        'source_file': entry['paths']['raw'],
        'source_pointer': '/result/design_system/' + section,
        'review_file': entry['paths']['review'],
        'has_data': entry['sections'][section]['has_data'],
    }


def positive(value):
    n = int(value)
    if n < 1:
        raise argparse.ArgumentTypeError('limit must be at least 1')
    return n


def compare(identifiers, section):
    if not 2 <= len(identifiers) <= 4 or len(set(identifiers)) != len(identifiers):
        raise ValueError('Compare two to four distinct references.')
    return {'section': section, 'references': [show(id, section) for id in identifiers]}


def main():
    taxonomy = json.loads((ROOT / 'catalog/taxonomy.json').read_text())
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest='command', required=True)
    find = subs.add_parser('search', help='Match words and tags; scores are not quality ratings')
    find.add_argument('query', nargs='?', default='')
    find.add_argument('--use-case', choices=taxonomy['use_cases'])
    find.add_argument('--style', choices=taxonomy['styles'])
    find.add_argument('--component', choices=taxonomy.get('components', []))
    find.add_argument('--include-limited', action='store_true')
    find.add_argument('--limit', type=positive, default=5)
    find.add_argument('--json', action='store_true')
    read = subs.add_parser('show', help='Read one profile or extraction section')
    read.add_argument('id')
    read.add_argument('--section')
    comparison = subs.add_parser('compare', help='Compare evidence from two to four references')
    comparison.add_argument('ids', nargs='+')
    comparison.add_argument('--section', required=True)
    comparison.add_argument('--json', action='store_true')
    args = parser.parse_args()
    try:
        if args.command == 'search':
            result = search(args.query, args.use_case, args.style,
                            args.include_limited, args.limit, args.component)
            if args.json:
                print(json.dumps(result, ensure_ascii=False, indent=2))
            elif not result:
                print('No matches. Try a style or use-case filter.')
            else:
                for item in result:
                    print(f"{item['id']} | {item['quality']} | word score {item['match_score']}")
                    print('  ' + item['selection_note'])
                    print('  ' + item['paths']['profile'])
                    for warning in item['warnings']:
                        print('  Warning: ' + warning)
        elif args.command == 'compare':
            result = compare(args.ids, args.section)
            if args.json:
                print(json.dumps(result, ensure_ascii=False, indent=2))
            else:
                for item in result['references']:
                    print(f"{item['id']} | {item['section']} | {item['quality']}")
                    print(f"Source: {item['source_url']} | Captured: {item['captured_at']}")
                    print(json.dumps(item['data'], ensure_ascii=False, indent=2))
        else:
            result = show(args.id, args.section)
            print(result if isinstance(result, str) else json.dumps(result, ensure_ascii=False, indent=2))
    except ValueError as error:
        parser.error(str(error))


if __name__ == '__main__':
    main()
