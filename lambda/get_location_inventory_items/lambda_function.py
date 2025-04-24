import boto3
import json
from decimal import Decimal
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')


# Handles Decimal serialization
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj) if obj % 1 == 0 else float(obj)
        return super(DecimalEncoder, self).default(obj)


def lambda_handler(event, context):
    try:
        path_params = event.get('pathParameters', {})
        location_id = path_params.get('id')

        if not location_id:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing location_id in path'})
            }

        response = table.query(
            IndexName='LocationIndex',
            KeyConditionExpression=Key('location_id').eq(Decimal(location_id))
        )

        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'], cls=DecimalEncoder)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
