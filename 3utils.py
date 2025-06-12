import numpy as np
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_risk(data):
    features = [
        data["age"], data["weight"], data["height"],
        data["heart_rate"], data["bp_systolic"],
        data["bp_diastolic"], data["oxygen_level"]
    ]
    prediction = model.predict([features])
    return int(prediction[0])
