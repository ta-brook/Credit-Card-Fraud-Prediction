import os
import pickle
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression

def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)

def make_writeable(arr):
    """Ensure that the numpy array is writeable."""
    arr.setflags(write=True)
    return arr

def train_model(X_train, y_train):
    """Train a logistic regression model using grid search for hyperparameter optimization."""
    param_grid = {
        'penalty': ['l1', 'l2',],
        'C': [0.01, 0.1, 1.0],
    }
    model = LogisticRegression(max_iter=1000)
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    return grid_search

def evaluate_model(model, X_test, y_test):
    """Evaluate the logistic regression model."""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred, output_dict=True)
    return accuracy, conf_matrix, class_report

def save_model(model, filename: str):
    """Save the trained model to a pickle file."""
    with open(filename, "wb") as f_out:
        pickle.dump(model, f_out)

def main():
    data_path ="output"
    model_path = "models"

    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_test, y_test = load_pickle(os.path.join(data_path, "test.pkl"))

    # Ensure arrays are writeable
    X_train = make_writeable(np.array(X_train))
    y_train = make_writeable(np.array(y_train))
    X_test = make_writeable(np.array(X_test))
    y_test = make_writeable(np.array(y_test))


    # Start MLflow run
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("Logistic Regression Experiment with HPO")
    with mlflow.start_run() as run:
        # Train the logistic regression model with hyperparameter optimization
        grid_search = train_model(X_train, y_train)

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

        # Save confusion matrix as a numpy file
        np.save(os.path.join(data_path, "confusion_matrix.npy"), conf_matrix)
        
        # Log the confusion matrix
        mlflow.log_artifact(os.path.join(data_path, "confusion_matrix.npy"))

        print(f"Accuracy: {accuracy}")
        print(f"Confusion Matrix:\n{conf_matrix}")
        print(f"Classification Report:\n{class_report}")

        # Log model parameters
        mlflow.log_param("model_type", "LogisticRegression")

        # Log the model
        mlflow.sklearn.log_model(best_model, "model")

        # Register the model
        mlflow.register_model(f"runs:/{run.info.run_id}/model", "fraudModel")

if __name__ == '__main__':
    main()

