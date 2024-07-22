provider "google" {
  project     = var.project_id
  region      = var.location
  credentials = file("../credentials/service-account.json")
}

resource "google_storage_bucket" "create_data_lake" {
  name          = var.data_lake_bucket_name
  project       = var.project_id
  location      = var.location
  storage_class = "STANDARD"
  uniform_bucket_level_access = true
}

resource "null_resource" "upload_clean_data" {
  depends_on = [google_storage_bucket.create_data_lake]
  provisioner "local-exec" {
    command = "gsutil -m cp -R $(pwd)/../data gs://${var.data_lake_bucket_name}"
  }
}

resource "google_artifact_registry_repository" "mlops_repo" {
  location      = var.artifact_registry_location
  repository_id = var.artifact_registry_name
  description   = "Example Docker repository"
  format        = "DOCKER"
  project       = var.project_id

  docker_config {
    immutable_tags = false
  }
}

resource "google_bigquery_dataset" "model_monitoring" {
  dataset_id                 = var.bigquery_dataset_id
  location                   = var.location
  project                    = var.project_id
  delete_contents_on_destroy = true
}

resource "google_bigquery_table" "model_predictions" {
  dataset_id = google_bigquery_dataset.model_monitoring.dataset_id
  table_id   = var.bigquery_model_predictions_table
  project    = var.project_id

  schema = jsonencode([
    {
      name = "distance_from_home"
      type = "FLOAT"
      mode = "NULLABLE"
    },
    {
      name = "distance_from_last_transaction"
      type = "FLOAT"
      mode = "NULLABLE"
    },
    {
      name = "ratio_to_median_purchase_price"
      type = "FLOAT"
      mode = "NULLABLE"
    },
    {
      name = "repeat_retailer"
      type = "FLOAT"
      mode = "NULLABLE"
    },
    {
      name = "used_chip"
      type = "FLOAT"
      mode = "NULLABLE"
    },
    {
      name = "used_pin_number"
      type = "FLOAT"
      mode = "NULLABLE"
    },
    {
      name = "online_order"
      type = "FLOAT"
      mode = "NULLABLE"
    },
    {
      name = "prediction"
      type = "FLOAT"
      mode = "NULLABLE"
    }
  ])
}

resource "google_bigquery_table" "model_runtime" {
  dataset_id = google_bigquery_dataset.model_monitoring.dataset_id
  table_id   = var.bigquery_model_runtime_table
  project    = var.project_id

  schema = jsonencode([
    {
      name = "runtime"
      type = "FLOAT"
      mode = "NULLABLE"
    }
  ])
}

resource "google_storage_bucket" "create_model_registry" {
  name          = var.model_registry
  project       = var.project_id
  location      = var.location
  storage_class = "STANDARD"
  uniform_bucket_level_access = true
}