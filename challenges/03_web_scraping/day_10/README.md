# Day 10: Extract Text from a PDF

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to read a local PDF, extract text from every page, combine the results, and print them in the terminal. This lesson uses PyMuPDF for local document processing rather than website requests.

## Files

| File | Purpose |
| --- | --- |
| [DAY_10.md](DAY_10.md) | The locally authored task based on the lesson script; not an original Udemy task statement. |
| [day_10.py](day_10.py) | The working reader using `pymupdf`, a script-relative PDF path, and specific error messages. |
| [test.pdf](test.pdf) | A two-page demonstration PDF created for this repository, containing selectable practice text. |

The script reads the PDF without modifying it and prints its text. It does not create a text, CSV, JSON, or image output file. Replace the sample PDF with your own document under the same filename to try different input.

## Original tutorial code

The complete code downloaded from the tutorial is preserved below, before the fixes. This is a historical reference; run the working [day_10.py](day_10.py) for the current version.

```python
import fitz


def read_pdf(file_path):
    doc = fitz.open(file_path)
    all_text = ""

    for page_num in range(len(doc)):
        page = doc[page_num]
        all_text += page.get_text()

    doc.close()
    return all_text


if __name__ == "__main__":
    file_path = "test.pdf"
    try:
        content = read_pdf(file_path)
        print("-" * 30)
        print(content)
        print("-" * 30)
    except Exception as e:
        print("Failed to read pdf, change that method")
```

## Why the original failed and what changed

Two separate issues produced the reported output:

- `import fitz` used a legacy PyMuPDF name and displayed a deprecation warning. The active script now uses `import pymupdf`.
- No `test.pdf` was present, and the relative filename was resolved from the terminal's working directory. The generic `except Exception` message hid the underlying error. The working code now resolves the input beside the script, includes a demonstration PDF, and prints useful error details.

The function name, page loop, accumulated string, and separator output remain close to the tutorial. A `with` block closes the document even if extraction raises an exception. A PDF without extractable text receives an explicit message.

## Setup

Install the package using the interpreter that runs the project:

```powershell
python -m pip install PyMuPDF
```

The installed package is **PyMuPDF**, and the working import is `pymupdf`. The historical `fitz` import remains only in the reference code above. For a missing module, install the package in the interpreter selected through **Python: Select Interpreter** in VS Code.

Verify the import with:

```powershell
python -c "import pymupdf; print('PyMuPDF import OK')"
```

`pathlib` is part of Python. No Requests, Beautiful Soup, API key, `.env`, or internet connection is required to read the local PDF after installation.

## PDF input and file location

The working script uses:

```python
file_path = Path(__file__).resolve().parent / "test.pdf"
```

It always reads:

```text
challenges/03_web_scraping/day_10/test.pdf
```

This works from the repository root, from the lesson folder, and through VS Code's **Ctrl + S** execution. A separate `test.pdf` in the root is not selected automatically.

The included sample has two pages with headings `Page 1` and `Page 2 - More Text to Extract`. It is locally created demonstration content, not a document downloaded from Udemy. To use another PDF, replace this file while retaining the name `test.pdf`. Prefer a document with selectable text; scanned page images need OCR, which this script does not perform.

## How the working code works

1. `read_pdf(file_path)` starts with an empty `all_text` string and opens the document with `with pymupdf.open(file_path) as doc:`.
2. `range(len(doc))` visits zero-based page indexes. `doc[page_num]` retrieves each page, and `page.get_text()` extracts its existing text.
3. `all_text += ...` appends the page text. Leaving the `with` block closes the document before the combined string is returned. No extra page separators are inserted.
4. The main guard builds the input path and attempts to read it. Missing-file errors receive their own message; document-data, operating-system, and value errors display the underlying reason.
5. If the returned text is non-empty after stripping whitespace, it is printed between two lines of 30 hyphens. Otherwise, the program prints `No extractable text found. This PDF may contain scanned images.`

Exact text order and line breaks depend on how the PDF stores its content. Plain-text extraction does not reproduce a PDF's visual layout.

## How to run

From the repository root:

```powershell
python "challenges/03_web_scraping/day_10/day_10.py"
```

Or, from this lesson's folder:

```powershell
python .\day_10.py
```

In VS Code, open `day_10.py` and press **Ctrl + S**. There are no input prompts. The supplied example should print text from both pages without the old `fitz` warning.

## Troubleshooting and current coverage

| Message or requirement | Meaning |
| --- | --- |
| Missing `pymupdf` import | Install PyMuPDF in the interpreter used by the project. |
| `PDF file not found: ...` | The required `test.pdf` is missing beside the script; the message includes the expected path. |
| `Failed to read PDF: ...` | Reading failed; the message includes the library or file-system error, for example for a malformed or empty file. |
| `No extractable text found...` | The PDF is blank or has no text layer. This reader does not perform OCR. |
| Page count | The page-count bonus from the local task is not implemented. |

The program does not authenticate password-protected PDFs, reconstruct layout, or export a separate text file.

## Validation

The working script was checked from both the repository root and the lesson folder using the included two-page sample. Additional temporary inputs covered a missing file, malformed PDF, zero-byte file, and valid blank PDF. These checks do not alter the learner's input file.

## Useful links for beginners

- [PyMuPDF documentation](https://pymupdf.readthedocs.io/en/latest/): the main reference for the PDF library used in Day 10.
- [PyMuPDF installation](https://pymupdf.readthedocs.io/en/latest/installation.html): installation and the modern `pymupdf` import name.
- [PyMuPDF text extraction](https://pymupdf.readthedocs.io/en/latest/recipes-text.html): reading document text and understanding its order.
- [Paths with pathlib](https://docs.python.org/3/library/pathlib.html): resolving the PDF path from the script's location.

## Package source repositories

- [PyMuPDF — GitHub](https://github.com/pymupdf/PyMuPDF): PDF text extraction (`pymupdf`).

See the [complete package index](../../../README.md#package-source-repositories) for import-name mappings and projects you can support with a GitHub star.

[Previous: Day 9](../day_9/README.md)
