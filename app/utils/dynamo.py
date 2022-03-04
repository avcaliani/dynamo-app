import json
from decimal import Decimal
from os import environ
from typing import Union, Optional

import boto3
from boto3.resources.base import ServiceResource
from pydantic import BaseModel


class DynamoFacade:
    """DynamoDB Facade.

    DynamoDB Table
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#table
    """

    def __init__(self):
        self.conn = self.create_conn()

    @staticmethod
    def create_conn() -> ServiceResource:
        print("Creating DynamoDB connection...")
        return boto3.resource(
            "dynamodb",
            endpoint_url=environ.get("DYNAMO_ENDPOINT"),
            region_name=environ.get("AWS_REGION"),
            aws_access_key_id=environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=environ.get("AWS_SECRET_ACCESS_KEY")
        )

    @staticmethod
    def to_dict(data: BaseModel) -> dict:
        return json.loads(
            data.json(),
            parse_float=Decimal
        )

    def get(self, table: str, id_: Optional[str] = None, id_field: str = 'document') -> Union[dict, list, None]:
        table = self.conn.Table(table)
        if not id_:
            return table.scan().get("Items", [])
        return table.get_item(Key={id_field: id_}).get("Item", None)

    def create(self, table: str, data: BaseModel) -> dict:
        table = self.conn.Table(table)
        return table.put_item(Item=self.to_dict(data))

    def update(self, table: str, id_: str, data: BaseModel):
        raise RuntimeError("Not implemented!")

    def delete(self, table: str, id_: str):
        raise RuntimeError("Not implemented!")


db = DynamoFacade()
