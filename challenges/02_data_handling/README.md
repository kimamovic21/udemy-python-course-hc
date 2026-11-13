# Challenges — Data Handling

This group corresponds to `02_data_handling` in the Udemy tutorial. It is the second challenge group, after [01_utilities](../01_utilities/README.md). Each lesson has its own README with the problem, implementation, files, setup, examples, and useful links.

**Status: in progress.** Local days 1–10 are documented; individual READMEs identify unfinished features. Continue through the later groups in the [challenge index](../README.md#challenge-groups) before returning to section `12_...`.

[Challenge index](../README.md) · [Main project overview](../../README.md#folder-overview)

## Learning order and file numbering

Follow the table from `day_1` to `day_10`, even if the Explorer sorts `day_10` near `day_1`. The tutorial restarts local numbering in this course group; the original filenames remain `DAY_N.md` and `day_N.py` inside each lesson folder.

The `DAY_*.md` files contain original task statements maintained manually by the repository owner. Their content stays unchanged; documentation belongs in README files.

## Folder layout

| Lesson guide | Project | Overview |
| --- | --- | --- |
| [day_1](day_1/README.md) | CLI Contact Book (CSV-Powered) | Add, list, and search contacts stored in CSV. |
| [day_2](day_2/README.md) | Student Marks Analyzer | Collect student marks and report summary statistics. |
| [day_3](day_3/README.md) | Personal Movie Tracker with JSON | Maintain a searchable movie collection in JSON. |
| [day_4](day_4/README.md) | Real-Time Weather Logger | Fetch OpenWeather data and save daily CSV records. |
| [day_5](day_5/README.md) | Weather Data Visualization | Plot temperatures and condition counts from a local CSV. |
| [day_6](day_6/README.md) | JSON-to-Excel Converter Tool | Convert JSON records to CSV for Excel. |
| [day_7](day_7/README.md) | CSV-to-JSON Converter Tool | Convert CSV rows to JSON records. |
| [day_8](day_8/README.md) | JSON Flattener | Flatten nested dictionaries and lists using recursion. |
| [day_9](day_9/README.md) | Offline Credential Manager | Practice Base64 storage and listing of credentials. |
| [day_10](day_10/README.md) | Offline Notes Locker | Encrypt note content with Fernet and search note titles. |

Each folder keeps its own script, original task, supporting files, and README. Relevant package references and examples are documented with the project that uses them.

## How to run these projects

Open a lesson's README and use its command from the repository root. For example:

```powershell
python "challenges/02_data_handling/day_1/day_1.py"
```

Or open its Python file in VS Code and press **Ctrl + S**. File paths resolve from the script, keeping input and output inside the corresponding lesson folder. See the [main setup guide](../../README.md#quick-start) for editor configuration.

Extra setup is required for [Day 4: OpenWeather, requests, and .env](day_4/README.md#day-4-setup-openweather-and-env), [Day 5: Matplotlib](day_5/README.md#day-5-setup-and-running), and [Day 10: cryptography](day_10/README.md#day-10-setup-and-local-files). Other lessons in this group use Python's standard library or built-in features.

## Data files and weather workflow

Data belongs to its lesson: contacts in `day_1`, movies in `day_3`, API configuration and logs in `day_4`, and converter inputs/outputs in `day_6`–`day_8`. Credential and note files stay in `day_9` and `day_10`. The local `.env` and `vault.key` are ignored by Git. Exact-path rules also exclude this group's `day_9/vault.txt` and `day_10/notes_vault.json`, leaving files with the same names in other folders unaffected by those two rules. The scripts create these data files when the first credential or note is saved; see the corresponding lesson README for details.

Day 4 and Day 5 have separate `weather_logs.csv` files. Copy newer logger records explicitly using the [Day 5 instructions](day_5/README.md#updating-day-5-from-day-4). Its README also explains the [November demonstration data](day_5/README.md#november-2026-demonstration-dataset) and displays the [saved chart examples](day_5/README.md#saved-chart-examples).
