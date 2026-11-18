# Day 7: Crypto Price Tracker with Graphs

[Group overview](../README.md) · [Challenge index](../../README.md) · [Main project overview](../../../README.md#folder-overview)

The task is to fetch prices for the top 10 cryptocurrencies by market capitalization from [CoinGecko](https://www.coingecko.com/), append timestamped records to a CSV, and plot a selected coin's recorded prices. This lesson reads a JSON API response rather than parsing a website's HTML.

## Files

| File | Purpose |
| --- | --- |
| [DAY_7.md](DAY_7.md) | The original challenge statement, maintained manually and left unchanged. |
| [day_7.py](day_7.py) | Fetching CoinGecko data, logging prices, and displaying a Matplotlib graph. |
| `crypto_prices.csv` | Local price history with `timestamp`, `coin`, and `price` columns, created beside the script. |

## Setup

Install the external packages using the Python interpreter that runs the script:

```powershell
python -m pip install requests matplotlib
```

`requests` fetches the JSON response, while `matplotlib.pyplot`, imported as `plt`, draws the graph. The `os`, `csv`, `pathlib`, and `datetime` modules come with Python. This lesson does not use Beautiful Soup, wget, or Pillow directly.

If these packages were installed for earlier projects in the same interpreter, they are already available. For unresolved imports, check **Python: Select Interpreter** in VS Code and install packages using that interpreter.

### CoinGecko API access

The configured endpoint is:

```text
https://api.coingecko.com/api/v3/coins/markets
```

The [official coins/markets documentation](https://docs.coingecko.com/demo/reference/coins-markets) describes its parameters and response fields. The current script sends no API key and does not load an `.env` file. CoinGecko's [Demo authentication guide](https://docs.coingecko.com/demo/reference/authentication) documents API-key access through the `x-cg-demo-api-key` header; that configuration is not implemented here.

If access is refused or a key is required for your request, consult those instructions: package installation alone does not configure authentication. API quotas and request limits depend on the service's access plan. The current code also lacks HTTP-error and response-shape checks, so an API error response may cause a later exception instead of a clear API message.

## How the code works

1. `fetch_crypto_data()` calls `requests.get(API_URL, params=PARAMS)` and converts the response JSON into Python data with `response.json()`.
2. `save_to_csv(data)` checks whether the output file exists, opens it in append mode, and writes the header only for a new file.
3. One local timestamp is generated for the fetched batch. Each returned coin contributes its `id` and `current_price` to a CSV row.
4. `main()` prints the fetched IDs and prices, then asks which coin to graph. Input is stripped and converted to lowercase.
5. `plot_graph(coin_id)` reads the CSV using `csv.DictReader`, keeps rows with the matching ID, and converts each stored price to `float`.
6. Matplotlib draws a line plot with point markers, a grid, and adjusted spacing. `plt.show()` displays a window; the script does not automatically save a PNG.

### Request parameters

| Parameter | Value | Meaning |
| --- | --- | --- |
| `vs_currency` | `usd` | Request prices in US dollars. |
| `order` | `market_cap_desc` | Order by descending market capitalization. |
| `per_page` | `10` | Request up to 10 coins. |
| `page` | `1` | Read the first result page. |
| `sparkline` | `False` | Do not request the API's sparkline series. |

The graph uses observations collected by this script, not a downloaded historical price series.

## CSV location and repeated runs

```python
CSV_FILE = Path(__file__).resolve().parent / "crypto_prices.csv"
```

Reads and writes stay at:

```text
challenges/03_web_scraping/day_7/crypto_prices.csv
```

This works from the repository root, from the lesson folder, and through **Ctrl + S**. The earlier plain filename could create `crypto_prices.csv` in the root. Any older root copy is separate and is not automatically loaded or moved by the current script.

The file is opened with mode `"a"` and `newline=""`. Each successful batch normally adds 10 rows, preserving existing history. Repeated runs do not deduplicate timestamps or observations. The timestamp format is `%Y-%m-%d %H-%M-%S`, using the computer's local time and hyphens between hour, minute, and second.

These fictional values illustrate the CSV structure; they are not real price quotes:

```csv
timestamp,coin,price
2026-11-18 12-00-00,bitcoin,100.0
2026-11-18 12-05-00,bitcoin,101.5
```

A new empty file that already exists does not receive a header in the current implementation, because the check only tests existence. File encoding is not explicitly specified in the code.

## How to run and choose a coin

From the repository root:

```powershell
python "challenges/03_web_scraping/day_7/day_7.py"
```

Or, from this lesson's folder:

```powershell
python .\day_7.py
```

In VS Code, open `day_7.py`, press **Ctrl + S**, and click inside the Run on Save terminal to answer the prompt.

Use a **coin ID printed by the program**, such as `bitcoin`, rather than a ticker such as `BTC`. Press **Enter** without a value to finish after logging. A coin with no matching CSV rows prints `No data found for ...`. Close the graph window to finish a plotting run.

After a first successful batch, each coin normally has one recorded point. Run the program at different times to build a series. The script stores timestamps as strings and plots rows in CSV order; it does not parse timestamps into date objects or schedule periodic collection.

## Current behaviour to understand

- The request has no explicit timeout, status check, exception handler, or JSON-schema validation. It expects a list of records with `id` and `current_price`.
- Logging happens before the graph prompt. Every Ctrl + S starts another fetch-and-append run; wait for or stop an earlier run before starting another.
- Prices are the API values available when fetched; the CSV timestamp is the local logging time, not the API's own update timestamp.
- File-reading, file-writing, missing-column, and invalid-price errors are not handled separately. Empty or absent API results are not validated before saving.
- The Matplotlib window displays the selected coin's stored values. It is not refreshed automatically and does not create an image file.

## Useful links for beginners

- [CoinGecko](https://www.coingecko.com/): the website of the data provider used in this project.
- [CoinGecko coins/markets endpoint](https://docs.coingecko.com/demo/reference/coins-markets): market-data parameters and the `id` and `current_price` fields.
- [CoinGecko Demo authentication](https://docs.coingecko.com/demo/reference/authentication): official API access and key configuration, not yet implemented in this script.
- [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html): creating figures, drawing data, and displaying charts.
- [Python CSV reading and writing](https://docs.python.org/3/library/csv.html): appending rows and reading columns with `DictReader`.
- [Paths with pathlib](https://docs.python.org/3/library/pathlib.html): keeping the CSV beside the script.

[Previous: Day 6](../day_6/README.md)
