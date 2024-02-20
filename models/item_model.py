from pydantic import BaseModel

class Item(BaseModel):
    itemId = int
    name : str
    quantity: int
    