import boto3

# Create EC2 client
ec2 = boto3.client("ec2")


def lambda_handler(event, context):

    print("===== AWS COST OPTIMIZER STARTED =====")

    # Find running EC2 instances
    response = ec2.describe_instances(
        Filters=[
            {
                "Name": "instance-state-name",
                "Values": ["running"]
            }
        ]
    )

    instance_ids = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_ids.append(instance["InstanceId"])

    # If no running instances are found
    if not instance_ids:
        print("No running EC2 instances found.")

        return {
            "statusCode": 200,
            "body": "No running EC2 instances found."
        }

    # Display running instances
    print("Running EC2 instances:")
    for instance_id in instance_ids:
        print(instance_id)

    # Stop running instances
    ec2.stop_instances(
        InstanceIds=instance_ids
    )

    print("EC2 instances stopped successfully.")

    return {
        "statusCode": 200,
        "body": f"Stopped EC2 instances: {instance_ids}"
    }
