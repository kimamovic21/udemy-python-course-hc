# Day 6: Quote of the Day Image Maker

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to extract quote text and authors from [Quotes to Scrape](https://quotes.toscrape.com/) and create a PNG image for each of the first five quotes. Unlike Days 4–5, this script generates new images from text instead of downloading existing image files.

## Files

| File | Purpose |
| --- | --- |
| [DAY_6.md](DAY_6.md) | The original challenge statement, maintained manually and left unchanged. |
| [day_6.py](day_6.py) | Fetching quotes and drawing quote cards with Pillow. |
| `quotes/` | Generated PNG output beside the script, excluded from Git for this lesson only. |

## Setup

Install the external packages using the Python interpreter that runs the script:

```powershell
python -m pip install requests beautifulsoup4 Pillow
```

If Requests and Beautiful Soup are already installed in that interpreter, only the additional image library is needed:

```powershell
python -m pip install Pillow
```

| Installed package | Python import | Role |
| --- | --- | --- |
| `requests` | `import requests` | Download the quote page HTML. |
| `beautifulsoup4` | `from bs4 import BeautifulSoup` | Find quote text and authors. |
| `Pillow` | `from PIL import Image, ImageDraw, ImageFont` | Create images and draw text. |

The package is called **Pillow**, but its import namespace is **PIL**. The `os`, `pathlib`, and `textwrap` modules and the `html.parser` parser are part of Python. No API key, `.env`, `wget`, or separate font download is required for this example.

For a missing `PIL` import, install Pillow in the same interpreter selected through **Python: Select Interpreter** in VS Code. Verify the import with:

```powershell
python -c "from PIL import Image, ImageDraw, ImageFont; print('Pillow import OK')"
```

## How the code works

1. `fetch_quotes()` downloads `BASE_URL` and parses the HTML with Beautiful Soup. `soup.select("div.quote")` finds quote blocks; `quotes[:5]` limits processing to the first five.
2. For each block, the script reads `span.text` and removes curly quotation marks from the text's edges with `.strip("“”")`. It also reads the `small.author` element.
3. Each quote is appended as a `(text, author)` tuple. `main()` loops over these tuples using `enumerate()`, which also supplies a zero-based index.
4. `create_image(text, author, index)` creates an **800 × 400 pixel RGB image** using `Image.new()`. The background is `#f8d77f`, and the text is `#262626`.
5. `ImageDraw.Draw(image)` provides drawing methods, while `ImageFont.load_default()` supplies a default font. `textwrap.fill(text, width=60)` inserts line breaks at a target width of 60 characters.
6. The quote is drawn starting at `(40, 60)`. The author is prefixed with `-` and drawn starting at x-coordinate `500`, with a y-coordinate based on the quote's line count.
7. The output folder is created if necessary. `image.save(filename)` writes `quote_1.png`, `quote_2.png`, and subsequent numbered PNGs, then prints the saved path.

The main guard calls `main()` only when the script is executed directly. The current selection is the first five quotes on the homepage; it does not choose randomly, follow pagination, or schedule a daily run.

## Output folder and Git

```python
OUTPUT_DIR = Path(__file__).resolve().parent / "quotes"
```

The final output stays in the lesson folder:

```text
challenges/03_web_scraping/day_6/quotes/
    quote_1.png
    quote_2.png
    quote_3.png
    quote_4.png
    quote_5.png
```

The script-relative path works from the repository root, from the Day 6 folder, and through VS Code's **Ctrl + S** execution. It no longer depends on the terminal's current working directory.

Only this lesson's `quotes/` folder is excluded through its exact path in the root [.gitignore](../../../.gitignore). Other folders named `quotes` are unaffected by that rule. These generated images stay local; run the script after cloning to create them again.

**Repeated saves overwrite the same numbered PNGs.** Unlike Day 5's wget downloader, this script does not create names such as `quote_1 (1).png`. It does not delete unrelated files already in the output folder.

## How to run

From the repository root:

```powershell
python "challenges/03_web_scraping/day_6/day_6.py"
```

Or, from this lesson's folder:

```powershell
python .\day_6.py
```

In VS Code, open `day_6.py` and press **Ctrl + S**. There are no input prompts. Wait for the saved-path messages, then open the PNGs from `day_6/quotes` in the Explorer.

## Current behaviour to understand

- Up to five images are generated, depending on the matching quotes returned. No matching quote blocks means no new images and no new output folder.
- The page request has no explicit timeout, HTTP status check, or exception handler. Network, missing-element, and image-writing errors are not handled separately.
- The canvas, text positions, and line-spacing calculation are fixed. Character-based wrapping does not measure the rendered pixel width, so unusually long text or author names may not fit the layout.
- `author_font` is loaded but unused in the current code; both text-drawing calls use `font`.
- The code creates quote cards directly. It does not use book records, downloaded covers, or any other previous lesson's files.

## Useful links for beginners

- [Quotes to Scrape](https://quotes.toscrape.com/): the source of the quote text and author names used here.
- [Pillow on PyPI](https://pypi.org/project/Pillow/): the image library installed as Pillow and imported as PIL.
- [Pillow tutorial](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html): basic image creation and saving.
- [Beautiful Soup CSS selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors): locating quote blocks in HTML.
- [Python textwrap](https://docs.python.org/3/library/textwrap.html#textwrap.fill): wrapping the quote into multiple lines.
- [Paths with pathlib](https://docs.python.org/3/library/pathlib.html): keeping generated images beside the script.

[Previous: Day 5](../day_5/README.md)
