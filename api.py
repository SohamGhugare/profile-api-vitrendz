"""
This file contains the main api code
"""
from fastapi import FastAPI, HTTPException
from uvicorn import run

from database.models import generate_schema, UserCreate, User
from database.parse_json import create_users
from database.db import Database

app = FastAPI()
db = Database()

## <<----------------------------------------------------->>
## CRUD Routes

# Fetching user from ID
@app.get("/clients/{id}")
async def get_user(id: int):
    user = db.fetch_user_by_id(id)
    # Do Stuff
    return {"data": f"Hello, {user.name}..!"}

# Creating new user
@app.post("/create-user")
async def create_user(user: UserCreate):
    try:
        user = db.create_user(user)
        # Do Stuff
        return {
            "response": 201,
            "data": f"Client {user.name} added successfully..!"
        }
    # Error handling for invalid email (handled in database/db.py)
    except HTTPException as e:
        return {
            "response": e.status_code,
            "detail": e.detail
        }

# Deleting an existing user
@app.delete("/clients/{id}")
async def delete_user(id: int):
    try:
        name = db.delete_user(id)
        return {
            "response": 202,
            "data": f"Client {name} deleted successfully..!"
        }
    # Error handling for invalid client id (handled in database/db.py)
    except HTTPException as e:
        return {
            "response": e.status_code,
            "detail": e.detail
        }

## <<----------------------------------------------------->>

if __name__ == "__main__":
    # Generating the database file and schema
    generate_schema()

    # Adding users from json to database
    # create_users()

    # Using uvicorn for creating an ASGI server
    run("api:app", reload=True)
