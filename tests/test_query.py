import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('query', Path(__file__).resolve().parents[1] / 'scripts/query.py')
query = importlib.util.module_from_spec(spec)
spec.loader.exec_module(query)


class QueryTests(unittest.TestCase):
    def test_limited_records_require_opt_in(self):
        self.assertEqual(query.search('ghost'), [])
        records = query.search('ghost', include_limited=True)
        self.assertEqual(records[0]['id'], 'ghost')
        self.assertTrue(records[0]['warnings'])

    def test_filters_apply_together(self):
        records = query.search(use_case='developer-tools', style='dark-technical', limit=40)
        self.assertIn('linear', [e['id'] for e in records])
        self.assertNotIn('apple', [e['id'] for e in records])
        for e in records:
            self.assertIn('developer-tools', e['use_cases'])
            self.assertIn('dark-technical', e['styles'])

    def test_spanish_accents_do_not_change_matches(self):
        a = query.search('cálido editorial', limit=40)
        b = query.search('calido editorial', limit=40)
        self.assertEqual([e['id'] for e in a], [e['id'] for e in b])
        self.assertGreater(len(a), 0)
        for item in a[:4]:
            self.assertIn('warm-editorial', item['styles'])

    def test_unknown_query_does_not_recommend_by_rank(self):
        self.assertEqual(query.search('zzzzzz_no_match'), [])

    def test_section_reads_keep_quality_and_source(self):
        result = query.show('ghost', 'colors')
        self.assertEqual(result['quality'], 'limited')
        self.assertTrue(result['warnings'])
        self.assertEqual(result['source_url'], 'https://ghost.ai/')
        self.assertEqual(result['data']['baseline'], [])

    def test_unknown_paths_are_rejected(self):
        with self.assertRaises(ValueError):
            query.show('../../README')
        with self.assertRaises(ValueError):
            query.show('linear', 'not-a-section')


if __name__ == '__main__':
    unittest.main()
