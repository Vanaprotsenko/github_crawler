import unittest
from crawler.parser import parse_github_search_results

with open("tests/sample_repos_file_for_test.html", encoding="utf-8") as f:
    sample_html = f.read()


class TestParser(unittest.TestCase):
    def test_parse_repositories(self):
        results = parse_github_search_results(sample_html, "Repositories")
        self.assertIsInstance(results, list)
        self.assertTrue(all("url" in r for r in results))
