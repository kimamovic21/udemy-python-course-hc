from pathlib import Path

import pymupdf


def read_pdf(file_path):
    all_text = ""

    with pymupdf.open(file_path) as doc:
        for page_num in range(len(doc)):
            page = doc[page_num]
            all_text += page.get_text()

    return all_text


if __name__ == "__main__":
    file_path = Path(__file__).resolve().parent / "test.pdf"
    try:
        content = read_pdf(file_path)
    except (FileNotFoundError, pymupdf.FileNotFoundError):
        print(f"PDF file not found: {file_path}")
    except (pymupdf.FileDataError, OSError, ValueError) as e:
        print(f"Failed to read PDF: {e}")
    else:
        if content.strip():
            print("-" * 30)
            print(content)
            print("-" * 30)
        else:
            print("No extractable text found. This PDF may contain scanned images.")
