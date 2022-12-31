"""
This file contains all the database operation functions
"""
from sqlmodel import create_engine, Session
from .models import User

class Database:
    def __init__(self) -> None:
        self.uri = "sqlite:///data/clients.db"

    @property
    def engine(self):
        return create_engine(self.uri, echo=True) #TODO: Turn off echo in production

    @property
    def session(self) -> Session:
        return Session(self.engine)
    
    ## <<----------------------------------------------------->>
    ## Database operations

    # Creating new user
    def create_user(self, user: User):
        with self.session as session:
            session.add(user)
            session.commit()
            return user.name

    ## <<----------------------------------------------------->>