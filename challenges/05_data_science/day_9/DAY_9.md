# Day 9: Book Recommendations from Descriptions

> This task description was written locally from the supplied `day_9.py`, at the repository owner's request. It is not an original task statement downloaded from Udemy.

## Goal

Build a simple content-based recommendation function that returns books with descriptions similar to a selected book.

## Tasks

1. Load the book dataset with pandas. In this repository, read the local `books.csv` beside `day_9.py`, copied from Day 8.
2. Create a `TfidfVectorizer` with `stop_words="english"` and transform the `description` column into numeric features.
3. Calculate the pairwise cosine similarity matrix for those features.
4. Create a pandas Series that maps book titles to their DataFrame row positions.
5. Define `get_recommendations(title, cosine_sim=cosine_sim)`.
6. Find the selected book's position, pair row positions with similarity scores, and sort the pairs from highest score to lowest.
7. Use `[1:6]` to skip the first result and select the next five, as in the supplied example.
8. Return a DataFrame containing the recommended books' `title` and `author` columns.
9. Demonstrate the function with `print(get_recommendations("Spacebound"))`.

## Expected result

Running the script prints a table of five recommended books and their authors for `Spacebound`. The script reads its CSV without modifying it and does not save a model or recommendations to disk.

The example assumes an exact, existing book title. Similarity comes from the descriptions; it does not use genre, ratings, or user history. Some results may have zero similarity because the practice dataset is small.

## Concepts and tools

pandas, CSV input, TF-IDF, English stop words, cosine similarity, Series lookups, `enumerate()`, sorting with a lambda, slicing, positional indexing with `iloc`, and script-relative paths.
