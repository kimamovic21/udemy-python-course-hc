# Day 7: YouTube Comment Classifier with Streamlit

> This task description was written locally from the supplied `day_7.py`, at the repository owner's request. It is not an original task statement downloaded from Udemy.

## Goal

Create a local web application where a user can enter a comment and receive a `toxic` or `support` prediction from a trained text classifier.

## Tasks

1. Read the local `youtube_comments.csv` using pandas. In this repository, use the copy beside `day_7.py`, originally copied from Day 6.
2. Create a `load_model()` function decorated with `@st.cache_resource`.
3. Inside the function, build a pipeline containing `TfidfVectorizer()` and `LogisticRegression()`.
4. Train the pipeline using the CSV's full `comment` and `label` columns, then return the fitted model.
5. Load the cached model and display a title and instructions with Streamlit.
6. Add a text area for entering a comment.
7. For a non-empty input, predict its class using `model.predict([user_input])[0]`.
8. Display an error-style message for a `toxic` prediction and a success message for `support`.
9. Run the app through Streamlit and test it in a browser.

## Expected result

The browser page displays a comment input and, after a non-empty entry is applied, a classification message. An empty input displays no classification result.

The fitted model is reused through Streamlit's resource cache. The app reads its local CSV without modifying it and does not save the model or predictions to a file. Unlike Day 6, this app does not create a train/test split or report test accuracy.

## Concepts and tools

Streamlit, text input, resource caching, pandas, TF-IDF features, scikit-learn pipelines, logistic regression classification, and local file paths.
