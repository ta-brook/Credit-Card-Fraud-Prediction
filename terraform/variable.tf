variable "project_id" {
  description = "Google Cloud project ID"
  type        = string
}

variable "location" {
  description = "Google Cloud location"
  type        = string
  default     = "US"
}

variable "data_lake_bucket_name" {
  description = "Name of the data lake storage bucket"
  type        = string
}

variable "artifact_registry_location" {
  description = "Location for the Artifact Registry"
  type        = string
  default     = "US"
}

variable "artifact_registry_name" {
  description = "Name of the Artifact Registry repository"
  type        = string
}

variable "bigquery_dataset_id" {
  description = "BigQuery dataset ID"
  type        = string
}

variable "bigquery_model_predictions_table" {
  description = "BigQuery model predictions table ID"
  type        = string
}

variable "bigquery_model_runtime_table" {
  description = "BigQuery model runtime table ID"
  type        = string
}
