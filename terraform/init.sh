# load-env.sh

source <(tr -d '\r' < .env)

export TF_VAR_model_registry="credit-card-fraud-model-registry"
export TF_VAR_bigquery_model_predictions_table="model_predictions"
export TF_VAR_bigquery_model_runtime_table="model_runtime"
export TF_VAR_bigquery_dataset_id="model_monitoring"