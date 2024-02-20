# typing hint
# these are only for the editor and the programmer to work with the variable functions
# The function can take other types of parameters 
def full_name (firstname :str ,lastname :str |int ): # means the firstname can be str or None and the lastname can be str or int or None
                                                    # None is bydefault included
    return firstname +" " +lastname

x = full_name(firstname="Imran",lastname='rahman')

print(x)


def students (name: list[str,str,str,int,str]):
    return name
print(type (students([1,2,3,4,4])[0]))


# pydantic tutorial

from pydantic import BaseModel


class User(BaseModel):
    id : int = 1
    name: str = 'Rahman'
    friends: list[int] = []


data = {
    "id" : "2",
    "name" : "Imran",
    "Age" : 12


}

user = User(**data) # passing the data to User class

print(user)

from typing import Annotated


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:  # Annotates is used to paass a metadata that can be used by fastapi . It does not validate the data just gives some info
    return f"Hello {name}"

print(say_hello("Imran"))

