# Day 9: Book Recommendations from Descriptions

Recommend five books by comparing their descriptions with a selected book. pandas loads the local dataset, while scikit-learn converts descriptions into TF-IDF features and calculates cosine similarity.

[Data Science overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

## Files and input data

```text
day_9/
├── day_9.py
├── books.csv
├── DAY_9.md
└── README.md
```

[books.csv](books.csv) is a local copy of the 10-book dataset generated in Day 8. Its columns are `title`, `author`, `genre`, and `description`. The script reads this copy beside `day_9.py`, independently of the terminal's working directory. Running Day 8 again does not update Day 9's copy.

To refresh this input from Day 8, run the following from the repository root:

```powershell
Copy-Item -LiteralPath "challenges/05_data_science/day_8/books.csv" -Destination "challenges/05_data_science/day_9/books.csv"
```

## How to run

Install the required packages in the Python environment used by VS Code, then run the script from the repository root:

```powershell
python -m pip install pandas scikit-learn
python "challenges/05_data_science/day_9/day_9.py"
```

Opening `day_9.py` and pressing **Ctrl + S** also runs it through the existing Run on Save configuration. This lesson runs in the terminal; it does not use Streamlit.

The current final line calls the function and prints its result:

```python
print(get_recommendations("Spacebound"))
```

With the included CSV, the output is a pandas table containing:

| title | author |
| --- | --- |
| Beneath the Waves | Diana Coast |
| Mystic Academy | Lara Moon |
| The Silent Forest | Jane Hill |
| Love in Paris | Emily Rose |
| Quantum Heist | Leo Hunt |

The numbers printed beside the terminal table are the original DataFrame row indexes. To try another book, replace `Spacebound` with an exact title from the CSV, such as `The Silent Forest`. There is no `input()` prompt. Without the final function call and `print()`, the script prepares the similarity data and defines the function, then exits without displaying recommendations.

## How the code works

1. `Path(__file__).resolve().parent / "books.csv"` locates the local input file, and `pd.read_csv()` loads it into `df`.
2. `TfidfVectorizer(stop_words="english")` prepares text features while ignoring common English stop words.
3. `fit_transform(df["description"])` learns a vocabulary from the descriptions and converts each description into a numeric vector.
4. `cosine_similarity(tfidf_matrix, tfidf_matrix)` compares every book with every other book. The current 10-book dataset produces a 10-by-10 matrix.
5. `pd.Series(df.index, index=df["title"])` maps each title to its row position.
6. Inside `get_recommendations()`, `indices[title]` finds the selected book and `enumerate(cosine_sim[idx])` pairs every row position with its similarity score.
7. `sorted(..., key=lambda x: x[1], reverse=True)` ranks those pairs by score. `[1:6]` skips the first result, which is the selected book for the supplied examples, and takes the next five.
8. The row positions are extracted into `book_indices`. `df[["title", "author"]].iloc[book_indices]` returns the corresponding titles and authors.

## What the recommendations mean

Only `description` is used to calculate similarity. `title` identifies the requested book and `author` appears in the output; `genre` is not used for ranking.

This is a content-based recommendation exercise. It does not learn from user ratings, purchase history, or browsing behavior. The vectorizer is fitted to the local descriptions each time the script runs; there is no labeled target or classification model like the comment classifier in Days 6–7.

With only 10 short descriptions, some recommendations can have a similarity score of zero. The function still returns five rows even when there are few meaningful matches. Tied scores follow their existing order, so a place in the result does not guarantee a strong connection. The implementation assumes unique titles and that the selected book is the first ranked result; it does not explicitly filter its row by identity.

The title lookup is exact and case-sensitive. A missing title raises `KeyError`; the current example does not add input validation. Scores and results remain in memory. The script does not modify `books.csv`, download data, or save recommendation/model files.

## Local adjustments and task description

The original `pd.read_csv("books.csv")` searched relative to the terminal's working directory. The local script uses `pathlib` to read Day 9's own CSV. A final `print(get_recommendations("Spacebound"))` demonstrates the result in the terminal.

[DAY_9.md](DAY_9.md) was authored locally from the supplied script at the owner's request because no original task statement was provided. Preserve that task statement during later documentation updates.

## Useful links and package sources

- [TfidfVectorizer reference](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html): text features and English stop words.
- [cosine_similarity reference](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html): comparing the description vectors.
- [scikit-learn documentation](https://scikit-learn.org/stable/): the machine learning library used in this section.
- [pandas](https://pandas.pydata.org/): CSV loading and table operations.
- [scikit-learn — GitHub](https://github.com/scikit-learn/scikit-learn): official source repository.
- [pandas — GitHub](https://github.com/pandas-dev/pandas): official source repository.

`pathlib` is included with Python and does not need a separate installation.
