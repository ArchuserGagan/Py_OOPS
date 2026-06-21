#most simple type hints
## | this describe or
#there is other way to use optional like you can import optional from typing then age : optional[int]
def create_user(first_name:str,last_name:str, age: int | None =None) -> dict[str,str | int | None]: #[key,value] #for optional use use union like a pipe character
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"
    return {
        "first_name" : first_name,
        "last_name" : last_name,
        "email" : email,
        "age" : age,
    }


user1 = create_user("gagan", "singh", age=30)
user2 = create_user("john", "doe")
print(user1)