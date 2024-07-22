from mage.utils.CICD.cloudbuild_trigger import run_build_trigger
import os
import time

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom

@custom
def transform_custom(*args, **kwargs):
    project_id = os.getenv('GOOGLE_CLOUD_PROJECT')  # Replace with your project ID
    trigger_id = "CI-package-image"  # Replace with your trigger ID
    location = "us-central1"  # Replace with your trigger location

    # Run the build trigger
    run_build_trigger(project_id, trigger_id, location)

    # wait for image to built (since this project is poc this will be sleep for easy development)
    print("wait for image to built (since this project is poc this will be sleep for easy development)")
    print("sleep for 2 minute")
    time.sleep(120)

    return True

