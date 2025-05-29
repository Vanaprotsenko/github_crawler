from urllib.parse import quote_plus


def build_search_url(keywords, search_type):
    base_url = "https://github.com/search"
    query = "+".join(quote_plus(kw) for kw in keywords)
    type_param = search_type.lower()
    return f"{base_url}?q={query}&type={type_param}"


def get_headers():
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
