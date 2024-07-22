import mlflow
import os
from mlflow.tracking import MlflowClient

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom


def print_model_info(rm):
    print("--Model--")
    print("name: {}".format(rm.name))
    print("aliases: {}".format(rm.aliases))

@custom
def transform_custom(run_info, *args, **kwargs):
    MODEL_NAME, run_id = run_info
    model_alias = "dev"

    # mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
    client = MlflowClient()

    filter_string = f"name='{MODEL_NAME}'"
    results = client.search_model_versions(filter_string)

    for idx, result in enumerate(results):
        if result.run_id == run_id:
            latest_model = result
            client.set_registered_model_alias(MODEL_NAME, model_alias, result.version)

    return latest_model
