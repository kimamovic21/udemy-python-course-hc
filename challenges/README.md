# Daily Challenges

This part of the course puts the earlier Python lessons into practice through daily projects. Use this README as the index for challenge groups. Each group's README explains its learning order and links to project documentation. In `02_data_handling`, `03_web_scraping`, `04_automation`, and `05_data_science`, each added lesson has its own folder and README.

**Status: in progress.** The first group has local days 1–11, `02_data_handling` and `03_web_scraping` have local days 1–10 documented, and `04_automation` has local days 1–4 documented. The current section is [05_data_science](05_data_science/README.md), with notebooks, dataset generation, regression, and a Streamlit app in local days 1–4. Individual project guides describe remaining challenge features.

## Learning order

1. Work through the numbered lesson folders up to `11_exceptions`.
2. Complete the challenge groups in order: `01_utilities`, `02_data_handling`, `03_web_scraping`, `04_automation`, then `05_data_science`. Within each group, follow its local project numbers.
3. After all challenge groups, continue with the next numbered course section (`12_...`, when added).

Follow this order even if your editor sorts the folders differently.

Project numbering restarts within each group. Folder names match the tutorial sections, and local file numbers identify projects within each group. Use the group path to distinguish projects with the same filename. Inside `02_data_handling` and `03_web_scraping`, each lesson has a separate `day_1` through `day_10` folder. Automation and Data Science follow the same layout. Data Science Day 1 is in `05_data_science/day_1`, containing `day_1.ipynb`, `DAY_1.md`, and its own README. Use folder and file numbers without leading zeros.

## Challenge groups

| Folder | Current coverage | Status |
| --- | --- | --- |
| [01_utilities](01_utilities/README.md) | Local days 1–11 | In progress |
| [02_data_handling](02_data_handling/README.md) | Local days 1–10 | In progress |
| [03_web_scraping](03_web_scraping/README.md) | Local days 1–10: extraction, exports, images, APIs, SQLite, and PDFs | In progress |
| [04_automation](04_automation/README.md) | Local days 1–4: file organization, renaming, Downloads monitoring, and system resources | In progress |
| [05_data_science](05_data_science/README.md) | Local days 1–4: notebooks, dataset generation, regression, and a Streamlit app | In progress — current section |

Further challenge groups will be added as the course progresses.

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
| `03_web_scraping` | 1 | [Scrape Wikipedia h2 Headers](03_web_scraping/day_1/README.md) | Requests, HTTP error handling, HTML parsing with Beautiful Soup, and extracting heading text into a list. |
| `03_web_scraping` | 2 | [Hacker News Top Posts Scraper](03_web_scraping/day_2/README.md) | CSS selectors, extracting titles and URLs, CSV export, and paths relative to the script. |
| `03_web_scraping` | 3 | [Scrape Books to Scrape (70 Books)](03_web_scraping/day_3/README.md) | Pagination, `urljoin()`, extracting titles and prices, list slicing, and JSON output. |
| `03_web_scraping` | 4 | [Download Cover Images of the First 10 Books](03_web_scraping/day_4/README.md) | Relative image URLs, filename cleanup, streamed downloads, and binary image output. |
| `03_web_scraping` | 5 | [Download Cover Images Using wget](03_web_scraping/day_5/README.md) | External package installation, download progress, numbered duplicates, and local image storage. |
| `03_web_scraping` | 6 | [Quote of the Day Image Maker](03_web_scraping/day_6/README.md) | Quote and author extraction, tuples, text wrapping, Pillow drawing, and local PNG output. |
| `03_web_scraping` | 7 | [Crypto Price Tracker with Graphs](03_web_scraping/day_7/README.md) | CoinGecko API JSON, timestamped CSV history, coin selection, and Matplotlib line graphs. |
| `03_web_scraping` | 8 | [Hourly Crypto Price Logger](03_web_scraping/day_8/README.md) | schedule jobs, polling intervals, hourly API fetching, and a separate CSV history. |
| `03_web_scraping` | 9 | [Store and Search Crypto Prices in SQLite](03_web_scraping/day_9/README.md) | SQLite tables, timestamped inserts, parameterized queries, and latest-price search. |
| `03_web_scraping` | 10 | [Extract Text from a PDF](03_web_scraping/day_10/README.md) | PyMuPDF, page iteration, text extraction, string accumulation, and error handling. |
| `04_automation` | 1 | [File Organizer](04_automation/day_1/README.md) | `os`, `shutil`, extension matching, folder creation, and moving files beside the script while skipping project files and existing folders. |
| `04_automation` | 2 | [Batch Rename Files in a Folder](04_automation/day_2/README.md) | Extension filtering, sorting, `enumerate()`, filename checks, a preview, confirmation, and renaming within the lesson folder. |
| `04_automation` | 3 | [Auto File Organizer with Watchdog](04_automation/day_3/README.md) | Filesystem events, observers, temporary-download filtering, stability checks, retries, and sorting files in Downloads. |
| `04_automation` | 4 | [Real-Time System Resource Monitor](04_automation/day_4/README.md) | psutil, CPU/RAM/disk statistics, byte conversion, terminal refreshes, timing, and `KeyboardInterrupt`. |
| `05_data_science` | 1 | [Introduction to Python Notebooks](05_data_science/day_1/README.md#day-1-explained) | Jupyter, Markdown and code cells, kernels, `print()`, `for`, `range()`, and f-strings. |
| `05_data_science` | 2 | [Generate an Experience and Salary Dataset](05_data_science/day_2/README.md) | NumPy arrays, seeded random values, vectorized calculations, pandas DataFrames, and CSV export. |
| `05_data_science` | 3 | [Salary Prediction with Linear Regression](05_data_science/day_3/README.md) | CSV input, features and targets, scikit-learn fitting/prediction, coefficients, and Matplotlib visualization. |
| `05_data_science` | 4 | [Interactive Salary Predictor with Streamlit](05_data_science/day_4/README.md) | Local web server, numeric input, regression predictions, and embedded Matplotlib charts. |

## Original challenge statements

The `DAY_*.md` files contain task descriptions maintained manually by the repository owner. Preserve original course wording where supplied. Web scraping Day 10 and Data Science Days 1–4 have marked, locally authored descriptions based on their supplied code, created at the owner's request because original statements were absent. Keep task files unchanged during later documentation updates; project explanations, running instructions, and progress belong in README files.

As new days are added, document the project in its lesson README, where applicable, and update the relevant group's overview and this index.

## Running the projects

For regular Python scripts, choose a command below and run it from the repository root. Data Science Day 1 uses notebook cells, and Day 4 uses the Streamlit runner; follow their separate instructions below.

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
python "challenges/03_web_scraping/day_1/day_1.py"
python "challenges/03_web_scraping/day_2/day_2.py"
python "challenges/03_web_scraping/day_3/day_3.py"
python "challenges/03_web_scraping/day_4/day_4.py"
python "challenges/03_web_scraping/day_5/day_5.py"
python "challenges/03_web_scraping/day_6/day_6.py"
python "challenges/03_web_scraping/day_7/day_7.py"
python "challenges/03_web_scraping/day_8/day_8.py"
python "challenges/03_web_scraping/day_9/day_9.py"
python "challenges/03_web_scraping/day_10/day_10.py"
python "challenges/04_automation/day_1/day_1.py"
python "challenges/04_automation/day_2/day_2.py"
python "challenges/04_automation/day_3/day_3.py"
python "challenges/04_automation/day_4/day_4.py"
python "challenges/05_data_science/day_2/day_2.py"
python "challenges/05_data_science/day_3/day_3.py"
```

Paths are quoted consistently so these commands also work if the repository is stored in a directory with spaces. Answer each prompt in the terminal and press **Enter** to continue.

In VS Code, open the Python file and press **Ctrl + S** to format and run it. Click inside the Run on Save terminal to enter your answers. See the [group README](01_utilities/README.md#how-to-run-these-projects) for detailed examples, including where Days 2, 6, and 7 save their files.

Automation Day 1 uses only Python's standard library and runs without an input prompt. It organizes sample files directly beside `04_automation/day_1/day_1.py` into `PDFs`, `Images`, `TextFiles`, and `Others`. It skips its script, `DAY_1.md`, `README.md`, and existing folders. The repository root is unaffected when launched from there. See the [Day 1 guide](04_automation/day_1/README.md) for the path adjustment and original tutorial code.

Automation Day 2 renames matching files only in `04_automation/day_2/images`, regardless of the terminal's current directory. Create this Git-ignored folder and add your practice images before running. Enter a base name and matching extension including the dot, review the preview, and confirm with `y`. It skips nested folders and checks for existing destination names. The [Day 2 guide](04_automation/day_2/README.md) shows how three house photos become `house_1.jpg`, `house_2.jpg`, and `house_3.jpg` and explains that undo is not implemented.

Automation Day 3 requires `watchdog` and watches the user's Downloads folder, rather than the lesson folder. New JPG/PNG images go to `Images`, PDFs to `PDFs`, and other completed files to `Others`. Common temporary downloads are skipped, and files are checked for stability before moving. Keep the process running and stop it with **Ctrl + C** before restarting. The [Day 3 guide](04_automation/day_3/README.md) includes installation, the original tutorial code, the Chrome download fix, limitations, and links to the official Watchdog documentation and GitHub repository.

Automation Day 4 requires `psutil` and displays CPU, RAM, and disk space usage in a terminal dashboard. It refreshes approximately every four seconds and creates no output files. Stop it with **Ctrl + C**. The [Day 4 guide](04_automation/day_4/README.md) includes installation, reading explanations, package links, and the remaining CPU/RAM warning requirement.

Data Science Day 1 uses [day_1.ipynb](05_data_science/day_1/day_1.ipynb). Open it in Jupyter Notebook, JupyterLab, or VS Code's notebook editor, select a Python kernel, and run cells with **Shift + Enter** or **Run All**. **Ctrl + S** saves the notebook; the existing `.py` Run on Save configuration does not execute its cells. The [Day 1 guide](05_data_science/day_1/README.md) explains setup, outputs, and the roles of [Anaconda](https://www.anaconda.com/download) and [Project Jupyter](https://jupyter.org/).

Data Science Day 2 uses [NumPy](https://numpy.org/) to generate 100 synthetic experience/salary records and [pandas](https://pandas.pydata.org/) to export them to `05_data_science/day_2/experience_salary.csv`. Each run replaces that file. The [Day 2 guide](05_data_science/day_2/README.md) includes installation, pandas import troubleshooting, the calculations, and official GitHub repositories.

Data Science Day 3 reads Day 2's CSV directly and fits a `LinearRegression` model using [scikit-learn](https://scikit-learn.org/stable/). It prints the fitted slope/intercept and displays data points and predictions with Matplotlib. It does not change the input CSV or automatically save output files. The [Day 3 guide](05_data_science/day_3/README.md) includes installation, the input dependency, code fixes, model explanations, and the official GitHub repository.

The manually saved [Day 3 chart example](05_data_science/day_3/README.md#saved-chart-example) shows the synthetic salary records and their fitted regression line.

Data Science Day 4 uses [Streamlit](https://streamlit.io/) to turn the same regression model into a local browser app. It reads Day 2's CSV, accepts years of experience, displays a formatted estimate, and embeds a chart. After installing its dependencies, start it from the repository root with:

```powershell
python -m streamlit run "challenges/05_data_science/day_4/day_4.py" --server.runOnSave true
```

Open the Local URL printed in the terminal. In VS Code, saving `day_4.py` starts a dedicated Streamlit task; later saves reuse that task and rerun the app. This replaces ordinary `python -u` execution for this file only. Stop the server with **Ctrl + C** in its task terminal. The [Day 4 guide](05_data_science/day_4/README.md) contains installation and troubleshooting details.

The CSV contact book saves `contacts.csv` beside its script in `02_data_handling/day_1`, regardless of the terminal's current working directory. See the [Day 1 README](02_data_handling/day_1/README.md#how-to-run) for details. The [CSV line-ending note](02_data_handling/day_1/README.md#csv-line-endings-and-the-windows-fix) explains the Windows blank-line issue and the commented original code beside the active fixes.

The movie tracker also saves its data beside its script: `movies.json` is created after the first successful movie addition.

Before running the weather logger, follow the [Day 4 setup instructions](02_data_handling/day_4/README.md#day-4-setup-openweather-and-env): install `requests` and `python-dotenv`, obtain your own OpenWeather key, and configure the local `.env` file. Weather records are saved beside the script in `weather_logs.csv`.

Day 5 needs `matplotlib` and reads its own `day_5/weather_logs.csv`, independent of Day 4's `day_4/weather_logs.csv`. Use the [copy instructions](02_data_handling/day_5/README.md#updating-day-5-from-day-4) to visualize updated logger records. Follow its [setup and running instructions](02_data_handling/day_5/README.md#day-5-setup-and-running) to display both charts. The working CSV currently contains a [30-day Sarajevo demonstration](02_data_handling/day_5/README.md#november-2026-demonstration-dataset), combining past model data, forecasts, and three simulated days. See the [saved chart examples](02_data_handling/day_5/README.md#saved-chart-examples) for both PNG snapshots and explanations.

Day 6 converts the sample `api_data.json` to `converted_data.csv` beside the script. The [Excel and VS Code notes](02_data_handling/day_6/README.md#opening-the-output-in-excel-and-vs-code) explain the separately saved XLSX copy and why CSV fields sometimes need quotes.

Day 7 reads its separate `raw_data.csv` sample and writes `converted_data.json` beside the script, then previews the first three records. CSV values remain strings in the JSON output.

Day 8 in the second group flattens `nested_data.json` into `flattened_data.json` beside the script. Press **Enter** at its separator prompt to use dots, or enter a separator such as `-`.

Day 9 stores Base64-encoded practice credentials in `vault.txt` beside the script. This lesson's `day_9/vault.txt` is ignored by Git and is created locally when the first credential is saved. Base64 is reversible encoding; the current viewer displays the decoded password. See its [current implementation notes](02_data_handling/day_9/README.md#day-9-current-challenge-coverage) for unfinished menu actions and masking.

Day 10 requires `cryptography`; follow the [Notes Locker setup](02_data_handling/day_10/README.md#day-10-setup-and-local-files). It keeps `notes_vault.json` and its local `vault.key` beside the script. The key is ignored by Git and is needed to decrypt previously saved content. This lesson's `day_10/notes_vault.json` is also ignored and is created locally when the first note is saved. The exact-path ignore rules for the two data files do not apply to files with the same names in other folders.

Web scraping Day 1 requires `requests` and `beautifulsoup4` (imported as `bs4`). Follow its [setup instructions](03_web_scraping/day_1/README.md#setup) before running it. It downloads the Wikipedia page and prints headings without creating local data files; see its [current challenge coverage](03_web_scraping/day_1/README.md#current-challenge-coverage) for remaining requirements.

Web scraping Day 2 reads the [Hacker News homepage](https://news.ycombinator.com/) and saves up to 20 titles and URLs to `03_web_scraping/day_2/hn_top20.csv`. It uses the same external packages as Day 1; follow its [Day 2 guide](03_web_scraping/day_2/README.md) for the exact `day_2.py` filename, output location, and CSV behaviour.

Web scraping Day 3 collects up to 70 titles and prices from [Books to Scrape](https://books.toscrape.com/) by following next-page links. Its `03_web_scraping/day_3/books_data.json` output stays beside the script, including when launched from the repository root. See the [Day 3 guide](03_web_scraping/day_3/README.md#json-output-and-current-file-location) for the output path and running instructions.

Web scraping Day 4 reads the first 10 book listings from the [Books to Scrape homepage](https://books.toscrape.com/) and attempts to download their covers. Images are saved in `03_web_scraping/day_4/images/` with cleaned book-title filenames. The [Day 4 guide](03_web_scraping/day_4/README.md) explains streaming, binary writes, and the current download-error messages.

Web scraping Day 5 adds the Python [wget package](https://pypi.org/project/wget/) to download the first 10 book covers into its own Git-ignored `03_web_scraping/day_5/images/` folder. Follow its [setup instructions](03_web_scraping/day_5/README.md#setup) and [Day 4 comparison](03_web_scraping/day_5/README.md#difference-from-day-4), including the numbered copies created on repeated runs.

Web scraping Day 6 uses [Quotes to Scrape](https://quotes.toscrape.com/) and [Pillow](https://pypi.org/project/Pillow/) to create a PNG card for each of the first five quotes and authors. Images stay in the Git-ignored `03_web_scraping/day_6/quotes/` folder; repeated runs overwrite the same numbered files. See the [Day 6 setup](03_web_scraping/day_6/README.md#setup) and [image-making walkthrough](03_web_scraping/day_6/README.md#how-the-code-works).

Web scraping Day 7 uses the [CoinGecko](https://www.coingecko.com/) JSON API and appends timestamped prices to `03_web_scraping/day_7/crypto_prices.csv`. Enter a printed coin ID to plot its saved history with Matplotlib, or submit an empty value to finish. The [Day 7 guide](03_web_scraping/day_7/README.md) explains dependencies, API-access limitations, append behaviour, and the CSV location.

Web scraping Day 8 uses [schedule](https://schedule.readthedocs.io/en/stable/) to log CoinGecko prices hourly to `03_web_scraping/day_8/crypto_prices.csv`. It waits for the next hour before its first fetch, creates its own CSV when saving first runs, and does not require Day 7's file. Follow the [Day 8 guide](03_web_scraping/day_8/README.md) for installation, the difference between scheduling and `time.sleep()`, and stopping the running process.

Web scraping Day 9 stores CoinGecko records in `03_web_scraping/day_9/crypto.db`. Choose `1` to fetch and store, or run again and choose `2` to search a saved coin ID. It currently runs on demand rather than hourly. The [Day 9 guide](03_web_scraping/day_9/README.md) explains the schema and how to open the binary database with [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer).

Web scraping Day 10 uses `pymupdf` to read the included two-page `03_web_scraping/day_10/test.pdf`. The input path is relative to the script, so running from the repository root also works. The [Day 10 guide](03_web_scraping/day_10/README.md) preserves the original tutorial code and explains modern imports, file paths, and error messages. Replace the sample with another text-based PDF under the same name to try it. The script prints text without creating an output file.

Day 8 in the first group hides password input: type in the terminal and press **Enter**, even though no characters or stars appear.

See the [main README](../README.md#folder-overview) for the overall course structure and [editor setup](../README.md#quick-start).

## Package source repositories

The [project-wide package index](../README.md#package-source-repositories) maps the imported packages to their upstream projects. It includes GitHub links for starring, labels the Beautiful Soup and wget exceptions, and explains where Python's standard-library code lives. Each relevant lesson README lists its own package sources.
