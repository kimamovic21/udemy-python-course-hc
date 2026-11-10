# Challenges — Days 12–21

This is the second challenge group. Work through it after [day 1–11](../day%20%5B1-11%5D/README.md), then continue with the later groups in the [challenge index](../README.md#challenge-groups).

**Status: in progress.** The first local project, CLI Contact Book (CSV-Powered), is implemented and documented.

Navigate through the [challenge index](../README.md) or return to the [main project overview](../../README.md#folder-overview).

## Learning order and file numbering

1. Read the [original Day 1 challenge](DAY_1.md), then explore [day_1.py](day_1.py).
2. Continue with later local projects in numerical order as they are added.
3. After this group, continue with `day [22-31]` and the remaining challenge groups before returning to the next numbered course section (`12_...`).

The tutorial restarts project numbering in this folder: `DAY_1.md` and `day_1.py` belong to `day [12-21]` and are separate from the files with those names in `day [1-11]`. Keep the original filenames; this README uses the local day numbers rather than renaming the first project to Day 12.

The `DAY_*.md` files contain original task descriptions maintained manually by the repository owner. Preserve their wording. Keep explanations, examples, and progress in README files.

## Files covered so far

| File | Purpose |
| --- | --- |
| [DAY_1.md](DAY_1.md) | The original CLI Contact Book (CSV-Powered) challenge and its bonus tasks. |
| [day_1.py](day_1.py) | Adding, viewing, and searching contacts stored in a CSV file. |
| `contacts.csv` | Runtime data with `Name`, `Phone`, and `Email` columns, created and reused beside `day_1.py` in this folder. |

## Day 1: CLI Contact Book (CSV-Powered)

The task is to build a terminal contact book whose data remains available between runs. The script uses Python's standard-library `csv` and `os` modules; no additional packages are needed.

### Menu and functions

`main()` repeats a menu in a `while True` loop and selects an action using `if` and `elif`:

| Option | Function | Behaviour |
| --- | --- | --- |
| `1` | `add_contact()` | Ask for a name, phone, and email; reject an existing name; append a new CSV row. |
| `2` | `view_contacts()` | Read the CSV rows, skip the header, and display each contact as `Name | Phone | Email`. |
| `3` | `search_contact()` | Find names containing the search text and print each matching name and phone number. |
| `4` | Exit | Print a goodbye message and leave the loop with `break`. |

An unrecognized menu option displays `Invalid choice of number`. The `if __name__ == "__main__":` block calls `main()` when the script is run directly.

### CSV storage

1. `FILENAME = Path(__file__).resolve().parent / "contacts.csv"` builds the path from the script's own folder. At startup, `os.path.exists()` checks whether it exists; a missing file is created with the header `Name,Phone,Email`. All reads and writes use this same path.
2. `csv.writer(...).writerow(...)` writes the header or a contact row. New contacts use append mode (`"a"`) to keep existing records.
3. `csv.DictReader` reads rows as dictionaries, letting the code access fields such as `row["Name"]`.
4. Before adding a contact, the script compares lowercase names to prevent case-insensitive duplicates. Search also converts names and the search term to lowercase, then uses `in` for partial matching.
5. `view_contacts()` uses `csv.reader` and collects nonempty rows with `[row for row in reader if row]`. This skips blank lines already present in a CSV. `rows[1:]` skips the header; each remaining row is printed with vertical-bar separators.

The script trims surrounding whitespace from user input, and phone numbers remain text. The current code does not validate phone or email formats or reject empty contact fields. An empty or header-only CSV displays `No contacts found`. All CSV reads and writes use `newline=""` so the CSV module handles line endings and avoids adding extra blank lines on Windows.

### CSV line endings and the Windows fix

Choosing **View All Contacts** originally displayed a saved contact and then raised `IndexError: list index out of range`. The CSV contained a blank line, which `csv.reader` returned as an empty list (`[]`). Accessing `row[0]`, `row[1]`, or `row[2]` on that row caused the crash.

On Windows, writing CSV data without `newline=""` can add an extra carriage return and produce blank lines. Passing `newline=""` lets the CSV module handle line endings, as described in the [official CSV documentation](https://docs.python.org/3/library/csv.html). These extra lines typically do not arise from the same code on macOS, but the original display loop would still fail there if the CSV already contained a blank line.

The changes address both writing new records and reading existing files:

| Original code | Active correction | Purpose |
| --- | --- | --- |
| `open(FILENAME, "r", encoding="utf-8")` | `open(FILENAME, "r", newline="", encoding="utf-8")` | Let the CSV module handle line endings while reading. |
| `open(FILENAME, "a", encoding="utf-8")` | `open(FILENAME, "a", newline="", encoding="utf-8")` | Prevent extra blank lines when appending contacts on Windows. |
| `rows = list(reader)` | `rows = [row for row in reader if row]` | Skip existing empty rows before displaying contacts. |
| `if len(rows) < 1:` | `if len(rows) <= 1:` | Treat an empty file or a header-only file as having no contacts. |

The original versions remain commented out directly above the active corrections in `day_1.py` for learning and comparison. The header-creation block already used `newline=""`. Existing contact data does not need to be deleted or rewritten: blank rows are skipped in memory, and the file is preserved.

### Example

Choose **Add Contact** and enter these practice details:

| Field | Value |
| --- | --- |
| Name | Alex |
| Phone | 0123456789 |
| Email | alex@example.com |

The script confirms `Contact added`. The CSV data is:

```csv
Name,Phone,Email
Alex,0123456789,alex@example.com
```

Choosing **View All Contacts** displays this contact row:

```text
Alex | 0123456789 | alex@example.com
```

Searching for `LEX` matches the same contact and displays:

```text
Alex | 📞 0123456789
```

Trying to add `alex` again prints `Contact name already exists`. A search with no matches prints `No matching contact found`. The table-like display, partial search, and duplicate-name checks implement the bonus tasks.

## How to run this project

From the repository root:

```powershell
python "challenges/day [12-21]/day_1.py"
```

**File location:** `contacts.csv` is created and reused in `challenges/day [12-21]`, beside `day_1.py`, even when the script is launched from the repository root. An existing CSV at another location is not moved automatically.

In VS Code, open this group's `day_1.py` and press **Ctrl + S** to format and run it. Click inside the Run on Save terminal, type your menu choice or contact detail, and press **Enter**. The save command uses the terminal's `python -u`; the CSV location remains beside the script.

See the [main README](../../README.md#quick-start) for editor setup.

## Useful links for beginners

- [Python CSV reading and writing](https://docs.python.org/3/library/csv.html): examples of `reader`, `writer`, and `DictReader` used in this project.
- [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files): file modes, encoding, and closing files with `with`.
- [Lists and dictionaries](https://docs.python.org/3/tutorial/datastructures.html): the row lists and named fields returned by CSV readers.
