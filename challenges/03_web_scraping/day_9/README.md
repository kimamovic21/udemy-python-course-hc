# Day 9: Store and Search Crypto Prices in SQLite

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to store CoinGecko price observations in a local SQLite database and retrieve a selected coin's latest saved price. This lesson replaces CSV storage with a database table and parameterized SQL queries.

## Files

| File | Purpose |
| --- | --- |
| [DAY_9.md](DAY_9.md) | The original challenge statement, maintained manually and left unchanged. |
| [day_9.py](day_9.py) | Creating a table, inserting API records, and searching saved prices. |
| `crypto.db` | The SQLite database created and reused beside the script. |

The current program is menu-driven. The original task's hourly logging requirement is not implemented, even though `schedule` and `time` are imported.

## Setup

Install the external packages using the interpreter that runs the script:

```powershell
python -m pip install requests schedule
```

`requests` fetches API data. `schedule` is an unused import but must still be installed for that import to succeed. `sqlite3`, `pathlib`, and `datetime` are included with this Python installation; no separate database server or `pip install sqlite3` is needed. The `os`, `csv`, and `time` imports are also unused in this version.

No API key or `.env` loading is configured. See the [Day 7 API-access notes](../day_7/README.md#coingecko-api-access) if CoinGecko requires authentication for your request.

## Database location and structure

```python
DB_NAME = Path(__file__).resolve().parent / "crypto.db"
```

All connections use `challenges/03_web_scraping/day_9/crypto.db`, regardless of the terminal's working directory. No CSV from Day 7 or Day 8 is required, and their records are not imported automatically.

`main()` calls `create_table()` before displaying the menu. `sqlite3.connect()` creates a missing database file, and `CREATE TABLE IF NOT EXISTS` creates the table without replacing existing data. The database can therefore exist with an empty table before any prices have been fetched.

The `crypto_prices` table contains:

| Column | Declared type | Meaning |
| --- | --- | --- |
| `id` | `INTEGER PRIMARY KEY AUTOINCREMENT` | Automatically assigned record identifier. |
| `timestamp` | `TEXT` | Local logging time in `%Y-%m-%d %H-%M-%S` format. |
| `coin` | `TEXT` | CoinGecko coin ID, such as `bitcoin`. |
| `price` | `REAL` | Saved numeric price in USD. |

SQLite may also show an internal `sqlite_sequence` table for automatic numbering. The project's price records belong in `crypto_prices`.

## Menu and functions

| Option | What happens |
| --- | --- |
| `1` — Fetch and store | Request up to 10 coins ordered by descending market capitalization, then insert their IDs and current USD prices. |
| `2` — Search latest price | Ask for a coin ID and display its most recent stored price and timestamp, if found. |
| Any other value | Print `Invalid option`. |

Each run performs one action and finishes. Run the script again to choose another action; there is no repeating menu loop.

- `fetch_crypto_data()` requests CoinGecko's `/coins/markets` endpoint and decodes its JSON response.
- `save_to_database(data)` creates one timestamp for the batch and inserts records with `VALUES (?, ?, ?)`. Values are supplied separately through a tuple. `commit()` saves the changes, then the connection is closed.
- `search_coin(coin_name)` uses `WHERE coin = ?`, `ORDER BY timestamp DESC`, and `LIMIT 1`. `fetchone()` returns the selected row, printed as a price and timestamp.

Successful fetch-and-store actions add rows rather than replacing history. There is no duplicate check. Search reads the database; it does not fetch a fresh price from the API.

## How to run

From the repository root:

```powershell
python "challenges/03_web_scraping/day_9/day_9.py"
```

Or, from this lesson's folder:

```powershell
python .\day_9.py
```

In VS Code, open `day_9.py`, press **Ctrl + S**, and answer in the Run on Save terminal. Choose `1` to collect data. Run again, choose `2`, and enter a saved coin ID such as `bitcoin`. A ticker such as `BTC` is not the same ID.

If no matching row exists, the current search function prints no result message. Option `2` can read existing records without making a network request.

## Opening crypto.db in VS Code

`crypto.db` is a binary SQLite database, not a text file. The editor message about binary files or unsupported encoding is expected when opening it in a text editor.

Use the [SQLite Viewer extension](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer), installed during this project's setup. On another machine, install it through Extensions or run:

```powershell
code --install-extension qwtel.sqlite-viewer
```

1. Open `crypto.db` in the Explorer.
2. If it still opens as text, right-click and choose **Open With… → SQLite Viewer**.
3. Select **crypto_prices** to inspect the saved rows and columns.

The basic viewer is read-only and caches its data. Reopen the database after new inserts if the displayed rows are stale. The Python script performs inserts and SQL searches; the viewer is optional and is not required for the script to run.

## Current behaviour to understand

- Hourly collection is not implemented: fetching happens only when option `1` is selected. There is no scheduled job or polling loop.
- `main()` is called at module level without a main guard. Importing the file creates or opens the database and displays the input prompt.
- There is no explicit request timeout, HTTP status check, API response validation, or exception handler. API, network, and database errors are not handled separately.
- Input is trimmed and lowercased, then matched against the complete coin ID. Partial-name searching and missing-result feedback are not implemented.
- Timestamps are stored as text. Rows with identical timestamps have no additional tie-breaking sort order in the latest-price query.

## Useful links for beginners

- [Python sqlite3 tutorial](https://docs.python.org/3/library/sqlite3.html#tutorial): connections, tables, inserts, queries, commits, and placeholders.
- [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer): viewing database tables inside VS Code.
- [CoinGecko](https://www.coingecko.com/): the project's market-data provider.
- [CoinGecko coins/markets API](https://docs.coingecko.com/demo/reference/coins-markets): request parameters and response fields.
- [Paths with pathlib](https://docs.python.org/3/library/pathlib.html): keeping the database beside the script.

[Previous: Day 8](../day_8/README.md)
