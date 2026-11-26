# Day 10: Book Recommendation App with Streamlit

Enter a book title in a browser and display five recommendations. This lesson adds a Streamlit interface to the TF-IDF/cosine-similarity approach introduced in Day 9.

[Data Science overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

## Files and local input

```text
day_10/
├── day_10.py
├── books.csv
├── DAY_10.md
└── README.md
```

[books.csv](books.csv) is a local copy of Day 9's 10-book dataset, originally generated in Day 8. `Path(__file__).resolve().parent / "books.csv"` reads this copy beside the script, regardless of the terminal's working directory. Updating the earlier lessons does not automatically update this file.

To refresh the local input from Day 9, stop the app and run this from the repository root:

```powershell
Copy-Item -LiteralPath "challenges/05_data_science/day_9/books.csv" -Destination "challenges/05_data_science/day_10/books.csv"
```

Then start the app again. The script reads the CSV without overwriting it and does not save recommendation or model files.

## Setup and running

Install the dependencies in the Python environment used by VS Code:

```powershell
python -m pip install streamlit pandas scikit-learn
```

Open `day_10.py` and press **Ctrl + S**. The workspace's Run on Save rule starts **Run current Data Science Streamlit app**, the shared task used by Days 4, 7, and 10. Open the Local URL printed in its terminal, normally `http://localhost:8501`.

Only one instance of this task runs at a time. Before switching from another Streamlit lesson, stop that app with **Ctrl + C** in its task terminal, then open and save `day_10.py`. Later saves let Streamlit rerun the current app. If the updated save rule has not loaded, run **Developer: Reload Window** and save again.

You can also start the app manually from the repository root:

```powershell
python -m streamlit run "challenges/05_data_science/day_10/day_10.py" --server.runOnSave true
```

Use the Streamlit runner instead of ordinary `python -u day_10.py`, which does not create the browser app's session. Stop the server with **Ctrl + C** when finished.

## Using the app

Enter `Spacebound` in **Book: Title** and press **Enter** to apply the text. With the included CSV, the table contains:

| title | author |
| --- | --- |
| Beneath the Waves | Diana Coast |
| Mystic Academy | Lara Moon |
| The Silent Forest | Jane Hill |
| Love in Paris | Emily Rose |
| Quantum Heist | Leo Hunt |

Numbers such as `7`, `4`, and `0` beside the table are the original DataFrame row indexes, not ratings or similarity scores.

Matching ignores letter case and whitespace at the beginning and end: `spacebound` and ` Spacebound ` also work. The title must otherwise match a book in the CSV; partial titles and spelling mistakes are not supported. An unknown title displays a warning instead of a recommendations table. An empty field displays no results.

## How the code works

1. pandas reads the CSV. `.str.strip()` cleans title edges, and `.fillna("")` replaces missing descriptions with empty strings.
2. `TfidfVectorizer(stop_words="english")` converts descriptions into numeric features while ignoring common English stop words.
3. `cosine_similarity()` compares the description vectors and creates a matrix of scores.
4. A pandas Series maps lowercase titles to row positions.
5. `get_recommendations()` normalizes the input and checks whether the title exists. For a known title, it sorts similarity scores and uses `[1:6]` to select five results after the first, which is the chosen book for the supplied examples.
6. `st.title()` and `st.write()` display the page heading and instructions. `st.text_input()` supplies the entered title.
7. The app calls the function when the input is non-empty. `st.table()` displays a returned DataFrame, while `st.warning()` displays the missing-title message.

The page is written in Python. Streamlit supplies the browser interface, so this lesson does not require writing HTML, CSS, or JavaScript.

## Difference from Day 9

| Day 9 | Day 10 |
| --- | --- |
| Prints recommendations in the terminal. | Displays recommendations in a browser table. |
| The example title is changed in Python code. | The title is entered in a text field. |
| Requires an exact, case-sensitive title. | Normalizes letter case and surrounding whitespace. |
| A missing title raises `KeyError`. | A missing title displays a warning. |

Both compare the `description` column. Genre and author are not ranking features, and neither lesson uses user ratings or browsing history.

## Limits and reruns

This is a small practice dataset. The function returns five rows even when some similarity scores are zero; tied scores can produce weak recommendations. The current ranking skips the first result rather than explicitly filtering the selected row. The sample assumes unique book titles and does not provide reliable duplicate-title handling.

Unlike Day 7's cached classifier, this script has no caching decorator. Streamlit reruns the script when submitted input changes, reading the CSV and rebuilding its TF-IDF features and similarity matrix. It does not train a supervised classifier or save a fitted model.

The original `pd.read_csv("books.csv")` searched the terminal's working directory and raised `FileNotFoundError`. The local path and included CSV fix that issue. The workspace also routes Day 10 through Streamlit on save.

[DAY_10.md](DAY_10.md) was authored locally from the supplied code because no original task statement was provided. Preserve that statement during later documentation updates.

## Useful links and package sources

- [Streamlit](https://streamlit.io/): the web application framework.
- [Run a Streamlit app](https://docs.streamlit.io/develop/concepts/architecture/run-your-app): starting the local server.
- [st.text_input](https://docs.streamlit.io/develop/api-reference/widgets/st.text_input): the book-title input.
- [st.table](https://docs.streamlit.io/develop/api-reference/data/st.table): displaying the recommendations.
- [TfidfVectorizer reference](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html): description features and stop words.
- [cosine_similarity reference](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html): comparing those features.
- [Streamlit — GitHub](https://github.com/streamlit/streamlit): official source repository.
- [scikit-learn — GitHub](https://github.com/scikit-learn/scikit-learn): official source repository.
- [pandas — GitHub](https://github.com/pandas-dev/pandas): official source repository.

`pathlib` is part of Python's standard library and needs no separate installation.
