from pydantic import BaseModel
from typing import ClassVar


class User(BaseModel):
    userId: int
    name: str
    email: str
    
    