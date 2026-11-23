# Day 8: Generate a Book Dataset

Create a small practice dataset from 10 book records defined in Python and export it to [books.csv](books.csv) using pandas.

[Data Science overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

## Files

```text
day_8/
├── day_8.py
├── books.csv
├── DAY_8.md
└── README.md
```

[DAY_8.md](DAY_8.md) describes the task. It was authored locally from the supplied script because no original task statement was provided.

## How to run

From the repository root, install pandas in the Python environment used by VS Code and run the script:

```powershell
python -m pip install pandas
python "challenges/05_data_science/day_8/day_8.py"
```

You can also open `day_8.py` and press **Ctrl + S** with the project's existing Run on Save configuration. This is a regular terminal script and does not require Streamlit or a notebook kernel.

Expected terminal output:

```text
✅ Book dataset created
```

## How the code works

1. `data` is a list containing 10 dictionaries. Each dictionary represents one book.
2. The keys `title`, `author`, `genre`, and `description` become the four CSV columns.
3. `pd.DataFrame(data)` creates a table, with one row per book.
4. `Path(__file__).resolve().parent / "books.csv"` selects an output file beside `day_8.py`, regardless of the terminal's working directory. This replaces the original working-directory-relative filename.
5. `df.to_csv(..., index=False)` writes the table without adding a separate row-index column.
6. `print()` confirms that the export has finished.

For example, the first record has the title `The Silent Forest`, author `Jane Hill`, and genre `Mystery`, along with a longer description.

## Output and repeat runs

The script creates or replaces `challenges/05_data_science/day_8/books.csv`. Every run writes the same 10 predefined records; it does not append duplicate rows. Manual changes to that CSV are replaced the next time the script runs, so change `data` in the Python file if you want the generated dataset to change.

The book records are local practice data. This script does not fetch books from the internet, request user input, train a model, or generate recommendations. You can inspect the CSV as text in VS Code or open it in a spreadsheet application.

## Useful links and package source

- [pandas](https://pandas.pydata.org/): the library used to create and export the table.
- [DataFrame reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html): creating a table from records.
- [DataFrame.to_csv reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html): CSV export options, including `index=False`.
- [pandas — GitHub](https://github.com/pandas-dev/pandas): the official source repository.

`pathlib` is part of Python's standard library and requires no separate installation.
