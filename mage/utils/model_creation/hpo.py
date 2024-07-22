from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

def hpo_train_model(X_train, y_train):
    """Train a logistic regression model using grid search for hyperparameter optimization."""
    param_grid = {
        'penalty': ['l1', 'l2',],
        'C': [0.01, 0.1, 1.0],
    }
    model = LogisticRegression(max_iter=1000)
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    return grid_search