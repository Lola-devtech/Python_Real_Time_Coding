import boto3
from botocore.config import Config

# Define the region
my_config = Config(region_name='us-east-1')

# Get the service resource with the custom configuration
dynamodb = boto3.resource('dynamodb', config=my_config)

# Create the DynamoDB table
try:
    table = dynamodb.create_table(
        TableName='heydevops',
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'  # String
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'  # String
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists
    print("Creating table...")
    table.wait_until_exists()

    # Print out some data about the table
    print(f"Table '{table.table_name}' created successfully!")
    print(f"Item count: {table.item_count}")

except Exception as e:
    print(f"An error occurred: {e}")

