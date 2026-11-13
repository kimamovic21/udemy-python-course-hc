# Day 10: Offline Notes Locker

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to add, list, read, and search local notes while encrypting their content with `cryptography.fernet.Fernet`. This differs from Day 9's reversible Base64 encoding: Fernet uses a secret key for encryption and decryption. Only note content is encrypted; titles and timestamps remain readable in the JSON.

Read the unchanged [original task](DAY_10.md) alongside [day_10.py](day_10.py). Project explanations and updates belong in this README; the original task text is maintained separately.

## Files

| File | Purpose |
| --- | --- |
| [DAY_10.md](DAY_10.md) | The original Offline Notes Locker challenge and optional tasks. |
| [day_10.py](day_10.py) | Adding, listing, viewing, and searching notes with Fernet-encrypted content. |
| `notes_vault.json` | Local note records containing readable titles/timestamps and encrypted content. |
| `vault.key` | The local Fernet key generated once and reused, excluded from Git. |

## Day 10 setup and local files

Install the external package using the Python interpreter that runs the script:

```powershell
python -m pip install cryptography
```

The import is `from cryptography.fernet import Fernet`. The `json`, `os`, `datetime`, and `pathlib` modules come with Python and need no separate installation. See the [official installation guide](https://cryptography.io/en/latest/installation/) and [Fernet documentation](https://cryptography.io/en/latest/fernet/).

Both file paths use `Path(__file__).resolve().parent`, so they stay beside `day_10.py` in `challenges/02_data_handling/day_10`, even when the script starts from the repository root:

| File | Created when | Role |
| --- | --- | --- |
| `vault.key` | At startup, if no key file exists. | Stores the secret key used to encrypt and decrypt note content. |
| `notes_vault.json` | After the first successful note addition. | Stores a JSON list of note titles, encrypted content, and timestamps. |

`load_or_create_key()` generates a key with `Fernet.generate_key()` and writes it in binary mode (`"wb"`), or reads the existing bytes with `"rb"`. It returns `Fernet(key)`. The module-level call `fernet = load_or_create_key()` runs before the menu and also runs if the module is imported.

Keep the same key with the corresponding notes: replacing or deleting it prevents decryption of their existing content. Anyone with the key and note file can read that content. The root [.gitignore](../../../.gitignore) excludes `vault.key`; documentation examples do not contain an actual key. Only this lesson's `notes_vault.json` is also excluded through its exact path in the root `.gitignore`; files with the same name in other folders are unaffected by that rule.

## Menu and functions

`main()` repeats the menu with `while True`, selects actions with `match`, and exits with option `5`:

| Option | Function | Behaviour |
| --- | --- | --- |
| `1` | `add_note()` | Read a title and content, encrypt the content, add a local timestamp, and save the note. |
| `2` | `list_notes()` | Show numbered titles and timestamps, or `No notes yet` for an empty vault. |
| `3` | `view_note()` | Ask for a displayed note number, decrypt that note's content, and print it. |
| `4` | `search_notes()` | Find case-insensitive partial matches in note titles and display matching titles/timestamps. |
| `5` | Exit | Leave the loop with `break`. |

`load_vault()` returns an empty list when the JSON file does not exist. `save_vault(data)` writes the complete list using UTF-8 and `json.dump(..., indent=2)`. Each successful save replaces the file, retaining previous notes because they are loaded into the list before appending the new one.

Within `add_note()`, `.strip()` trims the title and content. `content.encode()` produces bytes, `fernet.encrypt(...)` encrypts them, and `.decode()` turns the token into text that can be stored in JSON. `datetime.now().strftime("%Y-%m-%d %H:%M:%S")` records the computer's local time.

`view_note()` reverses the process with `fernet.decrypt(encrypted.encode()).decode()`. It subtracts `1` from the displayed note number because Python list indexes start at zero. Search uses a list comprehension over the title; it does not decrypt or search note bodies.

## Practice example

Choose **Add Note**, enter title `Python practice` and content `Today I learned about Fernet.`. The program confirms `✅ data saved`.

The saved record has this structure. Both the token and timestamp below are placeholders; the generated token changes each time:

```json
[
  {
    "title": "Python practice",
    "content": "<encrypted Fernet token>",
    "timestamp": "YYYY-MM-DD HH:MM:SS"
  }
]
```

Listing notes shows the title and timestamp. Selecting that note with **View Note** decrypts its content back to `Today I learned about Fernet.`. Searching for `PYTHON` finds the title without case sensitivity.

## Current challenge coverage

Adding notes, content encryption/decryption, listing, title search, and timestamps are implemented. The current file is named `notes_vault.json`, rather than the `.vault` filename suggested by the original challenge. The optional master password is not implemented; the program directly loads the local key file.

Empty titles and content are accepted, and an empty search matches all titles. The current view-selection check uses `index <= len(data)` instead of a strict upper bound, so a selection one beyond the last note reaches an `IndexError` and is reported as `Invalid input` by the bare handler. The view action also asks for a number after an empty list. Other file/JSON errors are not handled consistently yet.

## Reference mentioned in the tutorial

[William Stallings](https://williamstallings.com/) is the website mentioned by the instructor during this lesson. It is included as an optional course reference; the practical package instructions for this project are in the Fernet links above.

## How to run

From the repository root:

```powershell
python "challenges/02_data_handling/day_10/day_10.py"
```

Or, from this lesson's folder:

```powershell
python .\day_10.py
```

In VS Code, open `day_10.py` and press **Ctrl + S**. For input prompts, click inside the Run on Save terminal, type your answer, and press **Enter**. Exit an older running instance before starting the moved script.

Complete the [setup instructions](#day-10-setup-and-local-files) above before running this project.

Input and output paths resolve from this Python file, so data stays in this lesson folder regardless of the terminal's working directory.

## Useful links for beginners

- [Cryptography installation](https://cryptography.io/en/latest/installation/): installing the package used by Day 10.
- [Fernet encryption](https://cryptography.io/en/latest/fernet/): generating a key, encrypting bytes, and decrypting tokens.
- [JSON encoding and decoding](https://docs.python.org/3/library/json.html): reading and writing JSON records with `load()` and `dump()`.
- [Date and time format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes): formatting note timestamps with `datetime.now().strftime("%Y-%m-%d %H:%M:%S")`.
- [Paths with pathlib](https://docs.python.org/3/library/pathlib.html): `Path(__file__).resolve().parent` for keeping input and output beside the script.
- [William Stallings](https://williamstallings.com/): optional website reference mentioned by the instructor in the Notes Locker lesson.

[Previous: Day 9](../day_9/README.md)
