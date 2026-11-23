# Day 7: YouTube Comment Classifier with Streamlit

Enter a comment in a local browser app and classify it as `toxic` or `support`. A TF-IDF/logistic regression pipeline is trained using the local [youtube_comments.csv](youtube_comments.csv), copied from Day 6. `st.cache_resource` reuses the fitted model across app reruns.

[Data Science overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

## Running the app

Open `day_7.py` in VS Code and press **Ctrl + S**. This starts **Run current Data Science Streamlit app**. Open the Local URL printed in its terminal, normally `http://localhost:8501`.

The shared task permits one running app. Before switching between Day 4 and Day 7, stop the previous app with **Ctrl + C** in the task terminal, then open and save the intended script. Later saves of the running app let Streamlit rerun it. If the updated save rule is not picked up, run **Developer: Reload Window** and save again.

You can also start Day 7 manually from the repository root:

```powershell
python -m streamlit run "challenges/05_data_science/day_7/day_7.py" --server.runOnSave true
```

This app needs the Streamlit runner; ordinary `python -u day_7.py` does not create a Streamlit session and can produce `missing ScriptRunContext` or `NoSessionContext` messages.

## Input and output

`DATA_FILE` uses `Path(__file__).resolve().parent` to read `day_7/youtube_comments.csv`, independently of the terminal's working directory. Changes to Day 6's CSV do not automatically update this copy. The app does not overwrite its dataset or save the trained model to a file.

```text
day_7/
├── day_7.py
├── youtube_comments.csv
├── DAY_7.md
└── README.md
```

To replace the local dataset with a newer Day 6 copy, stop the app, copy the CSV, and start it again. From the repository root:

```powershell
Copy-Item -LiteralPath "challenges/05_data_science/day_6/youtube_comments.csv" -Destination "challenges/05_data_science/day_7/youtube_comments.csv"
```

Enter a non-empty comment to see the classification. A toxic prediction displays an error-style message; a support prediction displays a success message. The labels are predictions from a small English practice dataset and can be inaccurate on new wording or other languages. This app trains on the full CSV and does not display a separate test accuracy.

For example, try `This helped me a lot!` and `This is trash`, both of which are sample phrases used by the dataset generator. Apply the changed text by clicking outside the text area. An empty field produces no classification message. This is a text interface; there is no regression chart in this lesson.

## How the code works

1. `DATA_FILE` identifies the CSV beside the script.
2. `load_model()` reads the table and creates a pipeline with `TfidfVectorizer()` and `LogisticRegression()`.
3. `model.fit(df["comment"], df["label"])` learns from all labeled records in that CSV.
4. `@st.cache_resource` lets later app reruns reuse the fitted pipeline instead of training it again for each input change.
5. `st.title()` and `st.write()` display the heading and instructions.
6. `st.text_area()` supplies the user's text to `user_input`.
7. `if user_input:` checks whether the string is non-empty. It does not trim whitespace or validate the language.
8. `model.predict([user_input])` expects a collection of comments, so the brackets wrap the single string in a list. `[0]` takes the first prediction.
9. `st.error()` renders the toxic message, while `st.success()` renders the supportive message.

Day 6 fits on a training split and reports accuracy on a test split. Day 7 creates its own model from the full local dataset for interactive predictions; it does not load a model file saved by Day 6.

## Cached model and dataset changes

The cached model lives in the running server's memory. Changing a comment in the UI reruns the app while reusing that model. Updating the CSV alone does not automatically invalidate this no-argument cached function.

After replacing the CSV, stop and restart the Streamlit server to rebuild the model from the new records. No model or prediction file is created on disk by this script.

## Package setup

```powershell
python -m pip install streamlit pandas scikit-learn
```

`pathlib` is part of Python's standard library. The imported `train_test_split` is not used by the current script.

## Local fixes and task description

The original relative CSV filename searched in the terminal's working directory. The working script uses a local copy beside `day_7.py`. The original plain `python -u` launch also caused Streamlit session errors; the shared VS Code task now launches this file through `python -m streamlit run`.

`DAY_7.md` was authored locally from the supplied script because no original statement was provided. Preserve that task statement during later documentation updates.

## Useful links and package sources

- [Streamlit](https://streamlit.io/): the web application framework.
- [Run your Streamlit app](https://docs.streamlit.io/develop/concepts/architecture/run-your-app): starting the server.
- [st.cache_resource](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource): caching resources such as trained models.
- [st.text_area](https://docs.streamlit.io/develop/api-reference/widgets/st.text_area): the comment input widget.
- [TfidfVectorizer reference](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html): text-to-numeric feature conversion.
- [scikit-learn documentation](https://scikit-learn.org/stable/): pipelines and classifiers.
- [Streamlit — GitHub](https://github.com/streamlit/streamlit): official source repository.
- [scikit-learn — GitHub](https://github.com/scikit-learn/scikit-learn): official source repository.
