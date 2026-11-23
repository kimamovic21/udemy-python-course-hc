from pathlib import Path

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

DATA_FILE = Path(__file__).resolve().parent / "youtube_comments.csv"
df = pd.read_csv(DATA_FILE)

X_train, X_test, y_train, y_test = train_test_split(
    df["comment"], df["label"], test_size=0.2, random_state=42
)

model = Pipeline([("tfidf", TfidfVectorizer()), ("clf", LogisticRegression())])

model.fit(X_train, y_train)

acc = model.score(X_test, y_test)
print(f"Model trained. Accuracy: {round(acc * 100, 2)}%")
