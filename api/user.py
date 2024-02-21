import fastapi
from models.user_model import User

router = fastapi.APIRouter()

users = [
    {"userId": 1, "name": "dhananjay", "email": "dhananjay@example.com"},
    {"userId": 2, "name": "murli", "email": "murli@example.com"},
    {"userId": 3, "name": "leena", "email": "leena@example.com"}
]


@router.get("/users/")
def get_users():
    return users


@router.post("/users/")
def cerate_user(user: User):
    users.append(user)
    return f"{user.name} added successfully"
    
@router.put("/users/")
def update_user(user: User):
    for currUser in users:
        if(currUser["userId"] == user.userId):
           currUser["name"] = user.name
           currUser["email"] = user.email
           return f"{user.name} updated successfully"
    return "Error in updating the user"   
    
           
@router.delete("/users/{id}")
def delete_user(id: int):
    print(id)
    for curr in users:
        if(curr["userId"]== id): 
            users.remove(curr)
    
