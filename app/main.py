import os
import boto3
from time import sleep


def main():
    s3 = boto3.client(
        's3',
        endpoint_url="http://minio:9000",
        aws_access_key_id=os.getenv("CLIENT_USERNAME"),
        aws_secret_access_key=os.getenv("CLIENT_PASSWORD")
    )
    for i in range(10000):
        if i == 1200:
            sleep(100)
        s3.upload_file('test.jpeg', os.getenv("BUCKET_NAME"), f'test-{i}.jpeg')

if __name__ == "__main__":
    main()