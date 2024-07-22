from mage_ai.orchestration.triggers.api import trigger_pipeline

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom


@custom
def trigger_cicd(*args, **kwargs):

    trigger_pipeline(
        'retrain_model',
        check_status=True,
        error_on_failure=True,
        schedule_name='Automatic trigger retrain a new model after detect new dataset on bucket',
        verbose=True,
    )
