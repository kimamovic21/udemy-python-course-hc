# Daily Challenges

This part of the course puts the earlier Python lessons into practice through daily projects. Use this README as the index for challenge groups. Each group's README explains its learning order and links to project documentation. In `02_data_handling`, each lesson has its own README with explanations, examples, and running instructions.

**Status: in progress.** The first group has local days 1–11, and `02_data_handling` now contains local days 1–10, including weather projects, data conversion, JSON flattening, a credential exercise, and Fernet-encrypted notes. The first group's Day 11 currently implements basic scoring; see its README for remaining challenge features.

## Learning order

1. Work through the numbered lesson folders up to `11_exceptions`.
2. Complete the challenge groups in the order listed below, starting with `01_utilities`, then `02_data_handling`. Within each group, follow its local project numbers.
3. After all challenge groups, continue with the next numbered course section (`12_...`, when added).

Follow this order even if your editor sorts the folders differently.

Project numbering restarts inside `02_data_handling`: its first files are `DAY_1.md` and `day_1.py`. Folder names match the tutorial sections (`01_utilities` and `02_data_handling`); file numbers identify projects within each group. Keep the tutorial's original names and use the group path to distinguish projects with the same filename. Inside `02_data_handling`, each lesson now has a separate `day_1` through `day_10` folder containing its script, original task, and related data. See the [folder layout](02_data_handling/README.md#folder-layout) and each lesson's own README.

## Challenge groups

| Folder | Current coverage | Status |
| --- | --- | --- |
| [01_utilities](01_utilities/README.md) | Local days 1–11 | In progress |
| [02_data_handling](02_data_handling/README.md) | Local days 1–10 | In progress |
| `day [22-31]` | Reserved for later challenges | Planned |
| `day [32-35]` | Reserved for later challenges | Planned |
| `day [36-45]` | Reserved for later challenges | Planned |
| `day [46-52]` | Reserved for later challenges | Planned |

## Projects covered so far

| Group | Local day | Project | Main concepts |
| --- | --- | --- | --- |
| `01_utilities` | 1 | [Self-Intro Script Generator](01_utilities/README.md#day-1-self-intro-script-generator) | `input()`, `.strip()`, f-strings, the current date, and a decorative text border. |
| `01_utilities` | 2 | [Stylish Bio Generator](01_utilities/README.md#day-2-stylish-bio-generator) | Functions, conditional layouts, emojis, `textwrap.dedent()`, and optional UTF-8 text file output. |
| `01_utilities` | 3 | [Simple Bill Splitter](01_utilities/README.md#day-3-simple-bill-splitter) | Lists, loops, numeric conversion, retrying input with `ValueError`, division, and `round()`. |
| `01_utilities` | 4 | [Minutes Alive Calculator](01_utilities/README.md#day-4-minutes-alive-calculator) | Functions, numeric conversion, tuple unpacking, rounding, and repeated calculations. |
| `01_utilities` | 5 | [Emoji Enhancer for Messages](01_utilities/README.md#day-5-emoji-enhancer-for-messages) | Dictionaries, `.get()`, string cleanup, loops, and joining words into an enhanced message. |
| `01_utilities` | 6 | [Daily Learning Journal Logger](01_utilities/README.md#day-6-daily-learning-journal-logger) | Timestamps, optional input, UTF-8 file output, append mode, and paths relative to the script. |
| `01_utilities` | 7 | [Terminal-Based Task List Manager](01_utilities/README.md#day-7-terminal-based-task-list-manager) | Functions, lists of dictionaries, `match`, input validation, and persistent task storage. |
| `01_utilities` | 8 | [Password Strength Checker & Suggestion Tool](01_utilities/README.md#day-8-password-strength-checker-and-suggestion-tool) | Hidden input with `getpass`, character checks with `any()`, and random password suggestions. |
| `01_utilities` | 9 | [Countdown Timer](01_utilities/README.md#day-9-countdown-timer) | Input validation, descending `range()`, `divmod()`, time formatting, and live terminal updates. |
| `01_utilities` | 10 | [Secret Message Encryptor & Decryptor](01_utilities/README.md#day-10-secret-message-encryptor-and-decryptor) | Caesar cipher, functions, character codes with `ord()` and `chr()`, modulo, and integer conversion. |
| `01_utilities` | 11 | [Friendship Compatibility Calculator](01_utilities/README.md#day-11-friendship-compatibility-calculator) | Case normalization, sets, intersections, weighted scoring, and limiting results with `min()`. |
| `02_data_handling` | 1 | [CLI Contact Book (CSV-Powered)](02_data_handling/day_1/README.md) | CSV readers and writers, functions, file persistence, partial search, and duplicate-name checks. |
| `02_data_handling` | 2 | [Student Marks Analyzer](02_data_handling/day_2/README.md) | Dictionaries, numeric input, summary statistics, list comprehensions, and formatted reports. |
| `02_data_handling` | 3 | [Personal Movie Tracker with JSON](02_data_handling/day_3/README.md) | JSON persistence, lists of dictionaries, rating validation, duplicate checks, and title or genre search. |
| `02_data_handling` | 4 | [Real-Time Weather Logger](02_data_handling/day_4/README.md) | HTTP requests, API JSON responses, environment variables, CSV logging, and duplicate checks. |
| `02_data_handling` | 5 | [Weather Data Visualization](02_data_handling/day_5/README.md) | CSV reading, `defaultdict` counts, Matplotlib line plots, and bar charts. |
| `02_data_handling` | 6 | [JSON-to-Excel Converter Tool](02_data_handling/day_6/README.md) | JSON records, CSV headers with `DictWriter`, quoted fields, script-relative paths, and Excel viewing. |
| `02_data_handling` | 7 | [CSV-to-JSON Converter Tool](02_data_handling/day_7/README.md) | CSV dictionaries, JSON output, file paths, previewing records, and preserving text values. |
| `02_data_handling` | 8 | [JSON Flattener](02_data_handling/day_8/README.md) | Recursion, nested dictionaries, list indexes, custom separators, and preserving JSON value types. |
| `02_data_handling` | 9 | [Offline Credential Manager](02_data_handling/day_9/README.md) | Base64 encoding, append-mode storage, decoding, and simple password checks; update and masking remain pending. |
| `02_data_handling` | 10 | [Offline Notes Locker](02_data_handling/day_10/README.md) | Fernet encryption, local key reuse, JSON note storage, timestamps, and title search. |

## Original challenge statements

The `DAY_*.md` files contain the original task descriptions and are maintained manually by the repository owner. Preserve their original wording when working on solutions or documentation. Project explanations, running instructions, and progress belong in README files.

As new days are added, document the project in its lesson README, where applicable, and update the relevant group's overview and this index.

## Running the projects

From the repository root, choose the command for the project you want to run:

```powershell
python "challenges/01_utilities/day_1.py"
python "challenges/01_utilities/day_2.py"
python "challenges/01_utilities/day_3.py"
python "challenges/01_utilities/day_4.py"
python "challenges/01_utilities/day_5.py"
python "challenges/01_utilities/day_6.py"
python "challenges/01_utilities/day_7.py"
python "challenges/01_utilities/day_8.py"
python "challenges/01_utilities/day_9.py"
python "challenges/01_utilities/day_10.py"
python "challenges/01_utilities/day_11.py"
python "challenges/02_data_handling/day_1/day_1.py"
python "challenges/02_data_handling/day_2/day_2.py"
python "challenges/02_data_handling/day_3/day_3.py"
python "challenges/02_data_handling/day_4/day_4.py"
python "challenges/02_data_handling/day_5/day_5.py"
python "challenges/02_data_handling/day_6/day_6.py"
python "challenges/02_data_handling/day_7/day_7.py"
python "challenges/02_data_handling/day_8/day_8.py"
python "challenges/02_data_handling/day_9/day_9.py"
python "challenges/02_data_handling/day_10/day_10.py"
```

Paths are quoted consistently so these commands also work if the repository is stored in a directory with spaces. Answer each prompt in the terminal and press **Enter** to continue.

In VS Code, open the Python file and press **Ctrl + S** to format and run it. Click inside the Run on Save terminal to enter your answers. See the [group README](01_utilities/README.md#how-to-run-these-projects) for detailed examples, including where Days 2, 6, and 7 save their files.

The CSV contact book saves `contacts.csv` beside its script in `02_data_handling/day_1`, regardless of the terminal's current working directory. See the [Day 1 README](02_data_handling/day_1/README.md#how-to-run) for details. The [CSV line-ending note](02_data_handling/day_1/README.md#csv-line-endings-and-the-windows-fix) explains the Windows blank-line issue and the commented original code beside the active fixes.

The movie tracker also saves its data beside its script: `movies.json` is created after the first successful movie addition.

Before running the weather logger, follow the [Day 4 setup instructions](02_data_handling/day_4/README.md#day-4-setup-openweather-and-env): install `requests` and `python-dotenv`, obtain your own OpenWeather key, and configure the local `.env` file. Weather records are saved beside the script in `weather_logs.csv`.

Day 5 needs `matplotlib` and reads its own `day_5/weather_logs.csv`, independent of Day 4's `day_4/weather_logs.csv`. Use the [copy instructions](02_data_handling/day_5/README.md#updating-day-5-from-day-4) to visualize updated logger records. Follow its [setup and running instructions](02_data_handling/day_5/README.md#day-5-setup-and-running) to display both charts. The working CSV currently contains a [30-day Sarajevo demonstration](02_data_handling/day_5/README.md#november-2026-demonstration-dataset), combining past model data, forecasts, and three simulated days. See the [saved chart examples](02_data_handling/day_5/README.md#saved-chart-examples) for both PNG snapshots and explanations.

Day 6 converts the sample `api_data.json` to `converted_data.csv` beside the script. The [Excel and VS Code notes](02_data_handling/day_6/README.md#opening-the-output-in-excel-and-vs-code) explain the separately saved XLSX copy and why CSV fields sometimes need quotes.

Day 7 reads its separate `raw_data.csv` sample and writes `converted_data.json` beside the script, then previews the first three records. CSV values remain strings in the JSON output.

Day 8 in the second group flattens `nested_data.json` into `flattened_data.json` beside the script. Press **Enter** at its separator prompt to use dots, or enter a separator such as `-`.

Day 9 stores Base64-encoded practice credentials in `vault.txt` beside the script. This lesson's `day_9/vault.txt` is ignored by Git and is created locally when the first credential is saved. Base64 is reversible encoding; the current viewer displays the decoded password. See its [current implementation notes](02_data_handling/day_9/README.md#day-9-current-challenge-coverage) for unfinished menu actions and masking.

Day 10 requires `cryptography`; follow the [Notes Locker setup](02_data_handling/day_10/README.md#day-10-setup-and-local-files). It keeps `notes_vault.json` and its local `vault.key` beside the script. The key is ignored by Git and is needed to decrypt previously saved content. This lesson's `day_10/notes_vault.json` is also ignored and is created locally when the first note is saved. The exact-path ignore rules for the two data files do not apply to files with the same names in other folders.

Day 8 in the first group hides password input: type in the terminal and press **Enter**, even though no characters or stars appear.

See the [main README](../README.md#folder-overview) for the overall course structure and [editor setup](../README.md#quick-start).
