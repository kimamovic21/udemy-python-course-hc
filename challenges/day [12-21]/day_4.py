import os
import csv
from datetime import datetime
from pathlib import Path
import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

FILENAME = Path(__file__).resolve().parent / "weather_logs.csv"
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature", "Condition"])


def log_weather():
    if not API_KEY:
        print("Set OPENWEATHER_API_KEY in the .env file before logging weather.")
        return

    city = input("Enter your city name: ").strip()
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Date"] == date and row["City"].lower() == city.lower():
                print("Entry for this city and date exists")
                return

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"API Error ")
            return
        temp = data["main"]["temp"]
        condition = data["weather"][0]["main"]

        with open(FILENAME, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([date, city.title(), temp, condition])
            print(f"Logged: {temp} {condition} in {city.title()} on {date}")
    except Exception as e:
        print("Failed to make API call")


def view_logs():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
        if len(reader) <= 1:
            print("No Entries")
            return
        for row in reader[1:]:
            print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]}")


def main():
    while True:
        print("Real time weather logger")
        print("1. Add weather log")
        print("2. View weather log")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                log_weather()
            case "2":
                view_logs()
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
