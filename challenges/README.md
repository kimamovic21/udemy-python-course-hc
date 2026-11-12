# Daily Challenges

This part of the course puts the earlier Python lessons into practice through daily projects. Use this README as the index for challenge groups; each group's README contains the project explanations, examples, and running instructions.

**Status: in progress.** The first group has local days 1–11, and `day [12-21]` now contains local days 1–7, including weather collection and visualization, JSON-to-CSV conversion, and CSV-to-JSON conversion. The first group's Day 11 currently implements basic scoring; see its README for remaining challenge features.

## Learning order

1. Work through the numbered lesson folders up to `11_exceptions`.
2. Complete the challenge groups in the order listed below, starting with `day [1-11]`, then `day [12-21]`. Within each group, follow its local project numbers.
3. After all challenge groups, continue with the next numbered course section (`12_...`, when added).

Follow this order even if your editor sorts the folders differently.

Project numbering restarts inside `day [12-21]`: its first files are `DAY_1.md` and `day_1.py`. Folder names identify the course groups; file numbers identify projects within that group. Keep the tutorial's original names and use the group path to distinguish projects with the same filename.

## Challenge groups

| Folder | Current coverage | Status |
| --- | --- | --- |
| [day 1–11](day%20%5B1-11%5D/README.md) | Local days 1–11 | In progress |
| [day 12–21](day%20%5B12-21%5D/README.md) | Local days 1–7 | In progress |
| `day [22-31]` | Reserved for later challenges | Planned |
| `day [32-35]` | Reserved for later challenges | Planned |
| `day [36-45]` | Reserved for later challenges | Planned |
| `day [46-52]` | Reserved for later challenges | Planned |

## Projects covered so far

| Group | Local day | Project | Main concepts |
| --- | --- | --- | --- |
| `day [1-11]` | 1 | [Self-Intro Script Generator](day%20%5B1-11%5D/README.md#day-1-self-intro-script-generator) | `input()`, `.strip()`, f-strings, the current date, and a decorative text border. |
| `day [1-11]` | 2 | [Stylish Bio Generator](day%20%5B1-11%5D/README.md#day-2-stylish-bio-generator) | Functions, conditional layouts, emojis, `textwrap.dedent()`, and optional UTF-8 text file output. |
| `day [1-11]` | 3 | [Simple Bill Splitter](day%20%5B1-11%5D/README.md#day-3-simple-bill-splitter) | Lists, loops, numeric conversion, retrying input with `ValueError`, division, and `round()`. |
| `day [1-11]` | 4 | [Minutes Alive Calculator](day%20%5B1-11%5D/README.md#day-4-minutes-alive-calculator) | Functions, numeric conversion, tuple unpacking, rounding, and repeated calculations. |
| `day [1-11]` | 5 | [Emoji Enhancer for Messages](day%20%5B1-11%5D/README.md#day-5-emoji-enhancer-for-messages) | Dictionaries, `.get()`, string cleanup, loops, and joining words into an enhanced message. |
| `day [1-11]` | 6 | [Daily Learning Journal Logger](day%20%5B1-11%5D/README.md#day-6-daily-learning-journal-logger) | Timestamps, optional input, UTF-8 file output, append mode, and paths relative to the script. |
| `day [1-11]` | 7 | [Terminal-Based Task List Manager](day%20%5B1-11%5D/README.md#day-7-terminal-based-task-list-manager) | Functions, lists of dictionaries, `match`, input validation, and persistent task storage. |
| `day [1-11]` | 8 | [Password Strength Checker & Suggestion Tool](day%20%5B1-11%5D/README.md#day-8-password-strength-checker-and-suggestion-tool) | Hidden input with `getpass`, character checks with `any()`, and random password suggestions. |
| `day [1-11]` | 9 | [Countdown Timer](day%20%5B1-11%5D/README.md#day-9-countdown-timer) | Input validation, descending `range()`, `divmod()`, time formatting, and live terminal updates. |
| `day [1-11]` | 10 | [Secret Message Encryptor & Decryptor](day%20%5B1-11%5D/README.md#day-10-secret-message-encryptor-and-decryptor) | Caesar cipher, functions, character codes with `ord()` and `chr()`, modulo, and integer conversion. |
| `day [1-11]` | 11 | [Friendship Compatibility Calculator](day%20%5B1-11%5D/README.md#day-11-friendship-compatibility-calculator) | Case normalization, sets, intersections, weighted scoring, and limiting results with `min()`. |
| `day [12-21]` | 1 | [CLI Contact Book (CSV-Powered)](day%20%5B12-21%5D/README.md#day-1-cli-contact-book-csv-powered) | CSV readers and writers, functions, file persistence, partial search, and duplicate-name checks. |
| `day [12-21]` | 2 | [Student Marks Analyzer](day%20%5B12-21%5D/README.md#day-2-student-marks-analyzer) | Dictionaries, numeric input, summary statistics, list comprehensions, and formatted reports. |
| `day [12-21]` | 3 | [Personal Movie Tracker with JSON](day%20%5B12-21%5D/README.md#day-3-personal-movie-tracker-with-json) | JSON persistence, lists of dictionaries, rating validation, duplicate checks, and title or genre search. |
| `day [12-21]` | 4 | [Real-Time Weather Logger](day%20%5B12-21%5D/README.md#day-4-real-time-weather-logger) | HTTP requests, API JSON responses, environment variables, CSV logging, and duplicate checks. |
| `day [12-21]` | 5 | [Weather Data Visualization](day%20%5B12-21%5D/README.md#day-5-weather-data-visualization) | CSV reading, `defaultdict` counts, Matplotlib line plots, and bar charts. |
| `day [12-21]` | 6 | [JSON-to-Excel Converter Tool](day%20%5B12-21%5D/README.md#day-6-json-to-excel-converter-tool) | JSON records, CSV headers with `DictWriter`, quoted fields, script-relative paths, and Excel viewing. |
| `day [12-21]` | 7 | [CSV-to-JSON Converter Tool](day%20%5B12-21%5D/README.md#day-7-csv-to-json-converter-tool) | CSV dictionaries, JSON output, file paths, previewing records, and preserving text values. |

## Original challenge statements

The `DAY_*.md` files contain the original task descriptions and are maintained manually by the repository owner. Preserve their original wording when working on solutions or documentation. Project explanations, running instructions, and progress belong in README files.

As new days are added, update the relevant group's README and this index to reflect the actual content.

## Running the projects

From the repository root, choose the command for the project you want to run:

```powershell
python "challenges/day [1-11]/day_1.py"
python "challenges/day [1-11]/day_2.py"
python "challenges/day [1-11]/day_3.py"
python "challenges/day [1-11]/day_4.py"
python "challenges/day [1-11]/day_5.py"
python "challenges/day [1-11]/day_6.py"
python "challenges/day [1-11]/day_7.py"
python "challenges/day [1-11]/day_8.py"
python "challenges/day [1-11]/day_9.py"
python "challenges/day [1-11]/day_10.py"
python "challenges/day [1-11]/day_11.py"
python "challenges/day [12-21]/day_1.py"
python "challenges/day [12-21]/day_2.py"
python "challenges/day [12-21]/day_3.py"
python "challenges/day [12-21]/day_4.py"
python "challenges/day [12-21]/day_5.py"
python "challenges/day [12-21]/day_6.py"
python "challenges/day [12-21]/day_7.py"
```

The quotes keep the path's spaces and square brackets together. Answer each prompt in the terminal and press **Enter** to continue.

In VS Code, open the Python file and press **Ctrl + S** to format and run it. Click inside the Run on Save terminal to enter your answers. See the [group README](day%20%5B1-11%5D/README.md#how-to-run-these-projects) for detailed examples, including where Days 2, 6, and 7 save their files.

The CSV contact book saves `contacts.csv` beside its script in `day [12-21]`, regardless of the terminal's current working directory. See its [group README](day%20%5B12-21%5D/README.md#how-to-run-these-projects) for details. The [CSV line-ending note](day%20%5B12-21%5D/README.md#csv-line-endings-and-the-windows-fix) explains the Windows blank-line issue and the commented original code beside the active fixes.

The movie tracker also saves its data beside its script: `movies.json` is created after the first successful movie addition.

Before running the weather logger, follow the [Day 4 setup instructions](day%20%5B12-21%5D/README.md#day-4-setup-openweather-and-env): install `requests` and `python-dotenv`, obtain your own OpenWeather key, and configure the local `.env` file. Weather records are saved beside the script in `weather_logs.csv`.

Day 5 needs `matplotlib` and reads `weather_logs.csv` beside its script, using the same file as Day 4 regardless of the terminal's working directory. Follow its [setup and running instructions](day%20%5B12-21%5D/README.md#day-5-setup-and-running) to display both charts. The working CSV currently contains a [30-day Sarajevo demonstration](day%20%5B12-21%5D/README.md#november-2026-demonstration-dataset), combining past model data, forecasts, and three simulated days. See the [saved chart examples](day%20%5B12-21%5D/README.md#saved-chart-examples) for both PNG snapshots and explanations.

Day 6 converts the sample `api_data.json` to `converted_data.csv` beside the script. The [Excel and VS Code notes](day%20%5B12-21%5D/README.md#opening-the-output-in-excel-and-vs-code) explain the separately saved XLSX copy and why CSV fields sometimes need quotes.

Day 7 reads its separate `raw_data.csv` sample and writes `converted_data.json` beside the script, then previews the first three records. CSV values remain strings in the JSON output.

Day 8 in the first group hides password input: type in the terminal and press **Enter**, even though no characters or stars appear.

See the [main README](../README.md#folder-overview) for the overall course structure and [editor setup](../README.md#quick-start).
