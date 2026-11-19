# Challenges — Automation

This group corresponds to `04_automation` in the Udemy tutorial and follows [03_web_scraping](../03_web_scraping/README.md).

**Status: in progress — current course section.** Days 1–3 cover file organization, batch renaming, and automatic Downloads monitoring with Watchdog.

[Challenge index](../README.md) · [Main project overview](../../README.md#folder-overview)

## Learning order and folder layout

Each project has its own folder, starting with `day_1`. Use names such as `day_1/day_1.py` without leading zeros. Each lesson contains its Python script, original `DAY_*.md` task statement, and README with explanations and running instructions.

| Lesson guide | Project | Main concepts |
| --- | --- | --- |
| [day_1](day_1/README.md) | File Organizer | File extensions, `os`, `shutil`, folder creation, and moving files within the lesson folder. |
| [day_2](day_2/README.md) | Batch Rename Files in a Folder | Extension filtering, alphabetical sorting, numbered names with `enumerate()`, a preview, confirmation, and `os.rename()`. |
| [day_3](day_3/README.md) | Auto File Organizer with Watchdog | Filesystem events, observers, download readiness checks, retries, and automatic sorting in Downloads. |

Keep the original `DAY_*.md` task statements unchanged. Record implementation notes and progress in README files.

## Setup and running

Days 1–2 use Python's standard library; no additional packages are required. From the repository root, run the command for the lesson you want:

```powershell
python "challenges/04_automation/day_1/day_1.py"
python "challenges/04_automation/day_2/day_2.py"
```

Day 3 additionally requires Watchdog:

```powershell
python -m pip install watchdog
python "challenges/04_automation/day_3/day_3.py"
```

Or open the script in VS Code and press **Ctrl + S** with the existing Run on Save setup.

The organizer moves sample files directly beside its script into `PDFs`, `Images`, `TextFiles`, and `Others`. Its script, task statement, README, and existing folders stay in place. It uses `day_1` regardless of the terminal's current directory. See the [Day 1 guide](day_1/README.md) for details and the preserved original tutorial code.

The batch renamer changes filenames only in `day_2/images`, regardless of the terminal's current directory. Create that folder and add practice images before running; it is ignored by Git and is not included in a clone. Enter a base name and the matching extension including the dot (for example, `house` and `.jpg`), review the numbered names, and enter `y` to apply them. Images stay in the same folder. The script skips nested folders and stops if a destination belongs to another existing file. See the [Day 2 guide](day_2/README.md) for an example and the current limitations, including the optional undo feature that is not implemented.

Day 3 monitors the user's Downloads folder while the process is running. New JPG/PNG images go to `Images`, PDFs to `PDFs`, and other completed files to `Others`. It ignores temporary download extensions, handles creation and rename events, and waits for stable files before moving them. Existing destination names receive numbered suffixes. It does not scan existing files at startup or watch nested folders. Stop the previous instance with **Ctrl + C** before running again. The [Day 3 guide](day_3/README.md) preserves the original tutorial code and explains the Chrome download fix, timing limits, and error messages. ZIP-to-Archives sorting remains unimplemented.

## Useful links and package source

- [Watchdog documentation](https://python-watchdog.readthedocs.io/en/stable/): the library used in Day 3.
- [Watchdog quickstart](https://python-watchdog.readthedocs.io/en/stable/quickstart.html): basic observers, handlers, and folder monitoring.
- [Watchdog on PyPI](https://pypi.org/project/watchdog/): package installation information.
- [Watchdog — GitHub](https://github.com/gorakhargosh/watchdog): the official source repository, available to star.

Days 1–2 use standard-library modules such as `os` and `shutil`; Day 3 adds the external `watchdog` package and uses `os` and `time`. See the [project-wide package index](../../README.md#package-source-repositories) for the other course packages.
