# Challenges — Days 1–11

This group contains daily projects that apply the Python concepts covered so far. Work through the challenge groups after `11_exceptions` and before the next numbered course section (`12_...`).

**Status: in progress.** This checkpoint covers day 1: Self-Intro Script Generator.

Navigate through the [challenge index](../README.md) or return to the [main project overview](../../README.md#folder-overview).

## Learning order

1. Read the [original Day 1 challenge](DAY_1.md), then explore [day_1.py](day_1.py).
2. Continue with later days in numerical order as they are added to this group.
3. After this group, continue with `day [12-21]` and the later groups listed in the [challenge index](../README.md#challenge-groups) before returning to the numbered course sections.

The `DAY_*.md` files contain original challenge statements and are maintained manually by the repository owner. Preserve their original wording; keep project explanations and progress in README files.

## Files covered so far

| File | Purpose |
| --- | --- |
| [DAY_1.md](DAY_1.md) | The original Self-Intro Script Generator challenge and its bonus tasks. |
| [day_1.py](day_1.py) | Collecting personal introduction details, building a paragraph, and adding the current date and a star border. |

## Day 1: Self-Intro Script Generator

The task is to ask the user for their name, age, city, profession, and favorite hobby, then turn those answers into a friendly introduction.

The implementation works as follows:

1. `input()` collects each answer, and `.strip()` removes surrounding whitespace.
2. F-strings combine the answers into one introduction paragraph. The age is kept as text because it is used for display.
3. `datetime.date.today().isoformat()` gets the computer's current local date in `YYYY-MM-DD` format.
4. `"*" * 80` creates a border of 80 stars, displayed above and below the introduction.
5. `print()` displays the finished message in the terminal.

The date and decorative border implement both bonus tasks from the original challenge.

For example, enter:

| Prompt topic | Example answer |
| --- | --- |
| Name | Priya |
| Age | 22 |
| City | Jaipur |
| Profession | Software Developer |
| Hobby | playing guitar |

The resulting message is shown below. `YYYY-MM-DD` is a placeholder for the actual date on the computer when the script runs.

```text

********************************************************************************
Hello! my name is Priya, I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!

 Logged on: YYYY-MM-DD
********************************************************************************
```

## How to run this project

Open the repository root in VS Code, select your Python interpreter, and open `day_1.py`. Press **Ctrl + S** to format and run it using the project's editor settings. Click inside the Run on Save terminal, type an answer, and press **Enter** for each of the five prompts.

The save command uses `python -u` with the Python available in that terminal. The script waits for your answers before building the final introduction.

Alternatively, run it from the repository root:

```powershell
python "challenges/day [1-11]/day_1.py"
```

The quoted path includes the folder's spaces and square brackets. This script uses Python's standard library and does not require additional packages.

See the [main README](../../README.md#quick-start) for editor setup and the [folder overview](../../README.md#folder-overview) for the overall learning order.
