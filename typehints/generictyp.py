import random
from typing import NewType, TypeVar  #Any for external dataset #typevar is for generics it is basically for ide  
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
T = TypeVar("T")
def random_choice(items:list[T]) -> T: # another way is just put [T] after func name 
    return random.choice(items)

user1 = create_user("gagan", "singh", age=30, fav_color=RGB((109,209,309)))
user2 = create_user("john", "doe", fav_color=RGB((100,200, 300)))
print(user1)
print(user2)

users = [user1, user2]
rando_user = random.choice(users)
print(rando_user)

emails = [user.email for user in users]
rando_email = random_choice(emails)
print(rando_email)