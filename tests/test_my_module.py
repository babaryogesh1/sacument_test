import os
from my_module import process_directory, upload_to_s3, upload_to_gcs
import boto3
from google.cloud import storage
from unittest.mock import Mock, patch

def test_upload_to_s3():
    s3 = boto3.client('s3',aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_KEY') 
    s3_client.upload_file = Mock()
    upload_to_s3("test_directory/test_file.jpg", "aws_bucket_name")
    s3_client.upload_file.assert_called_with("test_directory/test_file.jpg", "aws_bucket_name")

def test_upload_to_gcs():
    storage_client = storage.Client.from_service_account_json('storage.json')
    storage_client.bucket = Mock()
   # storage_client.bucket().blob = Mock()
    upload_to_gcs("test_directory/test_file.pdf", "gcp_storage_bucket_name")
    storage_client.bucket.assert_called_with("test_directory/test_file.pdf","gcp_storage_bucket_name")
   # storage_client.bucket().blob.assert_called_with("test_file.pdf")
    print(storage_client)

def test_process_directory():
    with patch("my_module.os.walk") as mock_walk:
        mock_walk.return_value = [
            ("test_directory", [], ["test_file.jpg","test_file.pdf", "file2.docx"])
         
        ]
        with  patch("my_module.upload_to_s3") as mock_upload_s3,patch("my_module.upload_to_gcs") as mock_upload_gcs:
            process_directory("test_directory", "aws_bucket_name", "gcp_storage_bucket_name", ["jpg"], ["pdf"])
            mock_upload_s3.assert_called_with("test_directory/test_file.jpg", "aws_bucket_name")
            # mock_upload_s3.assert_not_called_with("file2.docx", "aws_bucket_name")
            mock_upload_gcs.assert_called_with("test_directory/test_file.pdf", "gcp_storage_bucket_name")
            #mock_upload_gcs.assert_not_called_with("file1.jpg", "gcp_storage_bucket_name")
            # mock_upload_s3.assert_not_called_with("file3.png", "aws_bucket_name")
            # mock_upload_gcs.assert_not_called_with("file3.png", "gcp_storage_bucket_name")

if __name__ == "__main__":
    pytest.main()
