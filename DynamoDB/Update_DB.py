import boto3
from botocore.config import Config


my_config = Config(
    region_name='us-east-1'
)

dynamodb = boto3.resource('dynamodb', config=my_config)
table = dynamodb.Table('heydevops')
print(table.creation_date_time)

table.update_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
)
