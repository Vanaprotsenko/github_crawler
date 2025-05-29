import unittest
from crawler.utils import build_search_url


class TestUtils(unittest.TestCase):
    def test_unicode_keywords(self):
        url = build_search_url(["питон", "бот"], "Repositories")
        self.assertIn("q=%D0%BF%D0%B8%D1%82%D0%BE%D0%BD", url)
