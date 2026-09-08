"""Product-led 또또 landing: semantic content, safe assets and destinations."""
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / 'ddoddo'


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.elements = []
        self.text = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)


class DdoddoLandingTest(unittest.TestCase):
    def test_product_preview_with_install_and_preserved_policy_destinations(self):
        doc = Document((PAGE / 'index.html').read_text())
        text = ''.join(doc.text)
        self.assertIn('마지막 수유,', text)
        self.assertIn('몇 시였지?', text)
        self.assertIn('실제 앱 화면 · 샘플 데이터', text)
        self.assertIn('의료적 진단', text)
        self.assertEqual(sum(tag == 'h1' for tag, _ in doc.elements), 1)
        images = [a for tag, a in doc.elements if tag == 'img' and 'product-screen' in a.get('class', '')]
        self.assertEqual(len(images), 1)
        for image in images:
            self.assertTrue(image.get('alt'))
            self.assertTrue(image.get('width') and image.get('height'))
            self.assertTrue((PAGE / image['src']).is_file())
        hrefs = {a['href'] for tag, a in doc.elements if tag == 'a'}
        for expected in ('https://apps.apple.com/kr/app/id6792637949',
                         'https://play.google.com/store/apps/details?id=com.dayseed.ddoddo',
                         'support/', 'privacy-policy/', 'terms/', 'account-deletion/'):
            self.assertIn(expected, hrefs)
        ids = [a['id'] for _, a in doc.elements if 'id' in a]
        self.assertEqual(len(ids), len(set(ids)))
        for href in hrefs:
            if href.startswith('#'):
                self.assertIn(href[1:], ids)
            elif ':' not in href:
                target = PAGE / href
                self.assertTrue(target.is_file() or (target / 'index.html').is_file(), href)
        for tag, attrs in doc.elements:
            self.assertNotEqual(tag, 'script')
            self.assertFalse(any(key.startswith('on') for key in attrs))
            self.assertFalse(any(value.lower().startswith('javascript:') for value in attrs.values() if value))


if __name__ == '__main__':
    unittest.main()
