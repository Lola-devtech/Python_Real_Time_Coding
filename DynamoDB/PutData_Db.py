import boto3
from botocore.config import Config


my_config = Config(
    region_name='us-east-1'
)

dynamodb = boto3.resource('dynamodb', config=my_config)
table = dynamodb.Table('heydevops')
print(table.creation_date_time)
table.put_item(
   Item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)
response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print(item)
