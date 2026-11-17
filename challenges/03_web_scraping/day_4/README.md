# Day 4: Download Cover Images of the First 10 Books

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to visit [Books to Scrape](https://books.toscrape.com/), read the first 10 book listings on the homepage, and download their cover images. Each image is saved using a filename derived from the book title.

## Files

| File | Purpose |
| --- | --- |
| [DAY_4.md](DAY_4.md) | The original challenge statement and bonus tasks, maintained manually and left unchanged. |
| [day_4.py](day_4.py) | Extracting cover URLs, cleaning filenames, and downloading image bytes. |
| `images/` | Runtime folder created inside `day_4` for the downloaded covers. |

This lesson creates image files rather than CSV or JSON output. It uses the same practice website as Day 3, but reads the homepage and does not follow pagination.

## Setup

Install the external packages using the Python interpreter that runs the project:

```powershell
python -m pip install requests beautifulsoup4
```

`requests` retrieves the homepage and image files. `BeautifulSoup`, imported from `bs4`, parses the HTML. The `os`, `pathlib`, `re`, and `urllib.parse` modules and the `html.parser` parser come with Python. No API key, `.env`, or image-processing package is needed.

If the packages were installed for previous scraping lessons in the same interpreter, they are already available. See the [Day 1 setup notes](../day_1/README.md#setup) for unresolved-import troubleshooting.

## How the code works

1. `scrape_and_download_images()` requests the homepage, parses its HTML, and selects up to 10 book cards using `soup.select("article.product_pod")[:10]`.
2. `book.h3.a["title"]` reads the full book title. `book.find("img")["src"]` reads the image's relative URL, and `urljoin(BASE_URL, relative_img)` turns it into a full download URL.
3. The script creates `IMAGE_DIR` with `os.makedirs()` if the directory does not exist.
4. `sanitize_filename(title)` removes characters outside the allowed pattern and replaces spaces with underscores. The script appends `.jpg` and joins the filename to `IMAGE_DIR`.
5. `download_image(img_url, filepath)` requests the image with `stream=True` and `timeout=10`, then checks its HTTP status with `raise_for_status()`.
6. The destination is opened in `"wb"` mode: write binary. `response.iter_content(8192)` reads the image in chunks requested at 8,192 bytes, and `f.write(chunk)` writes those bytes to disk.
7. The terminal displays the image URL, destination path, and book title before each download attempt. The main guard runs the scraper when `day_4.py` is executed directly.

## Filename example

For a title such as `A Light in the Attic`, the output filename becomes:

```text
A_Light_in_the_Attic.jpg
```

The regular expression allows word characters, hyphens, underscores, dots, and spaces before spaces are replaced. For example, punctuation such as `:` and `?` is removed. The script writes the downloaded bytes with a `.jpg` filename; it does not edit or convert the image.

## Image folder and file paths

```python
IMAGE_DIR = Path(__file__).resolve().parent / "images"
```

`Path(__file__).resolve().parent` locates the script's directory. All covers are therefore saved under:

```text
challenges/03_web_scraping/day_4/images/
```

For example:

```text
challenges/03_web_scraping/day_4/images/A_Light_in_the_Attic.jpg
```

The output location stays the same when running from the repository root, from the lesson folder, or through **Ctrl + S** in VS Code. The earlier plain `"images"` path depended on the terminal's working directory and could create an image folder in the root.

Existing images with the same generated filename are overwritten by `"wb"` mode. The script reuses an existing `images/` folder and does not remove unrelated files from it.

This lesson's `images/` folder is local output and is excluded from Git through its exact path in the root [.gitignore](../../../.gitignore). Other image folders are unaffected by that rule. Run `day_4.py` after cloning to download the covers locally.

## How to run

From the repository root:

```powershell
python "challenges/03_web_scraping/day_4/day_4.py"
```

Or, from this lesson's folder:

```powershell
python .\day_4.py
```

In VS Code, open `day_4.py` and press **Ctrl + S**. There are no input prompts. Wait for the download messages, then open `day_4/images` in the Explorer to inspect the saved covers.

## Current behaviour to understand

- The script attempts downloads for the first 10 matching homepage listings, or fewer if fewer are found. It does not use the 70-book JSON from Day 3.
- Each image download catches `Exception`, including request and file-writing failures, and prints the destination and exception. A failed download can leave an incomplete file.
- The initial homepage request has no explicit timeout, status check, or exception handler. Errors at that stage are not handled like the image-download errors.
- The final message always says `All 10 books covers downloaded to images/`. It is not a verified success count, so also check individual error messages and the saved files.
- Progress is reported per book; there is no byte-percentage progress bar. Different titles that produce the same cleaned filename can overwrite each other's files.

## Useful links for beginners

- [Books to Scrape](https://books.toscrape.com/): the practice website providing this project's book titles and cover images.
- [Beautiful Soup CSS selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors): selecting book cards and their elements.
- [Requests streaming downloads](https://requests.readthedocs.io/en/latest/user/advanced/#body-content-workflow): reading response data incrementally with `stream=True` and `iter_content()`.
- [Replacing matches with re.sub()](https://docs.python.org/3/library/re.html#re.sub): the substitution used to clean book titles for filenames.
- [Paths with pathlib](https://docs.python.org/3/library/pathlib.html): keeping the image folder beside the script.
- [Combining URLs with urljoin()](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin): resolving relative image addresses.

[Previous: Day 3](../day_3/README.md)
