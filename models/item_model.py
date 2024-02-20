from pydantic import BaseModel

class Item(BaseModel):
    itemId = int
    name : str
    price: int
    quantity: int
    