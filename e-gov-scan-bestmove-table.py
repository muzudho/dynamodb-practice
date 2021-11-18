"""
python.exe e-gov-scan-bestmove-table.py
"""

from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def scan_bestmove_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Bestmove')

    try:
        response = table.scan()
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Items']


if __name__ == '__main__':
    items = scan_bestmove_table()
    if items:
        print("Scan bestmove table succeeded:")
        pprint(items, sort_dicts=False)
