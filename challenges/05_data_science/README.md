# Challenges — Data Science

This group corresponds to `05_data_science` in the Udemy tutorial and follows [04_automation](../04_automation/README.md).

**Status: in progress — current course section.** Day 1 introduces Python notebooks, Day 2 generates an experience/salary dataset, and Day 3 fits and plots a linear regression model using that dataset.

[Challenge index](../README.md) · [Main project overview](../../README.md#folder-overview)

## Learning order and folder layout

Each lesson has its own folder, starting with `day_1`. Use names without leading zeros, such as `day_1/day_1.ipynb` and `day_2/day_2.py`. Keep each lesson's notebook or script, `DAY_*.md` task statement, data, and README together. This group README provides the overview and links to individual lessons.

| Lesson guide | Project | Main concepts |
| --- | --- | --- |
| [day_1](day_1/README.md) | Introduction to Python Notebooks | Markdown and code cells, kernels, `print()`, `for`, `range()`, and f-strings. |
| [day_2](day_2/README.md) | Generate an Experience and Salary Dataset | NumPy arrays, seeded random values, pandas DataFrames, CSV export, and script-relative output paths. |
| [day_3](day_3/README.md) | Salary Prediction with Linear Regression | CSV input, features and targets, scikit-learn, model fitting, predictions, and Matplotlib charts. |

The Day 1–3 task descriptions were authored locally from the supplied notebook/scripts because no original statements were provided. Their `DAY_*.md` files identify that origin. Preserve task statements during later documentation updates.

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

## Useful links for beginners

- [Download Anaconda](https://www.anaconda.com/download): Python distribution and notebook tools introduced in this section.
- [Project Jupyter](https://jupyter.org/): the notebook tools' official website.
- [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks): opening notebooks, selecting kernels, running cells, and saving outputs.
- [NumPy](https://numpy.org/): numerical arrays and random values used in Day 2.
- [NumPy for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html): introductory array examples.
- [pandas](https://pandas.pydata.org/): the table library used in Day 2.
- [Reading and writing tables with pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html): introductory CSV examples.
- [Kaggle Datasets](https://www.kaggle.com/datasets): datasets to explore as future practice; Day 2 currently generates its own data locally.
- [scikit-learn documentation](https://scikit-learn.org/stable/): the machine learning library used in Day 3.
- [LinearRegression reference](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html): the model used for experience/salary predictions.

## Package source repositories

- [NumPy — GitHub](https://github.com/numpy/numpy): imported as `numpy` (`np` in the script).
- [pandas — GitHub](https://github.com/pandas-dev/pandas): imported as `pandas` (`pd` in the script).
- [ipykernel — GitHub](https://github.com/ipython/ipykernel): Python kernel used by the notebook environment; [official documentation](https://ipykernel.readthedocs.io/en/stable/).
- [scikit-learn — GitHub](https://github.com/scikit-learn/scikit-learn): imported from `sklearn.linear_model` in Day 3.
- [Matplotlib — GitHub](https://github.com/matplotlib/matplotlib): imported as `matplotlib.pyplot` for the Day 3 chart.

Use **Star** on GitHub to support the projects. See the [project-wide package index](../../README.md#package-source-repositories) for other packages used in the course.

Related optional tool: [Kaggle CLI — GitHub](https://github.com/Kaggle/kaggle-cli), the official command-line tool for interacting with Kaggle. It is a reference for later use and is not required by the current lessons.
