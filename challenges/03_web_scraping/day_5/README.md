# Day 5: Download Cover Images Using wget

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to read the first 10 book listings from [Books to Scrape](https://books.toscrape.com/) and download their covers with the Python [wget package](https://pypi.org/project/wget/). This lesson keeps Day 4's scraping approach while replacing the active image-download call.

## Files

| File | Purpose |
| --- | --- |
| [DAY_5.md](DAY_5.md) | The original challenge statement and bonus tasks, maintained manually and left unchanged. |
| [day_5.py](day_5.py) | Finding book titles and cover URLs, then downloading images with `wget.download()`. |
| `images/` | Local output folder beside the script; excluded from Git for this lesson only. |

## Setup

Install the external packages using the interpreter that runs the script:

```powershell
python -m pip install requests beautifulsoup4 wget
```

If Requests and Beautiful Soup are already installed in that interpreter, the additional command is:

```powershell
python -m pip install wget
```

This is the Python package imported with `import wget`; no separate system command installation is needed. `requests` is still used for the homepage, and `from bs4 import BeautifulSoup` parses its HTML. The `os`, `pathlib`, `re`, and `urllib.parse` modules and the `html.parser` parser come with Python.

For `ModuleNotFoundError: No module named 'wget'`, install it in the same interpreter used by the terminal and selected through **Python: Select Interpreter** in VS Code. Verify the import with:

```powershell
python -c "import wget; print('wget import OK')"
```

No API key or `.env` file is needed.

## How the code works

1. `scrape_and_download_images()` downloads the Books to Scrape homepage with Requests and parses it with Beautiful Soup.
2. `soup.select("article.product_pod")[:10]` selects up to 10 book cards. The script reads each full title from the title link and each relative image URL from the image's `src` attribute.
3. `urljoin(BASE_URL, relative_img)` resolves the full cover URL. `sanitize_filename(title)` removes characters outside its allowed pattern and replaces spaces with underscores before `.jpg` is appended.
4. The script creates `IMAGE_DIR` if missing and joins each generated filename to that folder.
5. `wget.download(img_url, filepath)` handles the active image download and file saving, with the package's default progress display.
6. The terminal also prints the image URL, requested file path, and title for each book. The main guard starts the program when `day_5.py` is run directly.

The older `download_image()` function remains in the file for comparison, but its call is commented out. Its Requests-based streaming code and exception handler do not run when the active `wget.download()` call is used.

## Difference from Day 4

| Behaviour | Day 4 | Day 5 |
| --- | --- | --- |
| Homepage parsing | Requests and Beautiful Soup. | Requests and Beautiful Soup. |
| Active image download | `download_image()` writes chunks manually. | `wget.download()` handles downloading and saving. |
| Additional dependency | No `wget` dependency. | Requires the `wget` package. |
| Download progress | Book-by-book messages. | Book messages plus the package's progress display. |
| Existing destination | `"wb"` overwrites the same filename. | An existing filename causes a numbered new filename. |
| Image error handling | The helper catches errors and continues. | The active `wget.download()` call has no surrounding exception handler. |

### Repeated saves and duplicate images

Every **Ctrl + S** runs the script again. In this version, the installed `wget` package (3.2) preserves existing files by choosing another filename. For example:

```text
A_Light_in_the_Attic.jpg
A_Light_in_the_Attic (1).jpg
A_Light_in_the_Attic (2).jpg
```

It does not skip an image just because it already exists. The folder can therefore contain more than 10 images after repeated runs. The returned filename from `wget.download()` is not captured by the current script, so the printed `filepath` is the requested path, not necessarily the final numbered name.

## Image folder and Git

```python
IMAGE_DIR = Path(__file__).resolve().parent / "images"
```

Final downloaded covers stay in:

```text
challenges/03_web_scraping/day_5/images/
```

This works from the repository root, from the lesson folder, and through VS Code's **Ctrl + S** execution. Only this lesson's image folder is excluded through its exact path in the root [.gitignore](../../../.gitignore); the rule does not ignore other image folders. The images remain local and are generated again by running the script after cloning.

The installed package uses a temporary file in the terminal's working directory during transfer, then moves the completed download to the destination. This is separate from the final `day_5/images/` location; an interrupted download can leave a temporary file behind.

## How to run

From the repository root:

```powershell
python "challenges/03_web_scraping/day_5/day_5.py"
```

Or, from this lesson's folder:

```powershell
python .\day_5.py
```

In VS Code, open `day_5.py` and press **Ctrl + S**. There are no input prompts. After downloading, inspect the local `images/` folder and remember that repeated runs can create numbered copies.

## Current behaviour to understand

- The homepage request has no explicit timeout, HTTP status check, or exception handler. The active image-download call also has no surrounding handler, so an exception can stop the remaining downloads.
- The unused Requests helper's `timeout=10` and `try/except` do not configure or protect the `wget` calls.
- The final message says `All 10 books covers downloaded to images/` if execution reaches it; it does not calculate a successful download count. Fewer than 10 matching cards would still produce the same message.
- The code adds a `.jpg` filename but does not convert or edit image content. It does not read the Day 3 JSON or reuse the Day 4 image folder.

## Useful links for beginners

- [wget on PyPI](https://pypi.org/project/wget/): the package used in this lesson, including installation, API examples, and progress display.
- [Books to Scrape](https://books.toscrape.com/): the source of the book titles and cover-image URLs.
- [Beautiful Soup CSS selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors): selecting book cards and their elements.
- [Requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/): the library still used for fetching the homepage.
- [Paths with pathlib](https://docs.python.org/3/library/pathlib.html): keeping the final image folder beside the script.

[Previous: Day 4](../day_4/README.md) · [Next: Day 6](../day_6/README.md)
