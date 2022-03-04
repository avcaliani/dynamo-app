from fastapi import APIRouter, HTTPException

from app.models import User
from app.utils import db

DYNAMO_TABLE = "users"

user = APIRouter(prefix="/users", tags=["users"])


@user.get("")
async def find():
    return db.get(table=DYNAMO_TABLE)


@user.get("/{document}")
async def find_one(document: str):
    return db.get(table=DYNAMO_TABLE, id_=document)


@user.post("", status_code=201)
async def create(data: User):
    return db.create(table=DYNAMO_TABLE, data=data)


@user.put("/{document}")
async def update(document: str, data: User):
    return db.update(table=DYNAMO_TABLE, id_=document, data=data)


@user.delete("/{document}")
async def delete(document: str):
    try:
        return db.delete(table=DYNAMO_TABLE, id_=document)
    except RuntimeError as ex:
        raise HTTPException(status_code=404, detail=str(ex))
