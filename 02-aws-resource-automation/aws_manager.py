import boto3
import os
import sys
from botocore.exceptions import ClientError


# ============================================================
# AWS CONFIGURATION
# ============================================================

REGION = "ap-south-1"

# Your existing Project 2 bucket
DEFAULT_BUCKET = "static-portfolio-2026"


# ============================================================
# AWS CLIENTS
# ============================================================

s3 = boto3.client(
    "s3",
    region_name=REGION
)

ec2 = boto3.client(
    "ec2",
    region_name=REGION
)

ssm = boto3.client(
    "ssm",
    region_name=REGION
)


# ============================================================
# 1. CREATE S3 BUCKET
# ============================================================

def create_s3_bucket():

    print("\n========== CREATE S3 BUCKET ==========")

    bucket_name = input(
        "Enter new S3 bucket name: "
    ).strip()

    if not bucket_name:
        print("❌ Bucket name cannot be empty.")
        return

    try:

        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                "LocationConstraint": REGION
            }
        )

        print("\n✅ S3 bucket created successfully.")
        print("Bucket:", bucket_name)
        print("Region:", REGION)

    except ClientError as e:

        print(
            "\n❌ Bucket creation failed:"
        )

        print(
            e.response["Error"]["Message"]
        )


# ============================================================
# 2. LIST S3 BUCKETS
# ============================================================

def list_s3_buckets():

    print("\n========== S3 BUCKETS ==========")

    try:

        response = s3.list_buckets()

        buckets = response.get(
            "Buckets",
            []
        )

        if not buckets:

            print("No S3 buckets found.")

            return

        for bucket in buckets:

            print(
                "•",
                bucket["Name"]
            )

    except ClientError as e:

        print(
            "\n❌ Unable to list buckets:"
        )

        print(
            e.response["Error"]["Message"]
        )


# ============================================================
# 3. UPLOAD FILE TO S3
# ============================================================

def upload_file_to_s3():

    print("\n========== UPLOAD FILE TO S3 ==========")

    file_path = input(
        "Enter file path: "
    ).strip()

    if not os.path.isfile(file_path):

        print(
            "\n❌ File not found."
        )

        print(
            "Current folder:"
        )

        print(
            os.getcwd()
        )

        return

    bucket_name = input(
        f"Enter S3 bucket name "
        f"[Press Enter for {DEFAULT_BUCKET}]: "
    ).strip()

    if not bucket_name:

        bucket_name = DEFAULT_BUCKET

    file_name = os.path.basename(
        file_path
    )

    try:

        print(
            f"\nUploading {file_name}..."
        )

        s3.upload_file(
            file_path,
            bucket_name,
            file_name
        )

        print(
            "\n✅ File uploaded successfully."
        )

        print(
            "File:",
            file_name
        )

        print(
            "Bucket:",
            bucket_name
        )

    except ClientError as e:

        print(
            "\n❌ Upload failed:"
        )

        print(
            e.response["Error"]["Message"]
        )


# ============================================================
# 4. LIST EC2 INSTANCES
# ============================================================

def list_ec2_instances():

    print("\n========== EC2 INSTANCES ==========")

    try:

        response = ec2.describe_instances()

        found = False

        for reservation in response[
            "Reservations"
        ]:

            for instance in reservation[
                "Instances"
            ]:

                found = True

                instance_id = instance[
                    "InstanceId"
                ]

                instance_type = instance[
                    "InstanceType"
                ]

                state = instance[
                    "State"
                ][
                    "Name"
                ]

                print(
                    f"ID: {instance_id}"
                )

                print(
                    f"Type: {instance_type}"
                )

                print(
                    f"State: {state}"
                )

                print("-" * 40)

        if not found:

            print(
                "No EC2 instances found."
            )

    except ClientError as e:

        print(
            "\n❌ Unable to list EC2 instances:"
        )

        print(
            e.response["Error"]["Message"]
        )


# ============================================================
# 5. GET LATEST AMAZON LINUX 2023 AMI
# ============================================================

def get_latest_amazon_linux_ami():

    parameter_name = (
        "/aws/service/ami-amazon-linux-latest/"
        "al2023-ami-kernel-default-x86_64"
    )

    try:

        response = ssm.get_parameter(
            Name=parameter_name
        )

        ami_id = response[
            "Parameter"
        ][
            "Value"
        ]

        return ami_id

    except ClientError as e:

        print(
            "\n❌ Could not find Amazon Linux 2023 AMI:"
        )

        print(
            e.response["Error"]["Message"]
        )

        return None


# ============================================================
# 6. GET DEFAULT SUBNET
# ============================================================

def get_default_subnet():

    try:

        response = ec2.describe_subnets(
            Filters=[
                {
                    "Name": "default-for-az",
                    "Values": ["true"]
                }
            ]
        )

        subnets = response.get(
            "Subnets",
            []
        )

        if not subnets:

            return None

        return subnets[0][
            "SubnetId"
        ]

    except ClientError:

        return None


# ============================================================
# 7. GET DEFAULT SECURITY GROUP
# ============================================================

def get_default_security_group():

    try:

        response = ec2.describe_security_groups(
            Filters=[
                {
                    "Name": "group-name",
                    "Values": ["default"]
                }
            ]
        )

        groups = response.get(
            "SecurityGroups",
            []
        )

        if not groups:

            return None

        return groups[0][
            "GroupId"
        ]

    except ClientError:

        return None


# ============================================================
# 8. LAUNCH EC2 INSTANCE
# ============================================================

def launch_ec2_instance():

    print("\n========== LAUNCH EC2 INSTANCE ==========")

    try:

        # ----------------------------------------------------
        # Automatically find Amazon Linux 2023 AMI
        # ----------------------------------------------------

        print(
            "\nFinding latest Amazon Linux 2023 AMI..."
        )

        ami_id = get_latest_amazon_linux_ami()

        if not ami_id:

            return

        print(
            "✅ AMI found:"
        )

        print(
            ami_id
        )

        # ----------------------------------------------------
        # Find default subnet
        # ----------------------------------------------------

        print(
            "\nFinding default subnet..."
        )

        subnet_id = get_default_subnet()

        if not subnet_id:

            print(
                "❌ No default subnet found."
            )

            print(
                "Please make sure your VPC has a default subnet."
            )

            return

        print(
            "✅ Subnet:",
            subnet_id
        )

        # ----------------------------------------------------
        # Find default security group
        # ----------------------------------------------------

        print(
            "\nFinding default security group..."
        )

        security_group_id = (
            get_default_security_group()
        )

        if not security_group_id:

            print(
                "❌ Default security group not found."
            )

            return

        print(
            "✅ Security Group:",
            security_group_id
        )

        # ----------------------------------------------------
        # Confirm before creating EC2
        # ----------------------------------------------------

        print(
            "\n----------------------------------------"
        )

        print(
            "EC2 INSTANCE DETAILS"
        )

        print(
            "Region       :",
            REGION
        )

        print(
            "AMI          :",
            ami_id
        )

        print(
            "Instance Type: t2.micro"
        )

        print(
            "Count        : 1"
        )

        print(
            "----------------------------------------"
        )

        confirmation = input(
            "\nType YES to launch the instance: "
        ).strip()

        if confirmation != "YES":

            print(
                "\n❌ Launch cancelled."
            )

            return

        # ----------------------------------------------------
        # Launch EC2
        # ----------------------------------------------------

        print(
            "\nLaunching EC2 instance..."
        )

        response = ec2.run_instances(

            ImageId=ami_id,

            InstanceType="t2.micro",

            MinCount=1,

            MaxCount=1,

            SubnetId=subnet_id,

            SecurityGroupIds=[
                security_group_id
            ],

            TagSpecifications=[
                {
                    "ResourceType": "instance",

                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "AWS-Automation-Test"
                        }
                    ]
                }
            ]
        )

        instance_id = response[
            "Instances"
        ][0][
            "InstanceId"
        ]

        print(
            "\n========================================"
        )

        print(
            "✅ EC2 INSTANCE LAUNCHED"
        )

        print(
            "========================================"
        )

        print(
            "Instance ID :",
            instance_id
        )

        print(
            "AMI ID      :",
            ami_id
        )

        print(
            "Type        : t2.micro"
        )

        print(
            "Region      :",
            REGION
        )

        print(
            "Status      : pending"
        )

        print(
            "========================================"
        )

    except ClientError as e:

        print(
            "\n❌ EC2 launch failed:"
        )

        print(
            e.response["Error"]["Message"]
        )

    except Exception as e:

        print(
            "\n❌ Unexpected error:"
        )

        print(
            str(e)
        )


# ============================================================
# 9. STOP EC2 INSTANCE
# ============================================================

def stop_ec2_instance():

    print("\n========== STOP EC2 INSTANCE ==========")

    instance_id = input(
        "Enter EC2 Instance ID: "
    ).strip()

    if not instance_id:

        print(
            "❌ Instance ID cannot be empty."
        )

        return

    try:

        response = ec2.describe_instances(
            InstanceIds=[
                instance_id
            ]
        )

        instance = response[
            "Reservations"
        ][0][
            "Instances"
        ][0]

        state = instance[
            "State"
        ][
            "Name"
        ]

        print(
            "\nCurrent state:",
            state
        )

        if state == "stopped":

            print(
                "ℹ️ Instance is already stopped."
            )

            return

        if state == "terminated":

            print(
                "ℹ️ Instance is already terminated."
            )

            return

        if state == "stopping":

            print(
                "ℹ️ Instance is already stopping."
            )

            return

        confirmation = input(
            "\nType YES to stop this instance: "
        ).strip()

        if confirmation != "YES":

            print(
                "\n❌ Stop operation cancelled."
            )

            return

        ec2.stop_instances(
            InstanceIds=[
                instance_id
            ]
        )

        print(
            "\n✅ Stop request sent successfully."
        )

        print(
            "Instance:",
            instance_id
        )

    except ClientError as e:

        print(
            "\n❌ Stop failed:"
        )

        print(
            e.response["Error"]["Message"]
        )


# ============================================================
# 10. TERMINATE EC2 INSTANCE
# ============================================================

def terminate_ec2_instance():

    print(
        "\n========== TERMINATE EC2 INSTANCE =========="
    )

    instance_id = input(
        "Enter EC2 Instance ID: "
    ).strip()

    if not instance_id:

        print(
            "❌ Instance ID cannot be empty."
        )

        return

    try:

        response = ec2.describe_instances(
            InstanceIds=[
                instance_id
            ]
        )

        instance = response[
            "Reservations"
        ][0][
            "Instances"
        ][0]

        state = instance[
            "State"
        ][
            "Name"
        ]

        print(
            "\nCurrent state:",
            state
        )

        if state == "terminated":

            print(
                "ℹ️ Instance is already terminated."
            )

            return

        print(
            "\n⚠️ WARNING"
        )

        print(
            "Terminating an EC2 instance is destructive."
        )

        confirmation = input(
            "\nType TERMINATE to continue: "
        ).strip()

        if confirmation != "TERMINATE":

            print(
                "\n❌ Termination cancelled."
            )

            return

        ec2.terminate_instances(
            InstanceIds=[
                instance_id
            ]
        )

        print(
            "\n✅ Termination request sent."
        )

        print(
            "Instance:",
            instance_id
        )

    except ClientError as e:

        print(
            "\n❌ Termination failed:"
        )

        print(
            e.response["Error"]["Message"]
        )


# ============================================================
# 11. MAIN MENU
# ============================================================

def show_menu():

    while True:

        print("\n")

        print(
            "=" * 55
        )

        print(
            "              AWS RESOURCE MANAGER"
        )

        print(
            "=" * 55
        )

        print(
            "\nS3 OPERATIONS"
        )

        print(
            "1. Create S3 Bucket"
        )

        print(
            "2. List S3 Buckets"
        )

        print(
            "3. Upload File to S3"
        )

        print(
            "\nEC2 OPERATIONS"
        )

        print(
            "4. List EC2 Instances"
        )

        print(
            "5. Launch EC2 Instance"
        )

        print(
            "6. Stop EC2 Instance"
        )

        print(
            "7. Terminate EC2 Instance"
        )

        print(
            "\n8. Exit"
        )

        print(
            "=" * 55
        )

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            create_s3_bucket()

        elif choice == "2":

            list_s3_buckets()

        elif choice == "3":

            upload_file_to_s3()

        elif choice == "4":

            list_ec2_instances()

        elif choice == "5":

            launch_ec2_instance()

        elif choice == "6":

            stop_ec2_instance()

        elif choice == "7":

            terminate_ec2_instance()

        elif choice == "8":

            print(
                "\nThank you for using AWS Resource Manager."
            )

            sys.exit(0)

        else:

            print(
                "\n❌ Invalid choice."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    show_menu()