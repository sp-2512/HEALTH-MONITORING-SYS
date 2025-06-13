from flask import Flask, jsonify
from data_simulator import simulate_health_data
from utils import predict_risk

app = Flask(__name__)

@app.route("/monitor", methods=["GET"])
def monitor():
    data = simulate_health_data()
    risk = predict_risk(data)
    response = {
        "vitals": data,
        "predicted_risk": risk,
        "message": "High risk, seek medical attention!" if risk else "Normal vitals."
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
