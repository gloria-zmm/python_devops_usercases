
import boto3

client = boto3.client('s3')

"""
response = client.create_bucket(

    Bucket='test-bucket-20252013'
  
)
response = client.list_buckets(
    MaxBuckets=123,
    BucketRegion='us-east-1'
)
bucket_lists = [bucket["Name"] for bucket in response["Buckets"]]

print(bucket_lists[0])

"""


response = client.delete_bucket(
    Bucket='test-bucket-20252013'
)
