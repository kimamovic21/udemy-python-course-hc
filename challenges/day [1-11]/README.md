# Challenges — Days 1–11

This group contains daily projects that apply the Python concepts covered so far. Work through the challenge groups after `11_exceptions` and before the next numbered course section (`12_...`).

**Status: in progress.** This checkpoint covers days 1–3.

Navigate through the [challenge index](../README.md) or return to the [main project overview](../../README.md#folder-overview).

## Learning order

1. Read the [original Day 1 challenge](DAY_1.md), then explore [day_1.py](day_1.py).
2. Read the [original Day 2 challenge](DAY_2.md), then explore [day_2.py](day_2.py).
3. Read the [original Day 3 challenge](DAY_3.md), then explore [day_3.py](day_3.py).
4. Continue with later days in numerical order as they are added to this group.
5. After this group, continue with `day [12-21]` and the later groups listed in the [challenge index](../README.md#challenge-groups) before returning to the numbered course sections.

The `DAY_*.md` files contain original challenge statements and are maintained manually by the repository owner. Preserve their original wording; keep project explanations and progress in README files.

## Files covered so far

| File | Purpose |
| --- | --- |
| [DAY_1.md](DAY_1.md) | The original Self-Intro Script Generator challenge and its bonus tasks. |
| [day_1.py](day_1.py) | Collecting personal introduction details, building a paragraph, and adding the current date and a star border. |
| [DAY_2.md](DAY_2.md) | The original Stylish Bio Generator for Instagram/Twitter challenge and its bonus tasks. |
| [day_2.py](day_2.py) | Generating a social media bio in one of three layouts and optionally saving its text to a file. |
| [DAY_3.md](DAY_3.md) | The original Simple Bill Splitter challenge and its bonus tasks. |
| [day_3.py](day_3.py) | Collecting group members, reading a bill amount, and displaying each person's rounded share. |

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

## Day 2: Stylish Bio Generator

The task is to collect a name, profession, one-line passion, favorite emoji, and website or handle, then format those details into a social media bio. The emoji and website answers can be left blank.

The script trims surrounding whitespace from those answers with `.strip()`, then asks the user to choose a layout. `generate_bio(style)` selects the matching f-string template:

| Choice | Style | Layout |
| --- | --- | --- |
| `1` | Simple lines | Name and profession on the first line, followed by the passion and website. |
| `2` | Vertical flair | Details on separate lines, with fire emoji accents. |
| `3` | Emoji sandwich | The favorite emoji repeated three times above and below the bio details. |

Use one of the listed style values: `"1"`, `"2"`, or `"3"`.

The returned bio is displayed using `textwrap.dedent()`, which removes indentation shared by nonblank lines. A separate border of 50 stars surrounds the terminal output.

For example, enter:

| Prompt topic | Example answer |
| --- | --- |
| Name | Riya |
| Profession | Designer |
| Passion | Making things beautiful |
| Emoji | 🎨 |
| Website or handle | @riya.design |
| Style | 1 |
| Save to a file | n |

The Simple lines result appears as:

```text
**************************************************
🎨 Riya | Designer
💡 Making things beautiful
 @riya.design
**************************************************
```

### Optional text file output

Answering `y` at the final prompt saves the generated bio with UTF-8 encoding. The answer is converted to lowercase, so `Y` also saves it.

The filename is built from the name by converting it to lowercase, replacing spaces with underscores, and adding `_bio.txt`. For example, `Riya` produces `riya_bio.txt`.

The file is saved in the terminal's current working directory. With the repository-root command shown below, that is the project root. Write mode replaces the contents if the filename already exists. The file stores the generated bio text; the star border is added separately for the terminal display.

Both bonus tasks are implemented: choosing a layout and saving the bio to a text file.

## Day 3: Simple Bill Splitter

The task is to split a bill evenly between friends, displaying both a summary and the amount owed by each named person.

The implementation works as follows:

1. `int(input(...))` reads the group size.
2. A `for` loop collects that many names, trims surrounding whitespace with `.strip()`, and adds each name to a list with `.append()`.
3. `get_float(prompt)` uses a `while True` loop to read the bill amount. It attempts `float(...)`, catches `ValueError`, and asks again until conversion succeeds.
4. `round(total_bill / num_people, 2)` calculates the shared amount and rounds it to two decimal places.
5. The script prints the total, the shared amount, and one line per person, surrounded by borders of 40 stars.

For example, enter:

| Prompt topic | Example answer |
| --- | --- |
| Group size | 3 |
| Person 1 | Aman |
| Person 2 | Neha |
| Person 3 | Ravi |
| Total bill | 1200 |

Expected summary:

```text

****************************************
Total bill: 1200.0
Each person owes 400.0
Aman owes 400.0 rupees
Neha owes 400.0 rupees
Ravi owes 400.0 rupees

****************************************
```

The rounded shares use Python's default float display, so a value can appear as `400.0` rather than `400.00`. Rounding and the decorative summary implement both bonus tasks.

Enter a positive integer for the group size. The retry loop applies to the bill amount; invalid group-size text raises `ValueError`, and a group size of zero causes `ZeroDivisionError` in the current script.

## How to run these projects

Open the repository root in VS Code, select your Python interpreter, and open the Python file for the day you want to run. Press **Ctrl + S** to format and run it using the project's editor settings. Click inside the Run on Save terminal, type an answer, and press **Enter** for each prompt.

The save command uses `python -u` with the Python available in that terminal. Each script waits for your answers before generating its output.

Alternatively, choose the matching command from the repository root:

```powershell
python "challenges/day [1-11]/day_1.py"
python "challenges/day [1-11]/day_2.py"
python "challenges/day [1-11]/day_3.py"
```

The quoted paths include the folder's spaces and square brackets. All three scripts use Python's standard library or built-in features and do not require additional packages.

See the [main README](../../README.md#quick-start) for editor setup and the [folder overview](../../README.md#folder-overview) for the overall learning order.
