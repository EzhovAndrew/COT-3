import os
import boto3


def main():
    # Create an S3 client
    s3 = boto3.client(
        's3',
        endpoint_url="http://minio:9000",
        aws_access_key_id=os.getenv("CLIENT_USERNAME"),
        aws_secret_access_key=os.getenv("CLIENT_PASSWORD")
    )
    for i in range(10000):
        # Upload a file to S3
        s3.upload_file('test.jpeg', os.getenv("BUCKET_NAME"), f'test-{i}.jpeg')

if __name__ == "__main__":
    main()