from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load serialized model
model = joblib.load("models/trained_model.joblib")

@app.route("/test_link", methods=["GET"])
def test_endpoint():
    return jsonify({"test": "works"})


@app.route("/predict", methods=["GET"])
def predict():
    data = request.get_json()
    # data = {"DayOfWeek": 2}
    X = pd.DataFrame([data])
    pred = model.predict(X)[0]
    return jsonify({"prediction": int(pred)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)