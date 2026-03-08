import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Load dataset
data = pd.read_csv("dataset/urls.csv")

X = data["url"]
y = data["label"]

# ML Pipeline
model = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, "phishing_model.pkl")

print("Model trained successfully")
