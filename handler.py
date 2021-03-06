import json
from boto3 import resource
import os
import decimal
import uuid
import hashlib


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


def get_accession(event, context):
    table_name = os.environ['DYNAMODB_TABLE']
    field_name = os.environ['FIELD_NAME']
    dynamodb_resource = resource('dynamodb')
    table = dynamodb_resource.Table(table_name)

    response = table.update_item(
        Key={
            'id': 'accession'
        },
        UpdateExpression="set " + field_name + " = " + field_name + " + :incr",
        ExpressionAttributeValues={
            ':incr': decimal.Decimal(1)
        },
        ReturnValues="UPDATED_NEW"
    )

    body = {
        "accession": "HCA-" + str(response['Attributes'][field_name])
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def get_sha1(event, context):
    body = json.loads(event["body"])
    hash_result = hashlib.sha1(str(body).encode('utf-8')).hexdigest()
    print(hash_result)

    body = {
        "sha1": str(hash_result)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def get_uuid(event, context):
    body = {
        "uuid": str(uuid.uuid4())
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
