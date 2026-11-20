# Day 2: Generate an Experience and Salary Dataset

> This task description was written locally from the supplied `day_2.py`, at the repository owner's request. It is not an original task statement downloaded from Udemy.

## Goal

Use NumPy to generate a small synthetic dataset and pandas to organize it into a table and export it as CSV.

## Tasks

1. Import NumPy as `np` and pandas as `pd`.
2. Set the random seed to `42` so the same code produces repeatable sample values in the same environment.
3. Generate 100 experience values with `np.random.uniform(0.5, 10, 100)` and round them to two decimal places.
4. Calculate 100 salary values using a base amount of `30000`, an additional `6000` per year of experience, and random variation from `np.random.normal(0, 4000, size=100)`.
5. Round salary values to two decimal places.
6. Create a pandas DataFrame with columns named `YearsExperience` and `Salary`.
7. Export the table to `experience_salary.csv` without the DataFrame index. In the local project, save the CSV beside `day_2.py`.
8. Print a message confirming that the data was saved.

## Expected result

A CSV containing a header and 100 data rows with the columns:

```text
YearsExperience,Salary
```

The terminal prints:

```text
Data saved in file ✅
```

The records are generated practice data, not observations collected from real people.

## Concepts and tools

NumPy arrays, pseudorandom numbers, uniform and normal distributions, calculations across arrays, rounding, pandas DataFrames, CSV export, and paths relative to a Python script.
