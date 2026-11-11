# Challenges — Days 12–21

This is the second challenge group. Work through it after [day 1–11](../day%20%5B1-11%5D/README.md), then continue with the later groups in the [challenge index](../README.md#challenge-groups).

**Status: in progress.** Local days 1–3, CLI Contact Book (CSV-Powered), Student Marks Analyzer, and Personal Movie Tracker with JSON, are implemented and documented.

Navigate through the [challenge index](../README.md) or return to the [main project overview](../../README.md#folder-overview).

## Learning order and file numbering

1. Read the [original Day 1 challenge](DAY_1.md), then explore [day_1.py](day_1.py).
2. Read the [original Day 2 challenge](DAY_2.md), then explore [day_2.py](day_2.py).
3. Read the [original Day 3 challenge](DAY_3.md), then explore [day_3.py](day_3.py).
4. Continue with later local projects in numerical order as they are added.
5. After this group, continue with `day [22-31]` and the remaining challenge groups before returning to the next numbered course section (`12_...`).

The tutorial restarts project numbering in this folder: `DAY_1.md` and `day_1.py` belong to `day [12-21]` and are separate from the files with those names in `day [1-11]`. Keep the original filenames; this README uses the local day numbers rather than renaming the first project to Day 12.

The `DAY_*.md` files contain original task descriptions maintained manually by the repository owner. Preserve their wording. Keep explanations, examples, and progress in README files.

## Files covered so far

| File | Purpose |
| --- | --- |
| [DAY_1.md](DAY_1.md) | The original CLI Contact Book (CSV-Powered) challenge and its bonus tasks. |
| [day_1.py](day_1.py) | Adding, viewing, and searching contacts stored in a CSV file. |
| `contacts.csv` | Runtime data with `Name`, `Phone`, and `Email` columns, created and reused beside `day_1.py` in this folder. |
| [DAY_2.md](DAY_2.md) | The original Student Marks Analyzer challenge and its bonus tasks. |
| [day_2.py](day_2.py) | Collecting student marks and reporting the average, highest and lowest results, and student count. |
| [DAY_3.md](DAY_3.md) | The original Personal Movie Tracker with JSON challenge and its bonus tasks. |
| [day_3.py](day_3.py) | Adding, viewing, and searching movies with ratings stored in a JSON file. |
| `movies.json` | Movie data created after the first successful addition and reused beside `day_3.py`. |

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

## Day 2: Student Marks Analyzer

The task is to collect student names and marks, then display summary statistics and a detailed report. Marks are numeric scores; the program does not convert them to letter grades or a `1–5` grading scale.

### Collecting student data

`collect_student_data()` builds a dictionary whose keys are student names and whose values are their marks:

1. A `while True` loop asks for a name and removes surrounding whitespace with `.strip()`.
2. Entering `done` ends data collection with `break`. The command is case-insensitive, so `DONE` works too.
3. `if name in students` rejects a duplicate name and uses `continue` to ask for another. This comparison is case-sensitive: `Ana` and `ana` are different dictionary keys.
4. `float(input(...))` converts the mark to a number and stores it with `students[name] = marks`. Decimal marks are accepted, although the original task describes integer scores.
5. Invalid numeric text triggers `ValueError` and prints `Please enter a valid number for marks`. That record is not saved, and the loop returns to the name prompt.
6. The function returns the dictionary after data entry is finished.

The current script does not reject empty names or restrict marks to a particular range.

### Calculating and displaying the report

`display_report(students)` first checks for an empty dictionary. If there are no students, it prints `No student data ❌` and returns before attempting calculations.

For a nonempty dictionary:

- `list(students.values())` collects all marks.
- `max()` and `min()` find the highest and lowest marks.
- `sum(marks) / len(marks)` calculates the arithmetic mean; `{average:.2f}` displays it with two decimal places.
- List comprehensions over `students.items()` collect every name tied for the highest or lowest result. `', '.join(...)` formats those names for display.
- `len(students)` gives the student count, and a final loop prints each student's mark in input order.

The two calls at the bottom of the file collect all data first, then display the report. Results stay in memory for that run; this project does not create a data file.

### Example

Enter the following names and marks, then enter `done` at the next name prompt:

| Student | Mark |
| --- | --- |
| Ana | 80 |
| Marko | 90 |
| Sara | 90 |

The resulting report is:

```text

 Students marks report 🗓️
------------------------------
Total students: 3
average marks for students: 86.67
Highest marks : 90.0 by Marko, Sara
lowest marks : 80.0 by Ana
------------------------------
Detailed Marks 🗓️
 - Ana: 80.0
 - Marko: 90.0
 - Sara: 90.0
```

Both top-scoring students appear in the report. The same logic includes all students tied for the lowest mark. Collecting data before reporting, the report-style layout, and duplicate-name prevention implement the bonus tasks; duplicate checking uses the case-sensitive rule described above.

## Day 3: Personal Movie Tracker with JSON

The task is to maintain a personal movie collection through a terminal menu. Each movie is a dictionary with `title`, `genre`, and `rating` fields, and the collection is a list of these dictionaries.

### Menu and functions

`run_movie_db()` loads the collection once, then repeats a menu using `while True` and `match`:

| Option | Function | Behaviour |
| --- | --- | --- |
| `1` | `add_movies(movies)` | Collect a title, genre, and rating; validate the entry and save the updated list. |
| `2` | `view_movies(movies)` | Display the collection between separator lines, or `NO movies in DB` if empty. |
| `3` | `search_movies(movies)` | Find partial matches in either the title or genre and display the result count and matching movies. |
| `4` | Exit | Leave the loop with `break`. |

Other choices print `Enter valid choice`. The `if __name__ == "__main__":` block starts the menu when the script is run directly.

### Adding and searching movies

- Titles and genres are trimmed with `.strip()` and stored in lowercase with `.lower()`.
- `any(...)` checks for an existing title without case sensitivity. A duplicate prints `Movie already exists` and returns before asking for the other fields.
- `float(...)` accepts decimal ratings. The check `0 <= rating <= 10` includes both endpoints; an invalid number or an out-of-range value prints `Please enter valid number` and returns to the menu without adding the movie.
- Valid entries are appended to the list, saved, and confirmed with `Movie added ✅`.
- A list comprehension selects movies where the lowercase search term is contained in the title **or** genre. No matches print `No matching result`.

The current script does not reject blank titles, genres, or search terms. An empty search term matches every movie because `"" in some_string` is true.

### JSON storage and file location

`FILENAME = Path(__file__).resolve().parent / "movies.json"` keeps all movie data in `challenges/day [12-21]`, beside `day_3.py`, regardless of the terminal's working directory.

`load_movies()` returns an empty list if the file is missing. Otherwise, `json.load(f)` reads the saved JSON into Python objects. `save_movies(movies)` writes the current list with `json.dump(movies, f, indent=2)`, using UTF-8 and two-space indentation. Write mode replaces the saved collection after each successful addition; loading the old collection first keeps previous movies in that list.

The file is created after the first successful movie addition. Starting the menu, viewing an empty collection, or exiting alone does not create it. An existing file is expected to contain a valid JSON list of movie records; malformed JSON is not handled by the current loader.

### Example

Choose **Add Movie** and enter:

| Field | Value |
| --- | --- |
| Title | Inception |
| Genre | Sci-Fi |
| Rating | 8.8 |

The saved JSON is:

```json
[
  {
    "title": "inception",
    "genre": "sci-fi",
    "rating": 8.8
  }
]
```

Choosing **View All Movies** displays:

```text
------------------------------
inception -- sci-fi -- 8.8
------------------------------
```

Searching for `SCI` matches the genre and displays:

```text
 Found 1 result(s)
inception -- sci-fi -- 8.8
```

Searching for part of the title, such as `cept`, finds the same movie. Restarting the script reloads the collection from `movies.json`.

Duplicate prevention and JSON reading/writing implement those bonus tasks. The current display uses separators between values and around the list, rather than an aligned table with column headings.

## How to run these projects

From the repository root, choose the command for the project you want to run:

```powershell
python "challenges/day [12-21]/day_1.py"
python "challenges/day [12-21]/day_2.py"
python "challenges/day [12-21]/day_3.py"
```

**File location:** `contacts.csv` is created and reused in `challenges/day [12-21]`, beside `day_1.py`, even when the script is launched from the repository root. An existing CSV at another location is not moved automatically.

Day 3 also keeps `movies.json` beside its script, creating it after the first successful addition. Day 2 displays its report in the terminal without saving a file. All three projects use only Python's standard library or built-in features.

In VS Code, open the Python file for the local day you want to run and press **Ctrl + S** to format and run it. Click inside the Run on Save terminal, type your menu choice or requested details, and press **Enter**. The save command uses the terminal's `python -u`; the CSV and JSON files remain beside their respective scripts.

See the [main README](../../README.md#quick-start) for editor setup.

## Useful links for beginners

- [Python CSV reading and writing](https://docs.python.org/3/library/csv.html): examples of `reader`, `writer`, and `DictReader` used in this project.
- [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files): file modes, encoding, and closing files with `with`.
- [Lists and dictionaries](https://docs.python.org/3/tutorial/datastructures.html): the row lists and named fields returned by CSV readers.
