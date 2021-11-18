"""
python.exe e_gov_bestmove.py
"""

from pprint import pprint
import boto3
from botocore.exceptions import ClientError
from e_gov_scan_bestmove_table import scan_bestmove_table


if __name__ == '__main__':
    items = scan_bestmove_table()
    if items:
        print("Scan bestmove table succeeded:")
        pprint(items, sort_dicts=False)

        # items['bestmove']