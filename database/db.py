"""
This file contains all the database operation functions
"""
from sqlmodel import create_engine, Session, select
from .models import User, UserCreate, UserUpdate
from fastapi import HTTPException

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
    def create_user(self, user: UserCreate):
        # Error handling for duplicate user
        if self.validate_user(user):
            raise HTTPException(status_code=409, detail="Client already exists.")
        else:
            if self.validate_email(user):
                with self.session as session:
                    db_user = User.from_orm(user)
                    session.add(db_user)
                    session.commit()
                    session.refresh(db_user)
                    return db_user
            else:
                # Error handling for invalid email
                raise HTTPException(status_code=400, detail="Email must contain company name.")

    # Fetching user
    def fetch_user_by_id(self, id: int):
        with self.session as session:
            user = session.get(User, id)
            if not user:
                # Error handling for invalid user id
                raise HTTPException(status_code=404, detail="Client not found.")
            return user

    # Deleting user
    def delete_user(self, id: int):
        with self.session as session:
            user = session.get(User, id)
            if not user:
                # Error handling for invalid user id
                raise HTTPException(status_code=404, detail="Client not found.")
            name = user.name
            session.delete(user)
            session.commit()
            return name

    # Updating user
    def update_user(self, id: int, user: UserUpdate):
        with self.session as session:
            user_db = session.get(User, id)
            if not user_db:
                # Error handling for invalid user id
                raise HTTPException(status_code=404, detail="Client not found.")
            user_data = user.dict(exclude_unset=True)
            for key, value in user_data.items():
                setattr(user_db, key, value)
            session.add(user_db)
            session.commit()
            session.refresh(user_db)
            return user_db

    ## <<----------------------------------------------------->>
    ## Utility functions

    # Validating email to contain company name
    def validate_email(self, user: UserCreate):
        return user.email.split("@")[1].split(".")[0] == user.company.lower()

    # Checking if duplicate user exists
    def validate_user(self, user: UserCreate):
        with self.session as session:
            user = session.exec(select(User).where(User.name==user.name)).first()
            return user