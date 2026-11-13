import csv
from collections import defaultdict
from pathlib import Path
import matplotlib.pyplot as plt

FILENAME = Path(__file__).resolve().parent / "weather_logs.csv"


def visualize_weather():
    dates = []
    temps = []
    conditions = defaultdict(int)

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                date = row["Date"]
                temperature = float(row["Temperature"])
                condition = row["Condition"]
            except (KeyError, TypeError, ValueError):
                continue
            dates.append(date)
            # temps.append(row["Temperature"])  # Original: strings become categories.
            temps.append(temperature)
            conditions[condition] += 1
    if not dates:
        print("NO data is available")
        return

    plt.figure(figsize=(10, 7))
    plt.plot(dates, temps, marker="o")
    plt.title("Temperature over time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(7, 5))
    plt.bar(conditions.keys(), conditions.values(), color="skyblue")
    plt.xlabel("Condition")
    plt.ylabel("Records")
    plt.show()


visualize_weather()
