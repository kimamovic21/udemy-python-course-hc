# Day 2: Batch Rename Files in a Folder

Rename multiple files with the same extension using a shared base name and a numbered suffix, such as `house_1.jpg`, `house_2.jpg`, and `house_3.jpg`. Only filenames change; file contents stay the same.

[Automation overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

## Setup and running

The script uses Python's standard-library `os` module. No additional packages are required.

Create an `images` folder beside `day_2.py` if it does not exist, and put your practice images inside it before running the script. The script expects this folder to exist; it does not create it automatically.

From the repository root:

```powershell
python "challenges/04_automation/day_2/day_2.py"
```

Or open `day_2.py` in VS Code and press **Ctrl + S** with the existing Run on Save setup. Click in the terminal to answer the prompts and press **Enter** after each answer.

## Example: renaming house photos

Place these sample images inside `day_2/images`:

```text
bedroom.jpg
kitchen.jpg
toilet.jpg
```

Enter `house` as the base name and `.jpg` as the extension, including the dot. The script previews:

```text
bedroom.jpg => house_1.jpg
kitchen.jpg => house_2.jpg
toilet.jpg => house_3.jpg
```

Enter `y` to apply the changes. Any other answer cancels without renaming files. The current naming pattern uses an underscore (`_`), rather than a hyphen (`-`).

## How the code works

1. `os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")` selects the `images` folder beside the script.
2. `batch_rename()` checks that the base name and extension are non-empty and contain no path separators or drive colon.
3. `os.listdir()` finds entries directly in that folder. The script keeps matching files, skips subfolders, and protects `day_2.py`, `DAY_2.md`, and `README.md`.
4. `.lower().endswith()` matches the extension without distinguishing uppercase and lowercase. `.sort()` orders the original filenames before numbering.
5. `enumerate(files, start=1)` generates suffixes starting at `1`.
6. Before showing the preview, the script stops if a proposed filename belongs to a different existing file.
7. After confirmation, `os.rename()` applies each new name and the terminal reports the number of files processed.

## Folder scope and tutorial adjustment

The working script always uses `challenges/04_automation/day_2/images`, even when launched from the repository root. It does not ask for another folder path or scan folders nested inside `images`. Renamed images stay in that same folder; no separate output file or directory is created.

```text
day_2/
├── day_2.py
├── DAY_2.md
├── README.md
└── images/          # local practice images, ignored by Git
```

The exact `.gitignore` rule `/challenges/04_automation/day_2/images/` keeps this folder and its contents local. They are not included when someone clones the repository, so create the folder and add your own images before trying the project.

The tutorial version accepts a folder path and falls back to `os.getcwd()` for blank input. That value follows the terminal's current directory and can point to the repository root. The working version targets only the local `images` folder, with project-file protection and checks for existing destination names.

## Current challenge coverage

Extension filtering, alphabetical ordering, numbered names, a preview, confirmation, and renaming are implemented. The optional undo feature is not implemented; original names are not saved in a separate file.

If no eligible files match, the script prints `NO files found in dir`. Check that the images are inside `day_2/images` and that the extension matches their actual type: `.jpg` will not match `.png`. Include the dot so the new names retain a valid extension; the script does not insert it automatically.

For a first trial, use copies of a few sample files in `images`.
