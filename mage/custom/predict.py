import requests
import json
import time
import pandas as pd

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


def get_prediction(data):
    """
    Function to send data to the model and get prediction.
    """
    # URL of the deployed model API
    API_URL = 'https://fraud-prediction-zbwivrhxea-uc.a.run.app/predict'

    headers = {"Content-Type": "application/json"}
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


@custom
def predict(data, *args, **kwargs):
    """
    Function to loop through DataFrame rows and get predictions.
    """
    df_target, df_prepared = data

    start_time = time.time()
    results = []

    for _, row in df_prepared.iterrows():
        data = [{
            "distance_from_home": row['distance_from_home'],
            "distance_from_last_transaction": row['distance_from_last_transaction'],
            "ratio_to_median_purchase_price": row['ratio_to_median_purchase_price'],
            "repeat_retailer": row['repeat_retailer'],
            "used_chip": row['used_chip'],
            "used_pin_number": row['used_pin_number'],
            "online_order": row['online_order']
        }]
        
        prediction = get_prediction(data)
        if prediction:
            result_row = row.to_dict()
            result_row["prediction"] = prediction[0]
            results.append(result_row)
    
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Total predictions made: {len(results)}")
    print(f"Total runtime: {runtime:.2f} seconds")
    
    # merge data
    predicted_df = pd.DataFrame(results)
    df_to_log = pd.merge(predicted_df, df_target, left_index=True, right_index=True)
    
    return df_to_log
