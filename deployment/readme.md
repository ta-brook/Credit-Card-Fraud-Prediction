## Fetch latest model with alias dev from model registry
```python
python fetch_model.py
```

## Build and Run the Docker Container

Build the Docker image:
```sh
docker build -t fraud-model-deployment:latest .
```

Run the Docker container locally:
```sh
docker run -d -p 1150:1150 fraud-model-deployment:latest
```

## Run container from Artifact Registry

```docker
docker run -d -p 1150:1150 us-central1-docker.pkg.dev/logical-sled-430104-t6/mlops/fraude.predictiont:latest
```

## Test the Deployment
```
curl -X POST http://localhost:1150/predict -H "Content-Type: application/json" -d '[{"distance_from_home": 4.567738, "distance_from_last_transaction": 0.181920, "ratio_to_median_purchase_price": 0.782519, "repeat_retailer": 1.0, "used_chip": 0.0, "used_pin_number": 0.0, "online_order": 0.0}]'
```