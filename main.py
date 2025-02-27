from fastapi import FastAPI
from pydantic import BaseModel
import boto3

dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url="http://172.19.0.2:8000",
    region_name="us-east-1",
    aws_access_key_id="key",
    aws_secret_access_key="key",
)

tables = list(dynamodb.tables.all())
if "User" not in [table.name for table in tables]:
    table = dynamodb.create_table(
        TableName="User",
        KeySchema=[{"AttributeName": "name", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "name", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 4, "WriteCapacityUnits": 4},
    )
    table.wait_until_exists()


app = FastAPI()


class User(BaseModel):
    name: str
    phone: str


@app.post("/user")
async def create_user(user: User):
    table = dynamodb.Table("User")
    table.put_item(Item=user.model_dump())


@app.get("/users")
async def scan_users():
    table = dynamodb.Table("User")
    response = table.scan()
    return response["Items"]
