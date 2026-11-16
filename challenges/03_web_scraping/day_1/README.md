# Day 1: Scrape Wikipedia h2 Headers

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to download the [Wikipedia page about the Python programming language](https://en.wikipedia.org/wiki/Python_%28programming_language%29), extract its `<h2>` section headings, and collect their text in a list. This introduces web scraping: reading a page's HTML and extracting selected information from it.

## Files

| File | Purpose |
| --- | --- |
| [DAY_1.md](DAY_1.md) | The original challenge statement and bonus tasks, maintained manually and left unchanged. |
| [day_1.py](day_1.py) | Fetching Wikipedia HTML, finding `<h2>` tags, and printing heading titles. |

The script prints to the terminal. It does not create or read a local CSV, JSON, or other data file.

## Setup

Install both external packages using the Python interpreter that runs the script:

```powershell
python -m pip install requests beautifulsoup4
```

| Installed package | Python import | Responsibility |
| --- | --- | --- |
| `requests` | `import requests` | Download the page over HTTP. |
| `beautifulsoup4` | `from bs4 import BeautifulSoup` | Parse the returned HTML and search its elements. |

`html.parser` is built into Python. This example does not require `lxml`, an API key, or an `.env` file.

If Pylance reports `Import "bs4" could not be resolved`, install `beautifulsoup4` in the same interpreter selected through **Python: Select Interpreter** in VS Code. The package and import names differ. If the warning persists after selecting the correct interpreter, use **Developer: Reload Window**.

To check the Python used by the terminal and verify both imports:

```powershell
python -c "import sys; print(sys.executable)"
python -c "import requests; from bs4 import BeautifulSoup; print('Imports OK')"
```

## Original tutorial code

This is the complete original `day_1.py` downloaded from the Udemy lesson, preserved as a reference before the request-header adjustment. Compare it with the working [day_1.py](day_1.py). The original task statement in [DAY_1.md](DAY_1.md) remains unchanged.

```python
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"


def get_h2_headers(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")
    print(h2_tags)
    headers = []
    for tag in h2_tags:
        header_text = tag.get_text(strip=True)
        if header_text and header_text.lower() != "contents":
            headers.append(header_text)
    print(headers)


get_h2_headers(URL)
```

## Why the tutorial request returned 403

During local troubleshooting, the original request returned **HTTP 403 Forbidden**. The server response explicitly asked for a User-Agent and referred to Wikimedia's robot policy. The request used Requests' default identification, `python-requests/2.34.2`.

The [Wikimedia User-Agent policy](https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy/en) explains that generic client identifiers such as `python-requests/x` may be blocked. Automated scripts should identify their purpose and provide a contact method, such as a project website.

The video shows what worked in the instructor's environment at recording time. We cannot confirm the exact cause of the difference from the video alone: enforcement and access conditions can vary over time and between environments. In this local run, the server message identified the missing descriptive User-Agent, and the request succeeded after adding it. This does not indicate a Windows-specific Python problem or a Beautiful Soup installation failure.

### Request configuration in the working file

The working script adds a `request_headers` dictionary and passes it through the `headers=` argument:

```python
request_headers = {
    "User-Agent": (
        "PythonCourseHeadingScraper/1.0 "
        "(https://github.com/kimamovic21/udemy-python-course-hc)"
    )
}
response = requests.get(url, headers=request_headers, timeout=10)
```

`User-Agent` is the HTTP header name. Its value identifies this learning script, its version, and the project URL. Someone adapting the script for a different project should use their own descriptive identifier and a valid project or contact URL. No API key, account login, or `.env` configuration is required here. Use an informative script identity as described in the policy rather than copying a browser's identity.

The original function name, timeout, status check, exception handler, heading extraction, and printed output are retained. `request_headers` holds HTTP configuration; the existing `headers` list still collects the extracted titles. The old executable request and change-attribution comments have been removed from the Python file; the complete original remains above.

### Troubleshooting

| Symptom | Meaning and next step |
| --- | --- |
| `Import "bs4" could not be resolved` or `ModuleNotFoundError` | Install `beautifulsoup4` in the interpreter used by VS Code and the terminal; follow Setup above. |
| `403 Client Error: Forbidden` | The server refused the request. Check that the working request passes `request_headers`, read the response message, and consult Wikimedia's User-Agent policy. An informative header addresses the diagnosed issue but cannot guarantee access under every server or network condition. |
| Connection error or timeout | Check connectivity and the exception printed after `Failed to fetch page:`. |
| Two empty lists | The request succeeded, but the returned HTML contained no `<h2>` elements. |

## How the code works

1. `URL` selects the Wikipedia article about Python. `get_h2_headers(URL)` starts the request when the file runs. The call is at module level, so importing the file also starts it.
2. `request_headers` identifies the learning script. `requests.get(url, headers=request_headers, timeout=10)` sends that identification with the request and uses a 10-second timeout setting. `response.raise_for_status()` raises an exception for an unsuccessful HTTP status such as 403 or 404.
3. `except requests.RequestException` catches request failures, prints `Failed to fetch page:` with the exception, and returns an empty list. This includes connection failures, timeouts, and HTTP errors raised above.
4. `BeautifulSoup(response.text, "html.parser")` parses the returned HTML. `soup.find_all("h2")` finds all second-level heading elements. The first `print()` displays those tags, including their markup.
5. The loop uses `tag.get_text(strip=True)` to extract text and strip whitespace from each text fragment. It skips empty text and headings whose complete text equals `contents`, ignoring case.
6. Other titles are appended to `headers`. The second `print()` displays the list of extracted strings.

On success, the function prints the list and reaches the end without an explicit `return`, so its return value is `None`. The list is local to the function; it is not returned to the caller in the current version.

## Example

For illustration, if the downloaded page contained only:

```html
<h2>History</h2>
<h2>Contents</h2>
<h2><span>Design</span></h2>
```

The script would first print the three HTML tags, then this list:

```text
['History', 'Design']
```

This is an illustrative example, not a fixed snapshot of Wikipedia. Live headings and their count can change when the page changes.

## Current challenge coverage

| Requirement | Current implementation |
| --- | --- |
| Download the page HTML | Implemented with Requests and a timeout setting. |
| Parse all `<h2>` headings | Implemented with Beautiful Soup. |
| Collect heading text in a list | Implemented; empty text and an exact `Contents` heading are skipped. |
| Print the total and first 10 titles | Pending; the script currently prints all tags and the complete title list. |
| Remove trailing `[edit]` | Pending; `get_text(strip=True)` extracts text but does not explicitly remove this label. |
| Handle network errors | Implemented through `requests.RequestException`. |

## How to run

From the repository root:

```powershell
python "challenges/03_web_scraping/day_1/day_1.py"
```

Or, from this lesson's folder:

```powershell
python .\day_1.py
```

In VS Code, open `day_1.py` and press **Ctrl + S**. This script has no input prompts; wait for its terminal output. If it prints `Failed to fetch page:`, read the following exception for the reason. A failed request produces no heading lists. A successful response containing no `<h2>` elements produces two empty lists.

## Useful links for beginners

- [Python Package Index (PyPI)](https://pypi.org/): find Python packages such as `requests` and `beautifulsoup4`, including their installation instructions and project information.
- [Installing Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup): why the pip package is named `beautifulsoup4` while the import is `bs4`.
- [Beautiful Soup quick start](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start): short HTML parsing examples.
- [Finding tags with find_all()](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all): selecting matching HTML elements.
- [Extracting text with get_text()](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text): reading tag text and controlling whitespace.
- [Requests errors and exceptions](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions): request failures, HTTP status errors, and timeouts.
- [Wikimedia User-Agent policy](https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy/en): how scripts should identify themselves and why generic client identifiers may receive HTTP 403.
