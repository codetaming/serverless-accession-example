import json


def get_accession(event, context):
    body = {
        "accession": "HCA-1"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
