# Day 3: Personal Movie Tracker with JSON

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to maintain a personal movie collection through a terminal menu. Each movie is a dictionary with `title`, `genre`, and `rating` fields, and the collection is a list of these dictionaries.

Read the unchanged [original task](DAY_3.md) alongside [day_3.py](day_3.py). Project explanations and updates belong in this README; the original task text is maintained separately.

## Files

| File | Purpose |
| --- | --- |
| [DAY_3.md](DAY_3.md) | The original Personal Movie Tracker with JSON challenge and its bonus tasks. |
| [day_3.py](day_3.py) | Adding, viewing, and searching movies with ratings stored in a JSON file. |
| `movies.json` | Movie data created after the first successful addition and reused beside `day_3.py`. |

## Menu and functions

`run_movie_db()` loads the collection once, then repeats a menu using `while True` and `match`:

| Option | Function | Behaviour |
| --- | --- | --- |
| `1` | `add_movies(movies)` | Collect a title, genre, and rating; validate the entry and save the updated list. |
| `2` | `view_movies(movies)` | Display the collection between separator lines, or `NO movies in DB` if empty. |
| `3` | `search_movies(movies)` | Find partial matches in either the title or genre and display the result count and matching movies. |
| `4` | Exit | Leave the loop with `break`. |

Other choices print `Enter valid choice`. The `if __name__ == "__main__":` block starts the menu when the script is run directly.

## Adding and searching movies

- Titles and genres are trimmed with `.strip()` and stored in lowercase with `.lower()`.
- `any(...)` checks for an existing title without case sensitivity. A duplicate prints `Movie already exists` and returns before asking for the other fields.
- `float(...)` accepts decimal ratings. The check `0 <= rating <= 10` includes both endpoints; an invalid number or an out-of-range value prints `Please enter valid number` and returns to the menu without adding the movie.
- Valid entries are appended to the list, saved, and confirmed with `Movie added ✅`.
- A list comprehension selects movies where the lowercase search term is contained in the title **or** genre. No matches print `No matching result`.

The current script does not reject blank titles, genres, or search terms. An empty search term matches every movie because `"" in some_string` is true.

## JSON storage and file location

`FILENAME = Path(__file__).resolve().parent / "movies.json"` keeps all movie data in `challenges/02_data_handling/day_3`, beside `day_3.py`, regardless of the terminal's working directory.

`load_movies()` returns an empty list if the file is missing. Otherwise, `json.load(f)` reads the saved JSON into Python objects. `save_movies(movies)` writes the current list with `json.dump(movies, f, indent=2)`, using UTF-8 and two-space indentation. Write mode replaces the saved collection after each successful addition; loading the old collection first keeps previous movies in that list.

The file is created after the first successful movie addition. Starting the menu, viewing an empty collection, or exiting alone does not create it. An existing file is expected to contain a valid JSON list of movie records; malformed JSON is not handled by the current loader.

## Example

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

## How to run

From the repository root:

```powershell
python "challenges/02_data_handling/day_3/day_3.py"
```

Or, from this lesson's folder:

```powershell
python .\day_3.py
```

In VS Code, open `day_3.py` and press **Ctrl + S**. For input prompts, click inside the Run on Save terminal, type your answer, and press **Enter**. Exit an older running instance before starting the moved script.

This lesson uses only Python's standard library or built-in features; no package installation is required.

Input and output paths resolve from this Python file, so data stays in this lesson folder regardless of the terminal's working directory.

## Useful links for beginners

- [JSON encoding and decoding](https://docs.python.org/3/library/json.html): reading and writing JSON records with `load()` and `dump()`.
- [Lists and dictionaries](https://docs.python.org/3/tutorial/datastructures.html): the row lists and named fields returned by CSV readers.
- [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files): file modes, encoding, and closing files with `with`.
- [Paths with pathlib](https://docs.python.org/3/library/pathlib.html): `Path(__file__).resolve().parent` for keeping input and output beside the script.
- [Checking files with os.path](https://docs.python.org/3/library/os.path.html): `os.path.exists()` before reading a local file.

[Previous: Day 2](../day_2/README.md) · [Next: Day 4](../day_4/README.md)
