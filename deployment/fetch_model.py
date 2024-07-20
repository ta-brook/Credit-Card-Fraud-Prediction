import mlflow
from mlflow.tracking import MlflowClient
import os

mlflow.set_tracking_uri("http://127.0.0.1:5000")

def print_model_info(rm):
    print("--Model--")
    print("name: {}".format(rm.name))
    print("aliases: {}".format(rm.aliases))

def download_registered_model(model_name, model_alias, local_path):
    client = MlflowClient()
    latest_model = client.get_model_version_by_alias(model_name, model_alias)
    print_model_info(latest_model)
    model_uri = client.get_model_version_download_uri(model_name, latest_model.version)
    mlflow.artifacts.download_artifacts(model_uri, dst_path=local_path)

if __name__ == "__main__":
    model_name = "fraudModel"
    model_alias = "dev"  # Change this to the appropriate version
    local_path = "models"
    
    os.makedirs(local_path, exist_ok=True)
    download_registered_model(model_name, model_alias, local_path)
    print(f"Model downloaded to {local_path}")
