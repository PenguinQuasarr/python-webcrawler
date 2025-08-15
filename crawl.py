from urllib.parse import urlparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests


def normalize_url(input_url):
    parsed_input = urlparse(input_url)

    netloc = parsed_input.netloc
    path = parsed_input.path.rstrip("/")

    formatted_url = netloc + path
    return formatted_url


def get_urls_form_html(html, base_url):
    soup_obj = BeautifulSoup(html, "html.parser")

    list_of_urls = []

    for link in soup_obj.find_all("a"):
        url = link.get("href")
        absolute_url = urljoin(base_url, url)
        list_of_urls.append(absolute_url)

    return list_of_urls


def get_html(url):
    request_obj = requests.get(url)
    content_type = request_obj.headers["content-type"]

    if not request_obj.ok or "text/html" not in content_type:
        return "Nope"
    else:
        return request_obj.text


def crawl_page(base_url, current_url=None, pages=None):

    if base_url not in current_url:
        return

    current_normalized = normalize_url(current_url)

    if current_normalized not in pages:
        pages[current_normalized] = 1
    else:
        pages[current_normalized] += 1
        return

    if ".xml" in current_url:
        return

    html_page = get_html(current_url)
    print(f"Getting page: {current_url}")

    urls_list = get_urls_form_html(html_page, base_url)

    for url in urls_list:
        crawl_page(base_url, url, pages)
