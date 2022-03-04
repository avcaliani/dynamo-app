from os import environ

import boto3
from fire import Fire


def init() -> None:
    """This method will initialize the DynamoDB."""
    print('🦖 Connecting to Dynamo DB...')
    ddb = boto3.resource(
        'dynamodb',
        endpoint_url=environ.get('DYNAMO_ENDPOINT'),
        region_name=environ.get('AWS_REGION'),
        aws_access_key_id=environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=environ.get('AWS_SECRET_ACCESS_KEY')
    )
    print('📊 Creating tables...')
    ddb.create_table(
        TableName='users',
        AttributeDefinitions=[
            {'AttributeName': 'document', 'AttributeType': 'S'}
        ],
        KeySchema=[
            {'AttributeName': 'document', 'KeyType': 'HASH'}
        ],
        # TODO: Understand it better
        ProvisionedThroughput={'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10}
    )
    print('💚 Finished')


if __name__ == "__main__":
    Fire()
