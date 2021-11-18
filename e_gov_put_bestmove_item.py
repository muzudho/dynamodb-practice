"""
python.exe e_gov_put_bestmove_item.py
"""

from pprint import pprint
import boto3


def put_bestmove(your_name, secret, bestmove, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Bestmove')
    response = table.put_item(
       Item={
            'yourName': your_name,
            'secret': secret,
            # 'S'（文字列型）の 'bestmove' 属性を追加
            'bestmove': bestmove,
        }
    )
    return response


if __name__ == '__main__':
    movie_resp = put_bestmove("Muzudho", "abc1234", "+7776FU")
    movie_resp = put_bestmove("Kifuwarane", "bebebebebeYOYOYOYOYO", "+5958OU")
    movie_resp = put_bestmove("Kifuwarazusa", "bababababa00", "+5756FU")
    movie_resp = put_bestmove("Kifuwarakaku", "kokokokoKOKOKOKO", "+7776FU")
    print("Put bestmove succeeded:")
    pprint(movie_resp, sort_dicts=False)
