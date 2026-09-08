"""Run with: python3 -m unittest discover -s tests -v."""
from html.parser import HTMLParser
from pathlib import Path
import unittest


class StoreLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'store-button' in (attrs.get('class') or '').split():
            self.current = {'href': attrs.get('href'), 'text': ''}

    def handle_data(self, data):
        if self.current is not None:
            self.current['text'] += data

    def handle_endtag(self, tag):
        if tag == 'a' and self.current is not None:
            self.current['text'] = self.current['text'].strip()
            self.buttons.append(self.current)
            self.current = None


class MartLogStoreLinksTest(unittest.TestCase):
    def test_both_store_buttons_link_to_martlog(self):
        parser = StoreLinks()
        page = Path(__file__).resolve().parents[1] / 'martlog' / 'index.html'
        parser.feed(page.read_text(encoding='utf-8'))
        self.assertCountEqual(parser.buttons, [
            {'href': 'https://apps.apple.com/kr/app/id6778012377', 'text': 'App Store'},
            {'href': 'https://play.google.com/store/apps/details?id=com.dayseed.martlog',
             'text': 'Google Play'},
        ])


if __name__ == '__main__':
    unittest.main()
