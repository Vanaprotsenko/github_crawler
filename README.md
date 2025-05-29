# 🕷️ GitHub HTML Crawler

A fast and lightweight GitHub crawler that searches for Repositories, Issues or Wikis \
using raw HTML — no GitHub API needed. Supports random proxy usage and Unicode keywords.

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 🧪 Usage

Run the crawler using:

```bash
python run.py
```

Input should be provided via `input.json` (example below):

### 📁 input.json

```json
{
  "keywords": ["python", "web", "css"],
  "proxies": ["57.129.81.201", "13.78.125.167:8080"],
  "type": "Issues"
}
```

The output will be saved to `github_results.json`

## ✅ Testing

### Run Unit Tests

```bash
python -m unittest discover tests
```

### 🧪 Coverage Report

Generate coverage:

```bash
coverage run -m unittest discover tests
```

Show the report:

```bash
coverage report -m
```

## 📊 Example Output

`github_results.json`:

```json
[
  { "url": "https://github.com/example/wiki-1" },
  { "url": "https://github.com/example/wiki-2" }
]
```
