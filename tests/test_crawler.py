import unittest
from crawler.github_crawler import crawl_github


class TestCrawler(unittest.TestCase):
    def test_crawl_repositories(self):
        input_data = {
            "keywords": ["python", "jwt"],
            "proxies": ["194.126.37.94:8080", "13.78.125.167:8080"],
            "type": "Repositories"
        }
        results = crawl_github(input_data)
        self.assertIsInstance(results, list)
        self.assertTrue(all("url" in r for r in results))
