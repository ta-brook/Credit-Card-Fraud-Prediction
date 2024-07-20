import mlflow.pyfunc

mlflow.set_tracking_uri("http://127.0.0.1:5000")

model_name = "fraudModel"
alias = "book"

champion_version = mlflow.pyfunc.load_model(f"models:/{model_name}@{alias}")

print(champion_version)
