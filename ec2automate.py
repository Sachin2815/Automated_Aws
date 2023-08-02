import boto3
myec2= boto3.client("ec2")
myec2.run_instances(
    ImageId="ami-0ded8326293d201b",
    InstanceType="t2.micro",
    MaxCount=1,
    MinCount=1  
)
