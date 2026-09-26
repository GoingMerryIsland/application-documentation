"""Regression checks for artifact validation; no network or extra dependencies."""
import tempfile
import sys
sys.dont_write_bytecode = True
import unittest
from pathlib import Path
from validate_artifact import validate


class ArtifactValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.html('<h1 id="overview">Dokumentasi</h1>')

    def html(self, body):
        (self.root/'index.html').write_text('<!doctype html><html><body>'+body+'</body></html>', encoding='utf-8')

    def check(self, required=(), offline=True):
        return validate(self.root, required, offline)

    def test_minimal_preview_and_source_link(self):
        self.html('<h1 id="x">Docs</h1><a href="#x">Go</a><a href="https://example.com">Source</a>')
        self.assertEqual(self.check()['errors'], [])

    def test_missing_entrypoint(self):
        (self.root/'index.html').unlink()
        self.assertIn('Missing index.html', self.check()['errors'])

    def test_empty_preview(self):
        self.html('')
        self.assertTrue(any('no recognizable' in e for e in self.check()['errors']))

    def test_required_exports(self):
        errors = self.check(('pdf','pptx','png','jpg'))['errors']
        for fmt in ('pdf','pptx','png','jpg'):
            self.assertTrue(any(f'Missing required {fmt}' in e for e in errors))

    def test_broken_navigation_and_download(self):
        self.html('<h1>Docs</h1><a href="#missing">Go</a><a href="exports/missing.pdf">PDF</a>')
        errors=self.check()['errors']
        self.assertTrue(any('Broken in-page anchor' in e for e in errors))
        self.assertTrue(any('Missing linked file' in e for e in errors))

    def test_duplicate_identifiers(self):
        self.html('<h1 id="x">A</h1><section id="x">B</section>')
        self.assertTrue(any('Duplicate HTML ids' in e for e in self.check()['errors']))

    def test_outside_path_and_executable_link(self):
        self.html('<h1>Docs</h1><img src="../outside.png"><a href="javascript:alert(1)">X</a>')
        errors=self.check()['errors']
        self.assertTrue(any('escapes artifact folder' in e for e in errors))
        self.assertTrue(any('Executable URL' in e for e in errors))

    def test_offline_resources(self):
        self.html('<h1>Docs</h1><script src="https://example.com/script.js"></script><style>body{background:url(https://example.com/bg.png)}</style>')
        self.assertEqual(len(self.check()['errors']),2)
        self.assertEqual(self.check(offline=False)['errors'],[])

    def test_falsely_renamed_files(self):
        (self.root/'exports').mkdir()
        for fmt in ('pdf','pptx','png','jpg'):
            (self.root/'exports'/f'fake.{fmt}').write_text('<html>Wrong format</html>')
        errors=self.check()['errors']
        for fmt in ('pdf','pptx','png','jpg'):
            self.assertTrue(any(f'fake.{fmt}' in e for e in errors))

    def test_invalid_and_active_svg(self):
        (self.root/'bad.svg').write_text('<svg><unclosed>')
        (self.root/'active.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" onload="alert(1)"><script>alert(1)</script><image href="https://example.com/x.png"/></svg>')
        errors=self.check()['errors']
        for term in ('Invalid SVG','Active script in SVG','Active event handler in SVG','Network/absolute'):
            self.assertTrue(any(term in e for e in errors),term)

    def test_valid_svg_internal_marker(self):
        (self.root/'diagram.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg"><defs><marker id="arrow"/></defs><path style="marker-end:url(#arrow)" d="M0 0 L10 10"/></svg>')
        self.html('<h1>Docs</h1><img src="diagram.svg">')
        self.assertEqual(self.check()['errors'],[])

    def test_empty_srcset_is_safe(self):
        self.html('<h1>Docs</h1><img srcset=" , ">')
        self.assertEqual(self.check()['errors'],[])


if __name__=='__main__':
    unittest.main()
