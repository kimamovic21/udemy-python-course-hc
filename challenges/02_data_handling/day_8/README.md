# Day 8: JSON Flattener

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to turn nested JSON into one dictionary whose keys describe the original paths. The provided input comes from `DAY_8.md`: a user with a nested address, a list of roles, and an activity flag.

Read the unchanged [original task](DAY_8.md) alongside [day_8.py](day_8.py). Project explanations and updates belong in this README; the original task text is maintained separately.

## Files

| File | Purpose |
| --- | --- |
| [DAY_8.md](DAY_8.md) | The original JSON Flattener challenge with nested input and expected flattened output. |
| [day_8.py](day_8.py) | Recursively flattening dictionaries and lists into one dictionary of path-like keys. |
| [nested_data.json](nested_data.json) | The original example data copied into a runnable JSON input file. |
| [flattened_data.json](flattened_data.json) | The flattened JSON output generated using the selected separator. |

## Files, separator, and execution

`nested_data.json` is the input and `flattened_data.json` is the output. Both paths use `Path(__file__).resolve().parent`, keeping the files beside `day_8.py` in `challenges/02_data_handling/day_8` when running from the root or saving with **Ctrl + S**.

`main()` checks that the input exists, loads it with `json.load()`, and asks for a separator. `.strip() or "."` makes an empty answer, including whitespace, default to a dot. Enter `-` to build keys such as `user-address-city` instead of `user.address.city`.

After flattening, `json.dump(..., indent=2)` writes the result with two-space indentation and UTF-8 encoding. Each successful run replaces the output file; the input stays unchanged. The terminal reports the output's absolute path.

## How the recursive function works

`flatten_json(data, parent_key="", sep=".")` returns a dictionary called `items`. It handles three cases:

1. **Dictionary:** loop through `data.items()`. Build `full_key` by joining the parent path and current key with the separator. At the top level, use the current key alone, without a leading separator. Call `flatten_json()` again for the value, then merge its returned dictionary using `items.update(...)`.
2. **List:** use `enumerate(data)` to obtain each item and its zero-based index. Add that index to the path and recursively process the item. For example, the first role becomes `roles.0`.
3. **Other value:** the value is a leaf, such as a string, number, Boolean, or `null`. Store it directly with `items[parent_key] = data` and return the dictionary.

Calling the same function on smaller parts of the structure is **recursion**. For example, it follows `user` → `address` → `city` until it reaches the string `Delhi`, then stores that value under `user.address.city`.

## Example output

Run the script and press **Enter** at the separator prompt. The included input produces these eight fields:

```json
{
  "user.id": 1,
  "user.name": "Riya",
  "user.email": "riya@example.com",
  "user.address.city": "Delhi",
  "user.address.pincode": 110001,
  "roles.0": "admin",
  "roles.1": "editor",
  "is_active": true
}
```

Choosing `-` instead gives keys such as `user-id`, `user-address-pincode`, `roles-0`, and `roles-1`. Only the keys change; the leaf values keep their JSON types. Unlike Day 7's CSV input, JSON input already distinguishes numbers, strings, and Booleans, so `1` remains a number and `true` remains a Boolean.

## Terminal messages and current behaviour

The dictionary branch includes `print(full_key)`, which traces keys during recursion. Those intermediate terminal lines help show the traversal; they are not additional fields in the saved JSON.

A missing input prints `No input file found` and returns. Other exceptions inside the conversion block are caught by `except Exception as e`, which prints `Failed to flatten the data` and the error. The current implementation does not preserve empty dictionaries or lists, because they have no leaf values to add. Keys containing the chosen separator can also produce ambiguous paths or collisions; there is no collision check.

This project uses only Python's standard-library `json`, `os`, and `pathlib` modules. It needs no additional packages or API keys.

## How to run

From the repository root:

```powershell
python "challenges/02_data_handling/day_8/day_8.py"
```

Or, from this lesson's folder:

```powershell
python .\day_8.py
```

In VS Code, open `day_8.py` and press **Ctrl + S**. For input prompts, click inside the Run on Save terminal, type your answer, and press **Enter**. Exit an older running instance before starting the moved script.

This lesson uses only Python's standard library or built-in features; no package installation is required.

Input and output paths resolve from this Python file, so data stays in this lesson folder regardless of the terminal's working directory.

## Useful links for beginners

- [JSON encoding and decoding](https://docs.python.org/3/library/json.html): reading and writing JSON records with `load()` and `dump()`.
- [Lists and dictionaries](https://docs.python.org/3/tutorial/datastructures.html): the row lists and named fields returned by CSV readers.
- [Paths with pathlib](https://docs.python.org/3/library/pathlib.html): `Path(__file__).resolve().parent` for keeping input and output beside the script.

[Previous: Day 7](../day_7/README.md) · [Next: Day 9](../day_9/README.md)
