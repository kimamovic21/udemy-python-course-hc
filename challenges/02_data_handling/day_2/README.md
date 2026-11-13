# Day 2: Student Marks Analyzer

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to collect student names and marks, then display summary statistics and a detailed report. Marks are numeric scores; the program does not convert them to letter grades or a `1–5` grading scale.

Read the unchanged [original task](DAY_2.md) alongside [day_2.py](day_2.py). Project explanations and updates belong in this README; the original task text is maintained separately.

## Files

| File | Purpose |
| --- | --- |
| [DAY_2.md](DAY_2.md) | The original Student Marks Analyzer challenge and its bonus tasks. |
| [day_2.py](day_2.py) | Collecting student marks and reporting the average, highest and lowest results, and student count. |

## Collecting student data

`collect_student_data()` builds a dictionary whose keys are student names and whose values are their marks:

1. A `while True` loop asks for a name and removes surrounding whitespace with `.strip()`.
2. Entering `done` ends data collection with `break`. The command is case-insensitive, so `DONE` works too.
3. `if name in students` rejects a duplicate name and uses `continue` to ask for another. This comparison is case-sensitive: `Ana` and `ana` are different dictionary keys.
4. `float(input(...))` converts the mark to a number and stores it with `students[name] = marks`. Decimal marks are accepted, although the original task describes integer scores.
5. Invalid numeric text triggers `ValueError` and prints `Please enter a valid number for marks`. That record is not saved, and the loop returns to the name prompt.
6. The function returns the dictionary after data entry is finished.

The current script does not reject empty names or restrict marks to a particular range.

## Calculating and displaying the report

`display_report(students)` first checks for an empty dictionary. If there are no students, it prints `No student data ❌` and returns before attempting calculations.

For a nonempty dictionary:

- `list(students.values())` collects all marks.
- `max()` and `min()` find the highest and lowest marks.
- `sum(marks) / len(marks)` calculates the arithmetic mean; `{average:.2f}` displays it with two decimal places.
- List comprehensions over `students.items()` collect every name tied for the highest or lowest result. `', '.join(...)` formats those names for display.
- `len(students)` gives the student count, and a final loop prints each student's mark in input order.

The two calls at the bottom of the file collect all data first, then display the report. Results stay in memory for that run; this project does not create a data file.

## Example

Enter the following names and marks, then enter `done` at the next name prompt:

| Student | Mark |
| --- | --- |
| Ana | 80 |
| Marko | 90 |
| Sara | 90 |

The resulting report is:

```text

 Students marks report 🗓️
------------------------------
Total students: 3
average marks for students: 86.67
Highest marks : 90.0 by Marko, Sara
lowest marks : 80.0 by Ana
------------------------------
Detailed Marks 🗓️
 - Ana: 80.0
 - Marko: 90.0
 - Sara: 90.0
```

Both top-scoring students appear in the report. The same logic includes all students tied for the lowest mark. Collecting data before reporting, the report-style layout, and duplicate-name prevention implement the bonus tasks; duplicate checking uses the case-sensitive rule described above.

## How to run

From the repository root:

```powershell
python "challenges/02_data_handling/day_2/day_2.py"
```

Or, from this lesson's folder:

```powershell
python .\day_2.py
```

In VS Code, open `day_2.py` and press **Ctrl + S**. For input prompts, click inside the Run on Save terminal, type your answer, and press **Enter**. Exit an older running instance before starting the moved script.

This lesson uses only Python's standard library or built-in features; no package installation is required.

## Useful links for beginners

- [Lists and dictionaries](https://docs.python.org/3/tutorial/datastructures.html): storing student names and marks and iterating over dictionary values and items.
- [Built-in functions](https://docs.python.org/3/library/functions.html): `sum()`, `len()`, `min()`, and `max()` used in the report.

[Previous: Day 1](../day_1/README.md) · [Next: Day 3](../day_3/README.md)
