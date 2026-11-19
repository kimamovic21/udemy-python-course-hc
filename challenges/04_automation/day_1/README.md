# Day 1: File Organizer

This script groups files by extension into `PDFs`, `Images`, `TextFiles`, and `Others` folders.

This is the first project in the current tutorial section, `04_automation`, following [03_web_scraping](../../03_web_scraping/README.md). Local project numbering starts again at Day 1.

[Automation overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

## Running the project

Only Python's standard-library modules `os` and `shutil` are needed; no additional packages are required. From the repository root:

```powershell
python "challenges/04_automation/day_1/day_1.py"
```

Run `day_1.py` or save it with the existing VS Code run-on-save setup. The script uses its own location as the working folder: `challenges/04_automation/day_1`. It does not ask for a folder path.

- Only files directly beside the script are organized; existing subfolders are skipped.
- `day_1.py`, `DAY_1.md`, and `README.md` stay in place.
- Output folders are created beside the script, regardless of the terminal's current directory.
- If the folder contains only these three project files, nothing is moved.

To try the organizer, place a few sample files beside the script before running it. Files are moved into the matching output folders.

## Why the tutorial version was adjusted

The original version uses `os.getcwd()` when the folder prompt is left blank. This means the terminal's current directory, which may be the repository root when running from VS Code. It can therefore move project files unintentionally.

The current version uses `os.path.dirname(os.path.abspath(__file__))` and skips the three project files. After moving the lesson into `day_1`, the script automatically uses that folder without any Python code changes.

## Original tutorial code — reference only

The original code below is preserved for comparison. Running it with a blank folder input can organize the terminal's current directory.

```python
import os
import shutil

EXTENSION_MAP = {
    "PDFs": [".pdf"],
    "Images": [".png", ".jpeg", ".jpg"],
    "TextFiles": [".txt"],
}


def get_destination_folder(filename):
    ext = os.path.splitext(filename)[1].lower()
    for folder, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return folder
    return "Others"


def sort_files(folder_path):
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        # write a check if file name is "day_01.py" then ignore this file

        if os.path.isfile(full_path):
            dest_folder = get_destination_folder(file)
            dest_path = os.path.join(folder_path, dest_folder)

            os.makedirs(dest_path, exist_ok=True)

            # move the file
            shutil.move(full_path, os.path.join(dest_path, file))
            print(f"Moved : {file} -> {dest_folder}/")


if __name__ == "__main__":
    folder = input("Enter the folder path or leave blank: ").strip()
    folder = folder or os.getcwd()

    if not os.path.isdir(folder):
        print("Invalid directory")
    else:
        sort_files(folder)
        print("✅ sorting completed")
```
