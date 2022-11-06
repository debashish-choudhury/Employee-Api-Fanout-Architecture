import json
import boto3
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
# import requests


def lambda_handler(event, context):
    try:
        LOGGER.info(event)
        notification = "Here is the SNS notification for Lambda function tutorial."
        sns_client = boto3.client('sns')
        response = sns_client.publish(
            TargetArn="arn:aws:sns:ap-south-1:449845850442:MyFirstSNSTopic",
            Message=json.dumps({'default': event["body"]}),
            MessageStructure='json'
        )
    except Exception as e:
        LOGGER.info(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }

