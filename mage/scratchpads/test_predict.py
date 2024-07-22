import requests
import json

# URL of the deployed model API
API_URL = 'https://fraud-prediction-zbwivrhxea-uc.a.run.app/predict'

# Sample data to be sent in the POST request
data = [{
    "distance_from_home": 4.567738,
    "distance_from_last_transaction": 0.181920,
    "ratio_to_median_purchase_price": 0.782519,
    "repeat_retailer": 1.0,
    "used_chip": 0.0,
    "used_pin_number": 0.0,
    "online_order": 0.0
}]

# Function to send data to the model and get prediction
def get_prediction(data):
    headers = {"Content-Type": "application/json"}
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def main():
    # Get prediction from the model
    prediction = get_prediction(data)
    
    if prediction:
        print("Prediction result:")
        print(prediction)

if __name__ == '__main__':
    main()
