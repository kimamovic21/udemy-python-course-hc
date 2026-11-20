from pathlib import Path

import numpy as np
import pandas as pd

OUTPUT_FILE = Path(__file__).resolve().parent / "experience_salary.csv"

np.random.seed(42)

years = np.random.uniform(0.5, 10, 100).round(2)

salaries = (30000 + years * 6000 + np.random.normal(0, 4000, size=100)).round(2)

df = pd.DataFrame({"YearsExperience": years, "Salary": salaries})
df.to_csv(OUTPUT_FILE, index=False)
print("Data saved in file ✅")
