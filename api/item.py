import fastapi
from models.item_model import Item


items = [
    {"itemId": 1, "name": "Golden Watch", "price": 1000, "quantity": 10},
    {"itemId": 2, "name": "Diamond Ring", "price": 5000, "quantity": 5},
    {"itemId": 3, "name": "Platinum Necklace", "price": 3000, "quantity": 7},
    {"itemId": 4, "name": "Emerald Earrings", "price": 2500, "quantity": 8},
    {"itemId": 5, "name": "Ruby Bracelet", "price": 1500, "quantity": 12},
    {"itemId": 6, "name": "Sapphire Pendant", "price": 3500, "quantity": 6}
]

router = fastapi.APIRouter()

@router.get("/items")
def getItems():
    return items

@router.post("/items/buy/{id}")
def buyItem(id: int):
    for currItem in items:
        if(currItem["itemId"]==id):
            currItem["quantity"]-=1
            return f"{currItem["name"]} is bought successfully"
    return "Sorry this item is out of stock currently, come back later"

@router.get("/items/price/{id}")
def getPrice(id: int):
    for currItem in items:
        if(currItem["itemId"]==id):
            return f"Price for {currItem["name"]} is Rs{currItem["price"]}"
        
    return "Sorry, this item is not available"