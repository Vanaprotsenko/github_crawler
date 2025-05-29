from bs4 import BeautifulSoup


def parse_github_search_results(html, search_type):
    soup = BeautifulSoup(html, "lxml")
    results = []

    main_div = soup.find("div", class_='Box-sc-g0xbh4-0 gZKkEq')
    if main_div:
        repo_divs = main_div.find_all("div", class_=lambda x: x and x.startswith("Box-sc"))
        for repo_div in repo_divs:
            link = repo_div.find("a", class_=lambda x: x and x.startswith("prc-Link"))

            if link and 'href' in link.attrs:
                url = "https://github.com" + link['href']
                results.append({"url": url})

    return results
