# Day 7: CSV-to-JSON Converter Tool

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

This project converts a CSV table into a JSON list of dictionaries. It complements Day 6's JSON-to-CSV conversion, using its own input file rather than Day 6's output.

Read the unchanged [original task](DAY_7.md) alongside [day_7.py](day_7.py). Project explanations and updates belong in this README; the original task text is maintained separately.

## Files

| File | Purpose |
| --- | --- |
| [DAY_7.md](DAY_7.md) | The original CSV-to-JSON Converter Tool challenge heading. |
| [day_7.py](day_7.py) | Reading CSV rows as dictionaries, saving them as JSON, and previewing records. |
| [raw_data.csv](raw_data.csv) | Ten fictional users with `id`, `name`, `email`, `location`, and `is_active` columns. |
| [converted_data.json](converted_data.json) | The generated JSON list of records, with CSV field values preserved as strings. |

## Input, output, and file paths

`raw_data.csv` contains 10 fictional users with American names and cities. Its header defines five fields: `id`, `name`, `email`, `location`, and `is_active`. For example, the first record is:

```csv
id,name,email,location,is_active
1,Daniel Carter,daniel.carter@example.com,"Los Angeles, CA",true
```

The location is quoted because it contains a comma. `csv.DictReader` reads it as one field, without including the surrounding quotes in its value.

`INPUT_FILE` and `OUTPUT_FILE` use `Path(__file__).resolve().parent`, so the script reads `raw_data.csv` and creates `converted_data.json` in `challenges/02_data_handling/day_7`. The same paths work when running from the repository root or saving the Python file with **Ctrl + S**. The CSV input is not modified.

## Functions and conversion flow

1. `main()` calls `load_csv_data(INPUT_FILE)`. A missing file prints `CSV file not found` and returns an empty list.
2. `csv.DictReader` uses the header row as dictionary keys, and `list(reader)` collects the data rows. The loader also prints the complete list before returning it.
3. If the loaded list is empty, `main()` returns without writing output. Otherwise, it calls `save_as_json(data, OUTPUT_FILE)`.
4. `json.dump(data, f, indent=2)` saves the records as a JSON array using two-space indentation. UTF-8 write mode replaces the output file on each successful conversion.
5. The function prints the converted-record count and the output's absolute path. With the included input, the count is `10`.
6. `preview_data(data, count=3)` formats the first three records individually with `json.dumps(row, indent=2)`, then prints `.......`. The slice `data[:count]` controls the preview size.

The file contains all 10 records, even though the final formatted preview shows only three. The complete list printed earlier comes from the loader, not from an additional conversion.

## CSV text values in JSON

CSV values are read as strings. The first generated JSON record therefore looks like this:

```json
{
  "id": "1",
  "name": "Daniel Carter",
  "email": "daniel.carter@example.com",
  "location": "Los Angeles, CA",
  "is_active": "true"
}
```

`"1"` is text rather than the number `1`, and `"true"` is text rather than the JSON Boolean `true`. The current converter preserves CSV text without guessing types. Quotation marks around JSON keys and string values are part of valid JSON syntax.

## Running and current behaviour

Run the script using the command in the shared instructions below. It needs only Python's standard-library `csv`, `json`, `os`, and `pathlib` modules; no packages or API keys are required.

The input must have a header row. A header-only or empty file produces no new JSON output; an existing output file is left as it was. File-read errors and malformed CSV structures are not explicitly handled. Type conversion, choosing columns, and extra data validation are not implemented in the current script.

To view the result, open `converted_data.json` in VS Code. This project produces JSON rather than an Excel workbook, and it does not update Day 6's `converted_data.csv` or `converted_data.xlsx`.

## How to run

From the repository root:

```powershell
python "challenges/02_data_handling/day_7/day_7.py"
```

Or, from this lesson's folder:

```powershell
python .\day_7.py
```

In VS Code, open `day_7.py` and press **Ctrl + S**. For input prompts, click inside the Run on Save terminal, type your answer, and press **Enter**. Exit an older running instance before starting the moved script.

This lesson uses only Python's standard library or built-in features; no package installation is required.

Input and output paths resolve from this Python file, so data stays in this lesson folder regardless of the terminal's working directory.

## Useful links for beginners

- [Python CSV reading and writing](https://docs.python.org/3/library/csv.html): reading rows and dictionaries, writing records, and handling CSV line endings.
- [JSON encoding and decoding](https://docs.python.org/3/library/json.html): reading and writing JSON records with `load()` and `dump()`.
- [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files): file modes, encoding, and closing files with `with`.
- [Paths with pathlib](https://docs.python.org/3/library/pathlib.html): `Path(__file__).resolve().parent` for keeping input and output beside the script.

[Previous: Day 6](../day_6/README.md) · [Next: Day 8](../day_8/README.md)
