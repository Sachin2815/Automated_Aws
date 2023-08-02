import boto3
def get_running_instance_count():
    try:
        
        ec2_client = boto3.client('ec2')
        response = ec2_client.describe_instances()
        running_instance_count = 0
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                if instance['State']['Name'] == 'running':
                    running_instance_count += 1
        return running_instance_count

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

running_instances = get_running_instance_count()
if running_instances is not None:
    print(f"Number of running instances: {running_instances}")
