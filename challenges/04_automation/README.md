# Challenges — Automation

This group corresponds to `04_automation` in the Udemy tutorial and follows [03_web_scraping](../03_web_scraping/README.md).

**Status: in progress — current course section.** Days 1–2 cover organizing local files by extension and batch renaming with a preview and confirmation.

[Challenge index](../README.md) · [Main project overview](../../README.md#folder-overview)

## Learning order and folder layout

Each project has its own folder, starting with `day_1`. Use names such as `day_1/day_1.py` without leading zeros. Each lesson contains its Python script, original `DAY_*.md` task statement, and README with explanations and running instructions.

| Lesson guide | Project | Main concepts |
| --- | --- | --- |
| [day_1](day_1/README.md) | File Organizer | File extensions, `os`, `shutil`, folder creation, and moving files within the lesson folder. |
| [day_2](day_2/README.md) | Batch Rename Files in a Folder | Extension filtering, alphabetical sorting, numbered names with `enumerate()`, a preview, confirmation, and `os.rename()`. |

Keep the original `DAY_*.md` task statements unchanged. Record implementation notes and progress in README files.

## Setup and running

Days 1–2 use Python's standard library; no additional packages are required. From the repository root, run the command for the lesson you want:

```powershell
python "challenges/04_automation/day_1/day_1.py"
python "challenges/04_automation/day_2/day_2.py"
```

Or open the script in VS Code and press **Ctrl + S** with the existing Run on Save setup.

The organizer moves sample files directly beside its script into `PDFs`, `Images`, `TextFiles`, and `Others`. Its script, task statement, README, and existing folders stay in place. It uses `day_1` regardless of the terminal's current directory. See the [Day 1 guide](day_1/README.md) for details and the preserved original tutorial code.

The batch renamer changes filenames only in `day_2/images`, regardless of the terminal's current directory. Create that folder and add practice images before running; it is ignored by Git and is not included in a clone. Enter a base name and the matching extension including the dot (for example, `house` and `.jpg`), review the numbered names, and enter `y` to apply them. Images stay in the same folder. The script skips nested folders and stops if a destination belongs to another existing file. See the [Day 2 guide](day_2/README.md) for an example and the current limitations, including the optional undo feature that is not implemented.
