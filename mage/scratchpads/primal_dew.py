import requests
import json
import pandas as pd


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

def prepare_data(df, target_column):
    """
    Prepare data by removing the target column.
    """
    # Cut the dataset to 500 to reduce time for this project
    # the actual practice should be making prediction script receive batch/chunk data to increase performance
    # Or making a parallel processing to increase performance but we will leave the idea here
    df_cut = df.head(5)
    print(df_cut.info)

    return df_cut.drop(columns=[target_column])

@custom
def predict(df, *args, **kwargs):
    """
    Function to loop through DataFrame rows and get predictions.
    """
    # Prepare data by removing the target column
    df_prepared = prepare_data(df, 'fraud') 
    print('here')

    start_time = time.time()
    results = []
    print('here')
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
            result_row["prediction"] = prediction
            results.append(result_row)
    
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Total predictions made: {len(results)}")
    print(f"Total runtime: {runtime:.2f} seconds")
    
    return pd.DataFrame(results)

predict()