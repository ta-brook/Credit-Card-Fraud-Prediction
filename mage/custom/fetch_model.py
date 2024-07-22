import mlflow
from mlflow.tracking import MlflowClient
import os

def print_model_info(rm):
    print("--Model--")
    print("name: {}".format(rm.name))
    print("aliases: {}".format(rm.aliases))



if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    model_name = "fraudModel"
    model_alias = "dev"  # Change this to the appropriate version
    local_path = "models"
    print("here")
    client = MlflowClient()
    print("here")
    latest_model = client.get_model_version_by_alias(model_name, model_alias)
    print("here")
    print_model_info(latest_model)
    model_uri = client.get_model_version_download_uri(model_name, latest_model.version)
    mlflow.artifacts.download_artifacts(model_uri, dst_path=local_path)

    return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
