import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(8)

# Function to generate synthetic data
def generate_data(num_samples, drift=False):
    data = {
        "distance_from_home": np.random.normal(loc=10, scale=5, size=num_samples),
        "distance_from_last_transaction": np.random.normal(loc=2, scale=1, size=num_samples),
        "ratio_to_median_purchase_price": np.random.normal(loc=0.5, scale=0.2, size=num_samples),
        "repeat_retailer": np.random.binomial(1, 0.5, num_samples),
        "used_chip": np.random.binomial(1, 0.3, num_samples),
        "used_pin_number": np.random.binomial(1, 0.2, num_samples),
        "online_order": np.random.binomial(1, 0.1, num_samples),
        "fraud": np.random.binomial(1, 0.05, num_samples)
    }

    if drift:
        # Introduce data drift by changing the distribution parameters
        data["distance_from_home"] = np.random.normal(loc=20, scale=10, size=num_samples)
        data["distance_from_last_transaction"] = np.random.normal(loc=4, scale=2, size=num_samples)
        data["ratio_to_median_purchase_price"] = np.random.normal(loc=0.7, scale=0.3, size=num_samples)
        data["repeat_retailer"] = np.random.binomial(1, 0.6, num_samples)
        data["used_chip"] = np.random.binomial(1, 0.4, num_samples)
        data["used_pin_number"] = np.random.binomial(1, 0.3, num_samples)
        data["online_order"] = np.random.binomial(1, 0.2, num_samples)
        data["fraud"] = np.random.binomial(1, 0.1, num_samples)
    
    return pd.DataFrame(data)

# Generate reference data
reference_data = generate_data(num_samples=1000, drift=False)
reference_data.to_csv("data/predict/card_transdata.csv", index=False)

# Generate current data with data drift
current_data = generate_data(num_samples=1000, drift=True)
current_data.to_csv("data/drift/card_transdata.csv", index=False)

# Generate current data with data drift
current_data = generate_data(num_samples=1000, drift=True)
current_data.to_csv("data/dev/tarin.csv", index=False)

print("Data generation complete. Files saved as 'reference_data.csv' and 'current_data.csv'.")
