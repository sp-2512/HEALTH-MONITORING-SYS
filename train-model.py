import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Simulated dataset
data = pd.read_csv("https://raw.githubusercontent.com/datablist/sample-csv-files/main/files/people/people-100.csv")
data = data.rename(columns={"Age": "age", "Weight": "weight", "Height": "height"})
data["heart_rate"] = 60 + (data["age"] / 2).astype(int) + (data["weight"] % 10)
data["bp_systolic"] = 100 + (data["age"] // 2)
data["bp_diastolic"] = 70 + (data["weight"] % 10)
data["oxygen_level"] = 98 - (data["age"] % 5)
data["risk"] = ((data["heart_rate"] > 100) | (data["bp_systolic"] > 140)).astype(int)

features = ["age", "weight", "height", "heart_rate", "bp_systolic", "bp_diastolic", "oxygen_level"]
X = data[features]
y = data["risk"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
