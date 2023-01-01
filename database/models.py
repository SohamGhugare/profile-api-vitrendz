"""
This file contains all the models implemented in the DBMS system
"""
from sqlmodel import SQLModel, Field, create_engine, JSON, Column
from typing import Optional, List
from uuid import uuid4  
from datetime import datetime

# User Model - Contains all the user data
class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    guid: str = Field(nullable=False, default=str(uuid4()), unique=True)
    is_active: bool = Field(nullable=False, default=False)
    balance: float = Field(nullable=False, default=0.0)
    picture: str = Field(nullable=False, default="http://placehold.it/32x32")
    age: int = Field(nullable=False)
    eye_color: str = Field(nullable=False, default="unspecified")
    name: str = Field(nullable=False)  
    gender: str = Field(nullable=False, default="unspecified")    
    company: str = Field(nullable=False)  
    email: str = Field(nullable=False, unique=True)    
    phone: str = Field(nullable=False, default="unspecified")    
    address: str = Field(nullable=False, default="unspecified")    
    about: str = Field(nullable=True, default="unspecified")  
    registered: str = Field(nullable=False, default=str(datetime.utcnow()))  
    latitude: float = Field(nullable=False, default=-0.0)  
    longitude: float = Field(nullable=False, default=-0.0)  
    tags: List[str] = Field(sa_column=Column(JSON), default=[])
    friends: List[str] = Field(sa_column=Column(JSON), default=[])
    greeting: str = Field(nullable=False, default="unspecified")

# While creating new user, we only need these fields, the rest of them can be updated later
class UserCreate(SQLModel):
    name: str
    age: int
    company: str
    email: str

# Only these fields should be allowed to update
class UserUpdate(SQLModel):
    picture: Optional[str]
    age: Optional[int]
    eye_color: Optional[str] 
    name: Optional[str]
    gender: Optional[str]    
    company: Optional[str]
    email: Optional[str]
    phone: Optional[str]   
    address: Optional[str]    
    about: Optional[str] 
    latitude: Optional[float] 
    longitude: Optional[float]

def generate_schema():
    SQLModel.metadata.create_all(create_engine("sqlite:///data/clients.db"))

    

