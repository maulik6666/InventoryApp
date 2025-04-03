import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    try:
        item_id = event['pathParameters']['id']
        table.delete_item(Key={'Item id': item_id})
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item deleted successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }