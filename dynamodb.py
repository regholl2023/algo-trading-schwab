import boto3
import json
import os
from typing import Dict

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['PORTFOLIO_TABLE_NAME']
table = dynamodb.Table(table_name)

def store_portfolio(account_hash, portfolio):
    # Example: Put an item
    table.put_item(
       Item={
            'accountHash': account_hash,
            'cash': portfolio["cash"],
            'positions': portfolio["positions"]
        }
    )

def get_portfolio(account_hash):
    # Example: Get an item
    response = table.get_item(
        Key={
            'accountHash': account_hash,
        }
    )
    item = response.get('Item', None)

    if item:
        return {
            "cash": float(item["cash"]),
            "positions": float(item["positions"])
        }
    else:
        raise Exception("No portfolio found in dynamodb")
