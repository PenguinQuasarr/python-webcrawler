from urllib.parse import urlparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup


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
        print(link)
        url = link.get("href")
        absolute_url = urljoin(base_url, url)
        list_of_urls.append(absolute_url)

    return list_of_urls
