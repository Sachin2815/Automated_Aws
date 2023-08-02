import boto3

s3_client = boto3.client('s3')

response = s3_client.create_bucket(
    ACL='private',  # Use 'private' instead of 'enabled' for private ACL
    Bucket='vimal.lw13',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'  # Use the region code, not the region name
    }
)

print(response)
