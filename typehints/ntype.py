from typing import NewType

RGB = NewType("RGB",tuple[int,int,int])
HSL = NewType("HSL",tuple[int,int,int])


type  User = dict[str, str | int | RGB | None]


def create_user(
        first_name:str,
        last_name:str, 
        age: int | None = None,
        fav_color : RGB | None = None,
)  -> User: #this is type alias
    
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"
    return {
        "first_name" : first_name,
        "last_name" : last_name,
        "email" : email,
        "age" : age,
        "fav_color" : fav_color,

    }


user1 = create_user("gagan", "singh", age=30, fav_color=RGB((109,209,309)))
user2 = create_user("john", "doe", fav_color=RGB((100,200, 300)))
print(user1)