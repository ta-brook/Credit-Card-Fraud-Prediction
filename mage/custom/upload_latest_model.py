from google.cloud import storage
import os

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def upload_to_bucket(*args, **kwargs):
    """ Upload data to a bucket"""
    storage_client = storage.Client()

    buckets = list(storage_client.list_buckets())

    bucket = storage_client.get_bucket(os.getenv('MODEL_REGISTRY_BUCKET')) # your bucket name

    blob = bucket.blob('deployment/dev/model.pkl')
    blob.upload_from_filename('deployment/model/model.pkl')
    print(buckets)
    
    #returns a public url
    return blob.public_url

