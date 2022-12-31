"""
This file contains all the models implemented in the DBMS system
"""
from sqlmodel import SQLModel, Field, create_engine, JSON, Column
from typing import Optional, List
from uuid import uuid4  

# User Model - Contains all the user data
class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    guid: str = Field(nullable=False, default=str(uuid4()), unique=True)
    is_active: bool = Field(nullable=False, default=False)
    balance: float = Field(nullable=False, default=0.0)
    picture: str = Field(nullable=False, default="http://placehold.it/32x32")
    age: int = Field(nullable=False)
    eye_color: str = Field(nullable=False)
    name: str = Field(nullable=False)  
    gender: str = Field(nullable=False)    
    company: str = Field(nullable=False)  
    email: str = Field(nullable=False, unique=True)    
    phone: str = Field(nullable=False)    
    address: str = Field(nullable=False)    
    about: str = Field(nullable=True)  
    registered: str = Field(nullable=False)  
    latitude: float = Field(nullable=False)  
    longitude: float = Field(nullable=False)  
    tags: List[str] = Field(sa_column=Column(JSON))
    friends: List[str] = Field(sa_column=Column(JSON))
    greeting: str = Field(nullable=False)


def generate_schema():
    SQLModel.metadata.create_all(create_engine("sqlite:///data/clients.db"))

    

