import json
from botocore.vendored import requests

def lambda_handler(event, context):
    
    response = "Hello World!"

    return {
        "statusCode": 200,
        "body": response
    }

