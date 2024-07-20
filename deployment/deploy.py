import pickle
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the model from the local file
with open("models/model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        if not isinstance(data, list):
            return jsonify({"error": "Input data should be a list of feature values"}), 400

        input_df = pd.DataFrame(data)
        predictions = model.predict(input_df)
        return jsonify(predictions.tolist()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "ML Model Deployment API", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1150)
