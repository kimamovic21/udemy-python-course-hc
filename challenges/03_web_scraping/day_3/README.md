# Day 3: Scrape Books to Scrape (70 Books)

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to collect book titles and prices from [Books to Scrape](https://books.toscrape.com/), follow the next-page links until 70 books are collected, and save the result as JSON. The website is a scraping practice sandbox; its prices and ratings are demonstration data.

## Files

| File | Purpose |
| --- | --- |
| [DAY_3.md](DAY_3.md) | The original challenge statement and bonus tasks, maintained manually and left unchanged. |
| [day_3.py](day_3.py) | Scraping book listings, following pagination, and exporting a JSON list. |
| `books_data.json` | Runtime output containing book titles and prices; see the current output-location note below. |

## Setup

Use the same external packages as the previous scraping projects:

```powershell
python -m pip install requests beautifulsoup4
```

`requests` fetches each page, and `BeautifulSoup` parses its HTML using Python's built-in `html.parser`. The `json` and `pathlib` modules and `urllib.parse.urljoin` are part of the standard library. No API key, `.env`, or additional parser package is required.

## How the code works

1. `BASE_URL` selects Books to Scrape. `urljoin(BASE_URL, START_PAGE)` produces the first catalogue URL, `https://books.toscrape.com/catalogue/page-1.html`. `TARGET_COUNT` sets the target to 70.
2. `scrape_page(url)` sends a request with `timeout=10`, then calls `raise_for_status()`. A `requests.RequestException` prints `Failed to fetch url` and returns an empty list with no next-page URL.
3. `soup.select("article.product_pod")` locates the book cards. For each card, `select_one("h3 > a")` finds the title link; its `title` attribute provides the full title. `select_one("p.price_color").text.strip()` extracts the displayed price as text.
4. Each book becomes a dictionary with `title` and `price` keys. `soup.select_one("li.next > a")` finds the next-page link, and `urljoin(url, href)` resolves its relative address against the current page.
5. `main()` keeps requesting pages while fewer than 70 books have been collected and a next URL exists. `collected.extend(books)` adds each page's records. `collected[:TARGET_COUNT]` trims any extra records after the loop.
6. `json.dump(collected, f, indent=2)` writes the final list to `books_data.json`. The script prints each requested page URL, the final book count, and the output filename.

With 20 books per page, the loop collects 80 entries from four pages, then keeps the first 70. It reads the listing pages rather than opening each book's detail page.

## Pagination example

A normal run with enough available records follows this sequence:

| Page | Total collected before trimming |
| --- | --- |
| 1 | 20 |
| 2 | 40 |
| 3 | 60 |
| 4 | 80 |
| Final slice | 70 |

`urljoin()` is useful because the next link can be relative, such as `page-2.html`, while Requests needs the resolved page URL. If there is no next link, `next_url` becomes `None` and the loop stops.

## JSON output and current file location

The JSON contains a list of dictionaries. For example, an illustrative record is:

```json
[
  {
    "title": "Example book",
    "price": "GBP 12.50"
  }
]
```

The actual price is copied from the page, including any currency text; it remains a string, not a numeric amount. The code does not normalize prices or explicitly set the HTTP response encoding. `json.dump()` uses its default character escaping, so non-ASCII symbols can appear as `\u...` escapes in the file.

```python
OUTPUT_PAGE = Path(__file__).resolve().parent / "books_data.json"
```

`Path(__file__).resolve().parent` locates the script's folder, so the output is always:

```text
challenges/03_web_scraping/day_3/books_data.json
```

This works from the repository root, from the Day 3 folder, and through VS Code's **Ctrl + S** execution. The earlier plain filename used the terminal's working directory and could create the JSON in the repository root. Like Day 2, the script now keeps its output beside its Python file.

The JSON is opened with UTF-8 and mode `"w"`, so each run reaching the save step replaces the previous output in the lesson folder.

## How to run

From the repository root:

```powershell
python "challenges/03_web_scraping/day_3/day_3.py"
```

Or, from the lesson folder:

```powershell
python .\day_3.py
```

In VS Code, open `day_3.py` and press **Ctrl + S**. The JSON stays beside the script regardless of the Run on Save terminal's working directory. There are no input prompts; the program prints progress as it requests pages.

## Current behaviour to understand

- Fetching multiple pages, collecting titles/prices, trimming to 70, JSON output, progress messages, and the final count are implemented.
- A request failure or an early end to pagination can leave fewer than 70 records. The script still writes the collected list, including an empty list if the first request fails.
- Network failures are caught, but the caught exception details are not displayed. Missing title/price elements and file-writing errors are not handled separately.
- The bonus progress output shows page URLs and the final total; it does not print a running book count after every page.

## Useful links for beginners

- [Books to Scrape](https://books.toscrape.com/): the practice website used by this project.
- [Beautiful Soup CSS selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors): finding book cards, title links, prices, and pagination links.
- [Combining URLs with urljoin()](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin): resolving a relative next-page link against the current page URL.
- [Paths with pathlib](https://docs.python.org/3/library/pathlib.html): keeping JSON output beside the script with `Path(__file__).resolve().parent`.
- [Python JSON encoding and decoding](https://docs.python.org/3/library/json.html): saving lists and dictionaries with `dump()` and formatting with `indent`.
- [Requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/): making requests and handling HTTP errors.

[Previous: Day 2](../day_2/README.md) · [Next: Day 4](../day_4/README.md)
