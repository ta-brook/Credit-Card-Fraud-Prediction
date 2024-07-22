from google.cloud.devtools import cloudbuild_v1
from google.api_core.exceptions import NotFound, PermissionDenied, GoogleAPICallError
from google.api_core.operation import Operation

def run_build_trigger(project_id, trigger_id, location):
    client = cloudbuild_v1.CloudBuildClient()

    # Define the source
    source = cloudbuild_v1.RepoSource(
        branch_name="main",  # Use the branch name you want to build
    )

    try:
        name = f"projects/{project_id}/locations/{location}/triggers/{trigger_id}"
        print(f"Triggering build with the following details:")
        print(f"Name: {name}")
        print(f"Project ID: {project_id}")
        print(f"Trigger ID: {trigger_id}")
        print(f"Location: {location}")

        request = cloudbuild_v1.RunBuildTriggerRequest(
            name=name,
            project_id=project_id,
            trigger_id=trigger_id,
            source=source,
        )

        operation: Operation = client.run_build_trigger(request=request)
        print("Waiting for operation to complete...")

        # Add a timeout to avoid hanging indefinitely
        response = operation.result(timeout=600)

        print("Build triggered successfully!")
        print("Build ID:", response.id)
    except NotFound as e:
        print(f"Error: The project ID '{project_id}', trigger ID '{trigger_id}', or location '{location}' was not found.")
        print(e)
        print(f"***[NOTE] If you found this error. Please take a look at cloudbuild history it's might work but return 404 for no reason.***")
        print(f"***[NOTE] If you found this error. Please take a look at cloudbuild history it's might work but return 404 for no reason.***")
        print(f"***[NOTE] If you found this error. Please take a look at cloudbuild history it's might work but return 404 for no reason.***")
    except PermissionDenied as e:
        print(f"Error: Permission denied. Please check if the service account has the necessary permissions.")
        print(e)
    except GoogleAPICallError as e:
        print(f"Error: An API call error occurred.")
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")