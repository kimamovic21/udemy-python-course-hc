# Challenges — Web Scraping

This group corresponds to `03_web_scraping` in the Udemy tutorial. It follows [01_utilities](../01_utilities/README.md) and [02_data_handling](../02_data_handling/README.md).

**Status: in progress — current course section.** Days 1–6 cover HTML extraction, Wikipedia headings, Hacker News CSV export, paginated book scraping, cover-image downloads, and creating quote images with Pillow.

[Challenge index](../README.md) · [Main project overview](../../README.md#folder-overview)

## Learning order and folder layout

Local numbering starts again at `day_1`. Each lesson folder contains the script, the original task, and a README with implementation details and running instructions. Name Python files `day_1.py`, `day_2.py`, `day_3.py`, and so on, without leading zeros.

| Lesson guide | Project | Main concepts |
| --- | --- | --- |
| [day_1](day_1/README.md) | Scrape Wikipedia h2 Headers | HTTP requests, HTML parsing, heading extraction, lists, and request-error handling. |
| [day_2](day_2/README.md) | Hacker News Top Posts Scraper | CSS selectors, lists of dictionaries, CSV output, and script-relative paths. |
| [day_3](day_3/README.md) | Scrape Books to Scrape (70 Books) | Pagination, relative URL resolution, list slicing, and JSON export. |
| [day_4](day_4/README.md) | Download Cover Images of the First 10 Books | Image URLs, filename cleanup, streamed downloads, binary files, and script-relative folders. |
| [day_5](day_5/README.md) | Download Cover Images Using wget | Package-based downloading, progress display, numbered filenames, and local output folders. |
| [day_6](day_6/README.md) | Quote of the Day Image Maker | Quote extraction, tuples, text wrapping, Pillow drawing, and PNG output. |

The `DAY_*.md` files contain original task statements maintained manually by the repository owner. Keep their contents unchanged; record explanations and progress in README files.

## Setup and running

Install the packages with the Python interpreter used to run the project:

```powershell
python -m pip install requests beautifulsoup4
```

Day 5 additionally requires the Python `wget` package:

```powershell
python -m pip install wget
```

Day 6 additionally requires Pillow, imported as `PIL`:

```powershell
python -m pip install Pillow
```

`beautifulsoup4` is the package name used by pip; Python imports it with `from bs4 import BeautifulSoup`. These scripts use Python's built-in `html.parser`, so no additional parser package is needed. Day 2 also uses `csv` and `pathlib`; Day 3 uses `json`, `pathlib`, and `urllib.parse`. Day 4 uses `os`, `pathlib`, `re`, and `urllib.parse`. Day 6 uses `os`, `pathlib`, and `textwrap`. These modules are part of Python's standard library.

From the repository root:

```powershell
python "challenges/03_web_scraping/day_1/day_1.py"
python "challenges/03_web_scraping/day_2/day_2.py"
python "challenges/03_web_scraping/day_3/day_3.py"
python "challenges/03_web_scraping/day_4/day_4.py"
python "challenges/03_web_scraping/day_5/day_5.py"
python "challenges/03_web_scraping/day_6/day_6.py"
```

Or open the script in VS Code and press **Ctrl + S** using the existing Run on Save configuration. An internet connection is required for the page request. Day 1 prints its results in the terminal and does not create any data files.

See the [Day 1 README](day_1/README.md) for the function walkthrough, example, troubleshooting, and remaining challenge requirements.

Day 1 sends a descriptive `User-Agent` identifying the script and its project URL. The original generic Requests identification was rejected locally with HTTP 403. Its README preserves the [complete original tutorial code](day_1/README.md#original-tutorial-code) and explains the [request configuration and difference from the video](day_1/README.md#why-the-tutorial-request-returned-403). No API key or `.env` is needed for this lesson.

Day 2 uses the [Hacker News homepage](https://news.ycombinator.com/) as its source. It writes up to 20 titles and URLs to `day_2/hn_top20.csv`, beside `day_2.py`, regardless of the terminal's working directory. Each successful non-empty export replaces the previous CSV. See the [Day 2 README](day_2/README.md) for the selector, CSV format, and running instructions.

Day 3 uses [Books to Scrape](https://books.toscrape.com/), follows next-page links, and keeps up to 70 book titles and prices in JSON. Its `day_3/books_data.json` output stays beside `day_3.py` using a script-relative path, regardless of the terminal's working directory. See the [Day 3 output-location note](day_3/README.md#json-output-and-current-file-location) and [running instructions](day_3/README.md#how-to-run).

Day 4 also uses [Books to Scrape](https://books.toscrape.com/), downloading covers from the first 10 homepage listings into `day_4/images/`. The folder stays beside `day_4.py` regardless of the terminal's working directory. See the [Day 4 README](day_4/README.md) for filename cleanup, streamed binary downloads, and current error-handling behaviour.

Day 5 downloads the same first 10 homepage covers using [wget](https://pypi.org/project/wget/) and saves final files in `day_5/images/`. That folder is ignored by Git. Repeated saves can create numbered image copies instead of overwriting files; see the [Day 5 comparison with Day 4](day_5/README.md#difference-from-day-4) and its [setup instructions](day_5/README.md#setup).

Day 6 reads the first five quotes and authors from [Quotes to Scrape](https://quotes.toscrape.com/) and creates 800 × 400 PNG cards using Pillow. Output stays in `day_6/quotes/`, which is ignored by Git. Repeated runs overwrite the same numbered PNGs. See the [Day 6 guide](day_6/README.md) for installation, drawing steps, and current layout limitations.

## Useful links for beginners

- [Python Package Index (PyPI)](https://pypi.org/): browse external Python packages used in these projects.
- [Beautiful Soup quick start](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start): parsing HTML and exploring tags and text.
- [Requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/): fetching a page and working with its response.
- [Hacker News](https://news.ycombinator.com/): the homepage scraped in Day 2.
- [Beautiful Soup CSS selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors): selecting post links with `.select()`.
- [Python CSV reading and writing](https://docs.python.org/3/library/csv.html): exporting dictionaries with `DictWriter`.
- [Books to Scrape](https://books.toscrape.com/): the source for Day 3 book records and Day 4–5 cover images.
- [Combining URLs with urljoin()](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin): resolving next-page links.
- [Python JSON encoding and decoding](https://docs.python.org/3/library/json.html): exporting the collected books.
- [Requests streaming downloads](https://requests.readthedocs.io/en/latest/user/advanced/#body-content-workflow): reading and saving image data in chunks.
- [Replacing matches with re.sub()](https://docs.python.org/3/library/re.html#re.sub): cleaning book titles for image filenames.
- [wget on PyPI](https://pypi.org/project/wget/): installation and API examples for the Day 5 downloader.
- [Quotes to Scrape](https://quotes.toscrape.com/): the source for the Day 6 quote cards.
- [Pillow on PyPI](https://pypi.org/project/Pillow/): the additional Day 6 image library.
- [Pillow tutorial](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html): basic image creation and saving.
- [Wikimedia User-Agent policy](https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy/en): identification requirements for automated requests.
