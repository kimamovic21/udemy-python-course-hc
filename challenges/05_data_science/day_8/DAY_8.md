# Day 8: Generate a Book Dataset

> This task description was written locally from the supplied `day_8.py`, at the repository owner's request. It is not an original task statement downloaded from Udemy.

## Goal

Prepare a small book dataset in Python and save it as a CSV file using pandas.

## Tasks

1. Define a list named `data` containing the 10 supplied book records.
2. Represent each book as a dictionary with the keys `title`, `author`, `genre`, and `description`.
3. Convert the list to a pandas DataFrame.
4. Export the table to `books.csv` without a DataFrame index column.
5. In this repository, save the file beside `day_8.py` using a script-relative path.
6. Print `✅ Book dataset created` after the export finishes.

## Expected result

`books.csv` contains a header with four columns and 10 book records. Running the script again replaces the existing file with the same predefined data.

The program only prepares and exports data; it does not download book information or train a machine learning model.

## Concepts and tools

Lists, dictionaries, pandas DataFrames, CSV export, `index=False`, and script-relative paths with `pathlib`.
