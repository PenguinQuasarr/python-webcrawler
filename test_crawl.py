import unittest
from crawl import normalize_url
from crawl import get_urls_form_html


class TestCrawl(unittest.TestCase):
    def test_normalize_url(self):
        expected = "blog.boot.dev/path"

        inputs = [
                "https://blog.boot.dev/path/",
                "https://blog.boot.dev/path",
                "http://blog.boot.dev/path/",
                "http://blog.boot.dev/path"
                ]
        for url in inputs:
            result = normalize_url(url)
            self.assertEqual(result, expected)

    def test_get_urls_from_html(self):
        base_url = "https://blog.boot.dev"

        expected = ["https://blog.boot.dev"]
        result_list = []

        test_cases = ['<html><body><a href="https://blog.boot.dev"><span>Boot.dev</span></a></body><span>I like cake</span></html>']
        for case in test_cases:
            result_list += get_urls_form_html(case, base_url)
        self.assertEqual(result_list, expected)


if __name__ == "__main__":
    unittest.main()
