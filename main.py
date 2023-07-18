import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List all S3 buckets
response = s3.list_buckets()

print("S3 Buckets:")
for bucket in response['Buckets']:
    print(f"- {bucket['Name']}")

# Create an EC2 client
ec2 = boto3.client('ec2')

# List all EC2 instances
response = ec2.describe_instances()

print("\nEC2 Instances:")
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"- {instance['InstanceId']}")

# Create an SNS client
sns = boto3.client('sns')

# Publish a message to an SNS topic
topic_arn = 'arn:aws:sns:us-east-1:123456789012:MyTopic'
message = 'Hello from Python!'
sns.publish(TopicArn=topic_arn, Message=message)

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Create a new item in a DynamoDB table
table_name = 'MyTable'
item = {
    'id': {'S': '1'},
    'name': {'S': 'John Doe'},
    'age': {'N': '30'}
}
dynamodb.put_item(TableName=table_name, Item=item)
