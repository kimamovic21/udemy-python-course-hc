from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

DATA_FILE = Path(__file__).resolve().parent.parent / "day_2" / "experience_salary.csv"
data = pd.read_csv(DATA_FILE)

X = data[["YearsExperience"]]
y = data["Salary"]

model = LinearRegression()
model.fit(X, y)

st.title("Salary Predictor based on experience")
st.write("Enter your years of experience to predict your salary:")

years_input = st.number_input(
    "Years of experience", min_value=0.0, max_value=50.0, step=0.1
)

prediction_input = pd.DataFrame({"YearsExperience": [years_input]})
predicted_salary = model.predict(prediction_input)[0]
st.success(f"Estimated Salary: {predicted_salary:,.2f}")

st.subheader("Regression Line")

fig, ax = plt.subplots()
ax.scatter(X, y, color="blue", label="Actual Data")
ax.plot(X, model.predict(X), color="red", label="Regression line")
ax.set_xlabel("Years of experience")
ax.set_ylabel("Salary")
ax.set_title("Salary vs Experience")
ax.legend()

st.pyplot(fig)
plt.close(fig)
