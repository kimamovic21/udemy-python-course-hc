# Day 3: Salary Prediction with Linear Regression

> This task description was written locally from the supplied `day_3.py`, at the repository owner's request. It is not an original task statement downloaded from Udemy.

## Goal

Use the synthetic experience/salary dataset from Day 2 to fit a linear regression model and visualize the relationship between experience and salary.

## Tasks

1. Load `experience_salary.csv` into a pandas DataFrame. In this repository, read the file generated in `day_2`.
2. Select `YearsExperience` as the input feature `X`, keeping it as a two-dimensional table.
3. Select `Salary` as the target `y`. In the working version, use a one-dimensional Series for this single target.
4. Create a `LinearRegression` model from `sklearn.linear_model`.
5. Train the model using `model.fit(X, y)`.
6. Use `model.predict(X)` to calculate a predicted salary for each experience value and add a `PredictedSalary` column in memory.
7. Print the model's coefficient (slope) and intercept, rounded to two decimal places.
8. Display the original data as blue scatter points and predictions as a red regression line.
9. Add axis labels, a title, a legend, a grid, and a tidy layout to the Matplotlib chart.

## Expected result

The terminal displays the fitted slope and intercept. A Matplotlib window displays a chart titled `Salary vs Experience`, with years of experience on the horizontal axis and salary on the vertical axis.

Day 3 uses the generated practice data from Day 2. It does not overwrite that CSV or automatically save the model or chart to a file.

## Concepts and tools

pandas, CSV input, features and targets, scikit-learn, `LinearRegression`, `.fit()`, `.predict()`, model coefficients, and Matplotlib visualization.
