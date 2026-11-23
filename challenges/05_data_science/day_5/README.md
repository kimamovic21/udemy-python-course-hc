# Day 5: Generate a Labeled YouTube Comments Dataset

Build a synthetic CSV of 100 comments with `toxic` and `support` labels. The text comes from two lists in the script; no YouTube API or downloaded comments are used.

[Data Science overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

## Setup and running

Install the packages imported by the supplied script with the project's Python interpreter:

```powershell
python -m pip install pandas numpy
python "challenges/05_data_science/day_5/day_5.py"
```

Or open `day_5.py` in VS Code and press **Ctrl + S** with the existing Run on Save setup. This lesson runs as a regular Python script, not a notebook or Streamlit application.

`random` and `pathlib` are part of Python's standard library. pandas creates and exports the table. The supplied NumPy import is retained, although the current generation logic does not call NumPy.

## How the code works

1. `toxic_comments` contains ten sample toxic comments.
2. `supportive_comments` contains ten sample supportive comments.
3. `data = []` creates a list for the generated records.
4. `for i in range(50)` repeats the generation step 50 times.
5. Each iteration uses `random.choice()` once per list and appends two dictionaries: a toxic record and a support record.
6. `pd.DataFrame(data)` creates columns named `comment` and `label`.
7. `df.to_csv(OUTPUT_FILE, index=False)` writes the CSV without an extra row-index column.
8. The confirmation message is `✅ Data saved successfully`.

Each iteration adds two rows, so 50 iterations produce 100 records. Labels alternate between `toxic` and `support`, with 50 records in each class. The supportive class is stored as `support`, not `supportive`.

Selection is with replacement: the same comment can appear more than once. There are at most 20 distinct comment texts in the current lists. No random seed is set, so the chosen comments can vary between runs.

## CSV output and location

The output is created or replaced at:

```text
challenges/05_data_science/day_5/youtube_comments.csv
```

`OUTPUT_FILE` uses `Path(__file__).resolve().parent`, so the output stays beside `day_5.py` even when the terminal is in the repository root. The original relative filename followed the terminal's current directory; the local adjustment changes only this destination.

The CSV has one header and 100 data rows. Its columns are:

| Column | Content |
| --- | --- |
| `comment` | A randomly chosen sample comment. |
| `label` | `toxic` or `support`, based on the source list. |

Every run replaces the previous file rather than appending records. Open the CSV in VS Code or a spreadsheet application to inspect it.

## TfidfVectorizer reference and current coverage

[TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) is a scikit-learn tool for converting text into numeric TF-IDF features. The reference is included for later text-processing exercises.

This Day 5 script only generates the labeled dataset. It does not yet vectorize text, train a classifier, evaluate predictions, or create a graph. scikit-learn is not required to run this generator.

## Task description provenance

`DAY_5.md` was authored locally from the supplied script at the repository owner's request because no original task description was provided. Preserve that statement during later documentation updates.

## Useful links and package sources

- [TfidfVectorizer documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html): the related text-processing reference supplied for this lesson.
- [pandas](https://pandas.pydata.org/): DataFrames and CSV export.
- [pandas — GitHub](https://github.com/pandas-dev/pandas): the table library's official source repository.
- [NumPy](https://numpy.org/): the library imported in the supplied script, currently unused here.
- [scikit-learn — GitHub](https://github.com/scikit-learn/scikit-learn): the source project containing `TfidfVectorizer`.
