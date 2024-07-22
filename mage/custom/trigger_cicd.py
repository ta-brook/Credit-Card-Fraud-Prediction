from mage_ai.orchestration.triggers.api import trigger_pipeline

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom


@custom
def trigger_cicd(*args, **kwargs):

    trigger_pipeline(
        'model_deployment_cicd',
        check_status=True,
        error_on_failure=True,
        schedule_name='Automatic trigger CICD after train a new model',
        verbose=True,
    )
