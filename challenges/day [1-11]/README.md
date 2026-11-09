# Challenges — Days 1–11

This group contains daily projects that apply the Python concepts covered so far. Work through the challenge groups after `11_exceptions` and before the next numbered course section (`12_...`).

**Status: in progress.** This checkpoint covers days 1–8.

Navigate through the [challenge index](../README.md) or return to the [main project overview](../../README.md#folder-overview).

## Learning order

1. Read the [original Day 1 challenge](DAY_1.md), then explore [day_1.py](day_1.py).
2. Read the [original Day 2 challenge](DAY_2.md), then explore [day_2.py](day_2.py).
3. Read the [original Day 3 challenge](DAY_3.md), then explore [day_3.py](day_3.py).
4. Read the [original Day 4 challenge](DAY_4.md), then explore [day_4.py](day_4.py).
5. Read the [original Day 5 challenge](DAY_5.md), then explore [day_5.py](day_5.py).
6. Read the [original Day 6 challenge](DAY_6.md), then explore [day_6.py](day_6.py).
7. Read the [original Day 7 challenge](DAY_7.md), then explore [day_7.py](day_7.py).
8. Read the [original Day 8 challenge](DAY_8.md), then explore [day_8.py](day_8.py).
9. Continue with later days in numerical order as they are added to this group.
10. After this group, continue with `day [12-21]` and the later groups listed in the [challenge index](../README.md#challenge-groups) before returning to the numbered course sections.

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
| [DAY_4.md](DAY_4.md) | The original Minutes Alive Calculator challenge and its bonus tasks. |
| [day_4.py](day_4.py) | Estimating days, hours, and minutes from an age in years, with an option to calculate again. |
| [DAY_5.md](DAY_5.md) | The original Emoji Enhancer for Messages challenge and its bonus tasks. |
| [day_5.py](day_5.py) | Adding emojis after matching keywords while keeping the original words and their punctuation. |
| [DAY_6.md](DAY_6.md) | The original Daily Learning Journal Logger challenge and its bonus tasks. |
| [day_6.py](day_6.py) | Appending a timestamped learning entry and optional productivity rating to a journal beside the script. |
| `learning_journal.txt` | The journal output created or extended by Day 6 in this folder. |
| [DAY_7.md](DAY_7.md) | The original Terminal-Based Task List Manager challenge and its bonus tasks. |
| [day_7.py](day_7.py) | Adding, viewing, completing, and deleting tasks through a terminal menu, with persistent storage. |
| `tasks.txt` | The task data created or updated by Day 7 in this folder. |
| [DAY_8.md](DAY_8.md) | The original Password Strength Checker & Suggestion Tool challenge and its bonus task. |
| [day_8.py](day_8.py) | Checking password requirements, listing missing conditions, and generating a random suggestion. |

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

## Day 4: Minutes Alive Calculator

The task is to estimate how many days, hours, and minutes a person has been alive from their age in years. The input is converted with `float()`, so fractional ages such as `12.5` are accepted.

`calculate_minutes(age_years)` uses three fixed conversion values: `365.25` days per year, `24` hours per day, and `60` minutes per hour.

1. Multiply the age by `365.25` to obtain the estimated days.
2. Multiply that unrounded result by `24` for hours, then by `60` for minutes.
3. Return a tuple containing each total rounded to the nearest integer with `round()`.
4. Unpack the tuple into `days`, `hours`, and `minutes` for display.

These are approximate totals based on an average year length, rather than an exact birth date calculation.

A `while True` loop lets the user calculate again. The repeat answer is trimmed and converted to lowercase; entering `y` repeats the calculation, and any other answer prints `Good bye!` and exits with `break`.

For an age of `25` followed by `n` at the repeat prompt, the current script displays:

```text

 You are approx:
  -  9131 days old
  -  219150 hours old
  -  13149000 minutes old

Good bye!
```

The script uses a bare `except:` around the loop body. An exception inside that `try` block prints `Please enter a valid number for age`, and the loop asks for an age again.

The repeat-run bonus is implemented. Numbers currently use plain integer formatting; the optional comma separators from the original challenge have not been added.

## Day 5: Emoji Enhancer for Messages

The task is to read a message and add an emoji after each recognized keyword, then display the enhanced message.

The `emoji_map_fun` dictionary maps six keywords to emojis:

| Keyword | Emoji |
| --- | --- |
| `love` | ❤️ |
| `happy` | 😊 |
| `code` | 💻 |
| `tea` | 🍵 |
| `music` | 🎵 |
| `food` | 🍕 |

The implementation works as follows:

1. `input()` reads the message, and `message.split()` separates it into words using whitespace.
2. For each word, `.lower().strip(".,!?")` creates a lookup value in lowercase with the listed punctuation characters removed from both ends.
3. `emoji_map_fun.get(cleaned, "")` looks up the emoji. An unknown keyword returns an empty string instead of raising `KeyError`.
4. If an emoji is found, the script appends the original word followed by the emoji to `updated_words`. Otherwise, it appends the word unchanged.
5. `" ".join(updated_words)` combines the results with single spaces, and `print()` displays the message.

For example, enter:

```text
I love to code and drink tea when I'm Happy.
```

The current script displays:

```text

 Enhanced message:

I love ❤️ to code 💻 and drink tea 🍵 when I'm Happy. 😊
```

Both bonus tasks are implemented for the supported punctuation: matching is case-insensitive, and surrounding periods, commas, exclamation marks, and question marks do not prevent a match. The original spelling, capitalization, and punctuation stay with the word, so an emoji comes after its punctuation, as in `Happy. 😊`. Other punctuation characters are not removed for lookup.

Repeated spaces and tabs in the input become single spaces when the words are joined.

## Day 6: Daily Learning Journal Logger

The task is to record what the user learned today and append it to a text journal with the date and time. An optional productivity rating can be included with each entry.

The implementation works as follows:

1. `input()` collects the learning entry and optional rating, and `.strip()` removes surrounding whitespace. Leave the rating blank to omit it.
2. `datetime.datetime.now()` reads the computer's local date and time. `.strftime("%Y-%m-%d - %I:%M %p")` formats it with a year-month-day date and a 12-hour clock with AM/PM.
3. F-strings build the journal entry. The rating line is added only when the rating is nonempty, and a separator of 50 hyphens divides entries.
4. `Path(__file__).resolve().parent / "learning_journal.txt"` builds the output path from the script's folder. The journal is saved in `challenges/day [1-11]`, even when the script is launched from the repository root.
5. `open(journal_path, "a", encoding="utf-8")` creates the file if needed or appends to an existing journal. The `with` block closes it after writing, then the script prints a confirmation.

For example, enter `Today I learned about Python file paths!` as the learning entry and `4` as the rating. The appended text has this format; `YYYY-MM-DD - HH:MM AM/PM` stands for the actual local timestamp:

```text

 🗓️ YYYY-MM-DD - HH:MM AM/PM
Today I learned about Python file paths!
 Productivity Rating: 4

--------------------------------------------------
```

The terminal confirms that the entry was saved to `learning_journal.txt`. Open that file in this folder to read previous entries; each run adds another entry without replacing earlier content.

The optional rating, confirmation message, and separated entry format implement the bonus tasks. The rating prompt suggests `1–5`, but the current script stores the answer as text without validating that range or adding `/5` automatically.

## Day 7: Terminal-Based Task List Manager

The task is to manage a to-do list from the terminal and keep its contents between runs. Each task is stored in memory as a dictionary with `text` and `done` keys, and the dictionaries are collected in a list.

`task_manager()` loads existing tasks, then uses a `while True` loop and `match` to handle the menu:

| Option | Action |
| --- | --- |
| `1` | Add a task after trimming surrounding whitespace; reject an empty answer. |
| `2` | View numbered tasks, with `✅` for completed tasks and an empty checkbox for unfinished ones. |
| `3` | Mark a selected task as complete and save the updated list. |
| `4` | Remove a selected task with `.pop()` and save the updated list. |
| `5` | Exit the menu with `break`. |

An unrecognized menu choice asks the user to choose a valid option. Before completing or deleting a task, the script converts the task number with `int()`, catches `ValueError` for nonnumeric input, and checks that the number is between `1` and the list length. `num - 1` converts the displayed number to a zero-based list index.

### Loading, displaying, and saving tasks

- `load_tasks()` checks whether `tasks.txt` exists. If it does, each line is split with `.rsplit("||", 1)` into task text and status. Splitting only at the last separator allows `||` inside the task text. The status becomes a Boolean with `status == "done"`. A missing file starts an empty list.
- `display_tasks(tasks)` uses `enumerate(tasks, 1)` to show numbers starting at `1`. An empty list displays `NO tasks found`.
- `save_tasks(tasks)` writes the current list in UTF-8, using one `text||status` record per line. Write mode (`"w"`) replaces the saved list after each addition, completion, or deletion, so removed tasks do not return on the next run.

`TASK_FILE = Path(__file__).resolve().parent / "tasks.txt"` keeps both loading and saving in `challenges/day [1-11]`, beside `day_7.py`, regardless of the terminal's current working directory. The file is created on the first save. Unlike Day 6's journal, this project rewrites its current state rather than appending a history of changes.

For example, starting with an empty list, add `Do homework` and `Learn Python`, then mark task `2` as complete. Choosing **View Tasks** displays:

```text
1. [ ] Do homework
2. [✅] Learn Python
```

The corresponding records in `tasks.txt` are:

```text
Do homework||not_done
Learn Python||done
```

Restarting the script loads these saved tasks and their completion status. Both bonus tasks are implemented: preventing empty tasks and validating task numbers before completion or deletion.

## Day 8: Password Strength Checker and Suggestion Tool

The task is to check a password against five requirements, explain what is missing, and suggest a random password.

### Hidden password input

`getpass.getpass("Enter a password: ")` reads the password without displaying the typed characters. Click inside the terminal, type a practice password, and press **Enter**. No letters or stars appear while typing; the program is still receiving input. This implements the bonus task.

### Checking the password

`check_password_strength(password)` collects unmet requirements in an `issues` list:

| Requirement | Check |
| --- | --- |
| At least 8 characters | `len(password) < 8` identifies a password that is too short. |
| A lowercase letter | `any(c.islower() for c in password)` |
| An uppercase letter | `any(c.isupper() for c in password)` |
| A digit | `any(c.isdigit() for c in password)` |
| A special character | `any(c in string.punctuation for c in password)` |

Each `any()` call returns `True` when at least one character matches. When a check fails, a message is added with `.append()`. Returning an empty list means all five checks passed, and `if not issues` prints the success message. Otherwise, a loop prints every missing requirement.

For the practice input `abc`, the current script displays the following. The last line is a placeholder for the randomly generated suggestion:

```text
You got weak password
- Too short (minimum 8 characters)
- Missing upper case letter
- Missing a digit
- Missing a special character

 suggesting you a strong password
<random 12-character suggestion>
```

### Generating a suggestion

`generate_strong_password(length=12)` combines `string.ascii_letters`, `string.digits`, and `string.punctuation` into a character pool. A generator expression calls `random.choice(chars)` for each position, and `"".join(...)` combines the chosen characters into a string.

The default suggestion has 12 characters and is printed after every check, including when the entered password passes. Choosing from the combined pool does not guarantee that every required character category appears; the current script does not run its suggestion through the checker again.

The script uses only Python's standard library and displays results in the terminal without saving a file.

## How to run these projects

Open the repository root in VS Code, select your Python interpreter, and open the Python file for the day you want to run. Press **Ctrl + S** to format and run it using the project's editor settings. Click inside the Run on Save terminal, type an answer, and press **Enter** for each prompt.

The save command uses `python -u` with the Python available in that terminal. Each script waits for your answers before generating its output.

Alternatively, choose the matching command from the repository root:

```powershell
python "challenges/day [1-11]/day_1.py"
python "challenges/day [1-11]/day_2.py"
python "challenges/day [1-11]/day_3.py"
python "challenges/day [1-11]/day_4.py"
python "challenges/day [1-11]/day_5.py"
python "challenges/day [1-11]/day_6.py"
python "challenges/day [1-11]/day_7.py"
python "challenges/day [1-11]/day_8.py"
```

The quoted paths include the folder's spaces and square brackets. Day 7 uses `match`, which requires Python 3.10 or later. The projects covered so far use Python's standard library or built-in features and do not require additional packages.

See the [main README](../../README.md#quick-start) for editor setup and the [folder overview](../../README.md#folder-overview) for the overall learning order.
