# Day 10: Book Recommendation App with Streamlit

> This task description was written locally from the supplied `day_10.py`, at the repository owner's request. It is not an original task statement downloaded from Udemy.

## Goal

Build a browser interface where a user can enter a book title and view five recommendations based on description similarity.

## Tasks

1. Load the local `books.csv` beside `day_10.py`. Use a copy of the dataset from Day 9.
2. Strip surrounding whitespace from the dataset's titles and replace missing descriptions with empty strings.
3. Transform the descriptions using `TfidfVectorizer(stop_words="english")` and calculate pairwise cosine similarity.
4. Prepare a title-to-row lookup using lowercase titles.
5. Define `get_recommendations(title, df, cosine_sim, indices)`. Normalize the entered title with `strip().lower()` and return a message if it is missing from the dataset.
6. For an existing title, sort similarity scores, use `[1:6]` to select five results after the first, and return their titles and authors.
7. Add a Streamlit heading, instructions, and a text input for the title.
8. Display a returned DataFrame with `st.table()` or a missing-title message with `st.warning()`.
9. Run the app through Streamlit and try `Spacebound`, `spacebound`, and an unknown title.

## Expected result

An existing book title displays a table of five titles and authors. Matching ignores letter case and surrounding whitespace. An unknown title displays a warning, and an empty input displays no recommendations.

The app reads its local CSV without changing it. Recommendation data is calculated in memory; no model or results are saved to disk.

## Concepts and tools

Streamlit, text input, tables, warnings, pandas, TF-IDF, cosine similarity, string normalization, title lookups, and script-relative file paths.
