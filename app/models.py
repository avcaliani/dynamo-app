from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class UserScore(BaseModel):
    value: float
    status: str


class User(BaseModel):
    document: str
    name: str
    enabled: bool = True
    birthdate: date
    score: UserScore
    updated_at: Optional[datetime] = datetime.utcnow()
    created_at: Optional[datetime] = datetime.utcnow()

    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S"),
            date: lambda v: v.strftime("%Y-%m-%d")
        }
