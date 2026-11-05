from pathlib import Path

order_path = Path(__file__).resolve().parent / "order.txt"

file = open(order_path, "w", encoding="utf-8")
try:
    file.write("ginger tea - 4 cups")
finally:
    file.close()
