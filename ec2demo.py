import boto3
awskey = 'KEY'
awssecret = 'SECRET'

ec2client = boto3.client(
    'ec2',
    aws_access_key_id = awskey,
    aws_secret_access_key = awssecret,
    region_name = 'us-east-1'
)

instances = ec2client.describe_instances()
reservations = instances.get("Reservations")
for reservation in reservations:
    instancesjson = reservation.get("Instances") 
    print("VM(s) Found:")
    for instance in instancesjson:
        print(instance.get("ImageId") + " - " + str(instance.get("State")))
