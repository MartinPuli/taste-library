import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('audit_tastelabs', ROOT/'scripts/audit_tastelabs.py')
audit_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit_module)


class SourceAuditTests(unittest.TestCase):
    def snapshots(self, directory):
        for source in (ROOT/'data/raw').glob('*.json'):
            (directory/source.name).write_bytes(source.read_bytes())

    def test_extra_source_fields_are_detected_even_when_all_sections_match(self):
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            self.snapshots(directory)
            path = directory/'a24.json'
            snapshot = json.loads(path.read_text())
            snapshot['result']['new_source_field'] = {'not_exported': True}
            path.write_text(json.dumps(snapshot))
            report = audit_module.audit(directory)
            entry = next(r for r in report['records'] if r['id'] == 'a24')
            self.assertFalse(entry['full_result_matches'])
            self.assertTrue(all(entry['section_matches'].values()))
            self.assertEqual(report['counts']['matching_results'], 39)

    def test_changed_dates_and_null_to_empty_changes_are_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            self.snapshots(directory)
            path = directory/'a24.json'
            snapshot = json.loads(path.read_text())
            snapshot['completed_at'] = '2000-01-01T00:00:00Z'
            snapshot['result']['artifacts']['html'] = None
            path.write_text(json.dumps(snapshot))
            entry = next(r for r in audit_module.audit(directory)['records'] if r['id'] == 'a24')
            self.assertFalse(entry['provenance_matches'])
            self.assertFalse(entry['full_result_matches'])
            self.assertNotEqual(audit_module.digest(None), audit_module.digest([]))


if __name__ == '__main__':
    unittest.main()
