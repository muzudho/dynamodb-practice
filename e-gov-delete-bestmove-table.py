"""
python.exe e-gov-delete-bestmove-table.py
"""

import boto3

def delete_bestmove_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Bestmove')
    table.delete()


if __name__ == '__main__':
    delete_bestmove_table()
    print("Bestmove table deleted.")