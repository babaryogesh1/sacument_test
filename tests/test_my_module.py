import os
from my_module import process_directory, upload_to_s3, upload_to_gcs
import boto3
from google.cloud import storage
from unittest.mock import Mock, patch
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def test_upload_to_s3():   
    breakpoint() 
    s3_file = "test_directory/test_file.jpg"
    with patch("my_module.boto3.client") as mock_boto:
        s3_client = mock_boto.return_value
        upload_to_s3(s3_file, "sacumen")
        s3_client.upload_file.assert_called_once_with(s3_file, "sacumen","test_file.jpg")

def test_upload_to_gcs():
    storage_file = "test_file.pdf"
    with patch("my_module.storage") as mock_storage:
        storage_client = mock_storage.Client.from_service_account_json.return_value
        bucket = storage_client.bucket.return_value
        upload_to_gcs(storage_file, "rehlatimages")
        bucket.blob.assert_called_once_with(storage_file)
        bucket.blob.return_value.upload_from_filename.assert_called_once_with(storage_file)

def test_process_directory():
    with patch("my_module.upload_to_s3") as mock_upload_s3, patch("my_module.upload_to_gcs") as mock_upload_gcs:
        with patch("my_module.os.walk") as mock_walk:
            mock_walk.return_value = [
                (BASE_DIR + "/test/test_directory", [], ["test_file.jpg", "test_file.pdf", "file2.docx"])
            ]
            process_directory("test_directory", "sacumen", "rehlatimages", ["jpg"], ["pdf"])
            mock_upload_s3.assert_called_once_with(BASE_DIR + "/test/test_directory/test_file.jpg", "sacumen")
            mock_upload_gcs.assert_called_once_with(BASE_DIR + "/test/test_directory/test_file.pdf", "rehlatimages")

if __name__ == "__main__":
    pytest.main()
