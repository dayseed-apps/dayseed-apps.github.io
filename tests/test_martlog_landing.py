"""Semantic regression checks for the MartLog landing refinement."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class Elements(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []
        self.text = []
    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))
    def handle_data(self, data):
        self.text.append(data)

class MartLogLandingTest(unittest.TestCase):
    def setUp(self):
        self.doc = Elements()
        self.doc.feed((ROOT / 'martlog/index.html').read_text())

    def test_real_product_preview_has_accessible_text_and_sample_disclosure(self):
        previews = [a for t, a in self.doc.elements if t == 'img' and a.get('src','').startswith('assets/')]
        self.assertTrue(previews, 'Landing needs a real product screenshot, not only an app icon')
        for a in previews:
            self.assertTrue(a.get('alt'))
            self.assertGreater(int(a.get('width',0)), 0)
            self.assertGreater(int(a.get('height',0)), 0)
            self.assertTrue((ROOT / 'martlog' / a['src']).is_file())
        self.assertIn('샘플 데이터', ' '.join(self.doc.text))

if __name__ == '__main__':
    unittest.main()
