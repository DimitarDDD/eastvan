from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

class Book(BaseModel):
    title: str 
    description: str
    rating: int
    author_id: int

    class Config:
        orm_mode = True

class Author(BaseModel):
    name:str
    age:int

    class Config:
        orm_mode = True