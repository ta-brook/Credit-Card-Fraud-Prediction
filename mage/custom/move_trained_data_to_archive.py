from google.cloud import storage
import os
import time


if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom


@custom
def mv_blob(latest_model):
    """
    Function for moving files between directories or buckets. it will use GCP's copy 
    function then delete the blob from the old location.
    
    inputs
    -----
    bucket_name: name of bucket
    blob_name: str, name of file 
        ex. 'data/some_location/file_name'
    new_bucket_name: name of bucket (can be same as original if we're just moving around directories)
    new_blob_name: str, name of file in new directory in target bucket 
        ex. 'data/destination/file_name'
    """
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="credentials/service-account.json"
    storage_client = storage.Client()
    source_bucket = storage_client.get_bucket(os.getenv('DATA_SET_BUCKET'))
    source_blob = source_bucket.blob("data/dev/train.csv")
    destination_bucket = storage_client.get_bucket(os.getenv('DATA_SET_BUCKET'))
    new_blob_name=f"data/archive/train-{time.strftime('%Y%m%d-%H%M%S')}.csv"

    # copy to new destination
    new_blob = source_bucket.copy_blob(
        source_blob, destination_bucket, new_blob_name)
    # delete in old destination
    source_blob.delete()
    
    print(f'File moved from {source_blob} to {new_blob_name}')
