import os
import boto3
from google.cloud import storage

def upload_to_s3(file_path, s3_bucket_name):
    s3 = boto3.client('s3',aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_KEY')   
    file_name = os.path.basename(file_path)
    print("file_aws_path",file_name)
    s3.upload_file(file_path, s3_bucket_name, file_name)

def upload_to_gcs(file_path, gcs_bucket_name):
    storage_client = storage.Client.from_service_account_json('storage.json')
    bucket = storage_client.bucket(gcs_bucket_name)
    file_name = os.path.basename(file_path)
    print("file_name #######",file_name,gcs_bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_path)

def process_directory(directory_path, s3_bucket_name, gcs_bucket_name, s3_extensions, gcs_extensions):
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            print("file_need_to_upload",file_path)
            file_extension = file.split('.')[-1].lower()

            if file_extension in s3_extensions:
                upload_to_s3(file_path, s3_bucket_name)
            elif file_extension in gcs_extensions:
                upload_to_gcs(file_path, gcs_bucket_name)

if __name__ == "__main__":
    try:
        source_directory = "test_directory"
        aws_s3_bucket = "aws_bucket_name"
        gcs_bucket = "gcp_storage_bucket_name"

        s3_file_extensions = ['jpg', 'png', 'svg', 'webp', 'mp3', 'mp4', 'mpeg4', 'wmv', '3gp', 'webm']       
        gcs_file_extensions = ['doc', 'docx', 'csv', 'pdf']
        print("process request")
        process_directory(source_directory, aws_s3_bucket, gcs_bucket, s3_file_extensions, gcs_file_extensions)
    except Exception as e:
        print("Exception",str(e))

