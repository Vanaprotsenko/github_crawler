import requests
import random
from .parser import parse_github_search_results
from .utils import build_search_url, get_headers


def crawl_github(input_data):
    keywords = input_data["keywords"]
    proxies = input_data["proxies"]
    search_type = input_data["type"]

    proxy = {"http": f"http://{random.choice(proxies)}"}

    url = build_search_url(keywords, search_type)
    headers = get_headers()

    response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
    response.raise_for_status()

    return parse_github_search_results(response.text, search_type)
