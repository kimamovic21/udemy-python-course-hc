# Day 9: Offline Credential Manager

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

This exercise stores website, username, and password records in a local text file, using Base64 to encode each record. **Base64 is reversible encoding, not encryption.** The current input and viewer show passwords as plain text, so the example below uses fictional practice credentials.

Read the unchanged [original task](DAY_9.md) alongside [day_9.py](day_9.py). Project explanations and updates belong in this README; the original task text is maintained separately.

## Files

| File | Purpose |
| --- | --- |
| [DAY_9.md](DAY_9.md) | The original Offline Credential Manager challenge, assignment, and bonus tasks. |
| [day_9.py](day_9.py) | Adding and viewing Base64-encoded practice credentials with a simple strength-scoring helper. |
| `vault.txt` | Runtime data created beside `day_9.py` when the first credential is added. |

## Menu and current actions

`main()` repeats a menu with `while True` and dispatches the choice with `match`:

| Option | Current behaviour |
| --- | --- |
| `1` | Call `add_credential()` to collect and save a record. |
| `2` | Call `view_credentials()` to decode and display saved records. |
| `3` | Listed as **Update password**, but not implemented; currently prints `Invalid choice`. |
| `4` | Exit the menu using `break`. |

Other choices also print `Invalid choice`. The final `if __name__ == "__main__":` block starts the menu when the script is run directly.

## Encoding, file storage, and decoding

1. `add_credential()` reads the website, username, and password with `input()`. `.strip()` removes surrounding whitespace from all three inputs.
2. It calls `password_strength(password)` and assigns the result to `strength`. That value is currently neither printed nor saved.
3. An f-string joins the fields as `website||username||password`.
4. `encode(text)` turns that string into bytes with `.encode()`, applies `base64.b64encode()`, then uses `.decode()` to return the encoded content as text.
5. UTF-8 append mode (`"a"`) writes one encoded record per line, retaining earlier records. The function prints `✅ Credential saved`.
6. `view_credentials()` reads the lines, reverses Base64 with `decode(text)`, and splits each decoded record on `||` to recover the three fields.

`VAULT_FILE = Path(__file__).resolve().parent / "vault.txt"` keeps both reading and writing in `challenges/02_data_handling/day_9`, beside `day_9.py`, even when the terminal is at the repository root. The first successful addition creates the file. Viewing records before it exists prints `File not found` and returns to the menu.

Only this lesson's `vault.txt` is excluded from Git through its exact path in the root [.gitignore](../../../.gitignore). Files with the same name in other folders are unaffected by that rule.

## Password-strength helper

The helper adds one point for each of four conditions: at least eight characters, an uppercase letter, a digit, and a character from `!@#$%^&*().,<>`. `sum()` counts these Boolean checks, and `min(score, 3)` limits the list index:

| Checks passed | Returned label |
| --- | --- |
| 0 | `Weak` |
| 1 | `Medium` |
| 2 | `Strong` |
| 3 or 4 | `Very Strong` |

There is no lowercase-letter check. These labels describe the exercise's scoring rule; the returned label is not yet shown to the user.

## Practice example

Choose **Add credential** and enter:

| Field | Example |
| --- | --- |
| Website | `example.com` |
| Username | `demo_user` |
| Password | `Example123!` |

After `✅ Credential saved`, choose **View credentials**. The current code displays:

```text
example.com | demo_user | Example123!
```

Although `hidden_password = "*" * len(password)` builds a masked version, the following `print()` uses `password` instead. The masked value is currently unused.

## Day 9 current challenge coverage

Adding records, Base64 encoding/decoding, append-mode persistence, listing records, and the strength helper are implemented. Displaying the strength result, updating a website's password, searching entries, and masking the displayed password remain unfinished.

The script does not check duplicate websites or empty inputs. It assumes every saved line decodes into exactly three fields; malformed lines or field values containing `||` can fail during decoding or splitting. It uses only Python's standard-library `base64`, `os`, and `pathlib` modules and needs no additional packages or API keys.

## How to run

From the repository root:

```powershell
python "challenges/02_data_handling/day_9/day_9.py"
```

Or, from this lesson's folder:

```powershell
python .\day_9.py
```

In VS Code, open `day_9.py` and press **Ctrl + S**. For input prompts, click inside the Run on Save terminal, type your answer, and press **Enter**. Exit an older running instance before starting the moved script.

This lesson uses only Python's standard library or built-in features; no package installation is required.

Input and output paths resolve from this Python file, so data stays in this lesson folder regardless of the terminal's working directory.

## Useful links for beginners

- [Base64 encoding and decoding](https://docs.python.org/3/library/base64.html): `b64encode()` and `b64decode()` used by Day 9's credential exercise.
- [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files): file modes, encoding, and closing files with `with`.
- [Paths with pathlib](https://docs.python.org/3/library/pathlib.html): `Path(__file__).resolve().parent` for keeping input and output beside the script.

[Previous: Day 8](../day_8/README.md) · [Next: Day 10](../day_10/README.md)
