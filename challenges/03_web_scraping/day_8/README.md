# Day 8: Hourly Crypto Price Logger

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to automate Day 7's CoinGecko logging. The Python [schedule library](https://schedule.readthedocs.io/en/stable/) runs a job at the beginning of every hour, fetching prices and appending timestamped records to this lesson's own CSV.

## Files and relationship to Day 7

| File | Purpose |
| --- | --- |
| [DAY_8.md](DAY_8.md) | The original lesson note, maintained manually and left unchanged. |
| [day_8.py](day_8.py) | Scheduling requests and appending price records. |
| `crypto_prices.csv` | Runtime history created in this lesson folder when saving first runs. |

Day 8 builds on Day 7's concepts but **does not require Day 7's CSV or Python file**. It fetches fresh data independently and uses `day_8/crypto_prices.csv`. It has no graph prompt or Matplotlib dependency.

## Setup

Install the external packages using the Python interpreter that runs the script:

```powershell
python -m pip install requests schedule
```

If Requests is already installed in that interpreter, only the additional package is needed:

```powershell
python -m pip install schedule
```

The `os`, `csv`, `pathlib`, `datetime`, and `time` modules come with Python. For `ModuleNotFoundError: No module named 'schedule'`, install the package in the interpreter selected through **Python: Select Interpreter** in VS Code. Verify the import with:

```powershell
python -c "import schedule; print('schedule import OK')"
```

The current script sends no API key and does not load an `.env` file. See the [Day 7 API-access notes](../day_7/README.md#coingecko-api-access) and [CoinGecko authentication guide](https://docs.coingecko.com/demo/reference/authentication) if the service requires authentication for your request.

## How the code works

1. `fetch_crypto_data()` requests CoinGecko's `/coins/markets` endpoint and decodes its JSON. Parameters request up to 10 coins ordered by descending market capitalization, with prices in USD.
2. `save_to_csv(data)` writes a header for a new file, creates one local timestamp for the batch, and appends each coin's `id` and `current_price`.
3. `job()` prints `Fetching data hourly...`, fetches the data, and passes it to the CSV writer.
4. `schedule.every().hour.at(":00").do(job)` registers the function for minute zero of each hour. Passing `job` registers it; this statement does not immediately call `job()`.
5. The infinite loop calls `schedule.run_pending()` to run due jobs, then `time.sleep(60)` pauses before the next check.

The scheduler uses the computer's local time. The script must remain running; it does not install an operating-system task or service.

## First run and polling frequency

There is **no immediate fetch at startup**. A quiet terminal and no CSV before the first scheduled save are expected.

For example, starting at **16:11** schedules the next job for **17:00**, followed by **18:00**, **19:00**, and so on. It runs when the loop next checks for due work, so with a 60-second pause it can normally start up to roughly a minute after the hour. Network calls can add further delay.

| Loop pause | What changes | Fetch schedule |
| --- | --- | --- |
| `time.sleep(60)` | Check for due work approximately once a minute. | Beginning of every hour. |
| `time.sleep(1)` | Check for due work approximately once a second. | Still the beginning of every hour. |

The sleep duration controls polling frequency, not how often prices are requested. The current file uses `time.sleep(60)`.

An immediate first fetch would require a separate `job()` call, which the current code does not include. Stopping before the first scheduled job means no CSV is created through that job.

## CSV creation, location, and history

```python
CSV_FILE = Path(__file__).resolve().parent / "crypto_prices.csv"
```

The output is always:

```text
challenges/03_web_scraping/day_8/crypto_prices.csv
```

No CSV needs to exist beforehand. When the first job reaches `save_to_csv()`, opening a missing file creates it and writes the `timestamp,coin,price` header. A normal successful response then adds up to 10 rows.

Later jobs open the same file with mode `"a"` and `newline=""`, preserving history and adding new batches. With 10 coins per job, two completed batches produce 20 data rows plus the header. There is no duplicate check.

Timestamps use local time formatted as `%Y-%m-%d %H-%M-%S`. The CSV is independent of Day 7's history and any older root copy with the same name. Its location stays beside the script, including when launched from the repository root or via **Ctrl + S**.

## How to run and stop

From the repository root:

```powershell
python "challenges/03_web_scraping/day_8/day_8.py"
```

Or, from this lesson's folder:

```powershell
python .\day_8.py
```

In VS Code, open `day_8.py` and press **Ctrl + S**. There are no input prompts; the terminal may remain silent until the first scheduled fetch. Keep the process running and the computer awake for jobs to execute.

Stop it with **Ctrl + C** in its terminal. Before saving to run a changed version, stop the previous instance so multiple schedulers do not write to the same CSV. Code changes affect the next launched process, not one already running.

## Current behaviour to understand

- Scheduling and the infinite loop are at module level, with no main guard. Importing this file also starts the loop; use the direct run command rather than importing it for experimentation.
- There is no explicit request timeout, HTTP status check, response validation, or exception handler. An API, network, or file error can terminate the loop.
- An error before saving means no new CSV. An invalid response during saving can leave a header-only or partially written file.
- The header check tests existence only. An already existing empty CSV does not automatically receive a header.
- Jobs do not run while the process is stopped. Missed hourly observations are not reconstructed from historical API data.
- This version logs prices only; it does not show a graph or periodically print a waiting message.

## Useful links for beginners

- [schedule documentation](https://schedule.readthedocs.io/en/stable/): the library reference used in this lesson.
- [schedule examples](https://schedule.readthedocs.io/en/stable/examples.html): hourly jobs, `.at()`, and the `run_pending()` loop.
- [schedule on PyPI](https://pypi.org/project/schedule/): the package installed with pip.
- [CoinGecko](https://www.coingecko.com/): the source of market data.
- [CoinGecko coins/markets API](https://docs.coingecko.com/demo/reference/coins-markets): request parameters and JSON fields.
- [Python CSV reading and writing](https://docs.python.org/3/library/csv.html): creating headers and appending rows.

[Previous: Day 7](../day_7/README.md) · [Next: Day 9](../day_9/README.md)
