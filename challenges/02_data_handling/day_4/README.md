# Day 4: Real-Time Weather Logger

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to fetch weather for a city, save a daily CSV record, and let the user view previous records. The implementation uses OpenWeather's Current Weather API, `requests` for HTTP calls, and `python-dotenv` for local API configuration.

Read the unchanged [original task](DAY_4.md) alongside [day_4.py](day_4.py). Project explanations and updates belong in this README; the original task text is maintained separately.

## Files

| File | Purpose |
| --- | --- |
| [DAY_4.md](DAY_4.md) | The original Real-Time Weather Logger (API + CSV) challenge and its bonus tasks. |
| [day_4.py](day_4.py) | Fetching city weather from OpenWeather and saving one record per city and local date. |
| `weather_logs.csv` | The weather logger's local records; initialized with the existing dataset during reorganization. |
| [.env.example](.env.example) | A shareable template containing the environment variable name and a placeholder key. |
| `.env` | Local API configuration, excluded from Git by the root `.gitignore`. |

## Day 4 setup: OpenWeather and env

1. Install both external packages using the Python interpreter that runs the script:

   ```powershell
   python -m pip install requests python-dotenv
   ```

   The package is installed as `python-dotenv`, but imported as `from dotenv import load_dotenv`. `os`, `csv`, `datetime`, and `pathlib` are part of Python's standard library and need no separate installation.

2. Sign in or create an OpenWeather account, then open the [API keys page](https://home.openweathermap.org/api_keys) to obtain your own key. The page requires sign-in. See the [Current Weather API documentation](https://openweathermap.org/current) for the service used here.

3. Create `.env` inside `challenges/02_data_handling/day_4`, beside `day_4.py`. On a fresh clone, when that local file does not exist, copy the provided template from the repository root:

   ```powershell
   Copy-Item -LiteralPath "challenges/02_data_handling/day_4/.env.example" -Destination "challenges/02_data_handling/day_4/.env"
   ```

   Open `.env` and replace the placeholder with your own key:

   ```dotenv
   OPENWEATHER_API_KEY=your_openweather_api_key_here
   ```

   Keep the filename exactly `.env`, without an added `.txt` extension. If it already contains your key, keep that existing file instead of copying the template again.

4. Run the script again after editing the file:

   ```powershell
   python "challenges/02_data_handling/day_4/day_4.py"
   ```

The code loads the `.env` beside the script, then reads its variable:

```python
load_dotenv(Path(__file__).resolve().parent / ".env")
API_KEY = os.getenv("OPENWEATHER_API_KEY")
```

As described in the [python-dotenv documentation](https://bbc2.github.io/python-dotenv/), variables already set in the environment take precedence by default. The root [.gitignore](../../../.gitignore) excludes `.env` and `.env.*`, while allowing the placeholder-only `.env.example` to be committed. The real key belongs in the local `.env`, rather than Python code or README examples.

## Menu, API call, and CSV storage

- Option `1` calls `log_weather()`. A missing key prints setup instructions. Otherwise, the function reads the city, obtains the computer's local date with `datetime.now()`, and checks the CSV for the same city and date. City comparison is case-insensitive.
- `requests.get(...)` calls OpenWeather with the city, API key, and `units=metric`. `response.json()` converts the JSON response to Python data. The script reads temperature from `data["main"]["temp"]` and condition from `data["weather"][0]["main"]`.
- A successful request appends `Date,City,Temperature,Condition` data to the CSV. Temperatures are in degrees Celsius, and the city is stored using `.title()`.
- Option `2` calls `view_logs()` to display saved rows. A file without records displays `No Entries`.

`weather_logs.csv` is created with its header at startup if missing. Its path uses `Path(__file__).resolve().parent`, so all reads and writes stay beside `day_4.py`, even when the script is launched from the repository root. Existing logs are preserved by append mode.

For example, entering `Sarajevo` could produce the following result. The values are an example; live weather and the local date change:

```text
Logged: 15.95 Clouds in Sarajevo on 2026-11-11
```

The corresponding CSV record is:

```csv
Date,City,Temperature,Condition
2026-11-11,Sarajevo,15.95,Clouds
```

Entering the same city again on the same date prints `Entry for this city and date exists` before another API call is made.

## Troubleshooting and current coverage

| Message or behaviour | What to check |
| --- | --- |
| `No module named 'requests'` or `No module named 'dotenv'` | Run the package-install command above using the same Python interpreter. |
| `Set OPENWEATHER_API_KEY in the .env file before logging weather.` | Check the `.env` location and exact variable name, fill in the key, and restart the script. |
| `API Error` | The service returned a non-200 response. Check the city name and whether the configured key has access to Current Weather. The current message does not display the API's detailed reason. |
| `Failed to make API call` | An exception occurred inside the API/logging block; check connectivity and configuration. The current broad handler does not show the original exception. |
| The menu returns after saving | This is expected: the loop waits for another choice. Use **Ctrl + C** to stop it; no exit option is implemented yet. |

Adding and viewing daily records, duplicate prevention, and basic API-failure feedback are implemented. Average, highest, and lowest temperatures, the most frequent condition, an aligned table, and detailed invalid-city feedback from the original challenge are not implemented yet.

## How to run

From the repository root:

```powershell
python "challenges/02_data_handling/day_4/day_4.py"
```

Or, from this lesson's folder:

```powershell
python .\day_4.py
```

In VS Code, open `day_4.py` and press **Ctrl + S**. For input prompts, click inside the Run on Save terminal, type your answer, and press **Enter**. Exit an older running instance before starting the moved script.

Complete the [setup instructions](#day-4-setup-openweather-and-env) above before running this project.

Input and output paths resolve from this Python file, so data stays in this lesson folder regardless of the terminal's working directory.

## Useful links for beginners

- [Requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/): making HTTP requests and reading JSON responses for Day 4.
- [OpenWeather API keys](https://home.openweathermap.org/api_keys): sign in to manage the key used by Day 4.
- [OpenWeather Current Weather API](https://openweathermap.org/current): city queries, response fields, and metric temperature units.
- [python-dotenv](https://bbc2.github.io/python-dotenv/): installation and loading local environment variables.
- [Date and time format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes): understanding the weather logger's `datetime.now()` and `strftime("%Y-%m-%d")`.
- [Python CSV reading and writing](https://docs.python.org/3/library/csv.html): reading rows and dictionaries, writing records, and handling CSV line endings.
- [Paths with pathlib](https://docs.python.org/3/library/pathlib.html): `Path(__file__).resolve().parent` for keeping input and output beside the script.

[Previous: Day 3](../day_3/README.md) · [Next: Day 5](../day_5/README.md)
