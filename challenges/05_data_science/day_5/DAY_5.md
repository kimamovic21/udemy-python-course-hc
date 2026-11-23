# Day 5: Generate a Labeled YouTube Comments Dataset

> This task description was written locally from the supplied `day_5.py`, at the repository owner's request. It is not an original task statement downloaded from Udemy.

## Goal

Create a small synthetic dataset of comments with labels that can be used for later text-processing exercises.

## Tasks

1. Define a list of ten example toxic comments.
2. Define a list of ten example supportive comments.
3. Create an empty list to hold the dataset records.
4. Repeat 50 times: randomly choose one comment from each list and append two dictionaries to the dataset.
5. Give each dictionary the keys `comment` and `label`. Use the labels `toxic` and `support` exactly.
6. Create a pandas DataFrame from the records.
7. Export it to `youtube_comments.csv` without a DataFrame index. In this repository, save the CSV beside `day_5.py`.
8. Print a confirmation after saving.

## Expected result

A CSV containing the header below and 100 data rows: 50 labeled `toxic` and 50 labeled `support`.

```text
comment,label
```

The terminal prints:

```text
✅ Data saved successfully
```

Comments are selected with replacement, so repeated text is expected. The data comes from the sample lists in the script, not from downloading YouTube comments.

## Concepts and tools

Python lists and dictionaries, loops, `random.choice()`, labels, pandas DataFrames, CSV export, and script-relative output paths. The supplied script also imports NumPy but does not use it in the generation logic.

## Related reference

[TfidfVectorizer documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) describes converting text into numeric TF-IDF features. It is a related reference for later text-processing work and is not implemented in this generator.
