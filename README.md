# sacument_test
Please follow the below step the run the program
1) Install the requirment.txt file  
        #pip install -r requirment.txt
2) Update the the bucket_name of GCP and s3( source_directory = "source_directory name"
        aws_s3_bucket = "xxxxx"
        gcs_bucket = "xxxxxx")
3)Update aws s3_file_extensions and GCp file extension

4)Update YOUR_ACCESS_KEY and YOUR_SECRET_KEY in "upload_to_s3" and "test_upload_to_s3" in python and test file  on line
      s3 = boto3.client('s3',aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_KEY')

5) update GCP credentional json file in upload_to_gcs and test_upload_to_gcs in python and test file function
         storage_client = storage.Client.from_service_account_json('credentional_file.json')

6) transfer the file to s3 and GCP run the command
        #python my_module.py

7)to run the test cases run the command
        #pytest

8)you can run your tests with coverage
        #coverage run -m pytest

9)And generate a coverage report:
        #coverage report -m


        
