import boto3
import json
from ulid import ULID

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        item = {
            'Item id': str(ULID()),
            'Item name': data['name'],
            'Item description': data['description'],
            'Item qty on hand': int(data['qty']),
            'Item price': float(data['price']),
            'Item location_id': int(data['location_id'])
        }
        table.put_item(Item=item)
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Item added successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }