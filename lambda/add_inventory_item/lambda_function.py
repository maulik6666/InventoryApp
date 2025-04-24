import boto3
import json
import uuid
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')


def lambda_handler(event, context):
    try:
        # Parse incoming request body
        if isinstance(event.get('body'), str):
            data = json.loads(event['body'])
        elif isinstance(event.get('body'), dict):
            data = event['body']
        else:
            data = event

        item = {
            'item_id': str(uuid.uuid4()),  # Matches Partition Key
            'location_id': Decimal(str(data['location_id'])),  # Matches Sort Key
            'name': data['name'],
            'description': data['description'],
            'qty': Decimal(str(data['qty'])),
            'price': Decimal(str(data['price']))
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
