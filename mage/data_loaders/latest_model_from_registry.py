import mlflow
from mlflow.tracking import MlflowClient
import os

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def print_model_info(rm):
    print("--Model--")
    print("name: {}".format(rm.name))
    print("aliases: {}".format(rm.aliases))

@data_loader
def load_data(*args, **kwargs):
    model_name = "fraudModel"
    model_alias = "dev" 
    local_path = "deployment"

    client = MlflowClient()
    latest_model = client.get_model_version_by_alias(model_name, model_alias)
    print_model_info(latest_model)
    model_uri = client.get_model_version_download_uri(model_name, latest_model.version)
    mlflow.artifacts.download_artifacts(model_uri, dst_path=local_path)
    print(f"Model downloaded to {local_path}")

    return True


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
