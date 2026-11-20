# Day 2: Generate an Experience and Salary Dataset

Generate 100 synthetic experience/salary pairs with NumPy, arrange them in a pandas table, and export them to CSV.

[Data Science overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

## Setup and running

Install the packages with the same Python interpreter used to run the script:

```powershell
python -m pip install numpy pandas
python "challenges/05_data_science/day_2/day_2.py"
```

Or open `day_2.py` in VS Code and press **Ctrl + S** with the existing Run on Save setup. This lesson is a Python script; it does not require running notebook cells.

| Package | Import | Role |
| --- | --- | --- |
| NumPy | `import numpy as np` | Generates numeric arrays and random sample values, and performs calculations across the arrays. |
| pandas | `import pandas as pd` | Creates a DataFrame and exports it as a CSV table. |
| pathlib | `from pathlib import Path` | Locates the output beside the script; this module is part of Python's standard library. |

## How the code works

1. `np.random.seed(42)` initializes the pseudorandom sequence. Running the same code in the same environment reproduces the sample values.
2. `np.random.uniform(0.5, 10, 100).round(2)` generates 100 experience values and rounds them to two decimal places.
3. `np.random.normal(0, 4000, size=100)` generates 100 noise values centered on zero, with a standard deviation of `4000`.
4. `30000 + years * 6000 + noise` calculates salaries across the whole array. Each salary has a base amount, an experience-related amount, and random variation. The result is rounded to two decimal places.
5. `pd.DataFrame(...)` combines the two arrays into columns named `YearsExperience` and `Salary`.
6. `df.to_csv(OUTPUT_FILE, index=False)` saves those columns without adding a separate row-index column.
7. `print()` confirms the export in the terminal.

The numbers are synthetic practice data. The script does not specify a currency, read an external dataset, train a model, or plot a graph.

## CSV output and file location

`OUTPUT_FILE` uses `Path(__file__).resolve().parent`, so the file is saved as:

```text
challenges/05_data_science/day_2/experience_salary.csv
```

It stays beside the script even when the terminal is in the repository root. The original relative filename would have followed the terminal's current directory; only the output path was adjusted locally.

The generated CSV has one header and 100 data rows. Its first three records in the verified local environment are:

```csv
YearsExperience,Salary
4.06,54708.19
9.53,85983.97
7.45,75067.04
```

Each run replaces the existing CSV rather than appending records. Open the file in VS Code or a spreadsheet application to inspect the table. The terminal prints `Data saved in file ✅` after saving.

## If VS Code cannot resolve pandas

The initial warning appeared while pandas was missing from the terminal's Python environment. Installing it makes the import available to that interpreter.

If Pylance still displays the warning after installation:

1. Run `python -c "import sys; print(sys.executable)"` in the terminal to identify the interpreter used to run this project.
2. Use **Ctrl + Shift + P → Python: Select Interpreter** and choose that same Python environment.
3. If the diagnostic remains stale, use **Developer: Reload Window** from the command palette.

An Anaconda environment and the system Python have separate package installations. Select the environment where you installed NumPy and pandas.

## Task description provenance

`DAY_2.md` was authored locally from the supplied script at the repository owner's request because no original task description was available. Preserve that statement during later documentation updates.

## Useful links and package sources

- [NumPy](https://numpy.org/): the official project website.
- [NumPy for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html): imports, arrays, and basic calculations.
- [NumPy — GitHub](https://github.com/numpy/numpy): the official source repository, available to star.
- [pandas](https://pandas.pydata.org/): the official project website.
- [Reading and writing tables with pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html): introductory table and CSV examples.
- [pandas — GitHub](https://github.com/pandas-dev/pandas): the official source repository, available to star.
- [Kaggle Datasets](https://www.kaggle.com/datasets): a reference for finding datasets to explore in future exercises.
- [Kaggle CLI — GitHub](https://github.com/Kaggle/kaggle-cli): the official command-line tool for interacting with Kaggle, including downloading datasets.

Kaggle is an optional learning reference here. Day 2 generates its own synthetic CSV locally; it does not download Kaggle data or require the Kaggle CLI.
