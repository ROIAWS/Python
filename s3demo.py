import boto3
awskey = 'KEY'
awssecret = 'SECRET'

s3client = boto3.client(
    's3',
    aws_access_key_id = awskey,
    aws_secret_access_key = awssecret,
    region_name = 'us-east-1'
)

buckets = s3client.list_buckets()
print("Buckets: ")
for bucket in buckets['Buckets']:
    print(bucket.get("Name"))

bucketname = 'roifmrsy'
files = s3client.list_objects(Bucket=bucketname)
print("\n\nContents of Bucket " + bucketname)
for file in files.get("Contents"):
    print(file.get('Key'))

