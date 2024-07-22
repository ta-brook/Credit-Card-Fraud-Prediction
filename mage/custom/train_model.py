import os
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression

from mage.utils.model_creation.hpo import hpo_train_model
from mage.utils.model_creation.evaluation import evaluate_model

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(list_of_data, *args, **kwargs):
    X_train, X_test, y_train, y_test = list_of_data
    # Start MLflow run
    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
    mlflow.set_experiment("Logistic Regression Experiment with HPO")
    with mlflow.start_run() as run:
        MODEL_NAME = "fraudModel"

        # Train the logistic regression model with hyperparameter optimization
        grid_search = hpo_train_model(X_train, y_train)

        # Get the best model and parameters
        best_model = grid_search.best_estimator_
        best_params = grid_search.best_params_
        best_accuracy = grid_search.best_score_

        # Evaluate the best model
        accuracy, conf_matrix, class_report = evaluate_model(best_model, X_test, y_test)
        
        # Log parameters and metrics for the best model
        mlflow.log_params(best_params)
        mlflow.log_metric("mean_test_score", best_accuracy)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", class_report['weighted avg']['precision'])
        mlflow.log_metric("recall", class_report['weighted avg']['recall'])
        mlflow.log_metric("f1_score", class_report['weighted avg']['f1-score'])

        print(f"Accuracy: {accuracy}")
        print(f"Confusion Matrix:\n{conf_matrix}")
        print(f"Classification Report:\n{class_report}")

        # Log model parameters
        mlflow.log_param("model_type", "LogisticRegression")

        # Log the model
        mlflow.sklearn.log_model(best_model, "model")

        # Register the model
        mlflow.register_model(f"runs:/{run.info.run_id}/model", MODEL_NAME)


    return MODEL_NAME, run.info.run_id


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
