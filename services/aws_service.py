import boto3
from datetime import datetime, timezone, timedelta

def get_buckets_info():
    s3_client = boto3.client('s3')
    buckets = s3_client.list_buckets()["Buckets"]
    new_buckets = []
    old_buckets = []
    current_date = datetime.now(timezone.utc).astimezone()
    for bucket in buckets:
        bucket_name= bucket["Name"]
        creation_date = bucket["CreationDate"]
        days_ago_90 = current_date - timedelta(days=90)
        if creation_date < days_ago_90:
            old_buckets.append(bucket_name)
        else:
            new_buckets.append(bucket_name)

    return {
        "total_buckets": len(buckets),
        "new_buckets": len(new_buckets),
        "old_buckets": len(old_buckets),
        "new_buckets_list": new_buckets,
        "old_buckets_list": old_buckets
    }

def get_aws_user_info():
    sts = boto3.client('sts')
    identity = sts.get_caller_identity()
    return {
        "UserId": identity['UserId'],
        "Account": identity['Account'],
        "Arn": identity['Arn']
    }

def get_ec2_info():
    ec2_client = boto3.client('ec2')
    instances = ec2_client.describe_instances()
    instance_info = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_info.append({
                "InstanceId": instance['InstanceId'],
                "State": instance['State']['Name'],
                "Public IP": instance.get('PublicIpAddress', 'N/A')
            })
    return {
        "total_instances": len(instance_info),
        "instances": instance_info
    }

