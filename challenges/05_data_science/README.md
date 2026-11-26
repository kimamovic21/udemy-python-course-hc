# Challenges — Data Science

This group corresponds to `05_data_science` in the Udemy tutorial and follows [04_automation](../04_automation/README.md).

**Status: documented through Day 10.** Days 1–10 cover notebooks, synthetic datasets, regression, labeled comments, classification, Streamlit interfaces, book CSV export, and book recommendations in the terminal and browser. The next course project is [06_url_shortener](../06_url_shortener/README.md), section 16, days 46–52.

[Challenge index](../README.md) · [Main project overview](../../README.md#folder-overview)

## Learning order and folder layout

Each lesson has its own folder, starting with `day_1`. Use names without leading zeros, such as `day_1/day_1.ipynb` and `day_2/day_2.py`. Keep each lesson's notebook or script, `DAY_*.md` task statement, data, and README together. This group README provides the overview and links to individual lessons.

| Lesson guide | Project | Main concepts |
| --- | --- | --- |
| [day_1](day_1/README.md) | Introduction to Python Notebooks | Markdown and code cells, kernels, `print()`, `for`, `range()`, and f-strings. |
| [day_2](day_2/README.md) | Generate an Experience and Salary Dataset | NumPy arrays, seeded random values, pandas DataFrames, CSV export, and script-relative output paths. |
| [day_3](day_3/README.md) | Salary Prediction with Linear Regression | CSV input, features and targets, scikit-learn, model fitting, predictions, and Matplotlib charts. |
| [day_4](day_4/README.md) | Interactive Salary Predictor with Streamlit | Browser UI, numeric widgets, model predictions, embedded charts, and running a local Streamlit server. |
| [day_5](day_5/README.md) | Generate a Labeled YouTube Comments Dataset | Random sampling, labeled dictionaries, pandas DataFrames, and a balanced 100-row CSV. |
| [day_6](day_6/README.md) | Classify Comments with TF-IDF and Logistic Regression | Training/test splits, text features, pipelines, classification, and interpreting accuracy. |
| [day_7](day_7/README.md) | YouTube Comment Classifier with Streamlit | Text input, cached model training, TF-IDF classification, local CSV data, and browser messages. |
| [day_8](day_8/README.md) | Generate a Book Dataset | Lists of dictionaries, pandas DataFrames, CSV export without an index, and script-relative output paths. |
| [day_9](day_9/README.md) | Book Recommendations from Descriptions | TF-IDF, English stop words, cosine similarity, title lookups, sorting, and selecting five recommendations. |
| [day_10](day_10/README.md) | Book Recommendation App with Streamlit | Browser text input, title normalization, missing-title warnings, recommendation tables, and local CSV input. |

The Day 1–10 task descriptions were authored locally from the supplied notebook/scripts because no original statements were provided. Their `DAY_*.md` files identify that origin. Preserve task statements during later documentation updates.

## Opening the notebooks

Open `challenges/05_data_science/day_1/day_1.ipynb` in Jupyter Notebook, JupyterLab, or VS Code with its Jupyter extension. Select a Python kernel and run cells from top to bottom with **Shift + Enter** or **Run All**.

**Ctrl + S** saves the notebook; the existing `.py` Run on Save configuration does not execute notebook cells. See the [Day 1 setup instructions](day_1/README.md#running-the-notebook-in-vs-code) for kernel selection and the example outputs.

If the selected Python environment lacks the notebook runtime, install it with `python -m pip install ipykernel` using that environment's Python. See [Day 1: installing ipykernel](day_1/README.md#if-the-notebook-asks-for-ipykernel). This package runs notebook cells; the Day 2 `.py` script uses NumPy and pandas without requiring a notebook kernel.

## Running Day 2

Install NumPy and pandas in the Python environment used by the project, then run the script from the repository root:

```powershell
python -m pip install numpy pandas
python "challenges/05_data_science/day_2/day_2.py"
```

Day 2 can also run through the existing **Ctrl + S** setup for Python scripts. It creates or replaces `day_2/experience_salary.csv` beside the script with 100 synthetic records and no index column. The [Day 2 guide](day_2/README.md) explains the calculations, the output location, and resolving pandas imports in VS Code.

## Running Day 3

Day 3 requires pandas, Matplotlib, and scikit-learn. The package name is `scikit-learn`, while the Python import uses `sklearn`.

```powershell
python -m pip install pandas matplotlib scikit-learn
python "challenges/05_data_science/day_3/day_3.py"
```

Run Day 2 first if `day_2/experience_salary.csv` is missing. Day 3 reads that file directly using a script-relative path, fits a model, prints its slope and intercept, and opens a chart. Predictions remain in memory; it does not modify the CSV or save model/chart files automatically. The [Day 3 guide](day_3/README.md) explains the model, input path, import fix, and original array-shape issue.

A manually saved [chart example](day_3/README.md#saved-chart-example) is included as `day_3/salary_vs_experience_linear_regression.png`.

## Running Day 4

Day 4 uses Streamlit to display the salary predictor in a browser. It reads the same CSV generated by Day 2.

```powershell
python -m pip install streamlit pandas matplotlib scikit-learn
python -m streamlit run "challenges/05_data_science/day_4/day_4.py" --server.runOnSave true
```

Open the Local URL printed in the terminal and keep the process running. Stop it with **Ctrl + C**. In VS Code, **Ctrl + S** on `day_4.py` starts the shared Streamlit task instead of the regular `python -u` command. Later saves reuse the running task and rerun the app. Stop the previous app before switching between Days 4, 7, and 10. The [Day 4 guide](day_4/README.md) explains setup, task controls, the experience input, predictions, chart, and local code adjustments.

## Running Day 5

Day 5 uses pandas and imports NumPy, with Python's built-in `random` module selecting comments from predefined lists:

```powershell
python -m pip install pandas numpy
python "challenges/05_data_science/day_5/day_5.py"
```

It also runs on **Ctrl + S** as a regular Python script. Each run creates or replaces `day_5/youtube_comments.csv` with 100 records: 50 labeled `toxic` and 50 labeled `support`. Repeated comments are expected. The [Day 5 guide](day_5/README.md) explains the generation logic and the script-relative output path. `TfidfVectorizer` is linked as a related reference; text vectorization and classifier training are not implemented in this generator.

## Running Day 6

Day 6 reads its own copy of the CSV originally produced by Day 5 and trains a TF-IDF/logistic regression pipeline:

```powershell
python -m pip install pandas scikit-learn
python "challenges/05_data_science/day_6/day_6.py"
```

The input is included as `day_6/youtube_comments.csv`, beside `day_6.py`. Updating Day 5 does not change this local copy; follow the [Day 6 copy instructions](day_6/README.md#input-file-and-path-fix) to refresh it. Day 6 uses 80% of the rows for training and 20% for testing, prints an accuracy percentage, then exits. It runs through ordinary **Ctrl + S** execution and creates no output files. The guide explains the pipeline and why repeated sample comments can make a 100% score misleading for new text.

## Running Day 7

Day 7 uses its own `day_7/youtube_comments.csv`, copied from Day 6, to train a cached classifier and predict labels for user-entered comments.

```powershell
python -m pip install streamlit pandas scikit-learn
python -m streamlit run "challenges/05_data_science/day_7/day_7.py" --server.runOnSave true
```

In VS Code, open `day_7.py` and press **Ctrl + S** to start the shared Streamlit task. Open its Local URL, normally `http://localhost:8501`. Stop any previously running Streamlit task with **Ctrl + C** before switching apps. The [Day 7 guide](day_7/README.md) explains text input, prediction messages, local data copies, and restarting after CSV updates so the cached model is retrained. This app trains on the full CSV and does not report test accuracy.

## Running Day 8

Day 8 converts 10 predefined book dictionaries into a pandas table and exports it to CSV:

```powershell
python -m pip install pandas
python "challenges/05_data_science/day_8/day_8.py"
```

It also runs through ordinary **Ctrl + S** execution. Each run creates or replaces `day_8/books.csv` beside the script, with the columns `title`, `author`, `genre`, and `description`, and no index column. This lesson prepares local practice data without downloading books or training a model. The [Day 8 guide](day_8/README.md) explains the code, output path, and overwrite behavior.

## Running Day 9

Day 9 reads its own copy of `books.csv` beside the script and compares book descriptions using TF-IDF and cosine similarity:

```powershell
python -m pip install pandas scikit-learn
python "challenges/05_data_science/day_9/day_9.py"
```

It also runs through ordinary **Ctrl + S** execution. The current final line prints five recommendations for `Spacebound`; edit that title to try another existing book. Without a function call and `print()`, the script only prepares the data and produces no terminal output. It does not change the CSV or save results. The [Day 9 guide](day_9/README.md) explains local data copies, the ranking steps, and limitations of the small dataset.

## Running Day 10

Day 10 adds a Streamlit interface to the book recommender and reads its own `day_10/books.csv`, copied from Day 9:

```powershell
python -m pip install streamlit pandas scikit-learn
python -m streamlit run "challenges/05_data_science/day_10/day_10.py" --server.runOnSave true
```

In VS Code, **Ctrl + S** on `day_10.py` starts the shared Streamlit task used by Days 4, 7, and 10. Stop the previous app before switching lessons and open the printed Local URL, normally `http://localhost:8501`. Enter `Spacebound` and press **Enter** to see five titles and authors. Unknown titles show a warning. The [Day 10 guide](day_10/README.md) covers local input, title normalization, the difference from Day 9, and reruns without caching. The CSV is not modified and no output files are created.

## Useful links for beginners

- [Download Anaconda](https://www.anaconda.com/download): Python distribution and notebook tools introduced in this section.
- [Project Jupyter](https://jupyter.org/): the notebook tools' official website.
- [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks): opening notebooks, selecting kernels, running cells, and saving outputs.
- [NumPy](https://numpy.org/): numerical arrays and random values used in Day 2.
- [NumPy for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html): introductory array examples.
- [pandas](https://pandas.pydata.org/): the table library used to read and export lesson datasets, including the Day 8 book CSV.
- [Reading and writing tables with pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html): introductory CSV examples.
- [Kaggle Datasets](https://www.kaggle.com/datasets): datasets to explore as future practice; Day 2 currently generates its own data locally.
- [scikit-learn documentation](https://scikit-learn.org/stable/): the library used for salary regression, comment classification, and book-description similarity.
- [LinearRegression reference](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html): the model used for experience/salary predictions.
- [Logistic regression — Wikipedia](https://en.wikipedia.org/wiki/Logistic_regression): background reading for the Day 6 classifier.
- [LogisticRegression reference](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html): scikit-learn's classification model used in Day 6.
- [Streamlit](https://streamlit.io/): the framework used for the browser interfaces in Days 4, 7, and 10.
- [Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud): an optional service for publishing and sharing Streamlit apps from GitHub. The current lessons are configured for local execution.
- [Run your Streamlit app](https://docs.streamlit.io/develop/concepts/architecture/run-your-app): starting the local server using the project's Python interpreter.
- [Streamlit resource caching](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource): reusing the fitted comment classifier across Day 7 app reruns.
- [TfidfVectorizer reference](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html): converting text into features for the comment classifiers and book recommendations in Days 9–10.
- [cosine_similarity reference](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html): comparing book-description vectors in Days 9–10.

## Package source repositories

- [NumPy — GitHub](https://github.com/numpy/numpy): imported as `numpy` (`np` in the script).
- [pandas — GitHub](https://github.com/pandas-dev/pandas): imported as `pandas` (`pd` in the script).
- [ipykernel — GitHub](https://github.com/ipython/ipykernel): Python kernel used by the notebook environment; [official documentation](https://ipykernel.readthedocs.io/en/stable/).
- [scikit-learn — GitHub](https://github.com/scikit-learn/scikit-learn): regression, text vectorization, pipelines, train/test splitting, classification, and cosine similarity in Days 3–7 and 9–10.
- [Matplotlib — GitHub](https://github.com/matplotlib/matplotlib): imported as `matplotlib.pyplot` for the Day 3 chart.
- [Streamlit — GitHub](https://github.com/streamlit/streamlit): imported as `streamlit` (`st`) for the Day 4, Day 7, and Day 10 apps.

Use **Star** on GitHub to support the projects. See the [project-wide package index](../../README.md#package-source-repositories) for other packages used in the course.

Related optional tool: [Kaggle CLI — GitHub](https://github.com/Kaggle/kaggle-cli), the official command-line tool for interacting with Kaggle. It is a reference for later use and is not required by the current lessons.
