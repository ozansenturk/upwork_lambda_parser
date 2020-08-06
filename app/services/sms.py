import boto3
import os


# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id= os.getenv("access_key"),
    aws_secret_access_key=os.getenv("access_secret"),
    region_name="us-east-1"
)
def send_sms(content):
    # Send your sms message.
    # client.publish(
    #     PhoneNumber=os.getenv("mobile_number"),
    #     Message=content
    # )
    client.publish(

        Message=content,TopicArn=os.getenv("topic_arn")
    )