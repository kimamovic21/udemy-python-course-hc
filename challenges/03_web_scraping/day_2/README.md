# Day 2: Hacker News Top Posts Scraper

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to fetch the [Hacker News homepage](https://news.ycombinator.com/), extract the first 20 post titles and links, and save them in a CSV file. This project extends Day 1's HTML scraping with CSS selectors and file output.

## Files

| File | Purpose |
| --- | --- |
| [DAY_2.md](DAY_2.md) | The original challenge statement, maintained manually and left unchanged. |
| [day_2.py](day_2.py) | Fetching the homepage, extracting post links, and writing CSV records. |
| `hn_top20.csv` | Output containing `title` and `url` columns, created beside the script after a successful collection. |

Python filenames follow `day_1.py`, `day_2.py`, and so on, without leading zeros. Use these names in terminal commands.

## Setup

Install the external packages using the interpreter that runs the script:

```powershell
python -m pip install requests beautifulsoup4
```

`requests` downloads HTML, and `from bs4 import BeautifulSoup` imports the parser library installed as `beautifulsoup4`. The `csv` and `pathlib` modules and the `html.parser` parser come with Python. No API key, `.env`, or extra parser package is required for this project.

If these packages were installed for Day 1 in the same Python environment, they are already available. For unresolved imports, check **Python: Select Interpreter** in VS Code; see the [Day 1 setup notes](../day_1/README.md#setup).

## How the code works

1. `HN_URL` selects `https://news.ycombinator.com/`. The script reads the homepage HTML directly; it does not call a JSON API or visit each article.
2. `fetch_top_post()` requests the page with `timeout=10` and calls `raise_for_status()` to detect HTTP errors. `requests.RequestException` catches request failures, prints a network-error message, and returns an empty list.
3. `BeautifulSoup(response.text, "html.parser")` parses the HTML. `soup.select("span.titleline > a")` selects links that are direct children of a `span` with the `titleline` class. The `>` means a direct child relationship.
4. `post_links[:20]` limits processing to the first 20 matches, in page order. Each record contains the stripped link text as `title` and the stripped `href` value as `url`.
5. `save_to_csv(posts)` skips writing if the list is empty. Otherwise, `csv.DictWriter` writes the column header followed by the collected records.
6. `main()` connects fetching and saving. The `if __name__ == "__main__":` guard calls it when the file is executed directly.

The result contains up to 20 homepage posts, depending on the matches returned. The program does not independently sort by points, retrieve comments, or follow additional pages.

## CSV output and file location

```python
CSV_FILE = Path(__file__).resolve().parent / "hn_top20.csv"
```

`__file__` identifies the script. Resolving its parent keeps the output at:

```text
challenges/03_web_scraping/day_2/hn_top20.csv
```

This works from the repository root, from the lesson folder, and through VS Code's **Ctrl + S** execution. The earlier plain filename used the terminal's working directory and could create the CSV in the repository root instead.

The file uses UTF-8 and is opened with `newline=""` for CSV writing. Mode `"w"` replaces the previous export when a non-empty collection is saved. Failed requests or empty results leave an existing CSV unchanged.

These sample rows illustrate the format; they are not copied from the current homepage:

```csv
title,url
Learning Python,https://example.com/python
"Working with lists, sets and dictionaries",https://example.com/collections
```

The actual columns are lowercase `title` and `url`, corresponding to the Title and URL fields in the challenge. Quotes around a field containing a comma are normal CSV formatting; let `csv.DictWriter` handle them.

## How to run

From the repository root:

```powershell
python "challenges/03_web_scraping/day_2/day_2.py"
```

Or, from this lesson's folder:

```powershell
python .\day_2.py
```

In VS Code, open `day_2.py` and press **Ctrl + S**. There are no input prompts. After collecting records, the script prints a saved message with the CSV path; open that file to inspect the titles and links. The homepage changes over time, so later runs can produce different records.

## Current behaviour to understand

- Network and HTTP errors are handled before parsing. The current no-data message is `Noting to save`; it means no records were written. The progress message `Collected all data...` appears even after a failed request, so check the error and final save message.
- Records use the original `href` values. Relative URLs remain relative; the script does not convert them to full Hacker News URLs.
- The selector depends on the website's HTML structure. If that structure changes, it may return no matches. A missing `href` is not handled separately by the current `.get("href").strip()` expression.
- A successful export stores a snapshot; it is updated only when the script runs again and saves a non-empty result.

## Useful links for beginners

- [Hacker News](https://news.ycombinator.com/): the homepage used as this project's data source.
- [Beautiful Soup CSS selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors): using `.select()` to find HTML elements.
- [Requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/): downloading pages and handling request errors.
- [Python CSV reading and writing](https://docs.python.org/3/library/csv.html): `DictWriter`, header rows, quoting, and CSV line endings.
- [Paths with pathlib](https://docs.python.org/3/library/pathlib.html): building output paths relative to the script.

[Previous: Day 1](../day_1/README.md) · [Next: Day 3](../day_3/README.md)
