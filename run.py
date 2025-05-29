import json
from crawler.github_crawler import crawl_github


def main():
    with open("input.json", encoding="utf-8") as f:
        input_data = json.load(f)

    results = crawl_github(input_data)
    print(json.dumps(results, indent=2, ensure_ascii=False))

    # The code for saving our results in file
    with open("github_results.json", 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
