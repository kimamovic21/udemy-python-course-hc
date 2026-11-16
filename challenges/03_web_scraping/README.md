# Challenges — Web Scraping

This group corresponds to `03_web_scraping` in the Udemy tutorial. It follows [01_utilities](../01_utilities/README.md) and [02_data_handling](../02_data_handling/README.md).

**Status: in progress — current course section.** Day 1 introduces fetching HTML with Requests and extracting headings with Beautiful Soup.

[Challenge index](../README.md) · [Main project overview](../../README.md#folder-overview)

## Learning order and folder layout

Local numbering starts again at `day_1`. Each lesson folder contains the script, the original task, and a README with implementation details and running instructions.

| Lesson guide | Project | Main concepts |
| --- | --- | --- |
| [day_1](day_1/README.md) | Scrape Wikipedia h2 Headers | HTTP requests, HTML parsing, heading extraction, lists, and request-error handling. |

The `DAY_*.md` files contain original task statements maintained manually by the repository owner. Keep their contents unchanged; record explanations and progress in README files.

## Setup and running

Install the packages with the Python interpreter used to run the project:

```powershell
python -m pip install requests beautifulsoup4
```

`beautifulsoup4` is the package name used by pip; Python imports it with `from bs4 import BeautifulSoup`. The script uses Python's built-in `html.parser`, so no additional parser package is needed.

From the repository root:

```powershell
python "challenges/03_web_scraping/day_1/day_1.py"
```

Or open the script in VS Code and press **Ctrl + S** using the existing Run on Save configuration. An internet connection is required for the page request. Day 1 prints its results in the terminal and does not create any data files.

See the [Day 1 README](day_1/README.md) for the function walkthrough, example, troubleshooting, and remaining challenge requirements.

Day 1 sends a descriptive `User-Agent` identifying the script and its project URL. The original generic Requests identification was rejected locally with HTTP 403. Its README preserves the [complete original tutorial code](day_1/README.md#original-tutorial-code) and explains the [request configuration and difference from the video](day_1/README.md#why-the-tutorial-request-returned-403). No API key or `.env` is needed for this lesson.

## Useful links for beginners

- [Python Package Index (PyPI)](https://pypi.org/): browse external Python packages used in these projects.
- [Beautiful Soup quick start](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start): parsing HTML and exploring tags and text.
- [Requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/): fetching a page and working with its response.
- [Wikimedia User-Agent policy](https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy/en): identification requirements for automated requests.
