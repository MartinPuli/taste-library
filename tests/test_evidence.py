import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import shutil

ROOT = Path(__file__).resolve().parents[1]
def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/f'{name}.py')
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

query = module('query')
validator = module('validate')

class EvidenceTests(unittest.TestCase):
    def test_catalog_and_every_section_have_consistent_evidence(self):
        self.assertEqual(validator.validate(), [])

    def test_component_filter_is_backed_by_concrete_elements(self):
        matches = query.search(component='forms', limit=40)
        self.assertGreater(len(matches), 0)
        for match in matches:
            raw = json.loads((ROOT/match['paths']['raw']).read_text())['result']['design_system']
            for evidence in match['component_evidence']['forms']:
                value = raw[evidence['section']]
                for segment in evidence['pointer'].strip('/').split('/'):
                    value = value[int(segment)] if isinstance(value, list) else value[segment]
                self.assertEqual(value['type'], 'form')
        with self.assertRaises(ValueError):
            query.search(component='imaginary')

    def test_compare_preserves_distinct_values_and_capture_dates(self):
        result = query.compare(['linear','cursor'], 'layout')
        a,b = result['references']
        self.assertEqual(a['data']['grid']['columns'], 12)
        self.assertEqual(b['data']['grid']['columns'], 24)
        self.assertNotEqual(a['captured_at'], b['captured_at'])
        self.assertEqual(a['source_pointer'], '/result/design_system/layout')
        with self.assertRaises(ValueError):
            query.compare(['linear','linear'], 'layout')
        with self.assertRaises(ValueError):
            query.compare(['linear'], 'layout')

    def test_absent_palette_stays_absent(self):
        result = query.show('ghost','colors')
        self.assertFalse(result['has_data'])
        self.assertEqual(result['data']['baseline'], [])

    def test_validator_detects_changed_section_without_changing_raw(self):
        with tempfile.TemporaryDirectory() as temp:
            copy = Path(temp)
            for name in ['catalog','data','profiles','guides','skills']:
                shutil.copytree(ROOT/name, copy/name)
            path = copy/'data/sections/linear/layout.json'
            data = json.loads(path.read_text())
            data['data']['grid']['columns'] = 99
            path.write_text(json.dumps(data))
            self.assertTrue(any('section content differs: layout' in e for e in validator.validate(copy)))

    def test_briefs_can_reach_relevant_candidates(self):
        developer = query.search(use_case='developer-tools',component='buttons',limit=40)
        editorial = query.search(use_case='editorial-research',style='warm-editorial',limit=40)
        self.assertTrue({'cursor','linear'} <= {e['id'] for e in developer})
        self.assertTrue({'anthropic','pangram'} <= {e['id'] for e in editorial})

if __name__ == '__main__':
    unittest.main()
