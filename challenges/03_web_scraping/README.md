# Challenges — Web Scraping

This group corresponds to `03_web_scraping` in the Udemy tutorial. It follows [01_utilities](../01_utilities/README.md) and [02_data_handling](../02_data_handling/README.md).

**Status: local days 1–10 documented.** These projects cover HTML extraction, data exports, images, API graphs and logging, SQLite storage, and local PDF text extraction. Individual guides identify remaining task features. Continue with [04_automation](../04_automation/README.md), the current course section.

[Challenge index](../README.md) · [Main project overview](../../README.md#folder-overview)

## Learning order and folder layout

Local numbering starts again at `day_1`. Each lesson folder contains the script, a task statement, and a README with implementation details and running instructions. Name Python files `day_1.py`, `day_2.py`, `day_3.py`, and so on, without leading zeros.

| Lesson guide | Project | Main concepts |
| --- | --- | --- |
| [day_1](day_1/README.md) | Scrape Wikipedia h2 Headers | HTTP requests, HTML parsing, heading extraction, lists, and request-error handling. |
| [day_2](day_2/README.md) | Hacker News Top Posts Scraper | CSS selectors, lists of dictionaries, CSV output, and script-relative paths. |
| [day_3](day_3/README.md) | Scrape Books to Scrape (70 Books) | Pagination, relative URL resolution, list slicing, and JSON export. |
| [day_4](day_4/README.md) | Download Cover Images of the First 10 Books | Image URLs, filename cleanup, streamed downloads, binary files, and script-relative folders. |
| [day_5](day_5/README.md) | Download Cover Images Using wget | Package-based downloading, progress display, numbered filenames, and local output folders. |
| [day_6](day_6/README.md) | Quote of the Day Image Maker | Quote extraction, tuples, text wrapping, Pillow drawing, and PNG output. |
| [day_7](day_7/README.md) | Crypto Price Tracker with Graphs | JSON API responses, timestamped CSV appends, coin IDs, and Matplotlib plots. |
| [day_8](day_8/README.md) | Hourly Crypto Price Logger | Job scheduling, polling loops, hourly API requests, and independent CSV history. |
| [day_9](day_9/README.md) | Store and Search Crypto Prices in SQLite | Database tables, inserts, commits, parameterized queries, and latest-price search. |
| [day_10](day_10/README.md) | Extract Text from a PDF | PyMuPDF, page iteration, string accumulation, local input paths, and exception handling. |

The `DAY_*.md` files are task statements maintained manually by the repository owner. Preserve original course wording where supplied. Day 10's description was authored locally from the script because no original task statement was available; its file identifies that origin. Keep task statements unchanged during documentation updates and record explanations and progress in README files.

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

Day 7 uses Requests and Matplotlib rather than HTML parsing:

```powershell
python -m pip install requests matplotlib
```

Days 8–9 require Requests and the schedule package. Day 9 still imports schedule, although it does not schedule any jobs:

```powershell
python -m pip install requests schedule
```

Day 9 uses Python's standard-library `sqlite3` module; no separate SQLite server or pip package is needed. The optional [SQLite Viewer extension](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer) displays its database in VS Code.

Day 10 reads a local PDF using PyMuPDF, imported as `pymupdf` in the working script:

```powershell
python -m pip install PyMuPDF
```

`beautifulsoup4` is the package name used by pip; Python imports it with `from bs4 import BeautifulSoup`. The HTML-scraping lessons use Python's built-in `html.parser`, so no additional parser package is needed. Days 7–9 read API JSON instead. Day 2 also uses `csv` and `pathlib`; Day 3 uses `json`, `pathlib`, and `urllib.parse`. Day 4 uses `os`, `pathlib`, `re`, and `urllib.parse`. Day 6 uses `os`, `pathlib`, and `textwrap`. Days 7–8 use `os`, `csv`, `pathlib`, and `datetime`; Day 8 also uses `time`. Day 9 adds `sqlite3`. These modules are part of Python's standard library.

From the repository root:

```powershell
python "challenges/03_web_scraping/day_1/day_1.py"
python "challenges/03_web_scraping/day_2/day_2.py"
python "challenges/03_web_scraping/day_3/day_3.py"
python "challenges/03_web_scraping/day_4/day_4.py"
python "challenges/03_web_scraping/day_5/day_5.py"
python "challenges/03_web_scraping/day_6/day_6.py"
python "challenges/03_web_scraping/day_7/day_7.py"
python "challenges/03_web_scraping/day_8/day_8.py"
python "challenges/03_web_scraping/day_9/day_9.py"
python "challenges/03_web_scraping/day_10/day_10.py"
```

Or open the script in VS Code and press **Ctrl + S** using the existing Run on Save configuration. Online lessons need internet access; Day 10 reads a local PDF after package installation. Day 1 prints its results in the terminal and does not create any data files.

See the [Day 1 README](day_1/README.md) for the function walkthrough, example, troubleshooting, and remaining challenge requirements.

Day 1 sends a descriptive `User-Agent` identifying the script and its project URL. The original generic Requests identification was rejected locally with HTTP 403. Its README preserves the [complete original tutorial code](day_1/README.md#original-tutorial-code) and explains the [request configuration and difference from the video](day_1/README.md#why-the-tutorial-request-returned-403). No API key or `.env` is needed for this lesson.

Day 2 uses the [Hacker News homepage](https://news.ycombinator.com/) as its source. It writes up to 20 titles and URLs to `day_2/hn_top20.csv`, beside `day_2.py`, regardless of the terminal's working directory. Each successful non-empty export replaces the previous CSV. See the [Day 2 README](day_2/README.md) for the selector, CSV format, and running instructions.

Day 3 uses [Books to Scrape](https://books.toscrape.com/), follows next-page links, and keeps up to 70 book titles and prices in JSON. Its `day_3/books_data.json` output stays beside `day_3.py` using a script-relative path, regardless of the terminal's working directory. See the [Day 3 output-location note](day_3/README.md#json-output-and-current-file-location) and [running instructions](day_3/README.md#how-to-run).

Day 4 also uses [Books to Scrape](https://books.toscrape.com/), downloading covers from the first 10 homepage listings into `day_4/images/`. The folder stays beside `day_4.py` regardless of the terminal's working directory. See the [Day 4 README](day_4/README.md) for filename cleanup, streamed binary downloads, and current error-handling behaviour.

Day 5 downloads the same first 10 homepage covers using [wget](https://pypi.org/project/wget/) and saves final files in `day_5/images/`. That folder is ignored by Git. Repeated saves can create numbered image copies instead of overwriting files; see the [Day 5 comparison with Day 4](day_5/README.md#difference-from-day-4) and its [setup instructions](day_5/README.md#setup).

Day 6 reads the first five quotes and authors from [Quotes to Scrape](https://quotes.toscrape.com/) and creates 800 × 400 PNG cards using Pillow. Output stays in `day_6/quotes/`, which is ignored by Git. Repeated runs overwrite the same numbered PNGs. See the [Day 6 guide](day_6/README.md) for installation, drawing steps, and current layout limitations.

Day 7 fetches JSON market data from [CoinGecko](https://www.coingecko.com/), appends timestamped prices to `day_7/crypto_prices.csv`, and displays stored prices for a selected coin ID in a Matplotlib window. The CSV stays beside the script and grows across runs. See the [Day 7 guide](day_7/README.md) for setup, API-access limitations, and the graph prompt.

Day 8 uses [schedule](https://schedule.readthedocs.io/en/stable/) to fetch CoinGecko prices at the beginning of each hour and append them to its own `day_8/crypto_prices.csv`. It does not fetch immediately or require Day 7's CSV. The process must remain running; `time.sleep(60)` controls checks for due work, not the hourly interval. See the [Day 8 guide](day_8/README.md) for startup timing, CSV creation, and stopping the loop with Ctrl + C.

Day 9 stores CoinGecko observations in `day_9/crypto.db` and searches for a coin's latest saved price. Its single-action menu currently fetches on demand; the original task's hourly scheduling is not implemented. See the [Day 9 guide](day_9/README.md) for the table structure, menu, and [SQLite Viewer instructions](day_9/README.md#opening-cryptodb-in-vs-code).

Day 10 reads the included two-page `day_10/test.pdf` and prints its text using `pymupdf`. The input path stays beside the script regardless of the terminal's working directory. Its README preserves the [complete original tutorial code](day_10/README.md#original-tutorial-code) and explains the [fixes](day_10/README.md#why-the-original-failed-and-what-changed), [PDF location](day_10/README.md#pdf-input-and-file-location), and clear error messages. Replace the sample with your own text-based PDF under the same name to try other input.

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
- [CoinGecko](https://www.coingecko.com/): the data provider for Days 7–9.
- [CoinGecko coins/markets API](https://docs.coingecko.com/demo/reference/coins-markets): market-data request parameters and response fields.
- [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html): drawing and displaying the Day 7 graph.
- [schedule documentation](https://schedule.readthedocs.io/en/stable/): the library used for Day 8 hourly jobs.
- [schedule examples](https://schedule.readthedocs.io/en/stable/examples.html): `.at()`, `run_pending()`, and polling loops.
- [schedule on PyPI](https://pypi.org/project/schedule/): installation and package information.
- [Python sqlite3 tutorial](https://docs.python.org/3/library/sqlite3.html#tutorial): creating tables, inserting records, and searching with SQL.
- [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer): inspecting Day 9 database records inside VS Code.
- [PyMuPDF documentation](https://pymupdf.readthedocs.io/en/latest/): the main reference for the Day 10 PDF reader.
- [PyMuPDF installation](https://pymupdf.readthedocs.io/en/latest/installation.html): the package used by Day 10's modern `pymupdf` import.
- [PyMuPDF text extraction](https://pymupdf.readthedocs.io/en/latest/recipes-text.html): reading text from document pages.
- [Wikimedia User-Agent policy](https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy/en): identification requirements for automated requests.

## Package source repositories

- [Requests — GitHub](https://github.com/psf/requests): HTTP requests (`requests`).
- [Matplotlib — GitHub](https://github.com/matplotlib/matplotlib): plotting data (`matplotlib.pyplot`).
- [Beautiful Soup — Launchpad](https://code.launchpad.net/beautifulsoup): HTML parsing; the upstream source is hosted on Launchpad (`bs4`).
- [Pillow — GitHub](https://github.com/python-pillow/Pillow): creating images and drawing text (`PIL`).
- [wget — PyPI and source archive](https://pypi.org/project/wget/): file downloads; no official GitHub repository was confirmed (`wget`).
- [schedule — GitHub](https://github.com/dbader/schedule): registering and checking scheduled jobs (`schedule`).
- [PyMuPDF — GitHub](https://github.com/pymupdf/PyMuPDF): PDF text extraction (`pymupdf`).

See the [complete package index](../../README.md#package-source-repositories) for import-name mappings and projects you can support with a GitHub star.
