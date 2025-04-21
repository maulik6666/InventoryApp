import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')


# Custom encoder to handle Decimal types in DynamoDB
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj) if obj % 1 == 0 else float(obj)
        return super(DecimalEncoder, self).default(obj)


def lambda_handler(event, context):
    try:
        item_id = event.get('item_id')
        location_id = event.get('location_id')

        if not item_id or not location_id:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing item_id or location_id'})
            }

        response = table.get_item(
            Key={
                'item_id': item_id,
                'location_id': Decimal(location_id)
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps(response.get('Item', {}), cls=DecimalEncoder)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
