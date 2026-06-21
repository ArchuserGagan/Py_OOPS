from typing import NewType
from dataclasses import dataclass

RGB = NewType("RGB",tuple[int,int,int])
HSL = NewType("HSL",tuple[int,int,int])

@dataclass
class User:
    first_name :str
    last_name : str
    email : str
    age : int | None = None  # we can assign default values now
    fav_color : RGB | None = None



# dataclass doesnt verify at runtime


def create_user(
        first_name:str,
        last_name:str, 
        age: int | None = None,
        fav_color : RGB | None = None,
)  -> User: #this is type alias
    
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"
    return User(
        first_name= first_name,
        last_name=last_name,
        email=email,
        fav_color=fav_color,
    )

user1 = create_user("gagan", "singh", age=30, fav_color=RGB((109,209,309)))
user2 = create_user("john", "doe", fav_color=RGB((100,200, 300)))
print(user1)

